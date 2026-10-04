# Mikro Kazanım Ayrıştırması: MAT.8.6.1 (taslak v0.1)

> **MAT.8.6.1** Kategorik veya nicel veri ile çalışabilme ve veriye dayalı karar verebilme
> a) İstatistiksel araştırma gerektiren durumları fark eder
> b) Betimleme ya da karşılaştırma gerektiren araştırma soruları oluşturur
> c) Veriye ulaşmak için plan yapar
> ç) Anket soruları kullanarak veri toplar ya da hazır veriye ulaşır
> d) Veri görselleştirme ve özetleme araçlarını seçme gerekçelerini belirtir
> e) Toplanan veriyi uygun araçlarla analiz eder
> f) Araştırma sonuçlarına gerekçeler sunar
> g) Sonuçların soruya cevap verme düzeyini değerlendirip gerekirse süreci yeniden planlar
>
> Kaynak: https://tymm.meb.gov.tr/ortaokul-matematik-dersi/unite/477
> Sınıf teması: Mat08-T6 (İstatistiksel Araştırma Süreci) · Ana tema: 06 İstatistiksel Araştırma Süreci
> Sınırlama (TYMM): Veri setinde bilinmeyen verinin bulunması üzerine merkezî eğilim ya da yayılım ölçülerinin hesaplanmasına yer verilmez. Özetleme: aritmetik ortalama, ortanca, tepe değer, açıklık, ortalama mutlak sapma; görselleştirme: sütun, nokta, çizgi grafiği.
> Ön öğrenmeler: araştırma sürecinin adımlarını takip etme, veri özetleme hesaplamaları, nicel veriyi yorumlama ve veriye dayalı karar verme (TYMM temel kabulü).

Yöntem: fizikle aynı 8 adım (`Fizik/mikro-kazanimlar/FIZ.10.3.4-esdeger-direnc.md`); kodlama ve Bilgi/Beceri ölçütü: EVALORA kökündeki `KODLAMA.md`.

Tasarım notu: Araştırma süreci çıktısı olduğu için ağırlıklı ölçme performans görevi + rubriktir; hesaplama becerileri ayrıca ÇS ile ölçülür.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Mat06YG0001 | Küçük ya da evreni temsil etmeyen bir örneklemden evren hakkında kesin sonuç çıkarılabilir. |
| Mat06YG0002 | Kategorik veri (ör. sevilen renk) için aritmetik ortalama hesaplanabilir. |
| Mat06YG0006 | Ortalamaları eşit olan iki veri grubu aynı özelliktedir; yayılım önemsizdir. |
| Mat06YG0007 | Aritmetik ortalama, uç değer olsa bile veriyi her zaman en iyi temsil eden ölçüdür. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Mat06MK0001 | Bir durumun değişkenlik içeren veri gerektirdiği için istatistiksel araştırma gerektirip gerektirmediğini fark eder. | Bilgi | a | Anlama | – | – | ÇS |
| Mat06MK0002 | Betimlemeye yönelik istatistiksel araştırma sorusu oluşturur. | Beceri | b | Uygulama | Mat06MK0001 | – | PG |
| Mat06MK0003 | İki grubu karşılaştırmaya yönelik istatistiksel araştırma sorusu oluşturur. | Beceri | b | Uygulama | Mat06MK0001 | – | PG |
| Mat06MK0004 | Araştırmanın evrenini ve örneklemini belirler. | Beceri | c | Uygulama | Mat06MK0002; Mat06MK0003 | Mat06YG0001 | PG |
| Mat06MK0005 | Veri toplama planı yapar. | Beceri | c | Uygulama | Mat06MK0002; Mat06MK0003 | – | PG |
| Mat06MK0006 | Anket sorusu hazırlayarak veri toplar. | Beceri | ç | Uygulama | Mat06MK0005 | – | PG |
| Mat06MK0007 | Araştırma sorusuna uygun hazır veriye ulaşır. | Beceri | ç | Uygulama | Mat06MK0002; Mat06MK0003 | – | PG |
| Mat06MK0008 | Verinin kategorik mi nicel mi olduğunu belirler. | Bilgi | ç | Anlama | Mat06MK0001 | Mat06YG0002 | ÇS |
| Mat06MK0009 | Nicel verinin kesikli mi sürekli mi olduğunu belirler. | Bilgi | ç | Anlama | Mat06MK0008 | – | ÇS |
| Mat06MK0010 | Veri türüne uygun görselleştirme aracını (sütun, nokta, çizgi grafiği) seçip gerekçesini belirtir. | Beceri | d | Değerlendirme | Mat06MK0008; Mat06MK0009 | – | AU |
| Mat06MK0011 | Veri türüne uygun özetleme aracını seçip gerekçesini belirtir. | Beceri | d | Değerlendirme | Mat06MK0008; Mat06MK0009 | Mat06YG0002 | AU |
| Mat06MK0018 | Araştırma sonuçlarını veriye dayalı gerekçelerle sunar. | Beceri | f | Uygulama | Mat06MK0016; Mat06MK0017 | – | PG |
| Mat06MK0019 | Sonuçların araştırma sorusunu yanıtlama düzeyini değerlendirir. | Beceri | g | Değerlendirme | Mat06MK0018 | Mat06YG0001 | PG |
| Mat06MK0020 | Gerektiğinde araştırma sürecini yeniden planlar. | Beceri | g | Değerlendirme | Mat06MK0018 | – | PG |
| Mat06MK0034 | Nicel veride tepe değeri belirler. | Beceri | e | Uygulama | Mat06MK0008 | – | ÇS |
| Mat06MK0035 | Veriyi seçtiği grafikle görselleştirir. | Beceri | e | Analiz | Mat06MK0010; Mat06MK0028; Mat06MK0029 | – | AU, PG |
| Mat06MK0036 | Grafikten dağılımın merkezini yorumlar. | Beceri | e | Analiz | Mat06MK0028; Mat06MK0031; Mat06MK0033 | – | AU, PG |
| Mat06MK0037 | Grafikten dağılımın yayılımını yorumlar. | Beceri | e | Analiz | Mat06MK0028; Mat06MK0030 | Mat06YG0006 | AU, PG |
| Mat06MK0043 | Nicel veride ortalama mutlak sapmayı hesaplar. | Beceri | e | Uygulama | Mat06MK0033; Mat01MK0137 | Mat06YG0006 | ÇS |
| Mat06MK0044 | Uç değer içeren veride hangi merkezî eğilim ölçüsünün veriyi daha iyi temsil ettiğini belirler. | Bilgi | e | Analiz | Mat06MK0031; Mat06MK0033 | Mat06YG0007 | ÇS |

> 2026-10-01: Tek ölçülebilir hedef bölmesi ve yeniden numaralama sonrası tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 12 mikro kazanım (12 yeni, 0 yeniden kullanım); yeni olanlardan 3 Bilgi, 9 Beceri.

---

## 3. Örnek ölçme maddeleri

**Mat06MK0044:** Bir sınıftaki 6 öğrencinin haftalık cep harçlığı (TL): 100, 120, 110, 100, 130, 1000. Veriyi en iyi temsil eden ölçü hangisidir?  
A) Aritmetik ortalama (Mat06YG0007) · B) Ortanca ✔ · C) Açıklık · D) En büyük değer

**Mat06MK0019:** Performans görevi: "Okulumuzda öğrenciler günde kaç saat ekran başında?" araştırması. Rubrik: soru (b), plan ve örneklem (c), veri toplama (ç), araç seçimi gerekçesi (d), analiz (e), sonuç ve gerekçe (f), değerlendirme ve yeniden planlama (g); her ölçüt 1–4.

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
