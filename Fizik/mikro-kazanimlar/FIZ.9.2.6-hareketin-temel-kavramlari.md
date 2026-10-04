# Mikro Kazanım Ayrıştırması: FİZ.9.2.6 (taslak v0.1)

> **FİZ.9.2.6** Hareketin temel kavramlarının tanımlarına yönelik tümevarımsal akıl yürütebilme
> a) Örnekleri gözlemleyerek görseller arasındaki benzerlikleri bulur.
> b) Genellemeler yapar.
>
> Kaynak: https://tymm.meb.gov.tr/fizik-dersi/unite/57
> Sınıf ünitesi: Fiz09-U2 (Kuvvet ve Hareket) · Ana ünite: 02 Kuvvet ve Hareket

Yöntem: `Fizik/mikro-kazanimlar/FIZ.10.3.4-esdeger-direnc.md` dosyasındaki adımlar; kodlama, Bilgi/Beceri ve işlem türü ölçütü: `KODLAMA.md`.

---

## 1. Yanılgılar

| Kod | Yanılgı |
|---|---|
| Fiz02YG0006 | Yer değiştirme ile alınan yol her zaman birbirine eşittir. |
| Fiz02YG0007 | Hız ile sürat aynı kavramdır; hızın yönü yoktur. |
| Fiz02YG0008 | Ortalama sürat, ilk ve son süratlerin ortalamasıdır. |

---

## 2. Mikro kazanımlar

| Kod | Mikro kazanım (Öğrenci...) | Tür | İşlem türü | Bileşen | Düzey | Ön koşul | Yanılgı | Ölçme |
|---|---|---|---|---|---|---|---|---|
| Fiz02MK0036 | Referans noktasını tanımlar. | Bilgi | Tanıma ve hatırlama | a, b | Anlama | – | – | ÇS |
| Fiz02MK0037 | Konumu tanımlar. | Bilgi | Tanıma ve hatırlama | a, b | Anlama | Fiz02MK0036; Fiz02MK0012 | – | ÇS |
| Fiz02MK0038 | Alınan yolu tanımlar. | Bilgi | Tanıma ve hatırlama | a, b | Anlama | Fiz02MK0011 | – | ÇS |
| Fiz02MK0039 | Seçilen referans noktasına göre cismin konumunu işaretiyle (+/−) belirtir. | Beceri | Tanıma ve hatırlama | b | Uygulama | Fiz02MK0036; Fiz02MK0037 | – | ÇS |
| Fiz02MK0040 | Yer değiştirmeyi (son konum − ilk konum) alınan yoldan ayırt eder. | Bilgi | Ayırt etme ve sınıflama | b | Anlama | Fiz02MK0039; Fiz02MK0038 | Fiz02YG0006 | ÇS |
| Fiz02MK0041 | Hızın yönlü (vektörel) bir büyüklük olduğunu açıklar. | Bilgi | Açıklama ve özetleme | b | Anlama | Fiz02MK0040; Fiz02MK0013 | Fiz02YG0007 | ÇS |
| Fiz02MK0042 | Süratin yönsüz (skaler) bir büyüklük olduğunu açıklar. | Bilgi | Açıklama ve özetleme | b | Anlama | Fiz02MK0038; Fiz02MK0013 | – | ÇS |
| Fiz02MK0043 | Anlık sürat ile ortalama sürati örnekler üzerinden ayırt eder. | Bilgi | Ayırt etme ve sınıflama | b | Anlama | Fiz02MK0042 | Fiz02YG0008 | ÇS |
| Fiz02MK0044 | Anlık hız ile ortalama hızı örnekler üzerinden ayırt eder. | Bilgi | Ayırt etme ve sınıflama | b | Anlama | Fiz02MK0041 | – | ÇS |
| Fiz02MK0045 | İvmeyi hızdaki değişimi gösteren nicelik olarak örneklerle tanımlar. | Bilgi | Tanıma ve hatırlama | b | Anlama | Fiz02MK0041 | – | ÇS |
| Fiz02MK0046 | İvmenin vektörel bir nicelik olduğunu belirtir. | Bilgi | Tanıma ve hatırlama | b | Anlama | Fiz02MK0045; Fiz02MK0012 | – | ÇS |
| Fiz02MK0047 | Alınan yoldan ortalama sürati hesaplar. | Beceri | Kural uygulama | b | Uygulama | Fiz02MK0043 | – | ÇS |
| Fiz02MK0048 | Yer değiştirmeden ortalama hızı hesaplar. | Beceri | Kural uygulama | b | Uygulama | Fiz02MK0044 | Fiz02YG0007; Fiz02YG0006 | ÇS |
| Fiz02MK0049 | Hareketin temel kavramlarını sürat sınırları ve trafikteki yeşil dalga gibi günlük hayat durumlarıyla ilişkilendirerek açıklar. | Bilgi | Açıklama ve özetleme | b | Anlama | Fiz02MK0043; Fiz02MK0044; Fiz02MK0045; Fiz02MK0046 | – | AU, PG |

ÇS: çoktan seçmeli · AU: açık uçlu · PG: performans görevi (rubrikle)

Özet: 14 mikro kazanım (14 yeni, 0 yeniden kullanım); yeni olanlardan 11 Bilgi, 3 Beceri.

---

## 3. Örnek ölçme maddesi

**Fiz02MK0043:** Bir araç yolun ilk yarısını 40 km/h, ikinci yarısını 60 km/h süratle gidiyor. Ortalama sürati için hangisi doğrudur?  
A) 50 km/h (Fiz02YG0008) · B) 50 km/h'ten küçüktür ✔ · C) 50 km/h'ten büyüktür · D) Bilinemez

Ustalık ölçütü (varsayılan): farklı bağlamlarda 3 maddeden en az 2'si doğru; performans görevli olanlarda rubrikte "yeterli" ve üstü.
