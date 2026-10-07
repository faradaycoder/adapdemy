"""Uyarlamalı test motoru (ALGORITMA.md 6.2–6.3; algoritma sayfası: "EVALORA Uyarlamalı Test").

Kapsam: bir kazanımın (öğrenme çıktısı) MK'leri ve bunların aynı sınıf düzeyindeki ön koşul zinciri (alt sınıflara
inilmez). Havuz: kapsamdaki bir MK'yi tek başına ölçen, onaylı, çoktan seçmeli sorular.

Her MK için "biliyor" olasılığı P tutulur. Başlangıç: öğrencinin onaylı sınavlarından gelen kanıt (rapor.py), yoksa 0,5.
Cevap güncellemesi DINA modeliyle yapılır: doğru cevap için sorunun bütün MK'leri gerekir; P(doğru | hepsi biliniyor)
= 1 − s, P(doğru | en az biri bilinmiyor) = g = 1 / şık sayısı. Tek MK'li soruda bu, Bayesçi bilgi izlemenin kendisidir.

Karar eşikleri (Murat, 2026-10-07): %95 ve üstü biliyor, %5 ve altı bilmiyor (sınav değerlendirmesindeki %20 burada
kullanılmaz: tek yanlışla "bilmiyor" denmez; 4 şıkta bilmiyor için 2 yanlış gerekir).

Çıkarım (Bilgi Uzayı Kuramı) yalnız yukarıdan aşağı: "biliyor" kararı verilen MK'nin ön koşulları da biliniyor sayılır
ve sorulmaz ("çıkarım"). Ön koşulu bilinmeyen MK "bilmiyor" sayılmaz; sorulmaya devam eder, soru hakkı kalmazsa
"sorulmadı · ön koşulu eksik" olarak raporlanır.

Soru seçimi: (1) cevabı alınmaya başlanmış ama kararı verilmemiş MK; (2) bilinmeyen bir MK'nin kararı verilmemiş
ön koşulu (kökü arar: yanlışta aşağı); (3) zincirin en üstündeki kararsız MK (doğruda ön koşulları çıkarımla kapanır).
Bir MK'ye en çok MAKS_MK, teste en çok MAKS_TOPLAM soru sorulur. Eksiğin kökü: bilinmeyen ama bilinmeyen ön koşulu
olmayan MK.
"""

from dataclasses import dataclass, field
from itertools import product

from sqlalchemy import select
from sqlalchemy.orm import Session

from .modeller import MK, MKEsleme, MKOnKosul, Soru, UyarlamaliOturum
from .rapor import P0, S, mk_kanitlari, onayli_teslimler

MAKS_MK, MAKS_TOPLAM = 4, 15
BILIYOR, BILMIYOR = 0.95, 0.05


def karar(p: float) -> str:
    p = round(p, 2)
    return "biliyor" if p >= BILIYOR else "bilmiyor" if p <= BILMIYOR else "belirsiz"


def kazanim_sinifi(kazanim: str) -> int:
    return int(kazanim.split(".")[1])  # MAT.6.1.2 → 6


def kapsam(vt: Session, kazanim: str) -> tuple[list[str], dict[str, set[str]]]:
    """Kazanımın MK'leri + aynı sınıf düzeyindeki ön koşul kapanışı; ve kapsam içi doğrudan ön koşullar."""
    sinif = kazanim_sinifi(kazanim)
    hedef = list(dict.fromkeys(vt.scalars(select(MKEsleme.mk_kod).where(MKEsleme.ogrenme_ciktisi == kazanim))))
    bu_sinif = set(vt.scalars(select(MKEsleme.mk_kod).where(MKEsleme.sinif == sinif)))
    on: dict[str, set[str]] = {}
    kume, yigin = set(), list(hedef)
    while yigin:
        k = yigin.pop()
        if k in kume:
            continue
        kume.add(k)
        on[k] = set(vt.scalars(select(MKOnKosul.on_kosul_kod).where(MKOnKosul.mk_kod == k))) & bu_sinif
        yigin.extend(on[k])
    for k in on:
        on[k] &= kume
    return sorted(kume), on


def soru_mkleri(q: Soru) -> list[str]:
    return sorted({a.mk_kod for a in q.adimlar} | {m.mk_kod for m in q.mkler})


def havuz(vt: Session, sahipler: list[int], mkler: list[str]) -> dict[str, list[Soru]]:
    """MK → onu tek başına ölçen onaylı çoktan seçmeli sorular (id sırasıyla)."""
    sonuc: dict[str, list[Soru]] = {m: [] for m in mkler}
    if not sahipler:
        return sonuc
    q = select(Soru).where(Soru.olusturan_id.in_(sahipler), Soru.durum == "onayli", Soru.cevap_bicimi == "coktan_secmeli").order_by(Soru.id)
    for s in vt.scalars(q):
        m = soru_mkleri(s)
        if len(m) == 1 and m[0] in sonuc and s.secenekler:
            sonuc[m[0]].append(s)
    return sonuc


