"""Uyarlamalı test uçları (motor: app/uyarlamali.py).

Öğrenci, sınıflarının öğretmenlerinin havuzundaki sorularla bir kazanım için "eksiğini bul" testi çözer; sonuçta
MK durumları, eksiğin kökü ve kök MK'lerin videoları gelir. Öğretmen kendi havuzuyla deneme yapar (her adımda MK
olasılıklarını canlı görür) ve sınıflarındaki öğrencilerin testlerini listeler. Test sırasında doğru/yanlış
gösterilmez; doğru şık ve çözüm sonuçta açılır.
"""

from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from sqlalchemy import select
from sqlalchemy.orm import Session

from .. import uyarlamali as u
from ..kimlik import gecerli_kullanici, rol_gerekli
from ..modeller import MK, Kullanici, MKEsleme, Sinif, SinifUye, UyarlamaliCevap, UyarlamaliOturum, VideoParca
from ..vt import vt_oturumu
from .degerlendir import KonuKarti, VideoC, _kapak
from .mufredat import _metinler

router = APIRouter(prefix="/api/uyarlamali", tags=["uyarlamali"])
ogretmen = rol_gerekli("ogretmen")
EN_AZ_MK = 3  # listede gösterilmesi için havuzda sorusu olan en az MK sayısı


class KazanimC(BaseModel):
    kod: str
    ifade: str
    ders: str
    sinif_duzeyi: int
    mk_sayisi: int  # kapsam
    soru_sayisi: int  # havuz


class SecenekC(BaseModel):
    harf: str
    metin: str


class SoruC(BaseModel):
    soru_id: int
    metin: str
    gorsel: str | None
    secenekler: list[SecenekC]


class MKDurumC(BaseModel):
    kod: str
    ifade: str
    p: float
    durum: str  # biliyor / bilmiyor / belirsiz / sorulmadi
    cikarim: bool  # "biliyor" kararı ön koşul zincirinden çıkarıldı
    onkosulu_eksik: bool = False  # ön koşullarından biri bilinmiyor
    soru_sayisi: int
    havuz: int  # bu MK için havuzdaki soru sayısı
    on_kosullar: list[str]


class GecmisC(BaseModel):
    sira: int
    mk: str
    metin: str
    secilen: str
    dogru_sik: str | None
    dogru: bool
    cozum: str


class OturumC(BaseModel):
    id: int
    kazanim: str
    kazanim_ifade: str
    durum: str  # devam / bitti
    deneme: bool  # öğretmen denemesi
    sira: int  # şimdiki sorunun sırası (1'den)
    en_cok: int
    soru: SoruC | None  # devam ederken
    mkler: list[MKDurumC] = []  # öğretmende her adımda, öğrencide sonda
    gecmis: list[GecmisC] = []  # sonda (öğretmende her adımda)
    kokler: list[str] = []
    konular: list[KonuKarti] = []  # kök MK'lerin videoları (sonda)


class OturumKisaC(BaseModel):
    id: int
    ogrenci: str
    kazanim: str
    kazanim_ifade: str
    durum: str
    soru: int
    kokler: list[str]
    baslama: datetime


class BaslaG(BaseModel):
    kazanim: str = Field(max_length=24)


class CevapG(BaseModel):
    secilen: str = Field(max_length=2)


def _sahipler(vt: Session, k: Kullanici) -> list[int]:
    if k.rol == "ogretmen":
        return [k.id]
    return list(set(vt.scalars(select(Sinif.ogretmen_id).join(SinifUye).where(SinifUye.ogrenci_id == k.id))))


def _ders(kazanim: str) -> str:
    return "Fizik" if kazanim.startswith("FİZ") else "Matematik"


def _ifade(kazanim: str) -> str:
    return _metinler(_ders(kazanim), u.kazanim_sinifi(kazanim))[1].get(kazanim, "")


