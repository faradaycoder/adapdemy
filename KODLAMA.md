# EVALORA Kodlama Kuralları

## Mikro kazanım kodu

`<Ders><2 haneli ana ünite>MK<4 haneli numara>` (örnek: `Fiz05MK0056`, `Mat01MK0175`)

- Ders kısaltmaları: **Fiz** (Fizik), **Mat** (Matematik).
- Ana ünite kodu **sınıftan bağımsızdır**: aynı konu 10. ve 11. sınıfta işlense de aynı kodu taşır (Elektrik ve Manyetizma her zaman `05`).
- 4 haneli numara, o ana ünite içinde 0001'den başlayan sıra numarasıdır.
- Verilen kod **asla değişmez** ve silinse bile başka bir mikro kazanıma **yeniden verilmez**. Kullanımdan kalkan kodun durumu "iptal" yapılır.
- Aynı şeyi anlatan mikro kazanım başka bir sınıfta ya da öğrenme çıktısında geçerse **yeniden yazılmaz**; "Kazanım Eşleme" sayfasına yeni bir satır eklenir. Yeni kod vermeden önce aynı ana ünitedeki mevcut mikro kazanımlar taranır.

## Mikro kazanım türü (zorunlu): Bilgi / Beceri

Her mikro kazanım yazılırken türü de yazılır; CSV'lerde ve Excel'lerde "Tür" sütununda tutulur.

- **Bilgi:** Öğrencinin bir kavramı, tanımı, kuralı ya da ilişkiyi bilmesi, tanıması, açıklaması. Ölçülen şey doğru bilgidir ("ne", "neden"). Örnek: `Fiz05MK0035` seri bağlı dirençleri tanır.
- **Beceri:** Öğrencinin bir işlemi, yöntemi ya da süreci yürütmesi: ölçer, kaydeder, çizer, hesaplar, bağlar, test eder, değerlendirir. Ölçülen şey yapabilmektir. Örnek: `Fiz05MK0051` birleşik devrenin eşdeğer direncini hesaplar.
- Karar ana fiile ve ölçmede gözlenen çıktıya göre verilir. Bir mikro kazanım ikisini birden içeriyorsa atomik kurala göre ikiye bölünür.

### Tek ölçülebilir hedef kuralı (2026-10-01, Murat)

Bir mikro kazanım, ön koşullarının üzerine tek bir yeni bilgi ya da beceri adımı ekleyen ve tek bir soruyla bütünüyle ölçülebilen öğrenme birimidir (temel ya da bütünleştirici; tanım ve dayanakları `ALGORITMA.md` 2.2). Sınama: “Bir soru bu MK’nin yalnızca bir parçasını sorabilir mi?” Sorabiliyorsa MK bölünür; aksi hâlde öğrenci bir parçada başarısız olduğunda öbür parça hakkında da karar verilmiş olur (ölçme hatası) ve eksik kök yanlış teşhis edilir (içerik önerme hatası). Örnek: “ortalama sürati ve ortalama hızı hesaplar” iki MK’dir.

- Farklı içerik ayrı MK olur: farklı değişken (“frekansa bağlı değildir” ile “genliğe bağlı değildir”), kavram, kural, model, liste öğesi ya da durum (“aynı yönlüyse hızlanır” ile “zıt yönlüyse yavaşlar”).
- Bilgi ile Beceri aynı MK’de durmaz (“bağlar ve nedenini açıklar” iki MK’dir).
- Aynı becerinin farklı örneklere ya da bağlamlara uygulanması tek MK kalır (“her dirençteki akımı ölçer”, “kapı, anahtar ve tahterevalli gibi durumlarda torku hesaplar”).
- “X ile Y’yi ayırt eder” yalnızca ayrımın kendisi hedefse (bilinen karışıklık: yer değiştirme–yol, magnitüd–şiddet) tek MK kalır.
- Süreç adımları (problem çözmenin 4 adımı; muhakemenin varsayım, sınama, önerme, kullanışlılık ve ispat adımları) ayrı MK’dir ve adım sayısı korunur. Ancak adımın konusu birden çok ayrı içerik taşıyorsa (ör. “denklem ve eşitsizlik”, “2, 3, 4, 5, 8, 9 ve 10 ile bölünebilme”) adım konu konu bölünür (Murat, 2026-10-01). Tek konulu süreç adımı bütün kalır.
- Paralel bölmelerde (ör. kesirlerde toplama/çıkarma ile rasyonel sayılarda toplama/çıkarma) her parça yalnızca karşılığı olan parçaya ön koşul olarak bağlanır.
- “Ve” yalnızca bir işarettir; her MK tek tek okunup karar verilir. Bölmede mevcut kod ilk parçayı tutar, diğer parçalar yeni kod alır; başka MK’nin tekrarı çıkan kod “iptal” olur.