def _ataları(k: str, on: dict[str, set[str]]) -> set[str]:
    """k'nin kapsam içindeki bütün ön koşulları (zincir)."""
    out, yigin = set(), list(on.get(k, ()))
    while yigin:
        x = yigin.pop()
        if x not in out:
            out.add(x)
            yigin.extend(on.get(x, ()))
    return out


def dina(p: dict[str, float], mkler: list[str], dogru: bool, g: float, s: float = S) -> dict[str, float]:
    """Sorunun MK'lerinin yeni olasılıkları (birlikte dağılım üzerinden; MK'ler başta bağımsız)."""
    toplam, pay = 0.0, {m: 0.0 for m in mkler}
    for durumlar in product((True, False), repeat=len(mkler)):
        onsel = 1.0
        for m, b in zip(mkler, durumlar):
            onsel *= p[m] if b else 1 - p[m]
        p_dogru = (1 - s) if all(durumlar) else g
        olabilirlik = onsel * (p_dogru if dogru else 1 - p_dogru)
        toplam += olabilirlik
        for m, b in zip(mkler, durumlar):
            if b:
                pay[m] += olabilirlik
    return {m: pay[m] / toplam for m in mkler}


@dataclass
class Durum:
    mkler: list[str]
    on: dict[str, set[str]]
    p: dict[str, float]
    soru_sayisi: dict[str, int] = field(default_factory=dict)  # bu testte MK başına sorulan
    cikarim: dict[str, str] = field(default_factory=dict)  # MK → biliyor (ön koşul zincirinden çıkarım)

    def karar(self, m: str) -> str:
        if m in self.cikarim:
            return self.cikarim[m]
        return karar(self.p[m])

    def dogrudan_karar(self, m: str) -> str | None:
        d = karar(self.p[m])
        return d if d in ("biliyor", "bilmiyor") else None

    def onkosulu_eksik(self, m: str) -> bool:
        return any(self.dogrudan_karar(a) == "bilmiyor" for a in _ataları(m, self.on))

    def cikarimlari_yenile(self) -> None:
        self.cikarim = {}
        for m in self.mkler:
            if self.dogrudan_karar(m) == "biliyor":
                for a in _ataları(m, self.on):
                    if self.dogrudan_karar(a) is None:
                        self.cikarim[a] = "biliyor"

    def kokler(self) -> list[str]:
        return [m for m in self.mkler if self.dogrudan_karar(m) == "bilmiyor" and not self.onkosulu_eksik(m)]


def baslangic(vt: Session, o: UyarlamaliOturum) -> Durum:
    mkler, on = kapsam(vt, o.kazanim)
    p = {m: P0 for m in mkler}
    if o.kullanici.rol == "ogrenci":  # sınavlardan gelen kanıt
        for m, k in mk_kanitlari(vt, onayli_teslimler(vt, o.kullanici_id)).items():
            if m in p and k.p is not None:
                p[m] = k.p
    return Durum(mkler, on, p)


def yeniden_oynat(vt: Session, o: UyarlamaliOturum) -> Durum:
    d = baslangic(vt, o)
    for c in o.cevaplar:
        if c.secilen is None:
            continue
        ms = [m for m in soru_mkleri(c.soru) if m in d.p] or [c.mk_kod]
        d.p.update(dina(d.p, ms, bool(c.dogru), g=1 / max(2, len(c.soru.secenekler))))
        d.soru_sayisi[c.mk_kod] = d.soru_sayisi.get(c.mk_kod, 0) + 1
    d.cikarimlari_yenile()
    return d


def sonraki(d: Durum, o: UyarlamaliOturum, h: dict[str, list[Soru]]) -> tuple[str, Soru] | None:
    """Sıradaki (MK, soru) ya da test bittiyse None."""
    if sum(1 for c in o.cevaplar if c.secilen is not None) >= MAKS_TOPLAM:
        return None
    sorulan = {c.soru_id for c in o.cevaplar}

    def soru(m: str) -> Soru | None:
        if d.soru_sayisi.get(m, 0) >= MAKS_MK:
            return None
        return next((q for q in h.get(m, []) if q.id not in sorulan), None)

    adaylar = [m for m in d.mkler if d.karar(m) not in ("biliyor", "bilmiyor") and soru(m)]
    if not adaylar:
        return None
    son_mk = next((c.mk_kod for c in reversed(o.cevaplar) if c.secilen is not None), None)
    basladi = [m for m in adaylar if d.soru_sayisi.get(m)]
    if basladi:  # (1) yarım kalan MK: önce son sorulan
        m = son_mk if son_mk in basladi else basladi[0]
        return m, soru(m)
    bilinmeyenler = [m for m in d.mkler if d.dogrudan_karar(m) == "bilmiyor"]
    for b in bilinmeyenler:  # (2) kök arama: bilinmeyenin kararsız ön koşulu
        for a in sorted(d.on.get(b, ()), key=lambda x: -len(_ataları(x, d.on))):
            if a in adaylar:
                return a, soru(a)
    # (3) zincirin en üstü: kapsam içinde en çok ön koşulu olan, eşitse kanıtı en belirsiz olan
    m = max(adaylar, key=lambda x: (len(_ataları(x, d.on)), -abs(d.p[x] - 0.5), x))
    return m, soru(m)
