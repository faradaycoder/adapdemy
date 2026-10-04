# Mikro Kazanım Ayrıştırması: FİZ.10.2.2 (taslak v0.1)

> **FİZ.10.2.2** İş, enerji ve güç kavramlarına ilişkin çıkarım yapabilme
> a) İş, enerji ve güç kavramları hakkında mevcut bilgisi dâhilinde hipotez kurar
> b) İş, enerji ve güç kavramlarına yönelik ilişkileri listeler
> c) İş, enerji ve güç kavramlarını karşılaştırır
> ç) İş ve güç kavramları arasındaki ilişkiye yönelik önermelerde bulunur
> d) Önermelerini matematiksel modele dönüştürerek değerlendirir
>
> Kaynak: https://tymm.meb.gov.tr/fizik-dersi/unite/108
> Sınıf ünitesi: Fiz10-U2 (Enerji) · Ana ünite: 04 Enerji
> Sınırlama (TYMM): TYMM bu çıktı için sınırlama belirtmemiştir.
> Ön öğrenmeler: iş ve enerji kavramları hakkında temel düzeyde bilgi (TYMM ön kabulü).

Yöntem: `FIZ.10.3.4-esdeger-direnc.md` dosyasındaki 8 adım; kodlama ve Bilgi/Beceri ölçütü: `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Fiz04YG0013 | Enerji kullanıldıkça harcanıp yok olur. |
| Fiz04YG0014 | İş ve enerji farklı birimlerle ölçülür. |
| Fiz04YG0015 | Güç ile enerji (ya da iş) aynı kavramdır; güçlü makine her zaman daha çok iş yapar. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Fiz04MK0062 | İş, enerji ve güç arasındaki ilişki hakkında mevcut bilgisine dayalı sınanabilir bir hipotez kurar. | Beceri | a | Uygulama | Fiz04MK0059 | – | AU |
| Fiz04MK0063 | Enerjiyi iş yapabilme yeteneği olarak tanımlar. | Bilgi | b | Anlama | Fiz04MK0059 | – | ÇS |
| Fiz04MK0064 | Yapılan işin aktarılan enerjiye eşit olduğunu belirtir. | Bilgi | b | Anlama | Fiz04MK0059 | Fiz04YG0013 | ÇS |
| Fiz04MK0065 | İşin birimini (joule) belirtir. | Bilgi | b | Hatırlama | Fiz04MK0059 | Fiz04YG0014 | ÇS |
| Fiz04MK0066 | Enerjinin birimini (joule) belirtir. | Bilgi | b | Hatırlama | Fiz04MK0063; Fiz04MK0064 | Fiz04YG0014 | ÇS |
| Fiz04MK0067 | Gücün birimini (watt) belirtir. | Bilgi | b | Hatırlama | Fiz04MK0068 | – | ÇS |
| Fiz04MK0068 | Gücü birim zamanda yapılan iş (aktarılan enerji) olarak tanımlar. | Bilgi | c | Hatırlama | Fiz04MK0059; Fiz04MK0064 | – | ÇS |
| Fiz04MK0069 | Güç kavramını iş kavramından ayırt eder. | Bilgi | c | Hatırlama | Fiz04MK0063; Fiz04MK0064; Fiz04MK0068 | Fiz04YG0015 | ÇS |
| Fiz04MK0070 | Aynı işi daha kısa sürede yapan sistemin gücünün daha büyük olduğuna yönelik önermede bulunur. | Bilgi | ç | Analiz | Fiz04MK0068; Fiz04MK0069 | Fiz04YG0015 | ÇS, AU |
| Fiz04MK0071 | P = W / t modelini kullanarak güç, iş ya da süreyi hesaplar. | Beceri | d | Uygulama | Fiz04MK0068; Fiz04MK0069; Fiz04MK0059 | – | ÇS |
| Fiz04MK0072 | İş ve güce ilişkin önermelerini P = W / t modeliyle sınayarak değerlendirir (ör. iki motorun karşılaştırılması). | Beceri | d | Değerlendirme | Fiz04MK0070; Fiz04MK0071 | Fiz04YG0015 | AU |

> 2026-10-01: Tek ölçülebilir hedef taramasıyla güncellendi (bir MK = bir soruyla tamamı ölçülebilen tek hedef). Tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 7 mikro kazanım (7 yeni, 0 yeniden kullanım); yeni olanlardan 4 Bilgi, 3 Beceri.

---

## 3. Örnek ölçme maddeleri

**Fiz04MK0070:** A vinci bir yükü 10 s'de, B vinci aynı yükü aynı yüksekliğe 20 s'de çıkarıyor. Hangisi doğrudur?  
A) A daha çok iş yapmıştır (Fiz04YG0015) · B) İşler eşit, A'nın gücü büyüktür ✔ · C) B'nin gücü büyüktür · D) İşler ve güçler eşittir

**Fiz04MK0071:** 600 J'lük işi 30 s'de yapan motorun gücü kaç W'tır?  
A) 20 ✔ · B) 18 000 · C) 570 · D) 0,05

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
