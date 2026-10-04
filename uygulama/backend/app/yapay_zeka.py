"""Yapay zekâ katmanı: soruyu okuma, çözme, rubrik çıkarma ve adımları MK'ye eşleme.

İki sağlayıcı vardır:
- DemoSaglayici: API anahtarı yokken kullanılır; yalnız örnek soruları (app/demo/sorular.py) tanır.
- ClaudeSaglayici: ANTHROPIC_API_KEY ortam değişkeni varsa kullanılır. Görseli ve aday MK listesini modele
  gönderir, yapılandırılmış JSON ister. (Anahtar gelince denenecek; şu an test edilmedi.)
- AzureSaglayici: Azure anahtarları (backend/.env) varsa kullanılır. Document Intelligence sayfayı okur; Azure
  OpenAI (GPT) varsa okunan metin ve görselle soruyu çözer ve eşler. GPT yoksa yalnız okunan metni ve kelime
  benzerliğiyle aday MK önerilerini döndürür (eşleme öğretmende). Demo örnekleri her durumda tanınır.

Her iki sağlayıcı da aynı Analiz nesnesini döndürür. Sorunun MK'leri, zorluk ve paylar sağlayıcıdan değil,
eslestirme.py'deki kurallardan gelir; böylece model hangi MK'yi seçerse seçsin kurallar aynı uygulanır.
"""

import base64
import hashlib
import json
import os
import re
from dataclasses import dataclass, field
from pathlib import Path

from sqlalchemy import select
from sqlalchemy.orm import Session

from . import aday_mk, azure
from .demo.sorular import ORNEKLER
from .modeller import MK, MKEsleme

DEMO_KLASOR = Path(__file__).resolve().parent / "demo"


@dataclass
class Analiz:
    ders: str
    sinif_duzeyi: int
    metin: str
    cevap_bicimi: str
    secenekler: list[dict]  # {harf, metin, dogru, yanilgi_kod}
    dogru_cevap: str
    cozum: str
    birincil: str | None
    adimlar: list[dict]  # {aciklama, mk_kod}
    gorsel_ornek: str | None = None  # demo görselinin dosya adı
    notlar: list[str] = field(default_factory=list)


class TanimadiHatasi(Exception):
    pass


def _ornekten(o: dict) -> Analiz:
    return Analiz(
        ders=o["ders"], sinif_duzeyi=o["sinif_duzeyi"], metin=o["metin"], cevap_bicimi=o["cevap_bicimi"],
        secenekler=[{"harf": h, "metin": m, "dogru": d, "yanilgi_kod": None} for h, m, d in o["secenekler"]],
        dogru_cevap=o["dogru_cevap"], cozum=o["cozum"], birincil=o["birincil"],
        adimlar=[{"aciklama": a, "mk_kod": k} for a, k in o["adimlar"]], gorsel_ornek=o["gorsel"],
    )


def _ozet(veri: bytes) -> str:
    return hashlib.sha256(veri).hexdigest()


# Demo örneklerinin görselleri ve aynı adlı PDF sürümleri (ör. uc_cisim.png ve uc_cisim.pdf) tanınır.
_DEMO_OZETLER = {_ozet(d.read_bytes()): o for o in ORNEKLER if o["gorsel"]
                 for d in (DEMO_KLASOR / o["gorsel"], (DEMO_KLASOR / o["gorsel"]).with_suffix(".pdf")) if d.exists()}


class DemoSaglayici:
    ad = "demo"

    def ornekler(self) -> list[dict]:
        return [{"anahtar": o["anahtar"], "baslik": o["baslik"], "ders": o["ders"], "sinif_duzeyi": o["sinif_duzeyi"],
                 "gorsel": o["gorsel"]} for o in ORNEKLER]

    def ornek(self, anahtar: str) -> Analiz:
        for o in ORNEKLER:
            if o["anahtar"] == anahtar:
                return _ornekten(o)
        raise TanimadiHatasi("Böyle bir örnek soru yok.")

    def analiz_et(self, vt: Session, gorsel: bytes | None, metin: str | None, ders: str, sinif_duzeyi: int) -> Analiz:
        if gorsel and _ozet(gorsel) in _DEMO_OZETLER:
            return _ornekten(_DEMO_OZETLER[_ozet(gorsel)])
        if metin:
            for o in ORNEKLER:
                if o["metin"].strip() == metin.strip():
                    return _ornekten(o)
        raise TanimadiHatasi("Demo modunda yalnız örnek sorular tanınır. Gerçek okuma için API anahtarı gerekiyor.")


