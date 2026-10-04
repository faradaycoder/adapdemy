"""11. sınıf fizik açık uçlu sınav: Newton'un hareket yasaları ve sürtünme (FİZ.11.1.4–11.1.7).

Claude, 2026-10-04. Bu dosya sınavın tek kaynağıdır: sorular, çözümler ve rubrik adımları (adım → MK) burada.
uret.py bu veriden sınav PDF'ini, rubrik PDF'ini, soru görsellerini ve sistemin demo tanıma kaydını üretir.
Alt şıklar (a, b, c) ayrı soru değildir; rubrik adımlarında ayrılır.
"""

BASLIK = "11. Sınıf Fizik · Newton'un Hareket Yasaları ve Sürtünme"
ALT_BASLIK = "Açık uçlu yazılı sınav · 5 soru · 40 dakika"
YONERGE = ("Her sorunun çözümünü adım adım yaz; yalnız sonuç yazan cevaplar tam puan alamaz. "
           "Gerekli yerlerde g = 10 m/s² al. Şekil çizmen istenen yerde kuvvetleri okla ve adıyla göster.")

# Şekiller (SVG): soru 2 ve 4
SEKIL_KUTU = """
<svg viewBox="0 0 420 150" width="420" height="150" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial" font-size="16">
  <line x1="10" y1="120" x2="410" y2="120" stroke="#222" stroke-width="2"/>
  <g stroke="#888" stroke-width="1.2">
    <line x1="20" y1="120" x2="10" y2="132"/><line x1="50" y1="120" x2="40" y2="132"/><line x1="80" y1="120" x2="70" y2="132"/>
    <line x1="110" y1="120" x2="100" y2="132"/><line x1="140" y1="120" x2="130" y2="132"/><line x1="170" y1="120" x2="160" y2="132"/>
    <line x1="200" y1="120" x2="190" y2="132"/><line x1="230" y1="120" x2="220" y2="132"/><line x1="260" y1="120" x2="250" y2="132"/>
    <line x1="290" y1="120" x2="280" y2="132"/><line x1="320" y1="120" x2="310" y2="132"/><line x1="350" y1="120" x2="340" y2="132"/>
    <line x1="380" y1="120" x2="370" y2="132"/><line x1="410" y1="120" x2="400" y2="132"/>
  </g>
  <rect x="140" y="60" width="90" height="60" fill="#e8eef6" stroke="#1f3a5f" stroke-width="2"/>
  <text x="168" y="96">2 kg</text>
  <line x1="230" y1="90" x2="330" y2="90" stroke="#b42318" stroke-width="3"/>
  <polygon points="330,82 346,90 330,98" fill="#b42318"/>
  <text x="275" y="78">F = 20 N</text>
  <text x="20" y="108">k = 0,4</text>
</svg>"""

SEKIL_MAKARA = """
<svg viewBox="0 0 420 230" width="420" height="230" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial" font-size="16">
  <rect x="20" y="100" width="300" height="14" fill="#d0d5dd" stroke="#222" stroke-width="1.5"/>
  <line x1="40" y1="114" x2="40" y2="220" stroke="#222" stroke-width="3"/>
  <line x1="300" y1="114" x2="300" y2="220" stroke="#222" stroke-width="3"/>
  <rect x="90" y="50" width="80" height="50" fill="#e8eef6" stroke="#1f3a5f" stroke-width="2"/>
  <text x="105" y="81">A 3 kg</text>
  <line x1="170" y1="72" x2="334" y2="72" stroke="#222" stroke-width="1.6"/>
  <line x1="320" y1="100" x2="332" y2="86" stroke="#222" stroke-width="2"/>
  <circle cx="338" cy="86" r="14" fill="#fff" stroke="#222" stroke-width="2"/>
  <circle cx="338" cy="86" r="2.5" fill="#222"/>
  <line x1="352" y1="86" x2="352" y2="150" stroke="#222" stroke-width="1.6"/>
  <rect x="322" y="150" width="60" height="50" fill="#fef0c7" stroke="#93370d" stroke-width="2"/>
  <text x="330" y="181">B 2 kg</text>
  <text x="40" y="40">Sürtünmesiz yatay masa</text>
</svg>"""

