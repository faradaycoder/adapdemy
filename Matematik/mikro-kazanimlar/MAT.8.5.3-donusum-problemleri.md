# Mikro Kazanım Ayrıştırması: MAT.8.5.3 (taslak v0.1)

> **MAT.8.5.3** Öteleme ve yansıma dönüşümlerini içeren problemleri çözebilme
> a) Problemlerde ilgili matematiksel bileşenleri belirler
> b) Matematiksel bileşenler arasındaki ilişkileri belirler
> c) Problem bağlamındaki temsilleri farklı temsillere dönüştürür
> ç) Matematiksel temsillere dönüştürdüğü problemi açıklar
> d) Sonuca ilişkin tahminde bulunur ve stratejiler geliştirir
> e) Belirlenen stratejileri uygular
> f) Çözüm yollarını kontrol eder ve stratejiyi değiştirir
> g) Stratejileri gözden geçirerek kısa yolları değerlendirir
> ğ) Stratejileri farklı problemlerin çözümlerine geneller
> h) Genellemenin geçerliliğini matematiksel örneklerle değerlendirir
>
> Kaynak: https://tymm.meb.gov.tr/ortaokul-matematik-dersi/unite/476
> Sınıf teması: Mat08-T5 (Dönüşüm) · Ana tema: 05 Dönüşüm
> Sınırlama (TYMM): TYMM bu çıktı için sınırlama belirtmemiştir.
> Ön öğrenmeler: dik koordinat sisteminde noktanın yerini belirleme, yansıma dönüşümüne ilişkin çıkarım, şekil ile yansıma görüntüsü verildiğinde simetri doğrusunu oluşturma (TYMM temel kabulü).

Yöntem: fizikle aynı 8 adım (`Fizik/mikro-kazanimlar/FIZ.10.3.4-esdeger-direnc.md`); kodlama ve Bilgi/Beceri ölçütü: EVALORA kökündeki `KODLAMA.md`.

Tasarım notu: Problem çözme süreç bileşenleri (a–h) her biri ayrı mikro kazanım olarak yazıldı; içerik (öteleme, yansıma) koda ana tema üzerinden bağlandığı için üçgen problemlerindeki problem çözme mikro kazanımlarından ayrıdır.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Mat05YG0006 | x eksenine göre yansımada apsis, y eksenine göre yansımada ordinat işaret değiştirir. |
| Mat05YG0005 | Sağa ya da sola ötelemede ordinat, yukarı ya da aşağı ötelemede apsis değişir. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Mat05MK0037 | Öteleme problemindeki şekli, koordinatları ve dönüşümü belirleyerek problemi koordinat sisteminde çizimle ya da koordinat kuralıyla temsil eder. | Beceri | a, b, c, ç | Uygulama | Mat05MK0026; Mat05MK0031; Mat05MK0032 | – | AU |
| Mat05MK0038 | Yansıma problemindeki şekli, koordinatları ve dönüşümü belirleyerek problemi koordinat sisteminde çizimle ya da koordinat kuralıyla temsil eder. | Beceri | a, b, c, ç | Uygulama | Mat05MK0027; Mat05MK0028; Mat05MK0033; Mat05MK0034 | – | AU |
| Mat05MK0039 | Öteleme içeren dönüşüm problemlerinin sonucunu tahmin edip strateji geliştirerek çözer. | Beceri | d, e | Uygulama | Mat05MK0037 | Mat05YG0006; Mat05YG0005 | ÇS, AU |
| Mat05MK0040 | Yansıma içeren dönüşüm problemlerinin sonucunu tahmin edip strateji geliştirerek çözer. | Beceri | d, e | Uygulama | Mat05MK0038 | Mat05YG0006; Mat05YG0005 | ÇS, AU |
| Mat05MK0041 | Öteleme içeren dönüşüm probleminin çözümünü kontrol eder, gerekirse stratejisini değiştirir ve kısa yolları değerlendirir. | Beceri | f, g | Değerlendirme | Mat05MK0039 | – | AU |
| Mat05MK0042 | Yansıma içeren dönüşüm probleminin çözümünü kontrol eder, gerekirse stratejisini değiştirir ve kısa yolları değerlendirir. | Beceri | f, g | Değerlendirme | Mat05MK0040 | – | AU |
| Mat05MK0043 | Öteleme içeren dönüşüm problemlerinde kullandığı stratejiyi farklı problemlere genelleştirir ve genellemenin geçerliliğini yeni örneklerle değerlendirir. | Beceri | ğ, h | Analiz | Mat05MK0041 | – | AU |
| Mat05MK0044 | Yansıma içeren dönüşüm problemlerinde kullandığı stratejiyi farklı problemlere genelleştirir ve genellemenin geçerliliğini yeni örneklerle değerlendirir. | Beceri | ğ, h | Analiz | Mat05MK0042 | – | AU |

> 2026-10-01: Tek ölçülebilir hedef bölmesi ve yeniden numaralama sonrası tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 10 mikro kazanım (10 yeni, 0 yeniden kullanım); yeni olanlardan 0 Bilgi, 10 Beceri.

---

## 3. Örnek ölçme maddeleri

**Mat05MK0039:** K(2, 3) noktası önce 4 birim sola ötelenip sonra y eksenine göre yansıtılıyor. Son görüntünün koordinatları nedir?  
A) (2, 3) ✔ · B) (−2, 3) · C) (2, −3) · D) (6, 3)

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.

---

## Güncelleme (2026-10-01): problem çözme süreci 4 mikro kazanıma indirildi

Diğer sınıflarla aynı yapı: temsile dönüştürme, strateji geliştirip çözme, kontrol ve alternatif yollar, genelleme. Yukarıdaki tablo eski hâlidir; geçerli olanlar aşağıdadır. Kodlar silinmedi: birleştirilen kodların durumu "iptal" (haritaya ve zorluk hesabına girmez).

| Kod | Mikro kazanım (Öğrenci...) | İşlem türü | Ön koşul |
|---|---|---|---|
| Mat05MK0037 | Öteleme problemindeki şekli, koordinatları ve dönüşümü belirleyerek problemi koordinat sisteminde çizimle ya da koordinat kuralıyla temsil eder. | Dönüştürme | Mat05MK0026; Mat05MK0031; Mat05MK0032 |
| Mat05MK0039 | Öteleme içeren dönüşüm problemlerinin sonucunu tahmin edip strateji geliştirerek çözer. | Transfer ve problem çözme | Mat05MK0037 |
| Mat05MK0041 | Öteleme içeren dönüşüm probleminin çözümünü kontrol eder, gerekirse stratejisini değiştirir ve kısa yolları değerlendirir. | Sınama ve değerlendirme | Mat05MK0039 |
| Mat05MK0043 | Öteleme içeren dönüşüm problemlerinde kullandığı stratejiyi farklı problemlere genelleştirir ve genellemenin geçerliliğini yeni örneklerle değerlendirir. | Çıkarım ve ilişkilendirme | Mat05MK0041 |

İptal edilenler: [iptal: eski Mat05MK0012] → Mat05MK0037, [iptal: eski Mat05MK0013] → Mat05MK0037, [iptal: eski Mat05MK0015] → Mat05MK0037, [iptal: eski Mat05MK0016] → Mat05MK0039, [iptal: eski Mat05MK0019] → Mat05MK0041, [iptal: eski Mat05MK0021] → Mat05MK0043
