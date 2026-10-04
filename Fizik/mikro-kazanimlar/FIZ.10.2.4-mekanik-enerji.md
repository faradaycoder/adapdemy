# Mikro Kazanım Ayrıştırması: FİZ.10.2.4 (taslak v0.1)

> **FİZ.10.2.4** Mekanik enerjiyi çözümleyebilme
> a) Mekanik enerjiye ilişkin bileşenleri belirler
> b) Mekanik enerjiyle ilgili bileşenler arasındaki matematiksel ilişkiyi belirler
>
> Kaynak: https://tymm.meb.gov.tr/fizik-dersi/unite/108
> Sınıf ünitesi: Fiz10-U2 (Enerji) · Ana ünite: 04 Enerji
> Sınırlama (TYMM): TYMM bu çıktı için sınırlama belirtmemiştir.
> Ön öğrenmeler: iş ve enerji kavramları hakkında temel düzeyde bilgi (TYMM ön kabulü).

Yöntem: `FIZ.10.3.4-esdeger-direnc.md` dosyasındaki 8 adım; kodlama ve Bilgi/Beceri ölçütü: `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Fiz04YG0017 | Çekim potansiyel enerjisi yalnızca yüksekliğe bağlıdır; kütlenin etkisi yoktur. |
| Fiz04YG0019 | Hız iki katına çıkınca kinetik enerji de iki katına çıkar. |
| Fiz04YG0018 | Sürtünmesiz ortamda serbest düşen cismin mekanik enerjisi aşağı indikçe azalır. |
| Fiz04YG0013 | Enerji kullanıldıkça harcanıp yok olur. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Fiz04MK0089 | Mekanik enerjinin kinetik ve potansiyel enerjinin toplamı olduğunu belirtir. | Bilgi | a | Hatırlama | Fiz04MK0073; Fiz04MK0074; Fiz04MK0075 | – | ÇS |
| Fiz04MK0090 | Kinetik enerjinin kütleye bağlı olduğunu belirler. | Bilgi | a | Anlama | Fiz04MK0073 | – | ÇS |
| Fiz04MK0091 | Kinetik enerjinin hıza bağlı olduğunu belirler. | Bilgi | a | Anlama | Fiz04MK0073 | – | ÇS |
| Fiz04MK0092 | Çekim potansiyel enerjisinin kütleye bağlı olduğunu belirler. | Bilgi | a | Anlama | Fiz04MK0074 | Fiz04YG0017 | ÇS |
| Fiz04MK0093 | Çekim potansiyel enerjisinin yüksekliğe bağlı olduğunu belirler. | Bilgi | a | Anlama | Fiz04MK0074 | – | ÇS |
| Fiz04MK0094 | Sürtünmesiz ortamda mekanik enerjinin korunduğunu (Ek + Ep = sabit) belirtir. | Bilgi | b | Anlama | Fiz04MK0089 | Fiz04YG0018 | ÇS |
| Fiz04MK0095 | Ek = ½·m·v² modeliyle kinetik enerjiyi hesaplar. | Beceri | b | Uygulama | Fiz04MK0090; Fiz04MK0091 | Fiz04YG0019 | ÇS |
| Fiz04MK0096 | Ep = m·g·h modeliyle çekim potansiyel enerjisini seçilen referans düzeyine göre hesaplar. | Beceri | b | Uygulama | Fiz04MK0092; Fiz04MK0093 | Fiz04YG0017 | ÇS |
| Fiz04MK0097 | Sürtünmeli ortamda mekanik enerjinin bir kısmının ısı enerjisine dönüştüğünü açıklar. | Bilgi | b | Analiz | Fiz04MK0094; Fiz04MK0084; Fiz04MK0085; Fiz04MK0008 | – | ÇS, AU |
| Fiz04MK0098 | Sürtünmeli ortamda da toplam enerjinin korunduğunu açıklar. | Bilgi | b | Analiz | Fiz04MK0094; Fiz04MK0084; Fiz04MK0085 | Fiz04YG0013 | ÇS, AU |
| Fiz04MK0099 | Mekanik enerjinin korunumunu kullanarak serbest düşen ya da sürtünmesiz eğik düzlemden kayan cismin hızını ya da yüksekliğini hesaplar. | Beceri | b | Uygulama | Fiz04MK0095; Fiz04MK0096; Fiz04MK0094 | Fiz04YG0018 | ÇS, AU |

> 2026-10-01: Tek ölçülebilir hedef taramasıyla güncellendi (bir MK = bir soruyla tamamı ölçülebilen tek hedef). Tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 7 mikro kazanım (7 yeni, 0 yeniden kullanım); yeni olanlardan 4 Bilgi, 3 Beceri.

---

## 3. Örnek ölçme maddeleri

**Fiz04MK0095:** Hızı 10 m/s'den 20 m/s'ye çıkan bir aracın kinetik enerjisi nasıl değişir?  
A) 2 katına çıkar (Fiz04YG0019) · B) 4 katına çıkar ✔ · C) Değişmez · D) Yarıya iner

**Fiz04MK0099:** Sürtünmesiz ortamda 20 m yükseklikten serbest bırakılan cisim yere kaç m/s hızla çarpar? (g = 10 m/s²)  
A) 10 · B) 20 ✔ · C) 200 · D) 400

**Fiz04MK0097:** Kaydıraktan kayan çocuğun alttaki hızı, sürtünmesiz durumda beklenenden küçüktür. Enerji nereye gitmiştir? Açıklayın. ("Enerji harcandı, yok oldu" yanıtı Fiz04YG0013 yanılgısını gösterir.)

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
