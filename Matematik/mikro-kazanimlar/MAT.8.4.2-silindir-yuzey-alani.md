# Mikro Kazanım Ayrıştırması: MAT.8.4.2 (taslak v0.1)

> **MAT.8.4.2** Dik dairesel silindirin yüzey açınımına ilişkin deneyimlerini dik dairesel silindirin yüzey alanına yansıtabilme
> a) Yüzey açınımına ilişkin deneyimlerini gözden geçirir
> b) Yüzey alanına yönelik çıkarım yapar
> c) Çıkarımını farklı örnekler üzerinden değerlendirir
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
| Mat04YG0018 | Silindirin yüzey alanında yalnızca bir taban alanı hesaba katılır. |
| Mat04YG0011 | Yüzey alanı ile hacim karıştırılır; yüzey alanı küp birimle (cm³) ifade edilir. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Mat04MK0147 | Silindirin yüzey açınımını oluşturan iki daire ve bir dikdörtgeni silindirin ölçüleriyle ilişkilendirir. | Beceri | a | Uygulama | Mat04MK0142; Mat04MK0143 | – | PG, ÇS |
| Mat04MK0148 | Silindirin yüzey alanının iki taban alanı ile yanal alanın toplamı (2πr² + 2πr·h) olduğu çıkarımını yapar. | Bilgi | b | Analiz | Mat04MK0147; Mat04MK0099 | Mat04YG0018 | ÇS, AU |
| Mat04MK0149 | Dik dairesel silindirin yüzey alanını hesaplar ve uygun birimle ifade eder. | Beceri | b | Uygulama | Mat04MK0148 | Mat04YG0018; Mat04YG0011 | ÇS |
| Mat04MK0150 | Çıkarımını farklı durumlarda (kapaksız kutu, boru, etiket) değerlendirerek yüzey alanı hesabını duruma uyarlar. | Beceri | c | Değerlendirme | Mat04MK0149 | Mat04YG0018 | AU, PG |

> 2026-10-01: Tek ölçülebilir hedef bölmesi ve yeniden numaralama sonrası tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 4 mikro kazanım (4 yeni, 0 yeniden kullanım); yeni olanlardan 1 Bilgi, 3 Beceri.

---

## 3. Örnek ölçme maddeleri

**Mat04MK0149:** Yarıçapı 2 cm, yüksekliği 5 cm olan silindirin yüzey alanı kaç cm²'dir? (π = 3)  
A) 72 (Mat04YG0018: tek taban) · B) 84 ✔ · C) 60 · D) 84 cm³ (Mat04YG0011)

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
