from conftest import kayit_ol
from test_teslim import _kurulum

from app.rapor import durum, guncelle


def test_bayesci_izleme_algoritma_ornekleri():
    # ALGORITMA.md 6.2: çoktan seçmelide 2 doğru (%82, sonra %95), açık uçluda 1 doğru (%95) "biliyor" için yeter
    p1 = guncelle(0.5, True, 0.20)
    assert round(p1, 2) == 0.82 and durum(p1) == "belirsiz" and durum(guncelle(p1, True, 0.20)) == "biliyor"
    assert durum(guncelle(0.5, True, 0.05)) == "biliyor"
    assert durum(guncelle(0.5, False, 0.05)) == "bilmiyor" and durum(None) == "olculemedi"


def test_sinif_ve_ogrenci_raporu(istemci):
    b, ogr, a, q1, q2 = _kurulum(istemci, "r1")  # q1 çoktan seçmeli (doğru C), q2 yazılı
    istemci.post(f"/api/teslim/{a['id']}/basla", headers=ogr)
    istemci.put(f"/api/teslim/{a['id']}/cevap/{q1['id']}", json={"secilen": "C"}, headers=ogr)
    istemci.put(f"/api/teslim/{a['id']}/cevap/{q2['id']}", json={"metin": "çözüm"}, headers=ogr)
    istemci.post(f"/api/teslim/{a['id']}/gonder", headers=ogr)
    tid = istemci.get(f"/api/atamalar/{a['id']}/teslimler", headers=b).json()[0]["teslim_id"]
    d = istemci.get(f"/api/atamalar/{a['id']}/teslimler/{tid}/degerlendirme", headers=b).json()
    s2 = d["sorular"][1]
    kararlar = {str(x["adim_id"]): ("bilmiyor" if x["mk_kod"] == "Fiz04MK0129" else "biliyor") for x in s2["adimlar"]}
    istemci.put(f"/api/atamalar/{a['id']}/teslimler/{tid}/soru/{q2['id']}", json={"kararlar": kararlar}, headers=b)
    sid = a["sinif_id"]

    r = istemci.get(f"/api/siniflar/{sid}/rapor", headers=b).json()
    assert r["ogrenciler"][0]["teslim"] == 0 and r["mkler"] == []  # onaylanmadan rapora girmez

    istemci.post(f"/api/atamalar/{a['id']}/teslimler/{tid}/onayla", headers=b)
    r = istemci.get(f"/api/siniflar/{sid}/rapor", headers=b).json()
    o = r["ogrenciler"][0]
    assert o["teslim"] == 1 and o["mkler"]["Fiz04MK0129"]["durum"] == "bilmiyor"
    m = next(x for x in r["mkler"] if x["kod"] == "Fiz04MK0129")
    assert m["bilmiyor"] == 1 and m["biliyor"] == 0 and m["ifade"]
    assert any(x["durum"] == "biliyor" for x in o["mkler"].values())  # açık uçlu tek doğru yeter

    ro = istemci.get(f"/api/siniflar/{sid}/ogrenciler/{o['id']}/rapor", headers=b).json()
    assert ro["mkler"][0]["kod"] == "Fiz04MK0129" and ro["mkler"][0]["yanlis"] == 1  # bilinmeyenler önce
    kendi = istemci.get("/api/rapor", headers=ogr).json()
    assert kendi["teslim"] == 1 and kendi["mkler"][0]["durum"] == "bilmiyor"

    # başkasının sınıfı ve öğrenci rolü göremez
    baska = kayit_ol(istemci, "r1baska@ornek.com", "ogretmen")
    assert istemci.get(f"/api/siniflar/{sid}/rapor", headers=baska).status_code == 404
    assert istemci.get(f"/api/siniflar/{sid}/rapor", headers=ogr).status_code == 403
    assert istemci.get("/api/rapor", headers=b).status_code == 403


def test_ana_sayfa_ozeti(istemci):
    b, ogr, a, q1, q2 = _kurulum(istemci, "oz1")
    o = istemci.get("/api/ozet", headers=b).json()
    assert o["sinif"] == 1 and o["ogrenci"] == 1 and o["soru_onayli"] == 2 and o["sinav"] == 1 and o["bekleyenler"] == []
    istemci.post(f"/api/teslim/{a['id']}/basla", headers=ogr)
    istemci.post(f"/api/teslim/{a['id']}/gonder", headers=ogr)
    o = istemci.get("/api/ozet", headers=b).json()
    assert o["bekleyenler"][0]["bekleyen"] == 1 and o["bekleyenler"][0]["ogrenci"] == 1
    assert istemci.get("/api/ozet", headers=ogr).json()["mk"] == {"biliyor": 0, "belirsiz": 0, "bilmiyor": 0}


def test_mufredat_agaci_ve_mk_ile_soru_filtresi(istemci):
    b, ogr, a, q1, q2 = _kurulum(istemci, "mf1")  # Fizik 11 ve 12 soruları
    agac = istemci.get("/api/mufredat", params={"ders": "Matematik", "sinif": 6}, headers=b).json()
    tema1 = agac[0]
    assert tema1["ad"] == "Sayılar ve Nicelikler" and len(agac) >= 5
    k = next(x for x in tema1["kazanimlar"] if x["kod"] == "MAT.6.1.2")
    assert "bölünebilme" in k["ifade"] and any(m["kod"] == "Mat01MK0068" for m in k["mkler"])
    f = istemci.get("/api/mufredat", params={"ders": "Fizik", "sinif": 12}, headers=b).json()
    assert f and all(x["kazanimlar"] is not None for x in f)
    hepsi = {s["id"]: s for s in istemci.get("/api/sorular", headers=b).json()}
    mk = next(m for m in hepsi[q2["id"]]["soru_mkleri"] if m not in hepsi[q1["id"]]["soru_mkleri"])
    ids = [s["id"] for s in istemci.get("/api/sorular", params={"mkler": f"{mk},Yok0000"}, headers=b).json()]
    assert q2["id"] in ids and q1["id"] not in ids
    assert istemci.get("/api/mufredat", params={"ders": "Fizik", "sinif": 12}, headers=ogr).status_code == 403
