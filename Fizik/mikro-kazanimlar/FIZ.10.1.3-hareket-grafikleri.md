# Mikro Kazanım Ayrıştırması: FİZ.10.1.3 (taslak v0.1)

> **FİZ.10.1.3** Yatay doğrultuda sabit ivmeyle hareket eden cisimlerin hareket grafiklerinden elde edilen matematiksel modelleri yorumlayabilme
> a) Grafikleri inceler
> b) Grafikleri birbirine dönüştürerek matematiksel modellere ulaşır
> c) Grafikler ve matematiksel modeller arasındaki ilişkiyi kendi cümleleriyle ifade eder
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
| Fiz02YG0010 | Konum-zaman grafiği cismin izlediği yolun (yörüngenin) resmidir. |
| Fiz02YG0015 | Hız-zaman grafiğinde doğrunun aşağı doğru inmesi cismin geri gittiğini gösterir. |
| Fiz02YG0016 | İvme-zaman grafiği altındaki alan yer değiştirmeyi verir. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Fiz02MK0059 | Hız-zaman grafiği altındaki alandan yer değiştirmeyi hesaplar. | Beceri | b | Uygulama | Fiz02MK0058 | – | ÇS |
| Fiz02MK0071 | Sabit ivmeli hareketin konum-zaman grafiğini (parabol) şeklinden tanır. | Bilgi | a | Hatırlama | Fiz02MK0060; Fiz02MK0068 | Fiz02YG0010 | ÇS |
| Fiz02MK0072 | Sabit ivmeli hareketin hız-zaman grafiğini (eğik doğru) şeklinden tanır. | Bilgi | a | Hatırlama | Fiz02MK0058; Fiz02MK0068 | – | ÇS |
| Fiz02MK0073 | Sabit ivmeli hareketin ivme-zaman grafiğini (yatay doğru) şeklinden tanır. | Bilgi | a | Hatırlama | Fiz02MK0068 | – | ÇS |
| Fiz02MK0074 | Hız-zaman grafiğinden hareketin hızlanan ya da yavaşlayan olduğunu belirler. | Beceri | a | Analiz | Fiz02MK0069; Fiz02MK0070 | – | ÇS |
| Fiz02MK0075 | Hız-zaman grafiğinden cismin yön değiştirdiği anı belirler. | Beceri | a | Analiz | Fiz02MK0058; Fiz02MK0041 | Fiz02YG0015 | ÇS |
| Fiz02MK0076 | Hız-zaman grafiğinin eğiminden ivmeyi bulur. | Beceri | b | Uygulama | Fiz02MK0064; Fiz02MK0057 | – | ÇS |
| Fiz02MK0077 | İvme-zaman grafiği altındaki alandan hız değişimini bulur. | Beceri | b | Uygulama | Fiz02MK0076 | Fiz02YG0016 | ÇS |
| Fiz02MK0078 | Hız-zaman grafiğini ivme-zaman grafiğine dönüştürür. | Beceri | b | Uygulama | Fiz02MK0076 | – | AU |
| Fiz02MK0079 | Hız-zaman grafiğinden konum-zaman grafiğinin şeklini çizer. | Beceri | b | Analiz | Fiz02MK0059; Fiz02MK0071; Fiz02MK0072 | Fiz02YG0010 | AU |
| Fiz02MK0080 | Grafiklerden v = v₀ + a·t modeline ulaşır. | Beceri | b | Analiz | Fiz02MK0076 | – | AU |
| Fiz02MK0081 | Grafiklerden Δx = v₀·t + ½·a·t² modeline ulaşır. | Beceri | b | Analiz | Fiz02MK0076; Fiz02MK0059 | – | AU |
| Fiz02MK0082 | Grafik eğiminin matematiksel modeldeki karşılığını açıklar. | Bilgi | c | Analiz | Fiz02MK0080 | – | AU |
| Fiz02MK0083 | Grafik altındaki alanın matematiksel modeldeki karşılığını açıklar. | Bilgi | c | Analiz | Fiz02MK0081 | Fiz02YG0016 | AU |

> 2026-10-01: Tek ölçülebilir hedef taramasıyla güncellendi (bir MK = bir soruyla tamamı ölçülebilen tek hedef). Tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)
*(yeniden kullanım)*: Bu mikro kazanım daha önce başka bir çıktı için yazıldı; yeniden yazılmadı, bu çıktıya eşlendi.

Özet: 9 mikro kazanım (8 yeni, 1 yeniden kullanım); yeni olanlardan 2 Bilgi, 6 Beceri.

---

## 3. Örnek ölçme maddeleri

**Fiz02MK0074:** Hız-zaman grafiği (0 s, +12 m/s) ile (6 s, 0 m/s) arasında doğru olan cisim için hangisi doğrudur?  
A) Cisim geri gidiyor (Fiz02YG0015) · B) Cisim ileri yönde yavaşlıyor ✔ · C) Cisim duruyor · D) Cisim hızlanıyor

**Fiz02MK0059:** Aynı grafikte 0–6 s aralığında yer değiştirme kaç metredir?  
A) 72 · B) 36 ✔ · C) 12 · D) 2

**Fiz02MK0077:** İvme-zaman grafiği 0–5 s aralığında 2 m/s² değerinde yatay doğrudur. Bu aralıktaki hız değişimi kaç m/s'dir?  
A) 10 ✔ · B) 25 · C) "10 m yer değiştirme" (Fiz02YG0016) · D) 2,5

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
