# EVALORA Uygulaması: Kapsam ve Plan (taslak v0.1)

*EVALORA: Measure. Diagnose. Remediate. (Ölç. Teşhis et. Telafi et.)*

*Micro-skill based assessment, diagnosis and remediation (Mikro kazanım temelli ölçme, teşhis ve telafi)*

*2026-10-04. Ölçme modelinin kendisi `ALGORITMA.md`'de; bu doküman o modeli kullanan uygulamanın ne yapacağını ve nasıl kurulacağını anlatır. Onaylanınca kodlamaya geçilir.*

## 1. Amaç

Öğretmenin soru hazırlamasından öğrencinin MK MK raporuna kadar bütün sınav sürecini tek yerde yürüten bir web uygulaması. Her adımda MK eşlemesi vardır: soru MK'lere, rubrik adımları MK'lere, öğrencinin her adımdaki cevabı MK durumuna bağlanır. Uygulama kendi küçük LMS'iyle bağımsız çalışır; ileride okulların LMS'ine (Moodle vb.) bağlanabilecek biçimde kurulur.

## 2. Kapsam

### 2.1 İlk sürümde (v1)

| Alan | Ne yapar |
|---|---|
| Hesap ve sınıf | Öğretmen ve öğrenci hesapları; öğretmen sınıf açar, öğrenci sınıf koduyla katılır |
| Soru bankası | Soru yükleme (fotoğraf, PDF, Word, metin), sistemin okuması, çözmesi, rubrik çıkarması, MK eşlemesi ve zorluk hesabı; öğretmen onayı. MK ya da kazanımdan soru üretme |
| Sınav | Konu, kazanım ya da MK'ye göre soru seçme; online sürüm ve sayfalarında QR kod olan yazdırılabilir PDF |
| Atama | Sınavı sınıfa ya da öğrencilere başlangıç ve bitiş zamanıyla atama |
| Öğrenci ekranı | Online çözme (şık, kısa cevap, yazılı cevap) ya da kâğıtta çözüp soru soru ya da sayfa sayfa fotoğraf / tarama yükleme; aynı sınavda karışık |
| Değerlendirme | Sistemin her cevabı rubrik adımlarına göre puanlaması; her adım için biliyor / bilmiyor / ölçülemedi; emin olmadığı adımları işaretlemesi |
| Öğretmen kontrolü | Adım adım görüntüleme, düzeltme, onay; sonucu öğrenciye açma |
| Rapor | Öğrenci MK raporu; sınıf raporu ve MK ısı haritası; yanılgı dağılımı |

### 2.2 Sonraki sürümlerde

- **v2:** Ses kaydıyla cevap ve sesli soru; uyarlamalı test (ALGORITMA.md bölüm 6); eksik MK'den kişisel ödev / telafi sınavı; LTI 1.3 ile LMS bağlantısı.
- **v3:** İçerik önerisi (Faz 3); Rasch kalibrasyonu (veri birikince); yönetici ve veli ekranları; yeni dersler.

### 2.3 Kapsam dışı

Ders içeriği yönetimi, forum, mesajlaşma, takvim. Bunlar okulun LMS'inden gelir.

## 3. Kullanıcılar ve ana akışlar

**Roller:** Öğretmen (sınavı hazırlayan ve değerlendiren kişi), öğrenci. Yönetici v3'te.

**Akış 1, soru bankası:**
1. Öğretmen soruyu yükler (ya da MK seçip "soru üret" der).
2. Sistem soruyu okur, çözer, çözümü adımlara ayırır.
3. Her adımı MK'ye eşler; en üstteki MK'leri sorunun MK'leri yapar, birincil MK'yi işaretler (ALGORITMA.md 5.1).
4. Zorluğu hesaplar: b = Σ Z (5.2); rubrik paylarını çıkarır (5.3).
5. Öğretmen her şeyi görür, düzeltir, onaylar. Soru bankaya girer.

**Akış 2, sınav ve atama:**
1. Öğretmen konu, kazanım ya da MK seçer; sistem bankadan soru önerir (MK kapsamı ve zorluk dağılımıyla).
2. Öğretmen her soru için cevap biçimini seçer (şık, kısa cevap, yazılı, kâğıt).
3. Sistem online sürümü ve QR kodlu PDF'i hazırlar. Öğretmen sınavı atar.

**Akış 3, öğrencinin cevabı:**
1. Öğrenci atanan sınavı açar.
2. Online sorulara ekranda cevap verir; kâğıt sorularını PDF'ten çözüp fotoğraflar ya da tarar. Bir soruyu parça parça, birden çok fotoğrafla yükleyebilir.
3. QR kod sayesinde her sayfa doğru öğrenci, sınav ve soruyla eşleşir.
4. Teslim eder.

