# Mikro Kazanım Ayrıştırması: MAT.12.4.7 (taslak v0.1)

> **MAT.12.4.7** Türevin limit gösteriminden faydalanarak iki fonksiyonun toplamı, farkı, çarpımı, bölümü ve bileşkesinin türevine ilişkin muhakeme yapabilme
> a–b) Varsayımda bulunur, genelleme yapar.
> c–ç) Karşılaştırır, önerme sunar.
> d) Değerlendirir.
> e–f) İspatlar, değerlendirir.
>
> Kaynak: https://tymm.meb.gov.tr/matematik-dersi/unite/307
> Sınıf teması: Mat12-T4 (Değişimin Matematiği) · Ana tema: 11 Değişimin Matematiği
> Sınırlama (TYMM): Bileşke fonksiyonun türevinde iki fonksiyonun bileşkesiyle sınırlı kalınır.

Yöntem: `Fizik/mikro-kazanimlar/FIZ.10.3.4-esdeger-direnc.md` dosyasındaki adımlar; kodlama, Bilgi/Beceri ve işlem türü ölçütü: `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Mat11YG0006 | Çarpımın türevi, türevlerin çarpımıdır. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | İşlem türü | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|---|
| Mat11MK0066 | İki fonksiyonun toplamının türevine ilişkin varsayımda bulunup genelleme yapar. | Bilgi | Çıkarım ve ilişkilendirme | a, b | Analiz | Mat11MK0053 | – | AU |
| Mat11MK0067 | İki fonksiyonun farkının türevine ilişkin varsayımda bulunup genelleme yapar. | Bilgi | Çıkarım ve ilişkilendirme | a, b | Analiz | Mat11MK0053 | – | AU |
| Mat11MK0068 | İki fonksiyonun çarpımının türevine ilişkin varsayımda bulunup genelleme yapar. | Bilgi | Çıkarım ve ilişkilendirme | a, b | Analiz | Mat11MK0053 | Mat11YG0006 | AU |
| Mat11MK0069 | İki fonksiyonun bölümünün türevine ilişkin varsayımda bulunup genelleme yapar. | Bilgi | Çıkarım ve ilişkilendirme | a, b | Analiz | Mat11MK0053 | – | AU |
| Mat11MK0070 | İki fonksiyonun bileşkesinin türevine ilişkin varsayımda bulunup genelleme yapar. | Bilgi | Çıkarım ve ilişkilendirme | a, b | Analiz | Mat11MK0053; Mat02MK0401 | – | AU |
| Mat11MK0071 | İki fonksiyonun toplamının türevine ilişkin genellemelerini varsayımlarıyla karşılaştırarak önerme olarak sunar. | Beceri | Sınama ve değerlendirme | c, ç | Değerlendirme | Mat11MK0066 | – | AU |
| Mat11MK0072 | İki fonksiyonun farkının türevine ilişkin genellemelerini varsayımlarıyla karşılaştırarak önerme olarak sunar. | Beceri | Sınama ve değerlendirme | c, ç | Değerlendirme | Mat11MK0067 | – | AU |
| Mat11MK0073 | İki fonksiyonun çarpımının türevine ilişkin genellemelerini varsayımlarıyla karşılaştırarak önerme olarak sunar. | Beceri | Sınama ve değerlendirme | c, ç | Değerlendirme | Mat11MK0068 | – | AU |
| Mat11MK0074 | İki fonksiyonun bölümünün türevine ilişkin genellemelerini varsayımlarıyla karşılaştırarak önerme olarak sunar. | Beceri | Sınama ve değerlendirme | c, ç | Değerlendirme | Mat11MK0069 | – | AU |
| Mat11MK0075 | İki fonksiyonun bileşkesinin türevine ilişkin genellemelerini varsayımlarıyla karşılaştırarak önerme olarak sunar. | Beceri | Sınama ve değerlendirme | c, ç | Değerlendirme | Mat11MK0070 | – | AU |
| Mat11MK0076 | İki fonksiyonun toplamının türevine ilişkin önermeleri problem durumlarında kullanarak kullanışlılığını değerlendirir. | Beceri | Transfer ve problem çözme | d | Uygulama | Mat11MK0071 | – | AU |
| Mat11MK0077 | İki fonksiyonun farkının türevine ilişkin önermeleri problem durumlarında kullanarak kullanışlılığını değerlendirir. | Beceri | Transfer ve problem çözme | d | Uygulama | Mat11MK0072 | – | AU |
| Mat11MK0078 | İki fonksiyonun çarpımının türevine ilişkin önermeleri problem durumlarında kullanarak kullanışlılığını değerlendirir. | Beceri | Transfer ve problem çözme | d | Uygulama | Mat11MK0073 | – | AU |
| Mat11MK0079 | İki fonksiyonun bölümünün türevine ilişkin önermeleri problem durumlarında kullanarak kullanışlılığını değerlendirir. | Beceri | Transfer ve problem çözme | d | Uygulama | Mat11MK0074 | – | AU |
| Mat11MK0080 | İki fonksiyonun bileşkesinin türevine ilişkin önermeleri problem durumlarında kullanarak kullanışlılığını değerlendirir. | Beceri | Transfer ve problem çözme | d | Uygulama | Mat11MK0075 | – | AU |
| Mat11MK0081 | Toplamın türevini alır. | Beceri | Kural uygulama | d | Uygulama | Mat11MK0071; Mat11MK0053 | – | ÇS |
| Mat11MK0082 | Farkın türevini alır. | Beceri | Kural uygulama | d | Uygulama | Mat11MK0072; Mat11MK0053 | – | ÇS |
| Mat11MK0083 | Çarpım kuralıyla türev alır. | Beceri | Kural uygulama | d | Uygulama | Mat11MK0073; Mat11MK0053 | Mat11YG0006 | ÇS |
| Mat11MK0084 | Zincir kuralıyla iki fonksiyonun bileşkesinin türevini alır. | Beceri | Kural uygulama | d | Uygulama | Mat11MK0075; Mat11MK0053 | – | ÇS |
| Mat11MK0085 | Bölüm kuralıyla türev alır. | Beceri | Kural uygulama | d | Uygulama | Mat11MK0074; Mat11MK0053 | – | ÇS |
| Mat11MK0086 | İki fonksiyonun toplamının türevine ilişkin önermeleri matematiksel doğrulama ya da ispat yöntemleriyle doğrular. | Beceri | Model kurma | e, f | Analiz | Mat11MK0071 | – | AU |
| Mat11MK0087 | İki fonksiyonun farkının türevine ilişkin önermeleri matematiksel doğrulama ya da ispat yöntemleriyle doğrular. | Beceri | Model kurma | e, f | Analiz | Mat11MK0072 | – | AU |
| Mat11MK0088 | İki fonksiyonun çarpımının türevine ilişkin önermeleri matematiksel doğrulama ya da ispat yöntemleriyle doğrular. | Beceri | Model kurma | e, f | Analiz | Mat11MK0073 | – | AU |
| Mat11MK0089 | İki fonksiyonun bölümünün türevine ilişkin önermeleri matematiksel doğrulama ya da ispat yöntemleriyle doğrular. | Beceri | Model kurma | e, f | Analiz | Mat11MK0074 | – | AU |
| Mat11MK0090 | İki fonksiyonun bileşkesinin türevine ilişkin önermeleri matematiksel doğrulama ya da ispat yöntemleriyle doğrular. | Beceri | Model kurma | e, f | Analiz | Mat11MK0075 | – | AU |

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi (rubrikle)

Özet: 25 mikro kazanım (25 yeni, 0 yeniden kullanım); yeni olanlardan 5 Bilgi, 20 Beceri.

---

## 3. Örnek ölçme maddesi

**Mat11MK0081:** f(x) = x² · x³ fonksiyonunun türevi hangisidir?  
A) 2x · 3x² = 6x³ (Mat11YG0006) · B) 5x⁴ ✔ · C) x⁵ · D) 6x

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
