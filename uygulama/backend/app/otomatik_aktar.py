"""ice_aktarma/ altındaki yeni soru setlerini (sorular.json olan klasörler) öğretmenin bankasına kendiliğinden aktarır.

EVALORA-Baslat.command, GitHub'dan yeni içerik çektikçe bunu çalıştırır; böylece bulutta hazırlanan sınavlar elle komut
yazmadan uygulamaya girer. Her klasör bir kez aktarılır (backend/veri/aktarilanlar.txt). Sorularından biri bankada zaten
olan klasör daha önce elle aktarılmış sayılır ve atlanır; öğretmenin sildiği sorular ve sınavlar geri gelmez.

Öğretmen: EVALORA_OGRETMEN_EPOSTA ortam değişkeni (.env), yoksa tek öğretmen hesabı.
Kullanım (backend klasöründe):  python -m app.otomatik_aktar
"""

import json
import os
from pathlib import Path

from sqlalchemy import select

from .ayarlar import BACKEND, VERI
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
        if d.name in yapilan:
            continue
        metinler = [s["metin"] for s in json.loads((d / "sorular.json").read_text(encoding="utf-8"))["sorular"]]
        with Oturum() as vt:
            onceden = vt.scalar(select(Soru.id).where(Soru.olusturan_id == k.id, Soru.metin.in_(metinler)).limit(1))
        if not onceden:
            sonuc = aktar(d, k.eposta)
            sinav = next((f" ve sınav #{sid}" for no, sid, _, _ in sonuc if no == "sınav"), "")
            mesajlar.append(f"{d.name}: {sum(1 for no, *_ in sonuc if no != 'sınav')} soru{sinav} aktarıldı (taslak).")
        with KAYIT.open("a", encoding="utf-8") as f:
            f.write(d.name + "\n")
    return mesajlar


if __name__ == "__main__":
    for m in calistir():
        print(m)
