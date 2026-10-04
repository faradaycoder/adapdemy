# Mikro Kazanım Ayrıştırması: FİZ.11.2.1 (taslak v0.1)

> **FİZ.11.2.1** Elektrik yükleri arasındaki elektriksel kuvvetin matematiksel modeline yönelik tümevarımsal akıl yürütebilme
> a) İlişkiyi matematiksel olarak modeller.
> b) Model üzerinden genellemeler yapar.
>
> Kaynak: https://tymm.meb.gov.tr/fizik-dersi/unite/248
> Sınıf ünitesi: Fiz11-U2 (Elektrik ve Manyetizma) · Ana ünite: 05 Elektrik ve Manyetizma

Yöntem: `Fizik/mikro-kazanimlar/FIZ.10.3.4-esdeger-direnc.md` dosyasındaki adımlar; kodlama, Bilgi/Beceri ve işlem türü ölçütü: `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Fiz05YG0017 | Yükler arası uzaklık iki katına çıkınca elektriksel kuvvet yarıya iner. |
| Fiz05YG0018 | Büyük yüklü cisim küçük yüklü cisme daha büyük elektriksel kuvvet uygular. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | İşlem türü | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|---|
| Fiz05MK0086 | Aynı cins yüklerin birbirini ittiğini belirtir. | Bilgi | Tanıma ve hatırlama | a | Hatırlama | – | – | ÇS |
| Fiz05MK0087 | Zıt cins yüklerin birbirini çektiğini belirtir. | Bilgi | Tanıma ve hatırlama | a | Hatırlama | – | – | ÇS |
| Fiz05MK0088 | Simülasyon verilerinden elektriksel kuvvetin yüklerin çarpımıyla doğru orantılı olduğunu keşfeder. | Bilgi | Çıkarım ve ilişkilendirme | a | Analiz | Fiz05MK0086; Fiz05MK0087 | – | ÇS, AU |
| Fiz05MK0089 | Simülasyon verilerinden elektriksel kuvvetin uzaklığın karesiyle ters orantılı olduğunu keşfeder. | Bilgi | Çıkarım ve ilişkilendirme | a | Analiz | Fiz05MK0086; Fiz05MK0087 | Fiz05YG0017 | ÇS, AU |
| Fiz05MK0090 | Keşfettiği ilişkiyi F = k·q₁·q₂/d² (Coulomb Yasası) modeli olarak ifade eder. | Beceri | Model kurma | a | Analiz | Fiz05MK0088; Fiz05MK0089 | – | AU |
| Fiz05MK0091 | Coulomb Yasası’ndan yük değiştiğinde kuvvetin nasıl değişeceğini genelleştirir. | Bilgi | Çıkarım ve ilişkilendirme | b | Analiz | Fiz05MK0090 | Fiz05YG0018 | ÇS |
| Fiz05MK0092 | Coulomb Yasası’ndan uzaklık değiştiğinde kuvvetin nasıl değişeceğini genelleştirir. | Bilgi | Çıkarım ve ilişkilendirme | b | Analiz | Fiz05MK0090 | Fiz05YG0017 | ÇS |

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi (rubrikle)

Özet: 7 mikro kazanım (7 yeni, 0 yeniden kullanım); yeni olanlardan 6 Bilgi, 1 Beceri.

---

## 3. Örnek ölçme maddesi

**Fiz05MK0091:** İki nokta yük arasındaki uzaklık iki katına çıkarılırsa aralarındaki elektriksel kuvvet ne olur?  
A) Yarıya iner (Fiz05YG0017) · B) Dörtte birine iner ✔ · C) İki katına çıkar · D) Değişmez

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
