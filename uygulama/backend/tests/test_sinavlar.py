from datetime import datetime, timedelta, timezone

from conftest import kayit_ol


def _soru(istemci, b, ornek, sinif, onayla=True):
    a = istemci.post("/api/sorular/analiz", json={"ders": "Fizik", "sinif_duzeyi": sinif, "ornek": ornek}, headers=b).json()
    govde = {k: a[k] for k in ("ders", "sinif_duzeyi", "metin", "gorsel", "cevap_bicimi", "secenekler", "dogru_cevap", "cozum", "birincil", "adimlar")}
    s = istemci.post("/api/sorular", json=govde, headers=b).json()
    if onayla:
        istemci.post(f"/api/sorular/{s['id']}/onayla", headers=b)
    return s


def test_sinav_olustur_ata_ve_ogrenci_gorur(istemci):
    b = kayit_ol(istemci, "sv1@ornek.com", "ogretmen")
    q1 = _soru(istemci, b, "yay", 12)
    q2 = _soru(istemci, b, "uc_cisim", 12)
    taslak = _soru(istemci, b, "surtunmeli_yol", 12, onayla=False)

    # taslak soruyla sınav kaydedilebilir ama onaylanmadan atanamaz
    tsv = istemci.post("/api/sinavlar", json={"ad": "Enerji", "ders": "Fizik", "sinif_duzeyi": 12, "soru_idler": [q1["id"], taslak["id"]]}, headers=b)
    assert tsv.status_code == 201

    s = istemci.post("/api/sinavlar", json={"ad": "Enerji yoklaması", "ders": "Fizik", "sinif_duzeyi": 12,
                                            "soru_idler": [q1["id"], q2["id"]]}, headers=b).json()
    assert [x["id"] for x in s["sorular"]] == [q1["id"], q2["id"]]
    assert s["toplam_zorluk"] == round(q1["zorluk"] + q2["zorluk"], 2)
    assert {"Fiz04MK0133", "Fiz02MK0059"} <= {m["kod"] for m in s["kapsam"]}

    # öneri: yalnız onaylı sorular
    oneri = istemci.post("/api/sinavlar/oneri", json={"ders": "Fizik", "sinif_duzeyi": 12, "adet": 5}, headers=b).json()
    assert {x["id"] for x in oneri} == {q1["id"], q2["id"]}

    sinif = istemci.post("/api/siniflar", json={"ad": "12-A", "ders": "Fizik", "sinif_duzeyi": 12}, headers=b).json()
    ogr = kayit_ol(istemci, "sv2@ornek.com", "ogrenci", "Zeynep")
    istemci.post("/api/siniflar/katil", json={"kod": sinif["kod"]}, headers=ogr)
    simdi = datetime.now(timezone.utc)
    r = istemci.post(f"/api/sinavlar/{tsv.json()['id']}/ata", json={"sinif_id": sinif["id"], "baslangic": (simdi - timedelta(hours=1)).isoformat(),
                                                                "bitis": (simdi + timedelta(hours=1)).isoformat()}, headers=b)
    assert r.status_code == 422 and "onaylanmamış" in r.json()["detail"]
    a = istemci.post(f"/api/sinavlar/{s['id']}/ata", json={"sinif_id": sinif["id"], "baslangic": (simdi - timedelta(hours=1)).isoformat(),
                                                          "bitis": (simdi + timedelta(hours=1)).isoformat()}, headers=b)
    assert a.status_code == 201 and a.json()["durum"] == "acik"
    ogr_atamalar = istemci.get("/api/atamalar", headers=ogr).json()
    assert [x["sinav_adi"] for x in ogr_atamalar] == ["Enerji yoklaması"]

    y = istemci.get(f"/api/sinavlar/{s['id']}/yazdir", params={"atama_id": a.json()["id"]}, headers=b).json()
    assert [o["ad"] for o in y["ogrenciler"]] == ["Zeynep"] and len(y["sorular"]) == 2
    assert "dogru" not in str(y["sorular"])  # yazdırmada doğru cevap yok

    # başka öğretmen sınavı göremez, öğrenci sınav listesine erişemez
    baska = kayit_ol(istemci, "sv3@ornek.com", "ogretmen")
    assert istemci.get(f"/api/sinavlar/{s['id']}", headers=baska).status_code == 404
    assert istemci.get("/api/sinavlar", headers=ogr).status_code == 403


def test_bitis_baslangictan_once_olamaz(istemci):
    b = kayit_ol(istemci, "sv4@ornek.com", "ogretmen")
    q = _soru(istemci, b, "yay", 12)
    s = istemci.post("/api/sinavlar", json={"ad": "X", "ders": "Fizik", "sinif_duzeyi": 12, "soru_idler": [q["id"]]}, headers=b).json()
    sinif = istemci.post("/api/siniflar", json={"ad": "12-B", "ders": "Fizik", "sinif_duzeyi": 12}, headers=b).json()
    simdi = datetime.now(timezone.utc).isoformat()
    r = istemci.post(f"/api/sinavlar/{s['id']}/ata", json={"sinif_id": sinif["id"], "baslangic": simdi, "bitis": simdi}, headers=b)
    assert r.status_code == 422
