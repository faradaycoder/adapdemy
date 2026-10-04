# Mikro Kazanım Ayrıştırması: MAT.8.7.1 (taslak v0.1)

> **MAT.8.7.1** Gerçek yaşamda karşılaşabileceği bir olayın olasılığına ilişkin farklı olasılık yaklaşımlarından (öznel, deneysel, teorik) uygun olanı belirleyerek karar verebilme
> a) Bir olayın olasılığına ilişkin karar vermeye yönelik amacı belirler
> b) Karara ilişkin bilgi toplar
> c) Karara ilişkin olasılık yaklaşımlarına yönelik önermeler oluşturur
> ç) Karara ilişkin oluşturduğu önermeleri sorgular
> d) Ulaştığı sonuca göre olasılık yaklaşımlarına ilişkin seçim yapar
> e) Olasılık yaklaşımına ilişkin seçimini verdiği karara yansıtır
>
> Kaynak: https://tymm.meb.gov.tr/ortaokul-matematik-dersi/unite/478
> Sınıf teması: Mat08-T7 (Veriden Olasılığa) · Ana tema: 07 Veriden Olasılığa
> Sınırlama (TYMM): İki veya daha fazla olaylı deneylere girilmez.
> Ön öğrenmeler: bir olayın olasılığını öznel olarak yorumlama, deneysel olasılığı göreli sıklıkla ilişkilendirme, teorik olasılığı hesaplama (TYMM temel kabulü).

Yöntem: fizikle aynı 8 adım (`Fizik/mikro-kazanimlar/FIZ.10.3.4-esdeger-direnc.md`); kodlama ve Bilgi/Beceri ölçütü: EVALORA kökündeki `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Mat07YG0007 | Öznel olasılık kişisel tahmin olduğu için karar vermede hiçbir durumda kullanılamaz. |
| Mat07YG0002 | Her olayın olasılığı eşittir; bir olay ya olur ya olmaz, bu yüzden olasılığı %50'dir. |
| Mat07YG0003 | Az sayıda denemeyle bulunan deneysel olasılık teorik olasılığa eşit olmalıdır. |
| Mat07YG0008 | Bağımsız denemelerde önceki sonuçlar sonrakini etkiler (5 kez yazı geldiyse sıradaki tura gelmelidir). |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Mat07MK0017 | Gerçek yaşam durumunda olasılığa dayalı karar vermenin amacını belirler. | Beceri | a | Uygulama | Mat07MK0005 | – | AU |
| Mat07MK0018 | Karar için gerekli bilgiyi (geçmiş veri, deney sonuçları, olası çıktılar) toplar. | Beceri | b | Uygulama | Mat07MK0017 | – | PG |
| Mat07MK0019 | Deney ya da benzetim (simülasyon) yaparak göreli sıklıkla deneysel olasılığı hesaplar. | Beceri | b | Uygulama | Mat07MK0007; Mat07MK0018 | – | PG, ÇS |
| Mat07MK0020 | Öznel olasılığı tanımlar. | Bilgi | c | Hatırlama | Mat07MK0005 | Mat07YG0007 | ÇS |
| Mat07MK0021 | Deneysel olasılığı tanımlar. | Bilgi | c | Hatırlama | Mat07MK0008 | – | ÇS |
| Mat07MK0022 | Teorik olasılığı tanımlar. | Bilgi | c | Hatırlama | Mat07MK0011 | – | ÇS |
| Mat07MK0023 | Öznel, deneysel ve teorik olasılık yaklaşımlarını birbirinden ayırt eder. | Bilgi | c | Hatırlama | Mat07MK0020; Mat07MK0021; Mat07MK0022 | Mat07YG0007 | ÇS |
| Mat07MK0024 | Durumun eş olası çıktılara sahip olup olmadığına bakarak teorik olasılığın uygulanabilirliğini belirler. | Bilgi | c | Analiz | Mat07MK0022; Mat07MK0023 | Mat07YG0002 | ÇS |
| Mat07MK0025 | Karara ilişkin öznel olasılık yaklaşımıyla önermeler oluşturur. | Beceri | c | Analiz | Mat07MK0020; Mat07MK0018 | – | AU |
| Mat07MK0026 | Karara ilişkin deneysel olasılık yaklaşımıyla önermeler oluşturur. | Beceri | c | Analiz | Mat07MK0019; Mat07MK0021 | – | AU |
| Mat07MK0027 | Karara ilişkin teorik olasılık yaklaşımıyla önermeler oluşturur. | Beceri | c | Analiz | Mat07MK0024; Mat07MK0018 | – | AU |
| Mat07MK0028 | Deneme sayısı arttıkça deneysel olasılığın teorik olasılığa yaklaştığını benzetim verileriyle sorgular. | Bilgi | ç | Analiz | Mat07MK0019; Mat07MK0022 | Mat07YG0003; Mat07YG0008 | ÇS, AU |
| Mat07MK0029 | Durum için en uygun olasılık yaklaşımını gerekçesiyle seçer. | Beceri | d | Değerlendirme | Mat07MK0025; Mat07MK0026; Mat07MK0027; Mat07MK0028 | Mat07YG0007 | AU |
| Mat07MK0030 | Seçtiği yaklaşımla belirlediği olasılığı karara yansıtır ve kararını açıklar. | Beceri | e | Değerlendirme | Mat07MK0029 | – | PG |

> 2026-10-01: Tek ölçülebilir hedef bölmesi ve yeniden numaralama sonrası tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 9 mikro kazanım (9 yeni, 0 yeniden kullanım); yeni olanlardan 3 Bilgi, 6 Beceri.

---

## 3. Örnek ölçme maddeleri

**Mat07MK0028:** Bir para 5 kez atılıyor ve 5'inde de yazı geliyor. 6. atışta tura gelme olasılığı nedir?  
A) 1'e yakın, çünkü artık tura gelmeli (Mat07YG0008) · B) 1/2 ✔ · C) 1/6 · D) 0

**Mat07MK0024:** Yarın deprem olma olasılığı için hangisi doğrudur?  
A) %50'dir, ya olur ya olmaz (Mat07YG0002) · B) Teorik olasılık kullanılamaz; geçmiş veriye dayalı tahmin gerekir ✔ · C) 1/365'tir · D) 0'dır

**Mat07MK0030:** Performans görevi: okul kantini için "yarın hangi sandviçten kaç tane hazırlanmalı?" kararını, geçmiş satış verisi ve benzetimle destekleyerek verin. Rubrik: amaç (a), bilgi toplama (b), yaklaşım önermeleri (c), sorgulama (ç), yaklaşım seçimi (d), karar ve gerekçe (e).

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
