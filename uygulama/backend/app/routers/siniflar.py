"""Sınıflar: öğretmen sınıf açar, öğrenci sınıf koduyla katılır."""

import secrets
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..kimlik import gecerli_kullanici, rol_gerekli
from ..modeller import Kullanici, Sinif, SinifUye
from ..vt import vt_oturumu

router = APIRouter(prefix="/api/siniflar", tags=["siniflar"])

# Karıştırılabilecek karakterler (0/O, 1/I/L) kodda yok; kod sesli okunup tahtaya yazılabilir.
_KOD_HARFLER = "ABCDEFGHJKMNPQRSTUVWXYZ23456789"


def _yeni_kod(vt: Session) -> str:
    while True:
        kod = "".join(secrets.choice(_KOD_HARFLER) for _ in range(6))
        if not vt.scalar(select(Sinif).where(Sinif.kod == kod)):
            return kod


class SinifIstek(BaseModel):
    ad: str = Field(min_length=1, max_length=120)
    ders: str = Field(pattern="^(Fizik|Matematik)$")
    sinif_duzeyi: int = Field(ge=5, le=12)


class KatilIstek(BaseModel):
    kod: str = Field(min_length=6, max_length=6)


class UyeCikti(BaseModel):
    id: int
    ad: str
    eposta: str
    katilma: datetime


class SinifCikti(BaseModel):
    id: int
    ad: str
    ders: str
    sinif_duzeyi: int
    kod: str | None  # yalnız öğretmen görür
    ogretmen: str
    ogrenci_sayisi: int


class SinifAyrinti(SinifCikti):
    ogrenciler: list[UyeCikti]


def _cikti(s: Sinif, ogretmen_mi: bool) -> SinifCikti:
    return SinifCikti(id=s.id, ad=s.ad, ders=s.ders, sinif_duzeyi=s.sinif_duzeyi,
                      kod=s.kod if ogretmen_mi else None, ogretmen=s.ogretmen.ad, ogrenci_sayisi=len(s.uyeler))


@router.post("", response_model=SinifCikti, status_code=status.HTTP_201_CREATED)
def sinif_ac(istek: SinifIstek, k: Kullanici = Depends(rol_gerekli("ogretmen")), vt: Session = Depends(vt_oturumu)):
    s = Sinif(ad=istek.ad.strip(), ders=istek.ders, sinif_duzeyi=istek.sinif_duzeyi, kod=_yeni_kod(vt), ogretmen_id=k.id)
    vt.add(s)
    vt.commit()
    vt.refresh(s)
    return _cikti(s, True)


@router.get("", response_model=list[SinifCikti])
def siniflarim(k: Kullanici = Depends(gecerli_kullanici), vt: Session = Depends(vt_oturumu)):
    if k.rol == "ogretmen":
        siniflar = vt.scalars(select(Sinif).where(Sinif.ogretmen_id == k.id).order_by(Sinif.olusturma)).all()
    else:
        siniflar = vt.scalars(select(Sinif).join(SinifUye).where(SinifUye.ogrenci_id == k.id)).all()
    return [_cikti(s, k.rol == "ogretmen") for s in siniflar]


@router.post("/katil", response_model=SinifCikti)
def katil(istek: KatilIstek, k: Kullanici = Depends(rol_gerekli("ogrenci")), vt: Session = Depends(vt_oturumu)):
    s = vt.scalar(select(Sinif).where(Sinif.kod == istek.kod.strip().upper()))
    if not s:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Bu kodla bir sınıf bulunamadı.")
    if not any(u.ogrenci_id == k.id for u in s.uyeler):
        vt.add(SinifUye(sinif_id=s.id, ogrenci_id=k.id))
        vt.commit()
        vt.refresh(s)
    return _cikti(s, False)


@router.get("/{sinif_id}", response_model=SinifAyrinti)
def sinif_ayrinti(sinif_id: int, k: Kullanici = Depends(gecerli_kullanici), vt: Session = Depends(vt_oturumu)):
    s = vt.get(Sinif, sinif_id)
    ogretmen_mi = bool(s) and s.ogretmen_id == k.id
    uye_mi = bool(s) and any(u.ogrenci_id == k.id for u in s.uyeler)
    if not s or not (ogretmen_mi or uye_mi):
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Sınıf bulunamadı.")
    # Öğrenci sınıf arkadaşlarının e-postasını görmez (KVKK: en az veri).
    ogrenciler = [UyeCikti(id=u.ogrenci.id, ad=u.ogrenci.ad, eposta=u.ogrenci.eposta if ogretmen_mi else "",
                           katilma=u.katilma) for u in s.uyeler] if ogretmen_mi else []
    return SinifAyrinti(**_cikti(s, ogretmen_mi).model_dump(), ogrenciler=ogrenciler)
