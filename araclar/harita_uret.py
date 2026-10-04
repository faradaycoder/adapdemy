"""Mikro kazanımlar arasındaki ön koşul ilişkilerini etkileşimli HTML haritaya dönüştürür
ve tutarlılık denetimi yapar.

Kullanım (EVALORA klasöründen):  python3 araclar/harita_uret.py
excel_uret.py de sonunda bu betiği çalıştırır. Harita tek dosyadır, internet gerektirmez.
Denetim raporu: her dersin klasöründe "<Ders> Harita Denetimi.md".
"""

import csv
import json
from collections import defaultdict
from pathlib import Path

import zorluk

KOK = Path(__file__).resolve().parent.parent

DERSLER = [
    {"ad": "Fizik", "klasor": KOK / "Fizik", "onek": "fizik", "birim": "Ana ünite",
     "ana_csv": "fizik_ana_uniteler.csv"},
    {"ad": "Matematik", "klasor": KOK / "Matematik", "onek": "matematik", "birim": "Ana tema",
     "ana_csv": "matematik_ana_temalar.csv"},
]

RENKLER = ["#2a78d6", "#d6632a", "#2a9d5c", "#9b4dca", "#c9a100", "#d63a6c", "#1e9fb0", "#7a7a7a",
           "#5b4bd6", "#a0522d", "#7fb800", "#e0559a"]

KATMAN_ARALIK = 300
SATIR_ARALIK = 58
DUGUM_EN, DUGUM_BOY = 230, 44


