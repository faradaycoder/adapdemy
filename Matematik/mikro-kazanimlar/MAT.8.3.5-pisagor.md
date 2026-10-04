# Mikro Kazanım Ayrıştırması: MAT.8.3.5 (taslak v0.1)

> **MAT.8.3.5** Kenar uzunlukları a² + b² = c² eşitliğini sağlayan üçgenleri oluşturarak Pisagor bağıntısını yorumlayabilme
> a) a² + b² = c² eşitliğini sağlayan rasyonel sayıları inceler
> b) Dik üçgen oluşturur ve hipotenüs ilişkisini belirler
> c) Pisagor bağıntısını açı-kenar ilişkisi ile ilişkilendirir
>
> Kaynak: https://tymm.meb.gov.tr/ortaokul-matematik-dersi/unite/474
> Sınıf teması: Mat08-T3 (Geometrik Şekiller) · Ana tema: 03 Geometrik Şekiller
> Sınırlama (TYMM): TYMM bu çıktı için sınırlama belirtmemiştir.
> Ön öğrenmeler: üç doğrunun ikişerli kesişimiyle üçgen oluşturma, matematiksel araçları (cetvel, pergel, gönye, açıölçer) kullanma, kesişen iki çemberle üçgen inşa etme, üçgenin yardımcı elemanlarını belirleme (TYMM temel kabulü).

Yöntem: fizikle aynı 8 adım (`Fizik/mikro-kazanimlar/FIZ.10.3.4-esdeger-direnc.md`); kodlama ve Bilgi/Beceri ölçütü: EVALORA kökündeki `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Mat03YG0022 | Hipotenüs, üçgenin tabanda (altta) çizilen kenarıdır. |
| Mat03YG0023 | Dik üçgende kenarlar arasındaki ilişki a + b = c'dir (kareler alınmaz). |
| Mat03YG0024 | Pisagor bağıntısı her üçgende geçerlidir. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Mat03MK0140 | a² + b² = c² eşitliğini sağlayan sayı üçlülerini (3-4-5, 6-8-10, 5-12-13 gibi) inceler ve belirler. | Beceri | a | Uygulama | Mat01MK0176; Mat01MK0213 | – | ÇS |
| Mat03MK0141 | Dik üçgende hipotenüsü dik açının karşısındaki en uzun kenar olarak belirler. | Bilgi | b | Anlama | Mat03MK0110 | Mat03YG0022 | ÇS |
| Mat03MK0142 | Bu uzunluklarla oluşturduğu üçgenlerin dik üçgen olduğunu gözlemler. | Beceri | b | Uygulama | Mat03MK0140; Mat03MK0052; Mat03MK0021 | – | PG |
| Mat03MK0143 | Pisagor bağıntısını kullanarak dik üçgende bilinmeyen kenar uzunluğunu hesaplar. | Beceri | b | Uygulama | Mat03MK0142; Mat03MK0141; Mat01MK0213 | Mat03YG0023 | ÇS |
| Mat03MK0144 | En uzun kenar c için c² = a² + b² ise üçgenin dik üçgen olduğunu açı–kenar ilişkisiyle açıklar. | Bilgi | c | Analiz | Mat03MK0143; Mat03MK0110 | Mat03YG0024 | ÇS, AU |
| Mat03MK0145 | En uzun kenar c için c² > a² + b² ise üçgenin geniş açılı olduğunu açı–kenar ilişkisiyle açıklar. | Bilgi | c | Analiz | Mat03MK0143; Mat03MK0110 | – | ÇS, AU |
| Mat03MK0146 | En uzun kenar c için c² < a² + b² ise üçgenin dar açılı olduğunu açı–kenar ilişkisiyle açıklar. | Bilgi | c | Analiz | Mat03MK0143; Mat03MK0110 | – | ÇS, AU |

> 2026-10-01: Tek ölçülebilir hedef bölmesi ve yeniden numaralama sonrası tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 5 mikro kazanım (5 yeni, 0 yeniden kullanım); yeni olanlardan 2 Bilgi, 3 Beceri.

---

## 3. Örnek ölçme maddeleri

**Mat03MK0143:** Dik kenarları 6 cm ve 8 cm olan dik üçgenin hipotenüsü kaç cm'dir?  
A) 14 (Mat03YG0023) · B) 10 ✔ · C) 100 · D) 48

**Mat03MK0144:** Kenarları 4, 5, 6 cm olan üçgen dik üçgen midir? Açıklayın. ("Pisagor her üçgende geçerlidir" düşüncesi Mat03YG0024 yanılgısını gösterir.)

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
