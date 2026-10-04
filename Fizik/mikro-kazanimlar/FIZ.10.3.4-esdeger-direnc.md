# Mikro Kazanım Ayrıştırması: FİZ.10.3.4 (taslak v0.5)

> **FİZ.10.3.4** Dirençlerin bağlanma türlerine göre eşdeğer dirence ilişkin bilimsel çıkarım yapabilme
> a) Seri, paralel ve birleşik bağlanma türlerini tanımlar
> b) Eşdeğer direnç arasındaki ilişkiyi belirlemek üzere veri toplar ve kaydeder
> c) Verileri yorumlayarak çıkarımları matematiksel modellemeleri kullanarak test eder
>
> Kaynak: https://tymm.meb.gov.tr/fizik-dersi/unite/111
> Sınıf ünitesi: Fiz10-U3 (Elektrik) · Ana ünite: 05 Elektrik ve Manyetizma (ELK)
> Sınırlama: Kirchhoff'un potansiyel fark yasasına girilmez.
> Ön öğrenmeler: direnç ve bağlı olduğu faktörler, devre sembolleri, iletken/yalıtkan.
> Zenginleştirme (kapsam dışı, isteğe bağlı): renk kodları, Wheatstone köprüsü.

**Kodlar hakkında (v0.3):** Mikro kazanımlar sınıftan bağımsız `Fiz<ana ünite 2 hane>MK<4 hane>`, yanılgılar `Fiz<ana ünite>YG<4 hane>` biçimiyle kodlandı (kurallar: `KODLAMA.md`). Eski MK01…MK17 kodları Fiz05MK0035…Fiz05MK0052'ye, Y1…Y6 kodları Fiz05YG0010…Fiz05YG0009'ya karşılık gelir. Tek doğruluk kaynağı `veri/` klasöründeki CSV'ler ve onlardan üretilen `Fizik Mikro Kazanım.xlsx` dosyasıdır.

---

## 1. Yöntem (her kazanıma aynen uygulanacak 8 adım)

