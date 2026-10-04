import { useEffect, useState, type FormEvent } from "react";
import { Link } from "react-router-dom";
import { api, type Sinif } from "../api";

export default function OgretmenAna() {
  const [siniflar, setSiniflar] = useState<Sinif[]>([]);
  const [ad, setAd] = useState("");
  const [ders, setDers] = useState("Fizik");
  const [duzey, setDuzey] = useState(10);
  const [hata, setHata] = useState("");

  useEffect(() => { api<Sinif[]>("/api/siniflar").then(setSiniflar).catch((e) => setHata(e.message)); }, []);

  async function ac(e: FormEvent) {
    e.preventDefault();
    setHata("");
    try {
      const s = await api<Sinif>("/api/siniflar", { govde: { ad, ders, sinif_duzeyi: duzey } });
      setSiniflar([...siniflar, s]);
      setAd("");
    } catch (err) { setHata((err as Error).message); }
  }

  const duzeyler = ders === "Fizik" ? [9, 10, 11, 12] : [5, 6, 7, 8, 9, 10, 11, 12];

  return (
    <div className="sayfa">
      <h1>Sınıflarım</h1>
      {siniflar.length === 0 && <p className="soluk">Henüz sınıfın yok. Aşağıdan ilk sınıfını aç; öğrencilerin sınıf koduyla katılır.</p>}
      <div className="izgara">
        {siniflar.map((s) => (
          <Link key={s.id} to={`/sinif/${s.id}`} className="kart sinif">
            <strong>{s.ad}</strong>
            <span>{s.ders} · {s.sinif_duzeyi}. sınıf</span>
            <span>{s.ogrenci_sayisi} öğrenci</span>
            <span className="kod">Kod: {s.kod}</span>
          </Link>
        ))}
      </div>

      <form className="kart" onSubmit={ac}>
        <h2>Yeni sınıf aç</h2>
        <div className="satir">
          <label>Sınıf adı<input value={ad} onChange={(e) => setAd(e.target.value)} placeholder="ör. 10-A Fizik" required /></label>
          <label>Ders
            <select value={ders} onChange={(e) => { setDers(e.target.value); setDuzey(e.target.value === "Fizik" ? 10 : 8); }}>
              <option>Fizik</option><option>Matematik</option>
            </select>
          </label>
          <label>Sınıf düzeyi
            <select value={duzey} onChange={(e) => setDuzey(Number(e.target.value))}>
              {duzeyler.map((d) => <option key={d} value={d}>{d}</option>)}
            </select>
          </label>
        </div>
        {hata && <p className="hata">{hata}</p>}
        <button>Sınıf aç</button>
      </form>
    </div>
  );
}
