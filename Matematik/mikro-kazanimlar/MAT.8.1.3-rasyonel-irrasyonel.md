# Mikro Kazanım Ayrıştırması: MAT.8.1.3 (taslak v0.1)

> **MAT.8.1.3** Sayıların rasyonel ya da irrasyonelliğini değerlendirebilme
> a) Ondalık gösterimi ölçüt olarak belirler
> b) Ondalık gösterimi bölme işlemi veya hesap makinesiyle elde eder
> c) Ölçütle karşılaştırır
> ç) Rasyonellik hakkında yargıda bulunur
>
> Kaynak: https://tymm.meb.gov.tr/ortaokul-matematik-dersi/unite/472
> Sınıf teması: Mat08-T1 (Sayılar ve Nicelikler) · Ana tema: 01 Sayılar ve Nicelikler
> Sınırlama (TYMM): Ondalık gösterimler binde birler basamağına kadar ele alınır.
> Ön öğrenmeler: rasyonel sayıları ve basamak değerlerini yorumlama, rasyonel sayılarla dört işlem, doğal sayının karesini ve küpünü ifade etme (TYMM temel kabulü).

Yöntem: fizikle aynı 8 adım (`Fizik/mikro-kazanimlar/FIZ.10.3.4-esdeger-direnc.md`); kodlama ve Bilgi/Beceri ölçütü: EVALORA kökündeki `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Mat01YG0035 | Ondalık kısmı uzun olan her sayı irrasyoneldir (devirli ondalıklar da). |
| Mat01YG0036 | Kök içeren her sayı irrasyoneldir (√9 irrasyoneldir). |
| Mat01YG0037 | π sayısı 3,14'e ya da 22/7'ye eşittir, bu yüzden rasyoneldir. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Mat01MK0093 | Kesirleri bölme işlemiyle ondalık gösterime çevirir. | Beceri | b | Uygulama | Mat01MK0090; Mat01MK0018 | – | ÇS |
| Mat01MK0094 | Devirli ondalık gösterimde devreden kısmı belirler. | Beceri | b | Uygulama | Mat01MK0090 | – | ÇS |
| Mat01MK0218 | Rasyonel sayıların ondalık gösteriminin sonlu ya da devirli olduğunu ölçüt olarak belirtir. | Bilgi | a | Anlama | Mat01MK0140 | Mat01YG0035 | ÇS |
| Mat01MK0219 | İrrasyonel sayıların ondalık gösteriminin devirsiz ve sonsuz olduğunu ölçüt olarak belirtir. | Bilgi | a | Anlama | Mat01MK0140 | Mat01YG0035 | ÇS |
| Mat01MK0220 | Hesap makinesiyle tam kare olmayan sayıların kareköklerinin ve π'nin ondalık gösterimini elde eder. | Beceri | b | Uygulama | Mat01MK0216 | – | AU |
| Mat01MK0221 | Elde ettiği ondalık gösterimi ölçütle karşılaştırarak sonlu, devirli ya da devirsiz olduğunu belirler. | Beceri | c | Analiz | Mat01MK0218; Mat01MK0219; Mat01MK0220 | Mat01YG0035 | ÇS |
| Mat01MK0222 | Verilen sayıların (kareköklü ifadeler ve π dâhil) rasyonel ya da irrasyonel olduğuna gerekçeli yargıda bulunur. | Bilgi | ç | Değerlendirme | Mat01MK0221 | Mat01YG0036; Mat01YG0037 | ÇS, AU |

> 2026-10-01: Tek ölçülebilir hedef bölmesi ve yeniden numaralama sonrası tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 5 mikro kazanım (5 yeni, 0 yeniden kullanım); yeni olanlardan 2 Bilgi, 3 Beceri.

---

## 3. Örnek ölçme maddeleri

**Mat01MK0222:** Hangisi irrasyonel sayıdır?  
A) √9 (Mat01YG0036) · B) 0,333… (Mat01YG0035) · C) √7 ✔ · D) 22/7

**Mat01MK0222:** π sayısının rasyonel olup olmadığını gerekçesiyle açıklayın. ("π = 3,14 olduğu için rasyoneldir" yanıtı Mat01YG0037 yanılgısını gösterir.)

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
