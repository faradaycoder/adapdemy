from test_teslim import _kurulum

from app.modeller import VideoParca
from app.vt import Oturum


def test_otomatik_ve_ogretmen_degerlendirmesi(istemci):
    b, ogr, a, q1, q2 = _kurulum(istemci, "e1")  # q1 eğik atış (ÇS, doğru C), q2 yay (yazılı)
    istemci.post(f"/api/teslim/{a['id']}/basla", headers=ogr)
    istemci.put(f"/api/teslim/{a['id']}/cevap/{q1['id']}", json={"secilen": "C"}, headers=ogr)
    istemci.put(f"/api/teslim/{a['id']}/cevap/{q2['id']}", json={"metin": "100 J, 40 J, 60 J, x = 0,77 m"}, headers=ogr)
    istemci.post(f"/api/teslim/{a['id']}/gonder", headers=ogr)
    tid = istemci.get(f"/api/atamalar/{a['id']}/teslimler", headers=b).json()[0]["teslim_id"]

    d = istemci.get(f"/api/atamalar/{a['id']}/teslimler/{tid}/degerlendirme", headers=b).json()
    s1, s2 = d["sorular"]
    assert s1["tamam"] and all(x["durum"] == "biliyor" and x["kaynak"] == "otomatik" for x in s1["adimlar"])
    assert s1["puan"] == round(q1["zorluk"], 2)
    assert not s2["tamam"] and s2["puan"] == 0  # yazılı cevap öğretmeni bekliyor

    # öğrenci sonucu onaydan önce göremez
    assert istemci.get(f"/api/teslim/{a['id']}/sonuc", headers=ogr).status_code == 404

    # öğretmen: yay sorusunda sürtünme işi adımı yanlış, gerisi doğru
    kararlar = {str(x["adim_id"]): ("bilmiyor" if x["mk_kod"] == "Fiz04MK0129" else "biliyor") for x in s2["adimlar"]}
    d = istemci.put(f"/api/atamalar/{a['id']}/teslimler/{tid}/soru/{q2['id']}", json={"kararlar": kararlar, "not": "Sürtünme işini kontrol et."}, headers=b).json()
    s2 = d["sorular"][1]
    kayip = sum(x["en_yuksek"] for x in s2["adimlar"] if x["mk_kod"] == "Fiz04MK0129")
    assert abs(s2["puan"] - (q2["zorluk"] - kayip)) < 0.02
    assert {m["kod"]: m["durum"] for m in d["mkler"]}["Fiz04MK0129"] == "bilmiyor"

    with Oturum() as vt:  # bilinmeyen MK için onaylı bir video parçası (onaysız olan gösterilmez)
        vt.add_all([VideoParca(mk_kod="Fiz04MK0129", video_id="abc123", kanal="Kanal", baslik="Sürtünmenin işi", bas=60, son=150,
                               tur="konu", konu="Sürtünmenin yaptığı iş", onayli=True),
                    VideoParca(mk_kod="Fiz04MK0129", video_id="xyz789", baslik="Onaysız", bas=0, son=30, tur="soru", sira=-1)])
        vt.commit()
    d = istemci.post(f"/api/atamalar/{a['id']}/teslimler/{tid}/onayla", headers=b).json()
    assert d["degerlendirme"] == "onayli" and d["en_yuksek"] == round(q1["zorluk"] + q2["zorluk"], 2)
    o = istemci.get(f"/api/teslim/{a['id']}/sonuc", headers=ogr).json()
    assert o["puan"] == d["puan"] and o["sorular"][1]["aciklama"] == "Sürtünme işini kontrol et."
    assert o["sorular"][0]["durum"] == "dogru" and o["sorular"][1]["durum"] == "kismen"
    assert "Fiz04MK0129" not in str(o) and "adimlar" not in o["sorular"][0]  # öğrenciye MK kodu ve rubrik gitmez
    assert any("Sürtünme kuvvetinin" in x for x in o["calis"])
    assert o["sorular"][0]["konular"] == []
    kart = o["sorular"][1]["konular"][0]  # onaysız 'soru' parçası gösterilmez
    assert kart["konu"] == "Sürtünmenin yaptığı iş" and kart["anlatim"]["bas"] == 60 and kart["soru"] is None
    assert istemci.post(f"/api/video/{kart['anlatim']['id']}/izle", json={"teslim_atama_id": a["id"]}, headers=ogr).status_code == 204
    assert istemci.post(f"/api/video/{kart['anlatim']['id']}/izle", json={}, headers=b).status_code == 403
    satir = istemci.get(f"/api/atamalar/{a['id']}/teslimler", headers=b).json()[0]
    assert satir["degerlendirme"] == "onayli" and satir["puan"] == d["puan"]


def test_yanlis_sik_ve_bos(istemci):
    b, ogr, a, q1, q2 = _kurulum(istemci, "e2")
    istemci.post(f"/api/teslim/{a['id']}/basla", headers=ogr)
    istemci.put(f"/api/teslim/{a['id']}/cevap/{q1['id']}", json={"secilen": "A"}, headers=ogr)
    istemci.post(f"/api/teslim/{a['id']}/gonder", headers=ogr)
    tid = istemci.get(f"/api/atamalar/{a['id']}/teslimler", headers=b).json()[0]["teslim_id"]
    d = istemci.post(f"/api/atamalar/{a['id']}/teslimler/{tid}/onayla", headers=b).json()
    s1, s2 = d["sorular"]
    # yanlış şık: sorunun MK'si bilmiyor, yalnız teşhis için konan ön koşul adımları ölçülemedi
    durum = {x["mk_kod"]: x["durum"] for x in s1["adimlar"]}
    assert durum["Fiz02MK0099"] == "bilmiyor" and durum["Fiz02MK0097"] == "olculemedi"
    assert s1["puan"] == 0
    # boş bırakılan yazılı soru: hepsi ölçülemedi
    assert {x["durum"] for x in s2["adimlar"]} == {"olculemedi"} and d["puan"] == 0


def test_sonuc_bildirimi(istemci):
    b, ogr, a, q1, _ = _kurulum(istemci, "e3")
    istemci.post(f"/api/teslim/{a['id']}/basla", headers=ogr)
    istemci.put(f"/api/teslim/{a['id']}/cevap/{q1['id']}", json={"secilen": "C"}, headers=ogr)
    istemci.post(f"/api/teslim/{a['id']}/gonder", headers=ogr)
    assert istemci.get("/api/bildirimler", headers=ogr).json()["sayi"] == 0
    tid = istemci.get(f"/api/atamalar/{a['id']}/teslimler", headers=b).json()[0]["teslim_id"]
    istemci.post(f"/api/atamalar/{a['id']}/teslimler/{tid}/onayla", headers=b)
    bo = istemci.get("/api/bildirimler", headers=ogr).json()
    assert bo["sayi"] == 1 and bo["ogeler"][0]["tur"] == "sonuc" and bo["ogeler"][0]["baglanti"] == f"/sonuc/{a['id']}"
    istemci.get(f"/api/teslim/{a['id']}/sonuc", headers=ogr)  # sonucu görünce düşer
    assert istemci.get("/api/bildirimler", headers=ogr).json()["sayi"] == 0
