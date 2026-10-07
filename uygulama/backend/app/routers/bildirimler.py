"""Bildirimler (üst çubuktaki zil).

Öğrenci: açık olup henüz teslim etmediği sınavlar ("1 sınavın var") ve öğretmenin açıkladığı ama öğrencinin henüz
görmediği sonuçlar.
Öğretmen: öğrencilerin teslim ettiği ama öğretmenin henüz açmadığı sınavlar (süre dolunca kendiliğinden teslim
edilenler ve hiç açılmayıp boş teslim edilenler dahil). Teslim ayrıntısı açılınca ya da "tümünü okundu say" denince
bildirim düşer. Bekleyen süre uzatma talepleri, öğretmen karar verene kadar durur.
Öğrenci ayrıca uzatma talebine verilen kararı görür (sınavı açınca düşer).
"""

from datetime import datetime

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..kimlik import gecerli_kullanici
from ..modeller import Atama, Kullanici, Sinav, SinifUye, Teslim
from ..vt import vt_oturumu
from .sinavlar import _durum, _utc

router = APIRouter(prefix="/api/bildirimler", tags=["bildirimler"])


class Bildirim(BaseModel):
    tur: str  # acik_sinav / sonuc / teslim / uzatma / uzatma_sonuc
    metin: str
    baglanti: str
    zaman: datetime
    son: datetime | None = None  # açık sınavın bitişi


class Bildirimler(BaseModel):
    sayi: int
    ogeler: list[Bildirim]


@router.get("", response_model=Bildirimler)
def bildirimler(k: Kullanici = Depends(gecerli_kullanici), vt: Session = Depends(vt_oturumu)):
    ogeler: list[Bildirim] = []
    from .teslim import sure_dolanlari_teslim_et
    sure_dolanlari_teslim_et(vt)
    if k.rol == "ogrenci":
        atamalar = vt.scalars(select(Atama).where(Atama.sinif_id.in_(select(SinifUye.sinif_id).where(SinifUye.ogrenci_id == k.id))))
        teslimler = {t.atama_id: t for t in vt.scalars(select(Teslim).where(Teslim.ogrenci_id == k.id))}
        for a in atamalar:
            t = teslimler.get(a.id)
            if t and t.degerlendirme == "onayli" and not t.ogrenci_gordu:
                ogeler.append(Bildirim(tur="sonuc", baglanti=f"/sonuc/{a.id}", zaman=_utc(t.sonuc_zamani or a.bitis),
                                       metin=f"“{a.sinav.ad}” sınavının sonucu açıklandı: {t.puan:.2f} / {t.en_yuksek:.2f}."))
            if t and t.uzatma in ("verildi", "reddedildi") and not t.uzatma_ogrenci_gordu:
                ogeler.append(Bildirim(tur="uzatma_sonuc", baglanti=f"/sinav/{a.id}", zaman=_utc(t.uzatma_zamani),
                                       metin=f"“{a.sinav.ad}” için {t.uzatma_dk} dakika ek süre verildi; sınavına devam edebilirsin."
                                       if t.uzatma == "verildi" else f"“{a.sinav.ad}” için süre uzatma talebin kabul edilmedi; sınavın teslim edildi."))
            if t and t.uzatma == "verildi" and t.durum == "devam":
                continue  # açık sınav bildirimi yerine yukarıdaki
            if _durum(a) == "acik" and (not t or t.durum != "teslim"):
                ogeler.append(Bildirim(tur="acik_sinav", baglanti=f"/sinav/{a.id}", zaman=_utc(a.baslangic),
                                       metin=f"“{a.sinav.ad}” sınavın açık ({'devam ediyorsun' if t else 'henüz başlamadın'}).",
                                       son=_utc(a.bitis)))
    elif k.rol == "ogretmen":
        q = (select(Teslim).join(Atama).join(Sinav)
             .where(Sinav.olusturan_id == k.id, Teslim.durum == "teslim", Teslim.ogretmen_gordu.is_(False)))
        for t in vt.scalars(q):
            bos = not any(c.secilen or c.metin.strip() or c.dosyalar for c in t.cevaplar) and not t.genel_dosyalar
            ad, sinav, sinif = t.ogrenci.ad, t.atama.sinav.ad, t.atama.sinif.ad
            metin = (f"{ad}, “{sinav}” sınavını teslim etti ({sinif})." if not t.otomatik_teslim
                     else f"{ad}, “{sinav}”: süre doldu, boş kâğıt olarak teslim edildi ({sinif})." if bos
                     else f"{ad}, “{sinav}”: süre doldu, cevapları kendiliğinden teslim edildi ({sinif}).")
            ogeler.append(Bildirim(tur="teslim", baglanti=f"/atama/{t.atama_id}/teslimler", zaman=_utc(t.teslim_zamani), metin=metin))
        for t in vt.scalars(select(Teslim).join(Atama).join(Sinav).where(Sinav.olusturan_id == k.id, Teslim.uzatma == "bekliyor")):
            ogeler.append(Bildirim(tur="uzatma", baglanti=f"/atama/{t.atama_id}/teslimler", zaman=_utc(t.uzatma_zamani),
                                   metin=f"{t.ogrenci.ad}, “{t.atama.sinav.ad}” için süre uzatma istiyor ({t.atama.sinif.ad})"
                                   + (f": “{t.uzatma_notu}”" if t.uzatma_notu else ".")))
    ogeler.sort(key=lambda b: b.zaman, reverse=True)
    return Bildirimler(sayi=len(ogeler), ogeler=ogeler)


@router.post("/okundu")
def okundu(k: Kullanici = Depends(gecerli_kullanici), vt: Session = Depends(vt_oturumu)):
    """Öğretmenin teslim bildirimlerini okundu sayar. Öğrencinin açık sınav bildirimi, sınavı teslim edince düşer."""
    n = 0
    if k.rol == "ogretmen":
        for t in vt.scalars(select(Teslim).join(Atama).join(Sinav).where(Sinav.olusturan_id == k.id, Teslim.durum == "teslim",
                                                                         Teslim.ogretmen_gordu.is_(False))):
            t.ogretmen_gordu = True
            n += 1
        vt.commit()
    return {"okundu": n}
