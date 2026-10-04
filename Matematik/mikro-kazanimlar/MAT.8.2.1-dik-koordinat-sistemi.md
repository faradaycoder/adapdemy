# Mikro Kazanım Ayrıştırması: MAT.8.2.1 (taslak v0.1)

> **MAT.8.2.1** Gerçek yaşam durumları üzerinden dik koordinat sistemini çözümleyebilme
> a) Dik koordinat sisteminin bileşenlerini belirler
> b) Bileşenler arasındaki ilişkileri belirler
>
> Kaynak: https://tymm.meb.gov.tr/ortaokul-matematik-dersi/unite/473
> Sınıf teması: Mat08-T2 (Cebirsel Düşünme ve Değişimler) · Ana tema: 02 Cebirsel Düşünme ve Değişimler
> Sınırlama (TYMM): Fonksiyon tanımına girilmez.
> Ön öğrenmeler: birinci dereceden denklem ve eşitsizlikler, oranı yorumlama, temel cebirsel işlemler (TYMM temel kabulü).

Yöntem: fizikle aynı 8 adım (`Fizik/mikro-kazanimlar/FIZ.10.3.4-esdeger-direnc.md`); kodlama ve Bilgi/Beceri ölçütü: EVALORA kökündeki `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Mat02YG0012 | Koordinat düzleminin bölgeleri saat yönünde numaralandırılır. |
| Mat02YG0013 | Sıralı ikilide sıra önemli değildir; (2, 3) ile (3, 2) aynı noktadır. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Mat02MK0096 | Dik koordinat sisteminde x eksenini (apsis) belirler. | Bilgi | a | Anlama | Mat01MK0129 | – | ÇS |
| Mat02MK0097 | Dik koordinat sisteminde y eksenini (ordinat) belirler. | Bilgi | a | Anlama | Mat01MK0129 | – | ÇS |
| Mat02MK0098 | Dik koordinat sisteminde orijini belirler. | Bilgi | a | Anlama | Mat02MK0096; Mat02MK0097 | – | ÇS |
| Mat02MK0099 | Dik koordinat sisteminin bölgelerini belirler. | Bilgi | a | Anlama | Mat02MK0096; Mat02MK0097 | Mat02YG0012 | ÇS |
| Mat02MK0100 | Gerçek yaşam durumlarındaki konumları (sinema koltuğu, harita) sıralı ikililerle ifade eder. | Beceri | a | Uygulama | Mat02MK0096; Mat02MK0097 | Mat02YG0013 | ÇS, AU |
| Mat02MK0101 | Sıralı ikiliye karşılık gelen noktayı koordinat sisteminde işaretler. | Beceri | b | Uygulama | Mat02MK0096; Mat02MK0097; Mat02MK0098 | Mat02YG0013 | ÇS |
| Mat02MK0102 | Koordinat sisteminde işaretli bir noktanın koordinatlarını okur. | Beceri | b | Uygulama | Mat02MK0096; Mat02MK0097 | Mat02YG0013 | ÇS |
| Mat02MK0103 | Koordinatların işaretinden noktanın hangi bölgede olduğunu belirler. | Beceri | b | Uygulama | Mat02MK0102; Mat02MK0099 | Mat02YG0012 | ÇS |
| Mat02MK0104 | Koordinatlardan noktanın hangi eksen üzerinde olduğunu belirler. | Beceri | b | Uygulama | Mat02MK0102 | – | ÇS |
| Mat02MK0105 | Düzlemdeki her noktaya bir gerçek sayı ikilisinin, her gerçek sayı ikilisine düzlemde bir noktanın karşılık geldiğini açıklar. | Bilgi | b | Anlama | Mat02MK0101; Mat02MK0102 | – | AU |

> 2026-10-01: Tek ölçülebilir hedef bölmesi ve yeniden numaralama sonrası tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 5 mikro kazanım (5 yeni, 0 yeniden kullanım); yeni olanlardan 2 Bilgi, 3 Beceri.

---

## 3. Örnek ölçme maddeleri

**Mat02MK0101:** A(−3, 5) noktası için hangisi doğrudur?  
A) Apsisi 5 (Mat02YG0013) · B) Ordinatı 5 ✔ · C) Orijindedir · D) x ekseni üzerindedir

**Mat02MK0103:** (−4, −1) noktası hangi bölgededir?  
A) I · B) II · C) III ✔ · D) IV (Mat02YG0012)

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
