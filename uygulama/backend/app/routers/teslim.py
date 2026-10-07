"""Teslim: öğrencinin sınavı çözmesi (online cevap, soru başına fotoğraf/tarama) ve öğretmenin teslimleri görmesi.

Kurallar:
- Öğrenci yalnız üyesi olduğu sınıfa atanmış ve şu an açık olan sınavı çözebilir.
- Süre (sure_dk) varsa öğrencinin ilk açtığı andan başlar; süre ya da atamanın bitişi dolunca cevap kaydedilmez.
- Süre dolunca sınav kendiliğinden teslim edilir (öğrenci "teslim et"e basmasa da); atamanın bitişine kadar hiç açmayan
  öğrenci için boş kâğıt teslim edilir. Öğretmene "teslim etti" bildirimi gider.
- Kendiliğinden teslim edilen sınav için öğrenci süre uzatma ister; öğretmen ek süre (dakika) verir ya da reddeder.
  Verilirse sınav yeniden açılır ve öğrenci kaldığı yerden devam eder; reddedilirse teslim olduğu gibi kalır.
- Teslim edilen sınavda cevap değiştirilemez.
- Doğru cevap ve çözüm öğrenciye gönderilmez.
"""

import base64
import binascii
from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..kimlik import rol_gerekli
from ..modeller import Atama, Cevap, CevapDosya, Kullanici, SinifUye, Teslim, TeslimDosya
from ..degerlendirme import otomatik
from ..vt import vt_oturumu
from .sinavlar import YazdirC, YazdirOgrenci, YazdirSoru, _durum, _utc
from .sorular import _gorsel_kaydet

router = APIRouter(prefix="/api/teslim", tags=["teslim"])
ogretmen_router = APIRouter(prefix="/api/atamalar", tags=["teslim"])
ogrenci = rol_gerekli("ogrenci")
ogretmen = rol_gerekli("ogretmen")


# ---------- şemalar ----------

class DosyaC(BaseModel):
    id: int
    dosya: str
    kaynak: str = "ogrenci"


class CevapC(BaseModel):
    soru_id: int
    secilen: str | None
    metin: str
    dosyalar: list[DosyaC]


class SinavSorusuC(BaseModel):
    sira: int
    soru_id: int
    metin: str
    gorsel: str | None
    cevap_bicimi: str
    secenekler: list[dict]


class OturumC(BaseModel):
    atama_id: int
    sinav_adi: str
    ders: str
    aciklama: str
    sure_dk: int | None
    bitis: datetime  # sürenin ve atamanın bitişinden erken olanı
    durum: str  # devam / teslim / kapali
    sorular: list[SinavSorusuC]
    cevaplar: list[CevapC]
    genel_dosyalar: list[DosyaC] = []  # sınavın tamamı için yüklenenler
    otomatik_teslim: bool = False  # süre dolunca kendiliğinden teslim edildi
    uzatma: str | None = None  # bekliyor / verildi / reddedildi
    uzatma_dk: int | None = None


class UzatmaTalepG(BaseModel):
    aciklama: str = Field("", max_length=500)


class UzatmaKararG(BaseModel):
    karar: str = Field(pattern="^(ver|reddet)$")
    dk: int | None = Field(None, ge=1, le=1440)


class CevapG(BaseModel):
    secilen: str | None = Field(None, max_length=2)
    metin: str = ""


class DosyaG(BaseModel):
    dosya_base64: str


class TeslimSatir(BaseModel):
    teslim_id: int | None
    ogrenci_id: int
    ogrenci: str
    durum: str  # baslamadi / devam / teslim
    cevaplanan: int
    soru_sayisi: int
    teslim_zamani: datetime | None
    degerlendirme: str | None = None  # bekliyor / onayli
    genel_dosya: int = 0  # sınavın tamamı için yüklenen dosya sayısı
    puan: float | None = None
    en_yuksek: float | None = None
    otomatik_teslim: bool = False
    uzatma: str | None = None
    uzatma_notu: str = ""
    uzatma_zamani: datetime | None = None
    uzatma_dk: int | None = None


class TeslimAyrinti(BaseModel):
    teslim_id: int
    ogrenci: str
    durum: str
    teslim_zamani: datetime | None
    sorular: list[SinavSorusuC]
    cevaplar: list[CevapC]
    genel_dosyalar: list[DosyaC] = []


# ---------- yardımcılar ----------

def _atama_ogrenci(vt: Session, atama_id: int, k: Kullanici) -> Atama:
    a = vt.get(Atama, atama_id)
    if not a or not vt.scalar(select(SinifUye).where(SinifUye.sinif_id == a.sinif_id, SinifUye.ogrenci_id == k.id)):
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Sınav bulunamadı.")
    return a


