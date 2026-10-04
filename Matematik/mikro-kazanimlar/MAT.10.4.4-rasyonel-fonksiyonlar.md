# Mikro Kazanım Ayrıştırması: MAT.10.4.4 (taslak v0.1)

> **MAT.10.4.4** Gerçek sayılarda f(x) = 1/x şeklinde tanımlı rasyonel referans fonksiyonun ve bundan türetilen rasyonel fonksiyonların nitel özelliklerine ilişkin matematiksel muhakeme yapabilme
> a–b) Nitel özellikleri belirler.
> c–ç) Türetilmiş fonksiyonlara dönüştürür.
> d–e) Varsayımda bulunur, geneller.
> f–ğ) Kontrol eder, önerme sunar, değerlendirir.
> h–ı) Doğrular ya da ispatlar.
>
> Kaynak: https://tymm.meb.gov.tr/matematik-dersi/unite/250
> Sınıf teması: Mat10-T4 (Nicelikler ve Değişimler) · Ana tema: 02 Cebirsel Düşünme ve Değişimler

Yöntem: `Fizik/mikro-kazanimlar/FIZ.10.3.4-esdeger-direnc.md` dosyasındaki adımlar; kodlama, Bilgi/Beceri ve işlem türü ölçütü: `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Mat02YG0028 | f(x) = 1/x fonksiyonu x = 0 için 0 değerini alır. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | İşlem türü | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|---|
| Mat02MK0251 | Rasyonel referans fonksiyonun tanım kümesini belirler. | Bilgi | Yorumlama | a, b | Analiz | Mat02MK0196 | – | ÇS |
| Mat02MK0252 | Rasyonel referans fonksiyonun görüntü kümesini belirler. | Bilgi | Yorumlama | a, b | Analiz | Mat02MK0192 | – | ÇS |
| Mat02MK0253 | Rasyonel fonksiyonun sıfırlarını grafikten belirler. | Bilgi | Yorumlama | a, b | Analiz | Mat02MK0251 | – | ÇS |
| Mat02MK0254 | Rasyonel fonksiyonun işaretini grafikten belirler. | Bilgi | Yorumlama | a, b | Analiz | Mat02MK0251 | – | ÇS |
| Mat02MK0255 | Rasyonel fonksiyonun artan ve azalan olduğu aralıkları grafikten belirler. | Bilgi | Yorumlama | a, b | Analiz | Mat02MK0251 | – | ÇS |
| Mat02MK0256 | Rasyonel fonksiyonun en büyük ve en küçük değerlerini grafikten belirler. | Bilgi | Yorumlama | a, b | Analiz | Mat02MK0252 | – | ÇS |
| Mat02MK0257 | Rasyonel fonksiyonun bire bir olup olmadığını belirler. | Bilgi | Ayırt etme ve sınıflama | a, b | Analiz | Mat02MK0251 | – | ÇS |
| Mat02MK0258 | Rasyonel fonksiyonun örten olup olmadığını belirler. | Bilgi | Ayırt etme ve sınıflama | a, b | Analiz | Mat02MK0252 | – | ÇS |
| Mat02MK0259 | Rasyonel fonksiyonun tek ya da çift fonksiyon olup olmadığını belirler. | Bilgi | Ayırt etme ve sınıflama | a, b | Analiz | Mat02MK0251 | – | ÇS |
| Mat02MK0260 | Rasyonel referans fonksiyonun grafiğini yatay öteleyerek f(x ± r) biçimindeki fonksiyonları elde eder. | Beceri | Dönüştürme | c, ç | Uygulama | Mat02MK0251; Mat02MK0155 | Mat02YG0028 | ÇS, AU |
| Mat02MK0261 | Rasyonel referans fonksiyonun grafiğini düşey öteleyerek f(x) ± k biçimindeki fonksiyonları elde eder. | Beceri | Dönüştürme | c, ç | Uygulama | Mat02MK0252; Mat02MK0156 | – | ÇS, AU |
| Mat02MK0262 | Rasyonel referans fonksiyonun grafiğini a·f(x) ile dikey genişletir ya da daraltır. | Beceri | Dönüştürme | c, ç | Uygulama | Mat02MK0251; Mat02MK0157 | – | ÇS, AU |
| Mat02MK0263 | Rasyonel referans fonksiyonun grafiğini x eksenine göre yansıtır. | Beceri | Dönüştürme | c, ç | Uygulama | Mat02MK0251; Mat02MK0158 | – | ÇS, AU |
| Mat02MK0264 | f(x) = a / (x − r) + k fonksiyonunun düşey asimptotunu belirler. | Bilgi | Çıkarım ve ilişkilendirme | c | Analiz | Mat02MK0260; Mat02MK0251 | – | ÇS |
| Mat02MK0265 | f(x) = a / (x − r) + k fonksiyonunun yatay asimptotunu belirler. | Bilgi | Çıkarım ve ilişkilendirme | c | Analiz | Mat02MK0261; Mat02MK0252 | – | ÇS |
| Mat02MK0266 | Rasyonel fonksiyonun grafiğini asimptotlarından yararlanarak çizer. | Beceri | Dönüştürme | c | Uygulama | Mat02MK0264; Mat02MK0265 | – | AU |
| Mat02MK0267 | Rasyonel fonksiyonların nitel özelliklerinin a parametresine nasıl bağlı olduğuna dair varsayımda bulunup genelleme yapar. | Bilgi | Çıkarım ve ilişkilendirme | d, e | Analiz | Mat02MK0262; Mat02MK0263; Mat02MK0253; Mat02MK0254; Mat02MK0255; Mat02MK0256 | – | AU |
| Mat02MK0268 | Rasyonel fonksiyonların nitel özelliklerinin r parametresine nasıl bağlı olduğuna dair varsayımda bulunup genelleme yapar. | Bilgi | Çıkarım ve ilişkilendirme | d, e | Analiz | Mat02MK0260; Mat02MK0253; Mat02MK0254; Mat02MK0255; Mat02MK0256 | – | AU |
| Mat02MK0269 | Rasyonel fonksiyonların nitel özelliklerinin k parametresine nasıl bağlı olduğuna dair varsayımda bulunup genelleme yapar. | Bilgi | Çıkarım ve ilişkilendirme | d, e | Analiz | Mat02MK0261; Mat02MK0253; Mat02MK0254; Mat02MK0255; Mat02MK0256 | – | AU |
| Mat02MK0270 | Rasyonel fonksiyonların a parametresine bağlı nitel özelliklerine ilişkin genellemelerini kontrol ederek önerme olarak ifade eder ve gerçek yaşamdaki kullanışlılığını değerlendirir. | Beceri | Sınama ve değerlendirme | f, g, ğ | Değerlendirme | Mat02MK0267 | – | AU |
| Mat02MK0271 | Rasyonel fonksiyonların r parametresine bağlı nitel özelliklerine ilişkin genellemelerini kontrol ederek önerme olarak ifade eder ve gerçek yaşamdaki kullanışlılığını değerlendirir. | Beceri | Sınama ve değerlendirme | f, g, ğ | Değerlendirme | Mat02MK0268 | – | AU |
| Mat02MK0272 | Rasyonel fonksiyonların k parametresine bağlı nitel özelliklerine ilişkin genellemelerini kontrol ederek önerme olarak ifade eder ve gerçek yaşamdaki kullanışlılığını değerlendirir. | Beceri | Sınama ve değerlendirme | f, g, ğ | Değerlendirme | Mat02MK0269 | – | AU |
| Mat02MK0273 | Rasyonel fonksiyonların a parametresine bağlı nitel özelliklerine ilişkin önermelerini grafiksel olarak doğrular ya da cebirsel olarak ispatlar. | Beceri | Model kurma | h, ı | Analiz | Mat02MK0270 | – | AU |
| Mat02MK0274 | Rasyonel fonksiyonların r parametresine bağlı nitel özelliklerine ilişkin önermelerini grafiksel olarak doğrular ya da cebirsel olarak ispatlar. | Beceri | Model kurma | h, ı | Analiz | Mat02MK0271 | – | AU |
| Mat02MK0275 | Rasyonel fonksiyonların k parametresine bağlı nitel özelliklerine ilişkin önermelerini grafiksel olarak doğrular ya da cebirsel olarak ispatlar. | Beceri | Model kurma | h, ı | Analiz | Mat02MK0272 | – | AU |

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi (rubrikle)

Özet: 25 mikro kazanım (25 yeni, 0 yeniden kullanım); yeni olanlardan 14 Bilgi, 11 Beceri.

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
