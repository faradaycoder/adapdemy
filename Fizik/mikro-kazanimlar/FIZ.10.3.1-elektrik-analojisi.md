# Mikro Kazanım Ayrıştırması: FİZ.10.3.1 (taslak v0.1)

> **FİZ.10.3.1** Basit elektrik devresinde potansiyel fark, elektrik akımı ve direnç kavramlarının tanımına ilişkin analojik akıl yürütebilme
> a) Basit devre ile su tesisatı bileşenlerini gözlemler
> b) Benzerlikleri ve farklılıkları tespit eder
> c) Benzerliklere dayalı tanım hakkında çıkarım yapar
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
| Fiz05YG0002 | Akım ile potansiyel fark aynı kavramdır; birbirinin yerine kullanılabilir. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Fiz05MK0001 | Basit elektrik devresinin bileşenlerini (üreteç, iletken tel, direnç, anahtar) gözlemleyerek listeler. | Beceri | a | Uygulama | – | – | AU, PG |
| Fiz05MK0002 | Su tesisatının bileşenlerini (pompa, boru, dar boru, vana) gözlemleyerek listeler. | Beceri | a | Uygulama | – | – | AU, PG |
| Fiz05MK0003 | Üreteci su tesisatındaki pompayla eşleştirir. | Bilgi | b | Anlama | Fiz05MK0001; Fiz05MK0002 | – | ÇS |
| Fiz05MK0004 | Elektrik akımını su akışıyla eşleştirir. | Bilgi | b | Anlama | Fiz05MK0001; Fiz05MK0002 | – | ÇS |
| Fiz05MK0005 | Potansiyel farkı basınç farkıyla eşleştirir. | Bilgi | b | Anlama | Fiz05MK0001; Fiz05MK0002 | – | ÇS |
| Fiz05MK0006 | Direnci dar boruyla eşleştirir. | Bilgi | b | Anlama | Fiz05MK0001; Fiz05MK0002 | – | ÇS |
| Fiz05MK0007 | Anahtarı vanayla eşleştirir. | Bilgi | b | Anlama | Fiz05MK0001; Fiz05MK0002 | – | ÇS |
| Fiz05MK0008 | Analojinin sınırlarını tespit eder (ör. yüklerin telde zaten bulunması, devrenin kapalı olma zorunluluğu). | Bilgi | b | Analiz | Fiz05MK0003; Fiz05MK0004; Fiz05MK0005; Fiz05MK0006; Fiz05MK0007 | Fiz05YG0001 | AU |
| Fiz05MK0009 | Potansiyel farkı, yükleri devrede hareket ettiren etki (basınç farkı benzeri) olarak tanımlar. | Bilgi | c | Anlama | Fiz05MK0003; Fiz05MK0005 | Fiz05YG0002 | ÇS |
| Fiz05MK0010 | Elektrik akımını birim zamanda iletken kesitinden geçen yük miktarı (su akışı benzeri) olarak tanımlar. | Bilgi | c | Anlama | Fiz05MK0004 | Fiz05YG0001 | ÇS |
| Fiz05MK0011 | Direnci iletkenin akıma karşı gösterdiği zorluk (dar boru benzeri) olarak tanımlar. | Bilgi | c | Anlama | Fiz05MK0006 | – | ÇS |
| Fiz05MK0012 | Akım, potansiyel fark ve direnç kavramlarını birbirinden ayırt eder. | Bilgi | c | Anlama | Fiz05MK0009; Fiz05MK0010; Fiz05MK0011 | Fiz05YG0002 | ÇS |
| Fiz05MK0013 | Akımın birimini (amper) belirtir. | Bilgi | c | Hatırlama | Fiz05MK0010 | – | ÇS |
| Fiz05MK0014 | Potansiyel farkın birimini (volt) belirtir. | Bilgi | c | Hatırlama | Fiz05MK0009 | – | ÇS |
| Fiz05MK0015 | Direncin birimini (ohm) belirtir. | Bilgi | c | Hatırlama | Fiz05MK0011 | – | ÇS |

> 2026-10-01: Tek ölçülebilir hedef taramasıyla güncellendi (bir MK = bir soruyla tamamı ölçülebilen tek hedef). Tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 7 mikro kazanım (7 yeni, 0 yeniden kullanım); yeni olanlardan 6 Bilgi, 1 Beceri.

---

## 3. Örnek ölçme maddeleri

**Fiz05MK0003:** Su tesisatı analojisinde pompa devrenin hangi elemanına karşılık gelir?  
A) Direnç · B) Üreteç ✔ · C) Anahtar · D) Akım

**Fiz05MK0008:** Su tesisatı analojisinin elektrik devresini açıklamakta yetersiz kaldığı bir durumu açıklayın. (Beklenen: yükler telde zaten vardır, pil yük üretmez/depolamaz. "Pil akımı depolar" yanıtı Fiz05YG0001 yanılgısını gösterir.)

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
