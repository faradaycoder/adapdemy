"""Demo modundaki örnek sorular ve analizleri.

API anahtarı yokken yapay zekâ katmanı bu hazır analizleri döndürür. Analizler 2026-10-03'te Murat ile
konuşmada yapılan çözümlemelerdir (fizik) ve pilot kapsamı için hazırlanmış matematik sorularıdır.
Her analiz: soru metni, cevap biçimi, şıklar, doğru cevap, çözüm, birincil MK ve rubrik adımları (adım → MK).
Sorunun MK'leri, zorluğu ve rubrik payları burada yazılmaz; eslestirme.py kurallarla hesaplar.
"""

ORNEKLER = [
    {
        "anahtar": "egik_atis",
        "baslik": "Eğik atış ve duvara esnek çarpma",
        "ders": "Fizik", "sinif_duzeyi": 11, "gorsel": "egik_atis.png",
        "metin": "Sürtünmelerin önemsenmediği ortamda şekildeki gibi eğik atış hareketi yapan bir cisim, X noktasında "
                 "duvara esnek çarparak Y noktasına düşüyor. Z noktası cismin çıkabileceği maksimum yükseklik olduğuna "
                 "göre, h₁ / h_max oranı kaçtır? (Z'nin izdüşümü ile Y arası a, Y ile duvar arası a.)",
        "cevap_bicimi": "coktan_secmeli",
        "secenekler": [("A", "1/3", False), ("B", "1/2", False), ("C", "5/9", True), ("D", "7/9", False), ("E", "8/9", False)],
        "dogru_cevap": "C",
        "cozum": "Duvar yalnız yatay hızın yönünü değiştirir; düşey hareket Z'den yere kadar ilk hızı sıfır serbest "
                 "düşmedir. Yatay hız sabit olduğundan Z'den X'e (2a) 2t, X'ten Y'ye (a) t sürer; düşüş toplam 3t. "
                 "h ∝ t² olduğundan h_max ∝ 9, X'e kadar düşülen ∝ 4, h₁ ∝ 5; h₁ / h_max = 5/9.",
        "birincil": "Fiz02MK0099",
        "adimlar": [
            ("Z tepe noktasıdır; düşey hız sıfırdır ve Z'den sonrası düşeyde serbest düşmedir.", "Fiz02MK0098"),
            ("Yatay hız sabit olduğundan eşit yatay yollar eşit sürede alınır: Z→X 2t, X→Y t.", "Fiz02MK0097"),
            ("Duvar yalnız yatay hızı ters çevirir, düşey hareket bağımsız sürer: Z'den yere düşüş 3t.", "Fiz02MK0099"),
            ("h = ½gt² ile h_max ∝ 9, X'e kadar düşülen ∝ 4; h₁ / h_max = 5/9.", "Fiz02MK0095"),
        ],
    },
    {
        "anahtar": "surtunmeli_yol",
        "baslik": "Sürtünmeli yolda gidiş-dönüş",
        "ders": "Fizik", "sinif_duzeyi": 12, "gorsel": "surtunmeli_yol.png",
        "metin": "Kütlesi 2 kg olan cisim 5 m yükseklikteki K noktasından v hızıyla atılıyor, 8 m yükseklikteki L'ye "
                 "kadar çıkıp dönüşte M'de duruyor. Yalnız M–N arası sürtünmelidir. v kaç m/s'dir? (g = 10 m/s²)",
        "cevap_bicimi": "yazili",
        "secenekler": [],
        "dogru_cevap": "v = √220 ≈ 14,8 m/s",
        "cozum": "Dönüş: mg·8 − W = 0 ⇒ W = 160 J (M–N'de sürtünmeye giden enerji, her geçişte aynı). "
                 "Gidiş: ½mv² + mg·5 − W = mg·8 ⇒ v² + 100 − 160 = 160 ⇒ v² = 220, v ≈ 14,8 m/s.",
        "birincil": "Fiz04MK0133",
        "adimlar": [
            ("Dönüşte L'deki potansiyel enerjinin tamamı M–N'de ısıya gider: W = mg·8 = 160 J.", "Fiz04MK0129"),
            ("K'deki potansiyel enerji: Ep = mgh = 100 J.", "Fiz04MK0096"),
            ("K'deki kinetik enerji ½mv² olarak yazılır.", "Fiz04MK0095"),
            ("Sürtünmeli ortamda toplam enerji korunur; kayıp ısıya dönüşür.", "Fiz04MK0098"),
            ("Gidiş için enerji denklemi kurulur ve v bulunur: v² = 220.", "Fiz04MK0133"),
        ],
    },
    {
        "anahtar": "yay",
        "baslik": "Eğik düzlem, sürtünmeli yol ve yay",
        "ders": "Fizik", "sinif_duzeyi": 12, "gorsel": "yay.png",
        "metin": "Kütlesi 2 kg olan cisim K noktasından (h = 5 m) serbest bırakılıyor. K–L sürtünmesiz; 5 m uzunluğundaki "
                 "L–M yatay düzlemi sürtünmelidir (sürtünme katsayısı 0,4). M'den sonra yay sabiti 200 N/m olan yay vardır. "
                 "Cisim yayı en fazla kaç cm sıkıştırır? (g = 10 m/s²)",
        "cevap_bicimi": "yazili",
        "secenekler": [],
        "dogru_cevap": "x ≈ 77,5 cm",
        "cozum": "mgh = 100 J. Fs = 0,4·20 = 8 N, L–M'de iş 8·5 = 40 J. M'de Ek = 60 J. ½·200·x² = 60 ⇒ x² = 0,6, x ≈ 0,775 m.",
        "birincil": "Fiz04MK0133",
        "adimlar": [
            ("K'deki potansiyel enerji: mgh = 100 J.", "Fiz04MK0096"),
            ("Sürtünme kuvveti: Fs = k·N = 0,4·20 = 8 N.", "Fiz02MK0139"),
            ("Sürtünmenin işi (ısıya giden enerji): 8·5 = 40 J.", "Fiz04MK0129"),
            ("Yayda depolanan enerji: ½kx² = 60 J ⇒ x ≈ 77,5 cm.", "Fiz04MK0124"),
            ("Enerjilerin ve sürtünme işinin tek korunum zincirinde birleştirilmesi.", "Fiz04MK0133"),
        ],
    },
    {
        "anahtar": "uc_cisim",
        "baslik": "Sürtünmeli düzlemde duran üç cisim",
        "ders": "Fizik", "sinif_duzeyi": 12, "gorsel": "uc_cisim.png",
        "metin": "Sürtünmeli yatay düzlemdeki özdeş üç cisim eşit hızlarla fırlatılınca farklı yollar (x₁, x₂, x₃) alarak "
                 "duruyorlar. Cisimler duruncaya kadar I. ivmelerinin büyüklüğü, II. kaybettikleri mekanik enerji, "
                 "III. hareket süreleri niceliklerinden hangileri eşittir?",
        "cevap_bicimi": "kisa_cevap",
        "secenekler": [],
        "dogru_cevap": "Yalnız II",
        "cozum": "III: x = (v/2)·t ⇒ t = 2x/v, yollar farklı ⇒ süreler farklı. I: a = v/t, süreler farklı ⇒ ivmeler farklı. "
                 "II: kaybedilen mekanik enerji ½mv², hepsinde eşit.",
        "birincil": "Fiz04MK0097",
        "adimlar": [
            ("x = (v/2)·t ilişkisini kurar; yollar farklı olduğundan süreler farklı.", "Fiz02MK0059"),
            ("a = v / t ile ivmeleri karşılaştırır; süreler farklı olduğundan ivmeler farklı.", "Fiz02MK0064"),
            ("Kaybedilen enerjiyi ilk kinetik enerji (½mv²) olarak bulur.", "Fiz04MK0095"),
            ("Kaybolan mekanik enerji sürtünmeyle ısıya gider ve yoldan bağımsızdır; eşittir.", "Fiz04MK0097"),
        ],
    },
    {
        "anahtar": "pisagor_hipotenus",
        "baslik": "Dik üçgende hipotenüs",
        "ders": "Matematik", "sinif_duzeyi": 8, "gorsel": None,
        "metin": "Dik kenarları 9 cm ve 12 cm olan bir dik üçgenin hipotenüsü kaç cm'dir?",
        "cevap_bicimi": "coktan_secmeli",
        "secenekler": [("A", "13", False), ("B", "15", True), ("C", "18", False), ("D", "21", False)],
        "dogru_cevap": "B",
        "cozum": "Hipotenüs dik açının karşısındaki kenardır. c² = 9² + 12² = 81 + 144 = 225, c = √225 = 15 cm. "
                 "(21, dik kenarları toplamaktan gelen çeldiricidir.)",
        "birincil": "Mat03MK0143",
        "adimlar": [
            ("Hipotenüsün dik açının karşısındaki kenar olduğunu belirler.", "Mat03MK0141"),
            ("Pisagor bağıntısını kurar: c² = 81 + 144 = 225.", "Mat03MK0143"),
            ("Tam kare sayının karekökünü bulur: c = 15.", "Mat01MK0213"),
        ],
    },
    {
        "anahtar": "pisagor_ucgen_turu",
        "baslik": "Kenarlarından üçgenin türü",
        "ders": "Matematik", "sinif_duzeyi": 8, "gorsel": None,
        "metin": "Kenar uzunlukları 7 cm, 24 cm ve 25 cm olan bir üçgen dar açılı mı, dik mi, geniş açılı mı? Gerekçesiyle yazınız.",
        "cevap_bicimi": "yazili",
        "secenekler": [],
        "dogru_cevap": "Dik üçgen",
        "cozum": "En uzun kenar 25. 7² + 24² = 49 + 576 = 625 = 25². c² = a² + b² olduğundan 25 cm'lik kenarın karşısındaki açı diktir.",
        "birincil": "Mat03MK0144",
        "adimlar": [
            ("Kenarların karelerini hesaplar: 49, 576, 625.", "Mat01MK0176"),
            ("c² = a² + b² olduğunu görür ve üçgenin dik olduğunu açı–kenar ilişkisiyle açıklar.", "Mat03MK0144"),
        ],
    },
    {
        "anahtar": "temel_oranti",
        "baslik": "Temel orantı teoremi",
        "ders": "Matematik", "sinif_duzeyi": 9, "gorsel": None,
        "metin": "ABC üçgeninde DE ∥ BC, D noktası [AB], E noktası [AC] üzerindedir. |AD| = 4 cm, |DB| = 6 cm, |AE| = 6 cm ise |EC| kaç cm'dir?",
        "cevap_bicimi": "kisa_cevap",
        "secenekler": [],
        "dogru_cevap": "9 cm",
        "cozum": "DE ∥ BC olduğundan AD / DB = AE / EC. 4 / 6 = 6 / EC, içler-dışlar çarpımıyla EC = 36 / 4 = 9 cm.",
        "birincil": "Mat08MK0011",
        "adimlar": [
            ("DE ∥ BC'den temel orantıyı kurar: AD / DB = AE / EC.", "Mat08MK0011"),
            ("Orantıda bilinmeyeni içler-dışlar çarpımıyla bulur: EC = 9.", "Mat01MK0167"),
        ],
    },
]

