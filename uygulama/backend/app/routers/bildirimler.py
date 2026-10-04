"""Bildirimler (üst çubuktaki zil).

Öğrenci: açık olup henüz teslim etmediği sınavlar ("1 sınavın var") ve öğretmenin açıkladığı ama öğrencinin henüz
görmediği sonuçlar.
Öğretmen: öğrencilerin teslim ettiği ama öğretmenin henüz açmadığı sınavlar. Teslim ayrıntısı açılınca ya da
"tümünü okundu say" denince bildirim düşer.
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
    tur: str  # acik_sinav / sonuc / teslim
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
    if k.rol == "ogrenci":
        atamalar = vt.scalars(select(Atama).where(Atama.sinif_id.in_(select(SinifUye.sinif_id).where(SinifUye.ogrenci_id == k.id))))
        teslimler = {t.atama_id: t for t in vt.scalars(select(Teslim).where(Teslim.ogrenci_id == k.id))}
        for a in atamalar:
            t = teslimler.get(a.id)
            if t and t.degerlendirme == "onayli" and not t.ogrenci_gordu:
                ogeler.append(Bildirim(tur="sonuc", baglanti=f"/sonuc/{a.id}", zaman=_utc(t.sonuc_zamani or a.bitis),
                                       metin=f"“{a.sinav.ad}” sınavının sonucu açıklandı: {t.puan:.2f} / {t.en_yuksek:.2f}."))
            if _durum(a) == "acik" and (not t or t.durum != "teslim"):
                ogeler.append(Bildirim(tur="acik_sinav", baglanti=f"/sinav/{a.id}", zaman=_utc(a.baslangic),
                                       metin=f"“{a.sinav.ad}” sınavın açık ({'devam ediyorsun' if t else 'henüz başlamadın'}).",
                                       son=_utc(a.bitis)))
    elif k.rol == "ogretmen":
        q = (select(Teslim).join(Atama).join(Sinav)
             .where(Sinav.olusturan_id == k.id, Teslim.durum == "teslim", Teslim.ogretmen_gordu.is_(False)))
        for t in vt.scalars(q):
            ogeler.append(Bildirim(tur="teslim", baglanti=f"/atama/{t.atama_id}/teslimler", zaman=_utc(t.teslim_zamani),
                                   metin=f"{t.ogrenci.ad}, “{t.atama.sinav.ad}” sınavını teslim etti ({t.atama.sinif.ad})."))
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
