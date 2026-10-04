"""İstenen YouTube videolarının Türkçe altyazılarını (zaman kodlu) indirir.

Bulut oturumundaki Claude YouTube'a bot engeline takıldığı için video parçalarını seçerken altyazıları okuyamaz. Claude
uygulama/ice_aktarma/videolar/istek.json'a video kimliklerini yazar ({"videolar": ["<id>", ...]}); Murat'ın Mac'inde
başlatıcının iki dakikada bir çalıştırdığı otomatik_aktar bunu çağırır (gerekirse kütüphaneyi kurar), inen altyazıları
commit edip GitHub'a (main) gönderir. Claude onları okuyup parçaları seçer.
Çıktı: videolar/transkript/<id>.json  {"video", "kanal", "baslik", "dil", "satirlar": [[başlangıç_sn, süre_sn, metin]]}
Altyazısı olmayan video için {"video", "hata"} yazılır ki yeniden denenmesin.

Kullanım (backend klasöründe):  python -m app.transkript_al
"""

import json
import os
import subprocess
import sys

import httpx

from .ayarlar import BACKEND

KLASOR = BACKEND.parent / "ice_aktarma" / "videolar"


def _bilgi(vid: str) -> dict:
    try:
        r = httpx.get("https://www.youtube.com/oembed", params={"url": f"https://www.youtube.com/watch?v={vid}", "format": "json"},
                      timeout=20)
        return {"kanal": r.json().get("author_name", ""), "baslik": r.json().get("title", "")} if r.is_success else {}
    except httpx.HTTPError:
        return {}


def calistir(klasor=KLASOR) -> list[str]:
    istek = klasor / "istek.json"
    if not istek.exists():
        return []
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError:  # Mac'teki sanal ortamda ilk kez: kur
        subprocess.run([sys.executable, "-m", "pip", "install", "-q", "youtube-transcript-api"], capture_output=True)
        from youtube_transcript_api import YouTubeTranscriptApi

    cikti = klasor / "transkript"
    cikti.mkdir(exist_ok=True)
    api, yeni = YouTubeTranscriptApi(), []
    for vid in json.loads(istek.read_text(encoding="utf-8")).get("videolar", []):
        dosya = cikti / f"{vid}.json"
        if dosya.exists():
            continue
        try:
            t = api.fetch(vid, languages=["tr"])
            veri = {"video": vid, **_bilgi(vid), "dil": t.language_code,
                    "satirlar": [[round(s.start, 1), round(s.duration, 1), s.text] for s in t.snippets]}
        except Exception as h:  # altyazı yok, video kaldırılmış vb.
            if "429" in str(h) or "blocked" in str(h).lower():  # geçici engel: sonra yeniden dene
                continue
            veri = {"video": vid, **_bilgi(vid), "hata": type(h).__name__}
        dosya.write_text(json.dumps(veri, ensure_ascii=False), encoding="utf-8")
        yeni.append(vid)
    return yeni


def gonder() -> str | None:
    """İnen altyazıları commit edip main'e gönderir (yalnız transkript klasörü)."""
    kok, yol = BACKEND.parent.parent, str(KLASOR / "transkript")

    def git(*a):
        return subprocess.run(["git", "-C", str(kok), *a], capture_output=True, text=True,
                              env={**os.environ, "GIT_TERMINAL_PROMPT": "0"})
    if git("status", "--porcelain", "--", yol).stdout.strip():
        git("add", "--", yol)
        git("commit", "-q", "-m", "Video altyazıları (Mac'ten)", "--", yol)
    if git("log", "--oneline", "origin/main..HEAD", "--", yol).stdout.strip():
        return "Altyazılar Claude'a gönderildi." if git("push", "-q", "origin", "HEAD:main").returncode == 0 else None
    return None


if __name__ == "__main__":
    for v in calistir():
        print(f"Altyazı indirildi: {v}")
