"""Teslim: öğrencinin sınavı çözmesi (online cevap, soru başına fotoğraf/tarama) ve öğretmenin teslimleri görmesi.

Kurallar:
- Öğrenci yalnız üyesi olduğu sınıfa atanmış ve şu an açık olan sınavı çözebilir.
- Süre (sure_dk) varsa öğrencinin ilk açtığı andan başlar; süre ya da atamanın bitişi dolunca cevap kaydedilmez.
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
    t = vt.scalar(select(Teslim).where(Teslim.atama_id == a.id, Teslim.ogrenci_id == k.id))
    if not t:
        if _durum(a) != "acik":
            raise HTTPException(status.HTTP_409_CONFLICT, "Sınav şu an açık değil.")
        t = Teslim(atama_id=a.id, ogrenci_id=k.id)
        vt.add(t)
        vt.commit()
    bitis = _bitis(a, t)
    durum = t.durum if t.durum == "teslim" or datetime.now(timezone.utc) <= bitis else "kapali"
    return OturumC(atama_id=a.id, sinav_adi=a.sinav.ad, ders=a.sinav.ders, aciklama=a.sinav.aciklama, sure_dk=a.sinav.sure_dk,
                   bitis=bitis, durum=durum, sorular=_sorular(a), cevaplar=_cevaplar(t),
                   genel_dosyalar=[DosyaC(id=d.id, dosya=d.dosya) for d in t.genel_dosyalar])


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
        t.durum, t.teslim_zamani = "teslim", datetime.now(timezone.utc)
        sorular = {x.soru_id: x.soru for x in a.sinav.sorular}
        for c in t.cevaplar:  # çoktan seçmeliler teslimde otomatik değerlendirilir
            otomatik(vt, c, sorular[c.soru_id])
        vt.commit()
    return basla(atama_id, k, vt)


# ---------- öğretmen ----------

def _atama_ogretmen(vt: Session, atama_id: int, k: Kullanici) -> Atama:
    a = vt.get(Atama, atama_id)
    if not a or a.sinav.olusturan_id != k.id:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Atama bulunamadı.")
    return a


@ogretmen_router.get("/{atama_id}/teslimler", response_model=list[TeslimSatir])
def teslimler(atama_id: int, k: Kullanici = Depends(ogretmen), vt: Session = Depends(vt_oturumu)):
    a = _atama_ogretmen(vt, atama_id, k)
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
                                    genel_dosya=len(t.genel_dosyalar) if t else 0))
    return satirlar


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
