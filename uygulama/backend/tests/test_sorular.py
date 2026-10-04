from conftest import kayit_ol


def _ogretmen(istemci, ad):
    return kayit_ol(istemci, f"{ad}@ornek.com", "ogretmen")


def test_demo_saglayici_ve_ornekler(istemci):
    b = _ogretmen(istemci, "s1")
    r = istemci.get("/api/sorular/saglayici", headers=b).json()
    assert r["ad"] == "demo" and len(r["ornekler"]) == 12


def test_esdeger_direnc_paylari_algoritma_ornegiyle_ayni(istemci):
    """ALGORITMA.md 5.3: Fiz05MK0051 ve dört ön koşulu; paylar v²/Z², b = 5,72."""
    b = _ogretmen(istemci, "s2")
    adimlar = [{"aciklama": a, "mk_kod": k} for a, k in [
        ("gruplara ayırır", "Fiz05MK0037"), ("kısa devreyi çıkarır", "Fiz05MK0038"),
        ("seri", "Fiz05MK0045"), ("paralel", "Fiz05MK0047"), ("indirger", "Fiz05MK0051")]]
    e = istemci.post("/api/sorular/esle", json={"ders": "Fizik", "adimlar": adimlar}, headers=b).json()
    assert [m["kod"] for m in e["soru_mkleri"]] == ["Fiz05MK0051"]
    assert e["zorluk"] == 5.72
    paylar = [round(a["pay"] * 100, 1) for a in e["adimlar"]]
    assert paylar == [12.2, 20.4, 27.5, 27.5, 12.2]
    assert abs(sum(a["pay"] for a in e["adimlar"]) - 1) < 0.001


def test_oncul_soru_mk_si_olmaz(istemci):
    """Yay sorusu: Fiz04MK0129 ve Fiz04MK0124, Fiz04MK0133'ün öncülü; sorunun MK'leri yalnız en üsttekiler."""
    b = _ogretmen(istemci, "s3")
    a = istemci.post("/api/sorular/analiz", json={"ders": "Fizik", "sinif_duzeyi": 12, "ornek": "yay"}, headers=b).json()
    assert sorted(m["kod"] for m in a["eslesme"]["soru_mkleri"]) == ["Fiz02MK0139", "Fiz04MK0096", "Fiz04MK0133"]
    assert a["eslesme"]["zorluk"] == 10.81
    assert a["eslesme"]["birincil"] == "Fiz04MK0133"
    assert a["gorsel"]


def test_kaydet_onayla_listele_ve_yetki(istemci):
    b = _ogretmen(istemci, "s4")
    baska = _ogretmen(istemci, "s5")
    a = istemci.post("/api/sorular/analiz", json={"ders": "Matematik", "sinif_duzeyi": 8, "ornek": "pisagor_hipotenus"}, headers=b).json()
    govde = {k: a[k] for k in ("ders", "sinif_duzeyi", "metin", "gorsel", "cevap_bicimi", "secenekler", "dogru_cevap", "cozum", "birincil", "adimlar")}
    s = istemci.post("/api/sorular", json=govde, headers=b).json()
    assert s["durum"] == "taslak" and s["zorluk"] == 3.16
    assert istemci.post(f"/api/sorular/{s['id']}/onayla", headers=b).json()["durum"] == "onayli"
    assert [x["id"] for x in istemci.get("/api/sorular", params={"mk": "Mat03MK0143"}, headers=b).json()] == [s["id"]]
    assert istemci.get(f"/api/sorular/{s['id']}", headers=baska).status_code == 404  # başkasının sorusu
    ogrenci = kayit_ol(istemci, "s6@ornek.com", "ogrenci")
    assert istemci.get("/api/sorular", headers=ogrenci).status_code == 403


def test_tanimadigi_gorsel_demo_modunda_reddedilir(istemci):
    import base64
    b = _ogretmen(istemci, "s7")
    png = base64.b64encode(b"\x89PNG\r\n\x1a\n" + b"0" * 32).decode()
    r = istemci.post("/api/sorular/analiz", json={"ders": "Fizik", "sinif_duzeyi": 10, "gorsel_base64": png}, headers=b)
    assert r.status_code == 422 and "Demo" in r.json()["detail"]


def test_zincir_disi_rubrik_adimi_ayri_soru_mk_si_olur(istemci):
    """Temel orantı: içler-dışlar (Mat01MK0167) Mat08MK0011'in zincirinde yok, ayrı bir soru MK'si olarak kalır."""
    b = _ogretmen(istemci, "s8")
    a = istemci.post("/api/sorular/analiz", json={"ders": "Matematik", "sinif_duzeyi": 9, "ornek": "temel_oranti"}, headers=b).json()
    assert sorted(m["kod"] for m in a["eslesme"]["soru_mkleri"]) == ["Mat01MK0167", "Mat08MK0011"]


def test_pdf_yuklenir_ve_demo_pdf_tanınır(istemci):
    import base64
    from app.yapay_zeka import DEMO_KLASOR
    b = _ogretmen(istemci, "s9")
    pdf = base64.b64encode((DEMO_KLASOR / "uc_cisim.pdf").read_bytes()).decode()
    a = istemci.post("/api/sorular/analiz", json={"ders": "Fizik", "sinif_duzeyi": 12, "gorsel_base64": pdf}, headers=b).json()
    assert a["gorsel"].endswith(".pdf") and a["dogru_cevap"] == "Yalnız II"
    assert istemci.get(f"/api/gorsel/{a['gorsel']}").headers["content-type"] == "application/pdf"


def test_guncelle_ayni_mklerle_ve_toplu_onay(istemci):
    """Hata düzeltmesi: aynı MK'lerle güncelleme 500 veriyordu (soru_mk tekillik kuralı)."""
    b = _ogretmen(istemci, "s10")
    idler = []
    for ornek, sinif in (("yay", 12), ("uc_cisim", 12)):
        a = istemci.post("/api/sorular/analiz", json={"ders": "Fizik", "sinif_duzeyi": sinif, "ornek": ornek}, headers=b).json()
        govde = {k: a[k] for k in ("ders", "sinif_duzeyi", "metin", "gorsel", "cevap_bicimi", "secenekler", "dogru_cevap", "cozum", "birincil", "adimlar")}
        s = istemci.post("/api/sorular", json=govde, headers=b).json()
        govde["cozum"] += " (düzenlendi)"
        r = istemci.put(f"/api/sorular/{s['id']}", json=govde, headers=b)
        assert r.status_code == 200, r.text
        assert r.json()["zorluk"] == s["zorluk"]
        idler.append(s["id"])
    baska = _ogretmen(istemci, "s11")
    assert istemci.post("/api/sorular/toplu-onayla", json={"idler": idler}, headers=baska).json()["onaylanan"] == 0
    assert istemci.post("/api/sorular/toplu-onayla", json={"idler": idler}, headers=b).json()["onaylanan"] == 2
    assert {x["durum"] for x in istemci.get("/api/sorular", headers=b).json()} == {"onayli"}
