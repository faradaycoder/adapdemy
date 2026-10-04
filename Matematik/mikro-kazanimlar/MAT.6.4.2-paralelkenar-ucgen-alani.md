# Mikro Kazanım Ayrıştırması: MAT.6.4.2 (taslak v0.1)

> **MAT.6.4.2** Dikdörtgenin alan bağıntısına yönelik deneyimlerini paralelkenar ve üçgenin alan bağıntılarına yansıtabilme
> a) Dikdörtgenin alanını gözden geçirir.
> b) Paralelkenar ve üçgenin alanına çıkarım yapar.
> c) Değerlendirir.
>
> Kaynak: https://tymm.meb.gov.tr/ortaokul-matematik-dersi/unite/460
> Sınıf teması: Mat06-T4 (Geometrik Nicelikler) · Ana tema: 04 Geometrik Nicelikler

Yöntem: `Fizik/mikro-kazanimlar/FIZ.10.3.4-esdeger-direnc.md` dosyasındaki adımlar; kodlama, Bilgi/Beceri ve işlem türü ölçütü: `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Mat04YG0004 | Paralelkenarın alanı iki komşu kenarının çarpımıdır. |
| Mat04YG0005 | Üçgenin alanı taban ile yüksekliğin çarpımıdır; ikiye bölünmez. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | İşlem türü | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|---|
| Mat04MK0030 | Dikdörtgenin alanını kenar uzunluklarının çarpımı olarak belirtir. | Bilgi | Tanıma ve hatırlama | a | Hatırlama | Mat04MK0010 | – | ÇS |
| Mat04MK0031 | Paralelkenarda bir kenara ait yüksekliği belirler ve çizer. | Beceri | Beceri uygulama | b | Uygulama | Mat03MK0011 | – | ÇS |
| Mat04MK0032 | Üçgende bir kenara ait yüksekliği belirler ve çizer. | Beceri | Beceri uygulama | b | Uygulama | Mat03MK0011 | – | ÇS |
| Mat04MK0033 | Dikdörtgenden yola çıkarak paralelkenarın alan bağıntısına (taban × yükseklik) ulaşır. | Beceri | Model kurma | b | Analiz | Mat04MK0030; Mat04MK0031 | Mat04YG0004 | ÇS, AU |
| Mat04MK0034 | Paralelkenardan yola çıkarak üçgenin alan bağıntısına (taban × yükseklik / 2) ulaşır. | Beceri | Model kurma | b | Analiz | Mat04MK0033 | Mat04YG0005 | ÇS, AU |
| Mat04MK0035 | Paralelkenarın alanını hesaplar. | Beceri | Kural uygulama | c | Uygulama | Mat04MK0033 | – | ÇS |
| Mat04MK0036 | Üçgenin alanını hesaplar. | Beceri | Kural uygulama | c | Uygulama | Mat04MK0034 | Mat04YG0005 | ÇS |
| Mat04MK0037 | Paralelkenarın alan bağıntısını farklı örneklerde değerlendirir. | Beceri | Sınama ve değerlendirme | c | Değerlendirme | Mat04MK0035 | – | AU |
| Mat04MK0038 | Üçgenin alan bağıntısını farklı örneklerde değerlendirir. | Beceri | Sınama ve değerlendirme | c | Değerlendirme | Mat04MK0036 | – | AU |

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi (rubrikle)

Özet: 9 mikro kazanım (9 yeni, 0 yeniden kullanım); yeni olanlardan 1 Bilgi, 8 Beceri.

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
