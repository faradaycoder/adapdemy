# Mikro Kazanım Ayrıştırması: FİZ.10.3.6 (taslak v0.1)

> **FİZ.10.3.6** Elektrik akımının oluşturabileceği tehlikelere karşı alınması gereken önlemlerle ilgili bilgi toplayabilme
> a) Bilgiye ulaşmak için kullanacağı araçları belirler
> b) Belirlediği aracı kullanarak bilgileri bulur
> c) Bilgileri doğrular
> ç) Bilgileri kaydeder
>
> Kaynak: https://tymm.meb.gov.tr/fizik-dersi/unite/111
> Sınıf ünitesi: Fiz10-U3 (Elektrik) · Ana ünite: 05 Elektrik ve Manyetizma
> Sınırlama (TYMM): TYMM bu çıktı için sınırlama belirtmemiştir.
> Ön öğrenmeler: direnç ve bağlı olduğu faktörler, devre elemanlarını temsil eden semboller, iletken ve yalıtkan malzemeler (TYMM ön kabulü).

Yöntem: `FIZ.10.3.4-esdeger-direnc.md` dosyasındaki 8 adım; kodlama ve Bilgi/Beceri ölçütü: `KODLAMA.md`.

Tasarım notu: Bilgi toplama çıktısı olduğu için ağırlıklı ölçme performans görevi + rubriktir; fiziksel içerik (kısa devre, akımın vücuda etkisi, koruma elemanları) ayrı mikro kazanımlarla ÇS ile de ölçülür.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Fiz05YG0013 | Elektrik çarpmasının tehlikesi yalnızca gerilimin büyüklüğüne bağlıdır; vücut direnci, akımın süresi ve izlediği yol önemsizdir. |
| Fiz05YG0014 | Sigorta insanı elektrik çarpmasına karşı korur. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Fiz05MK0067 | Elektrik güvenliği konusunda bilgiye ulaşmak için güvenilir araçları (resmî kurum yayınları, ders kitabı, uzman görüşü, bilimsel kaynaklar) belirler. | Beceri | a | Uygulama | – | – | PG |
| Fiz05MK0068 | Kısa devrede direncin çok küçülmesi nedeniyle akımın çok büyüdüğünü açıklar. | Bilgi | b | Anlama | Fiz05MK0032; Fiz05MK0038 | – | ÇS |
| Fiz05MK0069 | Kısa devrede büyüyen akımın ısınma ve yangın tehlikesi oluşturduğunu açıklar. | Bilgi | b | Anlama | Fiz05MK0068 | – | ÇS |
| Fiz05MK0070 | Vücuttan geçen akımın etkisinin akım şiddetine bağlı olduğunu açıklar. | Bilgi | b | Anlama | Fiz05MK0010 | Fiz05YG0013 | ÇS |
| Fiz05MK0071 | Vücuttan geçen akımın etkisinin akımın geçme süresine bağlı olduğunu açıklar. | Bilgi | b | Anlama | Fiz05MK0010 | Fiz05YG0013 | ÇS |
| Fiz05MK0072 | Vücuttan geçen akımın etkisinin akımın vücutta izlediği yola bağlı olduğunu açıklar. | Bilgi | b | Anlama | Fiz05MK0010 | Fiz05YG0013 | ÇS |
| Fiz05MK0073 | Belirlediği araçlarla elektrik çarpması, kısa devre, aşırı akım ve yangın tehlikelerine ilişkin bilgileri bulur. | Beceri | b | Uygulama | Fiz05MK0067 | – | PG |
| Fiz05MK0074 | Sigortanın aşırı akımda devreyi keserek koruma işlevini açıklar. | Bilgi | b | Anlama | Fiz05MK0068; Fiz05MK0069 | Fiz05YG0014 | ÇS |
| Fiz05MK0075 | Kaçak akım rölesinin kaçak akımda devreyi keserek koruma işlevini açıklar. | Bilgi | b | Anlama | Fiz05MK0070; Fiz05MK0079 | Fiz05YG0014 | ÇS |
| Fiz05MK0076 | Yalıtımın akımın istenmeyen yola geçmesini önleme işlevini açıklar. | Bilgi | b | Anlama | Fiz05MK0011; Fiz05MK0070 | – | ÇS |
| Fiz05MK0077 | Bulduğu bilgileri en az iki bağımsız ve güvenilir kaynakla karşılaştırarak doğrular. | Beceri | c | Değerlendirme | Fiz05MK0073 | – | PG |
| Fiz05MK0078 | Doğrulanmış önlemleri kaynaklarıyla birlikte düzenli biçimde (tablo, afiş, broşür) kaydeder. | Beceri | ç | Uygulama | Fiz05MK0077 | – | PG |

> 2026-10-01: Tek ölçülebilir hedef taramasıyla güncellendi (bir MK = bir soruyla tamamı ölçülebilen tek hedef). Tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)

Özet: 7 mikro kazanım (7 yeni, 0 yeniden kullanım); yeni olanlardan 3 Bilgi, 4 Beceri.

---

## 3. Örnek ölçme maddeleri

**Fiz05MK0074:** Islak zeminde arızalı çamaşır makinesine dokunan kişiyi hangisi korur?  
A) Sigorta (Fiz05YG0014) · B) Kaçak akım rölesi ✔ · C) Uzatma kablosu · D) Anahtar

**Fiz05MK0078:** Performans görevi: "Evimizde elektrik güvenliği" broşürü hazırlayın. Rubrik: araç seçimi (a), bilgi kapsamı (b), en az iki kaynakla doğrulama (c), düzenli kayıt ve kaynak gösterimi (ç); her ölçüt 1–4 puan, "yeterli" = her ölçütte en az 3.

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
