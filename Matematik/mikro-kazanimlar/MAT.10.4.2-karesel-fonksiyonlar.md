# Mikro Kazanım Ayrıştırması: MAT.10.4.2 (taslak v0.1)

> **MAT.10.4.2** Gerçek sayılarda f(x) = x² şeklinde tanımlı karesel referans fonksiyonun ve bundan türetilen karesel fonksiyonların nitel özelliklerine ilişkin matematiksel muhakeme yapabilme
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
| Mat02YG0025 | f(x) = −x² ile f(x) = (−x)² aynı fonksiyondur. |
| Mat02YG0026 | y = (x − 2)² + 3 parabolünün tepe noktası (−2, 3)’tür. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | İşlem türü | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|---|
| Mat02MK0203 | Karesel referans fonksiyonun tanım kümesini belirler. | Bilgi | Yorumlama | a, b | Analiz | Mat02MK0190; Mat01MK0044 | – | ÇS |
| Mat02MK0204 | Karesel referans fonksiyonun görüntü kümesini belirler. | Bilgi | Yorumlama | a, b | Analiz | Mat02MK0192; Mat01MK0044 | – | ÇS |
| Mat02MK0205 | Karesel fonksiyonun sıfırlarını grafikten belirler. | Bilgi | Yorumlama | a, b | Analiz | Mat02MK0203 | – | ÇS |
| Mat02MK0206 | Karesel fonksiyonun işaretini grafikten belirler. | Bilgi | Yorumlama | a, b | Analiz | Mat02MK0203 | – | ÇS |
| Mat02MK0207 | Karesel fonksiyonun artan ve azalan olduğu aralıkları grafikten belirler. | Bilgi | Yorumlama | a, b | Analiz | Mat02MK0203 | – | ÇS |
| Mat02MK0208 | Karesel fonksiyonun en büyük ve en küçük değerlerini grafikten belirler. | Bilgi | Yorumlama | a, b | Analiz | Mat02MK0204 | – | ÇS |
| Mat02MK0209 | Karesel fonksiyonun bire bir olup olmadığını belirler. | Bilgi | Ayırt etme ve sınıflama | a, b | Analiz | Mat02MK0203 | – | ÇS |
| Mat02MK0210 | Karesel fonksiyonun örten olup olmadığını belirler. | Bilgi | Ayırt etme ve sınıflama | a, b | Analiz | Mat02MK0204 | – | ÇS |
| Mat02MK0211 | Karesel fonksiyonun tek ya da çift fonksiyon olup olmadığını belirler. | Bilgi | Ayırt etme ve sınıflama | a, b | Analiz | Mat02MK0203 | – | ÇS |
| Mat02MK0212 | Karesel referans fonksiyonun grafiğini yatay öteleyerek f(x ± r) biçimindeki fonksiyonları elde eder. | Beceri | Dönüştürme | c, ç | Uygulama | Mat02MK0203; Mat02MK0155 | Mat02YG0025 | ÇS, AU |
| Mat02MK0213 | Karesel referans fonksiyonun grafiğini düşey öteleyerek f(x) ± k biçimindeki fonksiyonları elde eder. | Beceri | Dönüştürme | c, ç | Uygulama | Mat02MK0204; Mat02MK0156 | – | ÇS, AU |
| Mat02MK0214 | Karesel referans fonksiyonun grafiğini a·f(x) ile dikey genişletir ya da daraltır. | Beceri | Dönüştürme | c, ç | Uygulama | Mat02MK0203; Mat02MK0157 | – | ÇS, AU |
| Mat02MK0215 | Karesel referans fonksiyonun grafiğini x eksenine göre yansıtır. | Beceri | Dönüştürme | c, ç | Uygulama | Mat02MK0203; Mat02MK0158 | – | ÇS, AU |
| Mat02MK0216 | Karesel fonksiyonun tepe noktasını tam kareye tamamlayarak bulur. | Beceri | Kural uygulama | c | Uygulama | Mat01MK0303; Mat01MK0304 | Mat02YG0026 | ÇS |
| Mat02MK0217 | Karesel fonksiyonun simetri eksenini bulur. | Beceri | Kural uygulama | c | Uygulama | Mat02MK0216 | – | ÇS |
| Mat02MK0218 | Karesel fonksiyonun grafiğini tepe noktası ve sıfırlarından yararlanarak çizer. | Beceri | Dönüştürme | c | Uygulama | Mat02MK0216; Mat02MK0217 | – | AU |
| Mat02MK0219 | Karesel fonksiyonların nitel özelliklerinin a parametresine nasıl bağlı olduğuna dair varsayımda bulunup genelleme yapar. | Bilgi | Çıkarım ve ilişkilendirme | d, e | Analiz | Mat02MK0214; Mat02MK0215; Mat02MK0205; Mat02MK0206; Mat02MK0207; Mat02MK0208 | – | AU |
| Mat02MK0220 | Karesel fonksiyonların nitel özelliklerinin r parametresine nasıl bağlı olduğuna dair varsayımda bulunup genelleme yapar. | Bilgi | Çıkarım ve ilişkilendirme | d, e | Analiz | Mat02MK0212; Mat02MK0205; Mat02MK0206; Mat02MK0207; Mat02MK0208 | – | AU |
| Mat02MK0221 | Karesel fonksiyonların nitel özelliklerinin k parametresine nasıl bağlı olduğuna dair varsayımda bulunup genelleme yapar. | Bilgi | Çıkarım ve ilişkilendirme | d, e | Analiz | Mat02MK0213; Mat02MK0205; Mat02MK0206; Mat02MK0207; Mat02MK0208 | – | AU |
| Mat02MK0222 | Karesel fonksiyonların a parametresine bağlı nitel özelliklerine ilişkin genellemelerini kontrol ederek önerme olarak ifade eder ve gerçek yaşamdaki kullanışlılığını değerlendirir. | Beceri | Sınama ve değerlendirme | f, g, ğ | Değerlendirme | Mat02MK0219 | – | AU |
| Mat02MK0223 | Karesel fonksiyonların r parametresine bağlı nitel özelliklerine ilişkin genellemelerini kontrol ederek önerme olarak ifade eder ve gerçek yaşamdaki kullanışlılığını değerlendirir. | Beceri | Sınama ve değerlendirme | f, g, ğ | Değerlendirme | Mat02MK0220 | – | AU |
| Mat02MK0224 | Karesel fonksiyonların k parametresine bağlı nitel özelliklerine ilişkin genellemelerini kontrol ederek önerme olarak ifade eder ve gerçek yaşamdaki kullanışlılığını değerlendirir. | Beceri | Sınama ve değerlendirme | f, g, ğ | Değerlendirme | Mat02MK0221 | – | AU |
| Mat02MK0225 | Karesel fonksiyonların a parametresine bağlı nitel özelliklerine ilişkin önermelerini grafiksel olarak doğrular ya da cebirsel olarak ispatlar. | Beceri | Model kurma | h, ı | Analiz | Mat02MK0222 | – | AU |
| Mat02MK0226 | Karesel fonksiyonların r parametresine bağlı nitel özelliklerine ilişkin önermelerini grafiksel olarak doğrular ya da cebirsel olarak ispatlar. | Beceri | Model kurma | h, ı | Analiz | Mat02MK0223 | – | AU |
| Mat02MK0227 | Karesel fonksiyonların k parametresine bağlı nitel özelliklerine ilişkin önermelerini grafiksel olarak doğrular ya da cebirsel olarak ispatlar. | Beceri | Model kurma | h, ı | Analiz | Mat02MK0224 | – | AU |

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi (rubrikle)

Özet: 25 mikro kazanım (25 yeni, 0 yeniden kullanım); yeni olanlardan 12 Bilgi, 13 Beceri.

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