def _aday_mkler(vt: Session, ders: str, sinif_duzeyi: int) -> list[MK]:
    """Modele gönderilecek aday MK'ler: dersin, öğrencinin sınıfına kadar eşlenmiş MK'leri."""
    alt = select(MKEsleme.mk_kod).where(MKEsleme.sinif <= sinif_duzeyi)
    return list(vt.scalars(select(MK).where(MK.ders == ders, MK.durum != "iptal", MK.kod.in_(alt)).order_by(MK.kod)))


def _cevaptan(v: dict, ders: str, sinif_duzeyi: int, notlar: list[str] | None = None) -> Analiz:
    return Analiz(ders=ders, sinif_duzeyi=sinif_duzeyi, metin=v["metin"], cevap_bicimi=v.get("cevap_bicimi", "yazili"),
                  secenekler=v.get("secenekler", []), dogru_cevap=v.get("dogru_cevap", ""), cozum=v.get("cozum", ""),
                  birincil=v.get("birincil"), adimlar=v.get("adimlar", []), notlar=notlar or [])


def _ocr_temizle(metin: str) -> str:
    metin = re.sub(r"<!--.*?-->", "", metin, flags=re.S)  # sayfa sonu vb. işaretler
    metin = re.sub(r"</?figure>", "", metin)
    return re.sub(r"\n{3,}", "\n\n", metin.replace("\\.", ".")).strip()


class ClaudeSaglayici:
    ad = "claude"
    MODEL = os.environ.get("EVALORA_MODEL", "claude-opus-5-5")

    def __init__(self, anahtar: str):
        self.anahtar = anahtar

    def ornekler(self) -> list[dict]:
        return DemoSaglayici().ornekler()

    def ornek(self, anahtar: str) -> Analiz:
        return DemoSaglayici().ornek(anahtar)

    def analiz_et(self, vt: Session, gorsel: bytes | None, metin: str | None, ders: str, sinif_duzeyi: int) -> Analiz:
        import httpx

        adaylar = "\n".join(f"{m.kod} | {m.ifade}" for m in _aday_mkler(vt, ders, sinif_duzeyi))
        icerik: list[dict] = []
        if gorsel:
            tur = _tur(gorsel)
            icerik.append({"type": "document" if tur == "application/pdf" else "image",
                           "source": {"type": "base64", "media_type": tur, "data": base64.b64encode(gorsel).decode()}})
        icerik.append({"type": "text", "text": _ISTEM.format(ders=ders, sinif=sinif_duzeyi, metin=metin or "(görselde)",
                                                            adaylar=adaylar)})
        r = httpx.post("https://api.anthropic.com/v1/messages", timeout=120, headers={
            "x-api-key": self.anahtar, "anthropic-version": "2023-06-01", "content-type": "application/json"},
            json={"model": self.MODEL, "max_tokens": 4000, "messages": [{"role": "user", "content": icerik}]})
        r.raise_for_status()
        metin_cikti = "".join(p.get("text", "") for p in r.json()["content"])
        v = json.loads(metin_cikti[metin_cikti.index("{"): metin_cikti.rindex("}") + 1])
        return _cevaptan(v, ders, sinif_duzeyi)