def _bitis(a: Atama, t: Teslim) -> datetime:
    if t.uzatma == "verildi" and t.uzatma_bitis:
        return _utc(t.uzatma_bitis)
    son = _utc(a.bitis)
    if a.sinav.sure_dk:
        son = min(son, _utc(t.baslama) + timedelta(minutes=a.sinav.sure_dk))
    return son


def _sorular(a: Atama) -> list[SinavSorusuC]:
    return [SinavSorusuC(sira=x.sira, soru_id=x.soru.id, metin=x.soru.metin, gorsel=x.soru.gorsel, cevap_bicimi=x.soru.cevap_bicimi,
                         secenekler=[{"harf": c.harf, "metin": c.metin} for c in x.soru.secenekler]) for x in a.sinav.sorular]


def _cevaplar(t: Teslim) -> list[CevapC]:
    return [CevapC(soru_id=c.soru_id, secilen=c.secilen, metin=c.metin, dosyalar=[DosyaC(id=d.id, dosya=d.dosya, kaynak=d.kaynak) for d in c.dosyalar])
            for c in t.cevaplar]


def _teslim_et(vt: Session, a: Atama, t: Teslim, zaman: datetime, otomatik_mi: bool = False) -> None:
    t.durum, t.teslim_zamani, t.otomatik_teslim, t.ogretmen_gordu = "teslim", zaman, otomatik_mi, False
    sorular = {x.soru_id: x.soru for x in a.sinav.sorular}
    for c in t.cevaplar:  # çoktan seçmeliler teslimde otomatik değerlendirilir
        otomatik(vt, c, sorular[c.soru_id])


def sure_dolanlari_teslim_et(vt: Session) -> int:
    """Süresi dolan açık oturumları teslim eder; bitmiş atamada hiç başlamamış (atama bitmeden sınıfa katılmış)
    öğrenciler için boş teslim oluşturur. Bildirim ve listeler okunmadan önce çağrılır. Teslim edilen sayısını döndürür."""
    simdi, n = datetime.now(timezone.utc), 0
    for t in vt.scalars(select(Teslim).where(Teslim.durum == "devam")).all():
        son = _bitis(t.atama, t)
        if simdi > son:
            _teslim_et(vt, t.atama, t, son, otomatik_mi=True)
            n += 1
    for a in vt.scalars(select(Atama).where(Atama.bitis < simdi)).all():
        if not _utc(a.bitis) < simdi:  # SQLite saat dilimini saklamaz; kesin karşılaştırma
            continue
        var = set(vt.scalars(select(Teslim.ogrenci_id).where(Teslim.atama_id == a.id)))
        for u in a.sinif.uyeler:
            if u.ogrenci_id not in var and _utc(u.katilma) < _utc(a.bitis):
                t = Teslim(atama_id=a.id, ogrenci_id=u.ogrenci_id, baslama=_utc(a.bitis))
                vt.add(t)
                vt.flush()
                _teslim_et(vt, a, t, _utc(a.bitis), otomatik_mi=True)
                n += 1
    if n:
        vt.commit()
    return n


def _oturum(a: Atama, t: Teslim) -> OturumC:
    bitis = _bitis(a, t)
    durum = t.durum if t.durum == "teslim" or datetime.now(timezone.utc) <= bitis else "kapali"
    return OturumC(atama_id=a.id, sinav_adi=a.sinav.ad, ders=a.sinav.ders, aciklama=a.sinav.aciklama, sure_dk=a.sinav.sure_dk,
                   bitis=bitis, durum=durum, sorular=_sorular(a), cevaplar=_cevaplar(t),
                   genel_dosyalar=[DosyaC(id=d.id, dosya=d.dosya) for d in t.genel_dosyalar],
                   otomatik_teslim=t.otomatik_teslim, uzatma=t.uzatma, uzatma_dk=t.uzatma_dk)


def _yazilabilir(vt: Session, atama_id: int, k: Kullanici) -> tuple[Atama, Teslim]:
    a = _atama_ogrenci(vt, atama_id, k)
    t = vt.scalar(select(Teslim).where(Teslim.atama_id == a.id, Teslim.ogrenci_id == k.id))
    if not t:
        raise HTTPException(status.HTTP_409_CONFLICT, "Önce sınavı başlat.")
    if t.durum == "teslim":
        raise HTTPException(status.HTTP_409_CONFLICT, "Sınav teslim edildi; cevaplar değiştirilemez.")
    if datetime.now(timezone.utc) > _bitis(a, t):
        raise HTTPException(status.HTTP_409_CONFLICT, "Sınav süresi doldu.")
    return a, t


