# Mikro Kazanım Ayrıştırması: FİZ.10.4.6 (taslak v0.1)

> **FİZ.10.4.6** Rezonans ve depreme ilişkin kavramlar üzerinden depremi sorgulayabilme
> a) İlişkili kavramları tanımlar
> b) Kavramlarla ilgili sorular sorar
> c) Kavramlar hakkında bilgi toplar
> ç) Toplanan bilgilerin doğruluğunu değerlendirir
> d) Depreme yönelik çıkarımlar yapar
>
> Kaynak: https://tymm.meb.gov.tr/fizik-dersi/unite/122
> Sınıf ünitesi: Fiz10-U4 (Dalgalar) · Ana ünite: 06 Dalgalar
> Sınırlama (TYMM): TYMM bu çıktı için sınırlama belirtmemiştir.
> Ön öğrenmeler: dönme, öteleme ve titreşim hareketleri; ses dalgalarının ortama göre değişen yayılma sürati; uzunluk ve zaman ölçümü; süratin matematiksel modeli (TYMM ön kabulü).

Yöntem: `FIZ.10.3.4-esdeger-direnc.md` dosyasındaki 8 adım; kodlama ve Bilgi/Beceri ölçütü: `KODLAMA.md`.

Tasarım notu: Sorgulama çıktısı olduğu için ağırlıklı ölçme performans görevi + rubriktir.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Fiz06YG0012 | Depremin odak noktası ile merkez üssü aynı noktadır. |
| Fiz06YG0013 | Depremin büyüklüğü (magnitüd) ile şiddeti aynı kavramdır. |
| Fiz06YG0014 | Depremin yeri, zamanı ve büyüklüğü önceden kesin olarak tahmin edilebilir. |
| Fiz06YG0015 | Deprem hasarı yalnızca depremin büyüklüğüne bağlıdır; zemin ve bina özellikleri önemsizdir. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Fiz06MK0047 | Doğal titreşim frekansını tanımlar. | Bilgi | a | Anlama | Fiz06MK0004; Fiz06MK0006 | – | ÇS |
| Fiz06MK0048 | Rezonansı dış etkinin frekansı doğal frekansa eşit olduğunda genliğin büyümesi olarak tanımlar. | Bilgi | a | Anlama | Fiz06MK0047; Fiz06MK0013 | – | ÇS |
| Fiz06MK0049 | Depremi tanımlar. | Bilgi | a | Hatırlama | – | – | ÇS |
| Fiz06MK0050 | Depremin odak noktasını tanımlar. | Bilgi | a | Hatırlama | – | Fiz06YG0012 | ÇS |
| Fiz06MK0051 | Depremin merkez üssünü tanımlar. | Bilgi | a | Hatırlama | – | Fiz06YG0012 | ÇS |
| Fiz06MK0052 | P dalgalarını boyuna dalga olarak ilişkilendirir. | Bilgi | a | Anlama | Fiz06MK0023; Fiz06MK0049 | – | ÇS |
| Fiz06MK0053 | S dalgalarını enine dalga olarak ilişkilendirir. | Bilgi | a | Anlama | Fiz06MK0023; Fiz06MK0049 | – | ÇS |
| Fiz06MK0054 | Yüzey dalgalarını dalga sınıflandırmasıyla ilişkilendirir. | Bilgi | a | Anlama | Fiz06MK0023; Fiz06MK0049 | – | ÇS |
| Fiz06MK0055 | Deprem büyüklüğü (magnitüd) ile şiddetini ayırt eder. | Bilgi | a | Anlama | Fiz06MK0049; Fiz06MK0050; Fiz06MK0051 | Fiz06YG0013 | ÇS |
| Fiz06MK0056 | Rezonans ve deprem ilişkisine yönelik araştırılabilir sorular sorar. | Beceri | b | Uygulama | Fiz06MK0047; Fiz06MK0048 | – | PG |
| Fiz06MK0057 | Rezonans, zemin özellikleri ve deprem dalgaları hakkında güvenilir kaynaklardan (AFAD, Kandilli Rasathanesi, bilimsel yayınlar) bilgi toplar. | Beceri | c | Uygulama | Fiz06MK0056 | – | PG |
| Fiz06MK0058 | Depremle ilgili toplanan bilgilerin (özellikle "deprem tahmini" iddialarının) doğruluğunu kaynak ve bilimsel tutarlılık açısından değerlendirir. | Beceri | ç | Değerlendirme | Fiz06MK0057 | Fiz06YG0014 | PG |
| Fiz06MK0059 | Bina doğal frekansı ile deprem dalgası frekansının örtüşmesinin (rezonans) hasarı artırdığı çıkarımını yapar. | Bilgi | d | Analiz | Fiz06MK0048; Fiz06MK0049 | Fiz06YG0015 | AU |

> 2026-10-01: Tek ölçülebilir hedef taramasıyla güncellendi (bir MK = bir soruyla tamamı ölçülebilen tek hedef). Tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 8 mikro kazanım (8 yeni, 0 yeniden kullanım); yeni olanlardan 5 Bilgi, 3 Beceri.

---

## 3. Örnek ölçme maddeleri

**Fiz06MK0055:** Aynı depremin iki farklı şehirde farklı etkiler göstermesi hangi kavramla açıklanır?  
A) Büyüklük (Fiz06YG0013) · B) Şiddet ✔ · C) Odak derinliği değişir · D) Magnitüd değişir

**Fiz06MK0059:** Aynı depremde 5 katlı binalar zarar görmezken 15 katlı binaların hasar görmesini rezonans kavramıyla açıklayın. ("Hasar sadece büyüklüğe bağlıdır" yanıtı Fiz06YG0015 yanılgısını gösterir.)

**Fiz06MK0058:** Performans görevi: sosyal medyadaki bir "deprem tahmini" iddiasını araştırın, kaynaklarını ve bilimsel tutarlılığını değerlendirin. Rubrik: soru (b), kaynak (c), doğruluk değerlendirmesi (ç), çıkarım (d); her ölçüt 1–4.

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
