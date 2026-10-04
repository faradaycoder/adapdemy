# Mikro Kazanım Ayrıştırması: MAT.9.5.2 (taslak v0.1)

> **MAT.9.5.2** Algoritmik yapılar içerisindeki mantık bağlaçlarını ve niceleyicileri çözümleyebilme
> a) Belirler.
> b) İlişkileri belirler.
>
> Kaynak: https://tymm.meb.gov.tr/matematik-dersi/unite/24
> Sınıf teması: Mat09-T5 (Algoritma ve Bilişim) · Ana tema: 09 Algoritma ve Bilişim

Yöntem: `Fizik/mikro-kazanimlar/FIZ.10.3.4-esdeger-direnc.md` dosyasındaki adımlar; kodlama, Bilgi/Beceri ve işlem türü ölçütü: `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Mat09YG0001 | "veya" bağlacı iki önermeden yalnızca birinin doğru olmasını gerektirir. |
| Mat09YG0002 | "Her" önermesinin değili "hiçbiri" önermesidir. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | İşlem türü | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|---|
| Mat09MK0005 | Önermeyi ve doğruluk değerini tanır. | Bilgi | Tanıma ve hatırlama | a | Hatırlama | – | – | ÇS |
| Mat09MK0006 | "Ve" bağlacını doğruluk tablosuyla kullanır. | Bilgi | Kural uygulama | a | Hatırlama | Mat09MK0005 | – | ÇS |
| Mat09MK0007 | "Veya" bağlacını doğruluk tablosuyla kullanır. | Bilgi | Kural uygulama | a | Hatırlama | Mat09MK0005 | Mat09YG0001 | ÇS |
| Mat09MK0008 | "Değil" işlemini doğruluk tablosuyla kullanır. | Bilgi | Kural uygulama | a | Hatırlama | Mat09MK0005 | – | ÇS |
| Mat09MK0009 | "İse" bağlacını doğruluk tablosuyla kullanır. | Beceri | Kural uygulama | a | Uygulama | Mat09MK0005 | – | ÇS |
| Mat09MK0010 | "Ancak ve ancak" bağlacını doğruluk tablosuyla kullanır. | Beceri | Kural uygulama | a | Uygulama | Mat09MK0009; Mat09MK0006 | – | ÇS |
| Mat09MK0011 | "Her" niceleyicisini kullanır. | Beceri | Kural uygulama | a | Uygulama | Mat09MK0005 | – | ÇS |
| Mat09MK0012 | "Bazı" niceleyicisini kullanır. | Beceri | Kural uygulama | a | Uygulama | Mat09MK0005 | – | ÇS |
| Mat09MK0013 | "Her" niceleyicili önermenin değilini yazar. | Beceri | Kural uygulama | a | Uygulama | Mat09MK0011; Mat09MK0008 | Mat09YG0002 | ÇS |
| Mat09MK0014 | "Bazı" niceleyicili önermenin değilini yazar. | Beceri | Kural uygulama | a | Uygulama | Mat09MK0012; Mat09MK0008 | – | ÇS |
| Mat09MK0015 | Koşul yapıları ile mantık bağlaçları arasındaki ilişkiyi belirler. | Bilgi | Çıkarım ve ilişkilendirme | b | Analiz | Mat09MK0006; Mat09MK0007; Mat09MK0008; Mat09MK0009; Mat09MK0010 | Mat09YG0001 | ÇS |
| Mat09MK0016 | Döngü yapıları ile niceleyiciler arasındaki ilişkiyi belirler. | Bilgi | Çıkarım ve ilişkilendirme | b | Analiz | Mat09MK0011; Mat09MK0012 | – | ÇS |

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi (rubrikle)

Özet: 12 mikro kazanım (12 yeni, 0 yeniden kullanım); yeni olanlardan 6 Bilgi, 6 Beceri.

---

## 3. Örnek ölçme maddesi

**Mat09MK0015:** "Bütün öğrenciler gözlüklüdür" önermesinin değili hangisidir?  
A) Hiçbir öğrenci gözlüklü değildir (Mat09YG0002) · B) En az bir öğrenci gözlüklü değildir ✔ · C) Bazı öğrenciler gözlüklüdür · D) Bütün öğrenciler gözlüksüzdür

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
