"""Cevapların rubrik adımlarına göre değerlendirilmesi (ALGORITMA.md 5.3 ve 6.1).

Puan: her rubrik adımı, sorunun zorluğunun (b) pay kadarıdır. Adım 'biliyor' ise puanı kazanılır.
Adım durumu üç değerlidir:
- biliyor: adım doğru yapılmış
- bilmiyor: adım denenmiş ama yanlış
- olculemedi: adıma gelinmemiş ya da boş bırakılmış (eksik veri; 'bilmiyor' sayılmaz)

Otomatik değerlendirme (yalnız çoktan seçmeli):
- Boş: bütün adımlar 'olculemedi'.
- Doğru şık: bütün adımlar 'biliyor' (sonuç ancak bütün adımlarla bulunur).
- Yanlış şık: sorunun MK'lerine bağlı adımlar 'bilmiyor', yalnız teşhis için konan ön koşul adımları
  'olculemedi' (yanlış şık hangi ön koşulda koptuğunu söylemez; uyarlamalı test bunları ayrıca yoklar).
  Şıkkın bir yanılgısı varsa cevaba yazılır.
Yazılı ve kâğıt cevaplar: API anahtarı varken yapay zekâ önerir (kaynak 'sistem'), yokken öğretmen değerlendirir.
Öğretmenin verdiği karar ('ogretmen') her zaman son sözdür.
"""

from sqlalchemy.orm import Session

from .modeller import ADIM_DURUMLARI, AdimDegerlendirme, Cevap, Soru

ADIM_DURUMLARI_GECERLI = set(ADIM_DURUMLARI)


def adim_puani(soru: Soru, pay: float, durum: str) -> float:
    return round((soru.zorluk or 0) * pay, 4) if durum == "biliyor" else 0.0


def otomatik(vt: Session, c: Cevap, soru: Soru) -> bool:
    """Çoktan seçmeli cevabı değerlendirir. Öğretmenin el koyduğu cevaba dokunmaz. Değerlendirdiyse True."""
    if soru.cevap_bicimi != "coktan_secmeli" or any(a.kaynak == "ogretmen" for a in c.adimlar):
        return False
    dogru = next((s for s in soru.secenekler if s.dogru), None)
    secilen = next((s for s in soru.secenekler if s.harf == c.secilen), None)
    ust = {m.mk_kod for m in soru.mkler}
    sonuc = []
    for adim in soru.adimlar:
        if not c.secilen:
            durum, gerekce = "olculemedi", "Boş bırakıldı."
        elif dogru and c.secilen == dogru.harf:
            durum, gerekce = "biliyor", f"Doğru şık ({c.secilen})."
        elif adim.mk_kod in ust:
            durum, gerekce = "bilmiyor", f"Yanlış şık ({c.secilen}); doğrusu {dogru.harf if dogru else '?'}."
        else:
            durum, gerekce = "olculemedi", "Yanlış şıktan bu ön koşul adımı hakkında karar verilemez."
        sonuc.append(AdimDegerlendirme(rubrik_adim_id=adim.id, durum=durum, puan=adim_puani(soru, adim.pay, durum),
                                       kaynak="otomatik", gerekce=gerekce))
    c.adimlar.clear()
    vt.flush()
    c.adimlar = sonuc
    c.yanilgi_kod = secilen.yanilgi_kod if secilen and not secilen.dogru else None
    return True


def ogretmen(vt: Session, c: Cevap, soru: Soru, kararlar: dict[int, str], gerekceler: dict[int, str] | None = None,
             kaynak: str = "ogretmen") -> None:
    """Adım kararlarını yazar (öğretmen ya da 'sistem' önerisi). Karar verilmeyen adımlar eski hâlinde kalır.
    Sistem önerisi öğretmenin verdiği bir kararın üstüne yazılmaz."""
    gerekceler = gerekceler or {}
    var = {a.rubrik_adim_id: a for a in c.adimlar}
    for adim in soru.adimlar:
        if adim.id not in kararlar:
            continue
        durum = kararlar[adim.id]
        a = var.get(adim.id)
        if a and kaynak == "sistem" and a.kaynak == "ogretmen":
            continue
        if not a:
            a = AdimDegerlendirme(rubrik_adim_id=adim.id, durum=durum, kaynak=kaynak)
            c.adimlar.append(a)
        eski_gerekce = a.gerekce
        a.durum, a.kaynak = durum, kaynak
        a.puan = adim_puani(soru, adim.pay, durum)
        a.gerekce = gerekceler.get(adim.id, eski_gerekce)


def cevap_puani(c: Cevap | None) -> float:
    return round(sum(a.puan for a in c.adimlar), 2) if c else 0.0


def degerlendirilmis_mi(c: Cevap | None, soru: Soru) -> bool:
    """Bütün rubrik adımlarının bir kararı var mı?"""
    if not c:
        return False
    return {a.rubrik_adim_id for a in c.adimlar} >= {a.id for a in soru.adimlar}
