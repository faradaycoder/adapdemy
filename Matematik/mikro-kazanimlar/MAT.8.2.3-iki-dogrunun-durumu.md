# Mikro Kazanım Ayrıştırması: MAT.8.2.3 (taslak v0.1)

> **MAT.8.2.3** Dik koordinat sisteminde iki doğrusal fonksiyonun birbirine göre durumuna ilişkin çıkarım yapabilme
> a) Varsayım oluşturur
> b) Genellemeler yapar
> c) Varsayımlarını karşılaştırır
> ç) Önermelerde bulunur
> d) Doğruların konumlarını değerlendirir
>
> Kaynak: https://tymm.meb.gov.tr/ortaokul-matematik-dersi/unite/473
> Sınıf teması: Mat08-T2 (Cebirsel Düşünme ve Değişimler) · Ana tema: 02 Cebirsel Düşünme ve Değişimler
> Sınırlama (TYMM): Fonksiyon tanımına girilmeden doğrusal fonksiyonun temsilleri üzerinden çalışılır; fonksiyonlar f(x) = mx + n biçiminde ifade edilir. Çalışmalar matematik yazılımıyla yürütülür.
> Ön öğrenmeler: birinci dereceden denklem ve eşitsizlikler, oranı yorumlama, temel cebirsel işlemler (TYMM temel kabulü).

Yöntem: fizikle aynı 8 adım (`Fizik/mikro-kazanimlar/FIZ.10.3.4-esdeger-direnc.md`); kodlama ve Bilgi/Beceri ölçütü: EVALORA kökündeki `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Mat02YG0018 | Paralel doğruların n değerleri (y eksenini kestikleri noktalar) de eşit olmalıdır. |
| Mat02YG0019 | Eğimleri zıt işaretli olan doğrular birbirine diktir (ör. eğimi 2 ve −2 olanlar). |
| Mat02YG0017 | İki doğrunun kesişim noktası her zaman y ekseni üzerindedir. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Mat02MK0126 | İki doğrusal fonksiyonun eğimlerine bakarak grafiklerinin paralel olacağına dair varsayım oluşturur. | Beceri | a | Analiz | Mat02MK0119 | – | AU |
| Mat02MK0127 | İki doğrusal fonksiyonun eğimlerine bakarak grafiklerinin kesişeceğine dair varsayım oluşturur. | Beceri | a | Analiz | Mat02MK0119 | – | AU |
| Mat02MK0128 | İki doğrusal fonksiyonun eğimlerine bakarak grafiklerinin dik olacağına dair varsayım oluşturur. | Beceri | a | Analiz | Mat02MK0119 | – | AU |
| Mat02MK0129 | İki doğrunun kesişim noktasının her iki fonksiyonu da sağlayan nokta (f(a) = g(a) = b) olduğu genellemesini yapar. | Bilgi | b | Analiz | Mat02MK0116 | Mat02YG0017 | ÇS |
| Mat02MK0130 | Matematik yazılımıyla grafikleri inceleyerek eğimleri eşit doğruların paralel olduğu genellemesini yapar. | Bilgi | b | Analiz | Mat02MK0126 | Mat02YG0018 | ÇS |
| Mat02MK0131 | Birbirine dik doğruların eğimlerinin çarpımının −1 olduğu genellemesini yapar. | Bilgi | b | Analiz | Mat02MK0128 | Mat02YG0019 | ÇS |
| Mat02MK0132 | İki doğrunun paralel olacağına dair varsayımını yazılımla elde ettiği grafiklerle karşılaştırır. | Beceri | c | Değerlendirme | Mat02MK0126; Mat02MK0130 | – | AU, PG |
| Mat02MK0133 | İki doğrunun dik olacağına dair varsayımını yazılımla elde ettiği grafiklerle karşılaştırır. | Beceri | c | Değerlendirme | Mat02MK0128; Mat02MK0131 | – | AU, PG |
| Mat02MK0134 | İki doğrunun kesişen olacağına dair varsayımını yazılımla elde ettiği grafiklerle karşılaştırır. | Beceri | c | Değerlendirme | Mat02MK0127; Mat02MK0130 | – | AU, PG |
| Mat02MK0135 | İki doğrunun paralel olmasına ilişkin önermeyi eğimler ve n değerleri üzerinden ifade eder. | Bilgi | ç | Anlama | Mat02MK0130 | – | AU |
| Mat02MK0136 | İki doğrunun dik olmasına ilişkin önermeyi eğimler üzerinden ifade eder. | Bilgi | ç | Anlama | Mat02MK0131 | – | AU |
| Mat02MK0137 | İki doğrunun kesişim noktasına ilişkin önermeyi ifade eder. | Bilgi | ç | Anlama | Mat02MK0130; Mat02MK0129 | – | AU |
| Mat02MK0138 | Cebirsel ifadeleri verilen iki doğrunun paralel olduğunu grafik çizmeden belirler. | Beceri | d | Uygulama | Mat02MK0135 | Mat02YG0018 | ÇS |
| Mat02MK0139 | Cebirsel ifadeleri verilen iki doğrunun dik olduğunu grafik çizmeden belirler. | Beceri | d | Uygulama | Mat02MK0136 | Mat02YG0019 | ÇS |
| Mat02MK0140 | Cebirsel ifadeleri verilen iki doğrunun kesiştiğini grafik çizmeden belirler. | Beceri | d | Uygulama | Mat02MK0137 | – | ÇS |
| Mat02MK0141 | Cebirsel ifadeleri verilen iki doğrunun çakışık olduğunu grafik çizmeden belirler. | Beceri | d | Uygulama | Mat02MK0135 | – | ÇS |

> 2026-10-01: Tek ölçülebilir hedef bölmesi ve yeniden numaralama sonrası tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 7 mikro kazanım (7 yeni, 0 yeniden kullanım); yeni olanlardan 4 Bilgi, 3 Beceri.

---

## 3. Örnek ölçme maddeleri

**Mat02MK0138:** f(x) = 2x + 1 ve g(x) = 2x − 3 doğruları için hangisi doğrudur?  
A) Çakışıktır (Mat02YG0018) · B) Paraleldir ✔ · C) Diktir · D) Orijinde kesişir

**Mat02MK0131:** Eğimi 2 olan doğruya dik doğrunun eğimi kaçtır?  
A) −2 (Mat02YG0019) · B) 1/2 · C) −1/2 ✔ · D) 2

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
