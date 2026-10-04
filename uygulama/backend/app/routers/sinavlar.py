"""Sınavlar: bankadaki onaylı sorulardan sınav oluşturma, soru önerisi, sınıfa atama (PLAN_UYGULAMA.md akış 2)."""

from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field, model_validator
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..kimlik import gecerli_kullanici, rol_gerekli
from ..modeller import Atama, Kullanici, MKEsleme, Sinav, SinavSoru, Sinif, SinifUye, Soru
from ..vt import vt_oturumu
from .sorular import SoruKisa, harita, soru_kisa

router = APIRouter(prefix="/api/sinavlar", tags=["sinavlar"])
atama_router = APIRouter(prefix="/api/atamalar", tags=["sinavlar"])
ogretmen = rol_gerekli("ogretmen")


def _utc(t: datetime) -> datetime:
    return t if t.tzinfo else t.replace(tzinfo=timezone.utc)


# ---------- şemalar ----------

class SinavG(BaseModel):
    ad: str = Field(min_length=1, max_length=160)
    ders: str = Field(pattern="^(Fizik|Matematik)$")
    sinif_duzeyi: int = Field(ge=5, le=12)
    aciklama: str = ""
    sure_dk: int | None = Field(None, ge=1, le=600)
    soru_idler: list[int] = []


class KapsamMK(BaseModel):
    kod: str
    ifade: str
    zorluk: float | None
    soru_sayisi: int


class AtamaC(BaseModel):
    id: int
    sinav_id: int
    sinav_adi: str
    sinif_id: int
    sinif_adi: str
    baslangic: datetime
    bitis: datetime
    durum: str  # baslamadi / acik / bitti
    soru_sayisi: int
    teslim_durumu: str | None = None  # öğrenci için: devam / teslim (başlamadıysa boş)
    sonuc_acik: bool = False  # öğrenci için: öğretmen değerlendirmeyi onayladı mı
    sonuc_yeni: bool = False  # öğrenci için: açıklanan sonucu henüz görmedi


class SinavC(BaseModel):
    id: int
    ad: str
    ders: str
    sinif_duzeyi: int
    aciklama: str
    sure_dk: int | None
    sorular: list[SoruKisa]
    toplam_zorluk: float
    kapsam: list[KapsamMK]  # sınavın ölçtüğü MK'ler (sorunun MK'leri)
    atamalar: list[AtamaC]


class SinavKisa(BaseModel):
    id: int
    ad: str
    ders: str
    sinif_duzeyi: int
    soru_sayisi: int
    toplam_zorluk: float
    atama_sayisi: int


class OneriIstek(BaseModel):
    ders: str
    sinif_duzeyi: int
    ogrenme_ciktisi: str | None = None
    mk_kodlari: list[str] = []
    adet: int = Field(10, ge=1, le=50)


class AtamaIstek(BaseModel):
    sinif_id: int
    baslangic: datetime
    bitis: datetime

    @model_validator(mode="after")
    def sira(self):
        if _utc(self.bitis) <= _utc(self.baslangic):
            raise ValueError("Bitiş, başlangıçtan sonra olmalı.")
        return self


# ---------- yardımcılar ----------

def _soru_kisa(s: Soru) -> SoruKisa:
    return soru_kisa(s)


def _durum(a: Atama) -> str:
    simdi = datetime.now(timezone.utc)
    return "baslamadi" if simdi < _utc(a.baslangic) else "bitti" if simdi > _utc(a.bitis) else "acik"


def _atama_c(a: Atama, teslim_durumu: str | None = None, sonuc_acik: bool = False, sonuc_yeni: bool = False) -> AtamaC:
    return AtamaC(id=a.id, sinav_id=a.sinav_id, sinav_adi=a.sinav.ad, sinif_id=a.sinif_id, sinif_adi=a.sinif.ad,
                  baslangic=_utc(a.baslangic), bitis=_utc(a.bitis), durum=_durum(a), soru_sayisi=len(a.sinav.sorular),
                  teslim_durumu=teslim_durumu, sonuc_acik=sonuc_acik, sonuc_yeni=sonuc_yeni)


def _sinav_c(vt: Session, s: Sinav) -> SinavC:
    sorular = [x.soru for x in s.sorular]
    sayac: dict[str, int] = {}
    for q in sorular:
        for m in q.mkler:
            sayac[m.mk_kod] = sayac.get(m.mk_kod, 0) + 1
    h = harita(vt)
    kapsam = [KapsamMK(kod=k, ifade=h.mk[k].ifade, zorluk=h.mk[k].zorluk, soru_sayisi=n)
              for k, n in sorted(sayac.items()) if k in h.mk]
    return SinavC(id=s.id, ad=s.ad, ders=s.ders, sinif_duzeyi=s.sinif_duzeyi, aciklama=s.aciklama, sure_dk=s.sure_dk,
                  sorular=[_soru_kisa(q) for q in sorular], toplam_zorluk=round(sum(q.zorluk or 0 for q in sorular), 2),
                  kapsam=kapsam, atamalar=[_atama_c(a) for a in s.atamalar])


