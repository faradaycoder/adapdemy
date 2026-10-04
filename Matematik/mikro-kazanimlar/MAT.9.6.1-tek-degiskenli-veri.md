# Mikro Kazanım Ayrıştırması: MAT.9.6.1 (taslak v0.1)

> **MAT.9.6.1** Tek nicel değişkenli veri dağılımları ile çalışabilme ve tek nicel değişken içeren veriye dayalı karar verebilme
> a) Durumları belirler.
> b) Soru oluşturur.
> c) Plan yapar.
> ç) Veriyi hazırlar.
> d) Araç seçer (nokta grafiği, histogram, kutu grafiği; ortalama, ortanca, tepe değer, açıklık, çeyrekler açıklığı).
> e) Analiz eder.
> f) Sonuç çıkarır.
> g) Değerlendirir.
>
> Kaynak: https://tymm.meb.gov.tr/matematik-dersi/unite/91
> Sınıf teması: Mat09-T6 (İstatistiksel Araştırma Süreci) · Ana tema: 06 İstatistiksel Araştırma Süreci

Yöntem: `Fizik/mikro-kazanimlar/FIZ.10.3.4-esdeger-direnc.md` dosyasındaki adımlar; kodlama, Bilgi/Beceri ve işlem türü ölçütü: `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Mat06YG0001 | Küçük ya da evreni temsil etmeyen bir örneklemden evren hakkında kesin sonuç çıkarılabilir. |
| Mat06YG0002 | Kategorik veri (ör. sevilen renk) için aritmetik ortalama hesaplanabilir. |
| Mat06YG0006 | Ortalamaları eşit olan iki veri grubu aynı özelliktedir; yayılım önemsizdir. |
| Mat06YG0008 | Kutu grafiğinde kutunun uzunluğu veri sayısını gösterir. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | İşlem türü | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|---|
| Mat06MK0001 | Bir durumun değişkenlik içeren veri gerektirdiği için istatistiksel araştırma gerektirip gerektirmediğini fark eder. | Bilgi | Ayırt etme ve sınıflama | a | Anlama | – | – | ÇS |
| Mat06MK0002 | Betimlemeye yönelik istatistiksel araştırma sorusu oluşturur. | Beceri | Çıkarım ve ilişkilendirme | b | Uygulama | Mat06MK0001 | – | PG |
| Mat06MK0003 | İki grubu karşılaştırmaya yönelik istatistiksel araştırma sorusu oluşturur. | Beceri | Çıkarım ve ilişkilendirme | b | Uygulama | Mat06MK0001 | – | PG |
| Mat06MK0004 | Araştırmanın evrenini ve örneklemini belirler. | Beceri | Üretme ve tasarım | c | Uygulama | Mat06MK0002; Mat06MK0003 | Mat06YG0001 | PG |
| Mat06MK0005 | Veri toplama planı yapar. | Beceri | Üretme ve tasarım | c | Uygulama | Mat06MK0002; Mat06MK0003 | – | PG |
| Mat06MK0006 | Anket sorusu hazırlayarak veri toplar. | Beceri | Gözlem ve kayıt | ç | Uygulama | Mat06MK0005 | – | PG |
| Mat06MK0007 | Araştırma sorusuna uygun hazır veriye ulaşır. | Beceri | Gözlem ve kayıt | ç | Uygulama | Mat06MK0002; Mat06MK0003 | – | PG |
| Mat06MK0010 | Veri türüne uygun görselleştirme aracını (sütun, nokta, çizgi grafiği) seçip gerekçesini belirtir. | Beceri | Sınama ve değerlendirme | d | Değerlendirme | Mat06MK0008; Mat06MK0009 | – | AU |
| Mat06MK0011 | Veri türüne uygun özetleme aracını seçip gerekçesini belirtir. | Beceri | Sınama ve değerlendirme | d | Değerlendirme | Mat06MK0008; Mat06MK0009 | Mat06YG0002 | AU |
| Mat06MK0019 | Sonuçların araştırma sorusunu yanıtlama düzeyini değerlendirir. | Beceri | Sınama ve değerlendirme | g | Değerlendirme | Mat06MK0018 | Mat06YG0001 | PG |
| Mat06MK0020 | Gerektiğinde araştırma sürecini yeniden planlar. | Beceri | Sınama ve değerlendirme | g | Değerlendirme | Mat06MK0018 | – | PG |
| Mat06MK0034 | Nicel veride tepe değeri belirler. | Beceri | Kural uygulama | d | Uygulama | Mat06MK0008 | – | ÇS |
| Mat06MK0035 | Veriyi seçtiği grafikle görselleştirir. | Beceri | Yorumlama | e | Analiz | Mat06MK0010; Mat06MK0028; Mat06MK0029 | – | AU, PG |
| Mat06MK0036 | Grafikten dağılımın merkezini yorumlar. | Beceri | Yorumlama | e | Analiz | Mat06MK0028; Mat06MK0031; Mat06MK0033 | – | AU, PG |
| Mat06MK0037 | Grafikten dağılımın yayılımını yorumlar. | Beceri | Yorumlama | e | Analiz | Mat06MK0028; Mat06MK0030 | Mat06YG0006 | AU, PG |
| Mat06MK0043 | Nicel veride ortalama mutlak sapmayı hesaplar. | Beceri | Kural uygulama | d | Uygulama | Mat06MK0033; Mat01MK0137 | Mat06YG0006 | ÇS |
| Mat06MK0046 | Nicel veriyi histogramla gösterir. | Beceri | Dönüştürme | d | Uygulama | Mat06MK0009; Mat06MK0014 | – | ÇS, AU |
| Mat06MK0047 | Nicel verinin çeyreklerini hesaplar. | Beceri | Kural uygulama | d, e | Uygulama | Mat06MK0031; Mat06MK0032 | – | ÇS |
| Mat06MK0048 | Nicel verinin çeyrekler açıklığını hesaplar. | Beceri | Kural uygulama | d, e | Uygulama | Mat06MK0047 | – | ÇS |
| Mat06MK0049 | Nicel veriyi beş sayı özetiyle kutu grafiğinde gösterir. | Beceri | Dönüştürme | d | Uygulama | Mat06MK0047 | Mat06YG0008 | ÇS, AU |
| Mat06MK0050 | Dağılımın biçimini (simetrik, çarpık) yorumlar. | Bilgi | Yorumlama | f | Analiz | Mat06MK0046; Mat06MK0049; Mat06MK0036; Mat06MK0037 | – | AU |
| Mat06MK0051 | Dağılımın merkezini yorumlar. | Bilgi | Yorumlama | f | Analiz | Mat06MK0046; Mat06MK0049; Mat06MK0036 | – | AU |
| Mat06MK0052 | Dağılımın yayılımını yorumlayarak verinin arasına ve ötesine ilişkin sonuç çıkarır. | Bilgi | Yorumlama | f | Analiz | Mat06MK0046; Mat06MK0049; Mat06MK0037 | – | AU |

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi (rubrikle)

Özet: 23 mikro kazanım (7 yeni, 16 yeniden kullanım); yeni olanlardan 3 Bilgi, 4 Beceri.

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
