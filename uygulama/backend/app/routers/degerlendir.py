"""Değerlendirme: öğretmenin teslimi rubrik adımlarına göre incelemesi ve onaylaması; öğrencinin sonucu görmesi."""

from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..degerlendirme import ADIM_DURUMLARI_GECERLI, cevap_puani, degerlendirilmis_mi, ogretmen as ogretmen_karari, otomatik
from ..kimlik import rol_gerekli
from ..modeller import AdimDegerlendirme, Atama, Cevap, Kullanici, Soru, Teslim, VideoIzleme, VideoParca, Yanilgi
from ..vt import vt_oturumu
from .sorular import harita
from .teslim import DosyaC, _atama_ogrenci, _atama_ogretmen

router = APIRouter(tags=["degerlendirme"])
ogretmen = rol_gerekli("ogretmen")
ogrenci = rol_gerekli("ogrenci")


class AdimSonuc(BaseModel):
    adim_id: int
    sira: int
    aciklama: str
    mk_kod: str
    mk_ifade: str
    soru_mk_mi: bool
    pay: float
    en_yuksek: float
    durum: str | None  # biliyor / bilmiyor / olculemedi / None (karar yok)
    puan: float
    kaynak: str | None
    gerekce: str


class SoruSonuc(BaseModel):
    sira: int
    soru_id: int
    metin: str
    gorsel: str | None
    cevap_bicimi: str
    secenekler: list[dict]
    dogru_cevap: str
    cozum: str
    zorluk: float
    secilen: str | None
    metin_cevap: str
    dosyalar: list[DosyaC]
    yanilgi: str | None
    ogretmen_notu: str  # öğrenciye açıklama
    aciklama_kaynak: str  # sistem / ogretmen
    adimlar: list[AdimSonuc]
    puan: float
    tamam: bool  # bütün adımlara karar verilmiş mi


class MKSonuc(BaseModel):
    kod: str
    ifade: str
    durum: str  # biliyor / bilmiyor / olculemedi
    kanit: int  # bu MK'ye bağlı adım sayısı


class DegerlendirmeC(BaseModel):
    teslim_id: int
    ogrenci: str
    sinav_adi: str
    degerlendirme: str
    teslim_zamani: datetime | None
    puan: float
    en_yuksek: float
    sorular: list[SoruSonuc]
    mkler: list[MKSonuc]
    genel_dosyalar: list[DosyaC] = []  # sınavın tamamı için yüklenen dosyalar (sorulara ayrılmamış)
    genel_geri_bildirim: str = ""
    genel_kaynak: str = "ogretmen"


class KararIstek(BaseModel):
    kararlar: dict[int, str]  # rubrik adım id → durum
    gerekceler: dict[int, str] = {}
    not_: str | None = Field(None, alias="not")


def _sonuc(vt: Session, a: Atama, t: Teslim) -> DegerlendirmeC:
    h = harita(vt)
    cevaplar = {c.soru_id: c for c in t.cevaplar}
    sorular, toplam, en_yuksek = [], 0.0, 0.0
    mk_kanit: dict[str, list[str]] = {}
    for x in a.sinav.sorular:
        q, c = x.soru, cevaplar.get(x.soru_id)
        ust = {m.mk_kod for m in q.mkler}
        kararlar = {d.rubrik_adim_id: d for d in c.adimlar} if c else {}
        adimlar = []
        for ad in q.adimlar:
            d = kararlar.get(ad.id)
            adimlar.append(AdimSonuc(adim_id=ad.id, sira=ad.sira, aciklama=ad.aciklama, mk_kod=ad.mk_kod,
                                     mk_ifade=h.mk[ad.mk_kod].ifade if ad.mk_kod in h.mk else "", soru_mk_mi=ad.mk_kod in ust,
                                     pay=ad.pay, en_yuksek=round((q.zorluk or 0) * ad.pay, 2), durum=d.durum if d else None,
                                     puan=round(d.puan, 2) if d else 0.0, kaynak=d.kaynak if d else None, gerekce=d.gerekce if d else ""))
            if d:
                mk_kanit.setdefault(ad.mk_kod, []).append(d.durum)
        puan = cevap_puani(c)
        toplam += puan
        en_yuksek += q.zorluk or 0
        sorular.append(SoruSonuc(
            sira=x.sira, soru_id=q.id, metin=q.metin, gorsel=q.gorsel, cevap_bicimi=q.cevap_bicimi,
            secenekler=[{"harf": s.harf, "metin": s.metin, "dogru": s.dogru} for s in q.secenekler],
            dogru_cevap=q.dogru_cevap, cozum=q.cozum, zorluk=q.zorluk or 0, secilen=c.secilen if c else None,
            metin_cevap=c.metin if c else "", dosyalar=[DosyaC(id=d.id, dosya=d.dosya, kaynak=d.kaynak) for d in c.dosyalar] if c else [],
            yanilgi=(h_yanilgi(vt, c.yanilgi_kod) if c and c.yanilgi_kod else None), ogretmen_notu=c.ogretmen_notu if c else "", aciklama_kaynak=c.aciklama_kaynak if c else "ogretmen",
            adimlar=adimlar, puan=puan, tamam=degerlendirilmis_mi(c, q)))
    # MK durumu: bir MK'nin herhangi bir adımı 'bilmiyor' ise bilmiyor; hepsi 'biliyor' ise biliyor; aksi hâlde ölçülemedi
    mkler = []
    for kod, durumlar in sorted(mk_kanit.items()):
        durum = "bilmiyor" if "bilmiyor" in durumlar else "biliyor" if all(d == "biliyor" for d in durumlar) else (
            "biliyor" if "biliyor" in durumlar else "olculemedi")
        mkler.append(MKSonuc(kod=kod, ifade=h.mk[kod].ifade if kod in h.mk else "", durum=durum, kanit=len(durumlar)))
    return DegerlendirmeC(teslim_id=t.id, ogrenci=t.ogrenci.ad, sinav_adi=a.sinav.ad, degerlendirme=t.degerlendirme,
                          teslim_zamani=t.teslim_zamani, puan=round(toplam, 2), en_yuksek=round(en_yuksek, 2), sorular=sorular, mkler=mkler,
                          genel_dosyalar=[DosyaC(id=d.id, dosya=d.dosya) for d in t.genel_dosyalar],
                          genel_geri_bildirim=t.genel_geri_bildirim or "", genel_kaynak=t.genel_kaynak or "ogretmen")


