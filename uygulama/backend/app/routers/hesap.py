"""Kayıt, giriş ve oturumdaki kullanıcı.

Google ile giriş B aşamasından önce eklenecek (Google Cloud'da bir OAuth istemcisi gerekiyor).
"""

import re

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field, field_validator
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..kimlik import gecerli_kullanici, jeton_uret, sifre_dogru, sifre_ozetle
from ..modeller import Kullanici
from ..vt import vt_oturumu

router = APIRouter(prefix="/api/hesap", tags=["hesap"])

_EPOSTA = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


class KayitIstek(BaseModel):
    ad: str = Field(min_length=2, max_length=120)
    eposta: str
    sifre: str = Field(min_length=8, max_length=128)
    rol: str = Field(pattern="^(ogretmen|ogrenci)$")  # yönetici kayıtla açılmaz

    @field_validator("eposta")
    @classmethod
    def eposta_gecerli(cls, v: str) -> str:
        v = v.strip().lower()
        if not _EPOSTA.match(v):
            raise ValueError("Geçerli bir e-posta adresi girin.")
        return v


class GirisIstek(BaseModel):
    eposta: str
    sifre: str


class KullaniciCikti(BaseModel):
    id: int
    ad: str
    eposta: str
    rol: str


class JetonCikti(BaseModel):
    jeton: str
    kullanici: KullaniciCikti


def _cikti(k: Kullanici) -> KullaniciCikti:
    return KullaniciCikti(id=k.id, ad=k.ad, eposta=k.eposta, rol=k.rol)


@router.post("/kayit", response_model=JetonCikti, status_code=status.HTTP_201_CREATED)
def kayit(istek: KayitIstek, vt: Session = Depends(vt_oturumu)):
    if vt.scalar(select(Kullanici).where(Kullanici.eposta == istek.eposta)):
        raise HTTPException(status.HTTP_409_CONFLICT, "Bu e-posta adresiyle bir hesap zaten var.")
    k = Kullanici(ad=istek.ad.strip(), eposta=istek.eposta, sifre_hash=sifre_ozetle(istek.sifre), rol=istek.rol)
    vt.add(k)
    vt.commit()
    return JetonCikti(jeton=jeton_uret(k.id), kullanici=_cikti(k))


@router.post("/giris", response_model=JetonCikti)
def giris(istek: GirisIstek, vt: Session = Depends(vt_oturumu)):
    k = vt.scalar(select(Kullanici).where(Kullanici.eposta == istek.eposta.strip().lower()))
    if not k or not k.aktif or not sifre_dogru(istek.sifre, k.sifre_hash):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "E-posta ya da şifre hatalı.")
    return JetonCikti(jeton=jeton_uret(k.id), kullanici=_cikti(k))


@router.get("/ben", response_model=KullaniciCikti)
def ben(k: Kullanici = Depends(gecerli_kullanici)):
    return _cikti(k)