### Ön koşul bağı kuralı (2026-10-02, Murat)

Bir MK'ye yalnızca o adımın **gerçekten dayandığı** MK'ler doğrudan ön koşul olarak bağlanır. Bağlanmaz: kardeş konu (kesir problemi ← ondalık işlem), süreç adımı (formülü kullanma ← formülün ispatı ya da sınanması), ilgisiz komşu (çift yarık deneyi ← ışık şiddeti birimi), birim bilgisi (kuvvetleri ayırt etme ← newton birimi), aynı ünitedeki önceki ama gereksiz MK. Dolaylı ön koşullar zincirden gelir, ayrıca bağlanmaz. Zorluk doğrudan ön koşullardan hesaplandığı için gereksiz bağ zorluğu şişirir.

## İşlem türü (zorunlu) ve zorluk

Her mikro kazanım, ön koşullarının üstüne tek bir ana işlem ekler; bu işlem CSV'de `islem_turu` sütununa yazılır. Türler ve değerleri `ortak/islem_turleri.csv`'dedir (15 tür, tüm dersler için):

İşlem değeri logaritmiktir, v = 1 + log₂(sıra) (Weber–Fechner):

- **1 (küçük):** Tanıma ve hatırlama, Gözlem ve kayıt, Taklit
- **2 (orta):** Kural uygulama, Dönüştürme, Ayırt etme ve sınıflama, Açıklama ve özetleme, Karşılaştırma, Beceri uygulama
- **2.585 (büyük):** Yorumlama, Çıkarım ve ilişkilendirme
- **3 (çok büyük):** Model kurma, Sınama ve değerlendirme, Üretme ve tasarım, Transfer ve problem çözme

Karar ana fiile ve ölçmede gözlenen çıktıya göre verilir ("tipik fiiller" sütununa bakılır). İki işlem içeren mikro kazanım atomik kurala göre bölünür; bölünmemiş eski kazanımlarda ağır basan (ölçülen) işlem seçilir.

Zorluk ve seviye elle yazılmaz, haritadan hesaplanır (`araclar/zorluk.py`):
- **Zorluk** = √(kendi işlem değerinin karesi + doğrudan ön koşullarının işlem değerlerinin kareleri toplamı) (RSS, 2026-10-02; alt zincir sayılmaz)
- **Seviye** = ⌊Zorluk⌋ (1 genişliğinde tam sayı aralıklar, üstü açık; açıklamalar `ortak/zorluk_seviyeleri.csv`)

Matematiği, gerekçesi ve dayandığı kuramlar (Bilgi Uzayı Kuramı, Weber–Fechner, Hick–Hyman, Bilişsel Yük Kuramı, RSS, Rasch): `ALGORITMA.md` bölüm 4.

## Yanılgı kodu

`<Ders><2 haneli ana ünite>YG<4 haneli numara>` (örnek: `Fiz05YG0006`). Yanılgılar da sınıftan bağımsızdır ve aynı kurallara uyar.

## Fizik ana üniteleri (tüm fizik müfredatı, 9–12)