def h_yanilgi(vt: Session, kod: str) -> str:
    y = vt.get(Yanilgi, kod)
    return f"{kod}: {y.ifade}" if y else kod


def _teslim(vt: Session, a: Atama, teslim_id: int) -> Teslim:
    t = vt.get(Teslim, teslim_id)
    if not t or t.atama_id != a.id:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Teslim bulunamadı.")
    return t


@router.get("/api/atamalar/{atama_id}/teslimler/{teslim_id}/degerlendirme", response_model=DegerlendirmeC)
def degerlendirme(atama_id: int, teslim_id: int, k: Kullanici = Depends(ogretmen), vt: Session = Depends(vt_oturumu)):
    a = _atama_ogretmen(vt, atama_id, k)
    t = _teslim(vt, a, teslim_id)
    degisti = False
    for c in t.cevaplar:  # eski teslimlerde otomatik değerlendirme yoksa şimdi yap
        q = vt.get(Soru, c.soru_id)
        if q.cevap_bicimi == "coktan_secmeli" and not c.adimlar:
            degisti |= otomatik(vt, c, q)
    if t.durum == "teslim" and not t.ogretmen_gordu:
        t.ogretmen_gordu, degisti = True, True
    if degisti:
        vt.commit()
    return _sonuc(vt, a, t)


@router.put("/api/atamalar/{atama_id}/teslimler/{teslim_id}/soru/{soru_id}", response_model=DegerlendirmeC)
def karar_ver(atama_id: int, teslim_id: int, soru_id: int, istek: KararIstek, k: Kullanici = Depends(ogretmen),
              vt: Session = Depends(vt_oturumu)):
    a = _atama_ogretmen(vt, atama_id, k)
    t = _teslim(vt, a, teslim_id)
    if soru_id not in {x.soru_id for x in a.sinav.sorular}:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Bu soru sınavda yok.")
    if any(d not in ADIM_DURUMLARI_GECERLI for d in istek.kararlar.values()):
        raise HTTPException(422, "Adım durumu biliyor, bilmiyor ya da olculemedi olmalı.")
    q = vt.get(Soru, soru_id)
    c = next((c for c in t.cevaplar if c.soru_id == soru_id), None)
    if not c:
        c = Cevap(soru_id=soru_id)
        t.cevaplar.append(c)
        vt.flush()
    ogretmen_karari(vt, c, q, {int(i): d for i, d in istek.kararlar.items()}, {int(i): g for i, g in istek.gerekceler.items()})
    if istek.not_ is not None:
        c.ogretmen_notu, c.aciklama_kaynak = istek.not_, "ogretmen"
    if t.degerlendirme == "onayli":  # onaylıyken değişirse puan da güncellenir
        t.puan = _sonuc(vt, a, t).puan
    vt.commit()
    return _sonuc(vt, a, t)


class GenelIstek(BaseModel):
    metin: str