1. **Kaynağı sabitle.** Öğrenme çıktısı, süreç bileşenleri (a, b, c...), içerik çerçevesi, sınırlamalar ve ön öğrenmeler TYMM'den alınır. Sınırlamanın dışına çıkan mikro kazanım yazılmaz.
2. **Süreç bileşenlerini iskelet yap.** Her mikro kazanım tek bir süreç bileşenine bağlanır. Böylece MEB'in yapısı korunur, raporlama çıktı düzeyine geri toplanabilir.
3. **Atomik kurala göre böl.** Bir mikro kazanım: tek eylem (fiil), tek içerik, tek bağlam içerir; tek bir soruyla (en fazla 2-3 maddeyle) ölçülebilir; öğrenci bunu yapınca gözlenebilir bir çıktı oluşur. "ve" ile bağlanan iki eylem görürsen ikiye böl.
4. **Ön koşulları bağla.** Mikro kazanımın dayandığı önceki kazanımlar (aynı ünitedeki ya da önceki sınıflardaki) işaretlenir. Bu, EVALORA'nın "öğrenci neden takıldı" sorusunu geriye doğru izlemesini sağlar.
5. **Yanılgıları eşle.** Bilinen kavram yanılgıları kodlanır ve ilgili mikro kazanıma bağlanır. Çeldiriciler bu yanılgılardan üretilir, böylece yanlış cevap hangi yanılgıyı gösteriyor, bilinir.
6. **Tür ata (zorunlu).** Her mikro kazanım **Bilgi** ya da **Beceri** olarak işaretlenir. Bilgi: öğrencinin bir kavramı, tanımı, kuralı ya da ilişkiyi bilmesi, tanıması, açıklaması ("ne" ve "neden"; ölçülen şey doğru bilgidir). Beceri: öğrencinin bir işlemi, yöntemi ya da süreci yürütmesi (ölçer, kaydeder, çizer, hesaplar, bağlar, test eder, değerlendirir; ölçülen şey "yapabilmek"tir). Karar mikro kazanımın ana fiiline ve ölçmede gözlenen çıktıya göre verilir; ikisi birden varsa atomik kurala göre bölünür.
7. **Bilişsel düzey ve ölçme türü ata.** Her mikro kazanıma düzey (Hatırlama, Anlama, Uygulama, Analiz, Değerlendirme, Yaratma) ve uygun ölçme türü (çoktan seçmeli, açık uçlu, deney/performans + rubrik) atanır.
8. **Ustalık ölçütü koy.** "Öğrenci bu mikro kazanıma hâkim" demek için eşik tanımlanır (varsayılan: farklı bağlamlarda 3 maddeden en az 2'si doğru).

Kalite kontrolü: Mikro kazanımların tamamı yapıldığında üst öğrenme çıktısı kapsanmış olmalı; hiçbiri çıktının kapsamı dışına taşmamalı. Yeni mikro kazanım yazmadan önce aynı ana ünitede aynı şeyi anlatan bir kod var mı bakılır; varsa yeniden yazılmaz, eşlenir.

---

## 2. Yanılgı kataloğu

| Kod | Yanılgı |
|---|---|
| Fiz05YG0010 | Paralel bağlamada direnç eklendikçe eşdeğer direnç artar. |
| Fiz05YG0008 | Akım dirençlerde "harcanır"; seri devrede ilk dirençten sonra akım azalır. |
| Fiz05YG0006 | Bağlanma türü şemadaki görünüşe göre belirlenir (yan yana çizilen = paralel, arka arkaya çizilen = seri). |
| Fiz05YG0007 | Kısa devre edilmiş direnç de eşdeğer dirence katılır. |
| Fiz05YG0004 | Ampermetre paralel, voltmetre seri bağlanabilir; ölçüm aletinin bağlanışı sonucu etkilemez. |
| Fiz05YG0009 | Paralel hesapta 1/Reş bulunur ama ters çevrilmeden sonuç olarak yazılır. |

---

## 3. Mikro kazanımlar

**Ön koşullar (önceki kazanımlardan):**
ÖK1 Devre elemanlarının sembollerini tanır (ön öğrenme) · ÖK2 = Fiz05MK0032 V = I·R ile bilinmeyen niceliği hesaplar (FİZ.10.3.3) · ÖK3 = Fiz05MK0012 Akım, potansiyel fark ve direnci ayırt eder (FİZ.10.3.1)

| Kod | Mikro kazanım (Öğrenci...) | Tür | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|
| Fiz05MK0023 | Ampermetreyi devreye seri bağlar. | Beceri | b | Uygulama | Fiz05MK0012; Fiz05MK0013 | Fiz05YG0004 | PG, ÇS |
| Fiz05MK0024 | Voltmetreyi devreye paralel bağlar. | Beceri | b | Uygulama | Fiz05MK0012; Fiz05MK0014 | Fiz05YG0004 | PG, ÇS |
| Fiz05MK0025 | Ampermetrenin neden seri bağlandığını açıklar. | Bilgi | b | Anlama | Fiz05MK0012; Fiz05MK0013 | – | ÇS |
| Fiz05MK0026 | Voltmetrenin neden paralel bağlandığını açıklar. | Bilgi | b | Anlama | Fiz05MK0012; Fiz05MK0014 | – | ÇS |
| Fiz05MK0035 | Devre şemasında seri bağlı dirençleri, akımın izleyebileceği tek yol olmasından tanır. | Bilgi | a | Anlama | – | Fiz05YG0006 | ÇS |
| Fiz05MK0036 | Devre şemasında paralel bağlı dirençleri, uçlarının aynı iki noktaya bağlı olmasından tanır. | Bilgi | a | Anlama | – | Fiz05YG0006 | ÇS |
| Fiz05MK0037 | Birleşik bir devreyi seri ve paralel alt gruplarına ayırır. | Beceri | a | Analiz | Fiz05MK0035; Fiz05MK0036 | Fiz05YG0006 | ÇS, AU |
| Fiz05MK0038 | Kısa devre olan direnci belirler ve devreden çıkarır. | Beceri | a | Analiz | Fiz05MK0036; Fiz05MK0011 | Fiz05YG0007 | ÇS |
| Fiz05MK0039 | Verilen üç direnci farklı bağlama biçimleriyle şematik olarak çizer. | Beceri | a | Uygulama | Fiz05MK0035; Fiz05MK0036 | – | AU, PG |
| Fiz05MK0040 | Seri devrede her dirençten geçen akımı ve üreteç akımını ölçüp tabloya kaydeder. | Beceri | b | Uygulama | Fiz05MK0023; Fiz05MK0035 | Fiz05YG0008 | PG |
| Fiz05MK0041 | Paralel devrede kol akımlarını ve ana kol akımını ölçüp tabloya kaydeder. | Beceri | b | Uygulama | Fiz05MK0023; Fiz05MK0036 | – | PG |
| Fiz05MK0042 | Ölçülen üreteç gerilimi ve ana kol akımından eşdeğer direnci Reş = V / I ile bulur. | Beceri | b | Uygulama | Fiz05MK0032; Fiz05MK0040; Fiz05MK0041 | – | AU, PG |
| Fiz05MK0043 | Seri devre verisinden akımın her dirençte aynı olduğu sonucunu çıkarır. | Bilgi | c | Analiz | Fiz05MK0040 | Fiz05YG0008 | ÇS, AU |
| Fiz05MK0044 | Paralel devre verisinden ana kol akımının kol akımları toplamına eşit olduğu sonucunu çıkarır. | Bilgi | c | Analiz | Fiz05MK0041 | – | ÇS, AU |
| Fiz05MK0045 | Seri bağlamada Reş = R1 + R2 + ... modelini veriyle test eder. | Beceri | c | Analiz | Fiz05MK0042; Fiz05MK0043 | – | AU |
| Fiz05MK0046 | Seri bağlamada Reş’in en büyük dirençten büyük olduğunu açıklar. | Bilgi | c | Anlama | Fiz05MK0042; Fiz05MK0043 | – | ÇS |
| Fiz05MK0047 | Paralel bağlamada 1/Reş = 1/R1 + 1/R2 + ... modelini veriyle test eder. | Beceri | c | Analiz | Fiz05MK0042; Fiz05MK0044 | Fiz05YG0009 | AU |
| Fiz05MK0048 | Paralel bağlamada Reş’in en küçük dirençten küçük olduğunu açıklar. | Bilgi | c | Anlama | Fiz05MK0042; Fiz05MK0044 | Fiz05YG0010 | ÇS |
| Fiz05MK0049 | n özdeş direnç seri bağlıyken Reş = n·R kısa yolunu kullanır. | Beceri | c | Uygulama | Fiz05MK0045; Fiz05MK0046 | – | ÇS |
| Fiz05MK0050 | n özdeş direnç paralel bağlıyken Reş = R/n kısa yolunu kullanır. | Beceri | c | Uygulama | Fiz05MK0047; Fiz05MK0048 | Fiz05YG0009 | ÇS |
| Fiz05MK0051 | Birleşik devrenin eşdeğer direncini adım adım indirgeyerek hesaplar. | Beceri | c | Uygulama | Fiz05MK0037; Fiz05MK0038; Fiz05MK0045; Fiz05MK0047 | Fiz05YG0007; Fiz05YG0009 | ÇS, AU |
| Fiz05MK0052 | Devreye seri direnç eklemenin eşdeğer direnci artırdığını gerekçesiyle tahmin eder. | Bilgi | c | Değerlendirme | Fiz05MK0045; Fiz05MK0046 | – | ÇS, AU |
| Fiz05MK0053 | Devreye seri direnç eklemenin ana kol akımını azalttığını gerekçesiyle tahmin eder. | Bilgi | c | Değerlendirme | Fiz05MK0045; Fiz05MK0046 | – | ÇS, AU |
| Fiz05MK0054 | Devreye paralel direnç eklemenin eşdeğer direnci azalttığını gerekçesiyle tahmin eder. | Bilgi | c | Değerlendirme | Fiz05MK0047; Fiz05MK0048 | Fiz05YG0010 | ÇS, AU |
| Fiz05MK0055 | Devreye paralel direnç eklemenin ana kol akımını artırdığını gerekçesiyle tahmin eder. | Bilgi | c | Değerlendirme | Fiz05MK0047; Fiz05MK0048 | – | ÇS, AU |
| Fiz05MK0056 | Hesaplanan eşdeğer dirençle ana kol akımını I = V / Reş ile tahmin eder. | Beceri | c | Uygulama | Fiz05MK0032; Fiz05MK0051 | – | ÇS |
| Fiz05MK0057 | Tahmin ettiği akımı ölçümle karşılaştırarak hipotezini değerlendirir. | Beceri | c | Uygulama | Fiz05MK0056 | – | ÇS |

> 2026-10-01: Tek ölçülebilir hedef taramasıyla güncellendi (bir MK = bir soruyla tamamı ölçülebilen tek hedef). Tablo veri dosyasından üretildi.
> Aşağıdaki öğrenme sırası bölmeden önceki hâli gösterir; güncel sıra haritadadır.

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi/deney

Tasarım notu: Sınırlama Kirchhoff'un potansiyel fark yasasını dışarıda bıraktığı için seri eşdeğer direnç "gerilimler toplanır" üzerinden değil, ölçülen V / I üzerinden (Fiz05MK0042 → Fiz05MK0045) kuruldu.

---

## 4. Öğrenme sırası (bağımlılık)

Kodlarda `Fiz05MK` öneki kısaltılmıştır (0009 = Fiz05MK0042). ÖK2 = Fiz05MK0032, ÖK3 = Fiz05MK0012.

```
ÖK1 ─┬─ 0001 ─┬─ 0003 ──────────────────┐
     └─ 0002 ─┼─ 0004 ──────────────────┤
              └─ 0005                   │
ÖK3 ── 0006 ─┬─ 0007 ─ 0010 ─┐          │
             └─ 0008 ─ 0012 ─┤          │
ÖK2 ── 0009 ─────────────────┼─ 0011 ───┼─ 0015 ─ 0016
                             └─ 0013 ───┤
                                0014    └─ 0017
```

---

## 5. Örnek ölçme maddeleri

**Fiz05MK0036 (Fiz05YG0006 çeldiricili):** Şemada R1 üstte, R2 altta çizilmiş ama ikisi de A ve B noktalarına bağlı; R3 ise R1'in hemen yanında çizilmiş ve R1 ile tek yol oluşturuyor. Hangi dirençler paralel bağlıdır?
A) R1 ve R3 (Fiz05YG0006: yan yana çizilmiş) · B) R1 ve R2 ✔ · C) Hepsi · D) Hiçbiri

