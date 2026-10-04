import os
import tempfile

import pytest

# Testler gerçek veritabanına dokunmaz: geçici bir SQLite dosyası kullanılır.
_gecici = tempfile.mkdtemp()
os.environ["DATABASE_URL"] = f"sqlite:///{_gecici}/test.db"
os.environ["EVALORA_SECRET"] = "test-anahtari"
os.environ["EVALORA_ENV_YOK"] = "1"  # .env'deki gerçek Azure/Anthropic anahtarları testlere girmesin

from fastapi.testclient import TestClient  # noqa: E402

from app.main import app  # noqa: E402


@pytest.fixture(scope="session")
def istemci():
    with TestClient(app) as c:  # açılışta tablolar kurulur ve MK verisi aktarılır
        yield c


def kayit_ol(istemci, eposta, rol, ad="Deneme Kişi"):
    r = istemci.post("/api/hesap/kayit", json={"ad": ad, "eposta": eposta, "sifre": "gizli-sifre-1", "rol": rol})
    assert r.status_code == 201, r.text
    return {"Authorization": f"Bearer {r.json()['jeton']}"}
