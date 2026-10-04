# Mikro Kazanım Ayrıştırması: MAT.8.3.4 (taslak v0.1)

> **MAT.8.3.4** Bir üçgene benzer üçgen oluşturmak için yeterli elemanlar hakkında çıkarım yapabilme
> a) Bir üçgene benzer üçgen oluşturmak için bilinmesi yeterli olan elemanlara dair varsayımda bulunur
> b) Matematiksel araç ve teknoloji yardımıyla varsayımlarına uygun benzer üçgenler oluşturur
> c) Oluşturduğu üçgenleri varsayımları ile karşılaştırır
> ç) Bir üçgene benzer üçgen oluşturmak için bilinmesi yeterli olan elemanlara dair önerme sunar
> d) Önermesinin iki üçgenin benzer olup olmadığını incelemeye yönelik katkısını değerlendirir
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
| Mat03YG0020 | Benzer üçgenlerde kenarlar aynı oranda değil, aynı miktarda artar (her kenara 2 cm eklemek). |
| Mat03YG0021 | Benzer üçgenler eş olmalıdır; eş üçgenler benzer sayılmaz. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Mat03MK0128 | Bir üçgene benzer üçgen oluşturmak için hangi elemanların yeterli olabileceğine dair varsayımda bulunur. | Beceri | a | Analiz | Mat03MK0123; Mat03MK0124; Mat03MK0125 | – | AU |
| Mat03MK0129 | Araç ya da yazılımla bir üçgeni belirli oranda büyüterek ya da küçülterek benzer üçgenler oluşturur. | Beceri | b | Uygulama | Mat03MK0128; Mat03MK0052 | – | PG |
| Mat03MK0130 | Oluşturduğu üçgenlerin karşılıklı açılarını ve kenar oranlarını ölçerek varsayımlarıyla karşılaştırır. | Beceri | c | Değerlendirme | Mat03MK0129 | Mat03YG0020 | PG |
| Mat03MK0131 | Benzerliği karşılıklı açıların eş, karşılıklı kenarların orantılı olması olarak ifade eder. | Bilgi | ç | Anlama | Mat03MK0130 | Mat03YG0020 | ÇS |
| Mat03MK0132 | Benzerlik oranını tanımlar. | Bilgi | ç | Hatırlama | Mat03MK0130 | – | ÇS |
| Mat03MK0133 | Açı-Açı benzerlik koşulunu önerme olarak ifade eder. | Bilgi | ç | Anlama | Mat03MK0131 | – | ÇS |
| Mat03MK0134 | Kenar-Açı-Kenar benzerlik koşulunu önerme olarak ifade eder. | Bilgi | ç | Anlama | Mat03MK0131 | – | ÇS |
| Mat03MK0135 | Kenar-Kenar-Kenar benzerlik koşulunu önerme olarak ifade eder. | Bilgi | ç | Anlama | Mat03MK0131 | – | ÇS |
| Mat03MK0136 | Eşliği benzerlik oranı 1 olan özel bir benzerlik durumu olarak açıklar. | Bilgi | ç | Analiz | Mat03MK0132; Mat03MK0123; Mat03MK0124; Mat03MK0125 | Mat03YG0021 | ÇS |
| Mat03MK0137 | Benzerlik oranını kullanarak benzer üçgenlerde bilinmeyen kenar uzunluğunu bulur. | Beceri | d | Uygulama | Mat03MK0132 | Mat03YG0020 | ÇS |
| Mat03MK0138 | Verilen iki üçgenin benzer olup olmadığını benzerlik koşullarıyla inceler. | Beceri | d | Değerlendirme | Mat03MK0133; Mat03MK0134; Mat03MK0135 | – | ÇS, AU |
| Mat03MK0139 | İki üçgenin benzerliğini ~ sembolüyle, karşılıklı köşeleri doğru sırada yazarak gösterir. | Beceri | d | Değerlendirme | Mat03MK0133; Mat03MK0134; Mat03MK0135 | – | ÇS, AU |

> 2026-10-01: Tek ölçülebilir hedef bölmesi ve yeniden numaralama sonrası tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 8 mikro kazanım (8 yeni, 0 yeniden kullanım); yeni olanlardan 3 Bilgi, 5 Beceri.

---

## 3. Örnek ölçme maddeleri

**Mat03MK0137:** Kenarları 3, 4, 5 cm olan üçgene benzer üçgenin en kısa kenarı 6 cm ise en uzun kenarı kaç cm'dir?  
A) 8 (Mat03YG0020: 5 + 3) · B) 10 ✔ · C) 7 · D) 12

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
