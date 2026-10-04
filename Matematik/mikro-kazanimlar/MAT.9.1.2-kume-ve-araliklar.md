# Mikro Kazanım Ayrıştırması: MAT.9.1.2 (taslak v0.1)

> **MAT.9.1.2** Gerçek sayı aralıklarının gösteriminde ve aralıklarla ilgili işlemlerde küme sembol ve işlemlerinden yararlanabilme
> a) Küme sembol ve işlemlerini tanır.
> b) Uygun olanı belirler.
> c) Kullanır.
>
> Kaynak: https://tymm.meb.gov.tr/matematik-dersi/unite/21
> Sınıf teması: Mat09-T1 (Sayılar) · Ana tema: 01 Sayılar ve Nicelikler
> Sınırlama (TYMM): Küme kavramının formel tanımına girilmez; temel sembol ve işlemlerle sınırlıdır.

Yöntem: `Fizik/mikro-kazanimlar/FIZ.10.3.4-esdeger-direnc.md` dosyasındaki adımlar; kodlama, Bilgi/Beceri ve işlem türü ölçütü: `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Mat01YG0041 | A \ B ile B \ A aynı kümedir. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | İşlem türü | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|---|
| Mat01MK0250 | Elemanı olma (∈) ve elemanı olmama (∉) sembollerini tanır. | Bilgi | Tanıma ve hatırlama | a | Hatırlama | – | – | ÇS |
| Mat01MK0251 | Alt küme (⊂) sembolünü tanır. | Bilgi | Tanıma ve hatırlama | a | Hatırlama | Mat01MK0250 | – | ÇS |
| Mat01MK0252 | Boş küme (∅) sembolünü tanır. | Bilgi | Tanıma ve hatırlama | a | Hatırlama | Mat01MK0250 | – | ÇS |
| Mat01MK0253 | Birleşim (∪) sembolünü tanır. | Bilgi | Tanıma ve hatırlama | a | Hatırlama | Mat01MK0250 | – | ÇS |
| Mat01MK0254 | Kesişim (∩) sembolünü tanır. | Bilgi | Tanıma ve hatırlama | a | Hatırlama | Mat01MK0250 | – | ÇS |
| Mat01MK0255 | Fark işleminin sembolünü tanır. | Bilgi | Tanıma ve hatırlama | a | Hatırlama | Mat01MK0250 | – | ÇS |
| Mat01MK0256 | Tümleme işleminin sembolünü tanır. | Bilgi | Tanıma ve hatırlama | a | Hatırlama | Mat01MK0250 | – | ÇS |
| Mat01MK0257 | Eleman sayısı gösterimini tanır. | Bilgi | Tanıma ve hatırlama | a | Hatırlama | Mat01MK0250 | – | ÇS |
| Mat01MK0258 | Gerçek sayı aralıklarını küme gösterimiyle ifade eder. | Beceri | Kural uygulama | b, c | Uygulama | Mat01MK0264; Mat01MK0228 | – | ÇS |
| Mat01MK0259 | Aralıklarla birleşim işlemi yapar. | Beceri | Kural uygulama | b, c | Uygulama | Mat01MK0270; Mat01MK0258 | – | ÇS |
| Mat01MK0260 | Aralıklarla kesişim işlemi yapar. | Beceri | Kural uygulama | b, c | Uygulama | Mat01MK0271; Mat01MK0231 | – | ÇS |
| Mat01MK0261 | Aralıklarla fark işlemi yapar. | Beceri | Kural uygulama | b, c | Uygulama | Mat01MK0272; Mat01MK0232 | Mat01YG0041 | ÇS |
| Mat01MK0262 | Aralıkların tümleyenini bulur. | Beceri | Kural uygulama | b, c | Uygulama | Mat01MK0273; Mat01MK0258 | – | ÇS |
| Mat01MK0263 | Kümeleri liste yöntemiyle gösterir. | Beceri | Dönüştürme | c | Uygulama | Mat01MK0250 | – | ÇS |
| Mat01MK0264 | Kümeleri ortak özellik yöntemiyle gösterir. | Beceri | Dönüştürme | c | Uygulama | Mat01MK0250 | – | ÇS |
| Mat01MK0265 | Kümeleri şema yöntemiyle gösterir. | Beceri | Dönüştürme | c | Uygulama | Mat01MK0250 | – | ÇS |
| Mat01MK0266 | Bir kümenin eleman sayısını belirler. | Beceri | Dönüştürme | c | Uygulama | Mat01MK0257 | – | ÇS |
| Mat01MK0267 | Alt kümeyi belirler. | Beceri | Ayırt etme ve sınıflama | c | Uygulama | Mat01MK0251; Mat01MK0263 | – | ÇS |
| Mat01MK0268 | Eşit kümeleri belirler. | Beceri | Ayırt etme ve sınıflama | c | Uygulama | Mat01MK0263 | – | ÇS |
| Mat01MK0269 | Bir kümenin alt küme sayısını bulur. | Beceri | Ayırt etme ve sınıflama | c | Uygulama | Mat01MK0266; Mat01MK0267 | – | ÇS |
| Mat01MK0270 | Kümelerle birleşim işlemi yapar. | Beceri | Kural uygulama | c | Uygulama | Mat01MK0253; Mat01MK0263 | – | ÇS |
| Mat01MK0271 | Kümelerle kesişim işlemi yapar. | Beceri | Kural uygulama | c | Uygulama | Mat01MK0254; Mat01MK0263 | – | ÇS |
| Mat01MK0272 | Kümelerle fark işlemi yapar. | Beceri | Kural uygulama | c | Uygulama | Mat01MK0255; Mat01MK0263 | Mat01YG0041 | ÇS |
| Mat01MK0273 | Bir kümenin tümleyenini bulur. | Beceri | Kural uygulama | c | Uygulama | Mat01MK0256; Mat01MK0263 | – | ÇS |

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi (rubrikle)

Özet: 24 mikro kazanım (24 yeni, 0 yeniden kullanım); yeni olanlardan 8 Bilgi, 16 Beceri.

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
