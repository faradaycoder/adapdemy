"""EVALORA arka ucu. Çalıştırma (backend klasöründe):  uvicorn app.main:app --reload"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import func, inspect, select, text

from . import modeller  # noqa: F401  (tabloları kaydeder)
from .ayarlar import IZINLI_KOKENLER
from .mk_aktar import aktar
from .routers import bildirimler, degerlendir, hesap, mk, ozet, raporlar, siniflar, sinavlar, sorular, teslim
from .vt import Oturum, Taban, motor


def _eksik_sutunlari_ekle():
    """Var olan veritabanına sonradan eklenen sütunlar (küçük, elle göç; ileride Alembic)."""
    eklenecek = {
        "teslim": [("ogretmen_gordu", "BOOLEAN DEFAULT 0"), ("degerlendirme", "VARCHAR(16) DEFAULT 'bekliyor'"),
                   ("puan", "FLOAT"), ("en_yuksek", "FLOAT"), ("sonuc_zamani", "DATETIME"),
                   ("ogrenci_gordu", "BOOLEAN DEFAULT 0"), ("genel_geri_bildirim", "TEXT DEFAULT ''"),
                   ("genel_kaynak", "VARCHAR(12) DEFAULT 'ogretmen'")],
        "video_parca": [("video_sure", "INTEGER"), ("tur", "VARCHAR(8) DEFAULT 'konu'"), ("konu", "VARCHAR(200) DEFAULT ''")],
        "cevap": [("ogretmen_notu", "TEXT DEFAULT ''"), ("yanilgi_kod", "VARCHAR(16)"),
                  ("aciklama_kaynak", "VARCHAR(12) DEFAULT 'ogretmen'")],
        "cevap_dosya": [("kaynak", "VARCHAR(16) DEFAULT 'ogrenci'")],
    }
    with motor.begin() as b:
        for tablo, sutunlar in eklenecek.items():
            var = {s["name"] for s in inspect(b).get_columns(tablo)}
            for ad, tur in sutunlar:
                if ad not in var:
                    b.execute(text(f"ALTER TABLE {tablo} ADD COLUMN {ad} {tur}"))


@asynccontextmanager
async def yasam(_app):
    Taban.metadata.create_all(motor)
    _eksik_sutunlari_ekle()
    with Oturum() as vt:  # MK verisi hiç aktarılmamışsa ilk açılışta aktar
        if not vt.scalar(select(func.count()).select_from(modeller.MK)):
            aktar(vt)
    yield


app = FastAPI(title="EVALORA", description="Measure. Diagnose. Remediate. Micro-skill based assessment, diagnosis and remediation.", version="0.1.0", lifespan=yasam)
app.add_middleware(CORSMiddleware, allow_origins=IZINLI_KOKENLER, allow_credentials=True,
                   allow_methods=["*"], allow_headers=["*"])
app.include_router(hesap.router)
app.include_router(siniflar.router)
app.include_router(mk.router)
app.include_router(sorular.router)
app.include_router(sorular.gorsel_router)
app.include_router(sinavlar.router)
app.include_router(sinavlar.atama_router)
app.include_router(teslim.router)
app.include_router(teslim.ogretmen_router)
app.include_router(bildirimler.router)
app.include_router(degerlendir.router)
app.include_router(raporlar.router)
app.include_router(ozet.router)


@app.get("/api/saglik")
def saglik():
    return {"durum": "çalışıyor"}