@router.put("/api/atamalar/{atama_id}/teslimler/{teslim_id}/genel", response_model=DegerlendirmeC)
def genel_geri_bildirim(atama_id: int, teslim_id: int, istek: GenelIstek, k: Kullanici = Depends(ogretmen),
                        vt: Session = Depends(vt_oturumu)):
    a = _atama_ogretmen(vt, atama_id, k)
    t = _teslim(vt, a, teslim_id)
    t.genel_geri_bildirim, t.genel_kaynak = istek.metin, "ogretmen"
    vt.commit()
    return _sonuc(vt, a, t)


@router.post("/api/atamalar/{atama_id}/teslimler/{teslim_id}/onayla", response_model=DegerlendirmeC)
def onayla(atama_id: int, teslim_id: int, k: Kullanici = Depends(ogretmen), vt: Session = Depends(vt_oturumu)):
    """Kararı olmayan adımlar 'olculemedi' olur (boş bırakılmış), puan yazılır, sonuç öğrenciye açılır."""
    a = _atama_ogretmen(vt, atama_id, k)
    t = _teslim(vt, a, teslim_id)
    if t.durum != "teslim":
        raise HTTPException(status.HTTP_409_CONFLICT, "Öğrenci henüz teslim etmedi.")
    cevaplar = {c.soru_id: c for c in t.cevaplar}
    for x in a.sinav.sorular:
        c = cevaplar.get(x.soru_id)
        if not c:
            c = Cevap(soru_id=x.soru_id)
            t.cevaplar.append(c)
            vt.flush()
        kararli = {d.rubrik_adim_id for d in c.adimlar}
        for ad in x.soru.adimlar:
            if ad.id not in kararli:
                c.adimlar.append(AdimDegerlendirme(rubrik_adim_id=ad.id, durum="olculemedi", puan=0.0, kaynak="otomatik",
                                                   gerekce="Karar verilmedi; ölçülemedi sayıldı."))
    vt.flush()
    s = _sonuc(vt, a, t)
    t.puan, t.en_yuksek, t.degerlendirme = s.puan, s.en_yuksek, "onayli"
    t.sonuc_zamani, t.ogrenci_gordu = datetime.now(timezone.utc), False  # öğrenciye bildirim gider
    vt.commit()
    return _sonuc(vt, a, t)


@router.post("/api/atamalar/{atama_id}/teslimler/{teslim_id}/geri-al", response_model=DegerlendirmeC)
def geri_al(atama_id: int, teslim_id: int, k: Kullanici = Depends(ogretmen), vt: Session = Depends(vt_oturumu)):
    a = _atama_ogretmen(vt, atama_id, k)
    t = _teslim(vt, a, teslim_id)
    t.degerlendirme = "bekliyor"
    vt.commit()
    return _sonuc(vt, a, t)


class VideoC(BaseModel):
    id: int
    video_id: str
    kanal: str
    baslik: str
    bas: int
    son: int
    kapak: str  # YouTube kapak görseli adı. Kanalın kendi kapağı (hqdefault): otomatik kareler (hq1–3) videonun
    # sabit %25/50/75 noktalarından alınıyor ve parçayla çoğu zaman ilgisiz çıkıyor (denendi, 2026-10-04).


def _kapak(vp: VideoParca) -> str:
    return "hqdefault"


class KonuKarti(BaseModel):
    """Bir eksik konu için kart: öğrenci konu anlatımını ya da benzer soru çözümünü seçer."""

    konu: str
    anlatim: VideoC | None
    soru: VideoC | None


class OgrenciSoru(BaseModel):
    sira: int
    metin: str
    gorsel: str | None
    cevap_bicimi: str
    secenekler: list[dict]  # {harf, metin} (doğru şık işaretsiz)
    secilen: str | None
    dogru_sik: str | None
    senin_cevabin: str  # öğrencinin yazdığı ya da kâğıttan okunan
    dosyalar: list[DosyaC]
    dogru_cevap: str
    cozum: str
    durum: str  # dogru / kismen / yanlis / bos
    puan: float
    en_yuksek: float
    aciklama: str  # nerede hata yaptın (öğretmen diliyle)
    konular: list[KonuKarti] = []  # bu sorudaki eksik konular için video kartları


class OgrenciSonucC(BaseModel):
    sinav_adi: str
    puan: float
    en_yuksek: float
    genel_geri_bildirim: str
    sorular: list[OgrenciSoru]
    calis: list[str]  # tekrar çalışılacak konular (bilinmeyen MK'ler, öğrenci diliyle, temelden üste)


_OKUNAN = "[Yüklenen kâğıttan okundu] "


