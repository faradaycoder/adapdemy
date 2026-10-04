# Mikro Kazanım Ayrıştırması: MAT.8.5.2 (taslak v0.1)

> **MAT.8.5.2** Koordinat sisteminde noktaların apsis ve ordinatlarının öteleme ve yansıma dönüşümündeki değişimlerine ilişkin çıkarım yapabilme
> a) Noktaların apsis ve ordinatlarındaki değişimlere dair varsayımlarda bulunur
> b) Öteleme ve yansıma dönüşümü altındaki görüntüleri oluşturur
> c) Oluşturduğu görüntülere ait noktaların koordinatlarını varsayımları ile karşılaştırır
> ç) Apsis ve ordinatların dönüşümdeki değişimlerine dair önermeler sunar
> d) Önermelerinin iki şekil arasında dönüşüm ilişkisi bulunup bulunmadığını incelemeye katkısını değerlendirir
>
> Kaynak: https://tymm.meb.gov.tr/ortaokul-matematik-dersi/unite/476
> Sınıf teması: Mat08-T5 (Dönüşüm) · Ana tema: 05 Dönüşüm
> Sınırlama (TYMM): Yansıma koordinat eksenlerine (x ve y ekseni) göre yapılır.
> Ön öğrenmeler: dik koordinat sisteminde noktanın yerini belirleme, yansıma dönüşümüne ilişkin çıkarım, şekil ile yansıma görüntüsü verildiğinde simetri doğrusunu oluşturma (TYMM temel kabulü).

Yöntem: fizikle aynı 8 adım (`Fizik/mikro-kazanimlar/FIZ.10.3.4-esdeger-direnc.md`); kodlama ve Bilgi/Beceri ölçütü: EVALORA kökündeki `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Mat05YG0005 | Sağa ya da sola ötelemede ordinat, yukarı ya da aşağı ötelemede apsis değişir. |
| Mat05YG0006 | x eksenine göre yansımada apsis, y eksenine göre yansımada ordinat işaret değiştirir. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Mat05MK0024 | Ötelemede noktanın apsis ve ordinatının nasıl değişeceğine dair varsayımda bulunur. | Beceri | a | Analiz | Mat02MK0101; Mat02MK0102; Mat05MK0016 | – | AU |
| Mat05MK0025 | Yansımada noktanın apsis ve ordinatının nasıl değişeceğine dair varsayımda bulunur. | Beceri | a | Analiz | Mat02MK0101; Mat02MK0102; Mat05MK0002 | – | AU |
| Mat05MK0026 | Koordinat sisteminde bir noktanın ve çokgenin öteleme altındaki görüntüsünü oluşturur. | Beceri | b | Uygulama | Mat05MK0016; Mat02MK0101; Mat02MK0102 | Mat05YG0005 | ÇS, AU |
| Mat05MK0027 | Bir noktanın ve çokgenin x eksenine göre yansımasını oluşturur. | Beceri | b | Uygulama | Mat02MK0101; Mat02MK0102; Mat05MK0002 | Mat05YG0006 | ÇS, AU |
| Mat05MK0028 | Bir noktanın ve çokgenin y eksenine göre yansımasını oluşturur. | Beceri | b | Uygulama | Mat02MK0101; Mat02MK0102; Mat05MK0002 | Mat05YG0006 | ÇS, AU |
| Mat05MK0029 | Ötelemede oluşturduğu görüntülerin koordinatlarını varsayımlarıyla karşılaştırır. | Beceri | c | Değerlendirme | Mat05MK0026 | – | AU |
| Mat05MK0030 | Yansımada oluşturduğu görüntülerin koordinatlarını varsayımlarıyla karşılaştırır. | Beceri | c | Değerlendirme | Mat05MK0027; Mat05MK0028 | – | AU |
| Mat05MK0031 | Ötelemede yatay kaydırmanın yalnızca apsisi değiştirdiği önermesini sunar. | Bilgi | ç | Analiz | Mat05MK0029 | Mat05YG0005 | ÇS |
| Mat05MK0032 | Ötelemede dikey kaydırmanın yalnızca ordinatı değiştirdiği önermesini sunar. | Bilgi | ç | Analiz | Mat05MK0029 | Mat05YG0005 | ÇS |
| Mat05MK0033 | x eksenine göre yansımada ordinatın işaret değiştirdiği önermesini sunar. | Bilgi | ç | Analiz | Mat05MK0030 | Mat05YG0006 | ÇS |
| Mat05MK0034 | y eksenine göre yansımada apsisin işaret değiştirdiği önermesini sunar. | Bilgi | ç | Analiz | Mat05MK0030 | Mat05YG0006 | ÇS |
| Mat05MK0035 | Koordinat önermelerini kullanarak iki şekil arasında öteleme ilişkisi olup olmadığını inceler. | Beceri | d | Değerlendirme | Mat05MK0031; Mat05MK0032 | – | ÇS, AU |
| Mat05MK0036 | Koordinat önermelerini kullanarak iki şekil arasında yansıma ilişkisi olup olmadığını inceler. | Beceri | d | Değerlendirme | Mat05MK0033; Mat05MK0034 | – | ÇS, AU |

> 2026-10-01: Tek ölçülebilir hedef bölmesi ve yeniden numaralama sonrası tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 7 mikro kazanım (7 yeni, 0 yeniden kullanım); yeni olanlardan 2 Bilgi, 5 Beceri.

---

## 3. Örnek ölçme maddeleri

**Mat05MK0033:** A(3, −2) noktasının x eksenine göre yansıması hangisidir?  
A) (−3, −2) (Mat05YG0006) · B) (3, 2) ✔ · C) (−3, 2) · D) (−2, 3)

**Mat05MK0031:** B(−1, 4) noktası 5 birim sağa ötelenirse görüntüsü hangisidir?  
A) (−1, 9) (Mat05YG0005) · B) (4, 4) ✔ · C) (−6, 4) · D) (4, 9)

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
