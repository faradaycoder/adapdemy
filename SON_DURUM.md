# Son durum ve sıradaki işler

Yeni oturum buradan devam eder. En son: 8 Ekim 2026 (Mac oturumu). Her oturum sonunda güncellenir.

## Bu oturumda yapılanlar (özet)

- **Tasarım:** Yeni logo (beyin + Ölç/Teşhis et/Telafi et döngüsü: mavi/turkuaz/mor), soru bankası ve sınav ekranları
  yeniden düzenlendi, soru ekle paneli (sınıf → ders → ünite → kazanım → çoklu MK seçimi).
- **MK haritası** uygulama içinde (`/mk`), kilit düğmesi; kilitliyken tıklanan MK'nin ayrıntısı yan panelde.
- **Süre:** süre dolunca sınav kendiliğinden teslim (açılmadıysa boş kâğıt), öğretmene bildirim; öğrenci süre uzatma
  ister, öğretmen dakika girerek verir ya da reddeder (Teslimler sayfası).
- **Uyarlamalı test** (ayrıntı: `UYARLAMALI_TEST.md`, çizimli akış: `UYARLAMALI_TEST_AKIS.html`):
  6. sınıf bölünebilme (MAT.6.1.2) için 80 soruluk havuz (`uygulama/ice_aktarma/mat6_bolunebilme_havuz`), motor
  `uygulama/backend/app/uyarlamali.py`, öğretmen "Uyarlamalı test › Dene", öğrenci "Eksiğini bul".
- **Demo sunumu** (12 slayt): https://claude.ai/artifact/BYzEkvdm1wa3hEYog4LSUs

## Murat'ın verdiği kararlar (7 Ekim)

- Uyarlamalı testte "bilmiyor" eşiği %5 (iki yanlış), "biliyor" %95; değerler standart olsun.
- Ön koşul çıkarımı iki yönde kalır (Bilgi Uzayı Kuramı).
- Uyarlamalı testi sınıfa atama şimdilik yok; demo öğretmen sayfasından ("Dene") yapılır.
- (8 Ekim) Test başına soru üst sınırı 20 (önce 15); MK başına 4 aynı. Alt sınır konmadı.

## Karar bekleyenler (Murat'a sorulmadan değiştirilmez)

- Uyarlamalı testte bir MK'nin 4 sorusundan biri rastgele mi seçilsin? (Şu an hep ilki; herkes aynı ilk soruyu görür.)
- Alt sınıfa (5. sınıf ön koşulları) inilsin mi?
- Zor MK'nin (Z) başlangıç olasılığı düşürülsün mü?
- Uyarlamalı test sonuçları Konu raporu ve sınıf raporuna eklensin mi?

## Hatırlatmalar

- Havuzdaki 80 soru bankaya **taslak** girer; Soru bankası › Tüm taslakları seç › Onayla, yoksa test görünmez.
- Pedagojik ya da algoritmik bir değeri (eşik, sınır, kural) Murat açıkça "yap" demeden değiştirme; soru sorması onay
  değildir (7 Ekim'de onaysız değişiklik geri alındı).
- Sınav, öğrenci kâğıdı, video döngüsü için CLAUDE.md'deki "Döngü" geçerli.

## Azure (8 Ekim)

- Azure ücretsiz deneme (200 $, 30 gün; ~3 Kasım'da biter), bölge Sweden Central. Document Intelligence (`evalora-ocr`,
  ücretsiz F0) çalışıyor: Soru ekle'de "Azure okuma modu" (metin + kelime benzerliğiyle aday MK).
- GPT (gpt-6.1-sol) için kota 0'dı; talep açıldı. 8 Ekim'de Azure "Free Tier → Tier 1 kota yükseltmesi" e-postası
  gönderdi (3 gün içinde kendiliğinden). Olunca Quota sayfasına bak, modeli `evalora-gpt` adıyla deploy et,
  `.env`'de `AZURE_OPENAI_DEPLOYMENT=evalora-gpt`, backend'i yeniden başlat → "Azure yapay zekâ modu".
- Claude ve diğer Marketplace modelleri krediden düşmez, karttan çekilir: deploy edilmez.