@router.get("/kazanimlar", response_model=list[KazanimC])
def kazanimlar(k: Kullanici = Depends(gecerli_kullanici), vt: Session = Depends(vt_oturumu)):
    """Havuzunda en az EN_AZ_MK MK için soru olan kazanımlar."""
    sahipler = _sahipler(vt, k)
    sonuc = []
    adaylar = set()
    for s in u.havuz(vt, sahipler, [m.kod for m in vt.scalars(select(MK))]).items():
        if s[1]:
            adaylar |= set(vt.scalars(select(MKEsleme.ogrenme_ciktisi).where(MKEsleme.mk_kod == s[0])))
    for kaz in sorted(a for a in adaylar if a.startswith(("MAT.", "FİZ."))):
        mkler, _ = u.kapsam(vt, kaz)
        h = u.havuz(vt, sahipler, mkler)
        dolu = sum(1 for m in mkler if h[m])
        if dolu >= EN_AZ_MK:
            sonuc.append(KazanimC(kod=kaz, ifade=_ifade(kaz), ders=_ders(kaz), sinif_duzeyi=u.kazanim_sinifi(kaz),
                                  mk_sayisi=len(mkler), soru_sayisi=sum(len(v) for v in h.values())))
    return sonuc


def _oturum(vt: Session, o: UyarlamaliOturum, k: Kullanici) -> UyarlamaliOturum:
    if not o:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Test bulunamadı.")
    if o.kullanici_id == k.id:
        return o
    if k.rol == "ogretmen" and vt.scalar(select(SinifUye).join(Sinif).where(SinifUye.ogrenci_id == o.kullanici_id, Sinif.ogretmen_id == k.id)):
        return o
    raise HTTPException(status.HTTP_404_NOT_FOUND, "Test bulunamadı.")


def _ilerlet(vt: Session, o: UyarlamaliOturum) -> None:
    """Sıradaki soruyu koyar ya da testi bitirir."""
    d = u.yeniden_oynat(vt, o)
    h = u.havuz(vt, _sahipler(vt, o.kullanici), d.mkler)
    s = u.sonraki(d, o, h)
    if s:
        o.cevaplar.append(UyarlamaliCevap(sira=len(o.cevaplar) + 1, soru_id=s[1].id, mk_kod=s[0]))
    else:
        o.durum, o.bitis = "bitti", datetime.now(timezone.utc)
    vt.commit()


def _cikti(vt: Session, o: UyarlamaliOturum, k: Kullanici) -> OturumC:
    d = u.yeniden_oynat(vt, o)
    deneme = o.kullanici.rol == "ogretmen"
    ayrinti = o.durum == "bitti" or k.rol == "ogretmen"
    acik = next((c for c in o.cevaplar if c.secilen is None), None)
    c = OturumC(id=o.id, kazanim=o.kazanim, kazanim_ifade=_ifade(o.kazanim), durum=o.durum, deneme=deneme,
                sira=acik.sira if acik else len(o.cevaplar), en_cok=u.MAKS_TOPLAM,
                soru=acik and SoruC(soru_id=acik.soru_id, metin=acik.soru.metin, gorsel=acik.soru.gorsel,
                                    secenekler=[SecenekC(harf=x.harf, metin=x.metin) for x in acik.soru.secenekler]))
    if not ayrinti:
        return c
    h = u.havuz(vt, _sahipler(vt, o.kullanici), d.mkler)
    for m in d.mkler:
        mk = vt.get(MK, m)
        k_ = d.karar(m)
        if k_ == "belirsiz" and not d.soru_sayisi.get(m) and m not in d.cikarim:
            k_ = "sorulmadi"  # bu testte kanıt yok (önceki sınavdan gelen belirsiz olasılık da sayılmaz)
        c.mkler.append(MKDurumC(kod=m, ifade=mk.ifade if mk else "", p=round(d.p[m], 3), durum=k_, cikarim=m in d.cikarim,
                                onkosulu_eksik=d.onkosulu_eksik(m),
                                soru_sayisi=d.soru_sayisi.get(m, 0), havuz=len(h[m]), on_kosullar=sorted(d.on.get(m, ()))))
    for x in o.cevaplar:
        if x.secilen is not None:
            dogru = next((s.harf for s in x.soru.secenekler if s.dogru), None)
            c.gecmis.append(GecmisC(sira=x.sira, mk=x.mk_kod, metin=x.soru.metin, secilen=x.secilen, dogru_sik=dogru,
                                    dogru=bool(x.dogru), cozum=x.soru.cozum))
    c.kokler = d.kokler()
    if o.durum == "bitti":
        for m in c.kokler:
            parca = {vp.tur: vp for vp in vt.scalars(select(VideoParca).where(VideoParca.mk_kod == m, VideoParca.onayli)
                                                   .order_by(VideoParca.sira.desc()))}
            a, b = parca.get("konu"), parca.get("soru")
            vc = lambda vp: vp and VideoC(id=vp.id, video_id=vp.video_id, kanal=vp.kanal, baslik=vp.baslik, bas=vp.bas, son=vp.son, kapak=_kapak(vp))
            if a or b:
                mk = vt.get(MK, m)
                c.konular.append(KonuKarti(konu=(a or b).konu or (mk.ifade.rstrip(".") if mk else m), anlatim=vc(a), soru=vc(b)))
    return c


