# Mikro Kazanım Ayrıştırması: FİZ.11.1.3 (taslak v0.1)

> **FİZ.11.1.3** İki boyutta sabit ivmeli hareket ile ilgili tümevarımsal akıl yürütebilme
> a) Bileşenleri ile sabit hızlı ve sabit ivmeli hareket arasındaki ilişkiyi bulur.
> b) Genelleme yapar.
>
> Kaynak: https://tymm.meb.gov.tr/fizik-dersi/unite/243
> Sınıf ünitesi: Fiz11-U1 (Kuvvet ve Hareket) · Ana ünite: 02 Kuvvet ve Hareket

Yöntem: `Fizik/mikro-kazanimlar/FIZ.10.3.4-esdeger-direnc.md` dosyasındaki adımlar; kodlama, Bilgi/Beceri ve işlem türü ölçütü: `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Fiz02YG0018 | Yatay doğrultuda atılan cismin yatay hızı zamanla azalır. |
| Fiz02YG0019 | Aynı yükseklikten yatay atılan cisim, serbest bırakılan cisimden daha geç yere düşer. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | İşlem türü | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|---|
| Fiz02MK0096 | Yalnızca yer çekimi etkisinde iki boyutta hareket eden cismin hızını trigonometri kullanarak yatay ve düşey bileşenlerine ayırır. | Beceri | Dönüştürme | a | Uygulama | Fiz02MK0023; Fiz02MK0086 | – | ÇS, AU |
| Fiz02MK0097 | İki boyutlu harekette yatay bileşenin sabit hızlı olduğu ilişkisini bulur. | Bilgi | Çıkarım ve ilişkilendirme | a | Analiz | Fiz02MK0096; Fiz02MK0060; Fiz02MK0061 | Fiz02YG0018 | ÇS, AU |
| Fiz02MK0098 | İki boyutlu harekette düşey bileşenin sabit ivmeli (g) olduğu ilişkisini bulur. | Bilgi | Çıkarım ve ilişkilendirme | a | Analiz | Fiz02MK0096; Fiz02MK0086 | – | ÇS, AU |
| Fiz02MK0099 | Yatay ve düşey hareketlerin birbirinden bağımsız olduğu genellemesini yapar. | Bilgi | Çıkarım ve ilişkilendirme | b | Analiz | Fiz02MK0097; Fiz02MK0098 | – | ÇS, AU |
| Fiz02MK0100 | Uçuş süresinin düşey hareketle belirlendiği genellemesini yapar. | Bilgi | Çıkarım ve ilişkilendirme | b | Analiz | Fiz02MK0097; Fiz02MK0098 | Fiz02YG0019 | ÇS, AU |
| Fiz02MK0101 | Bileşen modellerini kullanarak iki boyutlu harekette uçuş süresini hesaplar. | Beceri | Kural uygulama | b | Uygulama | Fiz02MK0099; Fiz02MK0100; Fiz02MK0094 | – | ÇS, AU |
| Fiz02MK0102 | İki boyutlu hareketin yörüngesini yorumlar. | Bilgi | Yorumlama | b | Analiz | Fiz02MK0099; Fiz02MK0100 | – | ÇS, AU |
| Fiz02MK0103 | İki boyutlu harekette yatay bileşenin hız-zaman grafiğini yorumlar. | Bilgi | Yorumlama | b | Analiz | Fiz02MK0099; Fiz02MK0100 | – | ÇS, AU |
| Fiz02MK0104 | İki boyutlu harekette düşey bileşenin hız-zaman grafiğini yorumlar. | Bilgi | Yorumlama | b | Analiz | Fiz02MK0099; Fiz02MK0100 | – | ÇS, AU |
| Fiz02MK0105 | İki boyutlu harekette en büyük yüksekliği düşey bileşen modeliyle hesaplar. | Beceri | Kural uygulama | b | Uygulama | Fiz02MK0101; Fiz02MK0095 | – | ÇS |
| Fiz02MK0106 | İki boyutlu harekette menzili yatay hız bileşeni ve uçuş süresinden hesaplar. | Beceri | Kural uygulama | b | Uygulama | Fiz02MK0101; Fiz02MK0096 | – | ÇS |

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi (rubrikle)

Özet: 11 mikro kazanım (11 yeni, 0 yeniden kullanım); yeni olanlardan 7 Bilgi, 4 Beceri.

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
