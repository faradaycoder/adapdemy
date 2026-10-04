# Mikro Kazanım Ayrıştırması: MAT.8.4.3 (taslak v0.1)

> **MAT.8.4.3** Dairenin alan bağıntısının oluşturulma sürecinden hareketle dik dairesel silindirin hacim bağıntısına yönelik analojik akıl yürütebilme
> a) Dairenin alan bağıntısı ve daire-silindir ilişkisini gözden geçirir
> b) Alan ve hacim oluşturulma süreçleri arasındaki ilişkileri belirler
> c) İlişkilerden hareketle hacim çıkarımı yapar
>
> Kaynak: https://tymm.meb.gov.tr/ortaokul-matematik-dersi/unite/475
> Sınıf teması: Mat08-T4 (Geometrik Nicelikler) · Ana tema: 04 Geometrik Nicelikler
> Sınırlama (TYMM): TYMM bu çıktı için sınırlama belirtmemiştir.
> Ön öğrenmeler: dikdörtgen ve paralelkenarın alanı, çemberin uzunluğu, dairenin alan bağıntısını oluşturma, dikdörtgenler prizmasının yüzey alanı ve hacim bağıntısı (TYMM temel kabulü).

Yöntem: fizikle aynı 8 adım (`Fizik/mikro-kazanimlar/FIZ.10.3.4-esdeger-direnc.md`); kodlama ve Bilgi/Beceri ölçütü: EVALORA kökündeki `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Mat04YG0019 | Silindirin hacmi hesaplanırken yarıçap yerine çap kullanılır. |
| Mat04YG0011 | Yüzey alanı ile hacim karıştırılır; yüzey alanı küp birimle (cm³) ifade edilir. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Mat04MK0098 | Dairenin alan bağıntısının daireyi dilimleyip paralelkenara benzeyen şekle dönüştürerek elde edildiğini açıklar. | Bilgi | a | Anlama | Mat04MK0058; Mat04MK0035 | – | AU |
| Mat04MK0151 | Silindiri üst üste konmuş özdeş daire katmanları olarak düşünerek daire ile silindir arasındaki ilişkiyi belirtir. | Bilgi | a | Anlama | Mat04MK0099 | – | AU |
| Mat04MK0152 | Dikdörtgenler prizmasının hacminin (taban alanı × yükseklik) oluşturulma süreci ile silindirin oluşturulma süreci arasındaki benzerliği belirler. | Bilgi | b | Analiz | Mat04MK0151; Mat04MK0078; Mat04MK0079 | – | AU |
| Mat04MK0153 | Silindirin hacminin taban alanı ile yüksekliğin çarpımı (V = πr²·h) olduğu çıkarımını yapar. | Bilgi | c | Analiz | Mat04MK0152 | – | ÇS |
| Mat04MK0154 | Dik dairesel silindirin hacmini hesaplar ve küp birimle ifade eder. | Beceri | c | Uygulama | Mat04MK0153 | Mat04YG0019; Mat04YG0011 | ÇS |
| Mat04MK0155 | Silindirin hacmini içeren gerçek yaşam problemlerini (su deposu) çözer. | Beceri | c | Uygulama | Mat04MK0154 | Mat04YG0011 | AU |
| Mat04MK0156 | Silindirin yüzey alanını içeren gerçek yaşam problemlerini (konserve kutusu etiketi) çözer. | Beceri | c | Uygulama | Mat04MK0149 | Mat04YG0011 | AU |

> 2026-10-01: Tek ölçülebilir hedef bölmesi ve yeniden numaralama sonrası tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 6 mikro kazanım (6 yeni, 0 yeniden kullanım); yeni olanlardan 4 Bilgi, 2 Beceri.

---

## 3. Örnek ölçme maddeleri

**Mat04MK0154:** Çapı 10 cm, yüksekliği 4 cm olan silindirin hacmi kaç cm³'tür? (π = 3)  
A) 1200 (Mat04YG0019) · B) 300 ✔ · C) 120 · D) 600

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