def _sahibi(vt: Session, sinav_id: int, k: Kullanici) -> Sinav:
    s = vt.get(Sinav, sinav_id)
    if not s or s.olusturan_id != k.id:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Sınav bulunamadı.")
    return s


def _sorulari_yaz(vt: Session, s: Sinav, idler: list[int], k: Kullanici) -> None:
    sorular = {q.id: q for q in vt.scalars(select(Soru).where(Soru.id.in_(idler), Soru.olusturan_id == k.id))}
    eksik = [i for i in idler if i not in sorular]
    if eksik:
        raise HTTPException(422, f"Bu sorular bankanda yok: {eksik}")
    if s.id:
        s.sorular.clear()
        vt.flush()
    s.sorular = [SinavSoru(soru_id=i, sira=n + 1) for n, i in enumerate(dict.fromkeys(idler))]


# ---------- uç noktalar ----------

@router.get("", response_model=list[SinavKisa])
def liste(k: Kullanici = Depends(ogretmen), vt: Session = Depends(vt_oturumu)):
    return [SinavKisa(id=s.id, ad=s.ad, ders=s.ders, sinif_duzeyi=s.sinif_duzeyi, soru_sayisi=len(s.sorular),
                      toplam_zorluk=round(sum(x.soru.zorluk or 0 for x in s.sorular), 2), atama_sayisi=len(s.atamalar))
            for s in vt.scalars(select(Sinav).where(Sinav.olusturan_id == k.id).order_by(Sinav.olusturma.desc()))]


@router.post("", response_model=SinavC, status_code=status.HTTP_201_CREATED)
def olustur(g: SinavG, k: Kullanici = Depends(ogretmen), vt: Session = Depends(vt_oturumu)):
    s = Sinav(ad=g.ad.strip(), ders=g.ders, sinif_duzeyi=g.sinif_duzeyi, aciklama=g.aciklama, sure_dk=g.sure_dk, olusturan_id=k.id)
    _sorulari_yaz(vt, s, g.soru_idler, k)
    vt.add(s)
    vt.commit()
    return _sinav_c(vt, s)


@router.post("/oneri", response_model=list[SoruKisa])
def oneri(istek: OneriIstek, k: Kullanici = Depends(ogretmen), vt: Session = Depends(vt_oturumu)):
    """Bankadaki onaylı sorulardan öneri: istenen kazanım ya da MK'leri (ve onların öncüllerini) ölçen sorular,
    MK kapsamı geniş olacak biçimde sıralanır; zorluğa göre kolaydan zora dizilir."""
    q = select(Soru).where(Soru.olusturan_id == k.id, Soru.durum == "onayli", Soru.ders == istek.ders,
                           Soru.sinif_duzeyi <= istek.sinif_duzeyi)
    adaylar = list(vt.scalars(q))
    hedef: set[str] = set(istek.mk_kodlari)
    if istek.ogrenme_ciktisi:
        hedef |= set(vt.scalars(select(MKEsleme.mk_kod).where(MKEsleme.ogrenme_ciktisi == istek.ogrenme_ciktisi)))
    if hedef:
        h = harita(vt)
        genis = set(hedef)
        for kod in hedef:
            genis |= h.oncul(kod)
        adaylar = [s for s in adaylar if any(m.mk_kod in genis for m in s.mkler)]
    secilen, kapsanan = [], set()
    for s in sorted(adaylar, key=lambda s: -len({m.mk_kod for m in s.mkler})):  # açgözlü kapsama
        yeni = {m.mk_kod for m in s.mkler} - kapsanan
        if yeni or len(secilen) < istek.adet:
            secilen.append(s)
            kapsanan |= yeni
        if len(secilen) >= istek.adet:
            break
    return [_soru_kisa(s) for s in sorted(secilen, key=lambda s: s.zorluk or 0)]


@router.get("/{sinav_id}", response_model=SinavC)
def ayrinti(sinav_id: int, k: Kullanici = Depends(ogretmen), vt: Session = Depends(vt_oturumu)):
    return _sinav_c(vt, _sahibi(vt, sinav_id, k))


@router.put("/{sinav_id}", response_model=SinavC)
def guncelle(sinav_id: int, g: SinavG, k: Kullanici = Depends(ogretmen), vt: Session = Depends(vt_oturumu)):
    s = _sahibi(vt, sinav_id, k)
    s.ad, s.ders, s.sinif_duzeyi, s.aciklama, s.sure_dk = g.ad.strip(), g.ders, g.sinif_duzeyi, g.aciklama, g.sure_dk
    _sorulari_yaz(vt, s, g.soru_idler, k)
    vt.commit()
    return _sinav_c(vt, s)


