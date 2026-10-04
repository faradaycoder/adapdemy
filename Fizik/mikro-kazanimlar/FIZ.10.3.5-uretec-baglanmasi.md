# Mikro Kazanım Ayrıştırması: FİZ.10.3.5 (taslak v0.1)

> **FİZ.10.3.5** Üreteçlerin bağlanma türüne göre devreye sağladıkları potansiyel farka ilişkin bilimsel çıkarım yapabilme
> a) Seri ve paralel bağlanma türlerini tanımlar
> b) İlişkiye yönelik veri toplayarak kaydeder
> c) Verileri yorumlayarak değerlendirir
>
> Kaynak: https://tymm.meb.gov.tr/fizik-dersi/unite/111
> Sınıf ünitesi: Fiz10-U3 (Elektrik) · Ana ünite: 05 Elektrik ve Manyetizma
> Sınırlama (TYMM): Problem çözümlerinde üreteçlerin iç direnci ihmal edilir; paralel bağlamalarda yalnızca özdeş üreteçler kullanılır. (Destekleme: seri bağlı üreteçlerde ters bağlanma verilmeyebilir.)
> Ön öğrenmeler: direnç ve bağlı olduğu faktörler, devre elemanlarını temsil eden semboller, iletken ve yalıtkan malzemeler (TYMM ön kabulü).

Yöntem: `FIZ.10.3.4-esdeger-direnc.md` dosyasındaki 8 adım; kodlama ve Bilgi/Beceri ölçütü: `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Fiz05YG0011 | Ters bağlanan üreteç de toplam potansiyel farka eklenir. |
| Fiz05YG0004 | Ampermetre paralel, voltmetre seri bağlanabilir; ölçüm aletinin bağlanışı sonucu etkilemez. |
| Fiz05YG0012 | Paralel bağlanan özdeş üreteçler devreye sağlanan potansiyel farkı artırır. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Fiz05MK0023 | Ampermetreyi devreye seri bağlar. | Beceri | b | Uygulama | Fiz05MK0012; Fiz05MK0013 | Fiz05YG0004 | PG, ÇS |
| Fiz05MK0024 | Voltmetreyi devreye paralel bağlar. | Beceri | b | Uygulama | Fiz05MK0012; Fiz05MK0014 | Fiz05YG0004 | PG, ÇS |
| Fiz05MK0025 | Ampermetrenin neden seri bağlandığını açıklar. | Bilgi | b | Anlama | Fiz05MK0012; Fiz05MK0013 | – | ÇS |
| Fiz05MK0026 | Voltmetrenin neden paralel bağlandığını açıklar. | Bilgi | b | Anlama | Fiz05MK0012; Fiz05MK0014 | – | ÇS |
| Fiz05MK0058 | Devre şemasında seri bağlı üreteçleri (birinin + ucu diğerinin − ucuna bağlı) tanır. | Bilgi | a | Anlama | – | – | ÇS |
| Fiz05MK0059 | Devre şemasında paralel bağlı özdeş üreteçleri (aynı işaretli uçları aynı noktaya bağlı) tanır. | Bilgi | a | Anlama | – | – | ÇS |
| Fiz05MK0060 | Seri bağlamada ters bağlanmış üreteci tanır. | Bilgi | a | Anlama | Fiz05MK0058 | Fiz05YG0011 | ÇS |
| Fiz05MK0061 | Seri ve paralel bağlı üreteçlerin uçları arasındaki potansiyel farkı voltmetreyle ölçüp tabloya kaydeder. | Beceri | b | Uygulama | Fiz05MK0058; Fiz05MK0059; Fiz05MK0024 | – | PG |
| Fiz05MK0062 | Seri bağlı üreteçlerde toplam potansiyel farkın potansiyel farklar toplamına eşit olduğunu verilerle çıkarır. | Bilgi | c | Analiz | Fiz05MK0061 | – | ÇS, AU |
| Fiz05MK0063 | Seri bağlamada ters bağlanan üretecin potansiyel farkının toplamdan çıkarıldığını verilerle çıkarır. | Bilgi | c | Analiz | Fiz05MK0061; Fiz05MK0060 | Fiz05YG0011 | ÇS, AU |
| Fiz05MK0064 | Paralel bağlı özdeş üreteçlerin toplam potansiyel farkının tek bir üretecinkine eşit olduğunu verilerle çıkarır. | Bilgi | c | Analiz | Fiz05MK0061 | Fiz05YG0012 | ÇS |
| Fiz05MK0065 | Üreteçlerin bağlanma türüne göre devre akımını V = I·R ile hesaplar. | Beceri | c | Uygulama | Fiz05MK0062; Fiz05MK0063; Fiz05MK0064; Fiz05MK0032 | Fiz05YG0012; Fiz05YG0011 | ÇS |
| Fiz05MK0066 | Paralel bağlı özdeş üreteçlerin tek üretece göre daha uzun süre kullanılabildiğini değerlendirir. | Bilgi | c | Değerlendirme | Fiz05MK0064 | Fiz05YG0012 | AU |

> 2026-10-01: Tek ölçülebilir hedef taramasıyla güncellendi (bir MK = bir soruyla tamamı ölçülebilen tek hedef). Tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)
*(yeniden kullanım)*: Bu mikro kazanım daha önce başka bir çıktı için yazıldı; yeniden yazılmadı, bu çıktıya eşlendi.

Özet: 9 mikro kazanım (8 yeni, 1 yeniden kullanım); yeni olanlardan 6 Bilgi, 2 Beceri.

---

## 3. Örnek ölçme maddeleri

**Fiz05MK0062:** 1,5 V'luk üç pil seri bağlanmış, biri ters. Toplam potansiyel fark kaç V'tur?  
A) 4,5 (Fiz05YG0011) · B) 1,5 ✔ · C) 3 · D) 0

**Fiz05MK0064:** 1,5 V'luk özdeş iki pil paralel bağlanıyor. Devreye sağlanan potansiyel fark kaç V'tur?  
A) 3 (Fiz05YG0012) · B) 1,5 ✔ · C) 0,75 · D) 0

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