@router.post("", response_model=OturumC)
def basla(g: BaslaG, k: Kullanici = Depends(gecerli_kullanici), vt: Session = Depends(vt_oturumu)):
    mkler, _ = u.kapsam(vt, g.kazanim)
    if not mkler:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Bu kazanım için mikro kazanım bulunamadı.")
    if not any(u.havuz(vt, _sahipler(vt, k), mkler).values()):
        raise HTTPException(status.HTTP_409_CONFLICT, "Bu kazanım için soru havuzunda soru yok.")
    o = UyarlamaliOturum(kullanici_id=k.id, kazanim=g.kazanim, ders=_ders(g.kazanim), sinif_duzeyi=u.kazanim_sinifi(g.kazanim))
    vt.add(o)
    vt.flush()
    vt.refresh(o)
    _ilerlet(vt, o)
    return _cikti(vt, o, k)


@router.get("/oturumlar", response_model=list[OturumKisaC])
def oturumlar(k: Kullanici = Depends(gecerli_kullanici), vt: Session = Depends(vt_oturumu)):
    """Öğrenci: kendi testleri. Öğretmen: sınıflarındaki öğrencilerin testleri ve kendi denemeleri."""
    if k.rol == "ogretmen":
        ogrenciler = select(SinifUye.ogrenci_id).join(Sinif).where(Sinif.ogretmen_id == k.id)
        q = select(UyarlamaliOturum).where(UyarlamaliOturum.kullanici_id.in_(ogrenciler) | (UyarlamaliOturum.kullanici_id == k.id))
    else:
        q = select(UyarlamaliOturum).where(UyarlamaliOturum.kullanici_id == k.id)
    sonuc = []
    for o in vt.scalars(q.order_by(UyarlamaliOturum.baslama.desc()).limit(200)):
        sonuc.append(OturumKisaC(id=o.id, ogrenci=o.kullanici.ad + (" (deneme)" if o.kullanici.rol == "ogretmen" else ""),
                                 kazanim=o.kazanim, kazanim_ifade=_ifade(o.kazanim), durum=o.durum,
                                 soru=sum(1 for c in o.cevaplar if c.secilen is not None),
                                 kokler=u.yeniden_oynat(vt, o).kokler() if o.durum == "bitti" else [], baslama=o.baslama))
    return sonuc


@router.get("/{oturum_id}", response_model=OturumC)
def oturum(oturum_id: int, k: Kullanici = Depends(gecerli_kullanici), vt: Session = Depends(vt_oturumu)):
    return _cikti(vt, _oturum(vt, vt.get(UyarlamaliOturum, oturum_id), k), k)


@router.post("/{oturum_id}/cevap", response_model=OturumC)
def cevapla(oturum_id: int, g: CevapG, k: Kullanici = Depends(gecerli_kullanici), vt: Session = Depends(vt_oturumu)):
    o = vt.get(UyarlamaliOturum, oturum_id)
    if not o or o.kullanici_id != k.id:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Test bulunamadı.")
    acik = next((c for c in o.cevaplar if c.secilen is None), None)
    if o.durum != "devam" or not acik:
        raise HTTPException(status.HTTP_409_CONFLICT, "Test bitti.")
    sik = next((s for s in acik.soru.secenekler if s.harf == g.secilen), None)
    if not sik:
        raise HTTPException(422, "Böyle bir şık yok.")
    acik.secilen, acik.dogru, acik.zaman = g.secilen, sik.dogru, datetime.now(timezone.utc)
    vt.flush()
    _ilerlet(vt, o)
    return _cikti(vt, o, k)
