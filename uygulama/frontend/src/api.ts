// Arka uçla konuşan küçük yardımcı. Jeton tarayıcıda saklanır ve her isteğe eklenir.

export type Kullanici = { id: number; ad: string; eposta: string; rol: "ogretmen" | "ogrenci" | "yonetici" };
export type Sinif = { id: number; ad: string; ders: string; sinif_duzeyi: number; kod: string | null; ogretmen: string; ogrenci_sayisi: number };
export type SinifAyrinti = Sinif & { ogrenciler: { id: number; ad: string; eposta: string; katilma: string }[] };
export type MKKisa = { kod: string; ifade: string; tur: string; islem_turu: string; zorluk: number | null; seviye: number | null };
export type MKAyrinti = MKKisa & {
  ders: string; ana_unite: string; bilissel_duzey: string; v: number | null; on_kosul_diger: string;
  olcme_turleri: string; ustalik_olcutu: string; on_kosullar: MKKisa[]; ardillar: MKKisa[];
  eslemeler: { sinif: number; sinif_unite: string; ogrenme_ciktisi: string; surec_bileseni: string }[];
  yanilgilar: { kod: string; ifade: string }[];
};

const JETON = "evalora_jeton";

export function jetonAl(): string | null {
  try { return localStorage.getItem(JETON); } catch { return null; }
}
export function jetonKaydet(j: string | null) {
  try { j ? localStorage.setItem(JETON, j) : localStorage.removeItem(JETON); } catch { /* özel pencerede saklanamaz */ }
}

export async function api<T>(yol: string, secenek: { method?: string; govde?: unknown } = {}): Promise<T> {
  const basliklar: Record<string, string> = { "Content-Type": "application/json" };
  const j = jetonAl();
  if (j) basliklar.Authorization = `Bearer ${j}`;
  const r = await fetch(yol, {
    method: secenek.method ?? (secenek.govde ? "POST" : "GET"),
    headers: basliklar,
    body: secenek.govde ? JSON.stringify(secenek.govde) : undefined,
  });
  if (!r.ok) {
    let mesaj = `Hata (${r.status})`;
    try {
      const v = await r.json();
      mesaj = typeof v.detail === "string" ? v.detail : (v.detail?.[0]?.msg ?? mesaj);
    } catch { /* gövde JSON değil */ }
    throw new Error(mesaj);
  }
  if (r.status === 204) return undefined as T;
  return r.json() as Promise<T>;
}

// ---------- Soru bankası ----------
export type MKBilgi = { kod: string; ifade: string; islem_turu: string; v: number | null; zorluk: number | null; seviye: number | null };
export type Secenek = { harf: string; metin: string; dogru: boolean; yanilgi_kod: string | null };
export type AdimG = { aciklama: string; mk_kod: string };
export type AdimC = AdimG & { pay: number; mk: MKBilgi | null; soru_mk_mi: boolean };
export type Esleme = { soru_mkleri: MKBilgi[]; birincil: string | null; zorluk: number | null; adimlar: AdimC[]; uyarilar: string[] };
export type SoruG = {
  ders: string; sinif_duzeyi: number; metin: string; gorsel: string | null; cevap_bicimi: string;
  secenekler: Secenek[]; dogru_cevap: string; cozum: string; birincil: string | null; adimlar: AdimG[];
};
export type Analiz = SoruG & { eslesme: Esleme; saglayici: string; notlar?: string[] };
export type Soru = SoruG & { id: number; zorluk: number | null; durum: string; kaynak: string; eslesme: Esleme };
export type SoruKisa = {
  id: number; ders: string; sinif_duzeyi: number; metin: string; gorsel: string | null; cevap_bicimi: string;
  zorluk: number | null; durum: string; birincil: string | null; soru_mkleri: string[];
  mk_detay: MKBilgi[]; onkosul_detay: MKBilgi[];
};
export type Ornek = { anahtar: string; baslik: string; ders: string; sinif_duzeyi: number; gorsel: string | null };

export const CEVAP_BICIMLERI: Record<string, string> = {
  coktan_secmeli: "Çoktan seçmeli", kisa_cevap: "Kısa cevap", yazili: "Yazılı (açık uçlu)", kagit: "Kâğıtta çözüm",
};

