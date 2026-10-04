# Mikro Kazanım Ayrıştırması: FİZ.9.2.4 (taslak v0.1)

> **FİZ.9.2.4** Vektörlerin toplanmasında kullanılan uç uca ekleme ve paralelkenar yöntemi ile bileşenlerine ayırma işlemine ilişkin tümevarımsal akıl yürütebilme
> a) Yöntemleri inceleyerek örüntüleri bulur.
> b) Genelleme yapar.
>
> Kaynak: https://tymm.meb.gov.tr/fizik-dersi/unite/57
> Sınıf ünitesi: Fiz09-U2 (Kuvvet ve Hareket) · Ana ünite: 02 Kuvvet ve Hareket

Yöntem: `Fizik/mikro-kazanimlar/FIZ.10.3.4-esdeger-direnc.md` dosyasındaki adımlar; kodlama, Bilgi/Beceri ve işlem türü ölçütü: `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Fiz02YG0004 | Bileşke vektörün büyüklüğü her zaman vektörlerin büyüklükleri toplamına eşittir. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | İşlem türü | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|---|
| Fiz02MK0022 | Aynı doğrultudaki iki vektörü uç uca ekleme yöntemiyle kareli düzlemde toplar. | Beceri | Kural uygulama | a | Uygulama | Fiz02MK0015; Fiz02MK0019 | – | ÇS |
| Fiz02MK0023 | Bir vektörü dik koordinat sisteminde, trigonometri kullanmadan x ve y bileşenlerine ayırır. | Beceri | Dönüştürme | a | Uygulama | Fiz02MK0015; Fiz02MK0016 | – | ÇS |
| Fiz02MK0024 | Farklı doğrultudaki iki vektörü uç uca ekleme yöntemiyle kareli düzlemde toplar. | Beceri | Kural uygulama | a | Uygulama | Fiz02MK0022 | Fiz02YG0004 | ÇS, AU |
| Fiz02MK0025 | Farklı doğrultudaki iki vektörü paralelkenar yöntemiyle kareli düzlemde toplayarak bileşkeyi çizer. | Beceri | Kural uygulama | a | Uygulama | Fiz02MK0024 | Fiz02YG0004 | ÇS |
| Fiz02MK0026 | Uç uca ekleme ve paralelkenar yöntemlerinin aynı bileşkeyi verdiği genellemesini yapar. | Bilgi | Çıkarım ve ilişkilendirme | b | Analiz | Fiz02MK0024; Fiz02MK0025 | – | ÇS, AU |
| Fiz02MK0027 | İki vektörün bileşkesinin vektörler aynı yönlüyken en büyük olduğu genellemesini yapar. | Bilgi | Çıkarım ve ilişkilendirme | b | Analiz | Fiz02MK0026; Fiz02MK0022 | Fiz02YG0004 | ÇS |
| Fiz02MK0028 | İki vektörün bileşkesinin vektörler zıt yönlüyken en küçük olduğu genellemesini yapar. | Bilgi | Çıkarım ve ilişkilendirme | b | Analiz | Fiz02MK0026; Fiz02MK0022 | Fiz02YG0004 | ÇS |

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi (rubrikle)

Özet: 7 mikro kazanım (7 yeni, 0 yeniden kullanım); yeni olanlardan 3 Bilgi, 4 Beceri.

---

## 3. Örnek ölçme maddesi

**Fiz02MK0026:** Büyüklükleri 3 N ve 4 N olan iki kuvvetin bileşkesi hangisi olamaz?  
A) 1 N · B) 5 N · C) 7 N · D) 8 N ✔ (7 N'yi her zaman bekleyen: Fiz02YG0004)

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