def _ogrenci_sonucu(vt: Session, a: Atama, t: Teslim) -> OgrenciSonucC:
    """Öğrencinin göreceği sonuç: rubrik, MK kodu, adım puanı ve teknik gerekçe içermez."""
    d = _sonuc(vt, a, t)
    h = harita(vt)
    parcalar: dict[tuple[str, str], VideoParca] = {}  # (MK, tür) -> en öncelikli onaylı parça
    for vp in vt.scalars(select(VideoParca).where(VideoParca.onayli).order_by(VideoParca.sira.desc())):
        parcalar[(vp.mk_kod, vp.tur)] = vp

    def vc(vp: VideoParca | None) -> VideoC | None:
        return vp and VideoC(id=vp.id, video_id=vp.video_id, kanal=vp.kanal, baslik=vp.baslik, bas=vp.bas, son=vp.son,
                             kapak=_kapak(vp))

    gosterilen: set[str] = set()
    sorular = []
    for s in d.sorular:
        bos = not s.secilen and not s.metin_cevap.strip() and not s.dosyalar
        durum = "bos" if bos else "dogru" if s.puan >= s.zorluk - 0.01 else "yanlis" if s.puan <= 0.01 else "kismen"
        # Bu sorunun bilinmeyen adımlarındaki MK'ler, temelden üste; her MK bir kart, soru başına en çok 3, sınavda bir kez.
        eksik = sorted({x.mk_kod for x in s.adimlar if x.durum == "bilmiyor"} - gosterilen,
                       key=lambda k: h.mk[k].zorluk if k in h.mk else 0)
        konular = []
        for k in eksik:
            anlatim, ornek = parcalar.get((k, "konu")), parcalar.get((k, "soru"))
            if (anlatim or ornek) and len(konular) < 3:
                konular.append(KonuKarti(konu=(anlatim or ornek).konu or h.mk[k].ifade.rstrip("."), anlatim=vc(anlatim), soru=vc(ornek)))
                gosterilen.add(k)
        sorular.append(OgrenciSoru(
            sira=s.sira, metin=s.metin, gorsel=s.gorsel, cevap_bicimi=s.cevap_bicimi,
            secenekler=[{"harf": x["harf"], "metin": x["metin"]} for x in s.secenekler], secilen=s.secilen,
            dogru_sik=next((x["harf"] for x in s.secenekler if x["dogru"]), None),
            senin_cevabin=s.metin_cevap.removeprefix(_OKUNAN), dosyalar=s.dosyalar, dogru_cevap=s.dogru_cevap, cozum=s.cozum,
            durum=durum, puan=s.puan, en_yuksek=round(s.zorluk, 2), aciklama=s.ogretmen_notu, konular=konular))
    eksik = [m.kod for m in d.mkler if m.durum == "bilmiyor"]
    eksik.sort(key=lambda k: h.mk[k].zorluk or 0)  # temelden üste
    calis = [h.mk[k].ifade.rstrip(".") for k in eksik if k in h.mk]
    return OgrenciSonucC(sinav_adi=d.sinav_adi, puan=d.puan, en_yuksek=d.en_yuksek, genel_geri_bildirim=d.genel_geri_bildirim,
                         sorular=sorular, calis=calis)


@router.get("/api/teslim/{atama_id}/sonuc", response_model=OgrenciSonucC)
def sonuc(atama_id: int, k: Kullanici = Depends(ogrenci), vt: Session = Depends(vt_oturumu)):
    """Öğrencinin sonucu: yalnız öğretmen değerlendirmeyi onayladıktan sonra."""
    a = _atama_ogrenci(vt, atama_id, k)
    t = vt.scalar(select(Teslim).where(Teslim.atama_id == a.id, Teslim.ogrenci_id == k.id))
    if not t or t.degerlendirme != "onayli":
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Sonuç henüz açıklanmadı.")
    if not t.ogrenci_gordu:
        t.ogrenci_gordu = True
        vt.commit()
    return _ogrenci_sonucu(vt, a, t)


class IzleIstek(BaseModel):
    teslim_atama_id: int | None = None


@router.post("/api/video/{parca_id}/izle", status_code=204)
def izle(parca_id: int, istek: IzleIstek, k: Kullanici = Depends(ogrenci), vt: Session = Depends(vt_oturumu)):
    """Öğrencinin bir video parçasını açtığını kaydeder (anlatım mı, benzer soru mu tercih ediyor)."""
    if not vt.get(VideoParca, parca_id):
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Video parçası bulunamadı.")
    t = istek.teslim_atama_id and vt.scalar(select(Teslim).where(Teslim.atama_id == istek.teslim_atama_id, Teslim.ogrenci_id == k.id))
    vt.add(VideoIzleme(ogrenci_id=k.id, parca_id=parca_id, teslim_id=t.id if t else None))
    vt.commit()