**Akış 4, değerlendirme ve rapor:**
1. Sistem cevapları okur ve rubrik adımlarına göre değerlendirir.
2. Öğretmen inceler: sistemin "emin değilim" dediği adımlar önde gösterilir. Düzeltir, onaylar.
3. Sonuç öğrenciye açılır. Öğrencinin MK durumları güncellenir (Bayesçi Bilgi İzleme, 6.2). Sınıf raporu ve ısı haritası güncellenir.

## 4. Ekranlar

**Öğretmen:**
- Ana sayfa: sınıflar, açık sınavlar, değerlendirme bekleyen teslimler.
- Soru bankası: liste ve filtre (ders, sınıf, kazanım, MK, zorluk); soru yükle; soru üret.
- Soru ayrıntısı: soru, çözüm, rubrik tablosu (adım, MK, pay), sorunun MK'leri, zorluk; ön koşul haritasında MK'nin yeri.
- Sınav oluşturma: soru seçme ve sıralama, cevap biçimleri, önizleme, PDF.
- Sınıf: öğrenciler, sınıf kodu, atamalar.
- Değerlendirme: öğrenci öğrenci, soru soru; yüklenen görüntü ile sistemin okuduğu metin yan yana; adım adım puan ve MK durumu; düzeltme.
- Raporlar: öğrenci raporu, sınıf raporu, MK ısı haritası, yanılgılar.

**Öğrenci:**
- Ana sayfa: atanan sınavlar, sonuçlar.
- Sınav çözme: online cevap; soru başına fotoğraf ya da dosya yükleme; telefonda kamera.
- Sonuç ve rapor: puan, soru soru geri bildirim, MK raporu (biliyor, bilmiyor, ölçülemedi).

Bütün ekranlar telefonda çalışır (PWA: ana ekrana eklenir, kamera açılır).

## 5. Mimari (öneri)

| Katman | Öneri | Neden |
|---|---|---|
| Ön yüz | React (Next.js), PWA | Web ve telefon tek kod; kamera ve dosya yükleme tarayıcıda çalışır |
| Arka uç | Python, FastAPI | MK, harita ve zorluk araçlarımız Python'da; doğrudan kullanılır |
| Veritabanı | PostgreSQL | İlişkisel veri (sınıf, sınav, teslim) ve MK haritası aynı yerde |
| Dosya deposu | S3 uyumlu nesne deposu | Fotoğraf, tarama, PDF, ileride ses |
| İş kuyruğu | Arka planda çalışan değerlendirme işleri | Okuma ve değerlendirme saniyeler sürer, kullanıcıyı bekletmez |
| Yapay zekâ | Claude API (görsel model) | Soru ve el yazısını okuma, çözme, rubrik, MK eşleme, değerlendirme; ayrı OCR yok |
| MK verisi | CSV'lerden veritabanına içe aktarma | CSV tek doğruluk kaynağı kalır; harita değişince yeniden aktarılır |

**MK eşlemenin nasıl yapılacağı:** Model 2.430 MK'nin hepsini bir anda görmez. Önce sorunun dersi, sınıfı ve konusu belirlenir; o kazanımlara eşli MK'ler ve ön koşul zincirleri aday olarak verilir; model adayların içinden seçer. Ardından kurallar kodla denetlenir: yalnız en üstteki MK'ler sorunun MK'si olur, rubrik MK'leri sorunun MK'lerinin zincirinde olmalıdır (5.1). Kurala uymayan eşleme öğretmene işaretlenir.

## 6. Veri modeli (ana tablolar)

| Tablo | Temel alanlar |
|---|---|
| kullanici | id, ad, e-posta, rol |
| sinif, sinif_uye | sınıf adı, ders, sınıf düzeyi, kod; öğrenci–sınıf |
| mk, mk_onkosul, mk_esleme, yanilgi | CSV'lerden; kod, ifade, tür, işlem türü, v, Z, seviye; ön koşul bağları; çıktı eşlemeleri |
| soru | metin, görsel, cevap biçimi, doğru cevap, çözüm, zorluk b, kaynak (yüklendi / üretildi), onay durumu |
| soru_mk | soru, MK, birincil mi |
| rubrik_adim | soru, sıra, açıklama, MK, pay |
| secenek | soru, şık, doğru mu, yanılgı kodu |
| sinav, sinav_soru, atama | sınav; sorular ve sıra; sınıf/öğrenci, başlangıç, bitiş |
| teslim, cevap, cevap_dosya | öğrenci ve sınav; soru başına cevap; yüklenen görüntüler |
| degerlendirme_adim | cevap, rubrik adımı, durum (biliyor / bilmiyor / ölçülemedi), puan, güven, kaynak (sistem / öğretmen) |
| ogrenci_mk | öğrenci, MK, P(biliyor), son kanıt tarihi |
| duzeltme | öğretmenin sistem kararını değiştirdiği kayıtlar (sistemi iyileştirmek için) |

