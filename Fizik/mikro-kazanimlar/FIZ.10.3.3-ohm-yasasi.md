# Mikro Kazanım Ayrıştırması: FİZ.10.3.3 (taslak v0.1)

> **FİZ.10.3.3** Ohm Yasası ile ilgili tümevarımsal akıl yürütebilme
> a) Deney yoluyla ilişkiyi keşfederek matematiksel modele ulaşır
> b) Matematiksel model üzerinden genelleme yapar
>
> Kaynak: https://tymm.meb.gov.tr/fizik-dersi/unite/111
> Sınıf ünitesi: Fiz10-U3 (Elektrik) · Ana ünite: 05 Elektrik ve Manyetizma
> Sınırlama (TYMM): Üreteçlerin iç direnci ile ilgili matematiksel hesaplamalardan kaçınılır; elektromotor kuvvet kavramına girilmez; üreteçlerin iç direnci ihmal edilir.
> Ön öğrenmeler: direnç ve bağlı olduğu faktörler, devre elemanlarını temsil eden semboller, iletken ve yalıtkan malzemeler (TYMM ön kabulü).

Yöntem: `FIZ.10.3.4-esdeger-direnc.md` dosyasındaki 8 adım; kodlama ve Bilgi/Beceri ölçütü: `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Fiz05YG0004 | Ampermetre paralel, voltmetre seri bağlanabilir; ölçüm aletinin bağlanışı sonucu etkilemez. |
| Fiz05YG0005 | Bir iletkenin direnci, uçlarına uygulanan potansiyel fark arttıkça artar (R = V / I ifadesinden). |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Fiz05MK0023 | Ampermetreyi devreye seri bağlar. | Beceri | a | Uygulama | Fiz05MK0012; Fiz05MK0013 | Fiz05YG0004 | PG, ÇS |
| Fiz05MK0024 | Voltmetreyi devreye paralel bağlar. | Beceri | a | Uygulama | Fiz05MK0012; Fiz05MK0014 | Fiz05YG0004 | PG, ÇS |
| Fiz05MK0025 | Ampermetrenin neden seri bağlandığını açıklar. | Bilgi | a | Anlama | Fiz05MK0012; Fiz05MK0013 | – | ÇS |
| Fiz05MK0026 | Voltmetrenin neden paralel bağlandığını açıklar. | Bilgi | a | Anlama | Fiz05MK0012; Fiz05MK0014 | – | ÇS |
| Fiz05MK0027 | Sabit dirençli bir devrede potansiyel farkı değiştirerek karşılık gelen akım değerlerini ölçer ve tabloya kaydeder. | Beceri | a | Uygulama | Fiz05MK0023; Fiz05MK0024 | – | PG |
| Fiz05MK0028 | Ölçüm verilerinden potansiyel fark-akım grafiğini çizer. | Beceri | a | Uygulama | Fiz05MK0027 | – | AU, PG |
| Fiz05MK0029 | Potansiyel fark-akım grafiğinden doğrusal ilişkiyi belirler. | Bilgi | a | Analiz | Fiz05MK0028 | – | ÇS |
| Fiz05MK0030 | Potansiyel fark-akım grafiğinin eğiminden direnci bulur. | Beceri | a | Uygulama | Fiz05MK0029 | – | ÇS |
| Fiz05MK0031 | Grafikten V = I·R modeline ulaşır. | Beceri | a | Uygulama | Fiz05MK0029; Fiz05MK0030 | – | ÇS |
| Fiz05MK0032 | V = I·R ile bilinmeyen niceliği (potansiyel fark, akım ya da direnç) hesaplar. | Beceri | b | Uygulama | Fiz05MK0031 | – | ÇS |
| Fiz05MK0033 | Direnç sabitken akımın potansiyel farkla doğru orantılı olduğu genellemesini yapar. | Bilgi | b | Analiz | Fiz05MK0031 | – | ÇS, AU |
| Fiz05MK0034 | Direncin potansiyel farka bağlı olmadığı, iletkenin yapısına bağlı olduğu genellemesini yapar. | Bilgi | b | Analiz | Fiz05MK0030; Fiz05MK0031 | Fiz05YG0005 | ÇS, AU |

> 2026-10-01: Tek ölçülebilir hedef taramasıyla güncellendi (bir MK = bir soruyla tamamı ölçülebilen tek hedef). Tablo veri dosyasından üretildi.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney (rubrikle)
*(yeniden kullanım)*: Bu mikro kazanım daha önce başka bir çıktı için yazıldı; yeniden yazılmadı, bu çıktıya eşlendi.

Özet: 6 mikro kazanım (5 yeni, 1 yeniden kullanım); yeni olanlardan 1 Bilgi, 4 Beceri.

---

## 3. Örnek ölçme maddeleri

**Fiz05MK0032:** 10 Ω'luk dirence 30 V potansiyel fark uygulanıyor. Dirençten geçen akım kaç A'dir?  
A) 300 · B) 3 ✔ · C) 0,33 · D) 40

**Fiz05MK0033:** Bir direncin uçlarındaki potansiyel fark iki katına çıkarılıyor (sıcaklık sabit). Direnç ve akım nasıl değişir?  
A) Direnç 2 katına çıkar, akım değişmez (Fiz05YG0005) · B) Direnç değişmez, akım 2 katına çıkar ✔ · C) İkisi de 2 katına çıkar · D) İkisi de değişmez

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