# 11. sınıf açık uçlu sınav (Claude, 2026-10-04): Newton'un hareket yasaları ve sürtünme. Kaynak ve PDF'ler:
# uygulama/ornek_dosyalar/fizik11_newton/ (sinav.py tek kaynak; soru görselleri soruN.png ile aynı).
ORNEKLER += [{'anahtar': 'f11_etki_tepki',
  'baslik': '11. sınıf Newton ve sürtünme: Etki-tepki: kamyon ile otomobil',
  'ders': 'Fizik',
  'sinif_duzeyi': 11,
  'gorsel': 'f11_etki_tepki.png',
  'metin': 'Dolu bir kamyon ile küçük bir otomobil düz bir yolda kafa kafaya çarpışıyor. Ali, "Kamyon çok daha ağır '
           'olduğu için otomobile, otomobilin kamyona uyguladığından daha büyük kuvvet uygular." diyor.\n'
           "a) Ali'nin görüşü doğru mudur? Çarpışma sırasında araçların birbirine uyguladığı kuvvetleri büyüklük ve "
           'yön bakımından karşılaştırarak açıklayınız.\n'
           'b) Bu iki kuvvet birbirini dengeler mi? Gerekçesiyle açıklayınız.\n'
           'c) Çarpışma sırasında hangi araç daha büyük ivme kazanır? Nedenini açıklayınız.',
  'cevap_bicimi': 'yazili',
  'secenekler': [],
  'dogru_cevap': 'a) Hayır; kuvvetler eşit büyüklükte ve zıt yönlüdür. b) Dengelemez; farklı cisimlere etki ederler. '
                 'c) Otomobil; kütlesi küçük olduğu için aynı kuvvetle daha büyük ivme kazanır.',
  'cozum': 'a) Kamyonun otomobile uyguladığı kuvvet ile otomobilin kamyona uyguladığı kuvvet etki-tepki çiftidir. '
           "Newton'un üçüncü yasasına göre bu kuvvetler kütleden bağımsız olarak eşit büyüklüktedir; Ali'nin görüşü "
           'yanlıştır. Kuvvetler zıt yönlüdür. b) Etki-tepki kuvvetleri farklı cisimlere (biri otomobile, biri '
           'kamyona) etki ettiği için birbirini dengelemez. c) a = F / m; kuvvetler eşit, otomobilin kütlesi küçük '
           'olduğundan otomobilin ivmesi daha büyüktür, sürücüsü daha çok sarsılır.',
  'birincil': 'Fiz02MK0110',
  'adimlar': [("a) Etki-tepki kuvvetlerinin kütleden bağımsız olarak eşit büyüklükte olduğunu belirtir; Ali'nin "
               'yanıldığını söyler.',
               'Fiz02MK0111'),
              ('a) Kuvvetlerin zıt yönlü olduğunu belirtir.', 'Fiz02MK0112'),
              ('b) Kuvvetlerin farklı cisimlere etki ettiği için birbirini dengelemediğini açıklar.', 'Fiz02MK0113'),
              ('c) Eşit kuvvet altında kütlesi küçük olan otomobilin ivmesinin daha büyük olduğunu (a = F / m) '
               'açıklar.',
               'Fiz02MK0110')]},
 {'anahtar': 'f11_surtunmeli_kutu',
  'baslik': '11. sınıf Newton ve sürtünme: Sürtünmeli yatay zeminde çekilen kutu',
  'ders': 'Fizik',
  'sinif_duzeyi': 11,
  'gorsel': 'f11_surtunmeli_kutu.png',
  'metin': 'Kütlesi 2 kg olan bir kutu, sürtünme katsayısı k = 0,4 olan yatay zeminde 20 N büyüklüğündeki yatay F '
           'kuvvetiyle şekildeki gibi çekiliyor. (g = 10 m/s²)\n'
           'a) Kutuya etki eden bütün kuvvetleri serbest cisim diyagramı üzerinde gösteriniz.\n'
           'b) Kutuya etki eden sürtünme kuvvetinin büyüklüğünü hesaplayınız.\n'
           'c) Kutunun ivmesini hesaplayınız.',
  'cevap_bicimi': 'yazili',
  'secenekler': [],
  'dogru_cevap': 'b) Fs = 8 N  c) a = 6 m/s² (F yönünde)',
  'cozum': 'a) Kutuya dört kuvvet etki eder: aşağı yönde ağırlık G = 20 N, yukarı yönde zeminin tepki kuvveti N, sağa '
           "F = 20 N ve F'ye zıt yönde (sola) sürtünme kuvveti Fs. b) Düşeyde denge vardır: N = G = m·g = 20 N. Fs = "
           'k·N = 0,4 · 20 = 8 N. c) Fnet = F − Fs = 20 − 8 = 12 N. a = Fnet / m = 12 / 2 = 6 m/s², F yönünde.',
  'birincil': 'Fiz02MK0140',
  'adimlar': [('a) Ağırlık, tepki, F ve sürtünme kuvvetini serbest cisim diyagramında doğru yönleriyle gösterir.',
               'Fiz02MK0121'),
              ("a) Sürtünme kuvvetini harekete (F'ye) zıt yönde çizer.", 'Fiz02MK0119'),
              ('b) N = m·g = 20 N bulup Fs = k·N = 0,4 · 20 = 8 N hesaplar.', 'Fiz02MK0139'),
              ('c) Net kuvveti Fnet = 20 − 8 = 12 N bulur.', 'Fiz02MK0125'),
              ('c) İvmeyi a = Fnet / m = 12 / 2 = 6 m/s² hesaplar.', 'Fiz02MK0140')]},
 {'anahtar': 'f11_statik_kinetik',
  'baslik': '11. sınıf Newton ve sürtünme: Statik ve kinetik sürtünme deneyi',
  'ders': 'Fizik',
  'sinif_duzeyi': 11,
  'gorsel': 'f11_statik_kinetik.png',
  'metin': 'Yatay masa üzerinde duran 5 kg kütleli bir bloğa yatay bir F kuvveti uygulanıyor ve F sıfırdan başlayarak '
           'yavaşça artırılıyor. Blok, F = 15 N olduğu anda harekete başlıyor. Blok kayarken ölçülen sürtünme kuvveti '
           "10 N'dur. (g = 10 m/s²)\n"
           'a) F = 8 N iken blok hareket etmiyor. Bu anda bloğa etki eden sürtünme kuvvetinin türü ve büyüklüğü nedir? '
           'Yönünü belirtiniz.\n'
           'b) Statik sürtünme kuvvetinin en büyük değeri ile kinetik sürtünme kuvvetini büyüklük bakımından '
           'karşılaştırınız.\n'
           "c) F, 0'dan 20 N'a kadar artırılırken sürtünme kuvveti–uygulanan kuvvet grafiğini çiziniz ve statik "
           'sürtünmenin en büyük değerini grafik üzerinde işaretleyiniz.\n'
           'd) Statik ve kinetik sürtünme katsayılarını hesaplayınız.',
  'cevap_bicimi': 'yazili',
  'secenekler': [],
  'dogru_cevap': "a) Statik sürtünme, 8 N, F'ye zıt yönde  b) Statik en büyük (15 N) > kinetik (10 N)  d) ks = 0,3, kk "
                 '= 0,2',
  'cozum': "a) Blok durgun olduğundan sürtünme statiktir ve uygulanan kuvveti dengeler: Fs = 8 N, F'ye zıt yönde. b) "
           "Statik sürtünmenin en büyük değeri 15 N, kinetik sürtünme 10 N'dur; statik sürtünmenin en büyük değeri "
           "kinetik sürtünmeden büyüktür. c) Grafik: F = 0'dan 15 N'a kadar Fs = F (orijinden geçen eğimli doğru), F = "
           "15 N'da tepe (statik sürtünmenin en büyük değeri, 15 N), harekete geçtikten sonra Fs = 10 N sabit (yatay "
           'doğru). d) N = m·g = 50 N. ks = 15 / 50 = 0,3; kk = 10 / 50 = 0,2.',
  'birincil': 'Fiz02MK0139',
  'adimlar': [("a) Durgun blokta sürtünmenin statik olduğunu, 8 N büyüklüğünde ve F'ye zıt yönde olduğunu belirtir.",
               'Fiz02MK0129'),
              ('b) Statik sürtünmenin en büyük değerinin (15 N) kinetik sürtünmeden (10 N) büyük olduğunu '
               'karşılaştırır.',
               'Fiz02MK0131'),
              ("c) Grafiği çizer: 0–15 N arasında Fs = F, sonra 10 N'da sabit.", 'Fiz02MK0135'),
              ('c) Statik sürtünmenin en büyük değerini (15 N) grafikte işaretler.', 'Fiz02MK0136'),
              ('d) N = 50 N alarak ks = 15 / 50 = 0,3 ve kk = 10 / 50 = 0,2 hesaplar.', 'Fiz02MK0139')]},
 {'anahtar': 'f11_makarali_sistem',
  'baslik': '11. sınıf Newton ve sürtünme: Makaralı sistemde ivme ve ip gerilmesi',
  'ders': 'Fizik',
  'sinif_duzeyi': 11,
  'gorsel': 'f11_makarali_sistem.png',
  'metin': 'Şekildeki sistemde 3 kg kütleli A bloğu sürtünmesiz yatay masa üzerindedir ve kütlesi önemsiz bir '
           'makaradan geçen hafif bir iple 2 kg kütleli B bloğuna bağlıdır. Sistem serbest bırakılıyor. (g = 10 m/s²)\n'
           'a) A ve B bloklarına etki eden kuvvetleri ayrı ayrı serbest cisim diyagramlarında gösteriniz.\n'
           'b) Sistemi hareket ettiren net kuvveti bulunuz.\n'
           'c) Sistemin ivmesini hesaplayınız.\n'
           'd) İpteki gerilme kuvvetini hesaplayınız.',
  'cevap_bicimi': 'yazili',
  'secenekler': [],
  'dogru_cevap': 'b) 20 N  c) a = 4 m/s²  d) T = 12 N',
  'cozum': 'a) A: aşağı ağırlık (30 N), yukarı tepki kuvveti (30 N), makaraya doğru ip gerilmesi T. B: aşağı ağırlık '
           "(20 N), yukarı ip gerilmesi T. b) A'nın ağırlığı tepki kuvvetiyle dengelenir; sistemi hareket ettiren net "
           "kuvvet B'nin ağırlığıdır: Fnet = mB·g = 20 N. c) a = Fnet / (mA + mB) = 20 / 5 = 4 m/s². d) A için: T = "
           'mA·a = 3 · 4 = 12 N. (Kontrol, B için: mB·g − T = mB·a ⇒ 20 − T = 8 ⇒ T = 12 N.)',
  'birincil': 'Fiz02MK0128',
  'adimlar': [('a) A için ağırlık, tepki ve ip gerilmesini; B için ağırlık ve ip gerilmesini serbest cisim '
               'diyagramlarında gösterir.',
               'Fiz02MK0121'),
              ('a) İp gerilmesini her iki blokta da ip boyunca, bloktan dışarı doğru gösterir.', 'Fiz02MK0118'),
              ('b) Sistemi hareket ettiren net kuvveti Fnet = mB·g = 20 N bulur.', 'Fiz02MK0125'),
              ('c) Ortak ivmeyi a = 20 / (3 + 2) = 4 m/s² hesaplar.', 'Fiz02MK0127'),
              ('d) İp gerilmesini T = mA·a = 12 N hesaplar (ya da B için 20 − T = 2 · 4).', 'Fiz02MK0128')]},
 {'anahtar': 'f11_surtunme_yonu',
  'baslik': '11. sınıf Newton ve sürtünme: Yürürken ve bisiklette sürtünmenin yönü; eylemsizlik',
  'ders': 'Fizik',
  'sinif_duzeyi': 11,
  'gorsel': 'f11_surtunme_yonu.png',
  'metin': 'a) Düz bir yolda yürürken yerin ayağımıza uyguladığı sürtünme kuvvetinin yönü nedir? Yürüyebilmemizi bu '
           'kuvvetle ilişkilendirerek açıklayınız.\n'
           'b) Pedal çevrilerek hızlanan bir bisikletin arka tekerleğine yerden etki eden sürtünme kuvvetinin yönü '
           'nedir? Açıklayınız.\n'
           'c) Uzay boşluğunda hareket eden bir aracın motorları kapatılıyor. Araca hiçbir kuvvet etki etmediğine göre '
           'araç nasıl hareket eder? Bir arkadaşınız "Motor kapanınca araç yavaşlayıp durur." diyor; bu görüşü '
           'değerlendiriniz.',
  'cevap_bicimi': 'yazili',
  'secenekler': [],
  'dogru_cevap': 'a) İleri (hareket yönünde)  b) İleri (hareket yönünde)  c) Sabit hızla doğrusal hareketine devam '
                 'eder; arkadaşın görüşü yanlıştır.',
  'cozum': 'a) Yürürken ayağımız yeri geriye doğru iter; yer de ayağımıza ileri yönde statik sürtünme kuvveti uygular. '
           'Bizi ileri götüren bu kuvvettir; buzda yürüyemememizin nedeni sürtünmenin az olmasıdır. b) Pedalla '
           'döndürülen arka tekerlek yeri geriye iter; yer, tekerleğe ileri yönde sürtünme kuvveti uygular ve '
           'bisikleti hızlandırır. c) Net kuvvet sıfır olduğundan araç sabit hızla doğrusal hareketine devam eder '
           "(Newton'un birinci yasası). Hareketin sürmesi için kuvvet gerekmez; yavaşlaması için bir kuvvet gerekir. "
           'Arkadaşın görüşü yanlıştır.',
  'birincil': 'Fiz02MK0138',
  'adimlar': [('a) Yürürken yerin ayağa uyguladığı sürtünmenin ileri yönde olduğunu ve bizi ileri götürdüğünü açıklar.',
               'Fiz02MK0138'),
              ('b) Hızlanan bisikletin arka tekerleğine etki eden sürtünmenin ileri yönde olduğunu açıklar.',
               'Fiz02MK0138'),
              ('c) Net kuvvet sıfırken aracın sabit hızla doğrusal hareketine devam ettiğini belirtir; arkadaşın '
               'görüşünü çürütür.',
               'Fiz02MK0108')]}]
