# Mikro Kazanım Ayrıştırması: FİZ.10.4.3 (taslak v0.1)

> **FİZ.10.4.3** Dalgaları özelliklerine göre sınıflandırabilme
> a) Dalgaların özelliklerini belirler
> b) Titreşim doğrultusu ve enerjiye göre ayrıştırır
> c) Titreşim doğrultusu ve enerjiye göre gruplandırır
> ç) Enine, boyuna, hem enine hem boyuna, mekanik ve elektromanyetik olarak adlandırır
>
> Kaynak: https://tymm.meb.gov.tr/fizik-dersi/unite/122
> Sınıf ünitesi: Fiz10-U4 (Dalgalar) · Ana ünite: 06 Dalgalar
> Sınırlama (TYMM): Genel açıklama: mekanik dalgaların yayılması için maddesel ortamın gerekliliği vurgulanır, sesin boşlukta yayılmadığına değinilir; dalgalar titreşim doğrultusu ve enerjiye göre isimleriyle sınırlı kalınarak ifade edilir.
> Ön öğrenmeler: dönme, öteleme ve titreşim hareketleri; ses dalgalarının ortama göre değişen yayılma sürati; uzunluk ve zaman ölçümü; süratin matematiksel modeli (TYMM ön kabulü).

Yöntem: `FIZ.10.3.4-esdeger-direnc.md` dosyasındaki 8 adım; kodlama ve Bilgi/Beceri ölçütü: `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Fiz06YG0005 | Ses dalgası enine bir dalgadır. |
| Fiz06YG0006 | Ses boşlukta da yayılabilir. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Fiz06MK0021 | Dalgaların titreşim doğrultusu ile yayılma doğrultusu arasındaki ilişkiyi belirler. | Bilgi | a | Anlama | Fiz06MK0008 | – | ÇS |
| Fiz06MK0022 | Dalgaların yayılmak için ortama ihtiyaç duyup duymadığını belirler. | Bilgi | a | Anlama | Fiz06MK0008; Fiz06MK0009 | – | ÇS |
| Fiz06MK0023 | Titreşim doğrultusuna göre dalgaları ayrıştırır (enine: yayılmaya dik, boyuna: yayılmaya paralel). | Bilgi | b | Anlama | Fiz06MK0021 | Fiz06YG0005 | ÇS |
| Fiz06MK0024 | Taşıdığı enerjiye göre dalgaları mekanik ve elektromanyetik olarak ayrıştırır. | Bilgi | b | Anlama | Fiz06MK0022 | Fiz06YG0006 | ÇS |
| Fiz06MK0025 | Mekanik dalgaların yayılması için maddesel ortam gerektiğini, sesin boşlukta yayılmadığını açıklar. | Bilgi | b | Anlama | Fiz06MK0024 | Fiz06YG0006 | ÇS |
| Fiz06MK0026 | Dalga türlerini doğru adlarıyla adlandırır (ör. su dalgası: hem enine hem boyuna; ışık: elektromanyetik ve enine). | Bilgi | ç | Hatırlama | Fiz06MK0023; Fiz06MK0024 | – | ÇS |

> 2026-10-01: Tek ölçülebilir hedef taramasıyla güncellendi (bir MK = bir soruyla tamamı ölçülebilen tek hedef). Tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 6 mikro kazanım (6 yeni, 0 yeniden kullanım); yeni olanlardan 5 Bilgi, 1 Beceri.

---

## 3. Örnek ölçme maddeleri

**Fiz06MK0023:** Hoparlörden çıkan ses dalgası için hangisi doğrudur?  
A) Enine ve mekanik (Fiz06YG0005) · B) Boyuna ve mekanik ✔ · C) Enine ve elektromanyetik · D) Boyuna ve elektromanyetik

**Fiz06MK0025:** Havası boşaltılan fanustaki çalar saatin sesi duyulmaz ama ışığı görülür. Nedenini açıklayın. ("Ses boşlukta da yayılır" diyen öğrenci: Fiz06YG0006.)

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
