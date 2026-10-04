# Mikro Kazanım Ayrıştırması: FİZ.10.4.2 (taslak v0.1)

> **FİZ.10.4.2** Dalgaların temel kavramlarına ilişkin operasyonel tanımlama yapabilme
> a) Temel kavramlara ilişkin nitelikleri tanımlar
> b) Niteliklerin ölçümünü yapar
> c) Kavramları niteliklerine bağlı olarak tanımlar
>
> Kaynak: https://tymm.meb.gov.tr/fizik-dersi/unite/122
> Sınıf ünitesi: Fiz10-U4 (Dalgalar) · Ana ünite: 06 Dalgalar
> Sınırlama (TYMM): Dalgaların temel kavramları ile ilgili matematiksel işlemler yaptırılır. (Destekleme: dalga boyu ölçümünde milimetrik kâğıda çizilmiş enine dalga görseli kullanılabilir.)
> Ön öğrenmeler: dönme, öteleme ve titreşim hareketleri; ses dalgalarının ortama göre değişen yayılma sürati; uzunluk ve zaman ölçümü; süratin matematiksel modeli (TYMM ön kabulü).

Yöntem: `FIZ.10.3.4-esdeger-direnc.md` dosyasındaki 8 adım; kodlama ve Bilgi/Beceri ölçütü: `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Fiz06YG0002 | Dalga ilerlerken ortamın maddesi de dalgayla birlikte ilerler. |
| Fiz06YG0003 | Dalga boyu, bir tepe ile hemen yanındaki çukur arasındaki uzaklıktır. |
| Fiz06YG0004 | Genliği büyük olan dalga daha hızlı yayılır. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Fiz06MK0008 | Dalgayı titreşimlerin ortamda yayılması olarak tanımlar. | Bilgi | a | Anlama | Fiz06MK0002 | – | ÇS |
| Fiz06MK0009 | Dalganın madde taşımadan enerji aktardığını belirtir. | Bilgi | a | Anlama | Fiz06MK0008 | Fiz06YG0002 | ÇS |
| Fiz06MK0010 | Dalga tepesini dalga görseli üzerinde gösterir. | Bilgi | a | Anlama | Fiz06MK0008 | – | ÇS |
| Fiz06MK0011 | Dalga çukurunu dalga görseli üzerinde gösterir. | Bilgi | a | Anlama | Fiz06MK0008 | – | ÇS |
| Fiz06MK0012 | Dalga boyunu dalga görseli üzerinde gösterir. | Bilgi | a | Anlama | Fiz06MK0008 | Fiz06YG0003 | ÇS |
| Fiz06MK0013 | Genliği dalga görseli üzerinde gösterir. | Bilgi | a | Anlama | Fiz06MK0008 | – | ÇS |
| Fiz06MK0014 | Belirli sürede oluşan dalga sayısından frekansı ölçer. | Beceri | b | Uygulama | Fiz06MK0004 | – | PG |
| Fiz06MK0015 | Bir dalganın oluşma süresinden periyodu ölçer. | Beceri | b | Uygulama | Fiz06MK0003 | – | PG |
| Fiz06MK0016 | Dalga görseli ya da yay/ip deneyinde dalga boyunu ölçer. | Beceri | b | Uygulama | Fiz06MK0012 | Fiz06YG0003 | ÇS, PG |
| Fiz06MK0017 | Dalga görseli ya da yay/ip deneyinde genliği ölçer. | Beceri | b | Uygulama | Fiz06MK0013 | – | ÇS, PG |
| Fiz06MK0018 | Frekansı kaynağın titreşimine bağlı bir nitelik olarak tanımlar. | Bilgi | c | Anlama | Fiz06MK0004; Fiz06MK0008 | – | ÇS |
| Fiz06MK0019 | Dalga ilerlerken frekansın değişmediğini belirtir. | Bilgi | c | Anlama | Fiz06MK0018 | – | ÇS |
| Fiz06MK0020 | v = λ·f (v = λ / T) modelini kullanarak yayılma sürati, dalga boyu ya da frekansı hesaplar. | Beceri | c | Uygulama | Fiz06MK0016; Fiz06MK0014; Fiz06MK0015; Fiz02MK0047 | Fiz06YG0004 | ÇS |

> 2026-10-01: Tek ölçülebilir hedef taramasıyla güncellendi (bir MK = bir soruyla tamamı ölçülebilen tek hedef). Tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 6 mikro kazanım (6 yeni, 0 yeniden kullanım); yeni olanlardan 3 Bilgi, 3 Beceri.

---

## 3. Örnek ölçme maddeleri

**Fiz06MK0016:** Milimetrik kâğıttaki enine dalgada ardışık iki tepe arası 8 kare (1 kare = 1 cm). Dalga boyu kaç cm'dir?  
A) 4 (Fiz06YG0003) · B) 8 ✔ · C) 16 · D) 2

**Fiz06MK0020:** Frekansı 5 Hz, dalga boyu 0,4 m olan dalganın yayılma sürati kaç m/s'dir?  
A) 2 ✔ · B) 12,5 · C) 0,08 · D) 5,4

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
