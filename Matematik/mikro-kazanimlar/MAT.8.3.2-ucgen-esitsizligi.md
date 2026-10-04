# Mikro Kazanım Ayrıştırması: MAT.8.3.2 (taslak v0.1)

> **MAT.8.3.2** Üçgenin kenar uzunlukları arasındaki ilişkiye yönelik çıkarım yapabilme
> a) Üçgen oluşturabilen doğru parçalarına dair varsayımda bulunur
> b) Varsayımlara uygun üçgenler oluşturur
> c) Doğru parçaları ile varsayımlarını karşılaştırır
> ç) Kenar uzunlukları arasındaki ilişkiye dair önerme sunar
> d) Önermenin gerekçelerini sunar
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
| Mat03YG0015 | Herhangi iki kenarın toplamının üçüncüden büyük olması yeterlidir; en uzun kenarı kontrol etmeye gerek yoktur. |
| Mat03YG0016 | İki kenarın toplamı üçüncü kenara eşit olduğunda da üçgen oluşur. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Mat03MK0113 | Verilen üç uzunlukla üçgen oluşturulup oluşturulamayacağına dair varsayımda bulunur. | Beceri | a | Analiz | Mat03MK0052; Mat03MK0053; Mat03MK0054 | – | AU |
| Mat03MK0114 | Çubuk, cetvel-pergel ya da yazılımla verilen uzunluklarla üçgen oluşturmayı dener. | Beceri | b | Uygulama | Mat03MK0113 | – | PG |
| Mat03MK0115 | Üçgen oluşturabildiği ve oluşturamadığı durumları varsayımlarıyla karşılaştırır. | Beceri | c | Değerlendirme | Mat03MK0114 | Mat03YG0015 | PG, AU |
| Mat03MK0116 | Bir üçgende herhangi iki kenarın uzunlukları toplamının üçüncü kenardan büyük olduğu önermesini sunar. | Bilgi | ç | Analiz | Mat03MK0115 | Mat03YG0016; Mat03YG0015 | ÇS |
| Mat03MK0117 | Bir üçgende herhangi iki kenarın uzunlukları farkının üçüncü kenardan küçük olduğu önermesini sunar. | Bilgi | ç | Analiz | Mat03MK0115 | – | ÇS |
| Mat03MK0118 | İki kenarı verilen üçgenin üçüncü kenarının alabileceği değer aralığını bulur. | Beceri | ç | Uygulama | Mat03MK0116; Mat03MK0117 | Mat03YG0016 | ÇS |
| Mat03MK0119 | Önermesini karşı örnek ve sınır durum (toplamın üçüncü kenara eşit olması) üzerinden gerekçelendirir. | Beceri | d | Değerlendirme | Mat03MK0116 | Mat03YG0016 | AU |

> 2026-10-01: Tek ölçülebilir hedef bölmesi ve yeniden numaralama sonrası tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 6 mikro kazanım (6 yeni, 0 yeniden kullanım); yeni olanlardan 1 Bilgi, 5 Beceri.

---

## 3. Örnek ölçme maddeleri

**Mat03MK0118:** Kenarları 5 cm ve 9 cm olan üçgenin üçüncü kenarı tam sayı ise kaç farklı değer alabilir?  
A) 9 ✔ · B) 11 (Mat03YG0016: 4 ve 14 dâhil) · C) 13 · D) 14

**Mat03MK0119:** 3 cm, 4 cm ve 7 cm uzunluğundaki çubuklarla üçgen oluşturulabilir mi? Gerekçenle açıkla.

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
