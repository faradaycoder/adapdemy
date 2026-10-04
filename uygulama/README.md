# EVALORA uygulaması

*Measure. Diagnose. Remediate.* (Ölç. Teşhis et. Telafi et.) · Micro-skill based assessment, diagnosis and remediation. Kapsam ve plan: `../PLAN_UYGULAMA.md`. Ölçme modeli: `../ALGORITMA.md`.

## Yapı

```
uygulama/
├── backend/    Python, FastAPI, SQLAlchemy (yerelde SQLite, sunucuda PostgreSQL)
│   ├── app/main.py          uygulama girişi
│   ├── app/modeller.py      veritabanı tabloları
│   ├── app/kimlik.py        şifre, oturum jetonu, roller
│   ├── app/mk_aktar.py      MK verisini EVALORA CSV'lerinden veritabanına aktarır
│   ├── app/eslestirme.py    soru–MK eşleme kuralları, soru zorluğu, rubrik payları (ALGORITMA.md bölüm 5)
│   ├── app/yapay_zeka.py    soruyu okuma ve eşleme: demo modu ya da Claude API (ANTHROPIC_API_KEY)
│   ├── app/demo/            demo modundaki örnek sorular ve görselleri
│   ├── app/routers/         hesap, siniflar, mk, sorular, sinavlar, teslim
│   └── tests/               pytest
└── frontend/   React, TypeScript, Vite (PWA)
```

## Çalıştırma (yerel)

En kolayı: `EVALORA/EVALORA-Baslat.command` dosyasına çift tıkla. İkisini birden başlatır ve tarayıcıyı açar; pencere açık kaldıkça çalışır. Açıkken iki dakikada bir GitHub'daki `main` dalını çeker ve `ice_aktarma/` altına gelen yeni soru setlerini öğretmenin bankasına kendiliğinden aktarır (`python -m app.otomatik_aktar`; her klasör bir kez). Birden çok öğretmen hesabı varsa `backend/.env`'ye `EVALORA_OGRETMEN_EPOSTA=<e-posta>` yazılır.

Elle başlatmak için:

Arka uç:
```
cd uygulama/backend
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload            # http://127.0.0.1:8000, API belgesi /docs
pytest                                   # testler
python -m app.mk_aktar                   # CSV'ler değişince MK verisini yeniden aktar
python -m app.ice_aktar ../ice_aktarma/kazanim_kavrama_16 <ogretmen-eposta>   # hazır analiz edilmiş soru setini (ve sınavı) bankaya aktar
python -m app.degerlendirme_aktar ../ice_aktarma/degerlendirmeler/<dosya>.json  # dışarıda yapılmış değerlendirmeyi sistem önerisi olarak aktar
```

Ön yüz (ayrı bir terminalde):
```
cd uygulama/frontend
npm install
npm run dev                              # http://localhost:5173
```

Veritabanı `backend/veri/evalora.db` dosyasındadır. Oturum jetonlarını imzalayan anahtar ilk açılışta `backend/veri/.gizli_anahtar` dosyasına yazılır; sunucuda `EVALORA_SECRET` ortam değişkeniyle verilir. PostgreSQL için `DATABASE_URL` ortam değişkeni ayarlanır.

## Aşamalar

- [x] **A. Temel:** hesaplar (öğretmen, öğrenci), sınıf açma, sınıf koduyla katılma, MK verisinin aktarımı, MK haritası görüntüleme
- [ ] Google ile giriş (Google Cloud'da OAuth istemcisi gerekiyor)
- [x] **B. Soru bankası (demo modu):** soru yükleme (fotoğraf, görsel, metin), okuma ve çözme, rubrik, adım → MK eşleme, sorunun MK'leri (en üsttekiler), zorluk (Σ Z), rubrik payları, öğretmenin düzeltip onaylaması, liste ve filtre. Gerçek okuma için `ANTHROPIC_API_KEY` gerekir; yokken yalnız 7 örnek soru tanınır.
- [x] **C. Sınav:** bankadaki onaylı sorulardan sınav (soru öneri: kazanım ya da MK'ye göre, MK kapsamı geniş), toplam zorluk ve sınavın ölçtüğü MK'ler, sınıfa atama (başlangıç, bitiş), öğrencinin sınav listesi, yazdırılabilir sınav (boş kopya ya da öğrenci başına kopya, soru başına QR verisi). Yazdırılan sayfalarda soru başına QR kod (`qrcode` paketi).
- [x] **D. Teslim:** öğrenci atanan sınavı açar (süre ilk açılışta başlar), çoktan seçmeli işaretler, kısa ya da yazılı cevap yazar (otomatik kayıt), soru başına fotoğraf ya da dosya (en fazla 6 parça) ekler, teslim eder; teslimden ve süreden sonra cevaplar kilitlenir. Öğretmen atama başına teslim durumunu ve cevapları görür.
- [x] **E. Değerlendirme:** çoktan seçmeliler teslimde otomatik değerlendirilir (doğru: bütün adımlar biliyor; yanlış: sorunun MK'leri bilmiyor, ön koşul adımları ölçülemedi; boş: ölçülemedi; çeldiricinin yanılgısı kaydedilir). Yazılı ve kâğıt cevaplarda öğretmen her rubrik adımına biliyor / bilmiyor / ölçülemedi der; puan = pay × soru zorluğu. Öğretmen onaylayınca sonuç öğrenciye açılır: puan, adım adım sonuç, MK teşhisi, doğru cevap ve çözüm.
- [ ] Soru üretme (MK'den) · F. Rapor · G. Pilot
