# EVALORA Uyarlamalı Test

7 Ekim 2026 · Murat

> Bu dosya, [Claude Docs belgesinin](https://claude.ai/code/artifact/e8207c51-2a15-4de0-8260-39521778b1e6) kopyasıdır. Akış şeması ve çizimli anlatım: `UYARLAMALI_TEST_AKIS.html` (çift tıklayınca tarayıcıda açılır).

## Amaç ve kapsam

Uyarlamalı test, bir kazanımda öğrencinin eksiğinin **kökünü** en az soruyla bulur: her soru, önceki cevaplara göre seçilir. Yanlışta ön koşula iner, doğruda yukarı çıkar; sonunda kök mikro kazanımın (MK) telafi videoları gelir.

- **İlk kapsam:** 6. sınıf bölünebilme kazanımı (MAT.6.1.2): kazanımın 19 MK'si + ön koşulu Mat01MK0047 (katlarını yazar) = 20 MK.
- **Havuz:** 80 soru (her MK için 4 kısa, tek MK'li, 4 şıklı test sorusu).
- **Kullanım (öneri):** sınıf sınavından sonra "eksiğini bul" testi; sınavın "belirsiz" ya da "ölçülemedi" bıraktığı MK'leri tamamlar.
- **Durum:** EVALORA'ya entegre, 7 Ekim 2026'da `main`'e gönderildi. Yöntem kaynağı: ALGORITMA.md bölüm 6.2–6.3.

## Kuramsal dayanak

EVALORA'nın testi, dünyada yerleşik iki yaklaşımın birleşimidir: Bilgi Uzayı Kuramı'nın ön koşul yapısı ve bilgi izlemenin olasılık güncellemesi. Klasik uyarlamalı testten farkı, tek bir yetenek puanı değil, MK MK "biliyor / bilmiyor" kararı vermesidir. Bu bölüm genel bilgiyle yazıldı; örnek sistemlerin bugünkü ayrıntıları yeniden araştırılmadı.

| Yaklaşım | Ne ölçer | Örnek | EVALORA'da karşılığı |
| --- | --- | --- | --- |
| Klasik uyarlamalı test (IRT) | Tek yetenek puanı | GRE, GMAT, NWEA MAP | Kullanılmıyor; ileride zorluk kalibrasyonu için Rasch |
| Bilgi Uzayı Kuramı (Doignon ve Falmagne) | Bilinenler kümesi, ön koşul yapısı | ALEKS | MK ön koşul haritası ve çıkarım kuralı |
| Bayesçi bilgi izleme (Corbett ve Anderson, 1995) | Her beceri için "biliyor" olasılığı | Carnegie Learning öğretmen sistemleri | MK başına P, tahmin (g) ve dikkatsizlik (s) payları |
| DINA modeli (bilişsel tanı) | Soru–beceri eşlemesiyle beceri durumu | Araştırmada CD-CAT | Çok MK'li soruda yanlışın suçunu paylaştırma |

Durum: kuramsal olarak sağlam, ampirik olarak henüz sınanmadı (bkz. Geçerlilik).

## Kullanılan veri

Test yeni veri istemez; EVALORA'da zaten olanları kullanır. Tek yeni parça soru havuzudur.

| Veri | Nereden | Testteki görevi |
| --- | --- | --- |
| MK ↔ kazanım eşlemesi | `Matematik/veri/matematik_kazanim_esleme.csv` | Kazanımın MK'lerini verir |
| Ön koşul haritası | `matematik_mikro_kazanimlar.csv` (on\_kosul\_kodlari) | Yanlışta inilecek, doğruda çıkarılacak MK'leri verir |
| Yanılgılar | `matematik_yanilgilar.csv` | Çeldiricileri hataya bağlar |
| Önceki sınavlar | Onaylı teslimlerdeki rubrik kararları | Öğrencinin başlangıç olasılıkları |
| Videolar | `ice_aktarma/videolar/` | Kök MK'nin telafisi |
| Soru havuzu | `ice_aktarma/mat6_bolunebilme_havuz/` (yeni) | Her MK için sorulacak sorular |

**Kapsam kuralı:** kazanımın MK'leri + bunların ön koşul zinciri, ama yalnız aynı sınıf düzeyinde (alt sınıfa inilmez). MAT.6.1.2 için zincir 5. sınıfa kadar 25 MK'ye uzanır; 6. sınıfta kalan 20 MK teste girer.

**Havuz kuralı:** bir soru, ancak tek bir MK'yi ölçüyorsa (sorunun MK'si ve rubrik adımı aynı MK), onaylıysa ve çoktan seçmeliyse havuza girer. Öğrenci, sınıflarının öğretmenlerinin havuzundan soru alır.

## Algoritma: olasılık, güncelleme ve çıkarım

Her MK için "biliyor" olasılığı P tutulur; her cevaptan sonra Bayes kuralıyla güncellenir ve kararlar ön koşul haritası boyunca yayılır.

1. **Başlangıç:** öğrencinin onaylı sınavlarından gelen P; kanıt yoksa P = 0,5. Öğretmen denemesinde hep 0,5.
2. **Parametreler:** dikkatsizlik s = 0,10 (bilen yanlış yapar); tahmin g = 1 / şık sayısı (4 şıkta 0,25).
3. **Güncelleme (DINA):** doğru cevap için sorunun bütün MK'leri gerekir. P(doğru | hepsi biliniyor) = 1 − s; P(doğru | en az biri bilinmiyor) = g. Her MK'nin yeni olasılığı, MK'lerin birlikte olasılığından hesaplanır.
4. **Tek MK'li soruda** (havuzdaki bütün sorular) bu, Bayesçi bilgi izlemenin kendisidir:

```latex
P_{\text{doğru}} \leftarrow \frac{P(1-s)}{P(1-s) + (1-P)\,g} \qquad P_{\text{yanlış}} \leftarrow \frac{P\,s}{P\,s + (1-P)(1-g)}
```

5. **Çok MK'li soruda** yanlışın suçu paylaştırılır: üç MK de %50 iken bir yanlış, her birini %44'e indirir (karar yok); bilinen MK (%95) suç almıyor, suç bilinmeyene kayıyor. Seçilen şık bir yanılgıya bağlıysa yanılgı raporlanır.
6. **Durum eşikleri** (yuvarlanmış P): %95 ve üstü biliyor; %5 ve altı bilmiyor; arası belirsiz. İki yönde aynı güven (%95) standart değerdir; 4 şıkta bilmiyor için 2 yanlış gerekir (Murat, 7 Ekim 2026). Sınav değerlendirmesindeki %20 eşiği burada kullanılmaz.
7. **Çıkarım (Bilgi Uzayı Kuramı):** "biliyor" kararı verilen MK'nin bütün ön koşulları da biliniyor sayılır; "bilmiyor" kararı verilen MK'ye dayanan MK'ler de bilinmiyor sayılır. Bunlara soru sorulmaz, raporda "çıkarım" diye geçer.

| Durum (4 şık, g = 0,25) | Olasılık yolu | Karar |
| --- | --- | --- |
| 3 doğru | %50 → %78 → %93 → %98 | biliyor |
| 1 yanlış | %50 → %12 | belirsiz, bir soru daha |
| 2 yanlış | %50 → %12 → %2 | bilmiyor |
| 1 doğru, 1 yanlış | %50 → %78 → %32 | belirsiz, soru devam |

## Soru seçimi, durma ve eksiğin kökü

Test tepeden başlar: öğrenci en üstteki MK'yi biliyorsa altındaki zincir çıkarımla kapanır; bilmiyorsa ön koşullara inilir.

*(Akış şeması: `UYARLAMALI_TEST_AKIS.html`)*

Her cevaptan sonra döngü başa döner; aday MK kalmadığında ya da 15 soru dolduğunda kök raporlanır.

Aday MK = kararı verilmemiş (çıkarım dahil), havuzda sorulmamış sorusu olan ve 4 soru sınırına gelmemiş MK. Adaylar arasından sırayla:

1. **Yarım kalan MK:** soru sorulmaya başlanmış ama kararı çıkmamış MK (önce en son sorulan).
2. **Kök arama:** "bilmiyor" kararı verilen bir MK'nin kararsız ön koşulu; önce zinciri en uzun olan.
3. **Zincirin tepesi:** kapsam içinde en çok ön koşulu olan MK; eşitse olasılığı %50'ye en yakın olan.

Soru, o MK'nin havuzdaki henüz sorulmamış ilk sorusudur. Test sırasında doğru/yanlış gösterilmez.

**Durma:** aday kalmadıysa ya da 15 soru soruldu ise. Karara ulaşamayan MK "belirsiz" olarak raporlanır.

**Eksiğin kökü:** doğrudan "bilmiyor" kararı verilen ve ön koşullarından hiçbiri bilinmiyor olmayan MK. Telafi videoları bu MK'ye gelir; üstteki belirtilere değil.

| Sınır | Değer | Neden |
| --- | --- | --- |
| MK başına soru | 4 | 3 doğru "biliyor" için yeter; bir yanlışa tolerans |
| Test başına soru | 15 | Bir ders saatinin bir bölümü; 20 MK'nin çoğu çıkarımla kapanır |
| Havuz | MK başına 4 soru | MK başına sınırla eş |

## Soru havuzu nasıl hazırlandı

80 soru altı adımda yazıldı ve doğrulandı; hepsi öğretmen onayıyla kullanıma girer.

1. **Kapsamı çıkarmak:** MAT.6.1.2'nin 19 MK'si ve ön koşul zinciri CSV'lerden okundu; 6. sınıfta kalan 20 MK alındı. Her MK'nin ifadesi, türü (Bilgi/Beceri), işlem türü ve yanılgıları listelendi.
2. **Soru biçimini seçmek:** her soru tek MK'yi ölçer (rubrikte tek adım, o MK); 4 şıklı test (LGS gibi), çünkü test sırasında anında puanlanmalı. MK başına 4 soru.
3. **MK türüne göre yazmak:**
   - Genelleme MK'leri (0054–0057): kuralın neden öyle olduğunu sorar (ör. "neden yalnız birler basamağına bakılır?").
   - Sınama MK'leri (0058–0061): bir iddiayı destekleyen ya da çürüten örneği buldurur.
   - Kural uygulama MK'leri (0062–0068): "hangisi tam bölünür / bölünmez", "★ yerine hangisi", bağlamlı bir problem.
   - Kullanışlılık MK'leri (0069–0072): hangi kuralın en kısa yol olduğunu sorar.
   - Ön koşul 0047: katları yazma.
4. **Çeldiricileri hatadan türetmek:** yanlış şıklar gerçek öğrenci hatalarından gelir (ilk basamağa bakmak, rakamlar toplamını 4 kuralında kullanmak, 3'e bölüneni 9'a da bölünür saymak). 13 çeldirici iki kayıtlı yanılgıya bağlandı: Mat01YG0009 (son basamağı 3'e bölünen sayı 3'e bölünür) ve Mat01YG0010 (6'ya bölünmek için 3'e bölünmek yeter).
5. **Betikle doğrulamak:** "hangisi tam bölünür / bölünmez" sorularında yalnız doğru şıkkın koşulu sağladığı bilgisayarla kontrol edildi; çözümlerdeki bölmeler (ör. 9 × 82 = 738) tek tek doğrulandı. Kontrol bir hatayı yakaladı: 2 241'in rakamları toplamı 9 olduğu için o da 9'a bölünüyordu; 4 512 ile değiştirildi.
6. **Şıkları dağıtmak ve aktarmak:** doğru şık A–D'ye eşit dağıldı (her harf 20). Set `sorular.json` olarak aktarıldı; geçici veritabanında 80 soru uyarısız girdi. Sorular bankaya taslak girer; öğretmen onaylayınca havuza katılır.

| MK grubu | MK | Soru |
| --- | --- | --- |
| Ön koşul (katlar) | 0047 | 4 |
| Genelleme | 0054–0057 | 16 |
| Sınama | 0058–0061 | 16 |
| Kural uygulama | 0062–0068 | 28 |
| Kullanışlılık | 0069–0072 | 16 |
| **Toplam** | **20 MK** | **80** |

## Örnek iz: kök 9. soruda kesinleşiyor

Uygulamadaki motorla çalıştırılan bir deneme: örnek öğrenci 3 ile bölünebilmeyi (0065) ve ona dayanan MK'leri bilmiyor, gerisini biliyor. "Bilmiyor" için iki yanlış gerektiğinden test kökü 9. soruda kesinleştirdi, kalan sorularla diğer dalları yokladı ve 15 soruda durdu.

| # | Sorulan MK | Cevap | Sonuç | Neden bu MK |
| --- | --- | --- | --- | --- |
| 1–2 | 0072 · 6 kuralının kullanışlılığı | Yanlış × 2 | %50 → %12 → %2, bilmiyor | Zincirin tepesi; tek yanlış karar için yetmedi |
| 3–4 | 0068 · 6 ile bölünebilme | Yanlış × 2 | %2, bilmiyor | 0072'nin en uzun zincirli ön koşulu |
| 5–6 | 0065 · 3 ile bölünebilme | Yanlış × 2 | %2, bilmiyor | 0068'in ön koşulu |
| 7–9 | 0059 · 3 ve 9 kuralını sınar | Doğru × 3 | %98, biliyor | 0065'in ön koşulu: kök 0065 |
| 10–12 | 0062 · 2 ile bölünebilme | Doğru × 3 | %98, biliyor | 0068'in diğer ön koşulu |
| 13–15 | 0069 · 2, 5, 10 kullanışlılığı | Doğru × 3 | %98, biliyor | Kalan dalın tepesi; 15 soru doldu |

**Sonuç:** kök eksik Mat01MK0065 (3 ile bölünebilme kuralını rakamlar toplamıyla kullanır); telafi videoları bu MK'ye geldi. 3 MK sorularla biliyor, 6 MK çıkarımla biliyor, 3 MK bilmiyor, 0070 çıkarımla bilmiyor; 7 MK soru hakkı dolduğu için belirsiz kaldı. Öğrenci varsayımsaldır; MK'ler, ön koşullar ve sorular gerçektir. Eşik %20 iken (tek yanlışla bilmiyor) bir deneme 6 soruda bitmişti.

## Uygulamadaki karşılığı

Test EVALORA'nın içinde; öğretmen ve öğrenci kendi menüsünden ulaşır.

| Kim | Nerede | Ne yapar |
| --- | --- | --- |
| Öğretmen | Üst menü › Uyarlamalı test › ▶ Dene | Testi kendisi çözer; sağ panelde her cevaptan sonra 20 MK'nin olasılığını, kararını ve çıkarımını canlı görür |
| Öğretmen | Aynı sayfa › Öğrencilerin testleri | Kim çözdü, kaç soru, eksiğin kökü; testi açıp sonucu inceler |
| Öğrenci | Üst menü › Eksiğini bul › ▶ Başla | Soruları tek tek çözer; test sırasında doğru/yanlış görmez |
| Öğrenci | Sonuç sayfası | "Önce bunları çalış": kök MK ve videoları; bütün MK'lerin durumu; her sorunun çözümü |

**Kod (depoda):**

- `uygulama/backend/app/uyarlamali.py`: motor (kapsam, havuz, DINA güncellemesi, çıkarım, soru seçimi, kök).
- `uygulama/backend/app/routers/uyarlamali.py`: uçlar. `GET /api/uyarlamali/kazanimlar`, `POST /api/uyarlamali` (başlat), `GET /api/uyarlamali/{id}`, `POST /api/uyarlamali/{id}/cevap`, `GET /api/uyarlamali/oturumlar`.
- `uygulama/backend/app/modeller.py`: `UyarlamaliOturum` ve `UyarlamaliCevap` tabloları. Durum saklanmaz; her istekte cevaplar yeniden oynatılır.
- `uygulama/frontend/src/sayfalar/Uyarlamali.tsx` ve `UyarlamaliTest.tsx`: ekranlar.
- `uygulama/ice_aktarma/mat6_bolunebilme_havuz/sorular.json`: 80 soru; Mac'teki otomatik aktarma bankaya taslak olarak alır.
- `uygulama/backend/tests/test_uyarlamali.py`: DINA sayıları (%81,8; %44), öğretmen denemesinde kökün bulunması, öğrencinin sonucu yalnız sonda görmesi, yetki. Bütün testler (46) geçiyor.

**Kullanmadan önce:** Soru bankası › Tüm taslakları seç › Seçilenleri onayla. Havuzda yalnız onaylı sorular kullanılır.

## Geçerlilik ve sonraki adımlar

Yöntem literatüre dayanıyor ama dört varsayımı henüz veriyle sınanmadı; sıra: simülasyon, pilot, kalibrasyon.

| Varsayım | Bugün | Nasıl sınanır |
| --- | --- | --- |
| Parametreler (s = 0,10; g = 1/şık; başlangıç 0,5) | Tahmin | Pilot cevaplarıyla bilgi izleme / DINA parametre kestirimi |
| Ön koşul haritası doğru | Uzman yargısı | Cevap örüntüleri ön koşul ilişkisine uyuyor mu (Bilgi Uzayı Kuramı yöntemleri) |
| Soru gerçekten o MK'yi ölçer | Yazar + betik kontrolü | Öğretmen incelemesi; veri birikince soru–MK eşlemesinin istatistik kontrolü |
| Sınıflandırma doğru | Bir örnek iz | Simülasyon: durumu bilinen sanal öğrencilerle doğruluk ve soru sayısı |

**Bilinen sınırlar:**

- Havuz yalnız MAT.6.1.2 için var; başka kazanım için MK başına 4 soru yazılmalı.
- Uyarlamalı test sonuçları henüz "Konu raporum" ve sınıf raporuna eklenmiyor.
- 4 şıkta "biliyor" için 3 doğru gerekiyor; 15 soruda 20 MK'nin bir kısmı "belirsiz" kalabiliyor.
- Zorluğa (Z) göre başlangıç olasılığı ayarı henüz uygulanmadı; bütün MK'ler kanıt yoksa 0,5'ten başlıyor.

**Sonraki adımlar:**

- [ ] Simülasyon: 1 000 sanal öğrenciyle doğruluk ve ortalama soru sayısı
- [ ] Pilot: aynı öğrencilere uyarlamalı test + yazılı sınav, sonuçları karşılaştırmak
- [ ] Uyarlamalı test kanıtını Konu raporum ve sınıf raporuna eklemek
- [ ] Yeni kazanımlar için havuz (sıra öğretmenin seçimi)
- [ ] Pilot verisiyle s, g ve Z kalibrasyonu (Elo, sonra Rasch)

## Kararı bekleyen konular

Aşağıdakiler pedagojik tercihler; şimdilik "şu an" sütunundaki değerlerle çalışıyor.

| Konu | Şu an | Seçenek |
| --- | --- | --- |
| "Bilmiyor" çıkarımı | Karar: kalır (Bilgi Uzayı Kuramı standardı). Ön koşulu bilinmeyen MK de "bilmiyor" sayılır; artık ancak iki yanlışla verilen karardan sonra | "Sorulmadı: ön koşulu eksik" diye ayrı gösterilsin; karar ancak soruyla verilsin |
| Alt sınıfa inme | İnilmez (kapsam 6. sınıf) | 5. sınıf ön koşullarına da inilsin |
| Soru sınırları | MK başına 4, test başına 15 | Test başına 20 (20 MK'nin hepsine karar için) |
| Yanlışın suçu (çok MK'li soru) | DINA ile paylaştırılır | Z'ye göre başlangıç olasılığı da düşürülsün |
| Kullanım | Sınavdan sonra "eksiğini bul" | Sınavın yerine |