class AzureSaglayici:
    """Document Intelligence ile okur; Azure GPT varsa çözer ve eşler, yoksa aday MK önerir."""

    def __init__(self):
        self.ad = "azure" if azure.gpt_hazir() else "azure-okuma"

    def ornekler(self) -> list[dict]:
        return DemoSaglayici().ornekler()

    def ornek(self, anahtar: str) -> Analiz:
        return DemoSaglayici().ornek(anahtar)

    def analiz_et(self, vt: Session, gorsel: bytes | None, metin: str | None, ders: str, sinif_duzeyi: int) -> Analiz:
        if gorsel and _ozet(gorsel) in _DEMO_OZETLER:  # hazır örnekler her zaman tanınır
            return _ornekten(_DEMO_OZETLER[_ozet(gorsel)])
        okunan = ""
        if gorsel and azure.di_hazir():
            okunan = _ocr_temizle(azure.di_oku(gorsel)["metin"])
        mkler = _aday_mkler(vt, ders, sinif_duzeyi)
        if azure.gpt_hazir():
            parcalar = [azure.dosya_parcasi(gorsel, _tur(gorsel))] if gorsel else []
            istem = _ISTEM.format(ders=ders, sinif=sinif_duzeyi, metin=metin or "(görselde)",
                                  adaylar="\n".join(f"{m.kod} | {m.ifade}" for m in mkler))
            if okunan:
                istem += f"\nSayfadan okunan metin (OCR; şekillerdeki sayılar hatalı olabilir, görsele güven):\n{okunan}\n"
            parcalar.append({"type": "text", "text": istem})
            return _cevaptan(azure.gpt_json(parcalar), ders, sinif_duzeyi, ["Azure GPT ile okundu ve eşlendi; kontrol et."])
        soru_metni = (metin or "").strip() or okunan
        if not soru_metni:
            raise TanimadiHatasi("Sayfa okunamadı. Soru metnini yazarak deneyebilirsin.")
        oneriler = aday_mk.oner(soru_metni, [(m.kod, m.ifade) for m in mkler])
        notlar = ["Metin Azure ile okundu. Yapay zekâ (GPT) henüz bağlı değil: çözümü, rubrik adımlarını ve MK'leri sen gir."]
        if oneriler:
            notlar.append("Kelime benzerliğine göre aday MK'ler (kesin değil): "
                          + "; ".join(f"{k} — {i}" for k, i, _ in oneriler))
        # Soru en az bir rubrik adımı ister: en olası aday MK'yle bir taslak adım; öğretmen düzeltir ve çoğaltır.
        ilk = oneriler[0][0] if oneriler else (mkler[0].kod if mkler else "")
        adimlar = [{"aciklama": "Çözüm adımını yaz (MK önerisi kesin değil, değiştir).", "mk_kod": ilk}]
        return Analiz(ders=ders, sinif_duzeyi=sinif_duzeyi, metin=soru_metni, cevap_bicimi="yazili", secenekler=[],
                      dogru_cevap="", cozum="", birincil=None, adimlar=adimlar, notlar=notlar)


def _tur(veri: bytes) -> str:
    if veri[:8] == b"\x89PNG\r\n\x1a\n":
        return "image/png"
    if veri[:3] == b"\xff\xd8\xff":
        return "image/jpeg"
    if veri[:5] == b"%PDF-":
        return "application/pdf"
    if veri[:4] == b"RIFF" and veri[8:12] == b"WEBP":
        return "image/webp"
    return "image/png"


_ISTEM = """Sen bir ölçme ve değerlendirme uzmanısın. Aşağıdaki {ders} sorusunu ({sinif}. sınıf) oku ve çöz.
Soru metni: {metin}

Kurallar:
1. Doğru çözümü, her adım tek bir iş yapacak biçimde adımlara ayır (rubrik adımları).
2. Her adımı aşağıdaki aday mikro kazanımlardan (MK) yalnız birine eşle: adımın gerçekten yaptığı işe karşılık gelen MK.
   Listede olmayan kod uydurma.
3. Sorunun asıl ölçtüğü MK'yi "birincil" olarak ver.
4. Çoktan seçmeliyse şıkları ve doğru şıkkı ver.

Yalnızca şu biçimde JSON döndür:
{{"metin": "...", "cevap_bicimi": "coktan_secmeli|kisa_cevap|yazili",
  "secenekler": [{{"harf": "A", "metin": "...", "dogru": false, "yanilgi_kod": null}}],
  "dogru_cevap": "...", "cozum": "...", "birincil": "MK kodu",
  "adimlar": [{{"aciklama": "...", "mk_kod": "MK kodu"}}]}}

Aday MK'ler (kod | ifade):
{adaylar}
"""


def saglayici():
    """Sıra: Anthropic anahtarı → Claude; Azure anahtarları → Azure; hiçbiri → demo."""
    anahtar = os.environ.get("ANTHROPIC_API_KEY")
    if anahtar:
        return ClaudeSaglayici(anahtar)
    if azure.di_hazir() or azure.gpt_hazir():
        return AzureSaglayici()
    return DemoSaglayici()
