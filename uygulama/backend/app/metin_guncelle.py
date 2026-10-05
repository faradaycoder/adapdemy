"""Aktarılmış bir soru setinin sorular.json'u sonradan düzeltilince (ör. çözümler LaTeX'e çevrilince) bankadaki
soruların yazılarını günceller.

Yalnız yazılar değişir: soru metni, doğru cevap, çözüm, şık metinleri ve rubrik adımlarının açıklamaları. MK'ler,
paylar ve zorluk değişmez. Bir alan, ancak bankadaki değeri o setin git geçmişindeki bir sürümüyle aynıysa
güncellenir; yani öğretmenin elle düzelttiği yazının üstüne yazılmaz. Rubrik adımları, adım sayısı ve MK'leri aynıysa
güncellenir.
"""

import json
import subprocess
from pathlib import Path

from sqlalchemy import select

from .modeller import Soru
from .vt import Oturum


def _surumler(dosya: Path) -> list[dict]:
    """Dosyanın şimdiki hâli ve git geçmişindeki bütün sürümleri."""
    surumler = [json.loads(dosya.read_text(encoding="utf-8"))]
    kok = subprocess.run(["git", "-C", str(dosya.parent), "rev-parse", "--show-toplevel"], capture_output=True, text=True)
    if kok.returncode:
        return surumler
    yol = str(dosya.resolve().relative_to(Path(kok.stdout.strip()).resolve()))
    kayitlar = subprocess.run(["git", "-C", kok.stdout.strip(), "log", "--format=%H", "--", yol], capture_output=True, text=True)
    for h in kayitlar.stdout.split():
        r = subprocess.run(["git", "-C", kok.stdout.strip(), "show", f"{h}:{yol}"], capture_output=True, text=True)
        if r.returncode == 0:
            try:
                surumler.append(json.loads(r.stdout))
            except json.JSONDecodeError:
                pass
    return surumler


def guncelle(set_klasoru: Path, ogretmen_id: int) -> int:
    """Güncellenen alan sayısını döndürür."""
    surumler = _surumler(set_klasoru / "sorular.json")
    simdiki, sayi = surumler[0], 0
    with Oturum() as vt:
        for s in simdiki["sorular"]:
            gecmis = [x for v in surumler for x in v["sorular"] if x["no"] == s["no"]]
            q = vt.scalar(select(Soru).where(Soru.olusturan_id == ogretmen_id, Soru.metin.in_({g["metin"] for g in gecmis})))
            if not q:
                continue
            for alan in ("metin", "dogru_cevap", "cozum"):
                yeni = s.get(alan, "")
                if getattr(q, alan) != yeni and getattr(q, alan) in {g.get(alan, "") for g in gecmis}:
                    setattr(q, alan, yeni)
                    sayi += 1
            sec = {h: m for h, m, _ in s.get("secenekler", [])}
            for x in q.secenekler:
                eski = {m for g in gecmis for h, m, _ in g.get("secenekler", []) if h == x.harf}
                if x.harf in sec and x.metin != sec[x.harf] and x.metin in eski:
                    x.metin = sec[x.harf]
                    sayi += 1
            if [m for _, m in s["adimlar"]] == [a.mk_kod for a in q.adimlar]:
                for i, (a, (yeni, _)) in enumerate(zip(q.adimlar, s["adimlar"])):
                    eski = {g["adimlar"][i][0] for g in gecmis if len(g["adimlar"]) > i}
                    if a.aciklama != yeni and a.aciklama in eski:
                        a.aciklama = yeni
                        sayi += 1
        vt.commit()
    return sayi
