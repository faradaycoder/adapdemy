# Mikro Kazanım Ayrıştırması: MAT.8.3.6 (taslak v0.1)

> **MAT.8.3.6** Üçgende açı-kenar ilişkisi, üçgen eşitsizliği ve Pisagor bağıntısını içeren problemleri çözebilme
> a) İlgili matematiksel bileşenleri (açıların ölçüsü, kenarların uzunluğu, şekil gibi) belirler
> b) Matematiksel bileşenler arasındaki ilişkileri belirler
> c) Problem bağlamındaki temsilleri farklı temsillere dönüştürür
> ç) Matematiksel temsillere dönüştürdüğü problemi kendi ifadeleri ile açıklar
> d) Problemin çözümünü gerçekleştirmek için stratejiler geliştirir
> e) Belirlenen stratejileri çözüm için uygular
> f) Çözüm yollarını kontrol eder ve çözüme ulaştırmayan stratejiyi değiştirir
> g) Kullandığı stratejileri gözden geçirerek kısa yolları değerlendirir
> ğ) Kullandığı strateji veya stratejileri farklı problemlerin çözümlerine geneller
> h) Genellemenin geçerliliğini matematiksel örneklerle değerlendirir
>
> Kaynak: https://tymm.meb.gov.tr/ortaokul-matematik-dersi/unite/474
> Sınıf teması: Mat08-T3 (Geometrik Şekiller) · Ana tema: 03 Geometrik Şekiller
> Sınırlama (TYMM): TYMM bu çıktı için sınırlama belirtmemiştir.
> Ön öğrenmeler: üç doğrunun ikişerli kesişimiyle üçgen oluşturma, matematiksel araçları (cetvel, pergel, gönye, açıölçer) kullanma, kesişen iki çemberle üçgen inşa etme, üçgenin yardımcı elemanlarını belirleme (TYMM temel kabulü).

Yöntem: fizikle aynı 8 adım (`Fizik/mikro-kazanimlar/FIZ.10.3.4-esdeger-direnc.md`); kodlama ve Bilgi/Beceri ölçütü: EVALORA kökündeki `KODLAMA.md`.

Tasarım notu: Problem çözme süreç bileşenleri (a–h) her biri ayrı mikro kazanım olarak yazıldı; içerik (açı-kenar, üçgen eşitsizliği, Pisagor) koda ana tema üzerinden bağlandığı için dönüşüm temasındaki problem çözme mikro kazanımlarından ayrıdır.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Mat03YG0016 | İki kenarın toplamı üçüncü kenara eşit olduğunda da üçgen oluşur. |
| Mat03YG0023 | Dik üçgende kenarlar arasındaki ilişki a + b = c'dir (kareler alınmaz). |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Mat03MK0147 | Açı-kenar ilişkisi içeren üçgen problemlerinde bileşenleri ve aralarındaki ilişkileri belirleyerek problemi şekil ya da denklemle temsil eder ve kendi ifadeleriyle açıklar. | Beceri | a, b, c, ç | Uygulama | Mat03MK0105; Mat03MK0106; Mat03MK0110 | – | AU |
| Mat03MK0148 | Üçgen eşitsizliği içeren üçgen problemlerinde bileşenleri ve aralarındaki ilişkileri belirleyerek problemi şekil ya da denklemle temsil eder ve kendi ifadeleriyle açıklar. | Beceri | a, b, c, ç | Uygulama | Mat03MK0116; Mat03MK0117 | – | AU |
| Mat03MK0149 | Pisagor bağıntısı içeren üçgen problemlerinde bileşenleri ve aralarındaki ilişkileri belirleyerek problemi şekil ya da denklemle temsil eder ve kendi ifadeleriyle açıklar. | Beceri | a, b, c, ç | Uygulama | Mat03MK0144; Mat03MK0145; Mat03MK0146 | – | AU |
| Mat03MK0150 | Açı-kenar ilişkisi içeren üçgen problemleri için strateji geliştirip uygulayarak problemi çözer. | Beceri | d, e | Uygulama | Mat03MK0111; Mat03MK0112; Mat03MK0147 | Mat03YG0016; Mat03YG0023 | ÇS, AU |
| Mat03MK0151 | Üçgen eşitsizliği içeren üçgen problemleri için strateji geliştirip uygulayarak problemi çözer. | Beceri | d, e | Uygulama | Mat03MK0118; Mat03MK0148 | Mat03YG0016; Mat03YG0023 | ÇS, AU |
| Mat03MK0152 | Pisagor bağıntısı içeren üçgen problemleri için strateji geliştirip uygulayarak problemi çözer. | Beceri | d, e | Uygulama | Mat03MK0143; Mat03MK0149 | Mat03YG0016; Mat03YG0023 | ÇS, AU |
| Mat03MK0153 | Açı-kenar ilişkisi içeren üçgen probleminin çözümünü kontrol eder, gerekirse stratejisini değiştirir ve kısa yolları değerlendirir. | Beceri | f, g | Değerlendirme | Mat03MK0150 | – | AU |
| Mat03MK0154 | Üçgen eşitsizliği içeren üçgen probleminin çözümünü kontrol eder, gerekirse stratejisini değiştirir ve kısa yolları değerlendirir. | Beceri | f, g | Değerlendirme | Mat03MK0151 | – | AU |
| Mat03MK0155 | Pisagor bağıntısı içeren üçgen probleminin çözümünü kontrol eder, gerekirse stratejisini değiştirir ve kısa yolları değerlendirir. | Beceri | f, g | Değerlendirme | Mat03MK0152; Mat03MK0140 | – | AU |
| Mat03MK0156 | Açı-kenar ilişkisi içeren üçgen problemlerinde kullandığı stratejiyi farklı problemlere genelleştirir ve genellemenin geçerliliğini yeni örneklerle değerlendirir. | Beceri | ğ, h | Analiz | Mat03MK0153 | – | AU |
| Mat03MK0157 | Üçgen eşitsizliği içeren üçgen problemlerinde kullandığı stratejiyi farklı problemlere genelleştirir ve genellemenin geçerliliğini yeni örneklerle değerlendirir. | Beceri | ğ, h | Analiz | Mat03MK0154 | – | AU |
| Mat03MK0158 | Pisagor bağıntısı içeren üçgen problemlerinde kullandığı stratejiyi farklı problemlere genelleştirir ve genellemenin geçerliliğini yeni örneklerle değerlendirir. | Beceri | ğ, h | Analiz | Mat03MK0155 | – | AU |

