"""Soru bankası: soruyu okut ve eşle, öğretmen düzeltsin, kaydet ve onayla (PLAN_UYGULAMA.md akış 1)."""

import base64
import binascii
import hashlib

import httpx
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from sqlalchemy import select
from sqlalchemy.orm import Session, object_session

from ..ayarlar import VERI
from ..eslestirme import Adim, Harita, esle
from ..kimlik import rol_gerekli
from ..modeller import MK, RubrikAdim, Secenek, Soru, SoruMK, Kullanici
from ..vt import vt_oturumu
from ..yapay_zeka import DEMO_KLASOR, TanimadiHatasi, saglayici

router = APIRouter(prefix="/api/sorular", tags=["sorular"])
gorsel_router = APIRouter(prefix="/api/gorsel", tags=["sorular"])
ogretmen = rol_gerekli("ogretmen")

YUKLEMELER = VERI / "yuklemeler"
YUKLEMELER.mkdir(exist_ok=True)
EN_BUYUK_GORSEL = 8 * 1024 * 1024

_harita: Harita | None = None


def harita(vt: Session) -> Harita:
    global _harita
    if _harita is None:
        _harita = Harita(vt)
    return _harita


# ---------- şemalar ----------

class SecenekG(BaseModel):
    harf: str = Field(max_length=2)
    metin: str
    dogru: bool = False
    yanilgi_kod: str | None = None


class AdimG(BaseModel):
    aciklama: str
    mk_kod: str


class MKBilgi(BaseModel):
    kod: str
    ifade: str
    islem_turu: str
    v: float | None
    zorluk: float | None
    seviye: int | None


class AdimC(AdimG):
    pay: float
    mk: MKBilgi | None
    soru_mk_mi: bool  # sorunun (en üst) MK'si mi, yoksa teşhis için ön koşul mu


class EslemeC(BaseModel):
    soru_mkleri: list[MKBilgi]
    birincil: str | None
    zorluk: float | None
    adimlar: list[AdimC]
    uyarilar: list[str]


class SoruG(BaseModel):
    ders: str = Field(pattern="^(Fizik|Matematik)$")
    sinif_duzeyi: int = Field(ge=5, le=12)
    metin: str = Field(min_length=1)
    gorsel: str | None = None
    cevap_bicimi: str = Field(pattern="^(coktan_secmeli|kisa_cevap|yazili|kagit)$")
    secenekler: list[SecenekG] = []
    dogru_cevap: str = ""
    cozum: str = ""
    birincil: str | None = None
    adimlar: list[AdimG] = Field(min_length=1)


class AnalizIstek(BaseModel):
    ders: str = Field(pattern="^(Fizik|Matematik)$")
    sinif_duzeyi: int = Field(ge=5, le=12)
    gorsel_base64: str | None = None
    metin: str | None = None
    ornek: str | None = None  # demo örneğinin anahtarı


class AnalizC(SoruG):
    eslesme: EslemeC
    saglayici: str
    notlar: list[str] = []  # sağlayıcının öğretmene notları (ör. aday MK önerileri)


class SoruC(SoruG):
    id: int
    zorluk: float | None
    durum: str
    kaynak: str
    eslesme: EslemeC


class SoruKisa(BaseModel):
    id: int
    ders: str
    sinif_duzeyi: int
    metin: str
    gorsel: str | None
    cevap_bicimi: str
    zorluk: float | None
    durum: str
    birincil: str | None
    soru_mkleri: list[str]
    mk_detay: list[MKBilgi] = []  # sorunun MK'leri, açıklamalarıyla
    onkosul_detay: list[MKBilgi] = []  # rubrikte teşhis için geçen ön koşul MK'ler


# ---------- yardımcılar ----------

def _mk_bilgi(m: MK | None) -> MKBilgi | None:
    if not m:
        return None
    return MKBilgi(kod=m.kod, ifade=m.ifade, islem_turu=m.islem_turu, v=m.v, zorluk=m.zorluk, seviye=m.seviye)


