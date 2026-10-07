"""MK ön koşul haritası: araclar/harita_uret.py'nin ürettiği tek dosyalık HTML (<Ders>/<Ders> Mikro Kazanım Haritası.html).

Uygulamada iframe içinde gösterilir; iframe yetki başlığı gönderemediği için giriş istemez (içerik müfredat haritasıdır,
kişisel veri yoktur). Adresin sonundaki #KOD o MK'yi seçer.
"""

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import FileResponse

from ..ayarlar import EVALORA_KOK

router = APIRouter(prefix="/api/harita", tags=["harita"])


@router.get("/{ders}", response_class=FileResponse)
def harita(ders: str):
    if ders not in ("Matematik", "Fizik"):
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Ders Matematik ya da Fizik olmalı.")
    dosya = EVALORA_KOK / ders / f"{ders} Mikro Kazanım Haritası.html"
    if not dosya.exists():
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Harita dosyası yok; araclar/harita_uret.py ile üretilir.")
    return FileResponse(dosya, media_type="text/html; charset=utf-8")
