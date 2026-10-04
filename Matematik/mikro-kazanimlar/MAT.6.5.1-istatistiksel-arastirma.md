# Mikro Kazanım Ayrıştırması: MAT.6.5.1 (taslak v0.1)

> **MAT.6.5.1** Kategorik veya nicel (kesikli) veri ile çalışabilme ve veriye dayalı karar verebilme
> a) Fark eder.
> b) Soru oluşturur.
> c) Plan yapar.
> ç) Veri toplar.
> d) Araç seçer (kök-yaprak, nokta grafiği; ortalama, ortanca, tepe değer, açıklık).
> e) Analiz eder.
> f) Gerekçe sunar.
> g) Değerlendirir, yeniden planlar.
>
> Kaynak: https://tymm.meb.gov.tr/ortaokul-matematik-dersi/unite/461
> Sınıf teması: Mat06-T5 (İstatistiksel Araştırma Süreci) · Ana tema: 06 İstatistiksel Araştırma Süreci

Yöntem: `Fizik/mikro-kazanimlar/FIZ.10.3.4-esdeger-direnc.md` dosyasındaki adımlar; kodlama, Bilgi/Beceri ve işlem türü ölçütü: `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Mat06YG0001 | Küçük ya da evreni temsil etmeyen bir örneklemden evren hakkında kesin sonuç çıkarılabilir. |
| Mat06YG0002 | Kategorik veri (ör. sevilen renk) için aritmetik ortalama hesaplanabilir. |
| Mat06YG0005 | Ortanca, veriler sıralanmadan ortadaki değerdir. |
| Mat06YG0006 | Ortalamaları eşit olan iki veri grubu aynı özelliktedir; yayılım önemsizdir. |

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
| Mat06MK0008 | Verinin kategorik mi nicel mi olduğunu belirler. | Bilgi | Ayırt etme ve sınıflama | ç | Anlama | Mat06MK0001 | Mat06YG0002 | ÇS |
| Mat06MK0009 | Nicel verinin kesikli mi sürekli mi olduğunu belirler. | Bilgi | Ayırt etme ve sınıflama | ç | Anlama | Mat06MK0008 | – | ÇS |
| Mat06MK0010 | Veri türüne uygun görselleştirme aracını (sütun, nokta, çizgi grafiği) seçip gerekçesini belirtir. | Beceri | Sınama ve değerlendirme | d | Değerlendirme | Mat06MK0008; Mat06MK0009 | – | AU |
| Mat06MK0011 | Veri türüne uygun özetleme aracını seçip gerekçesini belirtir. | Beceri | Sınama ve değerlendirme | d | Değerlendirme | Mat06MK0008; Mat06MK0009 | Mat06YG0002 | AU |
| Mat06MK0018 | Araştırma sonuçlarını veriye dayalı gerekçelerle sunar. | Beceri | Açıklama ve özetleme | f | Uygulama | Mat06MK0016; Mat06MK0017 | – | PG |
| Mat06MK0019 | Sonuçların araştırma sorusunu yanıtlama düzeyini değerlendirir. | Beceri | Sınama ve değerlendirme | g | Değerlendirme | Mat06MK0018 | Mat06YG0001 | PG |
| Mat06MK0020 | Gerektiğinde araştırma sürecini yeniden planlar. | Beceri | Sınama ve değerlendirme | g | Değerlendirme | Mat06MK0018 | – | PG |
| Mat06MK0028 | Nicel (kesikli) veriyi nokta grafiğiyle gösterir. | Beceri | Dönüştürme | d, e | Uygulama | Mat06MK0010 | – | ÇS, AU |
| Mat06MK0029 | Nicel veriyi kök-yaprak gösterimiyle düzenler. | Beceri | Dönüştürme | d, e | Uygulama | Mat06MK0010; Mat06MK0011 | – | ÇS |
| Mat06MK0030 | Nicel verinin açıklığını en büyük ve en küçük değer arasındaki fark olarak hesaplar. | Beceri | Kural uygulama | e | Uygulama | Mat06MK0008 | – | ÇS |
| Mat06MK0031 | Tek sayıda veride ortancayı bulur. | Beceri | Kural uygulama | e | Uygulama | Mat06MK0008 | Mat06YG0005 | ÇS |
| Mat06MK0032 | Çift sayıda veride ortancayı iki ortadaki değerin ortalaması olarak bulur. | Beceri | Kural uygulama | e | Uygulama | Mat06MK0031; Mat01MK0109 | Mat06YG0005 | ÇS |
| Mat06MK0033 | Nicel verinin aritmetik ortalamasını hesaplar. | Beceri | Kural uygulama | e | Uygulama | Mat06MK0008; Mat01MK0109 | – | ÇS |
| Mat06MK0034 | Nicel veride tepe değeri belirler. | Beceri | Kural uygulama | e | Uygulama | Mat06MK0008 | – | ÇS |
| Mat06MK0035 | Veriyi seçtiği grafikle görselleştirir. | Beceri | Yorumlama | e | Analiz | Mat06MK0010; Mat06MK0028; Mat06MK0029 | – | AU, PG |
| Mat06MK0036 | Grafikten dağılımın merkezini yorumlar. | Beceri | Yorumlama | e | Analiz | Mat06MK0028; Mat06MK0031; Mat06MK0033 | – | AU, PG |
| Mat06MK0037 | Grafikten dağılımın yayılımını yorumlar. | Beceri | Yorumlama | e | Analiz | Mat06MK0028; Mat06MK0030 | Mat06YG0006 | AU, PG |

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi (rubrikle)

Özet: 24 mikro kazanım (10 yeni, 14 yeniden kullanım); yeni olanlardan 0 Bilgi, 10 Beceri.

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