def soru_kisa(s: Soru) -> SoruKisa:
    """Liste görünümü için soru özeti; MK'ler açıklamalarıyla (öğretmen koda bakıp anlamak zorunda kalmasın)."""
    h = harita(object_session(s))
    kodlar = [m.mk_kod for m in s.mkler]
    onkosul = list(dict.fromkeys(a.mk_kod for a in s.adimlar if a.mk_kod not in kodlar))
    return SoruKisa(id=s.id, ders=s.ders, sinif_duzeyi=s.sinif_duzeyi, metin=s.metin, gorsel=s.gorsel,
                    cevap_bicimi=s.cevap_bicimi, zorluk=s.zorluk, durum=s.durum,
                    birincil=next((m.mk_kod for m in s.mkler if m.birincil), None), soru_mkleri=kodlar,
                    mk_detay=[b for k in kodlar if (b := _mk_bilgi(h.mk.get(k)))],
                    onkosul_detay=[b for k in onkosul if (b := _mk_bilgi(h.mk.get(k)))])


def _esle(vt: Session, ders: str, adimlar: list[AdimG], birincil: str | None) -> EslemeC:
    h = harita(vt)
    sonuc = esle(h, [Adim(a.aciklama, a.mk_kod.strip()) for a in adimlar], ders)
    uyarilar = list(sonuc.uyarilar)
    if birincil and birincil not in sonuc.soru_mkleri:
        uyarilar.append(f"Birincil MK {birincil}, sorunun MK'leri arasında değil (başka bir adımın öncülü ya da adımlarda yok).")
        birincil = None
    if not birincil and sonuc.soru_mkleri:
        birincil = max(sonuc.soru_mkleri, key=lambda k: h.mk[k].zorluk or 0)
    ust = set(sonuc.soru_mkleri)
    return EslemeC(
        soru_mkleri=[_mk_bilgi(h.mk[k]) for k in sonuc.soru_mkleri], birincil=birincil, zorluk=sonuc.zorluk,
        adimlar=[AdimC(aciklama=a.aciklama, mk_kod=a.mk_kod, pay=a.pay, mk=_mk_bilgi(h.mk.get(a.mk_kod)),
                       soru_mk_mi=a.mk_kod in ust) for a in sonuc.adimlar],
        uyarilar=uyarilar,
    )


def _gorsel_kaydet(veri: bytes) -> str:
    if len(veri) > EN_BUYUK_GORSEL:
        raise HTTPException(status.HTTP_413_REQUEST_ENTITY_TOO_LARGE, "Dosya en fazla 8 MB olabilir.")
    uzanti = (".png" if veri[:8] == b"\x89PNG\r\n\x1a\n" else ".jpg" if veri[:3] == b"\xff\xd8\xff"
              else ".pdf" if veri[:5] == b"%PDF-" else None)
    if not uzanti:
        raise HTTPException(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, "Yalnız PNG, JPEG ya da PDF yüklenebilir.")
    ad = hashlib.sha256(veri).hexdigest()[:32] + uzanti
    (YUKLEMELER / ad).write_bytes(veri)
    return ad


def _soru_cikti(vt: Session, s: Soru) -> SoruC:
    birincil = next((m.mk_kod for m in s.mkler if m.birincil), None)
    adimlar = [AdimG(aciklama=a.aciklama, mk_kod=a.mk_kod) for a in s.adimlar]
    return SoruC(
        id=s.id, ders=s.ders, sinif_duzeyi=s.sinif_duzeyi, metin=s.metin, gorsel=s.gorsel, cevap_bicimi=s.cevap_bicimi,
        secenekler=[SecenekG(harf=x.harf, metin=x.metin, dogru=x.dogru, yanilgi_kod=x.yanilgi_kod) for x in s.secenekler],
        dogru_cevap=s.dogru_cevap, cozum=s.cozum, birincil=birincil, adimlar=adimlar, zorluk=s.zorluk, durum=s.durum,
        kaynak=s.kaynak, eslesme=_esle(vt, s.ders, adimlar, birincil),
    )


