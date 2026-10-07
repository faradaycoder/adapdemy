import base64
from datetime import datetime, timedelta, timezone

from conftest import kayit_ol
from test_sinavlar import _soru


def _kurulum(istemci, ad, bas_saat=-1, bit_saat=1, sure=None):
    b = kayit_ol(istemci, f"{ad}o@ornek.com", "ogretmen")
    q1 = _soru(istemci, b, "egik_atis", 11)      # çoktan seçmeli
    q2 = _soru(istemci, b, "yay", 12)            # yazılı
    s = istemci.post("/api/sinavlar", json={"ad": "D testi", "ders": "Fizik", "sinif_duzeyi": 12, "sure_dk": sure,
                                            "soru_idler": [q1["id"], q2["id"]]}, headers=b).json()
    sinif = istemci.post("/api/siniflar", json={"ad": f"{ad}-sinif", "ders": "Fizik", "sinif_duzeyi": 12}, headers=b).json()
    ogr = kayit_ol(istemci, f"{ad}g@ornek.com", "ogrenci", "Ece")
    istemci.post("/api/siniflar/katil", json={"kod": sinif["kod"]}, headers=ogr)
    simdi = datetime.now(timezone.utc)
    a = istemci.post(f"/api/sinavlar/{s['id']}/ata", json={"sinif_id": sinif["id"], "baslangic": (simdi + timedelta(hours=bas_saat)).isoformat(),
                                                          "bitis": (simdi + timedelta(hours=bit_saat)).isoformat()}, headers=b).json()
    return b, ogr, a, q1, q2


def test_ogrenci_cozer_foto_yukler_teslim_eder_ogretmen_gorur(istemci):
    from app.yapay_zeka import DEMO_KLASOR
    b, ogr, a, q1, q2 = _kurulum(istemci, "d1")
    assert istemci.get(f"/api/teslim/{a['id']}/yazdir", headers=ogr).status_code == 409  # başlamadan yazdırılamaz
    o = istemci.post(f"/api/teslim/{a['id']}/basla", headers=ogr).json()
    y = istemci.get(f"/api/teslim/{a['id']}/yazdir", headers=ogr).json()  # öğrencinin kendi kopyası
    assert len(y["ogrenciler"]) == 1 and y["atama_id"] == a["id"] and len(y["sorular"]) == 2 and "cozum" not in str(y)
    assert o["durum"] == "devam" and [x["soru_id"] for x in o["sorular"]] == [q1["id"], q2["id"]]
    assert "dogru" not in str(o["sorular"]) and "cozum" not in str(o)

    assert istemci.put(f"/api/teslim/{a['id']}/cevap/{q1['id']}", json={"secilen": "C"}, headers=ogr).status_code == 200
    foto = base64.b64encode((DEMO_KLASOR / "yay.png").read_bytes()).decode()
    r = istemci.post(f"/api/teslim/{a['id']}/cevap/{q2['id']}/dosya", json={"dosya_base64": foto}, headers=ogr).json()
    assert len(r["dosyalar"]) == 1
    istemci.put(f"/api/teslim/{a['id']}/cevap/{q2['id']}", json={"metin": "x ≈ 77,5 cm"}, headers=ogr)

    o = istemci.post(f"/api/teslim/{a['id']}/gonder", headers=ogr).json()
    assert o["durum"] == "teslim"
    # teslimden sonra değişiklik yok
    assert istemci.put(f"/api/teslim/{a['id']}/cevap/{q1['id']}", json={"secilen": "A"}, headers=ogr).status_code == 409

    satirlar = istemci.get(f"/api/atamalar/{a['id']}/teslimler", headers=b).json()
    assert satirlar[0]["durum"] == "teslim" and satirlar[0]["cevaplanan"] == 2
    d = istemci.get(f"/api/atamalar/{a['id']}/teslimler/{satirlar[0]['teslim_id']}", headers=b).json()
    c = {x["soru_id"]: x for x in d["cevaplar"]}
    assert c[q1["id"]]["secilen"] == "C" and len(c[q2["id"]]["dosyalar"]) == 1 and c[q2["id"]]["metin"] == "x ≈ 77,5 cm"


def test_kapali_sinav_ve_sinif_disi_ogrenci(istemci):
    b, ogr, a, q1, _ = _kurulum(istemci, "d2", bas_saat=1, bit_saat=2)  # henüz başlamadı
    assert istemci.post(f"/api/teslim/{a['id']}/basla", headers=ogr).status_code == 409
    yabanci = kayit_ol(istemci, "d2y@ornek.com", "ogrenci")
    assert istemci.post(f"/api/teslim/{a['id']}/basla", headers=yabanci).status_code == 404
    assert istemci.get(f"/api/atamalar/{a['id']}/teslimler", headers=ogr).status_code == 403