// ---------- Sınavlar ----------
export type KapsamMK = { kod: string; ifade: string; zorluk: number | null; soru_sayisi: number };
export type AtamaT = {
  id: number; sinav_id: number; sinav_adi: string; sinif_id: number; sinif_adi: string;
  baslangic: string; bitis: string; durum: "baslamadi" | "acik" | "bitti"; soru_sayisi: number;
  teslim_durumu: "devam" | "teslim" | null;
  sonuc_acik: boolean;
  sonuc_yeni: boolean;
};
export type SinavT = {
  id: number; ad: string; ders: string; sinif_duzeyi: number; aciklama: string; sure_dk: number | null;
  sorular: SoruKisa[]; toplam_zorluk: number; kapsam: KapsamMK[]; atamalar: AtamaT[];
};
export type SinavKisa = { id: number; ad: string; ders: string; sinif_duzeyi: number; soru_sayisi: number; toplam_zorluk: number; atama_sayisi: number };
export type Yazdir = {
  sinav_id: number; ad: string; ders: string; sinif_duzeyi: number; aciklama: string; sure_dk: number | null;
  atama_id: number | null; sinif_adi: string | null;
  sorular: { sira: number; soru_id: number; metin: string; gorsel: string | null; cevap_bicimi: string; secenekler: { harf: string; metin: string }[] }[];
  ogrenciler: { id: number; ad: string }[];
};
export const ATAMA_DURUMU: Record<string, string> = { baslamadi: "Başlamadı", acik: "Açık", bitti: "Bitti" };
export const tarihSaat = (s: string) => new Date(s).toLocaleString("tr-TR", { dateStyle: "short", timeStyle: "short" });

// ---------- Teslim ----------
export type CevapT = { soru_id: number; secilen: string | null; metin: string; dosyalar: { id: number; dosya: string }[] };
export type SinavSorusu = { sira: number; soru_id: number; metin: string; gorsel: string | null; cevap_bicimi: string; secenekler: { harf: string; metin: string }[] };
export type OturumT = {
  atama_id: number; sinav_adi: string; ders: string; aciklama: string; sure_dk: number | null; bitis: string;
  durum: "devam" | "teslim" | "kapali"; sorular: SinavSorusu[]; cevaplar: CevapT[];
  genel_dosyalar: { id: number; dosya: string }[];
};
export type TeslimSatir = { teslim_id: number | null; ogrenci_id: number; ogrenci: string; durum: string; cevaplanan: number; soru_sayisi: number; teslim_zamani: string | null; degerlendirme: string | null; puan: number | null; en_yuksek: number | null; genel_dosya: number };
export type TeslimAyrinti = { teslim_id: number; ogrenci: string; durum: string; teslim_zamani: string | null; sorular: SinavSorusu[]; cevaplar: CevapT[] };
export const TESLIM_DURUMU: Record<string, string> = { baslamadi: "Başlamadı", devam: "Çözüyor", teslim: "Teslim etti", kapali: "Süre doldu" };

// ---------- Bildirimler ----------
export type Bildirim = { tur: "acik_sinav" | "sonuc" | "teslim"; metin: string; baglanti: string; zaman: string; son: string | null };
export type Bildirimler = { sayi: number; ogeler: Bildirim[] };

// ---------- Değerlendirme ----------
export type AdimSonuc = {
  adim_id: number; sira: number; aciklama: string; mk_kod: string; mk_ifade: string; soru_mk_mi: boolean;
  pay: number; en_yuksek: number; durum: "biliyor" | "bilmiyor" | "olculemedi" | null; puan: number; kaynak: string | null; gerekce: string;
};
export type SoruSonuc = {
  sira: number; soru_id: number; metin: string; gorsel: string | null; cevap_bicimi: string;
  secenekler: { harf: string; metin: string; dogru: boolean }[]; dogru_cevap: string; cozum: string; zorluk: number;
  secilen: string | null; metin_cevap: string; dosyalar: { id: number; dosya: string; kaynak?: string }[]; yanilgi: string | null;
  ogretmen_notu: string; aciklama_kaynak: string; adimlar: AdimSonuc[]; puan: number; tamam: boolean;
};
export type MKSonuc = { kod: string; ifade: string; durum: "biliyor" | "bilmiyor" | "olculemedi"; kanit: number };
export type DegerlendirmeT = {
  teslim_id: number; ogrenci: string; sinav_adi: string; degerlendirme: "bekliyor" | "onayli"; teslim_zamani: string | null;
  puan: number; en_yuksek: number; sorular: SoruSonuc[]; mkler: MKSonuc[];
  genel_dosyalar: { id: number; dosya: string }[]; genel_geri_bildirim: string; genel_kaynak: string;
};
// Öğrencinin gördüğü sonuç: rubrik, MK kodu ve adım puanı yok.
export type OgrenciSoruT = {
  sira: number; metin: string; gorsel: string | null; cevap_bicimi: string; secenekler: { harf: string; metin: string }[];
  secilen: string | null; dogru_sik: string | null; senin_cevabin: string; dosyalar: { id: number; dosya: string }[];
  dogru_cevap: string; cozum: string; durum: "dogru" | "kismen" | "yanlis" | "bos"; puan: number; en_yuksek: number; aciklama: string;
  konular: KonuKartiT[];
};
export type VideoT = { id: number; video_id: string; kanal: string; baslik: string; bas: number; son: number; kapak: string };
export type KonuKartiT = { konu: string; anlatim: VideoT | null; soru: VideoT | null };
export type OgrenciSonucT = { sinav_adi: string; puan: number; en_yuksek: number; genel_geri_bildirim: string; sorular: OgrenciSoruT[]; calis: string[] };
export const ADIM_DURUMU: Record<string, string> = { biliyor: "Biliyor", bilmiyor: "Bilmiyor", olculemedi: "Ölçülemedi" };
