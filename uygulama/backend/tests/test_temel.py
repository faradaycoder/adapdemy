from conftest import kayit_ol


def test_saglik(istemci):
    assert istemci.get("/api/saglik").json() == {"durum": "çalışıyor"}


def test_kayit_giris_ve_ben(istemci):
    baslik = kayit_ol(istemci, "ogretmen1@ornek.com", "ogretmen", "Ayşe Öğretmen")
    assert istemci.get("/api/hesap/ben", headers=baslik).json()["rol"] == "ogretmen"
    # aynı e-postayla ikinci kayıt olmaz
    r = istemci.post("/api/hesap/kayit", json={"ad": "X Y", "eposta": "OGRETMEN1@ornek.com", "sifre": "gizli-sifre-1", "rol": "ogrenci"})
    assert r.status_code == 409
    # doğru ve yanlış şifre
    assert istemci.post("/api/hesap/giris", json={"eposta": "ogretmen1@ornek.com", "sifre": "gizli-sifre-1"}).status_code == 200
    assert istemci.post("/api/hesap/giris", json={"eposta": "ogretmen1@ornek.com", "sifre": "yanlis-sifre"}).status_code == 401


def test_kayitla_yonetici_olunamaz(istemci):
    r = istemci.post("/api/hesap/kayit", json={"ad": "Kötü Niyet", "eposta": "y@ornek.com", "sifre": "gizli-sifre-1", "rol": "yonetici"})
    assert r.status_code == 422


def test_jetonsuz_ve_bozuk_jetonla_erisim_yok(istemci):
    assert istemci.get("/api/hesap/ben").status_code == 401
    assert istemci.get("/api/hesap/ben", headers={"Authorization": "Bearer bozuk.jeton"}).status_code == 401


def test_sinif_ac_katil_ve_yetki(istemci):
    ogretmen = kayit_ol(istemci, "ogretmen2@ornek.com", "ogretmen")
    ogrenci = kayit_ol(istemci, "ogrenci1@ornek.com", "ogrenci", "Ali Öğrenci")
    baska_ogrenci = kayit_ol(istemci, "ogrenci2@ornek.com", "ogrenci")

    # öğrenci sınıf açamaz
    assert istemci.post("/api/siniflar", json={"ad": "10-A", "ders": "Fizik", "sinif_duzeyi": 10}, headers=ogrenci).status_code == 403

    s = istemci.post("/api/siniflar", json={"ad": "10-A Fizik", "ders": "Fizik", "sinif_duzeyi": 10}, headers=ogretmen).json()
    assert len(s["kod"]) == 6

    # öğrenci kodla katılır (küçük harfle yazsa da), iki kez katılınca tek üyelik olur
    for kod in (s["kod"].lower(), s["kod"]):
        r = istemci.post("/api/siniflar/katil", json={"kod": kod}, headers=ogrenci)
        assert r.status_code == 200 and r.json()["kod"] is None  # öğrenci sınıf kodunu görmez
    assert istemci.post("/api/siniflar/katil", json={"kod": "ZZZZZZ"}, headers=ogrenci).status_code == 404

    ayrinti = istemci.get(f"/api/siniflar/{s['id']}", headers=ogretmen).json()
    assert [o["ad"] for o in ayrinti["ogrenciler"]] == ["Ali Öğrenci"]

    # sınıfta olmayan öğrenci sınıfı göremez
    assert istemci.get(f"/api/siniflar/{s['id']}", headers=baska_ogrenci).status_code == 404
    assert [x["ad"] for x in istemci.get("/api/siniflar", headers=ogrenci).json()] == ["10-A Fizik"]


def test_mk_verisi_aktarildi(istemci):
    baslik = kayit_ol(istemci, "ogretmen3@ornek.com", "ogretmen")
    ozet = istemci.get("/api/mk/ozet", headers=baslik).json()
    assert ozet["Fizik"]["mk"] == 766 and ozet["Matematik"]["mk"] == 1664
    assert ozet["Fizik"]["bag"] == 1208 and ozet["Matematik"]["bag"] == 2599

    m = istemci.get("/api/mk/Fiz05MK0051", headers=baslik).json()
    assert m["zorluk"] == 5.72 and m["seviye"] == 5
    assert {x["kod"] for x in m["on_kosullar"]} == {"Fiz05MK0037", "Fiz05MK0038", "Fiz05MK0045", "Fiz05MK0047"}
    assert any(e["ogrenme_ciktisi"] == "FİZ.10.3.4" for e in m["eslemeler"])

    sonuc = istemci.get("/api/mk", params={"ogrenme_ciktisi": "FİZ.10.3.4", "limit": 100}, headers=baslik).json()
    assert len(sonuc) == 27
