"""Bir teslimin dışarıda (ör. Claude ile sohbette) yapılmış değerlendirmesini 'sistem önerisi' olarak aktarır.

Dosya biçimi: uygulama/ice_aktarma/degerlendirmeler/*.json
  {"teslim_id": 2, "sorular": {"<soru_id>": {"okunan": "...", "kirpik": "dosya.png",
                                             "kararlar": {"<rubrik_adim_id>": ["biliyor", "gerekçe"]}}}}
'kirpik': öğrencinin tüm kâğıdından o sorunun çözümünün kırpılmış görüntüsü (JSON'un yanındaki klasörde); cevaba
'kagittan' kaynaklı dosya olarak eklenir ki öğretmen el yazısını okunan metinle karşılaştırabilsin.
Kararlar kaynak='sistem' olarak yazılır; öğretmen değerlendirme ekranında görür, değiştirir ve onaylar.
Öğretmenin daha önce verdiği kararların üstüne yazılmaz. 'okunan' metin, cevabın metni boşsa oraya konur.

Veritabanı kimliklerini bilmeden yazmak için (bulutta Claude ile): "soru_seti" verilir, sorular o setin sorular.json'undaki
"no" ile, adımlar rubrikteki sırasıyla (1'den) anılır; aktarırken teslimin sınavındaki aynı metinli soruya çevrilir:
  {"teslim_id": 12, "soru_seti": "mat6_bolunebilme", "sorular": {"6": {"okunan": "...", "kararlar": {"1": ["biliyor", "..."]}}}}
"soru_seti" varken "teslim_id" yazılmayabilir: o setin sınavında gönderilmiş ve henüz hiç değerlendirilmemiş tek bir teslim
varsa o alınır; birden çoksa teslim_id istenir.

Kullanım (backend klasöründe):  python -m app.degerlendirme_aktar ../ice_aktarma/degerlendirmeler/teslim2_deneme_ogrenci.json
"""

import json
import sys

from .degerlendirme import ADIM_DURUMLARI_GECERLI, ogretmen as karar_yaz
from pathlib import Path

from .modeller import Cevap, CevapDosya, Soru, Teslim
from .routers.sorular import _gorsel_kaydet
from sqlalchemy import select

from .vt import Oturum


def aktar(yol: str) -> list[str]:
    v = json.load(open(yol, encoding="utf-8"))
    rapor = []
    with Oturum() as vt:
        t = vt.get(Teslim, v["teslim_id"]) if v.get("teslim_id") else _tek_bekleyen_teslim(vt, Path(yol).parent.parent / v["soru_seti"])
        if not t:
            raise SystemExit("Teslim bulunamadı.")
        sinav_sorulari = {x.soru_id for x in t.atama.sinav.sorular}
        if v.get("soru_seti"):
            v = _kimliklere_cevir(v, Path(yol).parent.parent / v["soru_seti"], [x.soru for x in t.atama.sinav.sorular])
        for sid, s in v["sorular"].items():
            sid = int(sid)
            if sid not in sinav_sorulari:
                raise SystemExit(f"Soru {sid} bu sınavda yok.")
            q = vt.get(Soru, sid)
            c = next((c for c in t.cevaplar if c.soru_id == sid), None)
            if not c:
                c = Cevap(soru_id=sid)
                t.cevaplar.append(c)
                vt.flush()
            if s.get("kirpik"):
                ad = _gorsel_kaydet((Path(yol).with_suffix("") / s["kirpik"]).read_bytes())
                if not any(d.dosya == ad for d in c.dosyalar):
                    c.dosyalar.append(CevapDosya(dosya=ad, kaynak="kagittan"))
            if s.get("okunan") and not c.metin.strip():
                c.metin = f"[Yüklenen kâğıttan okundu] {s['okunan']}"
            kararlar = {int(a): d for a, (d, _) in s["kararlar"].items()}
            if any(d not in ADIM_DURUMLARI_GECERLI for d in kararlar.values()):
                raise SystemExit("Geçersiz adım durumu.")
            adim_idleri = {a.id for a in q.adimlar}
            if set(kararlar) - adim_idleri:
                raise SystemExit(f"Soru {sid}: rubrikte olmayan adım: {set(kararlar) - adim_idleri}")
            if s.get("aciklama") and (c.aciklama_kaynak != "ogretmen" or not c.ogretmen_notu):  # öğretmenin yazdığını ezme
                c.ogretmen_notu, c.aciklama_kaynak = s["aciklama"], "sistem"
            karar_yaz(vt, c, q, kararlar, {int(a): g for a, (_, g) in s["kararlar"].items()}, kaynak="sistem")
            vt.flush()
            rapor.append(f"Soru {sid}: {round(sum(a.puan for a in c.adimlar), 2)} / {q.zorluk}")
        if v.get("genel") and (t.genel_kaynak != "ogretmen" or not t.genel_geri_bildirim):
            t.genel_geri_bildirim, t.genel_kaynak = v["genel"], "sistem"
        vt.commit()
    return rapor


def _tek_bekleyen_teslim(vt, set_klasoru: Path) -> Teslim:
    """Setin sorularını içeren sınavlarda gönderilmiş, henüz hiçbir adımına karar verilmemiş teslim; tek olmalı."""
    metinler = {s["metin"] for s in json.loads((set_klasoru / "sorular.json").read_text(encoding="utf-8"))["sorular"]}
    adaylar = [t for t in vt.scalars(select(Teslim).where(Teslim.durum == "teslim", Teslim.degerlendirme == "bekliyor"))
               if any(x.soru.metin in metinler for x in t.atama.sinav.sorular)
               and not any(c.adimlar for c in t.cevaplar if c.secilen is None)]  # çoktan seçmeliler teslimde otomatik
    if len(adaylar) != 1:
        raise SystemExit(f"Bu sınavda değerlendirilmeyi bekleyen {len(adaylar)} teslim var; teslim_id yazılmalı.")
    return adaylar[0]


def _kimliklere_cevir(v: dict, set_klasoru: Path, sorular: list[Soru]) -> dict:
    """Set numarası ve adım sırasıyla yazılmış değerlendirmeyi soru ve rubrik adımı kimliklerine çevirir."""
    if not (set_klasoru / "sorular.json").is_file():
        raise SystemExit(f"Soru seti bulunamadı: {set_klasoru.name}")
    metinler = {str(s["no"]): s["metin"] for s in json.loads((set_klasoru / "sorular.json").read_text(encoding="utf-8"))["sorular"]}
    yeni = {}
    for no, s in v["sorular"].items():
        q = next((q for q in sorular if q.metin == metinler.get(no)), None)
        if not q:
            raise SystemExit(f"Soru {no}: bu teslimin sınavında yok (ya da metni değiştirilmiş).")
        kararlar = {}
        for sira, karar in s["kararlar"].items():
            if not 1 <= int(sira) <= len(q.adimlar):
                raise SystemExit(f"Soru {no}: rubrikte {sira}. adım yok (soruda {len(q.adimlar)} adım var).")
            kararlar[str(q.adimlar[int(sira) - 1].id)] = karar
        yeni[str(q.id)] = {**s, "kararlar": kararlar}
    return {**v, "sorular": yeni}


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    print("\n".join(aktar(sys.argv[1])))