def _cevap(vt: Session, t: Teslim, soru_id: int, a: Atama) -> Cevap:
    if soru_id not in {x.soru_id for x in a.sinav.sorular}:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Bu soru sınavda yok.")
    c = next((c for c in t.cevaplar if c.soru_id == soru_id), None)
    if not c:
        c = Cevap(soru_id=soru_id)
        t.cevaplar.append(c)
        vt.flush()
    return c


# ---------- öğrenci ----------

@router.post("/{atama_id}/basla", response_model=OturumC)
def basla(atama_id: int, k: Kullanici = Depends(ogrenci), vt: Session = Depends(vt_oturumu)):
    """Sınavı açar (ilk açılışta süre başlar) ve soruları ile kayıtlı cevapları döndürür."""
    a = _atama_ogrenci(vt, atama_id, k)
    sure_dolanlari_teslim_et(vt)
    t = vt.scalar(select(Teslim).where(Teslim.atama_id == a.id, Teslim.ogrenci_id == k.id))
    if not t:
        if _durum(a) != "acik":
            raise HTTPException(status.HTTP_409_CONFLICT, "Sınav şu an açık değil.")
        t = Teslim(atama_id=a.id, ogrenci_id=k.id)
        vt.add(t)
        vt.commit()
    if not t.uzatma_ogrenci_gordu:  # uzatma kararını gördü
        t.uzatma_ogrenci_gordu = True
        vt.commit()
    return _oturum(a, t)


@router.get("/{atama_id}/yazdir", response_model=YazdirC)
def yazdir(atama_id: int, k: Kullanici = Depends(ogrenci), vt: Session = Depends(vt_oturumu)):
    """Öğrencinin kendi kopyası (QR'ları ona özel), kâğıtta çözüp tarayarak yüklemek için. Sınav başlamış olmalı:
    yazdırma ekranı önce /basla'yı çağırır, böylece süre kâğıtta çözerken de işler. Doğru cevap ve çözüm gönderilmez."""
    a = _atama_ogrenci(vt, atama_id, k)
    t = vt.scalar(select(Teslim).where(Teslim.atama_id == a.id, Teslim.ogrenci_id == k.id))
    if not t:
        raise HTTPException(status.HTTP_409_CONFLICT, "Önce sınavı başlat.")
    s = a.sinav
    return YazdirC(
        sinav_id=s.id, ad=s.ad, ders=s.ders, sinif_duzeyi=s.sinif_duzeyi, aciklama=s.aciklama, sure_dk=s.sure_dk,
        atama_id=a.id, sinif_adi=a.sinif.ad,
        sorular=[YazdirSoru(sira=x.sira, soru_id=x.soru.id, metin=x.soru.metin, gorsel=x.soru.gorsel, cevap_bicimi=x.soru.cevap_bicimi,
                            secenekler=[{"harf": c.harf, "metin": c.metin} for c in x.soru.secenekler]) for x in s.sorular],
        ogrenciler=[YazdirOgrenci(id=k.id, ad=k.ad)],
    )


@router.put("/{atama_id}/cevap/{soru_id}", response_model=CevapC)
def cevapla(atama_id: int, soru_id: int, g: CevapG, k: Kullanici = Depends(ogrenci), vt: Session = Depends(vt_oturumu)):
    a, t = _yazilabilir(vt, atama_id, k)
    c = _cevap(vt, t, soru_id, a)
    c.secilen, c.metin = (g.secilen or None), g.metin
    vt.commit()
    return CevapC(soru_id=c.soru_id, secilen=c.secilen, metin=c.metin, dosyalar=[DosyaC(id=d.id, dosya=d.dosya) for d in c.dosyalar])


@router.post("/{atama_id}/cevap/{soru_id}/dosya", response_model=CevapC)
def dosya_ekle(atama_id: int, soru_id: int, g: DosyaG, k: Kullanici = Depends(ogrenci), vt: Session = Depends(vt_oturumu)):
    a, t = _yazilabilir(vt, atama_id, k)
    try:
        veri = base64.b64decode(g.dosya_base64.split(",")[-1], validate=True)
    except (binascii.Error, ValueError):
        raise HTTPException(422, "Dosya okunamadı.")
    c = _cevap(vt, t, soru_id, a)
    if len(c.dosyalar) >= 6:
        raise HTTPException(422, "Bir soruya en fazla 6 parça yüklenebilir.")
    c.dosyalar.append(CevapDosya(dosya=_gorsel_kaydet(veri)))
    vt.commit()
    return CevapC(soru_id=c.soru_id, secilen=c.secilen, metin=c.metin, dosyalar=[DosyaC(id=d.id, dosya=d.dosya) for d in c.dosyalar])


