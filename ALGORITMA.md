# EVALORA: Mikro Kazanım Haritasına Dayalı Ölçme, Teşhis ve Uyarlamalı Değerlendirme Modeli

*EVALORA: Measure. Diagnose. Remediate. (Ölç. Teşhis et. Telafi et.)*

*Micro-skill based assessment, diagnosis and remediation (Mikro kazanım temelli ölçme, teşhis ve telafi)*

*Kararlar, gerekçeler ve açık konular. Son güncelleme: 2026-10-03.*

## Özet

EVALORA (Education-focused Virtual Assistant for Learning-based Optimized Recommendations and Assessments), Türkiye Yüzyılı Maarif Modeli (TYMM) öğretim programlarındaki öğrenme çıktılarını, her biri öncekilerin üzerine tek bir yeni adım ekleyen ve tek bir soruyla ölçülebilen birimlere, **mikro kazanımlara (MK)** ayırır ve bu birimleri "önce bunu bilmeli" ilişkisiyle bir **ön koşul haritasına** bağlar. Şu an Fizik 9–12 (766 MK) ve Matematik 5–12 (1664 MK) haritalanmıştır. Bu doküman, haritanın nasıl kurulduğunu ve bu harita üzerine kurulan ölçme modelini anlatır: her MK'nin öğrenme zorluğunun nasıl hesaplandığı (bölüm 4), bir sorunun hangi MK'lere eşlendiği ve zorluğunun ne olduğu (bölüm 5), öğrencinin bir MK'yi bilip bilmediğine nasıl karar verildiği (bölüm 6) ve bunların bir uygulamaya nasıl dönüşeceği (bölüm 7). Her kararın yanında matematiği, gerekçesi ve dayandığı eğitim, psikoloji ve istatistik kuramı yazılıdır. Model, veri yokken kuramdan türetilen başlangıç değerleriyle çalışır; öğrenci cevapları biriktikçe Rasch modeliyle kalibre edilmek üzere tasarlanmıştır.

**Anahtar kavramlar:** mikro kazanım, ön koşul haritası, Bilgi Uzayı Kuramı, işlem türü, RSS, LLTM, Q-matris, Bayesçi Bilgi İzleme, uyarlamalı test.

## 1. Giriş

### 1.1 Sorun

Bir öğretim programındaki öğrenme çıktısı genellikle birden çok bilgi ve beceriyi bir arada taşır. Örneğin 10. sınıf fizikteki **FİZ.10.3.4**, "Dirençlerin bağlanma türlerine göre eşdeğer dirence ilişkin bilimsel çıkarım yapabilme" çıktısıdır ve üç süreç bileşeni vardır: (a) bağlanma türlerini tanımlamak, (b) veri toplayıp kaydetmek, (c) çıkarımları matematiksel modellerle test etmek. Bu çıktıdan sorulan bir soruyu yapamayan öğrenci için "FİZ.10.3.4'ü bilmiyor" demek öğretmene neredeyse hiçbir şey söylemez: öğrenci seri ve paralel bağlamayı mı ayırt edemiyor, kısa devreyi mi fark etmiyor, paralel bağlamadaki formülü mü bilmiyor, yoksa bunların hepsini bilip birleştirmede mi takılıyor?

Klasik sınav puanı da aynı sorunu taşır: tek bir sayı, eksiğin **nerede** olduğunu söylemez. İyi bir öğretmen bunu sorudan soruya, öğrenciden öğrenciye sezgiyle yapar; EVALORA'nın amacı bu teşhisi sistematik, tekrarlanabilir ve ölçeklenebilir kılmaktır.

### 1.2 Yaklaşım

EVALORA üç adımda ilerler:

1. **Ayrıştırma:** Her öğrenme çıktısı, her biri tek bir yeni adım ekleyen ve tek bir soruyla ölçülebilen birimlere, mikro kazanımlara bölünür (bölüm 2).
2. **Haritalama:** MK'ler, "B'yi öğrenmek için önce A gerekir" ilişkisiyle sınıf ve ünite sınırı tanımayan tek bir ağa bağlanır (bölüm 3).
3. **Ölçme ve teşhis:** Sorular MK'lere eşlenir, zorlukları haritadan hesaplanır; öğrencinin cevapları MK düzeyinde işlenir ve test, eksiğin kökünü bulana kadar haritada aşağı ya da yukarı ilerler (bölüm 4–6).

Sonuç, öğrencinin ve sınıfın MK MK ayrıntılı bir raporudur: hangi MK'ler biliniyor, hangileri bilinmiyor, hangileri henüz ölçülemedi ve eksiklerin kökü haritanın neresinde.

### 1.3 Bu dokümanın düzeni

Bölüm 2 temel kavramları ve veri yapısını, bölüm 3 ön koşul haritasını tanımlar. Bölüm 4 MK zorluğunu, bölüm 5 soru eşleme ve soru zorluğunu, bölüm 6 MK teşhisini ve "biliyor" kararını anlatır. Bölüm 7 uygulama ve demo kararlarını, bölüm 8 açık konuları içerir. Kaynaklar bölüm 9'da, terimler sözlüğü Ek A'dadır. Kararların tarihleri ve kararı veren kişi başlıklarda yazılıdır; dosya ve sütun adları `bu biçimde` gösterilir.

## 2. Temel kavramlar ve veri yapısı

### 2.1 TYMM öğrenme çıktısı ve süreç bileşeni

**Öğrenme çıktısı (ÖÇ):** TYMM öğretim programında öğrencinin ulaşması beklenen hedef. Resmî kodla gösterilir: `FİZ.10.3.4` (ders, sınıf, ünite, çıktı) ya da `MAT.9.4.4`. Kodlar TYMM'den değiştirilmeden alınır.

**Süreç bileşeni:** Bir öğrenme çıktısının (a), (b), (c) … diye sıralanan alt adımları. Her MK tek bir süreç bileşenine bağlanır; böylece MK düzeyindeki sonuçlar gerektiğinde çıktı düzeyine geri toplanabilir.

**Sınıf ünitesi / teması:** Çıktının sınıf programındaki yeri, ör. `Fiz10-U3` (10. sınıf fizik 3. ünite) ya da `Mat08-T1` (8. sınıf matematik 1. tema).

**Ana ünite / ana tema:** Sınıftan bağımsız içerik alanı. Aynı konu 10. ve 11. sınıfta işlense de aynı ana ünite kodunu taşır; ör. fizikte `05` her zaman Elektrik ve Manyetizma'dır. Fizikte 8 ana ünite (01–08), matematikte 11 ana tema (01–11) vardır (tam liste: `KODLAMA.md`).

### 2.2 Mikro kazanım (MK)

**Tanım (2026-10-03, Murat):** Mikro kazanım, ön koşullarının üzerine **tek bir yeni bilgi ya da beceri adımı** ekleyen ve tek bir soruyla bütünüyle ölçülebilen öğrenme birimidir. Öğrenciden beklenen davranışı gözlenebilir bir fiille anlatır ("… hesaplar", "… ayırt eder", "… genellemesini yapar"). "Mikro" sözcüğü içeriğin küçüklüğünü değil, **atılan yeni adımın küçüklüğünü** anlatır. MK iki türlüdür:

- **Temel MK:** Haritada ön koşulu yoktur; bir kavramı, kuralı ya da işlemi ilk kez kazandırır. Örnek: Fiz05MK0035, devre şemasında seri bağlı dirençleri tanır.
- **Bütünleştirici MK:** Daha önce kazanılmış MK'leri bir araya getirir ve üstüne yeni bir işlem ekler. Ortaya parçalarının toplamından fazlası olan yeni bir bilgi-beceri bütünü çıkar. Örnek: Fiz05MK0051, birleşik devrenin eşdeğer direncini adım adım indirgeyerek hesaplar. Devreyi seri ve paralel gruplara ayırma (Fiz05MK0037), kısa devreyi bulma (Fiz05MK0038), seri ve paralel eşdeğer direnç modelleri (Fiz05MK0045, Fiz05MK0047) bir araya gelir; üstüne "adım adım indirgeme" eklenir.

Kazanımlar böylece katman katman inşa edilir: her MK, öncekilerin üstüne konan bir tuğladır; ön koşul haritası (bölüm 3) bu inşanın planıdır. Zorluk formülü de bu inşayı yansıtır (bölüm 4): Z = √(v² + Σ ön koşul v²) ifadesinde v, MK'nin eklediği yeni adımın ağırlığı; ön koşullar, üstüne kurulduğu tuğlalardır. Rubrikteki "kendisi" payı da bu birleştirme adımıdır (5.3).

