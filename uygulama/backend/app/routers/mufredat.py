"""Müfredat ağacı (sınıf → ünite/tema → kazanım → mikro kazanım): sınava soru eklerken seçim için.

Ünite ve kazanım metinleri <Ders>/kazanimlar/<sınıf>-sinif-<ders>.md dosyalarından, kazanım–MK eşlemesi veritabanından
(mk_esleme) gelir. Her MK için öğretmenin bankasında o MK'yi ölçen (sorunun MK'si ya da rubrik adımı) soru sayısı verilir.
"""

import re
from functools import lru_cache

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import func, select, union
from sqlalchemy.orm import Session

from ..ayarlar import EVALORA_KOK
from ..kimlik import rol_gerekli
from ..modeller import MK, Kullanici, MKEsleme, RubrikAdim, Soru, SoruMK
from ..vt import vt_oturumu

router = APIRouter(prefix="/api/mufredat", tags=["mufredat"])
ogretmen = rol_gerekli("ogretmen")


class MKDugum(BaseModel):
    kod: str
    ifade: str
    soru_sayisi: int


class KazanimDugum(BaseModel):
    kod: str
    ifade: str
    mkler: list[MKDugum]


class UniteDugum(BaseModel):
    no: int
    ad: str
    kazanimlar: list[KazanimDugum]


@lru_cache
def _metinler(ders: str, sinif: int) -> tuple[list[tuple[int, str]], dict[str, str]]:
    """md dosyasından (ünite no, ad) listesi ve kazanım kodu → ifade."""
    dosya = EVALORA_KOK / ders / "kazanimlar" / f"{sinif}-sinif-{ders.lower()}.md"
    if not dosya.exists():
        return [], {}
    uniteler, kazanim = [], {}
    for satir in dosya.read_text(encoding="utf-8").splitlines():
        if m := re.match(r"##\s*(\d+)\.\s*(?:Tema|Ünite):\s*(.+?)\s*(?:\(http.*)?$", satir):
            uniteler.append((int(m[1]), m[2]))
        elif m := re.match(r"-\s*((?:MAT|FİZ)\.\d+\.\d+\.\d+)\s+(.+)$", satir):
            kazanim[m[1]] = m[2].strip()
    return uniteler, kazanim


@router.get("", response_model=list[UniteDugum])
def agac(ders: str, sinif: int, k: Kullanici = Depends(ogretmen), vt: Session = Depends(vt_oturumu)):
    if ders not in ("Matematik", "Fizik"):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Ders Matematik ya da Fizik olmalı.")
    uniteler, kazanim_metni = _metinler(ders, sinif)
    eslemeler = vt.execute(select(MKEsleme.ogrenme_ciktisi, MKEsleme.mk_kod, MK.ifade).join(MK, MK.kod == MKEsleme.mk_kod)
                           .where(MKEsleme.sinif == sinif, MK.ders == ders).order_by(MKEsleme.ogrenme_ciktisi, MKEsleme.mk_kod)).all()
    # öğretmenin sorularında MK geçiş sayısı (sorunun MK'si ya da rubrik adımı; soru başına bir kez)
    soru_mk = union(select(SoruMK.soru_id, SoruMK.mk_kod), select(RubrikAdim.soru_id, RubrikAdim.mk_kod)).subquery()
    sayilar = dict(vt.execute(select(soru_mk.c.mk_kod, func.count()).join(Soru, Soru.id == soru_mk.c.soru_id)
                              .where(Soru.olusturan_id == k.id).group_by(soru_mk.c.mk_kod)).all())
    kazanimlar: dict[str, list[MKDugum]] = {}
    for oc, kod, ifade in eslemeler:
        if not oc.startswith(("MAT.", "FİZ.")):  # Fizik eşlemesinde öğrenme çıktısı kodu ayrı sütunda
            continue
        liste = kazanimlar.setdefault(oc, [])
        if all(x.kod != kod for x in liste):
            liste.append(MKDugum(kod=kod, ifade=ifade, soru_sayisi=sayilar.get(kod, 0)))
    sonuc = []
    for no, ad in uniteler or sorted({(int(oc.split(".")[2]), f"{oc.split('.')[2]}. ünite") for oc in kazanimlar}):
        ks = [KazanimDugum(kod=oc, ifade=kazanim_metni.get(oc, ""), mkler=mk) for oc, mk in sorted(kazanimlar.items(), key=lambda x: [int(p) for p in x[0].split(".")[1:]])
              if int(oc.split(".")[2]) == no]
        sonuc.append(UniteDugum(no=no, ad=ad, kazanimlar=ks))
    return sonuc
