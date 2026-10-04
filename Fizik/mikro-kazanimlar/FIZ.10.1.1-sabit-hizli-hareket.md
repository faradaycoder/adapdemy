# Mikro Kazanım Ayrıştırması: FİZ.10.1.1 (taslak v0.1)

> **FİZ.10.1.1** Yatay doğrultuda sabit hızlı hareket ile ilgili tümevarımsal akıl yürütebilme
> a) Konum, yer değiştirme, hız ve zaman değişkenlerine yönelik gözlemler yapar
> b) Hız, sürat, yer değiştirme ve alınan yol değişkenlerine ilişkin matematiksel model bulur
> c) Söz konusu değişkenlere ilişkin matematiksel modellerle genelleme yapar
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
| Fiz02YG0006 | Yer değiştirme ile alınan yol her zaman birbirine eşittir. |
| Fiz02YG0010 | Konum-zaman grafiği cismin izlediği yolun (yörüngenin) resmidir. |
| Fiz02YG0011 | Negatif hız, cismin yavaşladığını gösterir. |
| Fiz02YG0007 | Hız ile sürat aynı kavramdır; hızın yönü yoktur. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Fiz02MK0039 | Seçilen referans noktasına göre cismin konumunu işaretiyle (+/−) belirtir. | Beceri | a | Uygulama | Fiz02MK0036; Fiz02MK0037 | – | ÇS |
| Fiz02MK0040 | Yer değiştirmeyi (son konum − ilk konum) alınan yoldan ayırt eder. | Bilgi | a | Anlama | Fiz02MK0039; Fiz02MK0038 | Fiz02YG0006 | ÇS |
| Fiz02MK0041 | Hızın yönlü (vektörel) bir büyüklük olduğunu açıklar. | Bilgi | b | Anlama | Fiz02MK0040; Fiz02MK0013 | Fiz02YG0007 | ÇS |
| Fiz02MK0042 | Süratin yönsüz (skaler) bir büyüklük olduğunu açıklar. | Bilgi | b | Anlama | Fiz02MK0038; Fiz02MK0013 | – | ÇS |
| Fiz02MK0047 | Alınan yoldan ortalama sürati hesaplar. | Beceri | b | Uygulama | Fiz02MK0043 | – | ÇS |
| Fiz02MK0048 | Yer değiştirmeden ortalama hızı hesaplar. | Beceri | b | Uygulama | Fiz02MK0044 | Fiz02YG0007; Fiz02YG0006 | ÇS |
| Fiz02MK0055 | Sabit hızlı hareket deneyinde ya da simülasyonda konum-zaman verisi toplar ve tabloya kaydeder. | Beceri | a | Uygulama | Fiz02MK0039 | – | PG |
| Fiz02MK0056 | Konum-zaman tablosundan konum-zaman grafiğini çizer. | Beceri | b | Uygulama | Fiz02MK0055 | Fiz02YG0010 | AU, PG |
| Fiz02MK0057 | Konum-zaman grafiğinin eğiminden hızı (v = Δx / Δt) bulur. | Beceri | b | Uygulama | Fiz02MK0056; Fiz02MK0048 | Fiz02YG0011 | ÇS, AU |
| Fiz02MK0058 | Hız değerlerinden hız-zaman grafiğini çizer. | Beceri | b | Uygulama | Fiz02MK0057 | – | AU |
| Fiz02MK0059 | Hız-zaman grafiği altındaki alandan yer değiştirmeyi hesaplar. | Beceri | b | Uygulama | Fiz02MK0058 | – | ÇS |
| Fiz02MK0060 | Sabit hızlı harekette konum-zaman grafiğinin eğik doğru olduğu genellemesini yapar. | Bilgi | c | Analiz | Fiz02MK0056 | Fiz02YG0010 | ÇS, AU |
| Fiz02MK0061 | Sabit hızlı harekette hız-zaman grafiğinin zaman eksenine paralel doğru olduğu genellemesini yapar. | Bilgi | c | Analiz | Fiz02MK0058 | – | ÇS, AU |
| Fiz02MK0062 | x = x₀ + v·t modelini kullanarak cismin herhangi bir andaki konumunu hesaplar. | Beceri | c | Uygulama | Fiz02MK0057; Fiz02MK0060 | Fiz02YG0011 | ÇS |

> 2026-10-01: Tek ölçülebilir hedef taramasıyla güncellendi (bir MK = bir soruyla tamamı ölçülebilen tek hedef). Tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 11 mikro kazanım (11 yeni, 0 yeniden kullanım); yeni olanlardan 3 Bilgi, 8 Beceri.

---

## 3. Örnek ölçme maddeleri

**Fiz02MK0040:** Bir öğrenci 0 m'den +8 m'ye yürüyüp +3 m'ye geri dönüyor. Yer değiştirmesi ve aldığı yol kaçar metredir?  
A) 3; 3 (Fiz02YG0006) · B) 3; 13 ✔ · C) 13; 3 · D) 11; 13

**Fiz02MK0057:** Konum-zaman grafiği (0 s, 12 m) ve (4 s, 0 m) noktalarından geçen doğru olan cismin hızı kaç m/s'dir?  
A) +3 · B) −3 ✔ · C) 12 · D) "Cisim yavaşlıyor" (Fiz02YG0011)

**Fiz02MK0060:** Sabit hızla giden bir aracın konum-zaman ve hız-zaman grafiklerini taslak olarak çizip neden bu şekilde olduklarını açıklayın. (AU; grafiği yörünge gibi çizen yanıt Fiz02YG0010 yanılgısına işaret eder.)

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
