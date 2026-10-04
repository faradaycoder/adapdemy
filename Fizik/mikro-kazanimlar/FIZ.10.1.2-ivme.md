# Mikro Kazanım Ayrıştırması: FİZ.10.1.2 (taslak v0.1)

> **FİZ.10.1.2** İvme ve hız değişimi arasındaki ilişkiye yönelik tümevarımsal akıl yürütebilme
> a) İlişkiyi keşfeder
> b) İlişkiyi genelleştirir
>
> Kaynak: https://tymm.meb.gov.tr/fizik-dersi/unite/100
> Sınıf ünitesi: Fiz10-U1 (Kuvvet ve Hareket) · Ana ünite: 02 Kuvvet ve Hareket
> Sınırlama (TYMM): TYMM bu çıktı için sınırlama belirtmemiştir.
> Ön öğrenmeler: hız, konum, yer değiştirme ve ivme kavramları (TYMM ön kabulü).

Yöntem: `FIZ.10.3.4-esdeger-direnc.md` dosyasındaki 8 adım; kodlama ve Bilgi/Beceri ölçütü: `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Fiz02YG0012 | Hızı büyük olan cismin ivmesi de büyüktür. |
| Fiz02YG0013 | Hızın sıfır olduğu anda ivme de sıfırdır. |
| Fiz02YG0014 | İvmenin negatif olması her zaman yavaşlama demektir. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Fiz02MK0063 | Hız-zaman verisinden birim zamandaki hız değişimini hesaplar. | Beceri | a | Uygulama | Fiz02MK0058 | – | AU, PG |
| Fiz02MK0064 | İvmeyi birim zamandaki hız değişimi (a = Δv / Δt) olarak tanımlar. | Bilgi | a | Anlama | Fiz02MK0063; Fiz02MK0045 | – | ÇS |
| Fiz02MK0065 | İvmenin birimini (m/s²) belirtir. | Bilgi | a | Anlama | Fiz02MK0064 | – | ÇS |
| Fiz02MK0066 | Hızın büyük olmasının ivmenin büyük olduğunu göstermediğini verilerle gösterir. | Bilgi | a | Analiz | Fiz02MK0064 | Fiz02YG0012 | ÇS, AU |
| Fiz02MK0067 | Hızın sıfır olmasının ivmenin sıfır olduğunu göstermediğini verilerle gösterir. | Bilgi | a | Analiz | Fiz02MK0064 | Fiz02YG0013 | ÇS, AU |
| Fiz02MK0068 | Sabit ivmeli harekette hızın eşit zaman aralıklarında eşit miktarda değiştiği genellemesini verilerle destekler. | Beceri | b | Analiz | Fiz02MK0064 | – | AU, PG |
| Fiz02MK0069 | Hız ve ivme aynı yönlüyse cismin hızlandığı genellemesini yapar. | Bilgi | b | Analiz | Fiz02MK0046; Fiz02MK0041 | – | ÇS |
| Fiz02MK0070 | Hız ve ivme zıt yönlüyse cismin yavaşladığı genellemesini yapar. | Bilgi | b | Analiz | Fiz02MK0046; Fiz02MK0041 | Fiz02YG0014 | ÇS |

> 2026-10-01: Tek ölçülebilir hedef taramasıyla güncellendi (bir MK = bir soruyla tamamı ölçülebilen tek hedef). Tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 5 mikro kazanım (5 yeni, 0 yeniden kullanım); yeni olanlardan 3 Bilgi, 2 Beceri.

---

## 3. Örnek ölçme maddeleri

**Fiz02MK0066:** Hızı 30 m/s olan ve sabit hızla giden A aracı ile 2 s'de 0'dan 10 m/s hıza ulaşan B aracından hangisinin ivmesi büyüktür?  
A) A, çünkü hızı büyük (Fiz02YG0012) · B) B ✔ · C) Eşit · D) Bilinemez

**Fiz02MK0069:** −x yönünde hareket eden cismin ivmesi de −x yönündedir. Cisim nasıl hareket eder?  
A) Yavaşlar (Fiz02YG0014) · B) Hızlanır ✔ · C) Sabit hızla gider · D) Durur

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