def test_bildirimler(istemci):
    b, ogr, a, q1, _ = _kurulum(istemci, "d3")
    bo = istemci.get("/api/bildirimler", headers=ogr).json()
    assert bo["sayi"] == 1 and bo["ogeler"][0]["baglanti"] == f"/sinav/{a['id']}"
    assert istemci.get("/api/bildirimler", headers=b).json()["sayi"] == 0
    istemci.post(f"/api/teslim/{a['id']}/basla", headers=ogr)
    istemci.post(f"/api/teslim/{a['id']}/gonder", headers=ogr)
    assert istemci.get("/api/bildirimler", headers=ogr).json()["sayi"] == 0  # teslim edince düşer
    bt = istemci.get("/api/bildirimler", headers=b).json()
    assert bt["sayi"] == 1 and "teslim etti" in bt["ogeler"][0]["metin"]
    assert istemci.post("/api/bildirimler/okundu", headers=b).json()["okundu"] == 1
    assert istemci.get("/api/bildirimler", headers=b).json()["sayi"] == 0


def test_sinav_silinince_teslimler_de_silinir(istemci):
    b, ogr, a, q1, _ = _kurulum(istemci, "d4")
    istemci.post(f"/api/teslim/{a['id']}/basla", headers=ogr)
    istemci.put(f"/api/teslim/{a['id']}/cevap/{q1['id']}", json={"secilen": "C"}, headers=ogr)
    assert istemci.delete(f"/api/sinavlar/{a['sinav_id']}", headers=b).status_code == 204
    from app.modeller import Teslim
    from app.vt import Oturum
    with Oturum() as vt:
        assert vt.query(Teslim).filter(Teslim.atama_id == a["id"]).count() == 0


def test_sinavin_tamami_icin_dosya(istemci):
    from app.yapay_zeka import DEMO_KLASOR
    b, ogr, a, q1, _ = _kurulum(istemci, "d5")
    istemci.post(f"/api/teslim/{a['id']}/basla", headers=ogr)
    pdf = base64.b64encode((DEMO_KLASOR / "uc_cisim.pdf").read_bytes()).decode()
    o = istemci.post(f"/api/teslim/{a['id']}/dosya", json={"dosya_base64": pdf}, headers=ogr).json()
    assert len(o["genel_dosyalar"]) == 1 and o["genel_dosyalar"][0]["dosya"].endswith(".pdf")
    did = o["genel_dosyalar"][0]["id"]
    foto = base64.b64encode((DEMO_KLASOR / "yay.png").read_bytes()).decode()
    istemci.post(f"/api/teslim/{a['id']}/dosya", json={"dosya_base64": foto}, headers=ogr)
    o = istemci.delete(f"/api/teslim/{a['id']}/dosya/{did}", headers=ogr).json()
    assert len(o["genel_dosyalar"]) == 1
    istemci.post(f"/api/teslim/{a['id']}/gonder", headers=ogr)
    satir = istemci.get(f"/api/atamalar/{a['id']}/teslimler", headers=b).json()[0]
    assert satir["genel_dosya"] == 1
    d = istemci.get(f"/api/atamalar/{a['id']}/teslimler/{satir['teslim_id']}/degerlendirme", headers=b).json()
    assert len(d["genel_dosyalar"]) == 1


def _geri_al(tablo, kimlik, alan, deger):
    """Testte zamanı ileri saramadığımız için kayıtları geçmişe çeker (ör. teslim başlaması, atama bitişi)."""
    from app.modeller import Atama, Teslim
    from app.vt import Oturum
    with Oturum() as vt:
        setattr(vt.get({"teslim": Teslim, "atama": Atama}[tablo], kimlik), alan, deger)
        vt.commit()


