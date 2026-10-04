# Mikro Kazanım Ayrıştırması: FİZ.10.4.5 (taslak v0.1)

> **FİZ.10.4.5** Su dalgalarında yansıma ve kırılma ile ilgili tümevarımsal akıl yürütebilme
> a) Yansıma ve kırılma olaylarına ilişkin gözlemler yapar
> b) Açılar arasında ilişki kurar
> c) Olaylara ilişkin genellemeler yapar
>
> Kaynak: https://tymm.meb.gov.tr/fizik-dersi/unite/122
> Sınıf ünitesi: Fiz10-U4 (Dalgalar) · Ana ünite: 06 Dalgalar
> Sınırlama (TYMM): Yankı ile ilgili matematiksel işlemlere girilmez. Doğrusal su dalgalarının oluşumu simülasyon ve görsel gibi materyallerle gösterilebilir.
> Ön öğrenmeler: dönme, öteleme ve titreşim hareketleri; ses dalgalarının ortama göre değişen yayılma sürati; uzunluk ve zaman ölçümü; süratin matematiksel modeli (TYMM ön kabulü).

Yöntem: `FIZ.10.3.4-esdeger-direnc.md` dosyasındaki 8 adım; kodlama ve Bilgi/Beceri ölçütü: `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Fiz06YG0009 | Gelme ve yansıma açıları engel yüzeyi ile yapılan açılardır. |
| Fiz06YG0010 | Kırılmada dalganın frekansı da değişir. |
| Fiz06YG0011 | Derin sudan sığ suya geçen dalganın dalga boyu artar. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Fiz06MK0037 | Dalga leğeni ya da simülasyonda doğrusal su dalgalarının engelden yansımasını gözlemler ve dalga tepelerini çizer. | Beceri | a | Uygulama | Fiz06MK0010 | – | PG |
| Fiz06MK0038 | Derinliği farklı iki ortam arasında su dalgalarının kırılmasını gözlemler ve dalga tepelerini çizer. | Beceri | a | Uygulama | Fiz06MK0030 | – | PG |
| Fiz06MK0039 | Gelme ve yansıma açılarını normale göre ölçer. | Beceri | b | Uygulama | Fiz06MK0037 | Fiz06YG0009 | PG |
| Fiz06MK0040 | Dalganın derin ortamdan sığ ortama geçerken normale yaklaştığını belirler. | Bilgi | b | Analiz | Fiz06MK0038 | – | ÇS |
| Fiz06MK0041 | Dalganın sığ ortamdan derin ortama geçerken normalden uzaklaştığını belirler. | Bilgi | b | Analiz | Fiz06MK0038 | – | ÇS |
| Fiz06MK0042 | Gelme açısının yansıma açısına eşit olduğunu bulur. | Beceri | b | Uygulama | Fiz06MK0037; Fiz06MK0039 | – | PG |
| Fiz06MK0043 | Kırılmada frekansın değişmediği genellemesini yapar. | Bilgi | c | Analiz | Fiz06MK0038; Fiz06MK0019 | Fiz06YG0010 | ÇS, AU |
| Fiz06MK0044 | Kırılmada yayılma sürati ile dalga boyunun birlikte (aynı oranda) değiştiği genellemesini yapar. | Bilgi | c | Analiz | Fiz06MK0038; Fiz06MK0019; Fiz06MK0020 | Fiz06YG0011 | ÇS, AU |
| Fiz06MK0045 | Yansıma genellemelerini günlük yaşam örnekleriyle (yankı) ilişkilendirir. | Bilgi | c | Uygulama | Fiz06MK0042 | – | AU |
| Fiz06MK0046 | Kırılma genellemelerini günlük yaşam örnekleriyle (kıyıya paralel gelen dalgalar) ilişkilendirir. | Bilgi | c | Uygulama | Fiz06MK0043; Fiz06MK0044 | – | AU |

> 2026-10-01: Tek ölçülebilir hedef taramasıyla güncellendi (bir MK = bir soruyla tamamı ölçülebilen tek hedef). Tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 6 mikro kazanım (6 yeni, 0 yeniden kullanım); yeni olanlardan 3 Bilgi, 3 Beceri.

---

## 3. Örnek ölçme maddeleri

**Fiz06MK0039:** Doğrusal dalga engelin normaliyle 30° açı yapacak şekilde geliyor. Yansıma açısı kaç derecedir?  
A) 60 (Fiz06YG0009) · B) 30 ✔ · C) 90 · D) 0

**Fiz06MK0043:** Derin sudan sığ suya geçen su dalgası için hangisi doğrudur?  
A) Frekans azalır (Fiz06YG0010) · B) Dalga boyu artar (Fiz06YG0011) · C) Sürat ve dalga boyu azalır, frekans değişmez ✔ · D) Hiçbiri değişmez

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
