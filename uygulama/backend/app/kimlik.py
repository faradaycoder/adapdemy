"""Şifre özetleme, oturum jetonu ve yetki kontrolü.

Şifre: PBKDF2-HMAC-SHA256, kullanıcıya özel tuz, 600.000 tekrar (OWASP 2023 önerisi).
Jeton: imzalı ve süreli; içerik base64(JSON), imza HMAC-SHA256. Yalnızca standart kütüphane kullanılır.
"""

import base64
import hashlib
import hmac
import json
import secrets
import time

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from .ayarlar import GIZLI_ANAHTAR, JETON_SURESI_SN
from .modeller import Kullanici
from .vt import vt_oturumu

_TEKRAR = 600_000


def sifre_ozetle(sifre: str) -> str:
    tuz = secrets.token_bytes(16)
    ozet = hashlib.pbkdf2_hmac("sha256", sifre.encode(), tuz, _TEKRAR)
    return f"pbkdf2_sha256${_TEKRAR}${tuz.hex()}${ozet.hex()}"


def sifre_dogru(sifre: str, kayitli: str | None) -> bool:
    if not kayitli:
        return False
    try:
        _, tekrar, tuz, ozet = kayitli.split("$")
        yeni = hashlib.pbkdf2_hmac("sha256", sifre.encode(), bytes.fromhex(tuz), int(tekrar))
        return hmac.compare_digest(yeni.hex(), ozet)
    except ValueError:
        return False


def _b64(b: bytes) -> str:
    return base64.urlsafe_b64encode(b).rstrip(b"=").decode()


def _b64_coz(s: str) -> bytes:
    return base64.urlsafe_b64decode(s + "=" * (-len(s) % 4))


def jeton_uret(kullanici_id: int) -> str:
    govde = _b64(json.dumps({"k": kullanici_id, "s": int(time.time()) + JETON_SURESI_SN}).encode())
    imza = _b64(hmac.new(GIZLI_ANAHTAR.encode(), govde.encode(), hashlib.sha256).digest())
    return f"{govde}.{imza}"


def jeton_coz(jeton: str) -> int | None:
    try:
        govde, imza = jeton.split(".")
        beklenen = _b64(hmac.new(GIZLI_ANAHTAR.encode(), govde.encode(), hashlib.sha256).digest())
        if not hmac.compare_digest(imza, beklenen):
            return None
        veri = json.loads(_b64_coz(govde))
        if veri["s"] < time.time():
            return None
        return int(veri["k"])
    except (ValueError, KeyError, json.JSONDecodeError):
        return None


_tasiyici = HTTPBearer(auto_error=False)


def gecerli_kullanici(
    kimlik: HTTPAuthorizationCredentials | None = Depends(_tasiyici),
    vt: Session = Depends(vt_oturumu),
) -> Kullanici:
    kid = jeton_coz(kimlik.credentials) if kimlik else None
    kullanici = vt.get(Kullanici, kid) if kid else None
    if not kullanici or not kullanici.aktif:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Oturum geçersiz ya da süresi dolmuş.")
    return kullanici


def rol_gerekli(*roller: str):
    def kontrol(k: Kullanici = Depends(gecerli_kullanici)) -> Kullanici:
        if k.rol not in roller:
            raise HTTPException(status.HTTP_403_FORBIDDEN, "Bu işlem için yetkiniz yok.")
        return k
    return kontrol
