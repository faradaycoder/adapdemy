"""Yapay zekâsız aday MK önerisi: soru metnindeki kelimeleri MK ifadeleriyle karşılaştırır (TF-IDF, kaba kök).

Yalnız öneri: bağlam içinde yazılmış sorularda (ör. "kamyon ile otomobil çarpışıyor" → etki-tepki) iyi çalışmaz;
2026-10-04 denemesinde 5 fizik sorusunun 3'ünde doğru MK'ler ilk 10'daydı, 2'sinde hiç yoktu. Son seçim öğretmende.
"""

import collections
import math
import re


def _kok(metin: str) -> list[str]:
    metin = metin.replace("İ", "i").replace("I", "ı").lower()
    return [w[:5] for w in re.findall(r"[a-zçğıöşü]+", metin) if len(w) > 2]


def oner(metin: str, adaylar: list[tuple[str, str]], adet: int = 8) -> list[tuple[str, str, float]]:
    """adaylar: (kod, ifade). Dönen: en benzer (kod, ifade, puan) listesi."""
    df = collections.Counter(w for _, ifade in adaylar for w in set(_kok(ifade)))
    n = len(adaylar) or 1

    def vektor(t: str) -> dict[str, float]:
        c = collections.Counter(_kok(t))
        return {w: k * (math.log((n + 1) / (1 + df[w])) + 1) for w, k in c.items() if w in df}  # yumuşatılmış idf

    q = vektor(metin)
    qn = math.sqrt(sum(x * x for x in q.values())) or 1.0
    sonuc = []
    for kod, ifade in adaylar:
        v = vektor(ifade)
        vn = math.sqrt(sum(x * x for x in v.values())) or 1.0
        puan = sum(q[w] * v.get(w, 0) for w in q) / (qn * vn)
        if puan > 0:
            sonuc.append((kod, ifade, round(puan, 3)))
    return sorted(sonuc, key=lambda x: -x[2])[:adet]
