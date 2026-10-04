# Mikro Kazanım Ayrıştırması: MAT.8.5.1 (taslak v0.1)

> **MAT.8.5.1** Matematiksel araç ve teknoloji yardımıyla öteleme dönüşümünü çözümleyebilme
> a) Düzlemde geometrik şekillerin öteleme dönüşümü altındaki görüntülerinin kenar ve açı özelliklerini belirler
> b) Geometrik şekiller ile öteleme dönüşümü altındaki görüntüleri arasındaki ilişkileri belirler
>
> Kaynak: https://tymm.meb.gov.tr/ortaokul-matematik-dersi/unite/476
> Sınıf teması: Mat08-T5 (Dönüşüm) · Ana tema: 05 Dönüşüm
> Sınırlama (TYMM): TYMM bu çıktı için sınırlama belirtmemiştir.
> Ön öğrenmeler: dik koordinat sisteminde noktanın yerini belirleme, yansıma dönüşümüne ilişkin çıkarım, şekil ile yansıma görüntüsü verildiğinde simetri doğrusunu oluşturma (TYMM temel kabulü).

Yöntem: fizikle aynı 8 adım (`Fizik/mikro-kazanimlar/FIZ.10.3.4-esdeger-direnc.md`); kodlama ve Bilgi/Beceri ölçütü: EVALORA kökündeki `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Mat05YG0003 | Ötelemede şeklin noktaları farklı miktarlarda kaydırılabilir. |
| Mat05YG0004 | Öteleme şeklin boyutunu ya da duruşunu (yönünü) değiştirir. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Mat05MK0016 | Araç ya da yazılımla bir çokgeni verilen yön ve uzaklıkta öteler. | Beceri | a | Uygulama | – | Mat05YG0003 | PG, ÇS |
| Mat05MK0017 | Öteleme altında görüntünün kenar uzunluklarının değişmediğini belirler. | Bilgi | a | Anlama | Mat05MK0016 | Mat05YG0004 | ÇS |
| Mat05MK0018 | Öteleme altında görüntünün açı ölçülerinin değişmediğini belirler. | Bilgi | a | Anlama | Mat05MK0016 | Mat05YG0004 | ÇS |
| Mat05MK0019 | Şekil ile ötelenmiş görüntüsünün eş olduğunu belirler. | Bilgi | b | Analiz | Mat05MK0017; Mat05MK0018 | – | ÇS |
| Mat05MK0020 | Karşılıklı noktaları birleştiren doğru parçalarının eşit uzunlukta olduğunu belirler. | Bilgi | b | Analiz | Mat05MK0017 | Mat05YG0003 | ÇS |
| Mat05MK0021 | Karşılıklı noktaları birleştiren doğru parçalarının paralel olduğunu belirler. | Bilgi | b | Analiz | Mat05MK0017; Mat05MK0018 | Mat05YG0003 | ÇS |
| Mat05MK0022 | Verilen şekil ve görüntüsünden ötelemenin yönünü belirler. | Beceri | b | Uygulama | Mat05MK0019 | – | ÇS |
| Mat05MK0023 | Verilen şekil ve görüntüsünden ötelemenin miktarını belirler. | Beceri | b | Uygulama | Mat05MK0019 | – | ÇS |

> 2026-10-01: Tek ölçülebilir hedef bölmesi ve yeniden numaralama sonrası tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 4 mikro kazanım (4 yeni, 0 yeniden kullanım); yeni olanlardan 2 Bilgi, 2 Beceri.

---

## 3. Örnek ölçme maddeleri

**Mat05MK0017:** Bir üçgen 4 birim sağa ötelendiğinde hangisi değişir?  
A) Kenar uzunlukları (Mat05YG0004) · B) Açı ölçüleri · C) Köşelerin konumu ✔ · D) Alanı

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