@router.delete("/{atama_id}/cevap/{soru_id}/dosya/{dosya_id}", status_code=status.HTTP_204_NO_CONTENT)
def dosya_sil(atama_id: int, soru_id: int, dosya_id: int, k: Kullanici = Depends(ogrenci), vt: Session = Depends(vt_oturumu)):
    a, t = _yazilabilir(vt, atama_id, k)
    c = _cevap(vt, t, soru_id, a)
    d = next((d for d in c.dosyalar if d.id == dosya_id), None)
    if not d:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Dosya bulunamadı.")
    c.dosyalar.remove(d)
    vt.commit()


@router.post("/{atama_id}/dosya", response_model=OturumC)
def genel_dosya_ekle(atama_id: int, g: DosyaG, k: Kullanici = Depends(ogrenci), vt: Session = Depends(vt_oturumu)):
    """Sınavın tamamı için dosya (tek PDF ya da sayfa fotoğrafı). En fazla 20 parça."""
    a, t = _yazilabilir(vt, atama_id, k)
    try:
        veri = base64.b64decode(g.dosya_base64.split(",")[-1], validate=True)
    except (binascii.Error, ValueError):
        raise HTTPException(422, "Dosya okunamadı.")
    if len(t.genel_dosyalar) >= 20:
        raise HTTPException(422, "Sınavın tamamı için en fazla 20 dosya yüklenebilir.")
    t.genel_dosyalar.append(TeslimDosya(dosya=_gorsel_kaydet(veri)))
    vt.commit()
    return basla(atama_id, k, vt)


@router.delete("/{atama_id}/dosya/{dosya_id}", response_model=OturumC)
def genel_dosya_sil(atama_id: int, dosya_id: int, k: Kullanici = Depends(ogrenci), vt: Session = Depends(vt_oturumu)):
    a, t = _yazilabilir(vt, atama_id, k)
    d = next((d for d in t.genel_dosyalar if d.id == dosya_id), None)
    if not d:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Dosya bulunamadı.")
    t.genel_dosyalar.remove(d)
    vt.commit()
    return basla(atama_id, k, vt)


@router.post("/{atama_id}/gonder", response_model=OturumC)
def gonder(atama_id: int, k: Kullanici = Depends(ogrenci), vt: Session = Depends(vt_oturumu)):
    a = _atama_ogrenci(vt, atama_id, k)
    t = vt.scalar(select(Teslim).where(Teslim.atama_id == a.id, Teslim.ogrenci_id == k.id))
    if not t:
        raise HTTPException(status.HTTP_409_CONFLICT, "Önce sınavı başlat.")
    if t.durum != "teslim":  # süre dolduktan sonra da teslim edilebilir; cevaplar zaten kilitli
        _teslim_et(vt, a, t, datetime.now(timezone.utc))
        vt.commit()
    return basla(atama_id, k, vt)


@router.post("/{atama_id}/uzatma", response_model=OturumC)
def uzatma_iste(atama_id: int, g: UzatmaTalepG, k: Kullanici = Depends(ogrenci), vt: Session = Depends(vt_oturumu)):
    """Süre dolunca kendiliğinden teslim edilen sınav için ek süre ister; öğretmene bildirim gider."""
    a = _atama_ogrenci(vt, atama_id, k)
    sure_dolanlari_teslim_et(vt)
    t = vt.scalar(select(Teslim).where(Teslim.atama_id == a.id, Teslim.ogrenci_id == k.id))
    if not t or t.durum != "teslim" or not t.otomatik_teslim:
        raise HTTPException(status.HTTP_409_CONFLICT, "Uzatma yalnız süresi dolan sınav için istenir.")
    if t.degerlendirme == "onayli":
        raise HTTPException(status.HTTP_409_CONFLICT, "Sınav değerlendirildi; uzatma istenemez.")
    if t.uzatma == "bekliyor":
        raise HTTPException(status.HTTP_409_CONFLICT, "Talebin öğretmeninde; kararı bekleniyor.")
    if t.uzatma == "reddedildi":
        raise HTTPException(status.HTTP_409_CONFLICT, "Öğretmenin uzatma talebini kabul etmedi; sınav teslim edildi.")
    t.uzatma, t.uzatma_notu, t.uzatma_zamani, t.uzatma_ogrenci_gordu = "bekliyor", g.aciklama.strip(), datetime.now(timezone.utc), True
    vt.commit()
    return _oturum(a, t)