| Kod | Kısaltma | Ana ünite | Sınıflar | Sınıf üniteleri |
|---|---|---|---|---|
| 01 | FBK | Fizik Bilimi ve Kariyer | 9 | Fiz09-U1 |
| 02 | MEK | Kuvvet ve Hareket | 9, 10, 11, 12 | Fiz09-U2, Fiz10-U1, Fiz11-U1, Fiz12-U1 |
| 03 | AKS | Akışkanlar | 9 | Fiz09-U3 |
| 04 | ENJ | Enerji | 9, 10, 12 | Fiz09-U4, Fiz10-U2, Fiz12-U2 |
| 05 | ELK | Elektrik ve Manyetizma | 10, 11 | Fiz10-U3, Fiz11-U2 |
| 06 | DLG | Dalgalar | 10, 12 | Fiz10-U4, Fiz12-U3 |
| 07 | OPT | Optik | 11 | Fiz11-U3 |
| 08 | MDD | Madde ve Doğası | 12 | Fiz12-U4 |

Fizik 9–12 üniteleri 29.09.2026'da TYMM'den doğrulandı (15 ünite).

## Matematik ana temaları

| Kod | Ana tema | Sınıflar | Sınıf temaları |
|---|---|---|---|
| 01 | Sayılar ve Nicelikler | 5; 6; 7; 8; 9; 10 | Mat05-T1; Mat06-T1; Mat07-T1; Mat08-T1; Mat09-T1; Mat10-T3 |
| 02 | Cebirsel Düşünme ve Değişimler | 5; 6; 7; 8; 9; 10; 11; 12 | Mat05-T2; Mat06-T2; Mat07-T2; Mat08-T2; Mat09-T2; Mat10-T4; Mat11-T3; Mat12-T1 |
| 03 | Geometrik Şekiller | 5; 6; 7; 8; 9; 10; 11; 12 | Mat05-T3; Mat06-T3; Mat07-T5; Mat08-T3; Mat09-T3; Mat10-T1; Mat11-T2; Mat12-T2 |
| 04 | Geometrik Nicelikler | 5; 6; 7; 8; 12 | Mat05-T4; Mat06-T4; Mat07-T4; Mat08-T4; Mat12-T3 |
| 05 | Dönüşüm | 7; 8 | Mat07-T3; Mat08-T5 |
| 06 | İstatistiksel Araştırma Süreci | 5; 6; 7; 8; 9; 10; 11; 12 | Mat05-T5; Mat06-T5; Mat07-T6; Mat08-T6; Mat09-T6; Mat10-T2; Mat11-T1; Mat12-T5 |
| 07 | Veriden Olasılığa | 5; 6; 7; 8; 9; 10 | Mat05-T6; Mat06-T6; Mat07-T7; Mat08-T7; Mat09-T7; Mat10-T7 |
| 08 | Eşlik ve Benzerlik | 9 | Mat09-T4 |
| 09 | Algoritma ve Bilişim | 9; 10 | Mat09-T5; Mat10-T5 |
| 10 | Analitik İnceleme | 10 | Mat10-T6 |
| 11 | Değişimin Matematiği | 12 | Mat12-T4 |

Matematik 5–12 tek ders ve tek haritadır. Ana tema, mikro kazanımın içerik alanıdır; TYMM'deki tema adı farklı olsa da içerik aynı alandaysa aynı kod kullanılır (lisedeki "Sayılar" → 01, "Nicelikler ve Değişimler" → 02, "Geometrik Cisimler" → 04, "Hazır Veriler Üzerinde Çalışma" → 06). Yeni bir içerik alanı çıkarsa numara sıradakinden devam eder (08–11 lisede eklendi; sıradaki yeni alan 12 olur).

## Sınıf ünitesi kodu

`<Ders><2 haneli sınıf>-U<ünite no>` (ör. `Fiz10-U3`) ya da temalı derslerde `-T<tema no>` (ör. `Mat08-T1`). Bu kod yalnızca sınıf programındaki yeri gösterir, mikro kazanım koduna girmez. Tam liste: `Ünite Kodları.xlsx`.

