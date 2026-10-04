# Mikro Kazanım Ayrıştırması: MAT.8.4.1 (taslak v0.1)

> **MAT.8.4.1** Dik prizmalar, dikdörtgen dik piramit, dik dairesel silindir ve dik dairesel koninin yüzey açınımlarını çözümleyebilme
> a) Yüzey açınımlarında yer alan şekilleri belirler
> b) Yüzey açınımlarında yer alan şekiller arasındaki ilişkileri belirler
>
> Kaynak: https://tymm.meb.gov.tr/ortaokul-matematik-dersi/unite/475
> Sınıf teması: Mat08-T4 (Geometrik Nicelikler) · Ana tema: 04 Geometrik Nicelikler
> Sınırlama (TYMM): TYMM bu çıktı için sınırlama belirtmemiştir.
> Ön öğrenmeler: dikdörtgen ve paralelkenarın alanı, çemberin uzunluğu, dairenin alan bağıntısını oluşturma, dikdörtgenler prizmasının yüzey alanı ve hacim bağıntısı (TYMM temel kabulü).

Yöntem: fizikle aynı 8 adım (`Fizik/mikro-kazanimlar/FIZ.10.3.4-esdeger-direnc.md`); kodlama ve Bilgi/Beceri ölçütü: EVALORA kökündeki `KODLAMA.md`.

Tasarım notu: TYMM bu temada yalnızca silindirin yüzey alanı ve hacmini hesaplatır; koni ve piramit açınımları hesaplama yapılmadan çözümlenir.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Mat04YG0015 | Koninin yanal yüzeyi açıldığında üçgen olur. |
| Mat04YG0016 | Doğru sayıda ve biçimde yüzü olan her açınım katlandığında cismi oluşturur; yüzlerin yerleşimi önemsizdir. |
| Mat04YG0017 | Silindirin yanal yüz açınımındaki dikdörtgenin bir kenarı taban çapına eşittir (taban çemberinin uzunluğuna değil). |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Mat04MK0132 | Dik prizmanın elemanlarını (taban, yanal yüz, cisim yüksekliği) belirler. | Bilgi | a | Anlama | Mat04MK0072 | – | ÇS |
| Mat04MK0133 | Dikdörtgen dik piramidin elemanlarını (taban, yanal yüz, tepe noktası, yükseklik) belirler. | Bilgi | a | Anlama | Mat03MK0040 | – | ÇS |
| Mat04MK0134 | Dik dairesel silindirin elemanlarını (taban, yanal yüz, yükseklik) belirler. | Bilgi | a | Anlama | Mat04MK0051; Mat04MK0052 | – | ÇS |
| Mat04MK0135 | Dik dairesel koninin elemanlarını (taban, tepe noktası, ana doğru, yükseklik) belirler. | Bilgi | a | Anlama | Mat04MK0052 | – | ÇS |
| Mat04MK0136 | Dik prizmanın yüzey açınımındaki şekilleri belirler. | Bilgi | a | Anlama | Mat04MK0132 | – | ÇS |
| Mat04MK0137 | Dikdörtgen dik piramidin yüzey açınımındaki şekilleri belirler. | Bilgi | a | Anlama | Mat04MK0133 | – | ÇS |
| Mat04MK0138 | Dik dairesel silindirin yüzey açınımındaki şekilleri belirler. | Bilgi | a | Anlama | Mat04MK0134 | – | ÇS |
| Mat04MK0139 | Dik dairesel koninin yüzey açınımındaki şekilleri belirler. | Bilgi | a | Anlama | Mat04MK0135 | Mat04YG0015 | ÇS |
| Mat04MK0140 | Verilen açınımın hangi cisme ait olduğunu belirler. | Beceri | a | Analiz | Mat04MK0136; Mat04MK0137; Mat04MK0138; Mat04MK0139 | – | ÇS |
| Mat04MK0141 | Verilen açınımın katlandığında cismi oluşturup oluşturmayacağını belirler. | Beceri | a | Analiz | Mat04MK0136; Mat04MK0137; Mat04MK0138; Mat04MK0139 | Mat04YG0016 | ÇS |
| Mat04MK0142 | Silindir açınımında yanal yüz dikdörtgeninin bir kenarının taban çemberinin uzunluğuna eşit olduğunu belirler. | Bilgi | b | Analiz | Mat04MK0138; Mat04MK0058 | Mat04YG0017 | ÇS |
| Mat04MK0143 | Silindir açınımında yanal yüz dikdörtgeninin diğer kenarının silindirin yüksekliğine eşit olduğunu belirler. | Bilgi | b | Analiz | Mat04MK0138 | – | ÇS |
| Mat04MK0144 | Piramit açınımında yanal yüz üçgeninin tabanının taban kenarına eşit olduğunu belirler. | Bilgi | b | Analiz | Mat04MK0137 | – | ÇS |
| Mat04MK0145 | Koni açınımında daire diliminin yay uzunluğunun taban çemberinin uzunluğuna eşit olduğunu belirler. | Bilgi | b | Analiz | Mat04MK0139; Mat04MK0104 | Mat04YG0015 | ÇS |
| Mat04MK0146 | Bir cismin yüzey açınımını çizer ya da kâğıttan oluşturup katlar. | Beceri | b | Uygulama | Mat04MK0140; Mat04MK0141 | Mat04YG0016 | PG |

> 2026-10-01: Tek ölçülebilir hedef bölmesi ve yeniden numaralama sonrası tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 6 mikro kazanım (6 yeni, 0 yeniden kullanım); yeni olanlardan 4 Bilgi, 2 Beceri.

---

## 3. Örnek ölçme maddeleri

**Mat04MK0136:** Dik dairesel koninin yüzey açınımında hangi şekiller bulunur?  
A) Daire ve üçgen (Mat04YG0015) · B) Daire ve daire dilimi ✔ · C) İki daire ve dikdörtgen · D) Kare ve dört üçgen

**Mat04MK0142:** Yarıçapı 3 cm, yüksekliği 10 cm olan silindirin yanal yüz açınımı olan dikdörtgenin kenarları kaç cm'dir? (π = 3)  
A) 6 ve 10 (Mat04YG0017) · B) 18 ve 10 ✔ · C) 9 ve 10 · D) 3 ve 10

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
