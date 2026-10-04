# Mikro Kazanım Ayrıştırması: MAT.8.3.3 (taslak v0.1)

> **MAT.8.3.3** Bir üçgene eş üçgen oluşturmak için yeterli elemanlar hakkında çıkarım yapabilme
> a) Bir üçgene eş üçgen oluşturmak için bilinmesi yeterli olan elemanlara dair varsayımda bulunur
> b) Matematiksel araç ve teknoloji yardımıyla varsayımlarına uygun üçgenler oluşturur
> c) Oluşturduğu üçgenleri varsayımları ile karşılaştırır
> ç) Bir üçgene eş üçgen oluşturmak için bilinmesi yeterli olan elemanlara dair önerme sunar
> d) Önermesinin iki üçgenin eş olup olmadığını incelemeye yönelik katkısını değerlendirir
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
| Mat03YG0017 | Üç açısı karşılıklı eşit olan üçgenler eştir. |
| Mat03YG0018 | İki kenar ve bu kenarların arasında olmayan bir açı eşse üçgenler her zaman eştir. |
| Mat03YG0019 | Eşlik gösteriminde (≅) köşelerin yazılış sırası önemli değildir. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Mat03MK0120 | Bir üçgene eş üçgen oluşturmak için hangi elemanların (kenar, açı) bilinmesinin yeterli olabileceğine dair varsayımda bulunur. | Beceri | a | Analiz | Mat03MK0105 | – | AU |
| Mat03MK0121 | Araç ya da yazılımla belirli elemanları verilen üçgenleri oluşturur. | Beceri | b | Uygulama | Mat03MK0120; Mat03MK0052; Mat03MK0022 | – | PG |
| Mat03MK0122 | Oluşturduğu üçgenleri üst üste koyarak ya da ölçerek varsayımlarıyla karşılaştırır. | Beceri | c | Değerlendirme | Mat03MK0121 | Mat03YG0017 | PG |
| Mat03MK0123 | Kenar-Açı-Kenar eşlik koşulunu önerme olarak ifade eder. | Bilgi | ç | Anlama | Mat03MK0122 | Mat03YG0017; Mat03YG0018 | ÇS |
| Mat03MK0124 | Açı-Kenar-Açı eşlik koşulunu önerme olarak ifade eder. | Bilgi | ç | Anlama | Mat03MK0122 | Mat03YG0017 | ÇS |
| Mat03MK0125 | Kenar-Kenar-Kenar eşlik koşulunu önerme olarak ifade eder. | Bilgi | ç | Anlama | Mat03MK0122 | Mat03YG0017 | ÇS |
| Mat03MK0126 | İki üçgenin eşliğini ≅ sembolüyle, karşılıklı köşeleri doğru sırada yazarak gösterir. | Beceri | ç | Uygulama | Mat03MK0123; Mat03MK0124; Mat03MK0125 | Mat03YG0019 | ÇS |
| Mat03MK0127 | Verilen iki üçgenin eş olup olmadığını eşlik koşullarını kullanarak inceler ve gerekçelendirir. | Beceri | d | Değerlendirme | Mat03MK0123; Mat03MK0124; Mat03MK0125 | Mat03YG0017; Mat03YG0018 | ÇS, AU |

> 2026-10-01: Tek ölçülebilir hedef bölmesi ve yeniden numaralama sonrası tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 6 mikro kazanım (6 yeni, 0 yeniden kullanım); yeni olanlardan 1 Bilgi, 5 Beceri.

---

## 3. Örnek ölçme maddeleri

**Mat03MK0127:** İki üçgenin üç açısı karşılıklı olarak 40°, 60°, 80°'dir. Bu üçgenler için ne söylenebilir?  
A) Kesinlikle eştir (Mat03YG0017) · B) Benzerdir, eş olmayabilir ✔ · C) Hiçbir ilişki yoktur · D) Alanları eşittir

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
