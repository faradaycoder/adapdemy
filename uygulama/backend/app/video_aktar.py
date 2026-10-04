"""MK'lere eşlenmiş YouTube video parçalarını aktarır.

Dosya biçimi: uygulama/ice_aktarma/videolar/*.json
  {"videolar": {"<video_id>": {"kanal": "...", "baslik": "...", "sure": saniye}},
   "konular": {"Mat01MK0106": "öğrenci dilinde konu adı"},
   "parcalar": [{"mk": "Mat01MK0106", "tur": "konu|soru", "video": "<video_id>", "bas": "16:47", "son": "18:16", "baslik": "...", "neden": "..."}]}
tur: konu = konu anlatımı, soru = benzer soru çözümü. Aynı MK ve türün parçaları dosyadaki sırayla önceliklendirilir. Aynı (video, başlangıç, MK) yeniden aktarılırsa güncellenir.
Pilotta parçalar onaylı aktarılır (Murat'ın seçtiği kanallar); öğretmen onay ekranı sonra gelecek.

Kullanım (backend klasöründe):  python -m app.video_aktar ../ice_aktarma/videolar/pilot_6sinif.json
"""

import json
import sys

from sqlalchemy import select

from .modeller import MK, VideoParca
from .vt import Oturum


def _saniye(z: str) -> int:
    s = 0
    for p in z.split(":"):
        s = s * 60 + int(p)
    return s


def aktar(yol: str) -> list[str]:
    v = json.load(open(yol, encoding="utf-8"))
    rapor, sira = [], {}
    with Oturum() as vt:
        for p in v["parcalar"]:
            if not vt.get(MK, p["mk"]):
                rapor.append(f"{p['mk']}: MK yok, atlandı")
                continue
            bilgi = v["videolar"][p["video"]]
            bas, son = _saniye(p["bas"]), _saniye(p["son"])
            vp = vt.scalar(select(VideoParca).where(VideoParca.video_id == p["video"], VideoParca.bas == bas,
                                                    VideoParca.mk_kod == p["mk"])) or VideoParca(mk_kod=p["mk"], video_id=p["video"], bas=bas)
            anahtar = (p["mk"], p.get("tur", "konu"))
            sira[anahtar] = sira.get(anahtar, -1) + 1
            vp.son, vp.baslik, vp.neden, vp.sira, vp.onayli = son, p["baslik"], p.get("neden", ""), sira[anahtar], True
            vp.kanal, vp.video_baslik, vp.video_sure = bilgi["kanal"], bilgi["baslik"], bilgi.get("sure")
            vp.tur, vp.konu = p.get("tur", "konu"), v.get("konular", {}).get(p["mk"], "")
            vt.add(vp)
            rapor.append(f"{p['mk']}: {p['baslik']} ({p['bas']}–{p['son']})")
        vt.commit()
    return rapor


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    print("\n".join(aktar(sys.argv[1])))
