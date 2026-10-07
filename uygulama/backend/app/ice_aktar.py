"""Hazır analiz edilmiş bir soru setini bir öğretmenin soru bankasına aktarır.

Klasörde sorular.json ve sorulardaki görseller bulunur (örnek: uygulama/ice_aktarma/kazanim_kavrama_16/).
sorular.json'da "sinav" alanı varsa sorular aynı sırayla bir sınav olarak da kaydedilir (PDF'teki sınavın kendisi).
Sorunun MK'leri, zorluk ve rubrik payları burada da eslestirme.py kurallarıyla hesaplanır; sorular taslak olarak girer,
öğretmen inceleyip onaylar. Aynı metinli soru aynı öğretmende zaten varsa yeniden eklenmez (sınava mevcut soru girer).

Kullanım (backend klasöründe):  python -m app.ice_aktar ../ice_aktarma/kazanim_kavrama_16 ogretmen@ornek.com
"""

import json
import sys
from pathlib import Path

from sqlalchemy import select

from .modeller import Kullanici, Sinav, SinavSoru, Soru
from .routers.sorular import AdimG, SecenekG, SoruG, _esle, _gorsel_kaydet, _yaz
from .vt import Oturum, Taban, motor


def aktar(klasor: Path, eposta: str) -> list[tuple[int, int | None, float | None, list[str]]]:
    Taban.metadata.create_all(motor)
    veri = json.loads((klasor / "sorular.json").read_text(encoding="utf-8"))
    sonuc = []
    with Oturum() as vt:
        k = vt.scalar(select(Kullanici).where(Kullanici.eposta == eposta.lower(), Kullanici.rol == "ogretmen"))
        if not k:
            raise SystemExit(f"{eposta} adresli bir öğretmen hesabı yok.")
        for s in veri["sorular"]:
            gorsel = _gorsel_kaydet((klasor / s["gorsel"]).read_bytes()) if s.get("gorsel") else None
            ayni = vt.scalar(select(Soru).where(Soru.olusturan_id == k.id, Soru.metin == s["metin"]))
            if ayni:
                sonuc.append((s["no"], ayni.id, ayni.zorluk, ["zaten var, yeniden eklenmedi"]))
                continue
            g = SoruG(
                ders=s.get("ders", veri["ders"]), sinif_duzeyi=s.get("sinif_duzeyi", veri["sinif_duzeyi"]), metin=s["metin"],
                gorsel=gorsel, cevap_bicimi=s["cevap_bicimi"],
                secenekler=[SecenekG(harf=x[0], metin=x[1], dogru=x[2], yanilgi_kod=x[3] if len(x) > 3 else None)
                            for x in s.get("secenekler", [])],  # [harf, metin, doğru mu, (yanılgı kodu)]
                dogru_cevap=s.get("dogru_cevap", ""), cozum=s.get("cozum", ""), birincil=s.get("birincil"),
                adimlar=[AdimG(aciklama=a, mk_kod=m) for a, m in s["adimlar"]],
            )
            soru = Soru(olusturan_id=k.id, kaynak="ice_aktarma", durum="taslak", ders=g.ders, sinif_duzeyi=g.sinif_duzeyi,
                        metin="", cevap_bicimi=g.cevap_bicimi)
            _yaz(vt, soru, g)
            vt.add(soru)
            vt.flush()
            sonuc.append((s["no"], soru.id, soru.zorluk, _esle(vt, g.ders, g.adimlar, g.birincil).uyarilar))
        if veri.get("sinav"):
            sv = veri["sinav"]
            sinav = Sinav(ad=sv["ad"], ders=veri["ders"], sinif_duzeyi=veri["sinif_duzeyi"], aciklama=sv.get("aciklama", ""),
                          sure_dk=sv.get("sure_dk"), olusturan_id=k.id)
            sinav.sorular = [SinavSoru(soru_id=sid, sira=n + 1) for n, (_, sid, _, _) in enumerate(sonuc)]
            vt.add(sinav)
            vt.flush()
            sonuc.append(("sınav", sinav.id, round(sum(z or 0 for _, _, z, _ in sonuc), 2), [sv["ad"]]))
        vt.commit()
    return sonuc


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    for no, sid, z, uyari in aktar(Path(sys.argv[1]), sys.argv[2]):
        print(f"Soru {no}: " + (f"#{sid}, zorluk {z}" if sid else "") + (f"  ({'; '.join(uyari)})" if uyari else ""))
