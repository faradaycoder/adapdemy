# Mikro Kazanım Ayrıştırması: FİZ.10.4.4 (taslak v0.1)

> **FİZ.10.4.4** Yayılma süratini etkileyen etmenlere ilişkin bilimsel gözleme dayalı tahmin yapabilme
> a) Etmenleri tahmin eder
> b) Farklı ortamlardaki yayılma süratini karşılaştırır
> c) Sonuç çıkarır
> ç) Elektromanyetik dalgalarla ilgili tahminlerde bulunur
> d) Tahminlerinin geçerliliğini sorgular
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
| Fiz06YG0007 | Ses en hızlı gazlarda yayılır. |
| Fiz06YG0008 | Dalganın yayılma sürati kaynağın frekansına bağlıdır; frekans artınca sürat artar. |
| Fiz06YG0004 | Genliği büyük olan dalga daha hızlı yayılır. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Fiz06MK0027 | Dalganın yayılma süratini etkileyebilecek etmenleri (ortamın türü, ipteki gerilme, su derinliği, sıcaklık) tahmin eder. | Beceri | a | Uygulama | Fiz06MK0020 | – | AU |
| Fiz06MK0028 | Sesin katı, sıvı ve gazlardaki yayılma süratlerini karşılaştırır. | Bilgi | b | Anlama | – | Fiz06YG0007 | ÇS |
| Fiz06MK0029 | Farklı gerilmelerdeki ipte ya da yayda dalga süratini gözlem ya da simülasyonla karşılaştırır. | Beceri | b | Uygulama | Fiz06MK0027 | – | PG |
| Fiz06MK0030 | Derin ve sığ suda su dalgalarının yayılma süratini gözlem ya da simülasyonla karşılaştırır. | Beceri | b | Uygulama | Fiz06MK0027 | – | PG |
| Fiz06MK0031 | Dalganın yayılma süratinin ortamın özelliklerine bağlı olduğu sonucunu çıkarır. | Bilgi | c | Analiz | Fiz06MK0029; Fiz06MK0030; Fiz06MK0028 | – | ÇS, AU |
| Fiz06MK0032 | Dalganın yayılma süratinin kaynağın frekansına bağlı olmadığı sonucunu çıkarır. | Bilgi | c | Analiz | Fiz06MK0029; Fiz06MK0030; Fiz06MK0028 | Fiz06YG0008 | ÇS, AU |
| Fiz06MK0033 | Dalganın yayılma süratinin genliğe bağlı olmadığı sonucunu çıkarır. | Bilgi | c | Analiz | Fiz06MK0029; Fiz06MK0030; Fiz06MK0028 | Fiz06YG0004 | ÇS, AU |
| Fiz06MK0034 | Elektromanyetik dalgaların boşlukta ışık süratiyle yayıldığını belirtir. | Bilgi | ç | Hatırlama | Fiz06MK0024 | – | ÇS |
| Fiz06MK0035 | Elektromanyetik dalgaların maddesel ortamda yavaşladığını tahmin eder. | Bilgi | ç | Hatırlama | Fiz06MK0031; Fiz06MK0034 | – | ÇS |
| Fiz06MK0036 | Tahminlerinin geçerliliğini gözlem verileri ve güvenilir kaynaklarla sorgular. | Beceri | d | Değerlendirme | Fiz06MK0031; Fiz06MK0032; Fiz06MK0033; Fiz06MK0034; Fiz06MK0035 | – | AU, PG |

> 2026-10-01: Tek ölçülebilir hedef taramasıyla güncellendi (bir MK = bir soruyla tamamı ölçülebilen tek hedef). Tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 7 mikro kazanım (7 yeni, 0 yeniden kullanım); yeni olanlardan 3 Bilgi, 4 Beceri.

---

## 3. Örnek ölçme maddeleri

**Fiz06MK0031:** Aynı gergin ipte frekans iki katına çıkarılıyor. Yayılma sürati ve dalga boyu nasıl değişir?  
A) Sürat 2 katına çıkar (Fiz06YG0008) · B) Sürat değişmez, dalga boyu yarıya iner ✔ · C) İkisi de değişmez · D) Dalga boyu 2 katına çıkar

**Fiz06MK0028:** Ses hangi ortamda en hızlı yayılır?  
A) Hava (Fiz06YG0007) · B) Su · C) Çelik ✔ · D) Boşluk

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
