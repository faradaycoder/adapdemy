# EVALORA: Claude için çalışma talimatı

Murat (öğretmen, proje sahibi) Türkçe yazar; cevaplar Türkçe, kısa ve sade olur. Kodlama kuralları `KODLAMA.md`, ölçme
modeli `ALGORITMA.md`, uygulama planı `PLAN_UYGULAMA.md`, uygulamanın kendisi `uygulama/README.md`, uyarlamalı
test `UYARLAMALI_TEST.md` (+ çizimli akış `UYARLAMALI_TEST_AKIS.html`).

## Sormadan yürü (Murat, 2026-10-04)

Her sınav için aynı döngü yapılır; adımlar için izin istenmez, onay beklenmez. Murat'a terminal komutu, git ya da GitHub
işi yaptırılmaz. Yalnız gerçekten onun vereceği bir karar varsa (ör. bir rubrik kararının pedagojik tercihi) sorulur;
o durumda da öneri uygulanır, karar ona bırakılır.

## Döngü

1. **Sınav kâğıdı gelir** (fotoğraf ya da PDF): soruları kırp (ImageMagick/pdftoppm), oku, çöz, rubrik adımlarını yaz,
   her adımı MK'ye eşle (ders + sınıf düzeyine uygun MK'ler: `<Ders>/veri/*_kazanim_esleme.csv`), `uygulama/ice_aktarma/<set>/`
   altına `sorular.json` + soru görselleri olarak koy (biçim: `ice_aktar.py`, örnek `mat6_bolunebilme/`). Sınav bilgisi
   (`"sinav"`) her zaman eklenir. Geçici veritabanıyla `python -m app.ice_aktar` deneyip uyarı olmadığını gör.
   Formüller LaTeX'le yazılır: satır içi `$...$` (kesir `\dfrac{a}{b}`, birim `20\,\text{N}`, ondalık `0{,}4`),
   uygulama KaTeX'le çizer (`frontend/src/Mat.tsx`). Çözüm, doğru cevap, rubrik adımları, şıklar ve öğrenci açıklamaları için
   geçerli. Aktarılmış bir seti düzeltmek serbest: değişen yazılar bankaya kendiliğinden geçer (`metin_guncelle.py`).
   MK ve yanılgı ifadeleri (`<Ders>/veri/*.csv`) LaTeX'e çevrilmez, düz yazı kalır: Excel ve MK haritası da onları kullanır
   (Murat, 2026-10-05).
2. **Öğrenci kâğıdı gelir**: oku, her rubrik adımına biliyor / bilmiyor / olculemedi kararı ve gerekçe, soru başına öğrenciye
   açıklama, sonda genel geri bildirim yaz; `uygulama/ice_aktarma/degerlendirmeler/<set>_<ad>.json` (biçim:
   `degerlendirme_aktar.py`, `soru_seti` + soru `no` + adım sırası). `teslim_id` bilinmiyorsa yazılmaz; bekleyen tek teslim
   kendiliğinden bulunur. Birden çok öğrenci varsa teslim numarası sorulur (değerlendirme sayfasında "Teslim no").
3. **Videolar**: sınavın MK'leri için (önce "bilmiyor" çıkanlar) YouTube'dan konu anlatımı ve benzer soru çözümü
   parçaları; altyazı okunarak başlangıç–bitiş seçilir. Kanallar: Partikül Matematik, Derslike (Murat'ın seçimi).
   `uygulama/ice_aktarma/videolar/*.json` (biçim: `video_aktar.py`). YouTube erişimi yoksa bunu bir kez söyle, gerisine devam et.
4. **Gönder**: commit, sonra doğrudan `main`'e push (izin verildi). Murat'ın Mac'inde `EVALORA-Baslat.command` açıkken
   iki dakikada bir `main`'i çeker ve `python -m app.otomatik_aktar` ile yeni setleri, değerlendirmeleri ve videoları
   aktarır. Murat'a yalnız ne geldiğini ve uygulamada nereye bakacağını söyle.

## Gizlilik

GitHub'a öğrenci adı, e-postası ya da el yazısı görüntüsü konmaz; değerlendirmede yalnız okunan metin ve kararlar olur.
`.env` (Azure/Anthropic anahtarları) ve `uygulama/backend/veri/` asla commit edilmez.

## Kontrol

Değişiklikten sonra `cd uygulama/backend && python -m pytest -q`. Testler gerçek veritabanına dokunmaz; elle denemelerde
`DATABASE_URL` geçici bir SQLite dosyasına verilir ve oluşan `uygulama/backend/veri/` silinir.
