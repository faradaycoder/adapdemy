import json

from sqlalchemy import select

from app import otomatik_aktar
from app.modeller import Sinav
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
