"""Ana sayfa özeti: öğretmen için sayılar ve değerlendirme bekleyen sınavlar; öğrenci için konu durumu."""

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from ..kimlik import gecerli_kullanici
from ..modeller import Atama, Kullanici, Sinav, Sinif, SinifUye, Soru
from ..rapor import mk_kanitlari, onayli_teslimler
from ..vt import vt_oturumu

router = APIRouter(prefix="/api/ozet", tags=["ozet"])


class BekleyenC(BaseModel):
    atama_id: int
    sinav_adi: str
    sinif_adi: str
    bekleyen: int  # teslim edilmiş, onay bekleyen
    teslim: int
    ogrenci: int


class OzetC(BaseModel):
    sinif: int = 0
    ogrenci: int = 0
    soru_onayli: int = 0
    soru_taslak: int = 0
    sinav: int = 0
    bekleyenler: list[BekleyenC] = []
    mk: dict[str, int] = {}  # öğrenci: biliyor / belirsiz / bilmiyor sayıları


@router.get("", response_model=OzetC)
def ozet(k: Kullanici = Depends(gecerli_kullanici), vt: Session = Depends(vt_oturumu)):
    if k.rol != "ogretmen":
        sayac: dict[str, int] = {"biliyor": 0, "belirsiz": 0, "bilmiyor": 0}
        for x in mk_kanitlari(vt, onayli_teslimler(vt, k.id)).values():
            if x.durum in sayac:
                sayac[x.durum] += 1
        return OzetC(mk=sayac)
    siniflar = vt.scalars(select(Sinif).where(Sinif.ogretmen_id == k.id)).all()
    soru = dict(vt.execute(select(Soru.durum, func.count()).where(Soru.olusturan_id == k.id).group_by(Soru.durum)).all())
    bekleyenler = []
    for a in vt.scalars(select(Atama).join(Sinav).where(Sinav.olusturan_id == k.id).order_by(Atama.bitis.desc())):
        teslim = [t for t in a.teslimler if t.durum == "teslim"]
        b = sum(1 for t in teslim if t.degerlendirme != "onayli")
        if b:
            bekleyenler.append(BekleyenC(atama_id=a.id, sinav_adi=a.sinav.ad, sinif_adi=a.sinif.ad, bekleyen=b,
                                         teslim=len(teslim), ogrenci=len(a.sinif.uyeler)))
    return OzetC(sinif=len(siniflar), ogrenci=vt.scalar(select(func.count(func.distinct(SinifUye.ogrenci_id))).where(
                     SinifUye.sinif_id.in_([s.id for s in siniflar]))) or 0,
                 soru_onayli=soru.get("onayli", 0), soru_taslak=soru.get("taslak", 0),
                 sinav=vt.scalar(select(func.count()).select_from(Sinav).where(Sinav.olusturan_id == k.id)) or 0,
                 bekleyenler=bekleyenler)
