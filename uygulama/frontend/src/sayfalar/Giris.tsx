import { useState, type FormEvent } from "react";
import { Link, Navigate } from "react-router-dom";
import { useOturum } from "../oturum";

export default function Giris() {
  const { kullanici, girisYap } = useOturum();
  const [eposta, setEposta] = useState("");
  const [sifre, setSifre] = useState("");
  const [hata, setHata] = useState("");
  const [bekle, setBekle] = useState(false);

  if (kullanici) return <Navigate to="/" replace />;

  async function gonder(e: FormEvent) {
    e.preventDefault();
    setHata(""); setBekle(true);
    try { await girisYap(eposta, sifre); } catch (err) { setHata((err as Error).message); } finally { setBekle(false); }
  }

  return (
    <form className="kart dar" onSubmit={gonder}>
      <p className="tanitim"><b>EVALORA</b> · Ölç. Teşhis et. Telafi et.<br /><span className="soluk">Mikro kazanım temelli ölçme, teşhis ve telafi</span></p>
      <h1>Giriş yap</h1>
      <label>E-posta<input type="email" value={eposta} onChange={(e) => setEposta(e.target.value)} required autoComplete="email" /></label>
      <label>Şifre<input type="password" value={sifre} onChange={(e) => setSifre(e.target.value)} required autoComplete="current-password" /></label>
      {hata && <p className="hata">{hata}</p>}
      <button disabled={bekle}>{bekle ? "Giriliyor…" : "Giriş yap"}</button>
      <button type="button" className="ikincil" disabled title="Yakında">Google ile giriş (yakında)</button>
      <p className="soluk">Hesabın yok mu? <Link to="/kayit">Kayıt ol</Link></p>
    </form>
  );
}
