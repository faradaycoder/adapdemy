"""Veritabanı tabloları (PLAN_UYGULAMA.md bölüm 6).

A aşamasında: hesaplar, sınıflar ve MK verisi. Soru, sınav, teslim ve değerlendirme tabloları sonraki aşamalarda eklenir.
Tablolar LTI 1.3'e uygun düşünülmüştür: kullanıcı ↔ LTI kullanıcısı, sınıf ↔ LTI bağlamı (context).
"""

from datetime import datetime, timezone

from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .vt import Taban


def _simdi():
    return datetime.now(timezone.utc)


# ---------- Hesaplar ve sınıflar ----------

ROLLER = ("ogretmen", "ogrenci", "yonetici")


class Kullanici(Taban):
    __tablename__ = "kullanici"
    id: Mapped[int] = mapped_column(primary_key=True)
    ad: Mapped[str] = mapped_column(String(120))
    eposta: Mapped[str] = mapped_column(String(254), unique=True, index=True)
    sifre_hash: Mapped[str | None] = mapped_column(String(255))  # Google ile girenlerde boş
    google_id: Mapped[str | None] = mapped_column(String(64), unique=True)
    okul_no: Mapped[str | None] = mapped_column(String(32))  # LMS bağlantısında öğrenci numarası
    rol: Mapped[str] = mapped_column(String(16))
    aktif: Mapped[bool] = mapped_column(Boolean, default=True)
    olusturma: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=_simdi)


class Sinif(Taban):
    __tablename__ = "sinif"
    id: Mapped[int] = mapped_column(primary_key=True)
    ad: Mapped[str] = mapped_column(String(120))
    ders: Mapped[str] = mapped_column(String(16))  # Fizik, Matematik
    sinif_duzeyi: Mapped[int] = mapped_column(Integer)  # 5–12
    kod: Mapped[str] = mapped_column(String(12), unique=True, index=True)  # öğrencinin katılma kodu
    ogretmen_id: Mapped[int] = mapped_column(ForeignKey("kullanici.id"))
    olusturma: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=_simdi)
    ogretmen: Mapped[Kullanici] = relationship()
    uyeler: Mapped[list["SinifUye"]] = relationship(back_populates="sinif", cascade="all, delete-orphan")


class SinifUye(Taban):
    __tablename__ = "sinif_uye"
    __table_args__ = (UniqueConstraint("sinif_id", "ogrenci_id"),)
    id: Mapped[int] = mapped_column(primary_key=True)
    sinif_id: Mapped[int] = mapped_column(ForeignKey("sinif.id"))
    ogrenci_id: Mapped[int] = mapped_column(ForeignKey("kullanici.id"))
    katilma: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=_simdi)
    sinif: Mapped[Sinif] = relationship(back_populates="uyeler")
    ogrenci: Mapped[Kullanici] = relationship()


# ---------- MK verisi (CSV'lerden içe aktarılır; tek doğruluk kaynağı CSV'lerdir) ----------

class MK(Taban):
    __tablename__ = "mk"
    kod: Mapped[str] = mapped_column(String(16), primary_key=True)  # Fiz05MK0051
    ders: Mapped[str] = mapped_column(String(16), index=True)
    ana_unite: Mapped[str] = mapped_column(String(4))
    ifade: Mapped[str] = mapped_column(Text)
    tur: Mapped[str] = mapped_column(String(8))  # Bilgi / Beceri
    bilissel_duzey: Mapped[str] = mapped_column(String(32))
    islem_turu: Mapped[str] = mapped_column(String(48))
    v: Mapped[float | None] = mapped_column(Float)  # işlem değeri
    zorluk: Mapped[float | None] = mapped_column(Float)  # Z (ALGORITMA.md bölüm 4)
    seviye: Mapped[int | None] = mapped_column(Integer)
    on_kosul_diger: Mapped[str] = mapped_column(Text, default="")
    olcme_turleri: Mapped[str] = mapped_column(String(32), default="")
    ustalik_olcutu: Mapped[str] = mapped_column(String(64), default="")
    durum: Mapped[str] = mapped_column(String(16), default="taslak")


