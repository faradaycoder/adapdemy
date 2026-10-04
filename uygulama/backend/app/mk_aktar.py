"""MK verisini EVALORA CSV'lerinden veritabanına aktarır.

CSV'ler tek doğruluk kaynağıdır; harita değiştiğinde bu betik yeniden çalıştırılır ve MK tabloları baştan yazılır.
Zorluk ve seviye, Excel'lerle aynı hesapla (araclar/zorluk.py) bulunur.

Kullanım (backend klasöründe):  python -m app.mk_aktar
"""

import csv
import sys

from sqlalchemy import delete

from .ayarlar import EVALORA_KOK
from .modeller import MK, MKEsleme, MKOnKosul, MKYanilgi, Yanilgi
from .vt import Oturum, Taban, motor

sys.path.insert(0, str(EVALORA_KOK / "araclar"))
import zorluk  # noqa: E402  (EVALORA/araclar/zorluk.py)

DERSLER = [("Fizik", "fizik"), ("Matematik", "matematik")]


def _oku(yol):
    with open(yol, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def _liste(s):
    return [x.strip() for x in (s or "").split(";") if x.strip()]


def aktar(vt=None) -> dict:
    Taban.metadata.create_all(motor)
    kendi = vt is None
    vt = vt or Oturum()
    try:
        for tablo in (MKYanilgi, MKEsleme, MKOnKosul, Yanilgi, MK):
            vt.execute(delete(tablo))
        ozet = {}
        for ders, onek in DERSLER:
            klasor = EVALORA_KOK / ders / "veri"
            mk = _oku(klasor / f"{onek}_mikro_kazanimlar.csv")
            z = zorluk.hesapla(mk)
            kodlar = {r["kod"] for r in mk}
            for r in mk:
                s = z.get(r["kod"], {})
                iptal = r.get("durum", "").strip() == "iptal"
                vt.add(MK(
                    kod=r["kod"], ders=ders, ana_unite=r["ana_unite"], ifade=r["ifade"], tur=r["tur"],
                    bilissel_duzey=r["bilissel_duzey"], islem_turu=r["islem_turu"], v=s.get("deger"),
                    zorluk=None if iptal else s.get("zorluk"), seviye=None if iptal else s.get("seviye"),
                    on_kosul_diger=r.get("on_kosul_diger", ""), olcme_turleri=r.get("olcme_turleri", ""),
                    ustalik_olcutu=r.get("ustalik_olcutu", ""), durum=r.get("durum", "taslak"),
                ))
            vt.flush()
            bag = 0
            for r in mk:
                for p in _liste(r["on_kosul_kodlari"]):
                    if p in kodlar:
                        vt.add(MKOnKosul(mk_kod=r["kod"], on_kosul_kod=p))
                        bag += 1
            es = _oku(klasor / f"{onek}_kazanim_esleme.csv")
            for e in es:
                if e["mikro_kod"] in kodlar:
                    vt.add(MKEsleme(mk_kod=e["mikro_kod"], sinif=int(e["sinif"]), sinif_unite=e["sinif_unite"],
                                    ogrenme_ciktisi=e["ogrenme_ciktisi"], surec_bileseni=e["surec_bileseni"]))
            yg = _oku(klasor / f"{onek}_yanilgilar.csv")
            for y in yg:
                vt.add(Yanilgi(kod=y["kod"], ders=ders, ana_unite=y["ana_unite"], ifade=y["yanilgi"]))
            vt.flush()
            ygkod = {y["kod"] for y in yg}
            for r in mk:
                for y in _liste(r.get("yanilgilar")):
                    if y in ygkod:
                        vt.add(MKYanilgi(mk_kod=r["kod"], yanilgi_kod=y))
            ozet[ders] = {"mk": len(mk), "bag": bag, "esleme": len(es), "yanilgi": len(yg)}
        vt.commit()
        return ozet
    finally:
        if kendi:
            vt.close()


if __name__ == "__main__":
    for ders, s in aktar().items():
        print(f"{ders}: {s['mk']} MK, {s['bag']} ön koşul bağı, {s['esleme']} eşleme, {s['yanilgi']} yanılgı")
