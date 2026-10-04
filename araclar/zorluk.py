"""Mikro kazanım zorluk puanını ve seviyesini ön koşul haritasından hesaplar.

Kural (ALGORITMA.md bölüm 4, 2026-10-02):
    Zorluk(k) = √( v(k)² + Σ v(p)² )   (p: k'nin doğrudan ön koşulları; kareler toplamının kökü, RSS)
    Seviye    = ⌊Zorluk⌋   (1 genişliğinde tam sayı aralıklar, üstü açık)

v(k), k'nin işlem türünün değeridir; değerler logaritmiktir: v = 1 + log₂(sıra) → 1, 2, 2.585, 3
(Weber–Fechner). İşlem değerleri ortak/islem_turleri.csv'den okunur; her mikro kazanımın işlem türü
<ders>_mikro_kazanimlar.csv'deki islem_turu sütunundadır. Yalnızca doğrudan ön koşullar sayılır;
geçmişi harita taşır, puan taşımaz.
"""

import csv
import math
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
ORTAK = KOK / "ortak"


def _oku(yol):
    with open(yol, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def islem_degerleri():
    return {r["islem_turu"]: float(r["deger"]) for r in _oku(ORTAK / "islem_turleri.csv")}


def seviye(zorluk):
    return int(math.floor(zorluk + 1e-9))


def hesapla(mikro):
    """mikro: mikro kazanım satırları. Dönüş: {kod: {"deger", "alt_sayisi", "zorluk", "seviye"}}.

    İşlem türü boş ya da tanımsız olan mikro kazanımın değeri 0 sayılır ve sonuçta "eksik" işaretlenir.
    """
    degerler = islem_degerleri()
    iptal = [m for m in mikro if m.get("durum", "").strip() == "iptal"]
    mikro = [m for m in mikro if m.get("durum", "").strip() != "iptal"]
    kodlar = {m["kod"] for m in mikro}
    on = {m["kod"]: [p.strip() for p in m["on_kosul_kodlari"].split(";") if p.strip() in kodlar] for m in mikro}
    v = {m["kod"]: degerler.get(m.get("islem_turu", "").strip()) for m in mikro}

    sonuc = {}
    for k in on:
        alt = set(on[k])
        eksik = v[k] is None or any(v[a] is None for a in alt)
        z = math.sqrt((v[k] or 0) ** 2 + sum((v[a] or 0) ** 2 for a in alt))
        sonuc[k] = {"deger": v[k], "alt_sayisi": len(alt), "zorluk": round(z, 2),
                    "seviye": seviye(z) if z > 0 else None, "eksik": eksik}
    for m in iptal:  # kullanımdan kalkan kodlar hesaba girmez
        sonuc[m["kod"]] = {"deger": degerler.get(m.get("islem_turu", "").strip()), "alt_sayisi": "",
                           "zorluk": "", "seviye": "iptal", "eksik": False}
    return sonuc


if __name__ == "__main__":
    import sys
    from collections import Counter
    for yol in sys.argv[1:]:
        s = hesapla(_oku(yol))
        print(yol, "seviye dağılımı:", sorted(Counter(x["seviye"] for x in s.values() if x["seviye"] != "iptal").items()),
              "en yüksek:", max(x["zorluk"] for x in s.values() if x["zorluk"] != ""),
              "eksik:", sum(x["eksik"] for x in s.values()))