class MKOnKosul(Taban):
    """A → B: B'yi (mk_kod) öğrenmek için A (on_kosul_kod) gerekir."""
    __tablename__ = "mk_on_kosul"
    __table_args__ = (UniqueConstraint("mk_kod", "on_kosul_kod"),)
    id: Mapped[int] = mapped_column(primary_key=True)
    mk_kod: Mapped[str] = mapped_column(ForeignKey("mk.kod"), index=True)
    on_kosul_kod: Mapped[str] = mapped_column(ForeignKey("mk.kod"), index=True)


class MKEsleme(Taban):
    __tablename__ = "mk_esleme"
    id: Mapped[int] = mapped_column(primary_key=True)
    mk_kod: Mapped[str] = mapped_column(ForeignKey("mk.kod"), index=True)
    sinif: Mapped[int] = mapped_column(Integer, index=True)
    sinif_unite: Mapped[str] = mapped_column(String(16))
    ogrenme_ciktisi: Mapped[str] = mapped_column(String(24), index=True)  # FİZ.10.3.4
    surec_bileseni: Mapped[str] = mapped_column(String(8))


class Yanilgi(Taban):
    __tablename__ = "yanilgi"
    kod: Mapped[str] = mapped_column(String(16), primary_key=True)  # Fiz05YG0007
    ders: Mapped[str] = mapped_column(String(16))
    ana_unite: Mapped[str] = mapped_column(String(4))
    ifade: Mapped[str] = mapped_column(Text)


class MKYanilgi(Taban):
    __tablename__ = "mk_yanilgi"
    __table_args__ = (UniqueConstraint("mk_kod", "yanilgi_kod"),)
    id: Mapped[int] = mapped_column(primary_key=True)
    mk_kod: Mapped[str] = mapped_column(ForeignKey("mk.kod"), index=True)
    yanilgi_kod: Mapped[str] = mapped_column(ForeignKey("yanilgi.kod"))


# ---------- Soru bankası (B aşaması; ALGORITMA.md bölüm 5) ----------

CEVAP_BICIMLERI = ("coktan_secmeli", "kisa_cevap", "yazili", "kagit")


class Soru(Taban):
    __tablename__ = "soru"
    id: Mapped[int] = mapped_column(primary_key=True)
    ders: Mapped[str] = mapped_column(String(16), index=True)
    sinif_duzeyi: Mapped[int] = mapped_column(Integer, index=True)
    metin: Mapped[str] = mapped_column(Text)  # sorunun okunmuş metni
    gorsel: Mapped[str | None] = mapped_column(String(255))  # yüklenen görselin dosya adı
    cevap_bicimi: Mapped[str] = mapped_column(String(16))
    dogru_cevap: Mapped[str] = mapped_column(Text, default="")
    cozum: Mapped[str] = mapped_column(Text, default="")
    zorluk: Mapped[float | None] = mapped_column(Float)  # b = Σ Z (sorunun MK'leri)
    kaynak: Mapped[str] = mapped_column(String(16), default="yuklendi")  # yuklendi / uretildi
    durum: Mapped[str] = mapped_column(String(16), default="taslak")  # taslak / onayli
    olusturan_id: Mapped[int] = mapped_column(ForeignKey("kullanici.id"))
    olusturma: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=_simdi)
    mkler: Mapped[list["SoruMK"]] = relationship(cascade="all, delete-orphan", order_by="SoruMK.id")
    adimlar: Mapped[list["RubrikAdim"]] = relationship(cascade="all, delete-orphan", order_by="RubrikAdim.sira")
    secenekler: Mapped[list["Secenek"]] = relationship(cascade="all, delete-orphan", order_by="Secenek.harf")


class SoruMK(Taban):
    """Sorunun MK'leri: çözüm için gereken en üstteki MK'ler (ALGORITMA.md 5.1)."""
    __tablename__ = "soru_mk"
    __table_args__ = (UniqueConstraint("soru_id", "mk_kod"),)
    id: Mapped[int] = mapped_column(primary_key=True)
    soru_id: Mapped[int] = mapped_column(ForeignKey("soru.id"), index=True)
    mk_kod: Mapped[str] = mapped_column(ForeignKey("mk.kod"))
    birincil: Mapped[bool] = mapped_column(Boolean, default=False)


