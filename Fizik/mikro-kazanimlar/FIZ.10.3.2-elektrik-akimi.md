# Mikro Kazanım Ayrıştırması: FİZ.10.3.2 (taslak v0.1)

> **FİZ.10.3.2** Elektrik yükünün hareketi üzerinden elektrik akımı kavramını çözümleyebilme
> a) Elektrik akımı oluşmasında değişkenleri belirler
> b) Değişkenler arasındaki ilişkiyi belirler
>
> Kaynak: https://tymm.meb.gov.tr/fizik-dersi/unite/111
> Sınıf ünitesi: Fiz10-U3 (Elektrik) · Ana ünite: 05 Elektrik ve Manyetizma
> Sınırlama (TYMM): TYMM bu çıktı için sınırlama belirtmemiştir.
> Ön öğrenmeler: direnç ve bağlı olduğu faktörler, devre elemanlarını temsil eden semboller, iletken ve yalıtkan malzemeler (TYMM ön kabulü).

Yöntem: `FIZ.10.3.4-esdeger-direnc.md` dosyasındaki 8 adım; kodlama ve Bilgi/Beceri ölçütü: `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Fiz05YG0001 | Üreteç (pil) içinde akım depolanır; pil bitince içindeki akım tükenmiştir. |
| Fiz05YG0003 | Akımın yönü, metal iletkende elektronların hareket yönüdür. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Fiz05MK0016 | Elektrik akımının oluşması için devrenin kapalı olması gerektiğini belirtir. | Bilgi | a | Anlama | Fiz05MK0010; Fiz05MK0007 | Fiz05YG0001 | ÇS |
| Fiz05MK0017 | Elektrik akımının oluşması için potansiyel fark gerektiğini belirtir. | Bilgi | a | Anlama | Fiz05MK0009 | Fiz05YG0001 | ÇS |
| Fiz05MK0018 | Akımın kesitten geçen yük miktarına bağlı olduğunu belirler. | Bilgi | a | Anlama | Fiz05MK0010 | – | ÇS |
| Fiz05MK0019 | Akımın yükün geçme süresine bağlı olduğunu belirler. | Bilgi | a | Anlama | Fiz05MK0010 | – | ÇS |
| Fiz05MK0020 | I = q / t modelini kullanarak akım, yük ya da süreyi hesaplar. | Beceri | b | Uygulama | Fiz05MK0018; Fiz05MK0019 | – | ÇS |
| Fiz05MK0021 | Metal iletkende akımı elektronların hareketiyle açıklar. | Bilgi | b | Anlama | Fiz05MK0010 | – | ÇS |
| Fiz05MK0022 | Geleneksel akım yönünü elektron hareketinin tersi olarak belirtir. | Bilgi | b | Hatırlama | Fiz05MK0021 | Fiz05YG0003 | ÇS |

> 2026-10-01: Tek ölçülebilir hedef taramasıyla güncellendi (bir MK = bir soruyla tamamı ölçülebilen tek hedef). Tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 4 mikro kazanım (4 yeni, 0 yeniden kullanım); yeni olanlardan 3 Bilgi, 1 Beceri.

---

## 3. Örnek ölçme maddeleri

**Fiz05MK0020:** Bir iletkenin kesitinden 4 s'de 12 C yük geçiyor. Akım kaç A'dir?  
A) 3 ✔ · B) 48 · C) 0,33 · D) 16

**Fiz05MK0021:** Bakır telde elektronlar A'dan B'ye hareket ediyor. Geleneksel akım yönü nedir?  
A) A'dan B'ye (Fiz05YG0003) · B) B'den A'ya ✔ · C) Akım yoktur · D) Her iki yönde

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
