# Mikro Kazanım Ayrıştırması: MAT.8.3.1 (taslak v0.1)

> **MAT.8.3.1** Matematiksel araç ve teknoloji yardımıyla üçgenin kenarları ve açıları arasındaki ilişkiyi yorumlayabilme
> a) Üçgenin kenar ve açı özelliklerini inceler
> b) Kenarları ve açıları büyüklüğüne göre sıralar
> c) Kenar uzunlukları ve açı ölçüleri arasındaki ilişkiyi ifade eder
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
| Mat03YG0013 | En büyük açı en uzun kenarın karşısında değil, yanındadır. |
| Mat03YG0014 | Kenar uzunlukları açı ölçüleriyle doğru orantılıdır; açı iki katına çıkınca karşısındaki kenar da iki katına çıkar. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Mat03MK0105 | Üçgende bir açının karşısındaki kenarı belirler. | Bilgi | a | Anlama | Mat03MK0010 | – | ÇS |
| Mat03MK0106 | Üçgende bir kenarın karşısındaki açıyı belirler. | Bilgi | a | Anlama | Mat03MK0010 | – | ÇS |
| Mat03MK0107 | Araç ya da dinamik geometri yazılımıyla bir açıyı büyüttüğünde karşısındaki kenarın uzadığını gözlemler. | Beceri | a | Uygulama | Mat03MK0105; Mat03MK0106 | – | PG |
| Mat03MK0108 | Üçgenin açılarını ölçülerine göre sıralar. | Beceri | b | Uygulama | Mat03MK0105; Mat03MK0106 | – | ÇS |
| Mat03MK0109 | Üçgenin kenarlarını uzunluklarına göre sıralar. | Beceri | b | Uygulama | Mat03MK0105; Mat03MK0106 | – | ÇS |
| Mat03MK0110 | Büyük açı karşısında büyük kenar, küçük açı karşısında küçük kenar bulunduğu ilişkisini ifade eder. | Bilgi | c | Anlama | Mat03MK0107; Mat03MK0108; Mat03MK0109 | Mat03YG0013; Mat03YG0014 | ÇS |
| Mat03MK0111 | Açı ölçüleri verilen üçgenin kenarlarını açı–kenar ilişkisiyle sıralar. | Beceri | c | Uygulama | Mat03MK0110 | Mat03YG0013 | ÇS |
| Mat03MK0112 | Kenarları verilen üçgenin açılarını açı–kenar ilişkisiyle sıralar. | Beceri | c | Uygulama | Mat03MK0110 | Mat03YG0013 | ÇS |

> 2026-10-01: Tek ölçülebilir hedef bölmesi ve yeniden numaralama sonrası tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 5 mikro kazanım (5 yeni, 0 yeniden kullanım); yeni olanlardan 2 Bilgi, 3 Beceri.

---

## 3. Örnek ölçme maddeleri

**Mat03MK0111:** ABC üçgeninde m(A) = 70°, m(B) = 50°. En uzun kenar hangisidir?  
A) AB (Mat03YG0013) · B) BC ✔ · C) AC · D) Belirlenemez

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
