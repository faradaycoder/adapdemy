# Mikro Kazanım Ayrıştırması: MAT.8.6.2 (taslak v0.1)

> **MAT.8.6.2** Başkaları tarafından oluşturulan veriye dayalı istatistiksel sonuçları tartışabilme
> a) İstatistiksel temellendirme yapar
> b) Hata ya da yanlılık tespit eder
> c) Sonuçları çürütür ya da kabul eder
>
> Kaynak: https://tymm.meb.gov.tr/ortaokul-matematik-dersi/unite/477
> Sınıf teması: Mat08-T6 (İstatistiksel Araştırma Süreci) · Ana tema: 06 İstatistiksel Araştırma Süreci
> Sınırlama (TYMM): Veri setinde bilinmeyen verinin bulunması üzerine merkezî eğilim ya da yayılım ölçülerinin hesaplanmasına yer verilmez. Özetleme: aritmetik ortalama, ortanca, tepe değer, açıklık, ortalama mutlak sapma; görselleştirme: sütun, nokta, çizgi grafiği.
> Ön öğrenmeler: araştırma sürecinin adımlarını takip etme, veri özetleme hesaplamaları, nicel veriyi yorumlama ve veriye dayalı karar verme (TYMM temel kabulü).

Yöntem: fizikle aynı 8 adım (`Fizik/mikro-kazanimlar/FIZ.10.3.4-esdeger-direnc.md`); kodlama ve Bilgi/Beceri ölçütü: EVALORA kökündeki `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Mat06YG0006 | Ortalamaları eşit olan iki veri grubu aynı özelliktedir; yayılım önemsizdir. |
| Mat06YG0001 | Küçük ya da evreni temsil etmeyen bir örneklemden evren hakkında kesin sonuç çıkarılabilir. |
| Mat06YG0004 | Grafikte dikey eksenin sıfırdan başlamaması ya da ölçeğin değiştirilmesi yorumu etkilemez. |
| Mat06YG0007 | Aritmetik ortalama, uç değer olsa bile veriyi her zaman en iyi temsil eden ölçüdür. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Mat06MK0021 | Örneklemin küçük olmasından kaynaklanan yanlılığı tespit eder. | Beceri | b | Analiz | Mat06MK0004 | Mat06YG0001 | ÇS, AU |
| Mat06MK0022 | Örneklemin evreni temsil etmemesinden kaynaklanan yanlılığı tespit eder. | Beceri | b | Analiz | Mat06MK0004 | Mat06YG0001 | ÇS, AU |
| Mat06MK0023 | Gönüllülerden oluşan örneklemin yanlılığını tespit eder. | Beceri | b | Analiz | Mat06MK0004 | – | ÇS, AU |
| Mat06MK0024 | Eksen başlangıcı nedeniyle yanıltıcı olan grafikleri tespit eder. | Beceri | b | Analiz | Mat06MK0014 | Mat06YG0004 | ÇS |
| Mat06MK0025 | Ölçek nedeniyle yanıltıcı olan grafikleri tespit eder. | Beceri | b | Analiz | Mat06MK0014 | Mat06YG0004 | ÇS |
| Mat06MK0026 | Eksik kategori nedeniyle yanıltıcı olan grafikleri tespit eder. | Beceri | b | Analiz | Mat06MK0014; Mat06MK0013 | – | ÇS |
| Mat06MK0027 | Tespitlerine dayanarak istatistiksel sonucu gerekçesiyle kabul eder ya da çürütür. | Beceri | c | Değerlendirme | Mat06MK0021; Mat06MK0022; Mat06MK0023; Mat06MK0024; Mat06MK0025; Mat06MK0026 | – | AU, PG |
| Mat06MK0038 | Başkalarının ulaştığı istatistiksel sonucun hangi veriye dayandığını belirler. | Beceri | a | Analiz | Mat06MK0007 | – | AU |
| Mat06MK0039 | Başkalarının ulaştığı sonucun hangi örnekleme dayandığını belirler. | Beceri | a | Analiz | Mat06MK0004 | – | AU |
| Mat06MK0040 | Başkalarının ulaştığı sonucun hangi özetleme ölçüsüne dayandığını belirler. | Beceri | a | Analiz | Mat06MK0031; Mat06MK0033; Mat06MK0034 | – | AU |
| Mat06MK0041 | Sonucu verinin merkezine ilişkin bilgilerle temellendirir. | Beceri | a | Analiz | Mat06MK0036 | – | AU |
| Mat06MK0042 | Sonucu verinin yayılımına ilişkin bilgilerle temellendirir. | Beceri | a | Analiz | Mat06MK0037 | Mat06YG0006 | AU |
| Mat06MK0045 | Uygun olmayan özetleme ölçüsü seçimini (ör. uç değerli veride ortalama) tespit eder. | Beceri | b | Analiz | Mat06MK0044 | Mat06YG0007 | ÇS |

> 2026-10-01: Tek ölçülebilir hedef bölmesi ve yeniden numaralama sonrası tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 6 mikro kazanım (6 yeni, 0 yeniden kullanım); yeni olanlardan 0 Bilgi, 6 Beceri.

---

## 3. Örnek ölçme maddeleri

**Mat06MK0024:** Dikey ekseni 95'ten başlayan bir sütun grafiğinde A markasının satışı (98) B'nin (96) üç katı gibi görünüyor. Bu grafik için hangisi doğrudur?  
A) A, B'nin 3 katı satmıştır (Mat06YG0004) · B) Eksen başlangıcı farkı abartmaktadır ✔ · C) Grafik doğrudur · D) B daha çok satmıştır

**Mat06MK0021:** "İnternet sitemizi ziyaret eden 50 kişiden 45'i ürünümüzü beğendi; Türkiye'nin %90'ı ürünümüzü seviyor." Bu sonucu değerlendirin. (Kabul eden yanıt Mat06YG0001 yanılgısını gösterir.)

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