class RubrikAdim(Taban):
    """Çözüm adımı; ön koşul MK'lere de bağlanabilir (teşhis için). pay: sorunun puanındaki oranı (0–1)."""
    __tablename__ = "rubrik_adim"
    id: Mapped[int] = mapped_column(primary_key=True)
    soru_id: Mapped[int] = mapped_column(ForeignKey("soru.id"), index=True)
    sira: Mapped[int] = mapped_column(Integer)
    aciklama: Mapped[str] = mapped_column(Text)
    mk_kod: Mapped[str] = mapped_column(ForeignKey("mk.kod"))
    pay: Mapped[float] = mapped_column(Float, default=0.0)


class Secenek(Taban):
    __tablename__ = "secenek"
    id: Mapped[int] = mapped_column(primary_key=True)
    soru_id: Mapped[int] = mapped_column(ForeignKey("soru.id"), index=True)
    harf: Mapped[str] = mapped_column(String(2))
    metin: Mapped[str] = mapped_column(Text)
    dogru: Mapped[bool] = mapped_column(Boolean, default=False)
    yanilgi_kod: Mapped[str | None] = mapped_column(ForeignKey("yanilgi.kod"))


# ---------- Sınav ve atama (C aşaması) ----------

class Sinav(Taban):
    __tablename__ = "sinav"
    id: Mapped[int] = mapped_column(primary_key=True)
    ad: Mapped[str] = mapped_column(String(160))
    ders: Mapped[str] = mapped_column(String(16))
    sinif_duzeyi: Mapped[int] = mapped_column(Integer)
    aciklama: Mapped[str] = mapped_column(Text, default="")
    sure_dk: Mapped[int | None] = mapped_column(Integer)
    olusturan_id: Mapped[int] = mapped_column(ForeignKey("kullanici.id"))
    olusturma: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=_simdi)
    sorular: Mapped[list["SinavSoru"]] = relationship(cascade="all, delete-orphan", order_by="SinavSoru.sira")
    atamalar: Mapped[list["Atama"]] = relationship(back_populates="sinav", cascade="all, delete-orphan")


class SinavSoru(Taban):
    __tablename__ = "sinav_soru"
    __table_args__ = (UniqueConstraint("sinav_id", "soru_id"),)
    id: Mapped[int] = mapped_column(primary_key=True)
    sinav_id: Mapped[int] = mapped_column(ForeignKey("sinav.id"), index=True)
    soru_id: Mapped[int] = mapped_column(ForeignKey("soru.id"))
    sira: Mapped[int] = mapped_column(Integer)
    soru: Mapped[Soru] = relationship()


class Atama(Taban):
    """Sınavın bir sınıfa verilmesi (LTI'daki 'assignment' karşılığı)."""
    __tablename__ = "atama"
    id: Mapped[int] = mapped_column(primary_key=True)
    sinav_id: Mapped[int] = mapped_column(ForeignKey("sinav.id"), index=True)
    sinif_id: Mapped[int] = mapped_column(ForeignKey("sinif.id"), index=True)
    baslangic: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    bitis: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    olusturma: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=_simdi)
    sinav: Mapped[Sinav] = relationship(back_populates="atamalar")
    sinif: Mapped[Sinif] = relationship()
    teslimler: Mapped[list["Teslim"]] = relationship(back_populates="atama", cascade="all, delete-orphan")


# ---------- Teslim ve cevap (D aşaması) ----------

