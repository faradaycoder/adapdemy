import { useState, type FormEvent } from "react";
import { Link, Navigate } from "react-router-dom";
import { useOturum } from "../oturum";

export default function Kayit() {
  const { kullanici, kayitOl } = useOturum();
  const [ad, setAd] = useState("");
  const [eposta, setEposta] = useState("");
  const [sifre, setSifre] = useState("");
  const [rol, setRol] = useState<"ogretmen" | "ogrenci">("ogretmen");
  const [hata, setHata] = useState("");
  const [bekle, setBekle] = useState(false);

  if (kullanici) return <Navigate to="/" replace />;

  async function gonder(e: FormEvent) {
    e.preventDefault();
    setHata(""); setBekle(true);
    try { await kayitOl(ad, eposta, sifre, rol); } catch (err) { setHata((err as Error).message); } finally { setBekle(false); }
  }

  return (
    <form className="kart dar" onSubmit={gonder}>
      <h1>Kayıt ol</h1>
      <div className="secim">
        <button type="button" className={rol === "ogretmen" ? "" : "ikincil"} onClick={() => setRol("ogretmen")}>Öğretmenim</button>
        <button type="button" className={rol === "ogrenci" ? "" : "ikincil"} onClick={() => setRol("ogrenci")}>Öğrenciyim</button>
      </div>
      <label>Ad soyad<input value={ad} onChange={(e) => setAd(e.target.value)} required minLength={2} autoComplete="name" /></label>
      <label>E-posta<input type="email" value={eposta} onChange={(e) => setEposta(e.target.value)} required autoComplete="email" /></label>
      <label>Şifre (en az 8 karakter)<input type="password" value={sifre} onChange={(e) => setSifre(e.target.value)} required minLength={8} autoComplete="new-password" /></label>
      {hata && <p className="hata">{hata}</p>}
      <button disabled={bekle}>{bekle ? "Kaydediliyor…" : "Kayıt ol"}</button>
      <p className="soluk">Hesabın var mı? <Link to="/giris">Giriş yap</Link></p>
    </form>
  );
}
