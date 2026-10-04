# Mikro Kazanım Ayrıştırması: MAT.8.1.4 (taslak v0.1)

> **MAT.8.1.4** Gerçek sayıları ve aralıklarını sayı doğrusunda yorumlayabilme
> a) Doğal sayılardan gerçek sayılara tüm sayıları inceler
> b) Gerçek sayıları sayı doğrusuna yerleştirir
> c) Gerçek sayı aralıkları arasındaki ilişkiyi açıklar
>
> Kaynak: https://tymm.meb.gov.tr/ortaokul-matematik-dersi/unite/472
> Sınıf teması: Mat08-T1 (Sayılar ve Nicelikler) · Ana tema: 01 Sayılar ve Nicelikler
> Sınırlama (TYMM): TYMM bu çıktı için sınırlama belirtmemiştir.
> Ön öğrenmeler: rasyonel sayıları ve basamak değerlerini yorumlama, rasyonel sayılarla dört işlem, doğal sayının karesini ve küpünü ifade etme (TYMM temel kabulü).

Yöntem: fizikle aynı 8 adım (`Fizik/mikro-kazanimlar/FIZ.10.3.4-esdeger-direnc.md`); kodlama ve Bilgi/Beceri ölçütü: EVALORA kökündeki `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Mat01YG0038 | İki gerçek sayı arasında sonlu sayıda sayı vardır (ör. 1 ile 2 arasında hiç sayı yoktur ya da yalnızca birkaç ondalık sayı vardır). |
| Mat01YG0039 | Açık aralık uç noktalarını da içerir; açık ve kapalı aralık aynı biçimde gösterilir. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Mat01MK0223 | Doğal, tam, rasyonel ve irrasyonel sayıların gerçek sayılar içindeki ilişkisini şema ile gösterir. | Bilgi | a | Anlama | Mat01MK0222 | – | ÇS |
| Mat01MK0224 | Rasyonel ve irrasyonel sayıları (ör. √2, √7) sayı doğrusunda yaklaşık yerlerine yerleştirir. | Beceri | b | Uygulama | Mat01MK0214; Mat01MK0223 | – | ÇS |
| Mat01MK0225 | Gerçek sayıları büyüklüklerine göre sıralar. | Beceri | b | Uygulama | Mat01MK0224; Mat01MK0141 | – | ÇS |
| Mat01MK0226 | Sayı doğrusunda iki nokta arasındaki tüm gerçek sayıların bir aralık oluşturduğunu açıklar. | Bilgi | c | Anlama | Mat01MK0224 | – | ÇS |
| Mat01MK0227 | İki gerçek sayı arasında sonsuz sayıda gerçek sayı bulunduğunu açıklar. | Bilgi | c | Anlama | Mat01MK0224 | Mat01YG0038 | ÇS |
| Mat01MK0228 | Açık aralığı sembolle ve sayı doğrusunda gösterir. | Beceri | c | Uygulama | Mat01MK0226 | Mat01YG0039 | ÇS |
| Mat01MK0229 | Kapalı aralığı sembolle ve sayı doğrusunda gösterir. | Beceri | c | Uygulama | Mat01MK0226 | Mat01YG0039 | ÇS |
| Mat01MK0230 | Yarı açık aralığı sembolle ve sayı doğrusunda gösterir. | Beceri | c | Uygulama | Mat01MK0226 | – | ÇS |
| Mat01MK0231 | İki aralığın ortak elemanlarını sayı doğrusunda yorumlar. | Beceri | c | Analiz | Mat01MK0228; Mat01MK0229; Mat01MK0230 | Mat01YG0039 | AU |
| Mat01MK0232 | İki aralığın farklı elemanlarını sayı doğrusunda yorumlar. | Beceri | c | Analiz | Mat01MK0228; Mat01MK0229; Mat01MK0230 | Mat01YG0039 | AU |

> 2026-10-01: Tek ölçülebilir hedef bölmesi ve yeniden numaralama sonrası tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 6 mikro kazanım (6 yeni, 0 yeniden kullanım); yeni olanlardan 2 Bilgi, 4 Beceri.

---

## 3. Örnek ölçme maddeleri

**Mat01MK0228:** (−2, 3] aralığı hangi tam sayıları içerir?  
A) −2, −1, 0, 1, 2, 3 (Mat01YG0039) · B) −1, 0, 1, 2, 3 ✔ · C) −1, 0, 1, 2 · D) −2, −1, 0, 1, 2

**Mat01MK0226:** 1 ile 2 arasında kaç gerçek sayı vardır? Açıklayın. ("Hiç yoktur" ya da "9 tane" yanıtı Mat01YG0038 yanılgısını gösterir.)

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