## 7. Kişisel veri ve güvenlik

- Öğrencilerin çoğu çocuktur; KVKK kapsamında açık rıza (gerekirse veli onayı), aydınlatma metni, veri saklama süresi ve silme hakkı baştan tasarlanır. Hukuki ayrıntı bir uzmana doğrulatılmalı.
- En az veri: öğrenci için ad ve e-posta (ya da okul numarası) yeter; T.C. kimlik numarası tutulmaz.
- Rol bazlı erişim: öğretmen yalnız kendi sınıflarını, öğrenci yalnız kendi verisini görür.
- Yüklenen görüntüler yalnız değerlendirme için yapay zekâya gönderilir; model sağlayıcısının veri kullanım koşulları kontrol edilir.

## 8. LMS bağlantısına hazırlık

v1'de kendi hesap ve sınıf yapımız kullanılır ama veri modeli LTI 1.3'e uygun kurulur (kullanıcı, kurs/sınıf, atama, not geri gönderimi). Soru alışverişi için QTI, öğrenme verisi için xAPI dışa aktarımı v2'de eklenir.

## 9. İş listesi (v1)

| Aşama | İş | Bitiş ölçütü |
|---|---|---|
| A. Temel | Proje iskeleti, hesaplar, roller, sınıf ve sınıf kodu; MK verisini içe aktarma | Öğretmen sınıf açar, öğrenci katılır; MK'ler ve harita veritabanında |
| B. Soru bankası | Soru yükleme, okuma, çözme, rubrik, MK eşleme, zorluk; öğretmen onay ekranı; soru üretme | Pilot kapsamdaki örnek sorular doğru eşleniyor (öğretmen kontrolüyle) |
| C. Sınav | Sınav oluşturma, önizleme, QR kodlu PDF, atama | Sınav online ve kâğıt olarak öğrenciye ulaşıyor |
| D. Teslim | Online cevap, fotoğraf / tarama yükleme, QR ile sayfa eşleme, teslim | Karışık bir sınav eksiksiz teslim ediliyor |
| E. Değerlendirme | Rubrik değerlendirmesi, güven işareti, öğretmen düzeltme ekranı, MK durumları | Örnek kâğıtlarda sistem ile öğretmen puanı karşılaştırılıyor |
| F. Rapor | Öğrenci raporu, sınıf raporu, ısı haritası, yanılgılar | Rapor MK MK eksikleri gösteriyor |
| G. Pilot | Fizik 10–12 enerji ve hareket, Matematik 8–9 üçgenler ve Pisagor ile gerçek öğretmen ve öğrenciyle deneme | Öğretmen geri bildirimi toplandı |

**Başarı ölçütleri (pilot):** Sistem ile öğretmenin MK eşlemesindeki uyum; rubrik puanındaki ortalama fark; öğretmenin bir kâğıdı değerlendirme süresi (elle değerlendirmeye göre); el yazısı okuma hatası oranı.

## 10. Riskler

| Risk | Önlem |
|---|---|
| El yazısı matematik ve fizik yanlış okunur | Güven puanı; düşük güvenli adımlar öğretmene işaretlenir; öğretmen onayı zorunlu |
| Kâğıttaki çözümün rubrik adımlarına bölünmesi hatalı olur | Pilot kâğıtlarla erken deneme (aşama E'yi B'den hemen sonra küçük ölçekte denemek) |
| Fotoğrafın hangi soruya ait olduğu karışır | QR kod; öğrencinin soru numarasını seçerek yüklemesi |
| Yapay zekâ maliyeti | Değerlendirmeyi kuyrukta toplu yapmak; aynı sorunun çözüm ve rubriğini bir kez üretip saklamak |
| Kişisel veri | Bölüm 7 |

## 11. Kararlar

| Konu | Karar (2026-10-04, Murat) |
|---|---|
| Barındırma | Şimdilik Murat'ın bilgisayarında. Kalıcı yer (bulut ya da Türkiye'de sunucu) sonra verilecek büyük bir karar; uygulama her ikisine de taşınabilecek biçimde kurulur. |
| Giriş | E-posta ve şifre ile Google hesabı. LMS bağlantısında öğrenciler okul numarasıyla gelir. |
| Ses kaydı | v2. |
| Ad | EVALORA (büyük harf). Türkçe açıklama henüz seçilmedi. |