class Teslim(Taban):
    """Bir öğrencinin bir atamadaki sınav oturumu."""
    __tablename__ = "teslim"
    __table_args__ = (UniqueConstraint("atama_id", "ogrenci_id"),)
    id: Mapped[int] = mapped_column(primary_key=True)
    atama_id: Mapped[int] = mapped_column(ForeignKey("atama.id"), index=True)
    ogrenci_id: Mapped[int] = mapped_column(ForeignKey("kullanici.id"), index=True)
    durum: Mapped[str] = mapped_column(String(16), default="devam")  # devam / teslim
    baslama: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=_simdi)
    teslim_zamani: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    ogretmen_gordu: Mapped[bool] = mapped_column(Boolean, default=False)  # teslim bildirimi okundu mu
    degerlendirme: Mapped[str] = mapped_column(String(16), default="bekliyor")  # bekliyor / onayli
    puan: Mapped[float | None] = mapped_column(Float)  # onaylanınca: kazanılan toplam
    en_yuksek: Mapped[float | None] = mapped_column(Float)  # sınavın toplam puanı (Σ b)
    sonuc_zamani: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))  # değerlendirme onaylandığında
    ogrenci_gordu: Mapped[bool] = mapped_column(Boolean, default=False)  # sonuç bildirimi okundu mu
    genel_geri_bildirim: Mapped[str] = mapped_column(Text, default="")  # öğrenciye sınavın geneli için kısa geri bildirim
    genel_kaynak: Mapped[str] = mapped_column(String(12), default="ogretmen")
    # Süre dolunca kendiliğinden teslim (öğrenci "teslim et"e basmadan; hiç açmadıysa boş kâğıt) ve süre uzatma
    otomatik_teslim: Mapped[bool] = mapped_column(Boolean, default=False)
    uzatma: Mapped[str | None] = mapped_column(String(12))  # None / bekliyor / verildi / reddedildi
    uzatma_notu: Mapped[str] = mapped_column(Text, default="")  # öğrencinin talep gerekçesi
    uzatma_zamani: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))  # talep ya da karar anı
    uzatma_dk: Mapped[int | None] = mapped_column(Integer)  # öğretmenin verdiği ek süre
    uzatma_bitis: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))  # verilen sürenin sonu (atama bitişini de aşar)
    uzatma_ogrenci_gordu: Mapped[bool] = mapped_column(Boolean, default=True)  # karar bildirimi okundu mu
    atama: Mapped[Atama] = relationship(back_populates="teslimler")
    ogrenci: Mapped[Kullanici] = relationship()
    cevaplar: Mapped[list["Cevap"]] = relationship(back_populates="teslim", cascade="all, delete-orphan")
    genel_dosyalar: Mapped[list["TeslimDosya"]] = relationship(cascade="all, delete-orphan", order_by="TeslimDosya.id")


class Cevap(Taban):
    __tablename__ = "cevap"
    __table_args__ = (UniqueConstraint("teslim_id", "soru_id"),)
    id: Mapped[int] = mapped_column(primary_key=True)
    teslim_id: Mapped[int] = mapped_column(ForeignKey("teslim.id"), index=True)
    soru_id: Mapped[int] = mapped_column(ForeignKey("soru.id"))
    secilen: Mapped[str | None] = mapped_column(String(2))  # çoktan seçmelide şık
    metin: Mapped[str] = mapped_column(Text, default="")  # kısa ya da yazılı cevap
    guncelleme: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=_simdi, onupdate=_simdi)
    teslim: Mapped[Teslim] = relationship(back_populates="cevaplar")
    dosyalar: Mapped[list["CevapDosya"]] = relationship(cascade="all, delete-orphan", order_by="CevapDosya.id")
    adimlar: Mapped[list["AdimDegerlendirme"]] = relationship(cascade="all, delete-orphan")
    ogretmen_notu: Mapped[str] = mapped_column(Text, default="")  # öğrenciye açıklama ("nerede hata yaptın"), öğretmen diliyle
    aciklama_kaynak: Mapped[str] = mapped_column(String(12), default="ogretmen")  # sistem (taslak) / ogretmen
    yanilgi_kod: Mapped[str | None] = mapped_column(String(16))  # seçilen çeldiricinin yanılgısı


class CevapDosya(Taban):
    """Kâğıda yapılan çözümün fotoğrafı ya da taraması (bir soru için birden çok parça olabilir)."""
    __tablename__ = "cevap_dosya"
    id: Mapped[int] = mapped_column(primary_key=True)
    cevap_id: Mapped[int] = mapped_column(ForeignKey("cevap.id"), index=True)
    dosya: Mapped[str] = mapped_column(String(255))
    kaynak: Mapped[str] = mapped_column(String(16), default="ogrenci")  # ogrenci (kendisi yükledi) / kagittan (tüm kâğıttan kırpıldı)
    yukleme: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=_simdi)


