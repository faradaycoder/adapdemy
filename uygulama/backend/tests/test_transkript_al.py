import json
import sys
import types
from types import SimpleNamespace as NS

from app import transkript_al


def test_istenen_altyazilar_iner_ve_bir_kez_alinir(tmp_path, monkeypatch):
    cagrilan = []

    class SahteApi:
        def fetch(self, vid, languages):
            cagrilan.append(vid)
            if vid == "yok":
                raise RuntimeError("TranscriptsDisabled")
            return NS(language_code="tr", snippets=[NS(start=1.04, duration=2.0, text="2 ile bölünebilme")])

    monkeypatch.setitem(sys.modules, "youtube_transcript_api", types.SimpleNamespace(YouTubeTranscriptApi=SahteApi))
    monkeypatch.setattr(transkript_al, "_bilgi", lambda vid: {"kanal": "K", "baslik": "B"})
    (tmp_path / "istek.json").write_text(json.dumps({"videolar": ["abc", "yok"]}), encoding="utf-8")

    assert transkript_al.calistir(tmp_path) == ["abc", "yok"]
    t = json.loads((tmp_path / "transkript" / "abc.json").read_text(encoding="utf-8"))
    assert t["satirlar"] == [[1.0, 2.0, "2 ile bölünebilme"]] and t["kanal"] == "K"
    assert "hata" in json.loads((tmp_path / "transkript" / "yok.json").read_text(encoding="utf-8"))
    assert transkript_al.calistir(tmp_path) == [] and cagrilan == ["abc", "yok"]  # inenler yeniden istenmez
