# Mikro Kazanım Ayrıştırması: FİZ.11.1.4 (taslak v0.1)

> **FİZ.11.1.4** Newton'ın Hareket Yasaları ile ilgili tümevarımsal akıl yürütebilme
> a) Bileşke kuvvet ile hareket arasındaki ilişkileri keşfeder.
> b) Genellemeler yapar.
>
> Kaynak: https://tymm.meb.gov.tr/fizik-dersi/unite/243
> Sınıf ünitesi: Fiz11-U1 (Kuvvet ve Hareket) · Ana ünite: 02 Kuvvet ve Hareket

Yöntem: `Fizik/mikro-kazanimlar/FIZ.10.3.4-esdeger-direnc.md` dosyasındaki adımlar; kodlama, Bilgi/Beceri ve işlem türü ölçütü: `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Fiz02YG0020 | Hareket eden cismin hareketini sürdürmesi için üzerine sürekli kuvvet etki etmelidir. |
| Fiz02YG0021 | Çarpışmada büyük kütleli cisim küçük kütleliye daha büyük kuvvet uygular. |
| Fiz02YG0022 | Etki ve tepki kuvvetleri aynı cisme etki ettiği için birbirini dengeler. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | İşlem türü | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|---|
| Fiz02MK0107 | Bileşke kuvvet sıfırken durgun cismin durgun kaldığı ilişkisini keşfeder. | Bilgi | Çıkarım ve ilişkilendirme | a | Analiz | Fiz02MK0024 | – | ÇS, AU |
| Fiz02MK0108 | Bileşke kuvvet sıfırken hareketli cismin sabit hızla hareketine devam ettiği ilişkisini keşfeder. | Bilgi | Çıkarım ve ilişkilendirme | a | Analiz | Fiz02MK0024 | Fiz02YG0020 | ÇS, AU |
| Fiz02MK0109 | Bileşke kuvvet ile ivmenin doğru orantılı olduğu ilişkisini keşfeder. | Bilgi | Çıkarım ve ilişkilendirme | a | Analiz | Fiz02MK0107; Fiz02MK0108; Fiz02MK0064 | – | ÇS, AU |
| Fiz02MK0110 | Aynı bileşke kuvvet altında kütle ile ivmenin ters orantılı olduğu ilişkisini keşfeder. | Bilgi | Çıkarım ve ilişkilendirme | a | Analiz | Fiz02MK0109 | – | ÇS |
| Fiz02MK0111 | Etki-tepki kuvvetlerinin eşit büyüklükte olduğu genellemesini yapar. | Bilgi | Çıkarım ve ilişkilendirme | b | Analiz | Fiz02MK0012 | Fiz02YG0021 | ÇS |
| Fiz02MK0112 | Etki-tepki kuvvetlerinin zıt yönde olduğu genellemesini yapar. | Bilgi | Çıkarım ve ilişkilendirme | b | Analiz | Fiz02MK0012 | – | ÇS |
| Fiz02MK0113 | Etki-tepki kuvvetlerinin farklı cisimlere etki ettiği genellemesini yapar. | Bilgi | Çıkarım ve ilişkilendirme | b | Analiz | Fiz02MK0012 | Fiz02YG0022 | ÇS |
| Fiz02MK0114 | Newton'ın ikinci yasasını Fnet = m·a modeli olarak genelleştirir. | Beceri | Model kurma | b | Analiz | Fiz02MK0109; Fiz02MK0110 | – | ÇS, AU |
| Fiz02MK0115 | Newtonu temel birimlerle (kg·m/s²) ifade eder. | Beceri | Dönüştürme | b | Uygulama | Fiz02MK0114; Fiz02MK0009 | – | ÇS |

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi (rubrikle)

Özet: 9 mikro kazanım (9 yeni, 0 yeniden kullanım); yeni olanlardan 7 Bilgi, 2 Beceri.

---

## 3. Örnek ölçme maddesi

**Fiz02MK0111:** Bir kamyon küçük bir otomobille çarpışıyor. Çarpışma sırasında birbirlerine uyguladıkları kuvvetler için hangisi doğrudur?  
A) Kamyonun uyguladığı daha büyüktür (Fiz02YG0021) · B) Eşit büyüklükte ve zıt yönlüdür ✔ · C) Otomobilin uyguladığı daha büyüktür · D) Birbirini dengeler (Fiz02YG0022)

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
