# Mikro Kazanım Ayrıştırması: MAT.10.7.1 (taslak v0.1)

> **MAT.10.7.1** Koşullu olasılık ile çıkarım yapabilme
> a) Varsayımda bulunur.
> b) Olası çıktıları listeler.
> c) Karşılaştırır.
> ç) Önerme sunar.
> d) Koşullu olasılıkla değerlendirir.
>
> Kaynak: https://tymm.meb.gov.tr/matematik-dersi/unite/274
> Sınıf teması: Mat10-T7 (Veriden Olasılığa) · Ana tema: 07 Veriden Olasılığa

Yöntem: `Fizik/mikro-kazanimlar/FIZ.10.3.4-esdeger-direnc.md` dosyasındaki adımlar; kodlama, Bilgi/Beceri ve işlem türü ölçütü: `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Mat07YG0010 | P(A | B) ile P(B | A) aynıdır. |
| Mat07YG0011 | Ayrık olaylar bağımsız olaylardır. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | İşlem türü | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|---|
| Mat07MK0036 | Bir olayın gerçekleşmesinin başka bir olaya bağlı olduğu durumların olasılığına ilişkin varsayımda bulunup örneklerden genelleme yapar. | Bilgi | Çıkarım ve ilişkilendirme | a, b | Analiz | Mat07MK0034 | Mat07YG0010 | AU |
| Mat07MK0037 | Bir olayın gerçekleşmesinin başka bir olaya bağlı olduğu durumların olasılığına ilişkin genellemelerini varsayımlarıyla karşılaştırarak önerme olarak sunar. | Beceri | Sınama ve değerlendirme | c, ç | Değerlendirme | Mat07MK0036 | – | AU |
| Mat07MK0038 | İki yönlü tablodan koşullu olasılık hesaplar. | Beceri | Kural uygulama | c | Uygulama | Mat07MK0039; Mat06MK0054; Mat06MK0055 | – | ÇS |
| Mat07MK0039 | Koşullu olasılığı P(A \| B) = P(A ∩ B) / P(B) ile hesaplar. | Beceri | Kural uygulama | ç, d | Uygulama | Mat07MK0037 | Mat07YG0010 | ÇS |
| Mat07MK0040 | Bir olayın gerçekleşmesinin başka bir olaya bağlı olduğu durumların olasılığına ilişkin önermeleri problem durumlarında kullanarak kullanışlılığını değerlendirir. | Beceri | Transfer ve problem çözme | d | Uygulama | Mat07MK0037 | – | AU |
| Mat07MK0041 | Bağımsız ve bağımlı olayları P(A \| B) = P(A) koşuluyla ayırt eder. | Bilgi | Ayırt etme ve sınıflama | d | Analiz | Mat07MK0039 | Mat07YG0011 | ÇS |

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi (rubrikle)

Özet: 6 mikro kazanım (6 yeni, 0 yeniden kullanım); yeni olanlardan 2 Bilgi, 4 Beceri.

---

## 3. Örnek ölçme maddesi

**Mat07MK0039:** Bir sınıfta öğrencilerin %40’ı gözlüklü, %10’u hem gözlüklü hem kız. Gözlüklü bir öğrencinin kız olma olasılığı kaçtır?  
A) 0,10 · B) 0,25 ✔ · C) 0,40 · D) P(gözlüklü | kız) ile aynıdır (Mat07YG0010)

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
