# Mikro Kazanım Ayrıştırması: MAT.8.1.1 (taslak v0.1)

> **MAT.8.1.1** Farklı bağlamlardaki üslü ifadelere, özelliklerine ve üslü ifadelerle yapılan işlemlere ilişkin çıkarım yapabilme
> a) Varsayımda bulunur
> b) Genellemeler belirler
> c) Varsayımı örnekler ve temsillerle sınar
> ç) Sözel ve cebirsel olarak ifade eder
> d) Matematiksel süreçlere katkısını açıklar
>
> Kaynak: https://tymm.meb.gov.tr/ortaokul-matematik-dersi/unite/472
> Sınıf teması: Mat08-T1 (Sayılar ve Nicelikler) · Ana tema: 01 Sayılar ve Nicelikler
> Sınırlama (TYMM): Üslü ifadeler tabanı rasyonel sayı, kuvveti tam sayı olanlarla sınırlıdır; bilimsel gösterime girilmez.
> Ön öğrenmeler: rasyonel sayıları ve basamak değerlerini yorumlama, rasyonel sayılarla dört işlem, doğal sayının karesini ve küpünü ifade etme (TYMM temel kabulü).

Yöntem: fizikle aynı 8 adım (`Fizik/mikro-kazanimlar/FIZ.10.3.4-esdeger-direnc.md`); kodlama ve Bilgi/Beceri ölçütü: EVALORA kökündeki `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Mat01YG0027 | Üslü ifadede taban ile üs çarpılır (2³ = 6). |
| Mat01YG0028 | (−2)⁴ ile −2⁴ aynı değerdir. |
| Mat01YG0029 | Sıfırıncı kuvvet sıfırdır (5⁰ = 0). |
| Mat01YG0031 | Negatif üs sonucu negatif yapar (2⁻³ = −8). |
| Mat01YG0030 | Aynı tabanlı üslü ifadeler toplanırken üsler toplanır (2³ + 2⁴ = 2⁷). |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Mat01MK0175 | Tekrarlı çarpımı üslü ifade olarak yazar. | Beceri | a | Uygulama | Mat01MK0044; Mat01MK0045 | – | ÇS |
| Mat01MK0176 | Üslü ifadenin değerini hesaplar. | Beceri | a | Uygulama | Mat01MK0044; Mat01MK0045 | Mat01YG0027 | ÇS |
| Mat01MK0177 | Negatif tabanlı üslü ifadelerde üs çift ise sonucun pozitif olduğuna dair varsayımda bulunur. | Beceri | a | Analiz | Mat01MK0176; Mat01MK0134 | Mat01YG0028 | AU |
| Mat01MK0178 | Negatif tabanlı üslü ifadelerde üs tek ise sonucun negatif olduğuna dair varsayımda bulunur. | Beceri | a | Analiz | Mat01MK0176; Mat01MK0134 | – | AU |
| Mat01MK0179 | Azalan kuvvetler örüntüsünden sıfırıncı kuvvetin 1 olduğu genellemesini belirler. | Bilgi | b | Analiz | Mat01MK0176; Mat02MK0059 | Mat01YG0029 | ÇS |
| Mat01MK0180 | Aynı tabanlı üslü ifadelerde çarpma kuralını (aᵐ·aⁿ = aᵐ⁺ⁿ) belirler. | Bilgi | b | Analiz | Mat01MK0175 | Mat01YG0030 | ÇS |
| Mat01MK0181 | Aynı tabanlı üslü ifadelerde bölme kuralını (aᵐ / aⁿ = aᵐ⁻ⁿ) belirler. | Bilgi | b | Analiz | Mat01MK0175 | – | ÇS |
| Mat01MK0182 | Negatif üssün çarpmaya göre tersi anlamına geldiği genellemesini (a⁻ⁿ = 1 / aⁿ) belirler. | Bilgi | b | Analiz | Mat01MK0179 | Mat01YG0031 | ÇS |
| Mat01MK0183 | Üssün üssü kuralını ((aᵐ)ⁿ = aᵐⁿ) belirler. | Bilgi | b | Analiz | Mat01MK0180 | – | ÇS |
| Mat01MK0184 | Çarpımın kuvveti kuralını ((a·b)ⁿ = aⁿ·bⁿ) belirler. | Bilgi | b | Analiz | Mat01MK0180 | – | ÇS |
| Mat01MK0185 | Bölümün kuvveti kuralını ((a / b)ⁿ = aⁿ / bⁿ) belirler. | Bilgi | b | Analiz | Mat01MK0181 | – | ÇS |
| Mat01MK0186 | Negatif tabanlı üslü ifadelerde çift üsle işaret kuralı varsayımını sayısal örnekler ve temsillerle sınar. | Beceri | c | Değerlendirme | Mat01MK0177 | – | AU |
| Mat01MK0187 | Negatif tabanlı üslü ifadelerde tek üsle işaret kuralı varsayımını sayısal örnekler ve temsillerle sınar. | Beceri | c | Değerlendirme | Mat01MK0178 | – | AU |
| Mat01MK0188 | Sıfırıncı kuvvet kuralı varsayımını sayısal örnekler ve temsillerle sınar. | Beceri | c | Değerlendirme | Mat01MK0179 | – | AU |
| Mat01MK0189 | Negatif üs kuralı varsayımını sayısal örnekler ve temsillerle sınar. | Beceri | c | Değerlendirme | Mat01MK0182 | – | AU |
| Mat01MK0190 | Aynı tabanlı üslü ifadelerde çarpma kuralı varsayımını sayısal örnekler ve temsillerle sınar. | Beceri | c | Değerlendirme | Mat01MK0180 | – | AU |
| Mat01MK0191 | Aynı tabanlı üslü ifadelerde bölme kuralı varsayımını sayısal örnekler ve temsillerle sınar. | Beceri | c | Değerlendirme | Mat01MK0181 | – | AU |
| Mat01MK0192 | Üssün üssü kuralı varsayımını sayısal örnekler ve temsillerle sınar. | Beceri | c | Değerlendirme | Mat01MK0183 | – | AU |
| Mat01MK0193 | Çarpımın kuvveti kuralı varsayımını sayısal örnekler ve temsillerle sınar. | Beceri | c | Değerlendirme | Mat01MK0184 | – | AU |
| Mat01MK0194 | Bölümün kuvveti kuralı varsayımını sayısal örnekler ve temsillerle sınar. | Beceri | c | Değerlendirme | Mat01MK0185 | – | AU |
| Mat01MK0195 | Negatif tabanlı üslü ifadelerde çift üsle işaret kuralını sözel ve cebirsel olarak ifade eder. | Bilgi | ç | Anlama | Mat01MK0186 | – | AU |
| Mat01MK0196 | Negatif tabanlı üslü ifadelerde tek üsle işaret kuralını sözel ve cebirsel olarak ifade eder. | Bilgi | ç | Anlama | Mat01MK0187 | – | AU |
| Mat01MK0197 | Sıfırıncı kuvvet kuralını sözel ve cebirsel olarak ifade eder. | Bilgi | ç | Anlama | Mat01MK0188 | – | AU |
| Mat01MK0198 | Negatif üs kuralını sözel ve cebirsel olarak ifade eder. | Bilgi | ç | Anlama | Mat01MK0189 | – | AU |
| Mat01MK0199 | Aynı tabanlı üslü ifadelerde çarpma kuralını sözel ve cebirsel olarak ifade eder. | Bilgi | ç | Anlama | Mat01MK0190 | – | AU |
| Mat01MK0200 | Aynı tabanlı üslü ifadelerde bölme kuralını sözel ve cebirsel olarak ifade eder. | Bilgi | ç | Anlama | Mat01MK0191 | – | AU |
| Mat01MK0201 | Üssün üssü kuralını sözel ve cebirsel olarak ifade eder. | Bilgi | ç | Anlama | Mat01MK0192 | – | AU |
| Mat01MK0202 | Çarpımın kuvveti kuralını sözel ve cebirsel olarak ifade eder. | Bilgi | ç | Anlama | Mat01MK0193 | – | AU |
| Mat01MK0203 | Bölümün kuvveti kuralını sözel ve cebirsel olarak ifade eder. | Bilgi | ç | Anlama | Mat01MK0194 | – | AU |
| Mat01MK0204 | Üslü ifadelerle çarpma işlemini kuralları kullanarak yapar. | Beceri | ç | Uygulama | Mat01MK0180 | Mat01YG0030; Mat01YG0031 | ÇS |
| Mat01MK0205 | Üslü ifadelerle bölme işlemini kuralları kullanarak yapar. | Beceri | ç | Uygulama | Mat01MK0181 | Mat01YG0031 | ÇS |
| Mat01MK0206 | Üslü ifadelerle kuvvet alma işlemini kuralları kullanarak yapar. | Beceri | ç | Uygulama | Mat01MK0183; Mat01MK0184; Mat01MK0185 | Mat01YG0031 | ÇS |
| Mat01MK0207 | Üslü ifadelerle toplama ve çıkarmayı değerlerini bularak yapar. | Beceri | ç | Uygulama | Mat01MK0176 | Mat01YG0030 | ÇS |
| Mat01MK0208 | Üslü ifadelerle toplama ve çıkarmayı ortak çarpan parantezine alarak yapar. | Beceri | ç | Uygulama | Mat01MK0204; Mat02MK0013 | Mat01YG0030 | ÇS |
| Mat01MK0209 | Üslü gösterimin tekrarlı çarpımı ve çok büyük ya da küçük nicelikleri kısa ifade etmedeki katkısını açıklar. | Bilgi | d | Anlama | Mat01MK0175 | – | AU |

> 2026-10-01: Tek ölçülebilir hedef bölmesi ve yeniden numaralama sonrası tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 11 mikro kazanım (11 yeni, 0 yeniden kullanım); yeni olanlardan 6 Bilgi, 5 Beceri.

---

## 3. Örnek ölçme maddeleri

**Mat01MK0182:** 2⁻³ ifadesinin değeri kaçtır?  
A) −8 (Mat01YG0031) · B) −6 · C) 1/8 ✔ · D) 8

**Mat01MK0207:** 3² + 3³ işleminin sonucu kaçtır?  
A) 3⁵ = 243 (Mat01YG0030) · B) 36 ✔ · C) 3⁶ · D) 15

**Mat01MK0177:** (−3)⁴ ile −3⁴ ifadelerinin değerleri eşit midir? Gerekçenle açıkla. ("Eşittir" yanıtı Mat01YG0028 yanılgısını gösterir.)

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
