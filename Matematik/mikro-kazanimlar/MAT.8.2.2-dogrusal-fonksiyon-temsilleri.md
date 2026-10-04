# Mikro Kazanım Ayrıştırması: MAT.8.2.2 (taslak v0.1)

> **MAT.8.2.2** Gerçek yaşam durumlarındaki doğrusal ilişkileri doğrusal fonksiyonlarla temsil edebilme
> a) Cebirsel, tablo ve grafik temsillerini tanır
> b) Uygun temsili belirler
> c) Gerektiğinde temsiller arası geçiş yaparak kullanır
> ç) Temsilin uygunluğunu değerlendirir
> d) Farklı temsilleri ekonomiklik ve kullanışlılık açısından karşılaştırır
> e) Karşılaştırmaya ilişkin karar verir
>
> Kaynak: https://tymm.meb.gov.tr/ortaokul-matematik-dersi/unite/473
> Sınıf teması: Mat08-T2 (Cebirsel Düşünme ve Değişimler) · Ana tema: 02 Cebirsel Düşünme ve Değişimler
> Sınırlama (TYMM): Fonksiyon tanımına girilmeden doğrusal fonksiyonun temsilleri üzerinden çalışılır; fonksiyonlar f(x) = mx + n biçiminde ifade edilir. Değişim oranı (eğim) dikey değişimin yatay değişime oranı olarak işlenir.
> Ön öğrenmeler: birinci dereceden denklem ve eşitsizlikler, oranı yorumlama, temel cebirsel işlemler (TYMM temel kabulü).

Yöntem: fizikle aynı 8 adım (`Fizik/mikro-kazanimlar/FIZ.10.3.4-esdeger-direnc.md`); kodlama ve Bilgi/Beceri ölçütü: EVALORA kökündeki `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Mat02YG0014 | Tablodaki her iki değişkenli ilişki doğrusaldır; değişim oranının sabit olup olmadığına bakmaya gerek yoktur. |
| Mat02YG0015 | Eğim, yatay değişimin dikey değişime oranıdır. |
| Mat02YG0016 | f(x) = mx + n ifadesinde n eğimdir ya da grafiğin x eksenini kestiği noktadır. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Mat02MK0106 | Doğrusal bir ilişkinin sözel temsilini tanır. | Bilgi | a | Anlama | Mat01MK0163 | – | ÇS |
| Mat02MK0107 | Doğrusal bir ilişkinin tablo temsilini tanır. | Bilgi | a | Anlama | Mat01MK0164 | – | ÇS |
| Mat02MK0108 | Doğrusal bir ilişkinin cebirsel (f(x) = mx + n) temsilini tanır. | Bilgi | a | Anlama | Mat02MK0050; Mat02MK0051 | – | ÇS |
| Mat02MK0109 | Doğrusal bir ilişkinin grafik temsilini tanır. | Bilgi | a | Anlama | Mat02MK0102; Mat01MK0165 | – | ÇS |
| Mat02MK0110 | Tablodaki değerlerde değişim oranının sabit olup olmadığına bakarak ilişkinin doğrusal olup olmadığını belirler. | Beceri | a | Analiz | Mat02MK0107 | Mat02YG0014 | ÇS |
| Mat02MK0111 | Gerçek yaşam durumunda bağımlı ve bağımsız değişkeni belirler. | Bilgi | b | Anlama | Mat02MK0106; Mat02MK0108 | – | ÇS |
| Mat02MK0112 | Verilen soruyu yanıtlamak için hangi temsilin (tablo, cebirsel, grafik) uygun olduğunu belirler. | Beceri | b | Uygulama | Mat02MK0107; Mat02MK0108; Mat02MK0109 | – | ÇS, AU |
| Mat02MK0113 | Sözel bir durumdan doğrusal ilişkinin tablosunu oluşturur. | Beceri | c | Uygulama | Mat02MK0111; Mat02MK0107 | – | AU |
| Mat02MK0114 | Sözel bir durumdan f(x) = mx + n cebirsel ifadesini oluşturur. | Beceri | c | Uygulama | Mat02MK0111; Mat02MK0108 | – | AU |
| Mat02MK0115 | Tablodan doğrusal fonksiyonun grafiğini çizer. | Beceri | c | Uygulama | Mat02MK0107; Mat02MK0109 | – | AU |
| Mat02MK0116 | Cebirsel ifadeden doğrusal fonksiyonun grafiğini çizer. | Beceri | c | Uygulama | Mat02MK0108; Mat02MK0051; Mat02MK0109 | – | AU |
| Mat02MK0117 | Doğrusal fonksiyonun grafiğinden tabloya geçer. | Beceri | c | Uygulama | Mat02MK0109; Mat02MK0107 | – | ÇS |
| Mat02MK0118 | Doğrusal fonksiyonun grafiğinden cebirsel ifadeye geçer. | Beceri | c | Uygulama | Mat02MK0116 | – | ÇS |
| Mat02MK0119 | Eğimi dikey değişimin yatay değişime oranı olarak hesaplar. | Beceri | c | Uygulama | Mat02MK0110; Mat02MK0109 | Mat02YG0015 | ÇS, AU |
| Mat02MK0120 | Eğimin durumdaki anlamını (birim başına değişim) yorumlar. | Bilgi | c | Analiz | Mat02MK0119 | – | ÇS |
| Mat02MK0121 | f(x) = mx + n ifadesinde n'nin başlangıç değeri, yani grafiğin y eksenini kestiği nokta olduğunu yorumlar. | Bilgi | c | Anlama | Mat02MK0116 | Mat02YG0016 | ÇS |
| Mat02MK0122 | Bir temsilin verilen durumu doğru ve eksiksiz yansıtıp yansıtmadığını (ör. değişkenin alabileceği değerler) değerlendirir. | Beceri | ç | Değerlendirme | Mat02MK0117; Mat02MK0118 | – | AU |
| Mat02MK0123 | Farklı temsilleri ekonomiklik açısından karşılaştırır. | Beceri | d | Değerlendirme | Mat02MK0122 | – | AU |
| Mat02MK0124 | Farklı temsilleri kullanışlılık açısından karşılaştırır. | Beceri | d | Değerlendirme | Mat02MK0122 | – | AU |
| Mat02MK0125 | Karşılaştırmaya dayanarak bir durum için kullanılacak temsile karar verir ve kararını gerekçelendirir. | Beceri | e | Değerlendirme | Mat02MK0123; Mat02MK0124 | – | AU |

> 2026-10-01: Tek ölçülebilir hedef bölmesi ve yeniden numaralama sonrası tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 12 mikro kazanım (12 yeni, 0 yeniden kullanım); yeni olanlardan 3 Bilgi, 9 Beceri.

---

## 3. Örnek ölçme maddeleri

**Mat02MK0119:** Bir taksinin ücreti f(x) = 4x + 20 (x: km). 4 sayısı neyi ifade eder?  
A) Açılış ücretini (Mat02YG0016) · B) Kilometre başına ücreti ✔ · C) Toplam ücreti · D) Gidilen yolu

**Mat02MK0110:** x: 1, 2, 3, 4 için y: 3, 5, 8, 12 olan tablo doğrusal bir ilişki midir? Neden? ("Evet, çünkü x düzenli artıyor" yanıtı Mat02YG0014 yanılgısını gösterir.)

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
