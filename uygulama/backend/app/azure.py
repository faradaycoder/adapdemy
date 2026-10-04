"""Azure servisleri: Document Intelligence (sayfa okuma, OCR) ve Azure OpenAI (soruyu anlama, eşleme).

Anahtarlar backend/.env'den gelir (ayarlar.py yükler):
  AZURE_DI_ENDPOINT, AZURE_DI_KEY                                   → okuma
  AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_KEY, AZURE_OPENAI_DEPLOYMENT → GPT
GPT kotası yokken yalnız okuma çalışır; sağlayıcı o durumda okunan metni ve aday MK önerilerini döndürür.
"""

import base64
import json
import os
import time

import httpx

DI_SURUM = "2024-11-30"


def di_hazir() -> bool:
    return bool(os.environ.get("AZURE_DI_ENDPOINT") and os.environ.get("AZURE_DI_KEY"))


def gpt_hazir() -> bool:
    return all(os.environ.get(k) for k in ("AZURE_OPENAI_ENDPOINT", "AZURE_OPENAI_KEY", "AZURE_OPENAI_DEPLOYMENT"))


def di_oku(veri: bytes, zaman_asimi: float = 90) -> dict:
    """Görseli ya da PDF'i 'layout' modeliyle okur. Dönen: {"metin": markdown, "sayfalar": [{"sayfa", "satirlar":
    [{"metin", "kutu"}]}], "figurler": [{"sayfa", "kutu"}]}. kutu: sayfa birimiyle çokgen (x1,y1,x2,y2,...)."""
    uc = os.environ["AZURE_DI_ENDPOINT"].rstrip("/")
    bas = {"Ocp-Apim-Subscription-Key": os.environ["AZURE_DI_KEY"]}
    r = httpx.post(f"{uc}/documentintelligence/documentModels/prebuilt-layout:analyze",
                   params={"api-version": DI_SURUM, "outputContentFormat": "markdown"}, headers=bas,
                   json={"base64Source": base64.b64encode(veri).decode()}, timeout=60)
    r.raise_for_status()
    konum, bitis = r.headers["operation-location"], time.monotonic() + zaman_asimi
    while True:
        time.sleep(1.5)
        s = httpx.get(konum, headers=bas, timeout=60).json()
        if s["status"] == "succeeded":
            break
        if s["status"] == "failed" or time.monotonic() > bitis:
            raise RuntimeError(f"Sayfa okunamadı ({s['status']}).")
    a = s["analyzeResult"]
    return {
        "metin": a.get("content", ""),
        "sayfalar": [{"sayfa": p["pageNumber"], "genislik": p.get("width"), "yukseklik": p.get("height"),
                      "satirlar": [{"metin": l["content"], "kutu": l.get("polygon", [])} for l in p.get("lines", [])]}
                     for p in a.get("pages", [])],
        "figurler": [{"sayfa": b["pageNumber"], "kutu": b.get("polygon", [])}
                     for f in (a.get("figures") or []) for b in f.get("boundingRegions", [])],
    }


def gpt_json(parcalar: list[dict], zaman_asimi: float = 180) -> dict:
    """Azure OpenAI'a (v1, sohbet) metin/görsel/PDF parçaları gönderir, JSON nesnesi bekler.
    parcalar: OpenAI içerik biçimi ({"type": "text"|"image_url"|"file", ...})."""
    uc = os.environ["AZURE_OPENAI_ENDPOINT"].rstrip("/")
    r = httpx.post(f"{uc}/openai/v1/chat/completions", headers={"api-key": os.environ["AZURE_OPENAI_KEY"]},
                   json={"model": os.environ["AZURE_OPENAI_DEPLOYMENT"], "response_format": {"type": "json_object"},
                         "messages": [{"role": "user", "content": parcalar}]}, timeout=zaman_asimi)
    r.raise_for_status()
    metin = r.json()["choices"][0]["message"]["content"]
    return json.loads(metin[metin.index("{"): metin.rindex("}") + 1])


def dosya_parcasi(veri: bytes, tur: str) -> dict:
    """Görsel ya da PDF'i sohbet içeriği parçasına çevirir."""
    b64 = base64.b64encode(veri).decode()
    if tur == "application/pdf":
        return {"type": "file", "file": {"filename": "soru.pdf", "file_data": f"data:application/pdf;base64,{b64}"}}
    return {"type": "image_url", "image_url": {"url": f"data:{tur};base64,{b64}"}}
