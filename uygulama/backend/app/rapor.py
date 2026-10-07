"""MK raporu: öğrencinin her MK için "biliyor" olasılığı (Bayesçi Bilgi İzleme, ALGORITMA.md 6.2).

Kanıt: onaylanmış teslimlerdeki rubrik adımı kararları, teslimlerin onaylanma sırasıyla. Biliyor → doğru cevap,
bilmiyor → yanlış cevap; ölçülemedi kanıt değildir (6.1). Sınav sırasında öğrenme yok sayılır (geçiş 0).
Başlangıç P(L₀) = 0,5; dikkatsizlik s = 0,10; tahmin g = 0,20 (çoktan seçmeli) ya da 0,05 (açık uçlu).
Durum: P ≥ 0,95 biliyor; P ≤ 0,20 bilmiyor; arada "belirsiz" (daha çok soru gerekir); kanıt yoksa ölçülemedi.
Ön koşul haritası üzerinden kanıt yayma (6.2, son paragraf) henüz yok.
"""

from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.orm import Session

from .modeller import Atama, Soru, Teslim

P0, S = 0.5, 0.10
G_COKTAN, G_ACIK = 0.20, 0.05
BILIYOR_ESIK, BILMIYOR_ESIK = 0.95, 0.20


def guncelle(p: float, dogru: bool, g: float, s: float = S) -> float:
    if dogru:
        return p * (1 - s) / (p * (1 - s) + (1 - p) * g)
    return p * s / (p * s + (1 - p) * (1 - g))


def durum(p: float | None) -> str:
    if p is None:
        return "olculemedi"
    p = round(p, 2)  # eşikler yüzde olarak: açık uçlu tek doğru 0,947 → %95 (ALGORITMA.md 6.2'deki örnekle aynı)
    return "biliyor" if p >= BILIYOR_ESIK else "bilmiyor" if p <= BILMIYOR_ESIK else "belirsiz"


@dataclass
class MKKanit:
    p: float | None = None
    dogru: int = 0
    yanlis: int = 0
    olculemedi: int = 0

    @property
    def durum(self) -> str:
        return durum(self.p)


def onayli_teslimler(vt: Session, ogrenci_id: int, sinif_id: int | None = None) -> list[Teslim]:
    q = select(Teslim).where(Teslim.ogrenci_id == ogrenci_id, Teslim.degerlendirme == "onayli")
    if sinif_id is not None:
        q = q.join(Atama).where(Atama.sinif_id == sinif_id)
    return sorted(vt.scalars(q), key=lambda t: (t.sonuc_zamani or t.teslim_zamani or t.baslama, t.id))


def mk_kanitlari(vt: Session, teslimler: list[Teslim]) -> dict[str, MKKanit]:
    """Teslimlerdeki adım kararlarını sırayla işler; MK → kanıt."""
    sonuc: dict[str, MKKanit] = {}
    for t in teslimler:
        for c in t.cevaplar:
            q = vt.get(Soru, c.soru_id)
            g = G_COKTAN if q and q.cevap_bicimi == "coktan_secmeli" else G_ACIK
            for a in c.adimlar:
                k = sonuc.setdefault(a.adim.mk_kod, MKKanit())
                if a.durum == "olculemedi":
                    k.olculemedi += 1
                    continue
                dogru = a.durum == "biliyor"
                k.p = guncelle(P0 if k.p is None else k.p, dogru, g)
                if dogru:
                    k.dogru += 1
                else:
                    k.yanlis += 1
    return sonuc