def _yaz(vt: Session, s: Soru, g: SoruG) -> None:
    e = _esle(vt, g.ders, g.adimlar, g.birincil)
    if not e.soru_mkleri:
        raise HTTPException(422, "Adımlar geçerli bir MK'ye eşlenmeli.")
    if g.cevap_bicimi == "coktan_secmeli" and sum(x.dogru for x in g.secenekler) != 1:
        raise HTTPException(422, "Çoktan seçmeli soruda tam bir doğru şık olmalı.")
    s.ders, s.sinif_duzeyi, s.metin, s.gorsel = g.ders, g.sinif_duzeyi, g.metin, g.gorsel
    s.cevap_bicimi, s.dogru_cevap, s.cozum, s.zorluk = g.cevap_bicimi, g.dogru_cevap, g.cozum, e.zorluk
    if s.id:  # güncellemede eski satırlar önce silinir; yoksa aynı MK yeniden eklenirken tekillik kuralı bozulur
        s.mkler.clear()
        s.adimlar.clear()
        s.secenekler.clear()
        vt.flush()
    s.mkler = [SoruMK(mk_kod=m.kod, birincil=m.kod == e.birincil) for m in e.soru_mkleri]
    s.adimlar = [RubrikAdim(sira=i + 1, aciklama=a.aciklama, mk_kod=a.mk_kod, pay=a.pay)
                 for i, a in enumerate(e.adimlar) if a.mk]
    s.secenekler = [Secenek(harf=x.harf, metin=x.metin, dogru=x.dogru, yanilgi_kod=x.yanilgi_kod or None) for x in g.secenekler]


def _sahibi(vt: Session, soru_id: int, k: Kullanici) -> Soru:
    s = vt.get(Soru, soru_id)
    if not s or s.olusturan_id != k.id:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Soru bulunamadı.")
    return s


# ---------- uç noktalar ----------

@router.get("/saglayici")
def saglayici_bilgisi(_: Kullanici = Depends(ogretmen)):
    sg = saglayici()
    return {"ad": sg.ad, "ornekler": sg.ornekler()}


@router.post("/analiz", response_model=AnalizC)
def analiz(istek: AnalizIstek, _: Kullanici = Depends(ogretmen), vt: Session = Depends(vt_oturumu)):
    """Soruyu okur, çözer, rubrik adımlarını MK'ye eşler. Kaydetmez; öğretmen inceleyip kaydeder."""
    sg = saglayici()
    gorsel_adi = None
    try:
        if istek.ornek:
            a = sg.ornek(istek.ornek)
            if a.gorsel_ornek:
                gorsel_adi = _gorsel_kaydet((DEMO_KLASOR / a.gorsel_ornek).read_bytes())
        else:
            veri = None
            if istek.gorsel_base64:
                try:
                    veri = base64.b64decode(istek.gorsel_base64.split(",")[-1], validate=True)
                except (binascii.Error, ValueError):
                    raise HTTPException(422, "Görsel okunamadı.")
                gorsel_adi = _gorsel_kaydet(veri)
            if not veri and not (istek.metin or "").strip():
                raise HTTPException(422, "Bir görsel ya da soru metni gönderin.")
            a = sg.analiz_et(vt, veri, istek.metin, istek.ders, istek.sinif_duzeyi)
    except TanimadiHatasi as e:
        raise HTTPException(422, str(e))
    except (httpx.HTTPError, RuntimeError, KeyError, ValueError) as e:  # Azure/Claude servis hatası
        raise HTTPException(502, f"Yapay zekâ servisi yanıt vermedi ya da beklenmeyen yanıt verdi: {str(e)[:200]}")
    adimlar = [AdimG(**x) for x in a.adimlar]
    return AnalizC(
        ders=a.ders, sinif_duzeyi=a.sinif_duzeyi, metin=a.metin, gorsel=gorsel_adi, cevap_bicimi=a.cevap_bicimi,
        secenekler=[SecenekG(**x) for x in a.secenekler], dogru_cevap=a.dogru_cevap, cozum=a.cozum,
        birincil=a.birincil, adimlar=adimlar, eslesme=_esle(vt, a.ders, adimlar, a.birincil), saglayici=sg.ad,
        notlar=a.notlar,
    )


class EsleIstek(BaseModel):
    ders: str
    adimlar: list[AdimG]
    birincil: str | None = None


