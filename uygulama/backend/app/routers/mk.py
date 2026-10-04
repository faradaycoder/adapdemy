"""MK verisini okuma: arama, ayrıntı (ön koşullar, ardıllar, eşlemeler, yanılgılar) ve özet."""

from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import BaseModel
from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session

from ..kimlik import gecerli_kullanici
from ..modeller import MK, MKEsleme, MKOnKosul, MKYanilgi, Yanilgi
from ..vt import vt_oturumu

router = APIRouter(prefix="/api/mk", tags=["mk"], dependencies=[Depends(gecerli_kullanici)])


class MKKisa(BaseModel):
    kod: str
    ifade: str
    tur: str
    islem_turu: str
    zorluk: float | None
    seviye: int | None


class EslemeCikti(BaseModel):
    sinif: int
    sinif_unite: str
    ogrenme_ciktisi: str
    surec_bileseni: str


class YanilgiCikti(BaseModel):
    kod: str
    ifade: str


class MKAyrinti(MKKisa):
    ders: str
    ana_unite: str
    bilissel_duzey: str
    v: float | None
    on_kosul_diger: str
    olcme_turleri: str
    ustalik_olcutu: str
    on_kosullar: list[MKKisa]
    ardillar: list[MKKisa]
    eslemeler: list[EslemeCikti]
    yanilgilar: list[YanilgiCikti]


def _kisa(m: MK) -> MKKisa:
    return MKKisa(kod=m.kod, ifade=m.ifade, tur=m.tur, islem_turu=m.islem_turu, zorluk=m.zorluk, seviye=m.seviye)


@router.get("/ozet")
def ozet(vt: Session = Depends(vt_oturumu)):
    """Ders başına MK, bağ ve öğrenme çıktısı sayıları."""
    sonuc = {}
    for ders in vt.scalars(select(MK.ders).distinct()):
        sonuc[ders] = {
            "mk": vt.scalar(select(func.count()).select_from(MK).where(MK.ders == ders, MK.durum != "iptal")),
            "bag": vt.scalar(select(func.count()).select_from(MKOnKosul).join(MK, MK.kod == MKOnKosul.mk_kod)
                             .where(MK.ders == ders)),
            "ogrenme_ciktisi": vt.scalar(select(func.count(func.distinct(MKEsleme.ogrenme_ciktisi)))
                                         .join(MK, MK.kod == MKEsleme.mk_kod).where(MK.ders == ders)),
        }
    return sonuc


@router.get("", response_model=list[MKKisa])
def ara(
    ders: str | None = None,
    sinif: int | None = Query(None, ge=5, le=12),
    ogrenme_ciktisi: str | None = None,
    q: str | None = Query(None, description="Kodda ya da ifadede geçen metin"),
    limit: int = Query(50, ge=1, le=500),
    vt: Session = Depends(vt_oturumu),
):
    sorgu = select(MK).where(MK.durum != "iptal")
    if ders:
        sorgu = sorgu.where(MK.ders == ders)
    if sinif or ogrenme_ciktisi:
        alt = select(MKEsleme.mk_kod)
        if sinif:
            alt = alt.where(MKEsleme.sinif == sinif)
        if ogrenme_ciktisi:
            alt = alt.where(MKEsleme.ogrenme_ciktisi == ogrenme_ciktisi)
        sorgu = sorgu.where(MK.kod.in_(alt))
    if q:
        sorgu = sorgu.where(or_(MK.kod.ilike(f"%{q}%"), MK.ifade.ilike(f"%{q}%")))
    return [_kisa(m) for m in vt.scalars(sorgu.order_by(MK.kod).limit(limit))]


@router.get("/{kod}", response_model=MKAyrinti)
def ayrinti(kod: str, vt: Session = Depends(vt_oturumu)):
    m = vt.get(MK, kod)
    if not m:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "MK bulunamadı.")
    onk = vt.scalars(select(MK).join(MKOnKosul, MKOnKosul.on_kosul_kod == MK.kod).where(MKOnKosul.mk_kod == kod)).all()
    ard = vt.scalars(select(MK).join(MKOnKosul, MKOnKosul.mk_kod == MK.kod).where(MKOnKosul.on_kosul_kod == kod)).all()
    es = vt.scalars(select(MKEsleme).where(MKEsleme.mk_kod == kod).order_by(MKEsleme.sinif)).all()
    yg = vt.scalars(select(Yanilgi).join(MKYanilgi, MKYanilgi.yanilgi_kod == Yanilgi.kod).where(MKYanilgi.mk_kod == kod)).all()
    return MKAyrinti(
        **_kisa(m).model_dump(), ders=m.ders, ana_unite=m.ana_unite, bilissel_duzey=m.bilissel_duzey, v=m.v,
        on_kosul_diger=m.on_kosul_diger, olcme_turleri=m.olcme_turleri, ustalik_olcutu=m.ustalik_olcutu,
        on_kosullar=[_kisa(x) for x in onk], ardillar=[_kisa(x) for x in ard],
        eslemeler=[EslemeCikti(sinif=e.sinif, sinif_unite=e.sinif_unite, ogrenme_ciktisi=e.ogrenme_ciktisi,
                               surec_bileseni=e.surec_bileseni) for e in es],
        yanilgilar=[YanilgiCikti(kod=y.kod, ifade=y.ifade) for y in yg],
    )
