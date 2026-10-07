from pathlib import Path

from app import ice_aktar
from app.uyarlamali import dina
from conftest import kayit_ol

HAVUZ = Path(__file__).resolve().parents[2] / "ice_aktarma" / "mat6_bolunebilme_havuz"


def test_dina_tek_mk_bilgi_izlemeyle_ayni_cok_mkde_sucu_paylastirir():
    p = dina({"a": 0.5}, ["a"], dogru=True, g=0.2)
    assert round(p["a"], 3) == 0.818  # tek MK: Bayesçi bilgi izleme
    p = dina({"a": 0.5, "b": 0.5, "c": 0.5}, ["a", "b", "c"], dogru=False, g=0.2)
    assert all(round(v, 2) == 0.44 for v in p.values())  # üç MK'li soruda bir yanlış kimseyi "bilmiyor" yapmaz
    p = dina({"a": 0.95, "b": 0.5}, ["a", "b"], dogru=False, g=0.2)
    assert p["a"] > 0.9 and p["b"] < 0.15  # suç bilinmeyene kayar


def _kur(istemci, ad):
    b = kayit_ol(istemci, f"{ad}@ornek.com", "ogretmen")
    ice_aktar.aktar(HAVUZ, f"{ad}@ornek.com")
    ids = [q["id"] for q in istemci.get("/api/sorular", headers=b).json()]
    istemci.post("/api/sorular/toplu-onayla", json={"idler": ids}, headers=b)
    return b


def _coz(istemci, h, bilmiyor, ogretmen_h):
    o = istemci.post("/api/uyarlamali", json={"kazanim": "MAT.6.1.2"}, headers=h).json()
    while o["durum"] == "devam":
        tam = istemci.get(f"/api/sorular/{o['soru']['soru_id']}", headers=ogretmen_h).json()
        dogru = next(s["harf"] for s in tam["secenekler"] if s["dogru"])
        yanlis = next(s["harf"] for s in tam["secenekler"] if not s["dogru"])
        o = istemci.post(f"/api/uyarlamali/{o['id']}/cevap", json={"secilen": yanlis if tam["birincil"] in bilmiyor else dogru}, headers=h).json()
    return o


def test_ogretmen_denemesi_koku_bulur(istemci):
    b = _kur(istemci, "u1")
    k = istemci.get("/api/uyarlamali/kazanimlar", headers=b).json()
    assert [x["kod"] for x in k] == ["MAT.6.1.2"] and k[0]["soru_sayisi"] == 80
    o = istemci.post("/api/uyarlamali", json={"kazanim": "MAT.6.1.2"}, headers=b).json()
    assert o["deneme"] and o["mkler"] and "dogru" not in str(o["soru"]["secenekler"])  # öğretmen olasılıkları canlı görür
    o = _coz(istemci, b, {"Mat01MK0065", "Mat01MK0068", "Mat01MK0070", "Mat01MK0072"}, b)
    assert o["kokler"] == ["Mat01MK0065"] and len(o["gecmis"]) <= 15
    assert [g["mk"] for g in o["gecmis"]][:2] == ["Mat01MK0072", "Mat01MK0068"]  # tepeden başlar, yanlışta ön koşula iner


def test_ogrenci_testi_sonda_acilir_ogretmen_listeler(istemci):
    b = _kur(istemci, "u2")
    sinif = istemci.post("/api/siniflar", json={"ad": "u2-6A", "ders": "Matematik", "sinif_duzeyi": 6}, headers=b).json()
    ogr = kayit_ol(istemci, "u2g@ornek.com", "ogrenci", "Ece")
    assert istemci.get("/api/uyarlamali/kazanimlar", headers=ogr).json() == []  # sınıfı yokken havuz yok
    istemci.post("/api/siniflar/katil", json={"kod": sinif["kod"]}, headers=ogr)
    o = istemci.post("/api/uyarlamali", json={"kazanim": "MAT.6.1.2"}, headers=ogr).json()
    assert not o["deneme"] and o["mkler"] == [] and o["gecmis"] == []  # öğrenci test sırasında sonuç görmez
    o = _coz(istemci, ogr, set(), b)  # her şeyi biliyor
    assert o["durum"] == "bitti" and o["kokler"] == [] and o["gecmis"]
    assert sum(1 for m in o["mkler"] if m["durum"] == "biliyor") >= 15
    satir = istemci.get("/api/uyarlamali/oturumlar", headers=b).json()
    assert satir[0]["ogrenci"] == "Ece" and satir[0]["durum"] == "bitti"
    assert istemci.get(f"/api/uyarlamali/{o['id']}", headers=b).status_code == 200
    yabanci = kayit_ol(istemci, "u2y@ornek.com", "ogrenci")
    assert istemci.get(f"/api/uyarlamali/{o['id']}", headers=yabanci).status_code == 404
    assert istemci.post(f"/api/uyarlamali/{o['id']}/cevap", json={"secilen": "A"}, headers=ogr).status_code == 409