**Fiz05MK0047 (Fiz05YG0010, Fiz05YG0009):** 6 Ω ve 3 Ω'luk dirençler paralel bağlanıyor. Eşdeğer direnç kaç Ω'dur?
A) 9 (Fiz05YG0010: toplanmış) · B) 1/2 (Fiz05YG0009: ters çevrilmemiş) · C) 2 ✔ · D) 4,5 (ortalama)

**Fiz05MK0052:** 12 V'luk üretece bağlı 4 Ω'luk dirence paralel olarak bir 4 Ω daha ekleniyor. Ana kol akımı nasıl değişir? Gerekçenle açıkla.
Beklenen: Reş 4 Ω'dan 2 Ω'a düşer, akım 3 A'dan 6 A'ya çıkar. "Azalır" diyen öğrenci Fiz05YG0010 yanılgısına işaret eder.

**Fiz05MK0056 (performans görevi):** Öğrenci 2 Ω, 3 Ω, 6 Ω ile birleşik bir devre kurar, Reş'i hesaplayıp ana kol akımını tahmin eder, ampermetreyle ölçer ve farkı yorumlar. Rubrik: tahminin doğruluğu, ölçüm doğruluğu, farkın gerekçelendirilmesi (ölçüm hatası, iç direnç vb.).

Ustalık ölçütü (varsayılan): her mikro kazanım için farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.

---

## 6. EVALORA veri şablonu (her mikro kazanım için bir kayıt)

Mikro kazanım kaydı sınıftan bağımsızdır; hangi sınıfta ve hangi öğrenme çıktısında kullanıldığı `eslemeler` listesinde tutulur. Aynı mikro kazanım başka bir sınıfta geçerse yalnızca bu listeye satır eklenir.

```json
{
  "kod": "Fiz05MK0047",
  "ana_unite": "05",
  "ifade": "Paralel bağlamada 1/Reş = 1/R1 + 1/R2 + ... modelini veriyle test eder; Reş'in en küçük dirençten küçük olduğunu açıklar.",
  "tur": "Beceri",
  "bilissel_duzey": "Analiz",
  "on_kosullar": ["Fiz05MK0042", "Fiz05MK0044"],
  "yanilgilar": ["Fiz05YG0010", "Fiz05YG0009"],
  "olcme_turleri": ["acik_uclu"],
  "ustalik_olcutu": "3 maddeden en az 2 doğru",
  "eslemeler": [
    {"sinif": 10, "sinif_unite": "Fiz10-U3", "ogrenme_ciktisi": "FİZ.10.3.4", "surec_bileseni": "c"}
  ]
}
```
