# Mikro Kazanım Ayrıştırması: FİZ.10.2.1 (taslak v0.1)

> **FİZ.10.2.1** Kuvvet-yer değiştirme grafiği kullanılarak iş ile ilgili tümevarımsal akıl yürütebilme
> a) Kuvvet, yer değiştirme ve iş arasındaki ilişkiyi matematiksel olarak modeller
> b) Kuvvet, yer değiştirme ve iş arasındaki ilişki hakkında genelleme yapar
>
> Kaynak: https://tymm.meb.gov.tr/fizik-dersi/unite/108
> Sınıf ünitesi: Fiz10-U2 (Enerji) · Ana ünite: 04 Enerji
> Sınırlama (TYMM): TYMM bu çıktı için sınırlama belirtmemiştir.
> Ön öğrenmeler: iş ve enerji kavramları hakkında temel düzeyde bilgi (TYMM ön kabulü).

Yöntem: `FIZ.10.3.4-esdeger-direnc.md` dosyasındaki 8 adım; kodlama ve Bilgi/Beceri ölçütü: `KODLAMA.md`.

Tasarım notu: TYMM açılı kuvvet (cos θ) hesaplaması belirtmediği için hesaplamalar kuvvetin yer değiştirmeyle aynı doğrultuda olduğu durumlarla sınırlandırıldı; dik kuvvet yalnızca nitel olarak işlendi.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Fiz04YG0011 | Kuvvet uygulanan her durumda iş yapılır (ör. duvarı itmek). |
| Fiz04YG0012 | Harekete dik uygulanan kuvvet de iş yapar (ör. çantayı yatay taşımak). |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Fiz04MK0056 | Kuvvet uygulandığı hâlde yer değiştirme olmazsa fiziksel anlamda iş yapılmadığını açıklar. | Bilgi | a | Anlama | Fiz02MK0040 | Fiz04YG0011 | ÇS |
| Fiz04MK0057 | Sabit kuvvet için kuvvet-yer değiştirme grafiğini çizer. | Beceri | a | Uygulama | Fiz04MK0056 | – | AU |
| Fiz04MK0058 | Kuvvet-yer değiştirme grafiği altındaki alandan yapılan işi hesaplar. | Beceri | a | Uygulama | Fiz04MK0057 | – | ÇS |
| Fiz04MK0059 | Kuvvet yer değiştirmeyle aynı doğrultuda iken W = F·Δx modelini kullanarak işi hesaplar. | Beceri | a | Uygulama | Fiz04MK0058 | – | ÇS |
| Fiz04MK0060 | Yer değiştirmeye dik kuvvetin iş yapmadığı sonucunu çıkarır. | Bilgi | b | Analiz | Fiz04MK0059; Fiz02MK0023 | Fiz04YG0012 | ÇS |
| Fiz04MK0061 | Değişken kuvvetlerde de yapılan işin kuvvet-yer değiştirme grafiği altındaki alana eşit olduğu genellemesini yapar. | Bilgi | b | Analiz | Fiz04MK0058 | – | AU |

> 2026-10-01: Tek ölçülebilir hedef taramasıyla güncellendi (bir MK = bir soruyla tamamı ölçülebilen tek hedef). Tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 6 mikro kazanım (6 yeni, 0 yeniden kullanım); yeni olanlardan 3 Bilgi, 3 Beceri.

---

## 3. Örnek ölçme maddeleri

**Fiz04MK0056:** Hangisinde fiziksel anlamda iş yapılır?  
A) Duvarı 5 dakika itmek (Fiz04YG0011) · B) Kutuyu yerden masaya kaldırmak ✔ · C) Çantayı elde sabit tutmak · D) Yatay yolda çantayı taşımak (Fiz04YG0012)

**Fiz04MK0061:** Kuvvet-yer değiştirme grafiği 0 m'de 0 N'dan 4 m'de 20 N'a doğrusal artıyor. Yapılan iş kaç J'dür? Nasıl bulduğunuzu açıklayın. (Beklenen: üçgenin alanı, 40 J.)

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
