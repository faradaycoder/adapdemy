# Mikro Kazanım Ayrıştırması: MAT.11.3.5 (taslak v0.1)

> **MAT.11.3.5** f(x) = logₐx şeklinde tanımlı logaritmik referans fonksiyonun ve bundan türetilen logaritmik fonksiyonların nitel özelliklerine ilişkin matematiksel muhakeme yapabilme
> a–b) Nitel özellikleri belirler.
> c–ç) Türetilmiş fonksiyonlara dönüştürür.
> d–e) Varsayımda bulunur, geneller.
> f–ğ) Kontrol eder, önerme sunar, değerlendirir.
> h–ı) Doğrular ya da ispatlar.
>
> Kaynak: https://tymm.meb.gov.tr/matematik-dersi/unite/281
> Sınıf teması: Mat11-T3 (Nicelikler ve Değişimler) · Ana tema: 02 Cebirsel Düşünme ve Değişimler

Yöntem: `Fizik/mikro-kazanimlar/FIZ.10.3.4-esdeger-direnc.md` dosyasındaki adımlar; kodlama, Bilgi/Beceri ve işlem türü ölçütü: `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Mat02YG0036 | log(a + b) = log a + log b’dir. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | İşlem türü | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|---|
| Mat02MK0353 | Logaritmik referans fonksiyonun tanım kümesini belirler. | Bilgi | Yorumlama | a, b | Analiz | Mat02MK0351 | – | ÇS |
| Mat02MK0354 | Logaritmik referans fonksiyonun görüntü kümesini belirler. | Bilgi | Yorumlama | a, b | Analiz | Mat02MK0351 | – | ÇS |
| Mat02MK0355 | Logaritmik fonksiyonun sıfırlarını grafikten belirler. | Bilgi | Yorumlama | a, b | Analiz | Mat02MK0353 | – | ÇS |
| Mat02MK0356 | Logaritmik fonksiyonun işaretini grafikten belirler. | Bilgi | Yorumlama | a, b | Analiz | Mat02MK0353 | – | ÇS |
| Mat02MK0357 | Logaritmik fonksiyonun artan ve azalan olduğu aralıkları grafikten belirler. | Bilgi | Yorumlama | a, b | Analiz | Mat02MK0353 | – | ÇS |
| Mat02MK0358 | Logaritmik fonksiyonun en büyük ve en küçük değerlerini grafikten belirler. | Bilgi | Yorumlama | a, b | Analiz | Mat02MK0354 | – | ÇS |
| Mat02MK0359 | Logaritmik fonksiyonun bire bir olup olmadığını belirler. | Bilgi | Ayırt etme ve sınıflama | a, b | Analiz | Mat02MK0353 | – | ÇS |
| Mat02MK0360 | Logaritmik fonksiyonun örten olup olmadığını belirler. | Bilgi | Ayırt etme ve sınıflama | a, b | Analiz | Mat02MK0354 | – | ÇS |
| Mat02MK0361 | Logaritmik fonksiyonun tek ya da çift fonksiyon olup olmadığını belirler. | Bilgi | Ayırt etme ve sınıflama | a, b | Analiz | Mat02MK0353 | – | ÇS |
| Mat02MK0362 | Logaritmik referans fonksiyonun grafiğini yatay öteleyerek f(x ± r) biçimindeki fonksiyonları elde eder. | Beceri | Dönüştürme | c, ç | Uygulama | Mat02MK0353; Mat02MK0155 | – | ÇS, AU |
| Mat02MK0363 | Logaritmik referans fonksiyonun grafiğini düşey öteleyerek f(x) ± k biçimindeki fonksiyonları elde eder. | Beceri | Dönüştürme | c, ç | Uygulama | Mat02MK0354; Mat02MK0156 | – | ÇS, AU |
| Mat02MK0364 | Logaritmik referans fonksiyonun grafiğini a·f(x) ile dikey genişletir ya da daraltır. | Beceri | Dönüştürme | c, ç | Uygulama | Mat02MK0353; Mat02MK0157 | – | ÇS, AU |
| Mat02MK0365 | Logaritmik referans fonksiyonun grafiğini x eksenine göre yansıtır. | Beceri | Dönüştürme | c, ç | Uygulama | Mat02MK0353; Mat02MK0158 | – | ÇS, AU |
| Mat02MK0366 | Logaritmanın çarpım özelliğini kullanır. | Beceri | Kural uygulama | ç | Uygulama | Mat02MK0351; Mat01MK0204 | Mat02YG0036 | ÇS |
| Mat02MK0367 | Logaritmanın bölüm özelliğini kullanır. | Beceri | Kural uygulama | ç | Uygulama | Mat02MK0351; Mat01MK0205 | – | ÇS |
| Mat02MK0368 | Logaritmanın üs özelliğini kullanır. | Beceri | Kural uygulama | ç | Uygulama | Mat02MK0351; Mat01MK0206 | – | ÇS |
| Mat02MK0369 | Logaritmada taban değiştirme kuralını kullanır. | Beceri | Kural uygulama | ç | Uygulama | Mat02MK0368; Mat02MK0367 | – | ÇS |
| Mat02MK0370 | Onluk logaritmayı (log) kullanır. | Beceri | Kural uygulama | ç | Uygulama | Mat02MK0351 | – | ÇS |
| Mat02MK0371 | Doğal logaritmayı (ln) kullanır. | Beceri | Kural uygulama | ç | Uygulama | Mat02MK0351 | – | ÇS |
| Mat02MK0372 | Logaritmik fonksiyonların nitel özelliklerinin a parametresine nasıl bağlı olduğuna dair varsayımda bulunup genelleme yapar. | Bilgi | Çıkarım ve ilişkilendirme | d, e | Analiz | Mat02MK0364; Mat02MK0365; Mat02MK0355; Mat02MK0356; Mat02MK0357; Mat02MK0358 | – | AU |
| Mat02MK0373 | Logaritmik fonksiyonların nitel özelliklerinin r parametresine nasıl bağlı olduğuna dair varsayımda bulunup genelleme yapar. | Bilgi | Çıkarım ve ilişkilendirme | d, e | Analiz | Mat02MK0362; Mat02MK0355; Mat02MK0356; Mat02MK0357; Mat02MK0358 | – | AU |
| Mat02MK0374 | Logaritmik fonksiyonların nitel özelliklerinin k parametresine nasıl bağlı olduğuna dair varsayımda bulunup genelleme yapar. | Bilgi | Çıkarım ve ilişkilendirme | d, e | Analiz | Mat02MK0363; Mat02MK0355; Mat02MK0356; Mat02MK0357; Mat02MK0358 | – | AU |
| Mat02MK0375 | Logaritmik fonksiyonların a parametresine bağlı nitel özelliklerine ilişkin genellemelerini kontrol ederek önerme olarak ifade eder ve gerçek yaşamdaki kullanışlılığını değerlendirir. | Beceri | Sınama ve değerlendirme | f, g, ğ | Değerlendirme | Mat02MK0372 | – | AU |
| Mat02MK0376 | Logaritmik fonksiyonların r parametresine bağlı nitel özelliklerine ilişkin genellemelerini kontrol ederek önerme olarak ifade eder ve gerçek yaşamdaki kullanışlılığını değerlendirir. | Beceri | Sınama ve değerlendirme | f, g, ğ | Değerlendirme | Mat02MK0373 | – | AU |
| Mat02MK0377 | Logaritmik fonksiyonların k parametresine bağlı nitel özelliklerine ilişkin genellemelerini kontrol ederek önerme olarak ifade eder ve gerçek yaşamdaki kullanışlılığını değerlendirir. | Beceri | Sınama ve değerlendirme | f, g, ğ | Değerlendirme | Mat02MK0374 | – | AU |
| Mat02MK0378 | Logaritmik fonksiyonların a parametresine bağlı nitel özelliklerine ilişkin önermelerini grafiksel olarak doğrular ya da cebirsel olarak ispatlar. | Beceri | Model kurma | h, ı | Analiz | Mat02MK0375 | – | AU |
| Mat02MK0379 | Logaritmik fonksiyonların r parametresine bağlı nitel özelliklerine ilişkin önermelerini grafiksel olarak doğrular ya da cebirsel olarak ispatlar. | Beceri | Model kurma | h, ı | Analiz | Mat02MK0376 | – | AU |
| Mat02MK0380 | Logaritmik fonksiyonların k parametresine bağlı nitel özelliklerine ilişkin önermelerini grafiksel olarak doğrular ya da cebirsel olarak ispatlar. | Beceri | Model kurma | h, ı | Analiz | Mat02MK0377 | – | AU |

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi (rubrikle)

Özet: 28 mikro kazanım (28 yeni, 0 yeniden kullanım); yeni olanlardan 12 Bilgi, 16 Beceri.

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
