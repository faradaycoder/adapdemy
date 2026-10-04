import json

from sqlalchemy import select

from app import otomatik_aktar
from app.modeller import Kullanici, Sinav
from app.vt import Oturum
from conftest import kayit_ol


def _set_yaz(klasor, metin, mk, sinav=None):
    klasor.mkdir()
    veri = {"ders": "Matematik", "sinif_duzeyi": 6,
            "sorular": [{"no": 1, "cevap_bicimi": "yazili", "metin": metin, "adimlar": [["Kuralı kullanır.", mk]]}]}
    if sinav:
        veri["sinav"] = {"ad": sinav, "sure_dk": 20}
    (klasor / "sorular.json").write_text(json.dumps(veri), encoding="utf-8")


def test_yeni_klasor_bir_kez_aktarilir(istemci, tmp_path, monkeypatch):
    kayit_ol(istemci, "oto@ornek.com", "ogretmen")
    monkeypatch.setenv("EVALORA_OGRETMEN_EPOSTA", "oto@ornek.com")
    monkeypatch.setattr(otomatik_aktar, "KAYIT", tmp_path / "aktarilanlar.txt")
    _set_yaz(tmp_path / "set1", "Oto: 102 sayısı 3 ile bölünür mü?", "Mat01MK0065", sinav="Oto sınav")

    mesajlar = otomatik_aktar.calistir(tmp_path)
    with Oturum() as vt:
        sid = vt.scalar(select(Sinav.id).where(Sinav.ad == "Oto sınav"))
    assert mesajlar == [f"set1: 1 soru ve sınav #{sid} aktarıldı (taslak)."]
    assert otomatik_aktar.calistir(tmp_path) == []  # ikinci kez aktarılmaz


def test_onceden_elle_aktarilan_atlanir(istemci, tmp_path, monkeypatch):
    kayit_ol(istemci, "oto2@ornek.com", "ogretmen")
    monkeypatch.setenv("EVALORA_OGRETMEN_EPOSTA", "oto2@ornek.com")
    monkeypatch.setattr(otomatik_aktar, "KAYIT", tmp_path / "aktarilanlar.txt")
    _set_yaz(tmp_path / "set2", "Oto: 96 sayısı 4 ile bölünür mü?", "Mat01MK0067")
    otomatik_aktar.aktar(tmp_path / "set2", "oto2@ornek.com")  # daha önce elle aktarılmış

    assert otomatik_aktar.calistir(tmp_path) == []
    assert "set2" in (tmp_path / "aktarilanlar.txt").read_text(encoding="utf-8")


def test_ogretmen_belirsizse_atlanir(istemci, tmp_path, monkeypatch):
    monkeypatch.delenv("EVALORA_OGRETMEN_EPOSTA", raising=False)  # testlerde birden çok öğretmen var
    assert "öğretmen belirlenemedi" in otomatik_aktar.calistir(tmp_path)[0]


def test_bulutta_okunan_kagit_degerlendirmesi_aktarilir(istemci, tmp_path, monkeypatch):
    import shutil
    from datetime import datetime, timedelta, timezone

    b = kayit_ol(istemci, "oto3@ornek.com", "ogretmen")
    monkeypatch.setenv("EVALORA_OGRETMEN_EPOSTA", "oto3@ornek.com")
    monkeypatch.setattr(otomatik_aktar, "KAYIT", tmp_path / "aktarilanlar.txt")
    shutil.copytree(otomatik_aktar.KLASOR / "mat6_bolunebilme", tmp_path / "mat6_bolunebilme")
    otomatik_aktar.calistir(tmp_path)
    with Oturum() as vt:
        sid = vt.scalar(select(Sinav.id).where(Sinav.ad == "6. sınıf bölünebilme kuralları çalışma kâğıdı",
                                               Sinav.olusturan_id == vt.scalar(select(Kullanici.id).where(Kullanici.eposta == "oto3@ornek.com"))))
    ids = [q["id"] for q in istemci.get("/api/sorular", headers=b).json()]
    assert istemci.post("/api/sorular/toplu-onayla", json={"idler": ids}, headers=b).status_code == 200
    sinif = istemci.post("/api/siniflar", json={"ad": "oto3-6A", "ders": "Matematik", "sinif_duzeyi": 6}, headers=b).json()
    ogr = kayit_ol(istemci, "oto3g@ornek.com", "ogrenci")
    istemci.post("/api/siniflar/katil", json={"kod": sinif["kod"]}, headers=ogr)
    simdi = datetime.now(timezone.utc)
    a = istemci.post(f"/api/sinavlar/{sid}/ata", json={"sinif_id": sinif["id"], "baslangic": (simdi - timedelta(hours=1)).isoformat(),
                                                      "bitis": (simdi + timedelta(hours=1)).isoformat()}, headers=b).json()
    istemci.post(f"/api/teslim/{a['id']}/basla", headers=ogr)
    istemci.post(f"/api/teslim/{a['id']}/gonder", headers=ogr)
    tid = istemci.get(f"/api/atamalar/{a['id']}/teslimler", headers=b).json()[0]["teslim_id"]

    (tmp_path / "degerlendirmeler").mkdir()
    (tmp_path / "degerlendirmeler" / "oto3.json").write_text(json.dumps({
        "teslim_id": tid, "soru_seti": "mat6_bolunebilme",
        "sorular": {"9": {"okunan": "4+★ 3'ün katı: 2, 5, 8 → 15",
                          "kararlar": {"1": ["biliyor", "Çift."], "2": ["biliyor", "2, 5, 8."], "3": ["biliyor", "15."]}}}}),
        encoding="utf-8")
    mesajlar = otomatik_aktar.calistir(tmp_path)
    assert len(mesajlar) == 1 and "değerlendirme önerisi aktarıldı" in mesajlar[0], mesajlar
    d = istemci.get(f"/api/atamalar/{a['id']}/teslimler/{tid}/degerlendirme", headers=b).json()
    s9 = next(s for s in d["sorular"] if s["metin"].startswith("Üç basamaklı 4★0"))
    assert [x["durum"] for x in s9["adimlar"]] == ["biliyor"] * 3 and {x["kaynak"] for x in s9["adimlar"]} == {"sistem"}
    assert s9["metin_cevap"].endswith("→ 15")
    assert otomatik_aktar.calistir(tmp_path) == []  # bir kez



def test_video_dosyasi_degisince_yeniden_aktarilir(istemci, tmp_path, monkeypatch):
    kayit_ol(istemci, "oto4@ornek.com", "ogretmen")
    monkeypatch.setenv("EVALORA_OGRETMEN_EPOSTA", "oto4@ornek.com")
    monkeypatch.setattr(otomatik_aktar, "KAYIT", tmp_path / "aktarilanlar.txt")
    (tmp_path / "videolar").mkdir()
    dosya = tmp_path / "videolar" / "v.json"
    veri = {"videolar": {"abcdefghijk": {"kanal": "K", "baslik": "B", "sure": 600}}, "konular": {},
            "parcalar": [{"mk": "Mat01MK0062", "tur": "konu", "video": "abcdefghijk", "bas": "0:10", "son": "1:00",
                          "baslik": "2 ile bölünme", "neden": "deneme"}]}
    dosya.write_text(json.dumps(veri), encoding="utf-8")
    assert otomatik_aktar.calistir(tmp_path)[0].startswith("v: ")
    assert otomatik_aktar.calistir(tmp_path) == []
    veri["parcalar"][0]["son"] = "1:10"
    dosya.write_text(json.dumps(veri), encoding="utf-8")
    assert otomatik_aktar.calistir(tmp_path)[0].startswith("v: ")
