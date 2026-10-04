# Mikro Kazanım Ayrıştırması: MAT.8.2.4 (taslak v0.1)

> **MAT.8.2.4** Doğrusal fonksiyonlara ilişkin problemlerin çözümlerini algoritma ifade yöntemlerini kullanarak yapılandırabilme
> a) Çözüm adımlarını ve ilişkileri açıklar
> b) Algoritma ifade yöntemlerini kullanarak uyumlu bir bütün oluşturur
>
> Kaynak: https://tymm.meb.gov.tr/ortaokul-matematik-dersi/unite/473
> Sınıf teması: Mat08-T2 (Cebirsel Düşünme ve Değişimler) · Ana tema: 02 Cebirsel Düşünme ve Değişimler
> Sınırlama (TYMM): Algoritma ifade yöntemleri: doğal dil, akış şeması ve Türkçe sözde kod. Problemler gerçek yaşamdan seçilir; girdi (bağımsız) ve çıktı (bağımlı) değişkenler belirtilir; koşul içeren karar yapıları tartışılabilir.
> Ön öğrenmeler: birinci dereceden denklem ve eşitsizlikler, oranı yorumlama, temel cebirsel işlemler (TYMM temel kabulü).

Yöntem: fizikle aynı 8 adım (`Fizik/mikro-kazanimlar/FIZ.10.3.4-esdeger-direnc.md`); kodlama ve Bilgi/Beceri ölçütü: EVALORA kökündeki `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Mat02YG0020 | Bağımlı değişken algoritmanın girdisidir. |
| Mat02YG0005 | Algoritmada adımların sırası sonucu etkilemez. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Mat02MK0142 | Doğrusal fonksiyon problemine ait girdi (bağımsız) ve çıktı (bağımlı) değişkenlerini belirler. | Bilgi | a | Anlama | Mat02MK0111 | Mat02YG0020 | ÇS |
| Mat02MK0143 | Problemin çözüm adımlarını sıralı olarak doğal dille açıklar. | Beceri | a | Uygulama | Mat02MK0142 | Mat02YG0005 | AU |
| Mat02MK0144 | Çözüm adımları arasındaki ilişkileri belirtir. | Beceri | a | Analiz | Mat02MK0143 | – | AU |
| Mat02MK0145 | Çözümdeki koşula bağlı karar noktalarını belirtir. | Beceri | a | Analiz | Mat02MK0143 | – | AU |
| Mat02MK0146 | Çözümü akış şemasıyla ifade eder. | Beceri | b | Uygulama | Mat02MK0144; Mat02MK0145; Mat02MK0093 | – | AU, PG |
| Mat02MK0147 | Çözümü Türkçe sözde kodla ifade eder. | Beceri | b | Uygulama | Mat02MK0144; Mat02MK0145; Mat02MK0093 | – | AU |
| Mat02MK0148 | Oluşturduğu algoritmayı örnek girdilerle adım adım işleterek doğruluğunu kontrol eder. | Beceri | b | Değerlendirme | Mat02MK0146; Mat02MK0147 | Mat02YG0005 | PG |

> 2026-10-01: Tek ölçülebilir hedef bölmesi ve yeniden numaralama sonrası tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 6 mikro kazanım (6 yeni, 0 yeniden kullanım); yeni olanlardan 1 Bilgi, 5 Beceri.

---

## 3. Örnek ölçme maddeleri

**Mat02MK0142:** "Bir spor salonu aylık 300 TL ücretin yanında her ders için 50 TL alıyor." Algoritmanın girdisi nedir?  
A) Toplam ücret (Mat02YG0020) · B) Ders sayısı ✔ · C) 300 TL · D) 50 TL

**Mat02MK0148:** Performans görevi: su faturası hesaplayan akış şeması ve sözde kod hazırlayıp üç farklı tüketim değeriyle işletin. Rubrik: girdi-çıktı (a), adımların sırası ve ilişkiler (a), iki yöntemin tutarlılığı (b), test ve düzeltme (b).

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
