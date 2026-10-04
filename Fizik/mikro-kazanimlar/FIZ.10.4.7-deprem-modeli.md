# Mikro Kazanım Ayrıştırması: FİZ.10.4.7 (taslak v0.1)

> **FİZ.10.4.7** Depremle ilgili bilimsel model oluşturabilme
> a) Model önerir
> b) Önerilen modeli geliştirir
>
> Kaynak: https://tymm.meb.gov.tr/fizik-dersi/unite/122
> Sınıf ünitesi: Fiz10-U4 (Dalgalar) · Ana ünite: 06 Dalgalar
> Sınırlama (TYMM): TYMM bu çıktı için sınırlama belirtmemiştir.
> Ön öğrenmeler: dönme, öteleme ve titreşim hareketleri; ses dalgalarının ortama göre değişen yayılma sürati; uzunluk ve zaman ölçümü; süratin matematiksel modeli (TYMM ön kabulü).

Yöntem: `FIZ.10.3.4-esdeger-direnc.md` dosyasındaki 8 adım; kodlama ve Bilgi/Beceri ölçütü: `KODLAMA.md`.

Tasarım notu: Model oluşturma, yöntemdeki bilişsel düzeylere Yaratma düzeyinin eklenmesini gerektirdi (bkz. FIZ.10.3.4 dosyası, 7. adım). Ölçme performans görevi + rubriktir.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Fiz06YG0015 | Deprem hasarı yalnızca depremin büyüklüğüne bağlıdır; zemin ve bina özellikleri önemsizdir. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Fiz06MK0060 | Deprem dalgalarının yayılmasını ya da binaların rezonansını gösteren bir model (ör. farklı yükseklikte çubuk-kütle binalar, sarsma masası) önerir. | Beceri | a | Yaratma | Fiz06MK0059 | – | PG |
| Fiz06MK0061 | Modelin hangi değişkenleri temsil ettiğini açıklar. | Bilgi | a | Analiz | Fiz06MK0060 | – | AU |
| Fiz06MK0062 | Modelin sınırlılıklarını açıklar. | Bilgi | a | Analiz | Fiz06MK0060 | – | AU |
| Fiz06MK0063 | Sarsıntı frekansını değiştirerek modeli test eder; hangi yapının en çok salındığını gözlemleyip kaydeder. | Beceri | b | Uygulama | Fiz06MK0060 | Fiz06YG0015 | PG |
| Fiz06MK0064 | Test sonuçlarına göre modeli geliştirir. | Beceri | b | Yaratma | Fiz06MK0063 | – | PG |
| Fiz06MK0065 | Modeldeki iyileşmeyi gerekçelendirir. | Beceri | b | Değerlendirme | Fiz06MK0063 | – | AU |

> 2026-10-01: Tek ölçülebilir hedef taramasıyla güncellendi (bir MK = bir soruyla tamamı ölçülebilen tek hedef). Tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 4 mikro kazanım (4 yeni, 0 yeniden kullanım); yeni olanlardan 1 Bilgi, 3 Beceri.

---

## 3. Örnek ölçme maddeleri

**Fiz06MK0064:** Performans görevi: çubuk-kütle bina modelinizi sarsma masasında farklı frekanslarda test edin, en çok salınan binayı sönümleyici ekleyerek iyileştirin. Rubrik: model önerisi (a), değişkenlerin ve sınırlılıkların açıklanması, test ve kayıt, geliştirme ve gerekçe (b).

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