## TYMM öğrenme çıktısı kodları

`FİZ.10.3.4` gibi resmi kodlar değiştirilmeden eşleme sayfasında tutulur.

## İlişki haritası ve adaptif test veri modeli

Her ders için mikro kazanımlar **yönlü ve döngüsüz bir ön koşul grafiği** oluşturur (beyindeki bağlantılar gibi). Grafik sınıftan bağımsızdır: yeni sınıflar eklendikçe aynı ağa yeni düğümler ve oklar eklenir, var olan düğümler yeniden yazılmaz.

- **Düğüm:** bir mikro kazanım (kod, ana ünite, tür, bilişsel düzey, işlem türü, zorluk, seviye, yanılgılar, eşlendiği öğrenme çıktıları).
- **Ok:** `on_kosul_kodlari` sütunundaki her kod, o kazanımdan bu kazanıma bir ok demektir (A → B: B'yi öğrenmek için A gerekir). Sınıf ya da ünite sınırı tanımaz.
- **Derinlik:** kazanımın altındaki en uzun ön koşul zinciri (0 = kök; ön koşulu grafikte yok).
- **Etki:** bu kazanıma doğrudan ya da dolaylı dayanan kazanım sayısı. Etkisi yüksek bir kazanımdaki eksik çok sayıda kazanımı etkiler.
- **Kurallar:** grafikte döngü olamaz; her kazanımın ya ön koşul kodu ya da `on_kosul_diger` açıklaması olmalı; kopuk düğüm (ne ön koşulu ne ardılı olan) olmamalı. `araclar/harita_uret.py` bunları her çalıştırmada denetler ve `<Ders> Harita Denetimi.md` raporunu yazar.

Üretilen dosyalar (her ders klasöründe):
- `<Ders> Mikro Kazanım Haritası.html`: tarayıcıda açılan, internet gerektirmeyen etkileşimli harita.
- `veri/<ders>_graf.json`: adaptif test motorunun okuyacağı grafik (düğümler ön koşul sırasında, derinlik, etki, zorluk ve seviyeyle).

**Adaptif testte kullanım (taslak algoritma):**
1. Öğrenci hedef kazanımdan (ör. bir öğrenme çıktısının en derin mikro kazanımı) başlar.
2. Doğru yanıt: kazanım "hâkim" sayılır ve ölçütüne göre (3 maddeden 2'si) doğrulanır; test ardıllara (daha derin kazanımlara) ilerler.
3. Yanlış yanıt: seçilen çeldiricinin yanılgı kodu kaydedilir; test doğrudan ön koşullara iner. Birden fazla ön koşul varsa önce etkisi en yüksek olan denenir.
4. Geriye iniş, öğrencinin yapabildiği bir ön koşula ulaşılınca durur. Yapabildiği son halka ile yapamadığı ilk halka arasındaki kazanım **eksik kök** olarak raporlanır; öğretim oradan başlatılır.
5. Hâkim olunduğu gösterilen bir kazanımın tüm ön koşulları da hâkim sayılır (tekrar sorulmaz), böylece test kısa kalır.

## Güncelleme akışı

1. İlgili dersin `veri/` klasöründeki CSV dosyasını düzenle (ör. `Fizik/veri/`, `Matematik/veri/`). CSV'ler tek doğruluk kaynağıdır.
2. EVALORA klasöründe `python3 araclar/excel_uret.py` çalıştır; tüm derslerin Mikro Kazanım Excel'leri, kökteki `Ünite Kodları.xlsx`, ilişki haritaları, denetim raporları ve graf JSON'ları yeniden üretilir. Denetim raporunda sorun varsa CSV'de düzeltilir.
3. `ortak/degisiklik_gunlugu.csv` ve README'deki Yapılanlar bölümüne satır ekle.
