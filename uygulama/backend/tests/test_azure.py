"""Azure sağlayıcısı: ağ çağrıları sahte (gerçek Azure'a gidilmez)."""

from app import azure, yapay_zeka
from app.aday_mk import oner
from app.vt import Oturum


def test_aday_mk_kelime_benzerligi():
    adaylar = [("A1", "Sürtünme kuvvetini serbest cisim diyagramında gösterir."), ("A2", "Işığın kırılmasını açıklar.")]
    assert oner("Sürtünmeli zeminde kutunun serbest cisim diyagramını çiziniz.", adaylar)[0][0] == "A1"


def test_saglayici_secimi(monkeypatch):
    for k in ("ANTHROPIC_API_KEY", "AZURE_DI_ENDPOINT", "AZURE_DI_KEY", "AZURE_OPENAI_ENDPOINT", "AZURE_OPENAI_KEY",
              "AZURE_OPENAI_DEPLOYMENT"):
        monkeypatch.delenv(k, raising=False)
    assert yapay_zeka.saglayici().ad == "demo"
    monkeypatch.setenv("AZURE_DI_ENDPOINT", "https://x"); monkeypatch.setenv("AZURE_DI_KEY", "k")
    assert yapay_zeka.saglayici().ad == "azure-okuma"
    for k, v in (("AZURE_OPENAI_ENDPOINT", "https://y"), ("AZURE_OPENAI_KEY", "k"), ("AZURE_OPENAI_DEPLOYMENT", "d")):
        monkeypatch.setenv(k, v)
    assert yapay_zeka.saglayici().ad == "azure"


def test_yalniz_okuma_aday_mk_onerir(istemci, monkeypatch):
    monkeypatch.setenv("AZURE_DI_ENDPOINT", "https://x"); monkeypatch.setenv("AZURE_DI_KEY", "k")
    for k in ("AZURE_OPENAI_ENDPOINT", "AZURE_OPENAI_KEY", "AZURE_OPENAI_DEPLOYMENT", "ANTHROPIC_API_KEY"):
        monkeypatch.delenv(k, raising=False)
    monkeypatch.setattr(azure, "di_oku", lambda veri: {"metin": "1\\. Sürtünme kuvveti 8 N, kütle 2 kg. İvmeyi bulunuz.\n<!-- PageBreak -->",
                                                         "sayfalar": [], "figurler": []})
    with Oturum() as vt:
        a = yapay_zeka.saglayici().analiz_et(vt, b"\x89PNG\r\n\x1a\nyeni", None, "Fizik", 11)
    assert a.metin.startswith("1. Sürtünme") and "PageBreak" not in a.metin and len(a.adimlar) == 1
    assert any("aday MK" in n for n in a.notlar)


def test_gpt_varken_cozer_ve_esler(istemci, monkeypatch):
    for k, v in (("AZURE_OPENAI_ENDPOINT", "https://y"), ("AZURE_OPENAI_KEY", "k"), ("AZURE_OPENAI_DEPLOYMENT", "d")):
        monkeypatch.setenv(k, v)
    monkeypatch.delenv("AZURE_DI_ENDPOINT", raising=False); monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    gonderilen = {}

    def sahte_gpt(parcalar):
        gonderilen["p"] = parcalar
        return {"metin": "İvmeyi bulunuz.", "cevap_bicimi": "yazili", "dogru_cevap": "6 m/s²", "cozum": "...",
                "birincil": "Fiz02MK0140", "adimlar": [{"aciklama": "a = F/m", "mk_kod": "Fiz02MK0140"}]}
    monkeypatch.setattr(azure, "gpt_json", sahte_gpt)
    with Oturum() as vt:
        a = yapay_zeka.saglayici().analiz_et(vt, b"\x89PNG\r\n\x1a\nyeni", None, "Fizik", 11)
    assert a.birincil == "Fiz02MK0140" and a.adimlar[0]["mk_kod"] == "Fiz02MK0140"
    assert gonderilen["p"][0]["type"] == "image_url" and "Fiz02MK0140" in gonderilen["p"][-1]["text"]