SORULAR = [
    {
        "no": 1,
        "anahtar": "f11_etki_tepki",
        "baslik": "Etki-tepki: kamyon ile otomobil",
        "metin": "Dolu bir kamyon ile küçük bir otomobil düz bir yolda kafa kafaya çarpışıyor. Ali, \"Kamyon çok daha "
                 "ağır olduğu için otomobile, otomobilin kamyona uyguladığından daha büyük kuvvet uygular.\" diyor.\n"
                 "a) Ali'nin görüşü doğru mudur? Çarpışma sırasında araçların birbirine uyguladığı kuvvetleri büyüklük "
                 "ve yön bakımından karşılaştırarak açıklayınız.\n"
                 "b) Bu iki kuvvet birbirini dengeler mi? Gerekçesiyle açıklayınız.\n"
                 "c) Çarpışma sırasında hangi araç daha büyük ivme kazanır? Nedenini açıklayınız.",
        "sekil": None,
        "dogru_cevap": "a) Hayır; kuvvetler eşit büyüklükte ve zıt yönlüdür. b) Dengelemez; farklı cisimlere etki ederler. "
                       "c) Otomobil; kütlesi küçük olduğu için aynı kuvvetle daha büyük ivme kazanır.",
        "cozum": "a) Kamyonun otomobile uyguladığı kuvvet ile otomobilin kamyona uyguladığı kuvvet etki-tepki çiftidir. "
                 "Newton'un üçüncü yasasına göre bu kuvvetler kütleden bağımsız olarak eşit büyüklüktedir; Ali'nin görüşü "
                 "yanlıştır. Kuvvetler zıt yönlüdür. b) Etki-tepki kuvvetleri farklı cisimlere (biri otomobile, biri kamyona) "
                 "etki ettiği için birbirini dengelemez. c) a = F / m; kuvvetler eşit, otomobilin kütlesi küçük olduğundan "
                 "otomobilin ivmesi daha büyüktür, sürücüsü daha çok sarsılır.",
        "adimlar": [
            ("a) Etki-tepki kuvvetlerinin kütleden bağımsız olarak eşit büyüklükte olduğunu belirtir; Ali'nin yanıldığını söyler.", "Fiz02MK0111"),
            ("a) Kuvvetlerin zıt yönlü olduğunu belirtir.", "Fiz02MK0112"),
            ("b) Kuvvetlerin farklı cisimlere etki ettiği için birbirini dengelemediğini açıklar.", "Fiz02MK0113"),
            ("c) Eşit kuvvet altında kütlesi küçük olan otomobilin ivmesinin daha büyük olduğunu (a = F / m) açıklar.", "Fiz02MK0110"),
        ],
    },
    {
        "no": 2,
        "anahtar": "f11_surtunmeli_kutu",
        "baslik": "Sürtünmeli yatay zeminde çekilen kutu",
        "metin": "Kütlesi 2 kg olan bir kutu, sürtünme katsayısı k = 0,4 olan yatay zeminde 20 N büyüklüğündeki yatay "
                 "F kuvvetiyle şekildeki gibi çekiliyor. (g = 10 m/s²)\n"
                 "a) Kutuya etki eden bütün kuvvetleri serbest cisim diyagramı üzerinde gösteriniz.\n"
                 "b) Kutuya etki eden sürtünme kuvvetinin büyüklüğünü hesaplayınız.\n"
                 "c) Kutunun ivmesini hesaplayınız.",
        "sekil": SEKIL_KUTU,
        "dogru_cevap": "b) Fs = 8 N  c) a = 6 m/s² (F yönünde)",
        "cozum": "a) Kutuya dört kuvvet etki eder: aşağı yönde ağırlık G = 20 N, yukarı yönde zeminin tepki kuvveti N, "
                 "sağa F = 20 N ve F'ye zıt yönde (sola) sürtünme kuvveti Fs. b) Düşeyde denge vardır: N = G = m·g = 20 N. "
                 "Fs = k·N = 0,4 · 20 = 8 N. c) Fnet = F − Fs = 20 − 8 = 12 N. a = Fnet / m = 12 / 2 = 6 m/s², F yönünde.",
        "adimlar": [
            ("a) Ağırlık, tepki, F ve sürtünme kuvvetini serbest cisim diyagramında doğru yönleriyle gösterir.", "Fiz02MK0121"),
            ("a) Sürtünme kuvvetini harekete (F'ye) zıt yönde çizer.", "Fiz02MK0119"),
            ("b) N = m·g = 20 N bulup Fs = k·N = 0,4 · 20 = 8 N hesaplar.", "Fiz02MK0139"),
            ("c) Net kuvveti Fnet = 20 − 8 = 12 N bulur.", "Fiz02MK0125"),
            ("c) İvmeyi a = Fnet / m = 12 / 2 = 6 m/s² hesaplar.", "Fiz02MK0140"),
        ],
    },
    {
        "no": 3,
        "anahtar": "f11_statik_kinetik",
        "baslik": "Statik ve kinetik sürtünme deneyi",
        "metin": "Yatay masa üzerinde duran 5 kg kütleli bir bloğa yatay bir F kuvveti uygulanıyor ve F sıfırdan başlayarak "
                 "yavaşça artırılıyor. Blok, F = 15 N olduğu anda harekete başlıyor. Blok kayarken ölçülen sürtünme kuvveti "
                 "10 N'dur. (g = 10 m/s²)\n"
                 "a) F = 8 N iken blok hareket etmiyor. Bu anda bloğa etki eden sürtünme kuvvetinin türü ve büyüklüğü nedir? "
                 "Yönünü belirtiniz.\n"
                 "b) Statik sürtünme kuvvetinin en büyük değeri ile kinetik sürtünme kuvvetini büyüklük bakımından karşılaştırınız.\n"
                 "c) F, 0'dan 20 N'a kadar artırılırken sürtünme kuvveti–uygulanan kuvvet grafiğini çiziniz ve statik "
                 "sürtünmenin en büyük değerini grafik üzerinde işaretleyiniz.\n"
                 "d) Statik ve kinetik sürtünme katsayılarını hesaplayınız.",
        "sekil": None,
        "dogru_cevap": "a) Statik sürtünme, 8 N, F'ye zıt yönde  b) Statik en büyük (15 N) > kinetik (10 N)  "
                       "d) ks = 0,3, kk = 0,2",
        "cozum": "a) Blok durgun olduğundan sürtünme statiktir ve uygulanan kuvveti dengeler: Fs = 8 N, F'ye zıt yönde. "
                 "b) Statik sürtünmenin en büyük değeri 15 N, kinetik sürtünme 10 N'dur; statik sürtünmenin en büyük değeri "
                 "kinetik sürtünmeden büyüktür. c) Grafik: F = 0'dan 15 N'a kadar Fs = F (orijinden geçen eğimli doğru), "
                 "F = 15 N'da tepe (statik sürtünmenin en büyük değeri, 15 N), harekete geçtikten sonra Fs = 10 N sabit "
                 "(yatay doğru). d) N = m·g = 50 N. ks = 15 / 50 = 0,3; kk = 10 / 50 = 0,2.",
        "adimlar": [
            ("a) Durgun blokta sürtünmenin statik olduğunu, 8 N büyüklüğünde ve F'ye zıt yönde olduğunu belirtir.", "Fiz02MK0129"),
            ("b) Statik sürtünmenin en büyük değerinin (15 N) kinetik sürtünmeden (10 N) büyük olduğunu karşılaştırır.", "Fiz02MK0131"),
            ("c) Grafiği çizer: 0–15 N arasında Fs = F, sonra 10 N'da sabit.", "Fiz02MK0135"),
            ("c) Statik sürtünmenin en büyük değerini (15 N) grafikte işaretler.", "Fiz02MK0136"),
            ("d) N = 50 N alarak ks = 15 / 50 = 0,3 ve kk = 10 / 50 = 0,2 hesaplar.", "Fiz02MK0139"),
        ],
    },
    {
        "no": 4,
        "anahtar": "f11_makarali_sistem",
        "baslik": "Makaralı sistemde ivme ve ip gerilmesi",
        "metin": "Şekildeki sistemde 3 kg kütleli A bloğu sürtünmesiz yatay masa üzerindedir ve kütlesi önemsiz bir makaradan "
                 "geçen hafif bir iple 2 kg kütleli B bloğuna bağlıdır. Sistem serbest bırakılıyor. (g = 10 m/s²)\n"
                 "a) A ve B bloklarına etki eden kuvvetleri ayrı ayrı serbest cisim diyagramlarında gösteriniz.\n"
                 "b) Sistemi hareket ettiren net kuvveti bulunuz.\n"
                 "c) Sistemin ivmesini hesaplayınız.\n"
                 "d) İpteki gerilme kuvvetini hesaplayınız.",
        "sekil": SEKIL_MAKARA,
        "dogru_cevap": "b) 20 N  c) a = 4 m/s²  d) T = 12 N",
        "cozum": "a) A: aşağı ağırlık (30 N), yukarı tepki kuvveti (30 N), makaraya doğru ip gerilmesi T. B: aşağı ağırlık "
                 "(20 N), yukarı ip gerilmesi T. b) A'nın ağırlığı tepki kuvvetiyle dengelenir; sistemi hareket ettiren net "
                 "kuvvet B'nin ağırlığıdır: Fnet = mB·g = 20 N. c) a = Fnet / (mA + mB) = 20 / 5 = 4 m/s². d) A için: T = mA·a "
                 "= 3 · 4 = 12 N. (Kontrol, B için: mB·g − T = mB·a ⇒ 20 − T = 8 ⇒ T = 12 N.)",
        "adimlar": [
            ("a) A için ağırlık, tepki ve ip gerilmesini; B için ağırlık ve ip gerilmesini serbest cisim diyagramlarında gösterir.", "Fiz02MK0121"),
            ("a) İp gerilmesini her iki blokta da ip boyunca, bloktan dışarı doğru gösterir.", "Fiz02MK0118"),
            ("b) Sistemi hareket ettiren net kuvveti Fnet = mB·g = 20 N bulur.", "Fiz02MK0125"),
            ("c) Ortak ivmeyi a = 20 / (3 + 2) = 4 m/s² hesaplar.", "Fiz02MK0127"),
            ("d) İp gerilmesini T = mA·a = 12 N hesaplar (ya da B için 20 − T = 2 · 4).", "Fiz02MK0128"),
        ],
    },
    {
        "no": 5,
        "anahtar": "f11_surtunme_yonu",
        "baslik": "Yürürken ve bisiklette sürtünmenin yönü; eylemsizlik",
        "metin": "a) Düz bir yolda yürürken yerin ayağımıza uyguladığı sürtünme kuvvetinin yönü nedir? Yürüyebilmemizi bu "
                 "kuvvetle ilişkilendirerek açıklayınız.\n"
                 "b) Pedal çevrilerek hızlanan bir bisikletin arka tekerleğine yerden etki eden sürtünme kuvvetinin yönü "
                 "nedir? Açıklayınız.\n"
                 "c) Uzay boşluğunda hareket eden bir aracın motorları kapatılıyor. Araca hiçbir kuvvet etki etmediğine göre "
                 "araç nasıl hareket eder? Bir arkadaşınız \"Motor kapanınca araç yavaşlayıp durur.\" diyor; bu görüşü "
                 "değerlendiriniz.",
        "sekil": None,
        "dogru_cevap": "a) İleri (hareket yönünde)  b) İleri (hareket yönünde)  c) Sabit hızla doğrusal hareketine devam eder; "
                       "arkadaşın görüşü yanlıştır.",
        "cozum": "a) Yürürken ayağımız yeri geriye doğru iter; yer de ayağımıza ileri yönde statik sürtünme kuvveti uygular. "
                 "Bizi ileri götüren bu kuvvettir; buzda yürüyemememizin nedeni sürtünmenin az olmasıdır. b) Pedalla döndürülen "
                 "arka tekerlek yeri geriye iter; yer, tekerleğe ileri yönde sürtünme kuvveti uygular ve bisikleti hızlandırır. "
                 "c) Net kuvvet sıfır olduğundan araç sabit hızla doğrusal hareketine devam eder (Newton'un birinci yasası). "
                 "Hareketin sürmesi için kuvvet gerekmez; yavaşlaması için bir kuvvet gerekir. Arkadaşın görüşü yanlıştır.",
        "adimlar": [
            ("a) Yürürken yerin ayağa uyguladığı sürtünmenin ileri yönde olduğunu ve bizi ileri götürdüğünü açıklar.", "Fiz02MK0138"),
            ("b) Hızlanan bisikletin arka tekerleğine etki eden sürtünmenin ileri yönde olduğunu açıklar.", "Fiz02MK0138"),
            ("c) Net kuvvet sıfırken aracın sabit hızla doğrusal hareketine devam ettiğini belirtir; arkadaşın görüşünü çürütür.", "Fiz02MK0108"),
        ],
    },
]
