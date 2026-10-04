"""Veritabanı bağlantısı ve oturum."""

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from .ayarlar import DATABASE_URL

_ek = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
motor = create_engine(DATABASE_URL, connect_args=_ek)
Oturum = sessionmaker(bind=motor, autoflush=False, expire_on_commit=False)


class Taban(DeclarativeBase):
    pass


def vt_oturumu():
    """FastAPI bağımlılığı: istek başına bir veritabanı oturumu."""
    vt = Oturum()
    try:
        yield vt
    finally:
        vt.close()