@router.post("/esle", response_model=EslemeC)
def yeniden_esle(istek: EsleIstek, _: Kullanici = Depends(ogretmen), vt: Session = Depends(vt_oturumu)):
    """Öğretmen bir adımın MK'sini değiştirince sorunun MK'lerini, zorluğu ve payları yeniden hesaplar."""
    return _esle(vt, istek.ders, istek.adimlar, istek.birincil)


@router.post("", response_model=SoruC, status_code=status.HTTP_201_CREATED)
def kaydet(g: SoruG, k: Kullanici = Depends(ogretmen), vt: Session = Depends(vt_oturumu)):
    s = Soru(olusturan_id=k.id, kaynak="yuklendi", durum="taslak", metin="", ders=g.ders, sinif_duzeyi=g.sinif_duzeyi,
             cevap_bicimi=g.cevap_bicimi)
    _yaz(vt, s, g)
    vt.add(s)
    vt.commit()
    return _soru_cikti(vt, s)


@router.get("", response_model=list[SoruKisa])
def liste(ders: str | None = None, sinif: int | None = None, mk: str | None = None, durum: str | None = None,
          k: Kullanici = Depends(ogretmen), vt: Session = Depends(vt_oturumu)):
    q = select(Soru).where(Soru.olusturan_id == k.id)
    if ders:
        q = q.where(Soru.ders == ders)
    if sinif:
        q = q.where(Soru.sinif_duzeyi == sinif)
    if durum:
        q = q.where(Soru.durum == durum)
    if mk:
        q = q.where(Soru.id.in_(select(SoruMK.soru_id).where(SoruMK.mk_kod == mk)))
    return [soru_kisa(s) for s in vt.scalars(q.order_by(Soru.olusturma.desc()))]


@router.get("/{soru_id}", response_model=SoruC)
def ayrinti(soru_id: int, k: Kullanici = Depends(ogretmen), vt: Session = Depends(vt_oturumu)):
    return _soru_cikti(vt, _sahibi(vt, soru_id, k))


@router.put("/{soru_id}", response_model=SoruC)
def guncelle(soru_id: int, g: SoruG, k: Kullanici = Depends(ogretmen), vt: Session = Depends(vt_oturumu)):
    s = _sahibi(vt, soru_id, k)
    _yaz(vt, s, g)
    s.durum = "taslak"  # değişen soru yeniden onaylanır
    vt.commit()
    return _soru_cikti(vt, s)


@router.post("/{soru_id}/onayla", response_model=SoruC)
def onayla(soru_id: int, k: Kullanici = Depends(ogretmen), vt: Session = Depends(vt_oturumu)):
    s = _sahibi(vt, soru_id, k)
    s.durum = "onayli"
    vt.commit()
    return _soru_cikti(vt, s)


class TopluOnayIstek(BaseModel):
    idler: list[int] = Field(min_length=1)


@router.post("/toplu-onayla")
def toplu_onayla(istek: TopluOnayIstek, k: Kullanici = Depends(ogretmen), vt: Session = Depends(vt_oturumu)):
    """Seçilen soruları tek seferde onaylar. Yalnız öğretmenin kendi soruları onaylanır."""
    sorular = vt.scalars(select(Soru).where(Soru.id.in_(istek.idler), Soru.olusturan_id == k.id)).all()
    for s in sorular:
        s.durum = "onayli"
    vt.commit()
    return {"onaylanan": len(sorular)}


@router.delete("/{soru_id}", status_code=status.HTTP_204_NO_CONTENT)
def sil(soru_id: int, k: Kullanici = Depends(ogretmen), vt: Session = Depends(vt_oturumu)):
    vt.delete(_sahibi(vt, soru_id, k))
    vt.commit()


@gorsel_router.get("/{ad}")
def gorsel(ad: str):
    """Yüklenen görsel. Ad, içeriğin özetidir (tahmin edilemez). Sunucuya taşınırken yetki kontrolü eklenecek."""
    if "/" in ad or ".." in ad or not (YUKLEMELER / ad).is_file():
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Görsel bulunamadı.")
    return FileResponse(YUKLEMELER / ad)

