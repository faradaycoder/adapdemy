"""Uygulama ayarları. Değerler ortam değişkenlerinden okunur; yoksa yerel geliştirme varsayılanları kullanılır."""

import os
import secrets
from pathlib import Path

BACKEND = Path(__file__).resolve().parent.parent
EVALORA_KOK = BACKEND.parent.parent  # MK verisinin (Fizik/, Matematik/, ortak/, araclar/) bulunduğu klasör
VERI = BACKEND / "veri"


def _env_yukle():
    """backend/.env dosyasındaki ANAHTAR=değer satırlarını ortama yükler (ortamda zaten olanları ezmez).
    Gizli anahtarlar (Azure, Anthropic) burada durur; dosya paylaşılmaz."""
    dosya = BACKEND / ".env"
    if not dosya.exists():
        return
    for satir in dosya.read_text(encoding="utf-8").splitlines():
        satir = satir.strip()
        if satir and not satir.startswith("#") and "=" in satir:
            ad, deger = satir.split("=", 1)
            if deger.strip():
                os.environ.setdefault(ad.strip(), deger.strip().strip('"').strip("'"))


if not os.environ.get("EVALORA_ENV_YOK"):  # testler gerçek anahtarları yüklemesin diye
    _env_yukle()
VERI.mkdir(exist_ok=True)

# Yerelde SQLite; sunucuya taşınırken DATABASE_URL ile PostgreSQL verilir (postgresql+psycopg://...).
DATABASE_URL = os.environ.get("DATABASE_URL", f"sqlite:///{VERI / 'evalora.db'}")


def _gizli_anahtar():
    """Oturum jetonlarını imzalayan anahtar. Ortamda yoksa bir kez üretilip dosyada saklanır."""
    if os.environ.get("EVALORA_SECRET"):
        return os.environ["EVALORA_SECRET"]
    dosya = VERI / ".gizli_anahtar"
    if not dosya.exists():
        dosya.write_text(secrets.token_urlsafe(48))
        dosya.chmod(0o600)
    return dosya.read_text().strip()


GIZLI_ANAHTAR = _gizli_anahtar()
JETON_SURESI_SN = int(os.environ.get("EVALORA_JETON_SURESI_SN", 60 * 60 * 24 * 7))  # 7 gün

# Ön yüzün çalıştığı adresler (geliştirmede Vite)
IZINLI_KOKENLER = os.environ.get("EVALORA_KOKENLER", "http://localhost:5173,http://127.0.0.1:5173").split(",")
