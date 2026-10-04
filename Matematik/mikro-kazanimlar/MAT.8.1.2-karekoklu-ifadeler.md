# Mikro Kazanım Ayrıştırması: MAT.8.1.2 (taslak v0.1)

> **MAT.8.1.2** Karşılaştığı problem durumlarında kareköklü ifadeler ile ilgili muhakeme yapabilme
> a) Karenin alanı ve kenar uzunluğu ilişkisini belirler
> b) Tam kare pozitif tam sayıları kareköklerle ilişkilendirir
> c) Tam kare olmayan sayıların karekökleri için matematiksel temsiller kullanır
> ç) Sayının karekökünü kendi ifadeleriyle açıklar
>
> Kaynak: https://tymm.meb.gov.tr/ortaokul-matematik-dersi/unite/472
> Sınıf teması: Mat08-T1 (Sayılar ve Nicelikler) · Ana tema: 01 Sayılar ve Nicelikler
> Sınırlama (TYMM): Kareköklü ifadeyi a√b biçiminde yazma ve katsayıyı kök içine alma çalışmalarına değinilmez.
> Ön öğrenmeler: rasyonel sayıları ve basamak değerlerini yorumlama, rasyonel sayılarla dört işlem, doğal sayının karesini ve küpünü ifade etme (TYMM temel kabulü).

Yöntem: fizikle aynı 8 adım (`Fizik/mikro-kazanimlar/FIZ.10.3.4-esdeger-direnc.md`); kodlama ve Bilgi/Beceri ölçütü: EVALORA kökündeki `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Mat01YG0032 | Bir sayının karekökü o sayının yarısıdır (√16 = 8). |
| Mat01YG0033 | Karekökler toplanırken kök içleri toplanır (√9 + √16 = √25). |
| Mat01YG0034 | Bir sayının karekökü hem pozitif hem negatif değerdir (√16 = ±4). |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Mat01MK0210 | Alanı verilen karenin kenar uzunluğunu bulur. | Beceri | a | Uygulama | Mat01MK0044 | – | ÇS |
| Mat01MK0211 | Kenar uzunluğu verilen karenin alanını bulur. | Beceri | a | Uygulama | Mat01MK0044 | – | ÇS |
| Mat01MK0212 | Tam kare pozitif tam sayıları belirler. | Bilgi | b | Hatırlama | Mat01MK0211 | – | ÇS |
| Mat01MK0213 | Tam kare sayıların karekökünü karenin kenar uzunluğu ile ilişkilendirerek bulur. | Beceri | b | Uygulama | Mat01MK0210; Mat01MK0212 | Mat01YG0032 | ÇS |
| Mat01MK0214 | Tam kare olmayan bir sayının karekökünün hangi iki ardışık doğal sayı arasında olduğunu belirler. | Beceri | c | Analiz | Mat01MK0213 | – | ÇS |
| Mat01MK0215 | Kareköklerin toplamının kök içlerinin toplamının kareköküne eşit olmadığını örneklerle gösterir. | Bilgi | c | Analiz | Mat01MK0213 | Mat01YG0033 | ÇS |
| Mat01MK0216 | Tam kare olmayan sayıların kareköklerini sayı doğrusu ya da alan modeliyle yaklaşık olarak temsil eder. | Beceri | c | Uygulama | Mat01MK0214 | – | AU |
| Mat01MK0217 | Bir sayının karekökünü, karesi o sayıya eşit olan negatif olmayan sayı olarak kendi ifadeleriyle açıklar. | Bilgi | ç | Anlama | Mat01MK0213 | Mat01YG0034; Mat01YG0032 | AU |

> 2026-10-01: Tek ölçülebilir hedef bölmesi ve yeniden numaralama sonrası tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 7 mikro kazanım (7 yeni, 0 yeniden kullanım); yeni olanlardan 3 Bilgi, 4 Beceri.

---

## 3. Örnek ölçme maddeleri

**Mat01MK0214:** √50 hangi iki ardışık doğal sayı arasındadır?  
A) 25 ile 26 (Mat01YG0032) · B) 7 ile 8 ✔ · C) 6 ile 7 · D) 49 ile 51

**Mat01MK0215:** √9 + √16 işleminin sonucu kaçtır?  
A) 5 (Mat01YG0033) · B) 7 ✔ · C) 25 · D) 12,5

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