**Eğitsel dayanak:**
- **Öğrenme hiyerarşileri** (Gagné, 1968): Üst düzey bir beceri, alt becerilerin birleşimiyle öğrenilir; alt beceriler kazanılmadan üstteki kazanılamaz.
- **Anlamlı öğrenme** (Ausubel, 1968) ve **yapılandırmacılık** (Piaget, 1970): Yeni bilgi, öğrencinin zihnindeki mevcut yapıya bağlanarak kurulur.
- **Şema kuramı ve öbekleme** (Sweller, 1988; Chase ve Simon, 1973): Birleştirilen bilgiler zamanla tek bir şemaya dönüşür ve bir sonraki adımda tek bir birim gibi kullanılır.
- **SOLO taksonomisi** (Biggs ve Collis, 1982): Parçaları ayrı ayrı bilmek (çok yapılı düzey) ile onları ilişkilendirip bir bütün kurmak (ilişkisel düzey) farklı düzeylerdir.
- **Davranışsal hedef** (Mager, 1962): Her MK, gözlenebilir ve ölçülebilir bir davranışla yazılır.

**Örnek:** FİZ.10.3.4 çıktısı 27 MK'ye ayrılmıştır. Bunlardan birkaçı:

| Kod | Mikro kazanım | Bileşen | Tür | İşlem türü |
|---|---|---|---|---|
| Fiz05MK0035 | Devre şemasında seri bağlı dirençleri, akımın izleyebileceği tek yol olmasından tanır. | a | Bilgi | Tanıma ve hatırlama |
| Fiz05MK0037 | Birleşik bir devreyi seri ve paralel alt gruplarına ayırır. | a | Beceri | Ayırt etme ve sınıflama |
| Fiz05MK0038 | Kısa devre olan direnci belirler ve devreden çıkarır. | a | Beceri | Yorumlama |
| Fiz05MK0040 | Seri devrede her dirençten geçen akımı ve üreteç akımını ölçüp tabloya kaydeder. | b | Beceri | Gözlem ve kayıt |
| Fiz05MK0047 | Paralel bağlamada 1/Reş = 1/R1 + 1/R2 + … modelini veriyle test eder. | c | Beceri | Sınama ve değerlendirme |
| Fiz05MK0051 | Birleşik devrenin eşdeğer direncini adım adım indirgeyerek hesaplar. | c | Beceri | Kural uygulama |

**Tek ölçülebilir hedef kuralı (2026-10-01, Murat):** Bir MK'yi bölüp bölmemeye şu soruyla karar verilir: *"Bir soru bu MK'nin yalnızca bir parçasını sorabilir mi?"* Sorabiliyorsa MK bölünür. Bölünmezse öğrenci bir parçada başarısız olduğunda öbür parça hakkında da karar verilmiş olur (ölçme hatası) ve eksiğin kökü yanlış bulunur (öneri hatası). Örneğin "ortalama sürati ve ortalama hızı hesaplar" iki MK'dir. Ayrıntılı kurallar: farklı değişken, kavram, kural, model ya da durum ayrı MK olur; Bilgi ile Beceri aynı MK'de durmaz; aynı becerinin farklı bağlamlara uygulanması tek MK kalır; problem çözme ve muhakeme süreç adımları ayrı MK'dir (`KODLAMA.md`).

**Ölçme açısından dayanak:** Bilişsel tanı modellerinde her sorunun hangi beceri (attribute) birimlerini ölçtüğü açıkça tanımlanmalıdır (Tatsuoka, 1983; Leighton ve Gierl, 2007); MK bu birimin karşılığıdır.