> 2026-10-01: Tek ölçülebilir hedef bölmesi ve yeniden numaralama sonrası tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 10 mikro kazanım (10 yeni, 0 yeniden kullanım); yeni olanlardan 0 Bilgi, 10 Beceri.

---

## 3. Örnek ölçme maddeleri

**Mat03MK0150:** 12 m uzunluğundaki merdiven duvara yaslanıyor; merdivenin ayağı duvardan 5 m uzakta. Merdiven duvara kaç m yükseklikte değer? (Beklenen: √119 ≈ 10,9 m; 12 − 5 = 7 yanıtı Mat03YG0023 yanılgısını gösterir.)

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.

---

## Güncelleme (2026-10-01): problem çözme süreci 4 mikro kazanıma indirildi

Diğer sınıflarla aynı yapı: temsile dönüştürme, strateji geliştirip çözme, kontrol ve alternatif yollar, genelleme. Yukarıdaki tablo eski hâlidir; geçerli olanlar aşağıdadır. Kodlar silinmedi: birleştirilen kodların durumu "iptal" (haritaya ve zorluk hesabına girmez).

| Kod | Mikro kazanım (Öğrenci...) | İşlem türü | Ön koşul |
|---|---|---|---|
| Mat03MK0147 | Açı-kenar ilişkisi içeren üçgen problemlerinde bileşenleri ve aralarındaki ilişkileri belirleyerek problemi şekil ya da denklemle temsil eder ve kendi ifadeleriyle açıklar. | Dönüştürme | Mat03MK0105; Mat03MK0106; Mat03MK0110 |
| Mat03MK0150 | Açı-kenar ilişkisi içeren üçgen problemleri için strateji geliştirip uygulayarak problemi çözer. | Transfer ve problem çözme | Mat03MK0111; Mat03MK0112; Mat03MK0147 |
| Mat03MK0153 | Açı-kenar ilişkisi içeren üçgen probleminin çözümünü kontrol eder, gerekirse stratejisini değiştirir ve kısa yolları değerlendirir. | Sınama ve değerlendirme | Mat03MK0150 |
| Mat03MK0156 | Açı-kenar ilişkisi içeren üçgen problemlerinde kullandığı stratejiyi farklı problemlere genelleştirir ve genellemenin geçerliliğini yeni örneklerle değerlendirir. | Çıkarım ve ilişkilendirme | Mat03MK0153 |

İptal edilenler: [iptal: eski Mat03MK0035] → Mat03MK0147, [iptal: eski Mat03MK0036] → Mat03MK0147, [iptal: eski Mat03MK0038] → Mat03MK0147, [iptal: eski Mat03MK0039] → Mat03MK0150, [iptal: eski Mat03MK0042] → Mat03MK0153, [iptal: eski Mat03MK0044] → Mat03MK0156
