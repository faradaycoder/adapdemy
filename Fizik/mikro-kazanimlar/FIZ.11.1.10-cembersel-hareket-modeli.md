# Mikro Kazanım Ayrıştırması: FİZ.11.1.10 (taslak v0.1)

> **FİZ.11.1.10** Düzgün çembersel hareketin değişkenleri arasındaki ilişkilerin matematiksel olarak modellenmesine ilişkin tümevarımsal akıl yürütebilme
> a) İlişkileri matematiksel olarak modeller.
> b) Hesaplamalar yaparak modelleri geneller.
>
> Kaynak: https://tymm.meb.gov.tr/fizik-dersi/unite/243
> Sınıf ünitesi: Fiz11-U1 (Kuvvet ve Hareket) · Ana ünite: 02 Kuvvet ve Hareket

Yöntem: `Fizik/mikro-kazanimlar/FIZ.10.3.4-esdeger-direnc.md` dosyasındaki adımlar; kodlama, Bilgi/Beceri ve işlem türü ölçütü: `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Fiz02YG0029 | Çembersel hareket yapan cisme dışa doğru bir merkezkaç kuvveti etki eder. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | İşlem türü | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|---|
| Fiz02MK0152 | Çizgisel sürati tanımlar. | Bilgi | Tanıma ve hatırlama | a | Hatırlama | Fiz02MK0149; Fiz02MK0042 | – | ÇS |
| Fiz02MK0153 | Açısal hızı tanımlar. | Bilgi | Tanıma ve hatırlama | a | Hatırlama | Fiz02MK0149 | – | ÇS |
| Fiz02MK0154 | Değişkenler arasındaki ilişkiden v = 2πr/T modeline ulaşır. | Beceri | Model kurma | a | Analiz | Fiz06MK0003; Fiz02MK0152 | – | AU |
| Fiz02MK0155 | Değişkenler arasındaki ilişkiden ω = 2π/T modeline ulaşır. | Beceri | Model kurma | a | Analiz | Fiz06MK0003; Fiz02MK0153 | – | AU |
| Fiz02MK0156 | Değişkenler arasındaki ilişkiden v = ω·r modeline ulaşır. | Beceri | Model kurma | a | Analiz | Fiz02MK0152; Fiz02MK0153 | – | AU |
| Fiz02MK0157 | Merkezcil ivmeyi çemberin merkezine yönelen ivme olarak tanımlar. | Bilgi | Tanıma ve hatırlama | a | Hatırlama | Fiz02MK0151; Fiz02MK0045 | – | ÇS |
| Fiz02MK0158 | Merkezcil kuvveti çemberin merkezine yönelen net kuvvet olarak tanımlar. | Bilgi | Tanıma ve hatırlama | a | Hatırlama | Fiz02MK0157; Fiz02MK0114 | Fiz02YG0029 | ÇS |
| Fiz02MK0159 | Değişkenler arasındaki ilişkiden a = v²/r modeline ulaşır. | Beceri | Model kurma | a | Analiz | Fiz02MK0154; Fiz02MK0157 | – | AU |
| Fiz02MK0160 | Değişkenler arasındaki ilişkiden F = m·v²/r modeline ulaşır. | Beceri | Model kurma | a | Analiz | Fiz02MK0159; Fiz02MK0158; Fiz02MK0114 | – | AU |
| Fiz02MK0161 | Düzgün çembersel harekette periyodu hesaplar. | Beceri | Kural uygulama | b | Uygulama | Fiz02MK0154; Fiz02MK0155 | – | ÇS, AU |
| Fiz02MK0162 | Düzgün çembersel harekette frekansı hesaplar. | Beceri | Kural uygulama | b | Uygulama | Fiz02MK0161; Fiz06MK0005 | – | ÇS, AU |
| Fiz02MK0163 | Düzgün çembersel harekette çizgisel sürati hesaplar. | Beceri | Kural uygulama | b | Uygulama | Fiz02MK0154; Fiz02MK0156 | – | ÇS, AU |
| Fiz02MK0164 | Düzgün çembersel harekette açısal hızı hesaplar. | Beceri | Kural uygulama | b | Uygulama | Fiz02MK0154; Fiz02MK0155 | – | ÇS, AU |
| Fiz02MK0165 | Yatay düzlemde düzgün çembersel harekette merkezcil ivmeyi hesaplar. | Beceri | Kural uygulama | b | Uygulama | Fiz02MK0159; Fiz02MK0163 | – | ÇS |
| Fiz02MK0166 | Yatay düzlemde düzgün çembersel harekette merkezcil kuvveti hesaplar. | Beceri | Kural uygulama | b | Uygulama | Fiz02MK0160; Fiz02MK0165 | – | ÇS |
| Fiz02MK0167 | Yatay virajda merkezcil kuvveti sürtünmenin sağladığını belirleyerek güvenli dönüş süratini hesaplar. | Beceri | Transfer ve problem çözme | b | Uygulama | Fiz02MK0166; Fiz02MK0139 | Fiz02YG0029 | AU |
| Fiz02MK0168 | Eğimli virajda merkezcil kuvveti tepki kuvvetinin bileşeninin sağladığını belirleyerek güvenli dönüş süratini hesaplar. | Beceri | Transfer ve problem çözme | b | Uygulama | Fiz02MK0166; Fiz02MK0023 | Fiz02YG0029 | AU |
| Fiz02MK0169 | Düşey düzlemde çembersel harekette en üst noktada ip gerilmesini ya da tepki kuvvetini hesaplar. | Beceri | Transfer ve problem çözme | b | Uygulama | Fiz02MK0166; Fiz02MK0125 | Fiz02YG0029 | ÇS |
| Fiz02MK0170 | Düşey düzlemde çembersel harekette en alt noktada ip gerilmesini ya da tepki kuvvetini hesaplar. | Beceri | Transfer ve problem çözme | b | Uygulama | Fiz02MK0166; Fiz02MK0125 | Fiz02YG0029 | ÇS |
| Fiz06MK0003 | Periyodu bir tekrarın süresi olarak tanımlar. | Bilgi | Tanıma ve hatırlama | a | Hatırlama | Fiz06MK0001 | – | ÇS |
| Fiz06MK0004 | Frekansı birim zamandaki tekrar sayısı olarak tanımlar. | Bilgi | Tanıma ve hatırlama | a | Hatırlama | Fiz06MK0001 | – | ÇS |
| Fiz06MK0005 | Periyot ile frekans arasındaki T = 1 / f ilişkisini kurar. | Bilgi | Çıkarım ve ilişkilendirme | a | Hatırlama | Fiz06MK0003; Fiz06MK0004 | – | ÇS |

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi (rubrikle)

Özet: 22 mikro kazanım (19 yeni, 3 yeniden kullanım); yeni olanlardan 4 Bilgi, 15 Beceri.

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
