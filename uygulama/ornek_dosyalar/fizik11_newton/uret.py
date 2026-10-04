"""sinav.py'den sınav PDF'i, rubrik PDF'i ve soru başına PNG üretir (Google Chrome başsız modla).

Kullanım (bu klasörde):  python3 uret.py
Puanlar puanlar.json'dan gelir (sistemin eşleme kurallarıyla hesaplanır, backend klasöründe üretilir).
"""

import html
import json
import subprocess
from pathlib import Path

from PIL import Image, ImageChops

from sinav import ALT_BASLIK, BASLIK, SORULAR, YONERGE

KLASOR = Path(__file__).resolve().parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PUAN = json.loads((KLASOR / "puanlar.json").read_text(encoding="utf-8"))

STIL = """
body { font-family: -apple-system, Helvetica, Arial, sans-serif; color: #1d2433; margin: 0; padding: 28px 36px; font-size: 15px; line-height: 1.5; }
h1 { font-size: 20px; margin: 0; } .alt { color: #667085; margin: 2px 0 14px; }
.ust { display: flex; justify-content: space-between; border-bottom: 2px solid #1f3a5f; padding-bottom: 10px; margin-bottom: 12px; }
.bilgi { font-size: 13px; color: #344054; line-height: 1.9; }
.yonerge { background: #f2f4f7; border-radius: 6px; padding: 8px 12px; font-size: 13px; margin-bottom: 18px; }
.soru { margin-bottom: 22px; page-break-inside: avoid; }
.soru h2 { font-size: 16px; margin: 0 0 6px; color: #1f3a5f; }
.soru p { margin: 4px 0; }
.sekil { margin: 8px 0 4px 10px; }
.bosluk { height: 150px; border: 1px dashed #d0d5dd; border-radius: 6px; margin-top: 8px; }
table { border-collapse: collapse; width: 100%; font-size: 13px; margin: 6px 0 4px; }
th, td { border: 1px solid #d0d5dd; padding: 5px 7px; text-align: left; vertical-align: top; }
th { background: #f2f4f7; }
td.p { text-align: right; white-space: nowrap; }
.cozum { background: #ecfdf3; border-left: 4px solid #12b76a; padding: 6px 10px; font-size: 13px; margin: 6px 0; }
.not { font-size: 12px; color: #667085; }
code { font-size: 12px; }
"""


def _paragraflar(metin: str) -> str:
    return "".join(f"<p>{html.escape(x)}</p>" for x in metin.split("\n"))


def _soru_html(q: dict, bosluk: bool) -> str:
    sekil = f'<div class="sekil">{q["sekil"]}</div>' if q["sekil"] else ""
    puan = PUAN[str(q["no"])]["zorluk"]
    return (f'<div class="soru"><h2>{q["no"]}. Soru <small style="color:#667085;font-weight:normal">({puan:.2f} puan)</small></h2>'
            f'{_paragraflar(q["metin"])}{sekil}{"<div class=bosluk></div>" if bosluk else ""}</div>')


def _sayfa(govde: str, baslik: str) -> str:
    return f'<!doctype html><html lang="tr"><head><meta charset="utf-8"><title>{baslik}</title><style>{STIL}</style></head><body>{govde}</body></html>'


def _pdf(ad: str, icerik: str):
    gecici = KLASOR / f"_{ad}.html"
    gecici.write_text(icerik, encoding="utf-8")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={KLASOR / ad}.pdf",
                    gecici.as_uri()], check=True, capture_output=True)
    gecici.unlink()


def _png(ad: str, icerik: str):
    gecici = KLASOR / f"_{ad}.html"
    gecici.write_text(icerik, encoding="utf-8")
    hedef = KLASOR / f"{ad}.png"
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=2",
                    "--window-size=820,1200", f"--screenshot={hedef}", gecici.as_uri()], check=True, capture_output=True)
    gecici.unlink()
    g = Image.open(hedef).convert("RGB")  # alttaki boşluğu kırp
    kutu = ImageChops.difference(g, Image.new("RGB", g.size, (255, 255, 255))).getbbox()
    if kutu:
        g.crop((0, 0, g.width, min(g.height, kutu[3] + 40))).save(hedef)


def main():
    toplam = sum(PUAN[str(q["no"])]["zorluk"] for q in SORULAR)
    ust = (f'<div class="ust"><div><h1>{BASLIK}</h1><div class="alt">{ALT_BASLIK} · Toplam {toplam:.2f} puan</div></div>'
           f'<div class="bilgi">Ad Soyad: ______________________<br>Sınıf / No: ____________</div></div>'
           f'<div class="yonerge">{html.escape(YONERGE)}</div>')
    _pdf("sinav", _sayfa(ust + "".join(_soru_html(q, True) for q in SORULAR), "Sınav"))

    parcalar = [f'<div class="ust"><div><h1>Rubrik · {BASLIK}</h1><div class="alt">Öğretmen için · toplam {toplam:.2f} puan</div></div></div>',
                '<p class="not">Her rubrik adımı tek bir mikro kazanıma (MK) eşlidir. Adım için karar: <b>Biliyor</b> (doğru yaptı, '
                'adım puanını alır), <b>Bilmiyor</b> (denedi, yanlış), <b>Ölçülemedi</b> (boş ya da o adıma gelmedi). Puanlar '
                'EVALORA kurallarıyla hesaplandı: soru puanı = sorunun en üst MK\'lerinin zorluklarının (Z) toplamı; adım payları '
                'MK ağırlığına (v²) göre.</p>']
    for q in SORULAR:
        p = PUAN[str(q["no"])]
        satirlar = "".join(
            f'<tr><td>{i}</td><td>{html.escape(a)}</td><td><code>{k}</code><br><span class="not">{html.escape(p["ifade"][k])}</span></td>'
            f'<td class="p">{p["puan"][i - 1]:.2f}</td></tr>' for i, (a, k) in enumerate(q["adimlar"], 1))
        parcalar.append(
            f'<div class="soru"><h2>{q["no"]}. Soru: {html.escape(q["baslik"])} <small style="color:#667085;font-weight:normal">'
            f'({p["zorluk"]:.2f} puan · soru MK\'leri: {", ".join(p["mkler"])})</small></h2>'
            f'<p><b>Doğru cevap:</b> {html.escape(q["dogru_cevap"])}</p><div class="cozum"><b>Çözüm:</b> {html.escape(q["cozum"])}</div>'
            f'<table><tr><th>#</th><th>Rubrik adımı (öğrenci ne yapmalı)</th><th>MK</th><th>Puan</th></tr>{satirlar}</table></div>')
    _pdf("rubrik", _sayfa("".join(parcalar), "Rubrik"))

    for q in SORULAR:
        _png(f"soru{q['no']}", _sayfa(_soru_html(q, False).replace(f' <small style="color:#667085;font-weight:normal">({PUAN[str(q["no"])]["zorluk"]:.2f} puan)</small>', ""), "Soru"))
    print("tamam:", ", ".join(sorted(x.name for x in KLASOR.glob("*.p*") if x.suffix in (".pdf", ".png"))))


if __name__ == "__main__":
    main()