def oku(yol):
    with open(yol, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def liste(s):
    return [x.strip() for x in s.split(";") if x.strip()]


def denetle_ve_yerlestir(mikro, esleme, yan):
    kodlar = {m["kod"] for m in mikro}
    on = {m["kod"]: liste(m["on_kosul_kodlari"]) for m in mikro}
    sorunlar = defaultdict(list)

    for k, ps in on.items():
        for p in ps:
            if p not in kodlar:
                sorunlar["Tanımsız ön koşul kodu"].append(f"{k} → {p}")
            if p == k:
                sorunlar["Kendini ön koşul gösteren"].append(k)
    on = {k: [p for p in ps if p in kodlar and p != k] for k, ps in on.items()}

    # döngü denetimi (DFS)
    durum, dongu = {}, []
    def dfs(k, yol):
        durum[k] = 1
        for p in on[k]:
            if durum.get(p) == 1:
                dongu.append(" → ".join(yol[yol.index(p):] + [p]) if p in yol else f"{k} → {p}")
            elif p not in durum:
                dfs(p, yol + [p])
        durum[k] = 2
    for k in on:
        if k not in durum:
            dfs(k, [k])
    for d in dongu:
        sorunlar["Döngü"].append(d)

    sonraki = defaultdict(list)
    for k, ps in on.items():
        for p in ps:
            sonraki[p].append(k)
    for m in mikro:
        k = m["kod"]
        if not on[k] and not sonraki[k]:
            sorunlar["Kopuk düğüm (ön koşulu da, ardılı da yok)"].append(k)
        if not on[k] and not m["on_kosul_diger"].strip():
            sorunlar["Ön koşulu hiç belirtilmemiş (başlangıç düğümü)"].append(k)
    eslenen = {e["mikro_kod"] for e in esleme}
    for k in sorted(kodlar - eslenen):
        sorunlar["Hiçbir öğrenme çıktısına eşlenmemiş"].append(k)
    for e in esleme:
        if e["mikro_kod"] not in kodlar:
            sorunlar["Eşlemede tanımsız mikro kod"].append(e["mikro_kod"])
    yk = {y["kod"] for y in yan}
    for m in mikro:
        for y in liste(m["yanilgilar"]):
            if y not in yk:
                sorunlar["Tanımsız yanılgı kodu"].append(f"{m['kod']} → {y}")
    for y in yan:
        if not liste(y["ilgili_mikro_kazanimlar"]):
            sorunlar["Hiçbir mikro kazanıma bağlanmamış yanılgı"].append(y["kod"])

    # katman (en uzun ön koşul zinciri), döngü varsa kırılır
    derinlik = {}
    def d(k, gorulen=()):
        if k in derinlik:
            return derinlik[k]
        if k in gorulen:
            return 0
        derinlik[k] = 0 if not on[k] else 1 + max(d(p, gorulen + (k,)) for p in on[k])
        return derinlik[k]
    for k in on:
        d(k)

    ana = {m["kod"]: m["ana_unite"] for m in mikro}
    katmanlar = defaultdict(list)
    for k in sorted(kodlar):
        katmanlar[derinlik[k]].append(k)
    sira = {}
    for L in sorted(katmanlar):
        katmanlar[L].sort(key=lambda k: (ana[k], k))
        for i, k in enumerate(katmanlar[L]):
            sira[k] = i
    # kesişimleri azaltmak için ağırlık merkezi (barycenter) sıralaması
    for _ in range(6):
        for L in sorted(katmanlar)[1:]:
            def agirlik(k):
                ps = on[k]
                return (sum(sira[p] for p in ps) / len(ps)) if ps else sira[k]
            katmanlar[L].sort(key=lambda k: (agirlik(k), ana[k], k))
            for i, k in enumerate(katmanlar[L]):
                sira[k] = i
        for L in sorted(katmanlar, reverse=True)[1:]:
            def agirlik2(k):
                ss = sonraki[k]
                return (sum(sira[s] for s in ss) / len(ss)) if ss else sira[k]
            katmanlar[L].sort(key=lambda k: (agirlik2(k), ana[k], k))
            for i, k in enumerate(katmanlar[L]):
                sira[k] = i
    en_uzun = max(len(v) for v in katmanlar.values())
    konum = {}
    for L, ks in katmanlar.items():
        ofset = (en_uzun - len(ks)) * SATIR_ARALIK / 2
        for i, k in enumerate(ks):
            konum[k] = (40 + L * KATMAN_ARALIK, 40 + ofset + i * SATIR_ARALIK)
    genislik = 80 + max(katmanlar) * KATMAN_ARALIK + DUGUM_EN
    yukseklik = 80 + en_uzun * SATIR_ARALIK
    return on, sonraki, konum, (genislik, yukseklik), sorunlar, max(katmanlar) + 1, derinlik


def organik_yerlestir(mikro, on, derinlik, etki):
    """Kuvvet tabanlı yerleşim. Ön koşul bağlantıları yay gibi çeker, düğümler birbirini iter;
    aynı ana ünite/temadaki düğümler hafifçe kendi merkezlerine çekilir (yumuşak gruplama),
    ünite içinde temel kazanımlar sola, ileri kazanımlar sağa yatkındır. Bağlantılar değişmez."""
    import numpy as np
    kodlar = [m["kod"] for m in mikro]
    ix = {k: i for i, k in enumerate(kodlar)}
    ana = [m["ana_unite"] for m in mikro]
    unite = sorted(set(ana))
    ui = np.array([unite.index(a) for a in ana])
    n = len(kodlar)
    # ünite içi derinlik (yalnızca aynı ünitedeki ön koşullar)
    yerel = {}
    def ld(k, gor=()):
        if k in yerel:
            return yerel[k]
        if k in gor:
            return 0
        ps = [p for p in on[k] if ana[ix[p]] == ana[ix[k]]]
        yerel[k] = 0 if not ps else 1 + max(ld(p, gor + (k,)) for p in ps)
        return yerel[k]
    L = np.array([ld(k) for k in kodlar], dtype=float)
    for u in range(len(unite)):
        m = ui == u
        L[m] = (L[m] - L[m].mean()) / (max(1.0, L[m].max() - L[m].min()))
    boyut = np.array([(ui == u).sum() for u in range(len(unite))], dtype=float)
    # ünite merkezleri: altın açı sarmalı, büyük üniteler merkeze yakın
    sira = np.argsort(-boyut)
    merkez = np.zeros((len(unite), 2))
    for r, u in enumerate(sira):
        aci = r * 2.39996
        yar = 0 if r == 0 else 260 * np.sqrt(r + 0.6)
        merkez[u] = (yar * np.cos(aci) * 1.5, yar * np.sin(aci))
    rng = np.random.default_rng(7)
    olcek = 12 * np.sqrt(boyut[ui])
    P = merkez[ui] + np.c_[L * olcek * 2.2, rng.normal(0, 1, n) * olcek * 0.6]
    E = np.array([(ix[p], ix[k]) for k in kodlar for p in on[k]], dtype=int).reshape(-1, 2)
    ayni = (ui[E[:, 0]] == ui[E[:, 1]]) if len(E) else np.array([], bool)
    yay_k = np.where(ayni, 0.06, 0.012)
    R = 6 + 2.0 * np.sqrt(np.array([etki[k] for k in kodlar], float))
    R = np.minimum(R, 32)
    sicak = 40.0
    for t in range(450):
        D = P[:, None, :] - P[None, :, :]
        d2 = (D ** 2).sum(-1) + 1e-6
        minm = (R[:, None] + R[None, :] + 14) ** 2
        itme = np.where(d2 < 180 ** 2, 900.0 / d2, 0) + np.where(d2 < minm, 3.0 / np.sqrt(d2), 0)
        np.fill_diagonal(itme, 0)
        F = (D * itme[..., None]).sum(1)
        if len(E):
            dd = P[E[:, 1]] - P[E[:, 0]]
            uz = np.sqrt((dd ** 2).sum(1)) + 1e-6
            f = (yay_k * (uz - 70))[:, None] * dd / uz[:, None]
            np.add.at(F, E[:, 0], f)
            np.add.at(F, E[:, 1], -f)
        # yumuşak gruplama ve ünite içi akış
        for u in range(len(unite)):
            m = ui == u
            c = P[m].mean(0)
            F[m] += 0.022 * (c - P[m])
            F[m, 0] += 0.03 * (c[0] + L[m] * olcek[m] * 2.2 - P[m, 0])
        F += -0.004 * (P - P.mean(0))
        boy = np.sqrt((F ** 2).sum(1)) + 1e-9
        P += F / boy[:, None] * np.minimum(boy, sicak)[:, None]
        sicak = max(1.5, sicak * 0.992)
    P -= P.min(0)
    P += 120
    konum = {k: (float(P[i, 0]), float(P[i, 1])) for i, k in enumerate(kodlar)}
    etiket = []
    for u, a in enumerate(unite):
        m = ui == u
        etiket.append({"ana": a, "x": float(np.median(P[m, 0])), "y": float(np.median(P[m, 1])) + 16, "n": int(m.sum())})
    return konum, (float(P[:, 0].max() + 120), float(P[:, 1].max() + 120)), etiket, {k: float(R[i]) for i, k in enumerate(kodlar)}


def uret(d):
    veri = d["klasor"] / "veri"
    yol = veri / f"{d['onek']}_mikro_kazanimlar.csv"
    if not yol.exists():
        return None
    mikro = [m for m in oku(yol) if m.get("durum", "").strip() != "iptal"]  # iptal kodlar haritaya girmez
    etkin = {m["kod"] for m in mikro}
    esleme = [e for e in oku(veri / f"{d['onek']}_kazanim_esleme.csv") if e["mikro_kod"] in etkin]
    yan = oku(veri / f"{d['onek']}_yanilgilar.csv")
    ana_rows = oku(veri / d["ana_csv"])
    ana_ad = {r["kod"]: r["ad"] for r in ana_rows}
    on, sonraki, konum, boyut, sorunlar, katman_sayisi, derinlik = denetle_ve_yerlestir(mikro, esleme, yan)

    def ardillar(k):
        gor, st = set(), [k]
        while st:
            for s in sonraki[st.pop()]:
                if s not in gor:
                    gor.add(s); st.append(s)
        return gor
    etki = {m["kod"]: len(ardillar(m["kod"])) for m in mikro}
    konum2, boyut2, cerceve, yaricap = organik_yerlestir(mikro, on, derinlik, etki)
    # adaptif test motoru için grafik (ön koşul sırasına göre, önce kökler)
    sirali = sorted(mikro, key=lambda m: (derinlik[m["kod"]], m["kod"]))
    zor = zorluk.hesapla(mikro)
    graf = {"ders": d["ad"], "aciklama": "Yönlü döngüsüz ön koşul grafiği. on: doğrudan ön koşullar; derinlik: en uzun ön koşul zinciri; etki: bu kazanıma doğrudan ya da dolaylı dayanan mikro kazanım sayısı; islem: işlem türü; zorluk: √(kendi işlem değerinin karesi + doğrudan ön koşullarının işlem değerlerinin kareleri toplamı) (RSS); seviye: ⌊zorluk⌋ (ALGORITMA.md). Liste ön koşul sırasındadır (topolojik).",
            "dugumler": [{"kod": m["kod"], "ana": m["ana_unite"], "tur": m["tur"], "duzey": m["bilissel_duzey"],
                          "islem": m.get("islem_turu", ""), "zorluk": zor[m["kod"]]["zorluk"],
                          "seviye": zor[m["kod"]]["seviye"],
                          "derinlik": derinlik[m["kod"]], "etki": etki[m["kod"]], "on": on[m["kod"]],
                          "sonraki": sorted(sonraki[m["kod"]]), "yanilgilar": liste(m["yanilgilar"]),
                          "ciktilar": sorted({e["ogrenme_ciktisi"] for e in esleme if e["mikro_kod"] == m["kod"]})}
                         for m in sirali]}
    (veri / f"{d['onek']}_graf.json").write_text(json.dumps(graf, ensure_ascii=False, indent=1), encoding="utf-8")

    es = defaultdict(list)
    for e in esleme:
        es[e["mikro_kod"]].append({"sinif": e["sinif"], "unite": e["sinif_unite"],
                                   "cikti": e["ogrenme_ciktisi"], "bilesen": e["surec_bileseni"]})
    kullanilan = sorted({m["ana_unite"] for m in mikro})
    renk = {a: RENKLER[i % len(RENKLER)] for i, a in enumerate(kullanilan)}
    dugumler = [{
        "kod": m["kod"], "ana": m["ana_unite"], "ifade": m["ifade"], "tur": m["tur"],
        "duzey": m["bilissel_duzey"], "on": on[m["kod"]], "sonraki": sorted(sonraki[m["kod"]]),
        "diger": m["on_kosul_diger"], "yan": liste(m["yanilgilar"]), "olcme": m["olcme_turleri"],
        "es": es[m["kod"]], "x": konum[m["kod"]][0], "y": konum[m["kod"]][1],
        "kx": round(konum2[m["kod"]][0], 1), "ky": round(konum2[m["kod"]][1], 1), "r": round(yaricap[m["kod"]], 1),
        "derinlik": derinlik[m["kod"]], "etki": etki[m["kod"]],
    } for m in mikro]
    veri_js = {
        "ders": d["ad"], "birim": d["birim"], "boyut": boyut, "kboyut": boyut2, "kume": cerceve, "en": DUGUM_EN, "boy": DUGUM_BOY,
        "dugumler": dugumler,
        "yanilgi": {y["kod"]: y["yanilgi"] for y in yan},
        "unite": [{"kod": a, "ad": ana_ad.get(a, a), "renk": renk[a]} for a in kullanilan],
        "ciktilar": sorted({e["ogrenme_ciktisi"] for e in esleme}),
    }
    html = SABLON.replace("__BASLIK__", f"{d['ad']} Mikro Kazanım Haritası").replace(
        "__VERI__", json.dumps(veri_js, ensure_ascii=False))
    cikis = d["klasor"] / f"{d['ad']} Mikro Kazanım Haritası.html"
    cikis.write_text(html, encoding="utf-8")

    kenar = sum(len(v) for v in on.values())
    kokler = sum(1 for m in mikro if derinlik[m["kod"]] == 0)
    rap = [f"# {d['ad']} Harita Denetimi", "",
           f"{len(mikro)} mikro kazanım, {kenar} ön koşul ilişkisi, {katman_sayisi} katman (en uzun ön koşul zinciri), {kokler} kök düğüm.", "",
           "En yüksek etkili 10 mikro kazanım (en çok kazanım bunlara dayanıyor): " + ", ".join(f"{k} ({v})" for k, v in sorted(etki.items(), key=lambda x: -x[1])[:10]), ""]
    if not sorunlar:
        rap.append("Sorun bulunmadı.")
    for baslik, kalemler in sorunlar.items():
        rap += [f"## {baslik} ({len(kalemler)})", "", ", ".join(kalemler), ""]
    (d["klasor"] / f"{d['ad']} Harita Denetimi.md").write_text("\n".join(rap) + "\n", encoding="utf-8")
    print(f"Üretildi: {cikis.relative_to(KOK)}")
    return {k: len(v) for k, v in sorunlar.items()}


SABLON = r"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>__BASLIK__</title>
<style>
:root{--bg:#fbfbfa;--panel:#ffffff;--ink:#1d1d1f;--muted:#6b6b70;--line:#c9c9cf;--edge:#9a9aa3;--hi:#e0443e;--hi2:#1f7a3f;--card:#f2f2f0;--glow:#ffffff}
@media (prefers-color-scheme: dark){:root{--bg:#161618;--panel:#1f1f22;--ink:#ececef;--muted:#a0a0a8;--line:#3a3a40;--edge:#5d5d66;--hi:#ff6b63;--hi2:#4cc47a;--card:#26262a;--glow:#25252b}}
*{box-sizing:border-box}html,body{margin:0;height:100%;background:var(--bg);color:var(--ink);font:14px/1.45 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
header{display:flex;flex-wrap:wrap;gap:8px 14px;align-items:center;padding:10px 16px;border-bottom:1px solid var(--line);background:var(--panel)}
h1{font-size:16px;margin:0 8px 0 0}
input,select,button{font:inherit;color:var(--ink);background:var(--bg);border:1px solid var(--line);border-radius:6px;padding:5px 8px}
button{cursor:pointer}
#arakutu{position:relative}
#sonuc{position:absolute;top:100%;left:0;z-index:20;width:min(560px,92vw);max-height:60vh;overflow:auto;background:var(--panel);border:1px solid var(--line);border-radius:8px;box-shadow:0 6px 18px rgba(0,0,0,.15);display:none}
#sonuc div{padding:6px 10px;font-size:13px;cursor:pointer;border-bottom:1px solid var(--line)}
#sonuc div:hover,#sonuc div.akt{background:var(--card)}
#sonuc b{margin-right:6px}
#legend{display:flex;flex-wrap:wrap;gap:6px 12px;font-size:12px;color:var(--muted)}
#legend span{display:inline-flex;align-items:center;gap:5px;cursor:pointer}
#legend i{width:11px;height:11px;border-radius:3px;display:inline-block}
main{display:flex;height:calc(100% - 58px)}
#wrap{flex:1;overflow:hidden;position:relative;cursor:grab}
#wrap.drag{cursor:grabbing}
svg{display:block}
.n rect{stroke-width:1.5}
.n text{font-size:11px;fill:var(--ink);pointer-events:none}
.n .c{font-weight:600}
.n.dim{opacity:.1}.e.dim{opacity:.03}
.e{fill:none;stroke:var(--edge);stroke-width:1.1}
.e.anc{stroke:var(--hi);stroke-width:2.2;opacity:1}.e.des{stroke:var(--hi2);stroke-width:2.2;opacity:1}
.n.sel rect{stroke:var(--ink);stroke-width:3}
.n.anc rect{stroke:var(--hi);stroke-width:2.5}.n.des rect{stroke:var(--hi2);stroke-width:2.5}
/* organik görünüm */
#wrap.org{background:radial-gradient(ellipse at 50% 45%,var(--glow) 0%,var(--bg) 70%)}
.org .kart{display:none}svg:not(.org) .nokta,svg:not(.org) .etiket{display:none}
.org .e{stroke-width:1.3;opacity:.42}.org .e.anc,.org .e.des{opacity:1;stroke-width:2.4}
.nokta circle{stroke:var(--bg);stroke-width:1.5;transition:r .15s}
.nokta circle.bilgi{fill:var(--bg)!important;stroke-width:3.5}
.nokta text{font-size:10px;fill:var(--muted);text-anchor:middle;display:none}
.yakin .nokta text{display:block}
.n.sel .nokta circle{stroke:var(--ink);stroke-width:4}
.n.anc .nokta circle{stroke:var(--hi);stroke-width:3.5}.n.des .nokta circle{stroke:var(--hi2);stroke-width:3.5}
.n.sel .nokta text,.n.anc .nokta text,.n.des .nokta text{display:block;fill:var(--ink);font-weight:600}
.etiket text{font-size:64px;font-weight:800;letter-spacing:.01em;opacity:.16;text-anchor:middle;pointer-events:none}
#ipucu{position:absolute;pointer-events:none;background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:6px 9px;font-size:12px;max-width:300px;box-shadow:0 4px 14px rgba(0,0,0,.12);display:none}
aside{width:360px;max-width:45vw;border-left:1px solid var(--line);background:var(--panel);overflow:auto;padding:14px 16px}
aside h2{font-size:15px;margin:0 0 6px}
.k{font-size:12px;color:var(--muted);margin-top:12px;text-transform:uppercase;letter-spacing:.04em}
.chip{display:inline-block;margin:2px 4px 2px 0;padding:2px 7px;border-radius:10px;background:var(--card);font-size:12px;cursor:pointer}
.tag{display:inline-block;padding:1px 7px;border-radius:10px;font-size:12px;border:1px solid var(--line);margin-right:4px}
ul{padding-left:18px;margin:4px 0}
.hint{color:var(--muted);font-size:13px}
@media (max-width:700px){main{flex-direction:column}aside{width:auto;max-width:none;height:40%;border-left:0;border-top:1px solid var(--line)}}
</style></head><body>
<header>
 <h1>__BASLIK__</h1>
 <div id="arakutu"><input id="q" placeholder="Ara: kod, ifade ya da çıktı (Enter: ilk sonuca git)" size="34" autocomplete="off"><div id="sonuc"></div></div>
 <select id="cikti"><option value="">Tüm öğrenme çıktıları</option></select>
 <button id="yerlesim" title="Yerleşimi değiştir (bağlantılar aynı kalır)">Görünüm: Harita</button>
 <button id="sifirla">Sıfırla</button>
 <div id="legend"></div>
</header>
<main>
 <div id="wrap"><svg id="svg"></svg><div id="ipucu"></div></div>
 <aside id="panel"><p class="hint">Bir mikro kazanıma tıklayın: kırmızı oklar ön koşul zincirini (öğrenci neden takılmış olabilir), yeşil oklar ona dayanan mikro kazanımları gösterir. "Harita" görünümünde her nokta bir mikro kazanımdır: renk ana ünite/temayı, büyüklük etkiyi (ona dayanan mikro kazanım sayısı) gösterir; dolu nokta Beceri, halka Bilgi. Aynı ünitedekiler bir arada toplanır, ünite içinde temel kazanımlar solda, ileri kazanımlar sağdadır. Yakınlaşınca kodlar görünür, üzerine gelince ifade çıkar. "Tek zincir" görünümünde tüm mikro kazanımlar kart olarak derinliğe göre soldan sağa dizilir (D = derinlik, E = etki). Sürükleyerek kaydırın, fare tekerleğiyle yakınlaştırın.</p><p class="hint">Adaptif testte kullanım: öğrenci bir kazanımda başarısız olursa kırmızı zincirde geriye inilir; yapabildiği son halka ile yapamadığı ilk halka arasındaki kazanım eksik köktür.</p></aside>
</main>
<script>
const V=__VERI__;
const NS="http://www.w3.org/2000/svg",svg=document.getElementById("svg"),wrap=document.getElementById("wrap");
const byK=Object.fromEntries(V.dugumler.map(n=>[n.kod,n])),renk=Object.fromEntries(V.unite.map(u=>[u.kod,u.renk]));
let mod="zincir";try{if(localStorage.getItem("harita-gorunum")==="org")mod="org"}catch(e){}
let [W,H]=V.boyut;
const g=document.createElementNS(NS,"g");svg.appendChild(g);
const el=(t,a,p)=>{const e=document.createElementNS(NS,t);for(const k in a)e.setAttribute(k,a[k]);(p||g).appendChild(e);return e};
const edges=[],nodes={};
const kg=el("g",{class:"etiket"});
for(const c of V.kume){const u=V.unite.find(u=>u.kod===c.ana)||{ad:c.ana,renk:"#888"};
 const t=el("text",{x:c.x,y:c.y},kg);t.textContent=u.ad;t.style.fill=u.renk}
const eg=el("g",{});
const pos=n=>mod==="org"?[n.kx,n.ky]:[n.x,n.y];
function yol(a,n){const [ax,ay]=pos(a),[nx,ny]=pos(n);
 if(mod==="org"){const dx=nx-ax,dy=ny-ay,mx=(ax+nx)/2-dy*.18,my=(ay+ny)/2+dx*.18;return `M${ax},${ay} Q${mx},${my} ${nx},${ny}`}
 const x1=ax+V.en,y1=ay+V.boy/2,x2=nx,y2=ny+V.boy/2,dx=Math.max(60,Math.abs(x2-x1)/2);
 return `M${x1},${y1} C${x1+dx},${y1} ${x2-dx},${y2} ${x2},${y2}`}
for(const n of V.dugumler)for(const p of n.on){const a=byK[p];
 edges.push({from:p,to:n.kod,e:el("path",{class:"e",d:"",stroke:renk[a.ana]},eg)});}
const kisalt=s=>s.length>38?s.slice(0,37)+"…":s;
const ipucu=document.getElementById("ipucu");
for(const n of V.dugumler){const ng=el("g",{class:"n"});
 const r=n.tur==="Bilgi"?16:3,c=renk[n.ana];
 const kart=el("g",{class:"kart"},ng);
 el("rect",{width:V.en,height:V.boy,rx:r,fill:"var(--panel)",stroke:c},kart);
 if(n.es.length>1)el("rect",{x:3,y:3,width:V.en-6,height:V.boy-6,rx:Math.max(r-3,1),fill:"none",stroke:c,"stroke-width":1},kart);
 el("rect",{width:6,height:V.boy,rx:2,fill:c,stroke:"none"},kart);
 const t1=el("text",{x:12,y:17,class:"c"},kart);t1.textContent=`${n.kod} · ${n.tur} · D${n.derinlik} · E${n.etki}`;
 const t2=el("text",{x:12,y:33},kart);t2.textContent=kisalt(n.ifade);
 const nk=el("g",{class:"nokta"},ng);
 const ci=el("circle",{r:n.r,fill:c,stroke:c},nk);if(n.tur==="Bilgi"){ci.classList.add("bilgi");ci.style.stroke=c}
 const tt=el("text",{y:n.r+12},nk);tt.textContent=n.kod;
 ng.style.cursor="pointer";ng.addEventListener("click",ev=>{ev.stopPropagation();sec(n.kod)});
 ng.addEventListener("mouseenter",ev=>{if(mod!=="org")return;ipucu.innerHTML=`<b>${n.kod}</b> · ${n.tur} · etki ${n.etki}<br>${n.ifade}`;ipucu.style.display="block"});
 ng.addEventListener("mousemove",ev=>{const r=wrap.getBoundingClientRect();ipucu.style.left=Math.min(ev.clientX-r.left+14,r.width-310)+"px";ipucu.style.top=(ev.clientY-r.top+14)+"px"});
 ng.addEventListener("mouseleave",()=>ipucu.style.display="none");
 nodes[n.kod]=ng;}
// büyük noktalar üstte dursun
[...V.dugumler].sort((a,b)=>a.r-b.r).forEach(n=>g.appendChild(nodes[n.kod]));
function yerlesim(){[W,H]=mod==="org"?V.kboyut:V.boyut;svg.classList.toggle("org",mod==="org");wrap.classList.toggle("org",mod==="org");
 for(const n of V.dugumler){const [x,y]=pos(n);nodes[n.kod].setAttribute("transform",`translate(${x},${y})`)}
 for(const e of edges)e.e.setAttribute("d",yol(byK[e.from],byK[e.to]));
 document.getElementById("yerlesim").textContent="Görünüm: "+(mod==="org"?"Harita":"Tek zincir")}
yerlesim();
document.getElementById("yerlesim").onclick=()=>{mod=mod==="org"?"zincir":"org";try{localStorage.setItem("harita-gorunum",mod)}catch(e){}yerlesim();sigdir();if(secili)odakla(secili)};
// ünite göstergesi
const lg=document.getElementById("legend");const gizli=new Set();
for(const u of V.unite){const s=document.createElement("span");s.innerHTML=`<i style="background:${u.renk}"></i>${u.kod} ${u.ad}`;
 s.onclick=()=>{gizli.has(u.kod)?gizli.delete(u.kod):gizli.add(u.kod);s.style.opacity=gizli.has(u.kod)?.35:1;filtre()};lg.appendChild(s)}
const cs=document.getElementById("cikti");for(const c of V.ciktilar){const o=document.createElement("option");o.value=o.textContent=c;cs.appendChild(o)}
// zincir
function zincir(k,yon){const out=new Set(),st=[k];while(st.length){const x=st.pop();for(const y of byK[x][yon])if(!out.has(y)){out.add(y);st.push(y)}}return out}
let secili=null;
function temizle(){for(const k in nodes)nodes[k].classList.remove("sel","anc","des","dim");for(const e of edges)e.e.classList.remove("anc","des","dim")}
function sec(k){secili=k;temizle();const A=zincir(k,"on"),D=zincir(k,"sonraki");
 for(const x in nodes){if(x===k)nodes[x].classList.add("sel");else if(A.has(x))nodes[x].classList.add("anc");else if(D.has(x))nodes[x].classList.add("des");else nodes[x].classList.add("dim")}
 for(const e of edges){const ia=(A.has(e.from)&&(A.has(e.to)||e.to===k)),id=((D.has(e.to))&&(D.has(e.from)||e.from===k));
  if(ia)e.e.classList.add("anc");else if(id)e.e.classList.add("des");else e.e.classList.add("dim")}
 panel(k,A,D)}
const chip=k=>`<span class="chip" data-k="${k}">${k}</span>`;
function panel(k,A,D){const n=byK[k],p=document.getElementById("panel");
 p.innerHTML=`<h2>${n.kod}</h2><span class="tag" style="border-color:${renk[n.ana]}">${V.birim} ${n.ana}</span><span class="tag">${n.tur}</span><span class="tag">${n.duzey}</span><span class="tag">Derinlik ${n.derinlik}</span><span class="tag">Etki ${n.etki}</span>
 <p>${n.ifade}</p>
 <div class="k">Kullanıldığı öğrenme çıktıları</div><ul>${n.es.map(e=>`<li>${e.sinif}. sınıf · ${e.unite} · ${e.cikti} (${e.bilesen})</li>`).join("")}</ul>
 <div class="k">Doğrudan ön koşullar</div>${n.on.map(chip).join("")||'<span class="hint">yok</span>'}${n.diger?`<p class="hint">${n.diger}</p>`:""}
 <div class="k">Tüm ön koşul zinciri (${A.size})</div>${[...A].sort().map(chip).join("")||'<span class="hint">yok</span>'}
 <div class="k">Bu kazanıma dayananlar (${D.size})</div>${[...D].sort().map(chip).join("")||'<span class="hint">yok</span>'}
 <div class="k">Yanılgılar</div><ul>${n.yan.map(y=>`<li><b>${y}</b> ${V.yanilgi[y]||""}</li>`).join("")||'<li class="hint">yok</li>'}</ul>
 <div class="k">Ölçme</div><p>${n.olcme}</p>`;
 p.querySelectorAll(".chip").forEach(c=>c.onclick=()=>{sec(c.dataset.k);odakla(c.dataset.k)})}
function filtre(){const q=document.getElementById("q").value.trim().toLocaleLowerCase("tr"),c=cs.value;secili=null;temizle();
 const gor=new Set();for(const n of V.dugumler){let ok=!gizli.has(n.ana);
  if(ok&&q)ok=(n.kod+" "+n.ifade+" "+n.es.map(e=>e.cikti).join(" ")).toLocaleLowerCase("tr").includes(q);
  if(ok&&c)ok=n.es.some(e=>e.cikti===c);if(ok)gor.add(n.kod);else nodes[n.kod].classList.add("dim")}
 for(const e of edges)if(!(gor.has(e.from)&&gor.has(e.to)))e.e.classList.add("dim")}
const qk=document.getElementById("q"),sonuc=document.getElementById("sonuc");let bul=[],akt=0;
const norm=t=>t.toLocaleLowerCase("tr");
function listele(){const q=norm(qk.value.trim());sonuc.innerHTML="";bul=[];akt=0;
 if(!q){sonuc.style.display="none";return}
 const kel=q.split(/\s+/);
 bul=V.dugumler.filter(n=>{const t=norm(n.kod+" "+n.ifade+" "+n.es.map(e=>e.cikti).join(" "));return kel.every(w=>t.includes(w))}).slice(0,60);
 if(!bul.length){sonuc.innerHTML='<div>Sonuç yok</div>';sonuc.style.display="block";return}
 bul.forEach((n,i)=>{const d=document.createElement("div");d.innerHTML=`<b>${n.kod}</b>${n.ifade}`;if(i===0)d.className="akt";
  d.onmousedown=ev=>{ev.preventDefault();git(n.kod)};sonuc.appendChild(d)});sonuc.style.display="block"}
function git(k){sonuc.style.display="none";const c=document.getElementById("cikti");if(c)c.value="";gizli.clear();
 document.querySelectorAll("#legend span").forEach(s=>s.style.opacity=1);sec(k);ts.s=Math.max(ts.s,.9);odakla(k)}
qk.oninput=()=>{listele();filtre()};
qk.onkeydown=e=>{const it=sonuc.querySelectorAll("div");
 if(e.key==="ArrowDown"&&bul.length){akt=Math.min(akt+1,bul.length-1)}
 else if(e.key==="ArrowUp"&&bul.length){akt=Math.max(akt-1,0)}
 else if(e.key==="Enter"&&bul.length){git(bul[akt].kod);return}
 else if(e.key==="Escape"){sonuc.style.display="none";return} else return;
 e.preventDefault();it.forEach((d,i)=>d.className=i===akt?"akt":"");it[akt]&&it[akt].scrollIntoView({block:"nearest"})};
qk.onfocus=()=>{if(qk.value.trim())listele()};qk.onblur=()=>setTimeout(()=>sonuc.style.display="none",150);
document.addEventListener("keydown",e=>{if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==="f"){e.preventDefault();qk.focus();qk.select()}});
cs.onchange=filtre;
document.getElementById("sifirla").onclick=()=>{document.getElementById("q").value="";cs.value="";gizli.clear();lg.querySelectorAll("span").forEach(s=>s.style.opacity=1);filtre();sigdir()};
// kaydırma / yakınlaştırma
let ts={x:0,y:0,s:1};const uyg=()=>{g.setAttribute("transform",`translate(${ts.x},${ts.y}) scale(${ts.s})`);svg.classList.toggle("yakin",ts.s>=.75)};
svg.setAttribute("width","100%");svg.setAttribute("height","100%");
wrap.addEventListener("wheel",e=>{e.preventDefault();const r=wrap.getBoundingClientRect(),mx=e.clientX-r.left,my=e.clientY-r.top,f=e.deltaY<0?1.12:1/1.12;
 const s=Math.min(3,Math.max(.05,ts.s*f));ts.x=mx-(mx-ts.x)*s/ts.s;ts.y=my-(my-ts.y)*s/ts.s;ts.s=s;uyg()},{passive:false});
let dr=null;wrap.addEventListener("pointerdown",e=>{dr={x:e.clientX,y:e.clientY,ox:ts.x,oy:ts.y,m:false};wrap.classList.add("drag")});
window.addEventListener("pointermove",e=>{if(!dr)return;const dx=e.clientX-dr.x,dy=e.clientY-dr.y;if(Math.abs(dx)+Math.abs(dy)>3)dr.m=true;ts.x=dr.ox+dx;ts.y=dr.oy+dy;uyg()});
window.addEventListener("pointerup",()=>{wrap.classList.remove("drag");setTimeout(()=>dr=null,0)});
wrap.addEventListener("click",()=>{if(dr&&dr.m)return;if(secili){secili=null;filtre()}});
function odakla(k){const n=byK[k],[x,y]=pos(n),r=wrap.getBoundingClientRect();ts.s=Math.max(ts.s,.8);ts.x=r.width/2-(x+V.en/2)*ts.s;ts.y=r.height/2-(y+V.boy/2)*ts.s;uyg()}
function sigdir(){const r=wrap.getBoundingClientRect(),w=r.width>50?r.width:innerWidth*.6,h=r.height>50?r.height:innerHeight-110;ts.s=Math.max(.05,Math.min(1,w/W,h/H));ts.x=(w-W*ts.s)/2;ts.y=(h-H*ts.s)/2;uyg()}
sigdir();requestAnimationFrame(sigdir);addEventListener("load",sigdir);
</script></body></html>
"""


if __name__ == "__main__":
    for d in DERSLER:
        s = uret(d)
        if s is not None:
            print(f"  {d['ad']} denetimi:", s or "sorun yok")