def test_sure_dolunca_kendiliginden_teslim_ve_uzatma(istemci):
    b, ogr, a, q1, q2 = _kurulum(istemci, "d6", sure=20)
    istemci.post(f"/api/teslim/{a['id']}/basla", headers=ogr)
    istemci.put(f"/api/teslim/{a['id']}/cevap/{q2['id']}", json={"metin": "yarım çözüm"}, headers=ogr)
    tid = istemci.get(f"/api/atamalar/{a['id']}/teslimler", headers=b).json()[0]["teslim_id"]
    assert istemci.post(f"/api/teslim/{a['id']}/uzatma", json={}, headers=ogr).status_code == 409  # süre dolmadan istenmez
    _geri_al("teslim", tid, "baslama", datetime.now(timezone.utc) - timedelta(minutes=30))

    # öğretmen: hiçbir şey yapılmasa da teslim edildi görünür ve bildirim gelir
    s = istemci.get(f"/api/atamalar/{a['id']}/teslimler", headers=b).json()[0]
    assert s["durum"] == "teslim" and s["otomatik_teslim"] and s["cevaplanan"] == 1
    assert "süre doldu, cevapları kendiliğinden teslim edildi" in istemci.get("/api/bildirimler", headers=b).json()["ogeler"][0]["metin"]
    o = istemci.post(f"/api/teslim/{a['id']}/basla", headers=ogr).json()
    assert o["durum"] == "teslim" and o["otomatik_teslim"]
    ana = istemci.get("/api/atamalar", headers=ogr).json()[0]  # öğrencinin ana sayfası: "Süre uzatma iste" gösterilir
    assert ana["teslim_durumu"] == "teslim" and ana["otomatik_teslim"] and ana["uzatma"] is None
    assert istemci.put(f"/api/teslim/{a['id']}/cevap/{q2['id']}", json={"metin": "x"}, headers=ogr).status_code == 409

    # öğrenci uzatma ister → öğretmene bildirim
    o = istemci.post(f"/api/teslim/{a['id']}/uzatma", json={"aciklama": "İnternetim kesildi"}, headers=ogr).json()
    assert o["uzatma"] == "bekliyor"
    assert istemci.post(f"/api/teslim/{a['id']}/uzatma", json={}, headers=ogr).status_code == 409  # bir kez
    bt = [x for x in istemci.get("/api/bildirimler", headers=b).json()["ogeler"] if x["tur"] == "uzatma"]
    assert len(bt) == 1 and "İnternetim kesildi" in bt[0]["metin"]
    istemci.post("/api/bildirimler/okundu", headers=b)
    assert any(x["tur"] == "uzatma" for x in istemci.get("/api/bildirimler", headers=b).json()["ogeler"])  # karar verilene kadar durur

    # öğretmen 15 dakika verir → sınav yeniden açılır, öğrenciye bildirim
    assert istemci.post(f"/api/atamalar/{a['id']}/teslimler/{tid}/uzatma", json={"karar": "ver"}, headers=b).status_code == 422
    r = istemci.post(f"/api/atamalar/{a['id']}/teslimler/{tid}/uzatma", json={"karar": "ver", "dk": 15}, headers=b).json()
    assert r[0]["durum"] == "devam" and r[0]["uzatma"] == "verildi" and r[0]["uzatma_dk"] == 15
    bo = istemci.get("/api/bildirimler", headers=ogr).json()["ogeler"]
    assert [x["tur"] for x in bo] == ["uzatma_sonuc"] and "15 dakika" in bo[0]["metin"]
    o = istemci.post(f"/api/teslim/{a['id']}/basla", headers=ogr).json()
    kalan = (datetime.fromisoformat(o["bitis"]) - datetime.now(timezone.utc)).total_seconds()
    assert o["durum"] == "devam" and 14 * 60 < kalan <= 15 * 60
    assert istemci.get("/api/bildirimler", headers=ogr).json()["sayi"] == 0  # sınavı açınca düştü
    assert istemci.put(f"/api/teslim/{a['id']}/cevap/{q2['id']}", json={"metin": "tam çözüm"}, headers=ogr).status_code == 200
    o = istemci.post(f"/api/teslim/{a['id']}/gonder", headers=ogr).json()
    assert o["durum"] == "teslim" and not o["otomatik_teslim"]


def test_uzatma_reddedilir(istemci):
    b, ogr, a, *_ = _kurulum(istemci, "d7", sure=10)
    istemci.post(f"/api/teslim/{a['id']}/basla", headers=ogr)
    tid = istemci.get(f"/api/atamalar/{a['id']}/teslimler", headers=b).json()[0]["teslim_id"]
    _geri_al("teslim", tid, "baslama", datetime.now(timezone.utc) - timedelta(minutes=11))
    istemci.post(f"/api/teslim/{a['id']}/uzatma", json={}, headers=ogr)
    r = istemci.post(f"/api/atamalar/{a['id']}/teslimler/{tid}/uzatma", json={"karar": "reddet"}, headers=b).json()
    assert r[0]["durum"] == "teslim" and r[0]["uzatma"] == "reddedildi"
    assert "kabul edilmedi" in istemci.get("/api/bildirimler", headers=ogr).json()["ogeler"][0]["metin"]
    assert istemci.post(f"/api/teslim/{a['id']}/basla", headers=ogr).json()["durum"] == "teslim"
    assert istemci.post(f"/api/teslim/{a['id']}/uzatma", json={}, headers=ogr).status_code == 409  # karar kesin


def test_hic_acilmayan_sinav_bos_kagit_olarak_teslim(istemci):
    b, ogr, a, *_ = _kurulum(istemci, "d8")
    _geri_al("atama", a["id"], "bitis", datetime.now(timezone.utc))  # öğrenci bitişten önce katılmıştı
    s = istemci.get(f"/api/atamalar/{a['id']}/teslimler", headers=b).json()[0]
    assert s["durum"] == "teslim" and s["otomatik_teslim"] and s["cevaplanan"] == 0
    assert "boş kâğıt" in istemci.get("/api/bildirimler", headers=b).json()["ogeler"][0]["metin"]
    o = istemci.post(f"/api/teslim/{a['id']}/basla", headers=ogr).json()  # atama bitmiş olsa da öğrenci durumunu görür
    assert o["durum"] == "teslim" and o["otomatik_teslim"]
    assert istemci.post(f"/api/teslim/{a['id']}/uzatma", json={}, headers=ogr).json()["uzatma"] == "bekliyor"
