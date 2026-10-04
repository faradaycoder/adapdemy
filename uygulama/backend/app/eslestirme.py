"""Soru–MK eşleme kuralları, soru zorluğu ve rubrik payları (ALGORITMA.md bölüm 5).

Girdi: rubrik adımları ve her adımın MK'si (yapay zekâ ya da öğretmen verir).
Çıktı:
- Sorunun MK'leri: adımların MK'lerinden en üsttekiler. Bir MK, başka bir adım MK'sinin doğrudan ya da
  dolaylı öncülüyse sorunun MK'si olmaz; o adım yalnız teşhis içindir (5.1).
- Soru zorluğu: b = Σ Z(sorunun MK'leri) (5.2). Ölçekleme yok.
- Rubrik payları (5.3): her adım, öncülü olduğu üst MK'nin grubuna girer (birden çok üst MK'nin öncülüyse
  ilkine). Grup içinde ağırlık v(MK)²'dir (aynı MK'yi kullanan adımlar bu ağırlığı paylaşır); grubun toplam
  payı Z(üst MK) / b'dir. Böylece tek üst MK'li soruda paylar v²/Z² oranına, çok üst MK'li soruda Z oranına uyar.
- Uyarılar: kodu bilinmeyen MK, farklı dersten MK.
"""

from dataclasses import dataclass, field
from functools import lru_cache

from sqlalchemy import select
from sqlalchemy.orm import Session

from .modeller import MK, MKOnKosul


@dataclass
class Adim:
    aciklama: str
    mk_kod: str
    pay: float = 0.0


@dataclass
class EslemeSonucu:
    soru_mkleri: list[str]
    zorluk: float | None
    adimlar: list[Adim]
    uyarilar: list[str] = field(default_factory=list)


class Harita:
    """Veritabanındaki MK haritasının bellekteki kopyası (öncül aramaları için)."""

    def __init__(self, vt: Session):
        self.mk = {m.kod: m for m in vt.scalars(select(MK))}
        self.on: dict[str, list[str]] = {}
        for b in vt.scalars(select(MKOnKosul)):
            self.on.setdefault(b.mk_kod, []).append(b.on_kosul_kod)
        self._oncul = lru_cache(maxsize=None)(self._oncul_hesapla)

    def _oncul_hesapla(self, kod: str) -> frozenset[str]:
        sonuc: set[str] = set()
        yigin = list(self.on.get(kod, []))
        while yigin:
            p = yigin.pop()
            if p not in sonuc:
                sonuc.add(p)
                yigin.extend(self.on.get(p, []))
        return frozenset(sonuc)

    def oncul(self, kod: str) -> frozenset[str]:
        """kod'un doğrudan ve dolaylı bütün ön koşulları."""
        return self._oncul(kod)


def esle(harita: Harita, adimlar: list[Adim], ders: str | None = None) -> EslemeSonucu:
    uyarilar = []
    gecerli = []
    for a in adimlar:
        m = harita.mk.get(a.mk_kod)
        if not m:
            uyarilar.append(f"{a.mk_kod}: bu kodla bir MK yok.")
            continue
        if m.durum == "iptal":
            uyarilar.append(f"{a.mk_kod}: kullanımdan kalkmış (iptal) bir MK.")
        if ders and m.ders != ders:
            uyarilar.append(f"{a.mk_kod}: sorunun dersi {ders}, bu MK {m.ders} dersinden.")
        gecerli.append(a)

    kodlar = list(dict.fromkeys(a.mk_kod for a in gecerli))  # sırayı koruyarak tekil
    ust = [k for k in kodlar if not any(k in harita.oncul(o) for o in kodlar if o != k)]
    if not ust:
        return EslemeSonucu([], None, adimlar, uyarilar or ["Adımlara MK eşlenmemiş."])

    z = {k: harita.mk[k].zorluk or 0.0 for k in ust}
    b = round(sum(z.values()), 2)

    # her adımı bir üst MK grubuna koy
    grup: dict[str, list[Adim]] = {k: [] for k in ust}
    for a in gecerli:
        hedef = a.mk_kod if a.mk_kod in grup else next(k for k in ust if a.mk_kod in harita.oncul(k))
        grup[hedef].append(a)

    for k, ad in grup.items():
        sayac: dict[str, int] = {}
        for a in ad:
            sayac[a.mk_kod] = sayac.get(a.mk_kod, 0) + 1
        agirlik = {a_kod: (harita.mk[a_kod].v or 0.0) ** 2 for a_kod in sayac}
        toplam = sum(agirlik.values()) or 1.0
        grup_payi = z[k] / b if b else 1.0 / len(ust)
        for a in ad:
            a.pay = round(grup_payi * agirlik[a.mk_kod] / toplam / sayac[a.mk_kod], 4)

    gecerli_id = {id(a) for a in gecerli}
    for a in adimlar:
        if id(a) not in gecerli_id:
            a.pay = 0.0
    return EslemeSonucu(ust, b, adimlar, uyarilar)