@router.delete("/{sinav_id}", status_code=status.HTTP_204_NO_CONTENT)
def sil(sinav_id: int, k: Kullanici = Depends(ogretmen), vt: Session = Depends(vt_oturumu)):
    vt.delete(_sahibi(vt, sinav_id, k))
    vt.commit()


@router.post("/{sinav_id}/ata", response_model=AtamaC, status_code=status.HTTP_201_CREATED)
def ata(sinav_id: int, istek: AtamaIstek, k: Kullanici = Depends(ogretmen), vt: Session = Depends(vt_oturumu)):
    s = _sahibi(vt, sinav_id, k)
    if not s.sorular:
        raise HTTPException(422, "Sorusu olmayan sınav atanamaz.")
    taslak = [x.sira for x in s.sorular if x.soru.durum != "onayli"]
    if taslak:  # sınav taslak sorularla kaydedilebilir ama öğrenciye ancak bütün soruları onaylıyken gider
        raise HTTPException(422, f"Sınavda onaylanmamış sorular var ({', '.join(map(str, taslak))}. sorular). Önce onayla, sonra ata.")
    sinif = vt.get(Sinif, istek.sinif_id)
    if not sinif or sinif.ogretmen_id != k.id:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Sınıf bulunamadı.")
    a = Atama(sinav_id=s.id, sinif_id=sinif.id, baslangic=_utc(istek.baslangic), bitis=_utc(istek.bitis))
    vt.add(a)
    vt.commit()
    vt.refresh(a)
    return _atama_c(a)


@atama_router.get("", response_model=list[AtamaC])
def atamalarim(k: Kullanici = Depends(gecerli_kullanici), vt: Session = Depends(vt_oturumu)):
    """Öğretmen: kendi sınavlarının atamaları. Öğrenci: üyesi olduğu sınıflara atanan sınavlar."""
    if k.rol == "ogretmen":
        q = select(Atama).join(Sinav).where(Sinav.olusturan_id == k.id)
        return [_atama_c(a) for a in vt.scalars(q.order_by(Atama.baslangic.desc()))]
    q = select(Atama).where(Atama.sinif_id.in_(select(SinifUye.sinif_id).where(SinifUye.ogrenci_id == k.id)))
    sonuc = []
    for a in vt.scalars(q.order_by(Atama.baslangic.desc())):
        t = next((t for t in a.teslimler if t.ogrenci_id == k.id), None)
        acik = bool(t and t.degerlendirme == "onayli")
        sonuc.append(_atama_c(a, t.durum if t else None, acik, acik and not t.ogrenci_gordu))
    return sonuc


@atama_router.delete("/{atama_id}", status_code=status.HTTP_204_NO_CONTENT)
def atama_sil(atama_id: int, k: Kullanici = Depends(ogretmen), vt: Session = Depends(vt_oturumu)):
    a = vt.get(Atama, atama_id)
    if not a or a.sinav.olusturan_id != k.id:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Atama bulunamadı.")
    vt.delete(a)
    vt.commit()


class YazdirSoru(BaseModel):
    sira: int
    soru_id: int
    metin: str
    gorsel: str | None
    cevap_bicimi: str
    secenekler: list[dict]


class YazdirOgrenci(BaseModel):
    id: int
    ad: str


class YazdirC(BaseModel):
    sinav_id: int
    ad: str
    ders: str
    sinif_duzeyi: int
    aciklama: str
    sure_dk: int | None
    atama_id: int | None
    sinif_adi: str | None
    sorular: list[YazdirSoru]
    ogrenciler: list[YazdirOgrenci]  # atamalı yazdırmada sınıftaki öğrenciler (öğrenci başına kopya)


@router.get("/{sinav_id}/yazdir", response_model=YazdirC)
def yazdir(sinav_id: int, atama_id: int | None = None, k: Kullanici = Depends(ogretmen), vt: Session = Depends(vt_oturumu)):
    """Yazdırma görünümü verisi. Doğru cevap ve çözüm gönderilmez."""
    s = _sahibi(vt, sinav_id, k)
    a = vt.get(Atama, atama_id) if atama_id else None
    if atama_id and (not a or a.sinav_id != s.id):
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Atama bulunamadı.")
    return YazdirC(
        sinav_id=s.id, ad=s.ad, ders=s.ders, sinif_duzeyi=s.sinif_duzeyi, aciklama=s.aciklama, sure_dk=s.sure_dk,
        atama_id=a.id if a else None, sinif_adi=a.sinif.ad if a else None,
        sorular=[YazdirSoru(sira=x.sira, soru_id=x.soru.id, metin=x.soru.metin, gorsel=x.soru.gorsel,
                            cevap_bicimi=x.soru.cevap_bicimi,
                            secenekler=[{"harf": c.harf, "metin": c.metin} for c in x.soru.secenekler]) for x in s.sorular],
        ogrenciler=[YazdirOgrenci(id=u.ogrenci.id, ad=u.ogrenci.ad) for u in a.sinif.uyeler] if a else [],
    )