# ---------- öğretmen ----------

def _atama_ogretmen(vt: Session, atama_id: int, k: Kullanici) -> Atama:
    a = vt.get(Atama, atama_id)
    if not a or a.sinav.olusturan_id != k.id:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Atama bulunamadı.")
    return a


@ogretmen_router.get("/{atama_id}/teslimler", response_model=list[TeslimSatir])
def teslimler(atama_id: int, k: Kullanici = Depends(ogretmen), vt: Session = Depends(vt_oturumu)):
    a = _atama_ogretmen(vt, atama_id, k)
    sure_dolanlari_teslim_et(vt)
    ts = {t.ogrenci_id: t for t in vt.scalars(select(Teslim).where(Teslim.atama_id == a.id))}
    n = len(a.sinav.sorular)
    satirlar = []
    for u in a.sinif.uyeler:
        t = ts.get(u.ogrenci_id)
        cev = sum(1 for c in t.cevaplar if c.secilen or c.metin.strip() or c.dosyalar) if t else 0
        satirlar.append(TeslimSatir(teslim_id=t.id if t else None, ogrenci_id=u.ogrenci_id, ogrenci=u.ogrenci.ad,
                                    durum=t.durum if t else "baslamadi", cevaplanan=cev, soru_sayisi=n,
                                    teslim_zamani=t.teslim_zamani if t else None,
                                    degerlendirme=t.degerlendirme if t and t.durum == "teslim" else None,
                                    puan=t.puan if t else None, en_yuksek=t.en_yuksek if t else None,
                                    genel_dosya=len(t.genel_dosyalar) if t else 0,
                                    otomatik_teslim=bool(t and t.otomatik_teslim), uzatma=t.uzatma if t else None,
                                    uzatma_notu=t.uzatma_notu if t else "", uzatma_zamani=t.uzatma_zamani if t else None,
                                    uzatma_dk=t.uzatma_dk if t else None))
    return satirlar


@ogretmen_router.post("/{atama_id}/teslimler/{teslim_id}/uzatma", response_model=list[TeslimSatir])
def uzatma_karar(atama_id: int, teslim_id: int, g: UzatmaKararG, k: Kullanici = Depends(ogretmen), vt: Session = Depends(vt_oturumu)):
    """Öğrencinin uzatma talebine karar: 'ver' (dk dakika, şu andan başlar; sınav yeniden açılır) ya da 'reddet'."""
    a = _atama_ogretmen(vt, atama_id, k)
    t = vt.get(Teslim, teslim_id)
    if not t or t.atama_id != a.id:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Teslim bulunamadı.")
    if t.uzatma != "bekliyor":
        raise HTTPException(status.HTTP_409_CONFLICT, "Bekleyen uzatma talebi yok.")
    simdi = datetime.now(timezone.utc)
    if g.karar == "ver":
        if not g.dk:
            raise HTTPException(422, "Ek süreyi dakika olarak gir.")
        t.uzatma, t.uzatma_dk, t.uzatma_bitis = "verildi", g.dk, simdi + timedelta(minutes=g.dk)
        t.durum, t.teslim_zamani, t.otomatik_teslim, t.ogretmen_gordu = "devam", None, False, True
    else:
        t.uzatma = "reddedildi"
    t.uzatma_zamani, t.uzatma_ogrenci_gordu = simdi, False
    vt.commit()
    return teslimler(atama_id, k, vt)


@ogretmen_router.get("/{atama_id}/teslimler/{teslim_id}", response_model=TeslimAyrinti)
def teslim_ayrinti(atama_id: int, teslim_id: int, k: Kullanici = Depends(ogretmen), vt: Session = Depends(vt_oturumu)):
    a = _atama_ogretmen(vt, atama_id, k)
    t = vt.get(Teslim, teslim_id)
    if not t or t.atama_id != a.id:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Teslim bulunamadı.")
    if t.durum == "teslim" and not t.ogretmen_gordu:
        t.ogretmen_gordu = True
        vt.commit()
    return TeslimAyrinti(teslim_id=t.id, ogrenci=t.ogrenci.ad, durum=t.durum, teslim_zamani=t.teslim_zamani,
                         sorular=_sorular(a), cevaplar=_cevaplar(t),
                         genel_dosyalar=[DosyaC(id=d.id, dosya=d.dosya) for d in t.genel_dosyalar])