**Aynı MK yeniden yazılmaz, eşlenir:** Aynı bilgi ya da beceri başka bir çıktıda ya da sınıfta geçerse yeni MK yazılmaz; mevcut MK o çıktıya da **eşlenir** (`<ders>_kazanim_esleme.csv`). Bu yüzden bir MK birden çok sınıfa ve çıktıya bağlı olabilir. (Örnek: Pisagor bağıntısıyla kenar hesaplama 8. sınıfta yazılmış ve 9. sınıf çıktısına da eşlenmiştir; 2026-10-02'de 9. sınıfta ayrıca yazılmış iki tekrar MK birleştirildi.)

### 2.3 Bir MK'nin özellikleri

Her MK'de şu alanlar tutulur (`<ders>_mikro_kazanimlar.csv`):

| Alan | Anlamı | Değerler |
|---|---|---|
| `kod` | Kalıcı kimlik (2.4) | Fiz05MK0051 |
| `ana_unite` | İçerik alanı | 01–11 |
| `ifade` | Öğrenciden beklenen davranış | "… hesaplar." |
| `tur` | Bilgi mi, beceri mi | **Bilgi**: kavramı, tanımı, kuralı ya da ilişkiyi bilmek, tanımak, açıklamak ("ne", "neden"). **Beceri**: bir işlemi, yöntemi ya da süreci yürütmek (ölçer, çizer, hesaplar, test eder) |
| `bilissel_duzey` | Yenilenmiş Bloom taksonomisindeki düzey (Anderson ve Krathwohl, 2001) | Hatırlama, Anlama, Uygulama, Analiz, Değerlendirme, Yaratma |
| `islem_turu` | MK'nin ön koşullarının üstüne eklediği tek ana zihinsel işlem; zorluk hesabının girdisi (4.2) | 15 tür, ör. Kural uygulama, Yorumlama, Model kurma |
| `on_kosul_kodlari` | Doğrudan ön koşul MK'leri (bölüm 3) | Fiz05MK0037; Fiz05MK0038; … |
| `on_kosul_diger` | Haritada karşılığı olmayan ön öğrenme | "Fen bilimleri: kuvvet çeşitleri (ön öğrenme)" |
| `yanilgilar` | Bu MK'de görülen kavram yanılgıları | Fiz05YG0007; Fiz05YG0009 |
| `olcme_turleri` | Uygun soru biçimi | ÇS (çoktan seçmeli), AU (açık uçlu), PG (performans görevi / deney, rubrikle) |
| `ustalik_olcutu` | Başlangıçtaki "biliyor" eşiği (bölüm 6'da yerini Bayesçi karar alır) | "3 maddeden en az 2'si doğru"; "Rubrikte yeterli ve üstü" |
| `durum` | Kaydın durumu | taslak, iptal |

**Kavram yanılgısı:** Öğrencilerde sık görülen, tutarlı ama yanlış bir düşünce, ör. Fiz05YG0010 "Paralel bağlamada direnç eklendikçe eşdeğer direnç artar." Yanılgılar ayrı kodlanır ve ilgili MK'ye bağlanır. Çoktan seçmeli soruların çeldiricileri bu yanılgılardan üretilir; böylece öğrencinin seçtiği yanlış şık hangi yanılgıyı taşıdığını gösterir.

**İşlem türü ile bilişsel düzey farkı:** Bilişsel düzey Bloom'un genel sınıflamasıdır ve raporlamada kullanılır. İşlem türü ise MK'nin *tek bir adımda* eklediği zihinsel işi daha ince tanımlar ve zorluk modelinin girdisidir (4.2). İkisi çoğu zaman uyumludur ama aynı şey değildir.

### 2.4 Kodlama

- **MK kodu:** `<Ders><2 haneli ana ünite>MK<4 haneli sıra>`, ör. `Fiz05MK0051`, `Mat03MK0143`. Kod sınıftan bağımsızdır.
- **Yanılgı kodu:** `<Ders><ana ünite>YG<4 hane>`, ör. `Fiz05YG0007`.
- **Kalıcılık:** Kodlar, sorulara ve öğrenci verisine eşlenmeye başlanana kadar düzenli tutmak için yeniden numaralanabilir (son yeniden numaralama: fizik ve matematik 2026-10-01, matematik Mat08 2026-10-02); eski–yeni karşılıkları `<ders>_kod_donusum.csv`'de saklanır. Eşleme başladıktan sonra kodlar değişmez, kullanımdan kalkan kod "iptal" olur ve başka MK'ye verilmez.

### 2.5 Veri dosyaları ve üretilen çıktılar

Her dersin `veri/` klasöründeki CSV dosyaları **tek doğruluk kaynağıdır**; diğer her şey bunlardan üretilir (`python3 araclar/excel_uret.py`):

| Dosya | İçerik |
|---|---|
| `<ders>_mikro_kazanimlar.csv` | MK'ler ve özellikleri (2.3) |
| `<ders>_kazanim_esleme.csv` | MK ↔ sınıf, sınıf ünitesi, öğrenme çıktısı, süreç bileşeni |
| `<ders>_yanilgilar.csv` | Yanılgılar ve ilgili MK'ler |
| `<ders>_kod_donusum.csv` | Eski kod → güncel kod |
| `<ders>_graf.json` | Uyarlamalı testin okuyacağı harita (düğümler, derinlik, etki, zorluk, seviye) |
| `<Ders> Mikro Kazanım.xlsx` | Öğretmenin okuyacağı tablo (MK'ler, eşleme, yanılgılar, işlem türleri, seviyeler) |
| `<Ders> Mikro Kazanım Haritası.html` | Tarayıcıda açılan etkileşimli ön koşul haritası |
| `mikro-kazanimlar/*.md` | Her öğrenme çıktısı için ayrıştırma dosyası (yanılgılar, MK tablosu) |
| `ortak/islem_turleri.csv`, `ortak/zorluk_seviyeleri.csv` | Tüm dersler için işlem türleri ve seviye açıklamaları |

**Bugünkü kapsam (2026-10-03):**

| | Fizik | Matematik |
|---|---|---|
| Sınıflar | 9–12 | 5–12 |
| Öğrenme çıktısı | 106 | 177 |
| Mikro kazanım | 766 (486 Bilgi, 280 Beceri) | 1664 (546 Bilgi, 1118 Beceri) |
| MK–çıktı eşlemesi | 784 | 1844 |
| Kavram yanılgısı | 135 | 185 |

## 3. Ön koşul haritası

### 3.1 Yapı

MK'ler bir **yönlü döngüsüz grafik** (DAG) oluşturur:

- **Düğüm:** bir MK.
- **Ok (bağ):** A → B, "B'yi öğrenmek için A gerekir" demektir; A, B'nin **doğrudan ön koşuludur**. Oklar sınıf ve ünite sınırı tanımaz: 12. sınıftaki bir MK, 7. sınıftaki bir MK'ye dayanabilir.
- **Öncül:** B'ye doğrudan ya da bir zincir üzerinden ulaşan her MK. Doğrudan ön koşulların ön koşulları dolaylı öncüllerdir ve ayrıca bağlanmaz.
- **Kök:** haritada ön koşulu olmayan MK. Dayandığı ön öğrenme `on_kosul_diger` alanına yazılır (ör. "Fen bilimleri: kuvvet çeşitleri").
- **Derinlik:** bir MK'nin altındaki en uzun ön koşul zinciri (kök = 0). **Katman sayısı**, haritadaki en büyük derinlik + 1'dir.
- **Etki:** bir MK'ye doğrudan ya da dolaylı dayanan MK sayısı. Etkisi yüksek bir MK'deki eksik çok sayıda MK'yi etkiler.

Örnek zincir: Fiz05MK0035 (seri bağlı dirençleri tanır) → Fiz05MK0040 (seri devrede akımları ölçer) → Fiz05MK0043 (akımın her dirençte aynı olduğu sonucunu çıkarır) → Fiz05MK0045 (Reş = R1 + R2 + … modelini test eder) → Fiz05MK0051 (birleşik devrenin eşdeğer direncini hesaplar).

### 3.2 Bağ kuralı: yalnız gerçek dayanak

**Kural (2026-10-02, Murat):** Bir MK'ye yalnız o adımın **gerçekten dayandığı** MK'ler doğrudan ön koşul olarak bağlanır. Sınama sorusu: *"Öğrenci A'yı bilmeden B'yi yapabilir mi?"* Yapabiliyorsa A, B'nin ön koşulu değildir.

Bağlanmayanlar:
- **Kardeş konu:** kesir problemi ← ondalık işlem.
- **Süreç adımı:** formülü kullanma ← formülün ispatı ya da sınanması.
- **İlgisiz komşu:** çift yarık deneyi ← ışık şiddeti birimi.
- **Birim bilgisi:** kuvvetleri ayırt etme ← newton birimi.
- **Aynı ünitede önce gelen ama gereksiz MK.**
- **Dolaylı öncül:** zincirden zaten gelir.

**Uygulama:** Haritalar üç kez tek tek denetlendi. 2026-10-01'de bölme sonrası geniş bağlar temizlendi; 2026-10-02'de gereksiz bağlar silindi; 2026-10-02'de her iki dersin bütün MK'leri "buna ne lazım ki yapabilsin" sorusuyla yeniden incelendi (fizikte 169, matematikte 355 MK'nin ön koşulu düzeltildi). Ayrıntı ve sayılar 4.5'te.

### 3.3 Denetimler

Harita her üretimde otomatik denetlenir (`araclar/harita_uret.py`, sonuç `<Ders> Harita Denetimi.md`):
- **Döngü yok:** A, B'nin ön koşuluysa B, A'nın öncülü olamaz.
- **Kopuk düğüm yok:** her MK'nin ya ön koşulu ya `on_kosul_diger` açıklaması vardır.
- **Sınıf sırası:** bir MK'nin ön koşullarının en düşük sınıfı, MK'nin kendi en düşük sınıfından büyük olamaz. Öğrenciye kendi sınıfının üstündeki bir bilgiye dayanan soru gelmez.

### 3.4 Kuramsal dayanak

- **Bilgi Uzayı Kuramı** (Knowledge Space Theory; Doignon ve Falmagne, 1985, 1999; Falmagne ve Doignon, 2011): Bir alandaki bilgi birimleri arasındaki "önce bunu bilmeli" ilişkisi (surmise relation) bir kısmi sıralamadır. Bir öğrencinin bilgi durumu, bu sıralamaya uyan bir MK kümesidir: bir MK'yi bilen, onun bütün öncüllerini de bilir. Kısmi sıralama yalnız doğrudan bağlarla (Hasse diyagramı) eksiksiz gösterilir; bu yüzden haritada yalnız doğrudan ön koşullar tutulur. ALEKS gibi uyarlamalı sistemler öğrencinin yerini bu yapıda arar; EVALORA'nın testi de yolunu haritadan alır.
- **Öğrenme hiyerarşileri** (Gagné, 1968): Bir beceriyi öğrenmek için önce onun alt becerilerinin öğrenilmesi gerekir; öğretim ve teşhis bu hiyerarşide aşağıdan yukarı ya da yukarıdan aşağı ilerler.

### 3.5 Bugünkü harita

| | Fizik | Matematik |
|---|---|---|
| Ön koşul bağı | 1.208 | 2.599 |
| Katman sayısı | 25 | 41 |
| Kök | 46 | 26 |
| Döngü / kopuk / sınıf sırası ihlali | 0 / 0 / 0 | 0 / 0 / 0 |

## 4. MK zorluğu (son karar: 2026-10-02, Murat)

Bu bölüm bir MK'yi öğrenmenin ne kadar zor olduğunu, haritadan nasıl hesapladığımızı anlatır. Özet:

> **Zorluk(k) = √( v(k)² + Σ v(p)² )**  (p: k'nin doğrudan ön koşulları; RSS)
> **v = 1 + log₂(r)**  (r: işlem türünün sırası, 1–4) → 1 · 2 · 2.585 · 3
> **Seviye(k) = ⌊Zorluk(k)⌋**

Aşağıda her parçanın ne olduğu, neden böyle seçildiği ve hangi eğitim, psikoloji, matematik ve istatistik kuramına dayandığı yazılıdır.

### 4.1 Haritanın yapısı ve "adım zorluğu" ilkesi

**Ne:** Her mikro kazanım (MK) haritada bir düğümdür. Ön koşul bağları yönlü ve döngüsüz bir grafik (DAG) oluşturur. Bir MK'nin zorluğu yalnızca **kendi adımına** bakılarak hesaplanır: kendi işlemi ve doğrudan ön koşulları. Daha alttaki zincir hesaba girmez.

**Neden:**
- 5. sınıftaki bir adım ile lisedeki bir adım, kendi içinde aynı yükü taşıyorsa aynı zorluktadır (Murat). Öğrencinin geçmişini (hangi yoldan geldiğini) **harita** taşır, **puan** taşımaz.
- İlk formül, MK'nin altındaki tüm zinciri topluyordu. Kazanımlar inceldikçe ve zincir uzadıkça puan şişti: teğet denklemi (Mat11MK0056) 218 alt MK ile 15.30'a çıkmıştı. Bu, adımın zorluğunu değil zincirin uzunluğunu ölçüyordu.
- Sonuç: "Bir MK, ön koşulundan kolay olamaz" kuralı kaldırıldı. İleri bir MK, ön koşulundan düşük puan alabilir, çünkü ölçülen şey adımın kendisidir.

**Kuram:**
- **Bilgi Uzayı Kuramı** (Knowledge Space Theory; Doignon ve Falmagne, 1985, 1999). Kazanımlar arasındaki "önce bunu bilmeli" ilişkisi (surmise relation) bir kısmi sıralamadır. Bu sıralama, yalnızca doğrudan bağlarla çizilen Hasse diyagramıyla eksiksiz gösterilir. Dolaylı bağlar zaten doğrudan bağların zincirinden çıkar; bu yüzden yalnızca doğrudan ön koşullar sayılır. ALEKS gibi uyarlamalı sistemler öğrencinin yerini bu yapıda bulur. Bizim adaptif testimiz de yolu haritadan alır.
- **Atomik kazanım:** her MK "tek ölçülebilir hedef" kuralına uyar (KODLAMA.md). Bu sayede her düğüm tek bir işlem ekler ve bu işlemin türü tek bir değerle temsil edilebilir.

### 4.2 İşlem türü ve değeri: v = 1 + log₂(r)

**Ne:** Her MK, ön koşullarının üstüne **tek bir ana işlem** ekler. İşlem türü MK'nin ana fiilinden ve ölçmede gözlenen çıktıdan belirlenir ve `<ders>_mikro_kazanimlar.csv`'deki **islem_turu** sütununda tutulur (zorunlu alan). 15 tür vardır, 4 sıraya ayrılır. Tanımlar, tipik fiiller ve örnekler `ortak/islem_turleri.csv`'dedir.

| Sıra (r) | v = 1 + log₂(r) | Grup | İşlem türleri |
|---|---|---|---|
| 1 | 1 | Küçük | Tanıma ve hatırlama · Gözlem ve kayıt · Taklit |
| 2 | 2 | Orta | Kural uygulama · Dönüştürme · Ayırt etme ve sınıflama · Açıklama ve özetleme · Karşılaştırma · Beceri uygulama |
| 3 | 2.585 | Büyük | Yorumlama · Çıkarım ve ilişkilendirme |
| 4 | 3 | Çok büyük | Model kurma · Sınama ve değerlendirme · Üretme ve tasarım · Transfer ve problem çözme |

**Sıralamanın kuramı:** Yenilenmiş Bloom taksonomisi (Anderson ve Krathwohl, 2001: hatırlama → anlama/uygulama → çözümleme → değerlendirme/yaratma) ve SOLO taksonomisi (Biggs ve Collis, 1982: tek yapılı → çok yapılı → ilişkisel → genişletilmiş soyut). Sıra, işlemin aynı anda işlenmesi gereken öğe ve ilişki sayısıyla birlikte artar. Bizdeki fark: seviyeyi uzman etiketi değil, haritadan hesaplanan puan belirler.

**Değerlerin matematiği (neden logaritmik):**
- **Weber–Fechner yasası** (Weber, 1834; Fechner, 1860): algılanan büyüklük, uyaranın logaritmasıyla artar, S = k · ln(I / I₀). Yük iki katına çıktığında algılanan zorluk iki katına değil, bir birim artar.
- **Hick–Hyman yasası** (Hick, 1952; Hyman, 1953): karar süresi seçenek sayısının logaritmasıyla artar, T = a + b · log₂(n + 1). Bilişsel işlem süresi de doğrusal değil logaritmik büyür.
- **Bilgi kuramı** (Shannon, 1948): bilgi miktarı log₂ ile ölçülür (bit). r sırasındaki işlem, kabaca r kat öğe ve ilişki taşır; bunun bilgi yükü log₂(r) bittir. +1 ise en basit işlemin taban değeridir.
- Sonuç: en büyük sıçrama tanımadan uygulamaya geçiştir (1 → 2). Yukarıdaki basamaklar arasındaki fark küçülür (2 → 2.585 → 3). Bu, sınıfta görüleni yansıtır: hatırlamakla uygulamak arasındaki uçurum, yorumlamakla model kurmak arasındakinden büyüktür. Murat'ın sezgiyle önerdiği 1 · 2 · 2.5 · 3 dizisi bu eğrinin neredeyse aynısıdır; tam logaritmik değer (2.585) seçildi.
- Bırakılan: doğrusal 1 · 2 · 3 · 4 (her basamak eşit fark varsayar, model kurmayı tanımanın 4 katı sayar) ve 0.25 · 0.5 · 0.75 · 1.0 (aynı doğrusal dizinin 4'e bölünmüşü).

### 4.3 Birleştirme: kareler toplamının kökü (RSS)

**Ne:** MK'nin kendi işlem değeri ve doğrudan ön koşullarının işlem değerleri birer bileşendir. Her bileşenin karesi alınır, kareler toplanır, toplamın karekökü alınır:

Z = √( v(k)² + v(p₁)² + v(p₂)² + … + v(pₙ)² )

**Neden:**
- **Tek ve tutarlı formül.** Kendi adımı ve ön koşullar aynı kurala uyar; doğrusal ve köklü terim karışmaz (bir önceki v + √Σ formülünün yöntemsel kusuru buydu).
- **Ön koşulsuz MK kendi değerini korur:** √(v²) = v. En küçük zorluk 1'dir (tanıma, ön koşulsuz); en küçük MK'ye gereksiz karekök uygulanmaz.
- **Zor bileşen baskındır.** Kare almak büyük değerlerin ağırlığını artırır: bir model kurma ön koşulu (3² = 9), dört tanıma ön koşulundan (4 × 1² = 4) daha çok katkı verir. Bir adımın zorluğunu en çok, birleştirdiği en zor bilgi belirler.
- **Ön koşul sayısı azalan oranda etkiler.** Aynı değerde n bileşen toplamı √n ile büyütür: kural uygulamalı bir MK, 1 kural uygulama ön koşuluyla √8 = 2.83, 4 tanesiyle √20 = 4.47 olur. Çok ön koşullu MK zorlaşır ama şişmez.

**Kuram:**
- **Hata yayılımı / kareler toplamının kökü (RSS):** bağımsız belirsizlikler σ = √(σ₁² + σ₂² + …) biçiminde birleşir (fizik ve ölçme kuramında standart; Taylor, 1997). Her bileşen (kendi işlemi, her ön koşul) öğrencinin o adımda yanılabileceği bağımsız bir kaynak gibi düşünülür; toplam belirsizlik, yani adımın zorluğu, bu kaynakların RSS'idir. Toplam n ile değil √n ile büyür; en büyük bileşen baskındır.
- **Bilişsel Yük Kuramı** (Cognitive Load Theory; Sweller, 1988; Sweller, van Merriënboer ve Paas, 1998). İçsel yük, aynı anda etkileşen öğe sayısına (element interactivity) bağlıdır. Ön koşullar öğrenilmiş ve otomatikleşmiş şemalardır; çalışma belleğinde öbek (chunk) gibi taşınırlar (Miller, 1956; Chase ve Simon, 1973). Bu yüzden her yeni ön koşul yükü artırır ama azalan oranda; RSS'nin √n davranışı bunu yansıtır.
- **Bilinen sınır:** RSS bileşen sayısını sınırlamaz. Haritası ince çizilmiş (MK başına ön koşul sayısı yüksek) derste tavan yükselir. Dersler arası karşılaştırılabilirlik, haritaların aynı incelikte çizilmesiyle ve sonunda Rasch kalibrasyonuyla sağlanacak (4.6).

### 4.4 Seviye: ⌊Zorluk⌋

**Ne:** Seviye, zorluğun tam sayı kısmıdır. Seviye 1 = [1, 2), Seviye 2 = [2, 3) …; **üstü açıktır** (ileri sınıflar eklendikçe yeni seviyeler kendiliğinden açılır).

**Neden:** Değer ölçeğinde 1 birim, Weber–Fechner anlamında algılanan zorlukta bir basamaktır (bilişsel yükün iki katına çıkması). Seviye sınırları bu yüzden tam sayılara konur; ek bir başlangıç değeri ya da genişlik sabiti gerekmez.

| Seviye | Zorluk | Ad | Açıklama (tüm dersler) | Sayısal örnek | Sözel örnek |
|---|---|---|---|---|---|
| 1 | 1 – 2 | Giriş | Tek bir bilgiyi tanır, adlandırır, hatırlar. | Fizik: birimi tanır | Tarih: olayı dönemiyle eşleştirir |
| 2 | 2 – 3 | Anlama | Kavramı kendi sözleriyle açıklar ya da tek bir kuralı uygular. | Matematik: tek adımlı işlem | Türkçe: cümledeki ögeyi bulur |
| 3 | 3 – 4 | Uygulama | Bilinen yöntemi birkaç adımda uygular; örneklerden kural çıkarır, karşılaştırır. | Fizik: grafikten hız | Coğrafya: iki iklimi karşılaştırır |
| 4 | 4 – 5 | Çözümleme ve yorumlama | Kaynağı, metni, grafiği ya da haritayı kendisi yorumlar; neden-sonuç kurar, genellemeye ulaşır. | Fizik: grafikten hareket denklemi | Tarih: olayın nedenlerini kaynaktan çıkarır |
| 5 | 5 – 6 | Sınama ve bütünleştirme | Farklı konuları birleştirir; iddiayı kanıtla ya da karşı örnekle sınar. | Fizik: modeli veriyle test eder | Edebiyat: yorumu metinden kanıtla destekler ya da çürütür |
| 6 | 6 – 7 | Sentez ve değerlendirme | Uzun öğrenme zincirinin tepesinde; özgün ürün ya da gerekçeli yargı, yeni bağlama aktarma. | Fizik: tahmin edip ölçümle sınar | Türkçe: görüşünü gerekçeleriyle savunan metin yazar |
| 7, 8, … | 7 – 8, … | (üstü açık) | | | |

Açıklamalar o aralığın tipik görünümünü anlatır; seviyeyi puan belirler. Kaynak: `ortak/zorluk_seviyeleri.csv`.

### 4.5 Örnekler ve sonuçlar

**Örnekler:**
- "Uzunluğun SI birimini (metre) belirtir." (Fiz02MK0001): tanıma, ön koşulu yok → √(1²) = **1.00**, Seviye 1.
- xⁿ fonksiyonunun türevini kural olarak kullanır (Mat11MK0053): kural uygulama (2), tek ön koşulu genellemeyi sınama (sınama ve değerlendirme, 3) → √(2² + 3²) = √13 = **3.61**, Seviye 3.
- Teğet denklemi (Mat11MK0056): kural uygulama (2), üç ön koşulu (xⁿ türev kuralı 2, türevi teğetin eğimi olarak yorumlama 2.585, doğru denklemi 2) → √(2² + 2² + 2.585² + 2²) = √18.68 = **4.32**, Seviye 4. (Sabit fonksiyonun türevi ön koşuldan çıkarıldı: teğet denklemi yazmak ona dayanmaz.)

**Sonuçlar** (2026-10-02, RSS; MK MK tam incelemeden sonra):

Fizik (766 MK):

| Sınıf | MK | S1 | S2 | S3 | S4 | S5 | S6 | S7 | En yüksek zorluk |
|---|---|---|---|---|---|---|---|---|---|
| 9 | 174 | 34 | 58 | 62 | 17 | 3 | – | – | 5.98 (Fiz04MK0055) |
| 10 | 244 | 57 | 90 | 72 | 22 | 2 | 1 | – | 6.06 (Fiz06MK0036) |
| 11 | 225 | 20 | 58 | 86 | 56 | 5 | – | – | 5.39 (Fiz05MK0126) |
| 12 | 132 | 11 | 41 | 63 | 17 | – | – | – | 4.97 (Fiz08MK0040) |

Matematik (1664 MK):

| Sınıf | MK | S1 | S2 | S3 | S4 | S5 | S6 | S7 | En yüksek zorluk |
|---|---|---|---|---|---|---|---|---|---|
| 5 | 204 | 14 | 55 | 110 | 21 | 2 | 1 | 1 | 7.01 (Mat06MK0027) |
| 6 | 223 | 6 | 52 | 124 | 37 | 2 | 1 | 1 | 7.01 (Mat06MK0027) |
| 7 | 209 | 7 | 48 | 102 | 50 | 1 | – | 1 | 7.01 (Mat06MK0027) |
| 8 | 269 | 12 | 63 | 137 | 54 | 1 | 1 | 1 | 7.01 (Mat06MK0027) |
| 9 | 223 | 9 | 30 | 122 | 45 | 14 | 2 | 1 | 7.01 (Mat06MK0027) |
| 10 | 245 | 3 | 31 | 135 | 60 | 6 | 9 | 1 | 7.01 (Mat06MK0027) |
| 11 | 215 | – | 22 | 122 | 49 | 11 | 10 | 1 | 7.01 (Mat06MK0027) |
| 12 | 256 | 3 | 28 | 143 | 79 | 2 | 1 | – | 6.12 (Mat06MK0065) |

(Bir MK birden çok sınıfa eşlenebildiği için sınıf toplamları MK sayısından fazladır.) Tüm MK'ler: matematik S1 54 · S2 300 · S3 886 · S4 359 · S5 39 · S6 25 · S7 1 (en yüksek 7.01); fizik S1 119 · S2 243 · S3 281 · S4 112 · S5 10 · S6 1 (en yüksek 6.06).

**Ön koşul temizliği (2026-10-01):** Tek hedef bölmesinden sonra, bölünen bir MK'ye bağlı kazanımlar varsayılan olarak tüm parçalara bağlanmıştı. Her durum tek tek incelenip yalnızca gerçekten gereken parça bırakıldı. Matematikte 1.307 durumda 1.864 bağ kaldırıldı (4.711 → 2.852), fizikte 92 durumda 75 bağ kaldırıldı. Kopuk kalan 5 matematik MK'si uygun ardılına bağlandı. Doğrudan ön koşul sayısı formüle girdiği için bu temizlik zorluğun doğru çıkmasının ön şartıdır.

**İkinci bağ kontrolü (2026-10-02, Murat: "gereksiz bağları sil"):** Her MK'nin doğrudan ön koşulları tek tek incelendi; yalnızca o adımın gerçekten dayandığı bilgiler bırakıldı. Kaldırılan tipik bağlar: kardeş konu (kesir problemi ← ondalık işlem), süreç adımı (formülü kullanma ← formülün ispatı), ilgisiz komşu (çift yarık deneyi ← ışık şiddeti birimi), birim bilgisi (kuvvetleri ayırt etme ← newton birimi). 5+ ön koşullu MK'lerde 109 bağ (mat 60, fizik 49), 2–4 ön koşullu MK'lerde 378 bağ kaldırıldı, 7 doğru bağ eklendi; tek ön koşullu MK'lerde 67 yanlış bağ doğrusuyla değiştirildi (ör. kesirlerle bölme ← kesirlerle toplama yerine çarpma). Sonuç: matematik 2.852 → 2.615, fizik 1.563 → 1.320 ön koşul ilişkisi; matematikte en uzun zincir 63 → 43 katman.

**Üçüncü kontrol: MK MK tam inceleme (2026-10-02, Murat: "MK'yı iyice düşün, buna ne lazım ki yapabilsin… bu harita kusursuz olmalı"):** Bu kez yalnız şüpheli bağlara değil, her iki dersteki her MK'ye tek tek bakıldı ve şu soru soruldu: *öğrenci bu adımı yapabilmek için önceden neyi bilmek zorunda?* Bilgi Uzayı Kuramı'ndaki (Doignon ve Falmagne) "gerekli koşul" tanımı ölçüt alındı: B'yi bilmeyen öğrencinin A'yı yapamaması gerekir; yalnızca yardımcı olan ya da aynı ünitede önce gelen bilgi ön koşul sayılmaz. Düzeltilen tipik hatalar: (1) yanlış kardeşe bağlanma (ikizkenar üçgende yükseklik ← "dik üçgende yükseklik" yerine genel yükseklik; sürat ← "yer değiştirme" yerine alınan yol), (2) tanım bilgisinin uygulamaya değil süreç adımına bağlanması (karesel fonksiyonun tanım kümesi ← "temsiller hakkında yargıda bulunur" yerine ← fonksiyonun tanım kümesi ve kare alma), (3) gerçek ön koşulun eksik olması (birim çemberde kosinüs ← dik üçgende kosinüs oranı; sin²x + cos²x = 1 ← Pisagor bağıntısı; logaritma kuralları ← üslü ifade kuralları), (4) dolaylı yoldan zaten gelen bağın tekrar yazılması. Ön koşulu tümüyle bilinen ön öğrenmeye dayanan MK'ler kök yapıldı ve ön öğrenme `on_kosul_diger` alanına yazıldı (ör. kuvvet çeşitlerini belirleme ← fen bilimleri). Fizikte 169, matematikte 355 MK'nin ön koşulu değişti (matematik: 414 bağ çıktı, 400 bağ girdi). Sonuç: fizik 1.208 bağ, 25 katman, 46 kök; matematik 2.601 bağ, 41 katman, 26 kök. Sınıf sırası ihlali ve harita denetim hatası yok. Ardından aynı becerinin iki sınıfta ayrı MK olarak yazıldığı iki tekrar birleştirildi (Murat: "birleştir"): 9. sınıftaki Pisagor ile kenar hesaplama (eski Mat08MK0015) Mat03MK0143'e, Pisagor üçlüleri (eski Mat08MK0016) Mat03MK0140'a katıldı; 8. sınıf MK'leri 9. sınıf öğrenme çıktısına da eşlendi, ardılları bunlara bağlandı, Mat08 kodları boşluksuz yeniden numaralandı. Tek hedef kuralı: aynı soruyla ölçülen beceri tek MK'dir; 9. sınıfta yeni olan ispat (Mat08MK0010) zaten ayrı MK. Matematik 1.664 MK, 2.599 bağ.

**Formülün tarihçesi:**
1. 2026-10-01: Z = √(kendisi + altındaki tüm farklı MK'ler), v = 0.25 · 0.5 · 0.75 · 1.0, Seviye = 0.5'lik aralık. Bölme sonrası şişti (en yüksek 15.30).
2. 2026-10-01: Z = √(kendisi + doğrudan ön koşullar). Şişme bitti ama kendi değeri kök altında ezildi; MK'lerin çoğu tek seviyede toplandı (2026-10-02'de aralık geçici olarak 0.25'e daraltıldı).
3. 2026-10-02: Z = v + √Σ v(p), v = 1 + log₂(r), Seviye = ⌊Z⌋. Kendi değeri tam sayıldı, ama doğrusal ve köklü terim karıştı (saf RSS değil).
4. **2026-10-02 (geçerli, Murat: "logaritmik + RSS"):** Z = √(v² + Σ v(p)²), v = 1 + log₂(r), Seviye = ⌊Z⌋.

### 4.6 Kalibrasyon (ileride)

Değerler ön (a priori) ağırlıklardır. Veri yokken harita değerleriyle başlanır; ilk cevaplarla değerler Elo güncellemesiyle (Elo, 1978; eğitimde Pelánek, 2016) küçük adımlarla düzeltilir; yeterli veri birikince Rasch kalibrasyonuna geçilir. Öğrenci verisi geldiğinde her MK'nin gerçek zorluğu **Rasch modeliyle** (Rasch, 1960; Madde Tepki Kuramı, IRT) logit ölçeğinde kestirilecek: P(doğru) = 1 / (1 + e^−(θ − b)). Logit ölçeği de logaritmiktir; bu yüzden logaritmik işlem değerleri ile Rasch zorlukları (b) arasında doğrusal bir ilişki beklenir. Regresyonla işlem değerleri ve birleştirme üssü (RSS'de kare ve kök; genel biçimde Z = (Σ vᵢ^q)^(1/q), şu an q = 2) veriye göre ayarlanacak.

### 4.7 Denenen ve bırakılan yollar (kısa)

- Uzmanın S1–S5 vermesi (gözle ya da ölçüt puanıyla): kişiye bağlı, ön koşul ilişkisini yansıtmıyor.
- max(öz puan, ön koşul tabanı): erken bir S3 sonrakilerin hepsini S3'e çekti.
- Sıralı ağırlıklar (%100, %50, %25, %10, %5) + işlem değeri, açık denklemde tekrarı silerek: birikim doğru ama düz toplama, en uzun zincirde 35 kat fark (0.25 → 8.77). RSS'de yan dallar tam sayılıyor; sıralı ağırlıklar zaten RSS'nin yaklaşığıydı (5 ve 5: 7.5 / RSS 7.07; 5 ve 1: 5.5 / RSS 5.10).
- En büyük ön koşulun %80–%90'ını almak: tavan oluşuyor ama bazı MK'ler ön koşulunun altına düşüyor.
- İşlem değerini çarpan yapmak (×1.5, ×2 …): zincir boyunca katlanarak büyüyor (0016 ≈ 300).

## 5. Soru eşleme ve soru zorluğu (karar: 2026-10-03, Murat)

Özet:

> **Sorunun MK'leri = çözüm için gereken MK'lerin en üsttekileri** (birbirinin öncülü olanlardan alttaki çıkar)
> **Soru zorluğu b = Σ Z(k)**  (k: sorunun MK'leri; Z: bölüm 4'teki MK zorluğu)
> Ölçekleme yok: b ne çıkıyorsa sorunun zorluğu odur.

### 5.1 İki ayrı eşleme: sorunun MK'leri ve rubrik MK'leri

Bir soru, birden çok MK'nin birlikte kullanılmasını ölçer. Bu yüzden iki eşleme tutulur ve ikisinin aynı olması gerekmez:

- **Sorunun MK'leri:** Soruyu bir bütün olarak çözmek için gereken **en üstteki** MK'ler. Eşlenen bir MK, eşlenen başka bir MK'nin doğrudan ya da dolaylı öncülüyse listeden çıkarılır, çünkü üstteki MK'yi bilmek onu bilmeyi de içerir (Murat: "MK10 ve MK20'yi bilmek diğerlerini bilmek demek zaten"). Soru zorluğu bunlardan hesaplanır. Uyarlamalı test "bu MK'ler biliniyor mu" kararını bunlarla verir. Biri **birincil MK** olarak işaretlenir (sorunun asıl ölçtüğü); bu, hesaba değil eşleme ve rapora girer.
- **Rubrik MK'leri:** Çözümün her adımının dayandığı MK. Bunlar sorunun MK'lerinin ön koşulları da olabilir. Teşhis içindir: öğrenci soruyu yapamadığında eksiğin üst MK'nin kendisinde mi, yoksa onu oluşturan bir ön koşulda mı olduğunu gösterir.

**Denetim kuralı:** Her rubrik MK'si ya sorunun MK'lerinden biri ya da onların ön koşul zincirinde olmalıdır. Zincir dışında bir MK gerektiren rubrik adımı, sorunun MK listesinde bir üst MK'nin eksik olduğunu gösterir.

**Kuram:** Madde düzeyinde Q-matris (soru × beceri tablosu; Tatsuoka, 1983, Kural Uzayı), adım düzeyinde bilişsel tanı modelleri (ör. DINA; de la Torre, 2009). Ön koşulların soruya ayrıca eşlenmemesi Bilgi Uzayı Kuramı'ndaki ön koşul ilişkisinden gelir (Doignon ve Falmagne, 1999): üstteki bilgi, alttakini gerektirir.

### 5.2 Soru zorluğu: b = Σ Z

**Ne:** Sorunun (en üstteki) MK'lerinin Z değerlerinin düz toplamı.

**Neden toplam:** Rasch modelinde zorluk logit ölçeğindedir (P(doğru) = e^(θ − b) / (1 + e^(θ − b))). Bir soruyu çözmek için her bileşenin başarılması gerekir; bağımsız olayların birlikte gerçekleşme olasılığı çarpımla bulunur, logaritmik ölçekte bu çarpım toplama dönüşür. Bileşenlerden soru zorluğu kuran model **LLTM**'dir (Doğrusal Lojistik Test Modeli; Fischer, 1973): b(soru) = Σ q(soru, k) · η(k) + c. Bizde q, sorunun MK eşlemesi; η(k)'nın başlangıç değeri MK'nin Z'si. Benzer yaklaşım: açıklayıcı madde tepki kuramı (De Boeck ve Wilson, 2004) ve Embretson'un bilişsel tasarım sistemi (Embretson, 1998).

**Neden v değil Z:** İlk öneri η = v (yalnız işlem değeri) idi. Murat'ın itirazı: işlem değerleri aynı iki soru, MK'lerinin ön koşul zincirleri farklıysa aynı zorlukta çıkar; bu adil değil. Gerçekte derin bir zincirin üstündeki MK'yi daha az öğrenci bilir ve veri geldiğinde Rasch bunu yüksek η olarak tahmin eder. Bu yüzden başlangıç değeri, ön koşul payını da içeren Z'dir. Çift sayım, 5.1'deki "yalnız en üstteki MK'ler" kuralıyla önlenir.

**Neden RSS değil:** Soru düzeyinde RSS'in ölçme kuramında dayanağı yok (ölçüm hatası birleştirmesinden bir benzetme). Toplam ise logit ölçeğinin doğal birleştirmesi.

**Neden ölçekleme yok:** 1–10 gibi bir aralığa çevirmek için en kolay ve en zor sorunun bilinmesi gerekir; başlangıçta soru bankası çok küçük. b olduğu gibi kullanılır (Murat, 2026-10-03).

**Bilinen sınır:** Model yalnız bileşen toplamını görür. Soruya özgü zorluk (ör. kilit bir fikri fark etmek) artık terim olarak kalır; veriyle Rasch kalibrasyonu ya da LLTM'ye ek bir bileşen bunu düzeltir.

### 5.3 Rubrik ve puanlama

**Ağırlıklar MK modelinden gelir.** Bir MK'nin Z'si, kendi işi ile doğrudan ön koşullarının birleşimidir: Z² = v² + Σ v(p)². Her parçanın payı v²/Z²'dir. "Kendi" payı, ön koşulları bildikten sonra onları birleştirip üstüne koyduğu beceridir (Murat: "üstüne kural uygulama becerisini ekliyor, rubrikte bunu da ölçeceğim").

**Puan:** Her şeyi doğru yapan sorunun b'sinin tamamını alır; kısmen yapan, yaptığı adımların payı kadarını: **puan = Σ (doğru adımların payı) × b**. Kazanılan v²'lerin karekökü alınmaz, çünkü o zaman parçaların toplamı bütüne eşit çıkmaz.

**Örnek: Fiz05MK0051**, birleşik devrenin eşdeğer direncini adım adım indirgeyerek hesaplar (Z = 5,72):

| Parça | v | v² | Pay | 5,72 üzerinden |
|---|---|---|---|---|
| Fiz05MK0051 kendisi: adım adım indirgeme (kural uygulama) | 2 | 4 | %12,2 | 0,70 |
| Fiz05MK0037 devreyi seri ve paralel gruplarına ayırır | 2 | 4 | %12,2 | 0,70 |
| Fiz05MK0038 kısa devre olan direnci bulur ve çıkarır | 2,585 | 6,68 | %20,4 | 1,17 |
| Fiz05MK0045 seri bağlamada Reş = R1 + R2 + … | 3 | 9 | %27,5 | 1,58 |
| Fiz05MK0047 paralel bağlamada 1/Reş = 1/R1 + 1/R2 + … | 3 | 9 | %27,5 | 1,58 |

Paralel formülü dışındaki her şeyi doğru yapan öğrenci %72,5 × 5,72 = 4,15 alır. Not: 0045 ve 0047 "modeli veriyle test eder" diye yazıldığı için v = 3; soruda formül yalnız uygulanıyor, ağırlık olduğundan büyük görünebilir. Kalibrasyonda bakılacak.

Soru birden çok üst MK'ye eşlendiğinde her üst MK bir rubrik adımıdır ve payı kendi Z'sidir; gerekirse her biri yukarıdaki gibi kendi parçalarına bölünür.

### 5.4 Örnekler

**Yay sorusu** (2 kg cisim 5 m yükseklikten bırakılıyor, K–L sürtünmesiz, L–M 5 m ve k = 0,4, sonra k = 200 N/m yay; en fazla sıkışma ≈ 77,5 cm):

| Sorunun MK'si | Z |
|---|---|
| Fiz04MK0133 kinetik, çekim ve esneklik potansiyel enerjisi ile sürtünme işini birlikte kullanarak enerjinin korunumunu değerlendirir (birincil) | 3,74 |
| Fiz04MK0096 Ep = m·g·h | 3,46 |
| Fiz02MK0139 Fs = k·N | 3,61 |
| **b** | **10,81** |

Sürtünme işi (Fiz04MK0129) ve Ep = ½kx² (Fiz04MK0124), Fiz04MK0133'ün öncülleri olduğu için soruya ayrıca eşlenmez; rubrik adımı olarak teşhiste yer alır.

**Üç özdeş cisim sorusu** (aynı hızla fırlatılıp farklı yollarda duruyorlar; ivme, kaybedilen mekanik enerji, süre hangileri eşit? Cevap: yalnız II):

| Rubrik adımı | Sorunun MK'si | Z |
|---|---|---|
| III. x = (v/2)·t, süreler farklı | Fiz02MK0059 hız-zaman grafiği altındaki alandan yer değiştirme | 2,83 |
| I. a = v / t, ivmeler farklı | Fiz02MK0064 ivme = Δv / Δt | 2,45 |
| II-a. Kayıp = ilk kinetik enerji ½mv² | Fiz04MK0095 Ek = ½·m·v² | 3,46 |
| II-b. Kayıp sürtünmeyle ısıya gider, yoldan bağımsız, eşit | Fiz04MK0097 sürtünmeli ortamda mekanik enerjinin ısıya dönüşmesi | 3,70 |
| **b** | | **12,44** |

Örnek öğrenci yalnız x = (v/2)·t ilişkisini üç cisim için kurmuş: 2,83 / 12,44 (%23). Doğru çizdiği sürtünme kuvveti yönü (Fiz02MK0119) cevap için gerekli olmadığından puana girmez.

## 6. MK teşhisi ve "biliyor" kararı (karar: 2026-10-03, Murat)

### 6.1 Üç durum

Puan ile teşhis ayrıdır. Yapılmayan adımdan puan alınmaz; ama MK durumu üçtür:
- **Biliyor:** adım doğru yapılmış.
- **Bilmiyor:** adım denenmiş ama yanlış yapılmış (yanlış formül, yön ya da sonuç).
- **Ölçülemedi:** adıma gelinmemiş ya da boş bırakılmış.

Boş adım "bilmiyor" sayılmaz: süre, önceki bir adımda takılma ya da yazmama da nedeni olabilir. Bilişsel tanı modellerinde de boş cevap "yanlış" değil "eksik veri" olarak işlenir. "Ölçülemedi" MK'ler uyarlamalı testin sıradaki hedefidir: o MK'yi tek başına ölçen kısa bir soru sorulur.

### 6.2 Biliyor kararı: Bayesçi Bilgi İzleme

**Ne:** Her öğrenci ve MK için "biliyor" olasılığı P(L) tutulur, her cevaptan sonra Bayes kuralıyla güncellenir (Bayesian Knowledge Tracing; Corbett ve Anderson, 1995):
- Doğru cevaptan sonra: P(L) ← P(L)(1 − s) / [P(L)(1 − s) + (1 − P(L)) g]
- Yanlış cevaptan sonra: P(L) ← P(L) s / [P(L) s + (1 − P(L))(1 − g)]
- g: tahminle doğru bulma olasılığı; s: bilenin dikkatsizlikle yanlış yapma olasılığı.

**Karar eşikleri:** P(L) ≥ 0,95 ise **biliyor**; P(L) ≤ 0,20 ise **bilmiyor**; arada kaldıkça soru sorulur. Sınav sırasında öğrenme olmadığı varsayılır (öğrenme geçişi 0).

**Başlangıç değerleri (varsayım, veriyle tahmin edilecek):** P(L₀) = 0,5; s = 0,10; g = 0,20 (5 şıklı çoktan seçmeli), g ≈ 0,05 (açık uçlu). Buna göre "biliyor" için çoktan seçmelide 2 doğru (%82, sonra %95), açık uçluda 1 doğru (%95) yeter; karışık cevaplarda daha çok soru gerekir.

**Neden sabit kural değil:** CSV'deki "3 maddeden en az 2'si doğru" kuralı bu varsayımlarla bilmeyen öğrenciyi %10,4 olasılıkla "biliyor" sayar; bileni %97 olasılıkla doğru tanır. Bayesçi izleme kanıt yeterli olunca durur, soru sayısını cevaplara göre ayarlar. "3'te 2" kuralı veri yokken kontrol olarak kalır.

**Ek kanıtlar:** Bir sorunun içinde doğru yapılan rubrik adımı, o MK için bir doğru cevap gibi işlenir. Ön koşul haritası da kanıt taşır: üstteki MK biliniyorsa alttakilerin P(L)'si yükselir, alttaki bilinmiyorsa üsttekinin düşer (Bilgi Uzayı Kuramı). İkisi de sorulması gereken soru sayısını azaltır.

### 6.3 Uyarlamalı akış (örnek)

Öğrenci büyük bir soruyu yapamazsa önce sorunun daha basit hâli sorulur (ör. sürtünmesiz sürümü). Doğruysa eksik çıkarılan parçadadır (sürtünme işi), yanlışsa ön koşullara (Ek, Ep modelleri) inilir. Yanlış cevabın kendisi de bilgi taşır (ör. sürtünme kaybını hiç düşmemek Fiz04MK0097/0098 eksikliğini gösterir). Haritada yanlışta aşağı, doğruda yukarı ya da yana gidilir.

## 7. Uygulama ve demo kararları (2026-10-03, Murat)

- **Hedef:** MK haritası, kazanım eşlemesi ve zorluk modeliyle çalışan bir uygulama: soru üretme ve MK'ye eşleme; verilen bir soruyu (fotoğraf, PDF, Word) okuyup MK'ye eşleme, çözme, rubrik çıkarma ve rubrik adımlarını MK'ye eşleme; uyarlamalı test; MK bazında ayrıntılı rapor. İçerik önerisi Faz 3.
- **Platform:** Önce web; telefonda tarayıcıdan kamera ile fotoğraf çekilebilir, PWA olarak ana ekrana eklenebilir. Mobil uygulama sonra.
- **Kullanıcı:** Demo öğretmenlere ve fikrin gösterileceği kişilere yönelik; öğrenci ekranı şimdilik yok. Uyarlamalı sınav, öğretmenin cevapları seçtiği "örnek öğrenci" canlandırmasıyla gösterilecek.
- **Demo sırası:** 1) soru yükle → oku, çöz, rubrik, MK eşleme, zorluk; 2) MK ya da kazanımdan soru üret, öğretmen onayıyla bankaya; 3) sınav hazırla, uyarlamalı akış ve rapor; ayrıca ön koşul haritası görünümü.
- **Pilot kapsam:** Fizik 10–12 enerji ve hareket; Matematik 8–9 üçgenler ve Pisagor.
- **Teknik yön (öneri):** Okuma, çözme ve eşlemede Claude'un görsel modeli (ayrı OCR yok); arka uç Python (zorluk ve harita araçları Python'da); ön yüz web.

## 8. Açık konular

- İşlem türü atamalarının gözden geçirilmesi (316 MK).
- Kalibrasyon: bkz. 4.6 (Rasch ile işlem değerleri ve ön koşul teriminin katsayı ve üssü ayarlanacak).
- Alt sınıfa eşlenen mikro kazanımlar: bir mikro kazanım alt sınıfa eşlenince, üst sınıf ön koşulları alt sınıf karşılıklarıyla değiştirilir (öğrenciye kendi sınıfının üstünden soru gelmemesi için). Denetim: her mikro kazanımın ön koşullarının en düşük sınıfı, kendi en düşük sınıfından büyük olamaz.
- Dersler arası karşılaştırılabilirlik: haritaların incelik düzeyi farklıysa (ör. 8. sınıf problem çözme süreci 10 MK'ye bölünmüştü; 2026-10-01'de 4 MK'ye indirildi) puanlar yapay yükselebilir. Dersler eklendikçe dağılımlar yan yana kontrol edilecek.
- y (MK başarı oranı = doğru / karşılaşılan soru) nerede kullanılacak?
- "Anladı" eşiği: 6.2'de Bayesçi Bilgi İzleme ile karara bağlandı; tahmin (g) ve dikkatsizlik (s) payları veriyle tahmin edilecek.
- "Modeli veriyle test eder" türündeki MK'ler (ör. Fiz05MK0045, 0047) sorularda yalnız uygulanıyor; işlem değeri ve rubrik ağırlığı olduğundan büyük olabilir (5.3).
- Soru zorluğunda soruya özgü bileşen (kilit fikri fark etme) LLTM'ye nasıl eklenecek (5.2).
- Bir rubrik adımının kanıtı ile ayrı bir sorunun kanıtı Bayesçi izlemede aynı ağırlıkta mı sayılacak (6.2).

## 9. Kaynakça

- Anderson, L. W. ve Krathwohl, D. R. (Ed.) (2001). *A Taxonomy for Learning, Teaching, and Assessing: A Revision of Bloom's Taxonomy of Educational Objectives.* New York: Longman.
- Ausubel, D. P. (1968). *Educational Psychology: A Cognitive View.* New York: Holt, Rinehart and Winston.
- Biggs, J. B. ve Collis, K. F. (1982). *Evaluating the Quality of Learning: The SOLO Taxonomy.* New York: Academic Press.
- Chase, W. G. ve Simon, H. A. (1973). Perception in chess. *Cognitive Psychology*, 4(1), 55–81.
- Corbett, A. T. ve Anderson, J. R. (1995). Knowledge tracing: Modeling the acquisition of procedural knowledge. *User Modeling and User-Adapted Interaction*, 4(4), 253–278.
- De Boeck, P. ve Wilson, M. (Ed.) (2004). *Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach.* New York: Springer.
- de la Torre, J. (2009). DINA model and parameter estimation: A didactic. *Journal of Educational and Behavioral Statistics*, 34(1), 115–130.
- Doignon, J.-P. ve Falmagne, J.-C. (1985). Spaces for the assessment of knowledge. *International Journal of Man-Machine Studies*, 23(2), 175–196.
- Doignon, J.-P. ve Falmagne, J.-C. (1999). *Knowledge Spaces.* Berlin: Springer.
- Elo, A. E. (1978). *The Rating of Chessplayers, Past and Present.* New York: Arco.
- Embretson, S. E. (1998). A cognitive design system approach to generating valid tests: Application to abstract reasoning. *Psychological Methods*, 3(3), 380–396.
- Falmagne, J.-C. ve Doignon, J.-P. (2011). *Learning Spaces: Interdisciplinary Applied Mathematics.* Berlin: Springer.
- Fechner, G. T. (1860). *Elemente der Psychophysik.* Leipzig: Breitkopf und Härtel.
- Fischer, G. H. (1973). The linear logistic test model as an instrument in educational research. *Acta Psychologica*, 37(6), 359–374.
- Gagné, R. M. (1968). Learning hierarchies. *Educational Psychologist*, 6(1), 1–9.
- Hick, W. E. (1952). On the rate of gain of information. *Quarterly Journal of Experimental Psychology*, 4(1), 11–26.
- Hyman, R. (1953). Stimulus information as a determinant of reaction time. *Journal of Experimental Psychology*, 45(3), 188–196.
- Leighton, J. P. ve Gierl, M. J. (Ed.) (2007). *Cognitive Diagnostic Assessment for Education: Theory and Applications.* Cambridge: Cambridge University Press.
- Mager, R. F. (1962). *Preparing Instructional Objectives.* Palo Alto: Fearon.
- Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. *Psychological Review*, 63(2), 81–97.
- Pelánek, R. (2016). Applications of the Elo rating system in adaptive educational systems. *Computers & Education*, 98, 169–179.
- Piaget, J. (1970). *Genetic Epistemology.* New York: Columbia University Press.
- Rasch, G. (1960). *Probabilistic Models for Some Intelligence and Attainment Tests.* Kopenhag: Danmarks Pædagogiske Institut.
- Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27(3), 379–423.
- Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science*, 12(2), 257–285.
- Sweller, J., van Merriënboer, J. J. G. ve Paas, F. G. W. C. (1998). Cognitive architecture and instructional design. *Educational Psychology Review*, 10(3), 251–296.
- Tatsuoka, K. K. (1983). Rule space: An approach for dealing with misconceptions based on item response theory. *Journal of Educational Measurement*, 20(4), 345–354.
- Taylor, J. R. (1997). *An Introduction to Error Analysis* (2. baskı). Sausalito: University Science Books.
- Weber, E. H. (1834). *De pulsu, resorptione, auditu et tactu: Annotationes anatomicae et physiologicae.* Leipzig: Koehler.

## Ek A. Terimler sözlüğü

| Terim | Anlamı |
|---|---|
| **Birincil MK** | Bir sorunun asıl ölçtüğü MK; eşleme ve raporda kullanılır (5.1). |
| **Bilgi / Beceri** | MK türü: bilmek, tanımak, açıklamak (Bilgi) ya da bir işlemi yürütmek (Beceri) (2.3). |
| **Bilgi Uzayı Kuramı** | Bilgi birimleri arasındaki ön koşul ilişkisini kısmi sıralama olarak modelleyen kuram (3.4). |
| **Bayesçi Bilgi İzleme (BKT)** | Her cevaptan sonra "biliyor" olasılığını güncelleyen model (6.2). |
| **Çeldirici** | Çoktan seçmeli sorudaki yanlış şık; yanılgılardan üretilir (2.3). |
| **DAG** | Yönlü döngüsüz grafik; ön koşul haritasının matematiksel yapısı (3.1). |
| **Derinlik / katman** | Bir MK'nin altındaki en uzun ön koşul zinciri; katman sayısı = en büyük derinlik + 1 (3.1). |
| **Doğrudan ön koşul** | Bir MK'ye ok ile bağlı, o adımın gerçekten dayandığı MK (3.2). |
| **Elo güncellemesi** | Her cevaptan sonra öğrenci ve soru puanını küçük adımlarla düzelten yöntem; veri azken kullanılır (4.6). |
| **Eşleme** | Bir MK'nin bir öğrenme çıktısına (ve sınıfa) bağlanması; aynı MK birden çok çıktıya eşlenebilir (2.2). |
| **İşlem türü / işlem değeri (v)** | MK'nin eklediği tek zihinsel işlem ve bunun sayısal ağırlığı: 1, 2, 2,585, 3 (4.2). |
| **Kök** | Haritada ön koşulu olmayan MK (3.1). |
| **Temel / bütünleştirici MK** | Ön koşulu olmayan, bir şeyi ilk kez kazandıran MK / önceki MK'leri birleştirip üstüne yeni adım ekleyen MK (2.2). |
| **LLTM** | Doğrusal Lojistik Test Modeli; soru zorluğunu bileşenlerin katkılarının toplamı olarak modeller (5.2). |
| **Logit** | Rasch ölçeğinin birimi; olasılığın logaritmik dönüşümü. |
| **Mikro kazanım (MK)** | Ön koşullarının üzerine tek bir yeni bilgi ya da beceri adımı ekleyen, tek bir soruyla bütünüyle ölçülebilen öğrenme birimi; temel ya da bütünleştirici olur (2.2). |
| **Ölçülemedi** | Öğrencinin ulaşmadığı ya da boş bıraktığı adımın MK durumu; "bilmiyor" sayılmaz (6.1). |
| **Öğrenme çıktısı (ÖÇ)** | TYMM programındaki hedef, ör. FİZ.10.3.4 (2.1). |
| **Q-matris** | Hangi sorunun hangi MK'yi ölçtüğünü gösteren soru × MK tablosu (5.1). |
| **Rasch modeli** | Doğru cevap olasılığını öğrenci yeteneği ile soru zorluğu farkına bağlayan model; kalibrasyonun aracı (4.6, 5.2). |
| **RSS** | Kareler toplamının kökü; MK zorluğunda bileşenleri birleştirme yöntemi (4.3). |
| **Rubrik** | Bir sorunun çözüm adımları ve her adımın puan payı; adımlar MK'lere eşlenir (5.3). |
| **Seviye** | MK zorluğunun tam sayı kısmı: ⌊Z⌋ (4.4). |
| **Soru zorluğu (b)** | Sorunun en üstteki MK'lerinin Z değerlerinin toplamı (5.2). |
| **Süreç bileşeni** | Öğrenme çıktısının (a), (b), (c) alt adımları (2.1). |
| **Tek ölçülebilir hedef** | Bir soru MK'nin yalnız bir parçasını sorabiliyorsa MK'nin bölünmesi kuralı (2.2). |
| **Yanılgı** | Öğrencilerde sık görülen, tutarlı ama yanlış düşünce; YG koduyla tutulur (2.3). |
| **Zorluk (Z)** | Bir MK'yi öğrenmenin zorluğu: √(v² + Σ doğrudan ön koşul v²) (bölüm 4). |
