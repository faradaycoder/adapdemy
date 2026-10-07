"""F. Rapor: sınıf raporu (MK ısı haritası, yanılgılar) ve öğrenci MK raporu (ALGORITMA.md 6)."""

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..kimlik import rol_gerekli
from ..modeller import MK, Kullanici, Sinif, VideoParca, Yanilgi
from ..rapor import MKKanit, mk_kanitlari, onayli_teslimler
from ..vt import vt_oturumu
from .degerlendir import KonuKarti, VideoC, _kapak

router = APIRouter(tags=["rapor"])
ogretmen = rol_gerekli("ogretmen")
ogrenci = rol_gerekli("ogrenci")


class HucreC(BaseModel):
    durum: str  # biliyor / bilmiyor / belirsiz / olculemedi
    p: float | None


class SinifOgrenciC(BaseModel):
    id: int
    ad: str
    teslim: int  # onaylanmış teslim sayısı
    mkler: dict[str, HucreC]


class SinifMKC(BaseModel):
    kod: str
    ifade: str
    biliyor: int
    belirsiz: int
    bilmiyor: int
    olculemedi: int


class YanilgiC(BaseModel):
    kod: str
    ifade: str
    sayi: int
    ogrenciler: list[str]


class SinifRaporC(BaseModel):
    sinif: str
    ders: str
    sinif_duzeyi: int
    ogrenciler: list[SinifOgrenciC]
    mkler: list[SinifMKC]  # temelden üste (zorluğa göre)
    yanilgilar: list[YanilgiC]


class OgrenciMKC(BaseModel):
    kod: str
    ifade: str
    durum: str
    p: float | None
    dogru: int
    yanlis: int
    olculemedi: int
    konu: KonuKarti | None = None  # bilinmeyen ya da belirsiz MK için video kartı


class OgrenciRaporC(BaseModel):
    ogrenci: str
    teslim: int
    mkler: list[OgrenciMKC]
    yanilgilar: list[YanilgiC]


def _sinif(vt: Session, sinif_id: int, k: Kullanici) -> Sinif:
    s = vt.get(Sinif, sinif_id)
    if not s or s.ogretmen_id != k.id:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Sınıf bulunamadı.")
    return s


def _zorluk(vt: Session, kod: str) -> float:
    m = vt.get(MK, kod)
    return (m.zorluk or 0) if m else 0


def _yanilgilar(vt: Session, teslimler_ad: list[tuple[str, list]]) -> list[YanilgiC]:
    sayac: dict[str, list[str]] = {}
    for ad, teslimler in teslimler_ad:
        for t in teslimler:
            for c in t.cevaplar:
                if c.yanilgi_kod:
                    sayac.setdefault(c.yanilgi_kod, []).append(ad)
    out = []
    for kod, adlar in sorted(sayac.items(), key=lambda x: -len(x[1])):
        y = vt.get(Yanilgi, kod)
        out.append(YanilgiC(kod=kod, ifade=y.ifade if y else "", sayi=len(adlar), ogrenciler=sorted(set(adlar))))
    return out


@router.get("/api/siniflar/{sinif_id}/rapor", response_model=SinifRaporC)
def sinif_raporu(sinif_id: int, k: Kullanici = Depends(ogretmen), vt: Session = Depends(vt_oturumu)):
    s = _sinif(vt, sinif_id, k)
    uyeler = sorted((u.ogrenci for u in s.uyeler), key=lambda o: o.ad)
    teslimler = {o.id: onayli_teslimler(vt, o.id, s.id) for o in uyeler}
    kanit = {o.id: mk_kanitlari(vt, teslimler[o.id]) for o in uyeler}
    kodlar = sorted({m for x in kanit.values() for m in x}, key=lambda m: (_zorluk(vt, m), m))
    mkler = []
    for m in kodlar:
        d = [kanit[o.id].get(m, MKKanit()).durum for o in uyeler]
        mk = vt.get(MK, m)
        mkler.append(SinifMKC(kod=m, ifade=mk.ifade if mk else "", biliyor=d.count("biliyor"), belirsiz=d.count("belirsiz"),
                              bilmiyor=d.count("bilmiyor"), olculemedi=d.count("olculemedi")))
    ogrenciler = [SinifOgrenciC(id=o.id, ad=o.ad, teslim=len(teslimler[o.id]),
                                mkler={m: HucreC(durum=x.durum, p=x.p and round(x.p, 3)) for m, x in kanit[o.id].items()})
                  for o in uyeler]
    return SinifRaporC(sinif=s.ad, ders=s.ders, sinif_duzeyi=s.sinif_duzeyi, ogrenciler=ogrenciler, mkler=mkler,
                       yanilgilar=_yanilgilar(vt, [(o.ad, teslimler[o.id]) for o in uyeler]))


def _ogrenci_raporu(vt: Session, o: Kullanici, sinif_id: int | None, videolu: bool) -> OgrenciRaporC:
    teslimler = onayli_teslimler(vt, o.id, sinif_id)
    kanit = mk_kanitlari(vt, teslimler)
    parcalar: dict[tuple[str, str], VideoParca] = {}
    if videolu:
        for vp in vt.scalars(select(VideoParca).where(VideoParca.onayli).order_by(VideoParca.sira.desc())):
            parcalar[(vp.mk_kod, vp.tur)] = vp

    def vc(vp):
        return vp and VideoC(id=vp.id, video_id=vp.video_id, kanal=vp.kanal, baslik=vp.baslik, bas=vp.bas, son=vp.son, kapak=_kapak(vp))

    sira = {"bilmiyor": 0, "belirsiz": 1, "olculemedi": 2, "biliyor": 3}
    mkler = []
    for m, x in sorted(kanit.items(), key=lambda i: (sira[i[1].durum], _zorluk(vt, i[0]), i[0])):
        mk = vt.get(MK, m)
        konu = None
        if x.durum in ("bilmiyor", "belirsiz"):
            a, b = parcalar.get((m, "konu")), parcalar.get((m, "soru"))
            if a or b:
                konu = KonuKarti(konu=(a or b).konu or (mk.ifade.rstrip(".") if mk else m), anlatim=vc(a), soru=vc(b))
        mkler.append(OgrenciMKC(kod=m, ifade=mk.ifade if mk else "", durum=x.durum, p=x.p and round(x.p, 3),
                                dogru=x.dogru, yanlis=x.yanlis, olculemedi=x.olculemedi, konu=konu))
    return OgrenciRaporC(ogrenci=o.ad, teslim=len(teslimler), mkler=mkler, yanilgilar=_yanilgilar(vt, [(o.ad, teslimler)]))


@router.get("/api/siniflar/{sinif_id}/ogrenciler/{ogrenci_id}/rapor", response_model=OgrenciRaporC)
def ogrenci_raporu_ogretmen(sinif_id: int, ogrenci_id: int, k: Kullanici = Depends(ogretmen), vt: Session = Depends(vt_oturumu)):
    s = _sinif(vt, sinif_id, k)
    u = next((u for u in s.uyeler if u.ogrenci_id == ogrenci_id), None)
    if not u:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Öğrenci bu sınıfta değil.")
    return _ogrenci_raporu(vt, u.ogrenci, s.id, videolu=False)


@router.get("/api/rapor", response_model=OgrenciRaporC)
def kendi_raporum(k: Kullanici = Depends(ogrenci), vt: Session = Depends(vt_oturumu)):
    return _ogrenci_raporu(vt, k, None, videolu=True)
