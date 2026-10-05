"""ice_aktarma/ altındaki yeni soru setlerini (sorular.json olan klasörler) öğretmenin bankasına kendiliğinden aktarır.

EVALORA-Baslat.command, GitHub'dan yeni içerik çektikçe bunu çalıştırır; böylece bulutta hazırlanan sınavlar elle komut
yazmadan uygulamaya girer. Her klasör bir kez aktarılır (backend/veri/aktarilanlar.txt). Sorularından biri bankada zaten
olan klasör daha önce elle aktarılmış sayılır ve atlanır; öğretmenin sildiği sorular ve sınavlar geri gelmez.
Aktarılmış bir set sonradan düzeltilirse bankadaki yazılar güncellenir (metin_guncelle.py; öğretmenin düzelttiği korunur).
ice_aktarma/degerlendirmeler/ altındaki "soru_seti"li değerlendirmeler de (bulutta okunan öğrenci kâğıtları) bir kez,
'sistem önerisi' olarak aktarılır; teslim henüz yoksa ya da hata varsa bir sonraki çalışmada yeniden denenir.
ice_aktarma/videolar/ altındaki MK video parçaları, dosya her değiştiğinde yeniden aktarılır (aktarma güncelleyerek yapar).
Komut satırından çalışınca Claude'un istediği video altyazılarını da indirip gönderir (transkript_al.py).

Öğretmen: EVALORA_OGRETMEN_EPOSTA ortam değişkeni (.env), yoksa tek öğretmen hesabı.
Kullanım (backend klasöründe):  python -m app.otomatik_aktar
"""

import hashlib
import json
import os
from pathlib import Path

from sqlalchemy import select

from .ayarlar import BACKEND, VERI
from . import degerlendirme_aktar, metin_guncelle, video_aktar
from .ice_aktar import aktar
from .modeller import Kullanici, Soru
from .vt import Oturum, Taban, motor

KLASOR = BACKEND.parent / "ice_aktarma"
KAYIT = VERI / "aktarilanlar.txt"


def _ogretmen() -> Kullanici | None:
    with Oturum() as vt:
        if e := os.environ.get("EVALORA_OGRETMEN_EPOSTA"):
            return vt.scalar(select(Kullanici).where(Kullanici.eposta == e.lower(), Kullanici.rol == "ogretmen"))
        ogretmenler = vt.scalars(select(Kullanici).where(Kullanici.rol == "ogretmen", Kullanici.aktif)).all()
        return ogretmenler[0] if len(ogretmenler) == 1 else None


def calistir(klasor: Path = KLASOR) -> list[str]:
    Taban.metadata.create_all(motor)
    k = _ogretmen()
    if not k:
        return ["Otomatik aktarma atlandı: öğretmen belirlenemedi. backend/.env dosyasına "
                "EVALORA_OGRETMEN_EPOSTA=<e-posta> satırını ekle."]
    yapilan = set(KAYIT.read_text(encoding="utf-8").split("\n")) if KAYIT.exists() else set()
    mesajlar = []
    for d in sorted(p for p in klasor.iterdir() if (p / "sorular.json").is_file()):
        yazi = f"yazi/{d.name}:{hashlib.sha256((d / 'sorular.json').read_bytes()).hexdigest()[:12]}"
        if d.name in yapilan:
            if yazi not in yapilan:  # set sonradan düzeltildi (ör. LaTeX): bankadaki yazıları güncelle
                if n := metin_guncelle.guncelle(d, k.id):
                    mesajlar.append(f"{d.name}: {n} yazı güncellendi (çözüm, cevap, rubrik).")
                _isaretle(yazi)
            continue
        metinler = [s["metin"] for s in json.loads((d / "sorular.json").read_text(encoding="utf-8"))["sorular"]]
        with Oturum() as vt:
            onceden = vt.scalar(select(Soru.id).where(Soru.olusturan_id == k.id, Soru.metin.in_(metinler)).limit(1))
        if not onceden:
            sonuc = aktar(d, k.eposta)
            sinav = next((f" ve sınav #{sid}" for no, sid, _, _ in sonuc if no == "sınav"), "")
            mesajlar.append(f"{d.name}: {sum(1 for no, *_ in sonuc if no != 'sınav')} soru{sinav} aktarıldı (taslak).")
        else:
            metin_guncelle.guncelle(d, k.id)
        _isaretle(d.name)
        _isaretle(yazi)
    for j in sorted((klasor / "degerlendirmeler").glob("*.json")):
        ad = f"degerlendirmeler/{j.name}"
        if ad in yapilan or "soru_seti" not in json.loads(j.read_text(encoding="utf-8")):
            continue
        try:
            rapor = degerlendirme_aktar.aktar(str(j))
        except (SystemExit, Exception) as h:  # teslim henüz yok ya da veri hatalı: sonra yeniden denenir
            mesajlar.append(f"{j.stem}: değerlendirme aktarılamadı ({h}).")
            continue
        mesajlar.append(f"{j.stem}: değerlendirme önerisi aktarıldı ({'; '.join(rapor)}). Onay öğretmende.")
        _isaretle(ad)
    for j in sorted((klasor / "videolar").glob("*.json")):
        ad = f"videolar/{j.name}:{hashlib.sha256(j.read_bytes()).hexdigest()[:12]}"
        if ad in yapilan:
            continue
        try:
            rapor = video_aktar.aktar(str(j))
        except (SystemExit, Exception) as h:
            mesajlar.append(f"{j.stem}: videolar aktarılamadı ({h}).")
            continue
        mesajlar.append(f"{j.stem}: {len(rapor)} video parçası aktarıldı.")
        _isaretle(ad)
    return mesajlar


def _isaretle(ad: str) -> None:
    with KAYIT.open("a", encoding="utf-8") as f:
        f.write(ad + "\n")


if __name__ == "__main__":
    for m in calistir():
        print(m)
    try:
        from . import transkript_al
        for v in transkript_al.calistir():
            print(f"Video altyazısı indirildi: {v}")
        if m := transkript_al.gonder():  # önceki denemede gönderilemeyen de gider
            print(m)
    except Exception as h:
        print(f"Video altyazıları alınamadı ({type(h).__name__}).")
