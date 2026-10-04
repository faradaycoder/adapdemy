# Mikro Kazanım Ayrıştırması: MAT.11.3.1 (taslak v0.1)

> **MAT.11.3.1** Trigonometrik referans fonksiyonların (sin x, cos x, tan x, cot x) nitel özellikleri ile bu fonksiyonlardan türetilen fonksiyonların nitel özelliklerine ilişkin matematiksel muhakeme yapabilme
> a–b) Nitel özellikleri belirler.
> c–ç) Türetilmiş fonksiyonlara dönüştürür.
> d–e) Varsayımda bulunur, geneller.
> f–ğ) Kontrol eder, önerme sunar, değerlendirir.
> h–ı) Doğrular ya da ispatlar.
>
> Kaynak: https://tymm.meb.gov.tr/matematik-dersi/unite/281
> Sınıf teması: Mat11-T3 (Nicelikler ve Değişimler) · Ana tema: 02 Cebirsel Düşünme ve Değişimler
> Sınırlama (TYMM): Açı ölçü birimleri radyan ve derecedir.

Yöntem: `Fizik/mikro-kazanimlar/FIZ.10.3.4-esdeger-direnc.md` dosyasındaki adımlar; kodlama, Bilgi/Beceri ve işlem türü ölçütü: `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Mat02YG0031 | π sayısı 180’e eşittir. |
| Mat02YG0032 | Trigonometrik oranlar her bölgede pozitiftir. |
| Mat02YG0033 | sin 2x fonksiyonunun periyodu 4π’dir. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | İşlem türü | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|---|
| Mat02MK0293 | Derece ile verilen açı ölçüsünü radyana dönüştürür. | Beceri | Kural uygulama | a | Uygulama | Mat04MK0104 | Mat02YG0031 | ÇS |
| Mat02MK0294 | Radyan ile verilen açı ölçüsünü dereceye dönüştürür. | Beceri | Kural uygulama | a | Uygulama | Mat04MK0104 | Mat02YG0031 | ÇS |
| Mat02MK0295 | Birim çemberde bir açının kosinüs değerini noktanın apsisi olarak tanımlar. | Bilgi | Tanıma ve hatırlama | a | Anlama | Mat03MK0167; Mat02MK0102 | – | ÇS |
| Mat02MK0296 | Birim çemberde bir açının sinüs değerini noktanın ordinatı olarak tanımlar. | Bilgi | Tanıma ve hatırlama | a | Anlama | Mat03MK0166; Mat02MK0102 | – | ÇS |
| Mat02MK0297 | Trigonometrik fonksiyonların bölgelere göre işaretlerini belirler. | Beceri | Kural uygulama | a | Uygulama | Mat02MK0295; Mat02MK0296; Mat02MK0103 | Mat02YG0032 | ÇS |
| Mat02MK0298 | Açıları indirgeme formülleriyle dar açıya indirger. | Beceri | Kural uygulama | a | Uygulama | Mat02MK0295; Mat02MK0296 | – | ÇS |
| Mat02MK0299 | Trigonometrik referans fonksiyonun tanım kümesini belirler. | Bilgi | Yorumlama | a, b | Analiz | Mat02MK0295; Mat02MK0296; Mat02MK0293; Mat02MK0190 | – | ÇS |
| Mat02MK0300 | Trigonometrik referans fonksiyonun görüntü kümesini belirler. | Bilgi | Yorumlama | a, b | Analiz | Mat02MK0295; Mat02MK0296; Mat02MK0192 | – | ÇS |
| Mat02MK0301 | Trigonometrik fonksiyonun sıfırlarını grafikten belirler. | Bilgi | Yorumlama | a, b | Analiz | Mat02MK0299 | – | ÇS |
| Mat02MK0302 | Trigonometrik fonksiyonun işaretini grafikten belirler. | Bilgi | Yorumlama | a, b | Analiz | Mat02MK0299 | – | ÇS |
| Mat02MK0303 | Trigonometrik fonksiyonun artan ve azalan olduğu aralıkları grafikten belirler. | Bilgi | Yorumlama | a, b | Analiz | Mat02MK0299 | – | ÇS |
| Mat02MK0304 | Trigonometrik fonksiyonun en büyük ve en küçük değerlerini grafikten belirler. | Bilgi | Yorumlama | a, b | Analiz | Mat02MK0300 | – | ÇS |
| Mat02MK0305 | Trigonometrik fonksiyonun bire bir olup olmadığını belirler. | Bilgi | Ayırt etme ve sınıflama | a, b | Analiz | Mat02MK0299 | – | ÇS |
| Mat02MK0306 | Trigonometrik fonksiyonun örten olup olmadığını belirler. | Bilgi | Ayırt etme ve sınıflama | a, b | Analiz | Mat02MK0300 | – | ÇS |
| Mat02MK0307 | Trigonometrik fonksiyonun tek ya da çift fonksiyon olup olmadığını belirler. | Bilgi | Ayırt etme ve sınıflama | a, b | Analiz | Mat02MK0299 | – | ÇS |
| Mat02MK0308 | Trigonometrik referans fonksiyonun grafiğini yatay öteleyerek f(x ± r) biçimindeki fonksiyonları elde eder. | Beceri | Dönüştürme | c, ç | Uygulama | Mat02MK0299; Mat02MK0155 | Mat02YG0033 | ÇS, AU |
| Mat02MK0309 | Trigonometrik referans fonksiyonun grafiğini düşey öteleyerek f(x) ± k biçimindeki fonksiyonları elde eder. | Beceri | Dönüştürme | c, ç | Uygulama | Mat02MK0300; Mat02MK0156 | – | ÇS, AU |
| Mat02MK0310 | Trigonometrik referans fonksiyonun grafiğini a·f(x) ile dikey genişletir ya da daraltır. | Beceri | Dönüştürme | c, ç | Uygulama | Mat02MK0299; Mat02MK0157 | – | ÇS, AU |
| Mat02MK0311 | Trigonometrik referans fonksiyonun grafiğini x eksenine göre yansıtır. | Beceri | Dönüştürme | c, ç | Uygulama | Mat02MK0299; Mat02MK0158 | – | ÇS, AU |
| Mat02MK0312 | Trigonometrik fonksiyonların periyodunu bulur. | Beceri | Kural uygulama | c | Uygulama | Mat02MK0310 | Mat02YG0033 | ÇS |
| Mat02MK0313 | Trigonometrik fonksiyonların nitel özelliklerinin a parametresine nasıl bağlı olduğuna dair varsayımda bulunup genelleme yapar. | Bilgi | Çıkarım ve ilişkilendirme | d, e | Analiz | Mat02MK0310; Mat02MK0311; Mat02MK0301; Mat02MK0302; Mat02MK0303; Mat02MK0304 | – | AU |
| Mat02MK0314 | Trigonometrik fonksiyonların nitel özelliklerinin r parametresine nasıl bağlı olduğuna dair varsayımda bulunup genelleme yapar. | Bilgi | Çıkarım ve ilişkilendirme | d, e | Analiz | Mat02MK0308; Mat02MK0301; Mat02MK0302; Mat02MK0303; Mat02MK0304 | – | AU |
| Mat02MK0315 | Trigonometrik fonksiyonların nitel özelliklerinin k parametresine nasıl bağlı olduğuna dair varsayımda bulunup genelleme yapar. | Bilgi | Çıkarım ve ilişkilendirme | d, e | Analiz | Mat02MK0309; Mat02MK0301; Mat02MK0302; Mat02MK0303; Mat02MK0304 | – | AU |
| Mat02MK0316 | Trigonometrik fonksiyonların a parametresine bağlı nitel özelliklerine ilişkin genellemelerini kontrol ederek önerme olarak ifade eder ve gerçek yaşamdaki kullanışlılığını değerlendirir. | Beceri | Sınama ve değerlendirme | f, g, ğ | Değerlendirme | Mat02MK0313 | – | AU |
| Mat02MK0317 | Trigonometrik fonksiyonların r parametresine bağlı nitel özelliklerine ilişkin genellemelerini kontrol ederek önerme olarak ifade eder ve gerçek yaşamdaki kullanışlılığını değerlendirir. | Beceri | Sınama ve değerlendirme | f, g, ğ | Değerlendirme | Mat02MK0314 | – | AU |
| Mat02MK0318 | Trigonometrik fonksiyonların k parametresine bağlı nitel özelliklerine ilişkin genellemelerini kontrol ederek önerme olarak ifade eder ve gerçek yaşamdaki kullanışlılığını değerlendirir. | Beceri | Sınama ve değerlendirme | f, g, ğ | Değerlendirme | Mat02MK0315 | – | AU |
| Mat02MK0319 | Trigonometrik fonksiyonların a parametresine bağlı nitel özelliklerine ilişkin önermelerini grafiksel olarak doğrular ya da cebirsel olarak ispatlar. | Beceri | Model kurma | h, ı | Analiz | Mat02MK0316 | – | AU |
| Mat02MK0320 | Trigonometrik fonksiyonların r parametresine bağlı nitel özelliklerine ilişkin önermelerini grafiksel olarak doğrular ya da cebirsel olarak ispatlar. | Beceri | Model kurma | h, ı | Analiz | Mat02MK0317 | – | AU |
| Mat02MK0321 | Trigonometrik fonksiyonların k parametresine bağlı nitel özelliklerine ilişkin önermelerini grafiksel olarak doğrular ya da cebirsel olarak ispatlar. | Beceri | Model kurma | h, ı | Analiz | Mat02MK0318 | – | AU |

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi (rubrikle)

Özet: 29 mikro kazanım (29 yeni, 0 yeniden kullanım); yeni olanlardan 14 Bilgi, 15 Beceri.

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