# ---------- Değerlendirme (E aşaması; ALGORITMA.md 5.3 ve 6.1) ----------

ADIM_DURUMLARI = ("biliyor", "bilmiyor", "olculemedi")


class AdimDegerlendirme(Taban):
    """Bir cevabın bir rubrik adımındaki sonucu. Puan = pay × soru zorluğu (yalnız 'biliyor' ise)."""
    __tablename__ = "adim_degerlendirme"
    __table_args__ = (UniqueConstraint("cevap_id", "rubrik_adim_id"),)
    id: Mapped[int] = mapped_column(primary_key=True)
    cevap_id: Mapped[int] = mapped_column(ForeignKey("cevap.id"), index=True)
    rubrik_adim_id: Mapped[int] = mapped_column(ForeignKey("rubrik_adim.id"))
    durum: Mapped[str] = mapped_column(String(12))  # biliyor / bilmiyor / olculemedi
    puan: Mapped[float] = mapped_column(Float, default=0.0)
    kaynak: Mapped[str] = mapped_column(String(12))  # otomatik / sistem / ogretmen
    gerekce: Mapped[str] = mapped_column(Text, default="")
    adim: Mapped[RubrikAdim] = relationship()


class TeslimDosya(Taban):
    """Sınavın tamamı için yüklenen dosya (tek PDF ya da sayfa sayfa fotoğraf). Sorulara henüz ayrılmamıştır:
    öğretmen değerlendirirken görür; API anahtarı ve QR okuma gelince sayfalar sorulara otomatik dağıtılacak."""
    __tablename__ = "teslim_dosya"
    id: Mapped[int] = mapped_column(primary_key=True)
    teslim_id: Mapped[int] = mapped_column(ForeignKey("teslim.id"), index=True)
    dosya: Mapped[str] = mapped_column(String(255))
    yukleme: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=_simdi)


# ---------- Telafi: MK'ye eşlenmiş video parçaları ----------


class VideoParca(Taban):
    """Bir YouTube videosunun tek bir MK'yi anlatan parçası (başlangıç–bitiş saniyesi). Öğrenciye 'izle' olarak önerilir."""

    __tablename__ = "video_parca"
    __table_args__ = (UniqueConstraint("video_id", "bas", "mk_kod"),)
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    mk_kod: Mapped[str] = mapped_column(ForeignKey("mk.kod"), index=True)
    video_id: Mapped[str] = mapped_column(String(16))  # YouTube video kimliği
    kanal: Mapped[str] = mapped_column(String(120), default="")
    video_baslik: Mapped[str] = mapped_column(String(300), default="")
    video_sure: Mapped[int | None] = mapped_column(Integer, nullable=True)  # saniye; kapak karesini seçmek için
    baslik: Mapped[str] = mapped_column(String(200))  # öğrenci dilinde parça başlığı
    tur: Mapped[str] = mapped_column(String(8), default="konu")  # konu (anlatım) / soru (benzer soru çözümü)
    konu: Mapped[str] = mapped_column(String(200), default="")  # MK'nin öğrenci dilinde adı (kart başlığı)
    bas: Mapped[int] = mapped_column(Integer)  # saniye
    son: Mapped[int] = mapped_column(Integer)
    sira: Mapped[int] = mapped_column(Integer, default=0)  # aynı MK için öncelik (küçük önce)
    neden: Mapped[str] = mapped_column(Text, default="")  # neden seçildi (öğretmen için)
    onayli: Mapped[bool] = mapped_column(Boolean, default=False)


class VideoIzleme(Taban):
    """Öğrencinin hangi parçayı açtığı: kim anlatımdan, kim örnekten öğreniyor, sonra öğrenmeyle karşılaştırılır."""

    __tablename__ = "video_izleme"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    ogrenci_id: Mapped[int] = mapped_column(ForeignKey("kullanici.id"), index=True)
    parca_id: Mapped[int] = mapped_column(ForeignKey("video_parca.id"), index=True)
    teslim_id: Mapped[int | None] = mapped_column(ForeignKey("teslim.id"), nullable=True)
    zaman: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=_simdi)
