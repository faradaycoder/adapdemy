# Mikro Kazanım Ayrıştırması: FİZ.10.3.7 (taslak v0.1)

> **FİZ.10.3.7** Topraklama olayının önemini sorgulayabilme
> a) Topraklamayı tanımlar
> b) İlgili sorular sorar
> c) Bilgi toplar
> ç) Bilgilerin doğruluğunu değerlendirir
> d) Önem hakkında çıkarım yapar
>
> Kaynak: https://tymm.meb.gov.tr/fizik-dersi/unite/111
> Sınıf ünitesi: Fiz10-U3 (Elektrik) · Ana ünite: 05 Elektrik ve Manyetizma
> Sınırlama (TYMM): TYMM bu çıktı için sınırlama belirtmemiştir.
> Ön öğrenmeler: direnç ve bağlı olduğu faktörler, devre elemanlarını temsil eden semboller, iletken ve yalıtkan malzemeler (TYMM ön kabulü).

Yöntem: `FIZ.10.3.4-esdeger-direnc.md` dosyasındaki 8 adım; kodlama ve Bilgi/Beceri ölçütü: `KODLAMA.md`.

Tasarım notu: Sorgulama çıktısı olduğu için ağırlıklı ölçme performans görevi + rubriktir.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Fiz05YG0015 | Topraklama yalnızca yıldırıma karşı yapılır. |
| Fiz05YG0016 | Toprak hattı ile nötr (sıfır) hattı aynı şeydir. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Fiz05MK0079 | Topraklamayı, cihazın metal gövdesinin iletkenle toprağa bağlanarak kaçak yüklerin toprağa aktarılması olarak tanımlar. | Bilgi | a | Anlama | Fiz05MK0016; Fiz05MK0017 | Fiz05YG0015 | ÇS |
| Fiz05MK0080 | Priz ve fişte toprak hattını faz ve nötr hatlarından ayırt eder. | Bilgi | a | Anlama | Fiz05MK0079 | Fiz05YG0016 | ÇS |
| Fiz05MK0081 | Topraklamanın önemine ilişkin araştırılabilir sorular sorar. | Beceri | b | Uygulama | Fiz05MK0079 | – | PG |
| Fiz05MK0082 | Topraklamanın işlevi ve uygulamasına ilişkin güvenilir kaynaklardan bilgi toplar. | Beceri | c | Uygulama | Fiz05MK0081 | – | PG |
| Fiz05MK0083 | Topraklamayla ilgili bilgilerin doğruluğunu kaynağın güvenilirliği ve fiziksel tutarlılık açısından değerlendirir. | Beceri | ç | Değerlendirme | Fiz05MK0082 | – | PG |
| Fiz05MK0084 | Kaçak akımda topraklamanın akımı insan yerine düşük dirençli toprak hattından geçirdiğini açıklayarak can güvenliği için önemini çıkarır. | Bilgi | d | Analiz | Fiz05MK0079; Fiz05MK0070; Fiz05MK0071; Fiz05MK0072 | Fiz05YG0015 | AU |
| Fiz05MK0085 | Paratoner ile cihaz topraklamasının ortak ilkesini (yüklerin düşük dirençli yolla toprağa aktarılması) açıklar. | Bilgi | d | Analiz | Fiz05MK0084 | Fiz05YG0015 | AU |

> 2026-10-01: Tek ölçülebilir hedef taramasıyla güncellendi (bir MK = bir soruyla tamamı ölçülebilen tek hedef). Tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 7 mikro kazanım (7 yeni, 0 yeniden kullanım); yeni olanlardan 4 Bilgi, 3 Beceri.

---

## 3. Örnek ölçme maddeleri

**Fiz05MK0084:** Gövdesine kaçak akım olan topraklı ve topraksız iki çamaşır makinesine dokunan kişiler için ne olur? Açıklayın. ("Topraklama sadece yıldırım içindir" yanıtı Fiz05YG0015 yanılgısını gösterir.)

**Fiz05MK0083:** Performans görevi: topraklamayla ilgili üç iddiayı (biri yanlış) araştırıp doğruluğunu kaynak göstererek değerlendirin. Rubrik: soru kalitesi (b), kaynak güvenilirliği (c), doğruluk değerlendirmesi (ç), çıkarım (d).

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
