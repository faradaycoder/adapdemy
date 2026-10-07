import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api, type SinifAyrinti } from "../api";

export default function SinifSayfasi() {
  const { id } = useParams();
  const [s, setS] = useState<SinifAyrinti | null>(null);
  const [hata, setHata] = useState("");

  useEffect(() => { api<SinifAyrinti>(`/api/siniflar/${id}`).then(setS).catch((e) => setHata(e.message)); }, [id]);

  if (hata) return <p className="hata sayfa">{hata}</p>;
  if (!s) return <p className="orta">Yükleniyor…</p>;

  return (
    <div className="sayfa">
      <p><Link to="/">← Sınıflarım</Link></p>
      <h1>{s.ad}</h1>
      <p className="soluk">{s.ders} · {s.sinif_duzeyi}. sınıf</p>
      {s.kod && (
        <div className="kart vurgu">
          <span>Öğrencilerin bu kodla katılır:</span>
          <span className="buyuk-kod">{s.kod}</span>
        </div>
      )}
      <p><Link className="dugme" to={`/sinif/${id}/rapor`}>📊 Sınıf raporu (MK ısı haritası)</Link></p>
      <section className="kart">
        <h2>Öğrenciler ({s.ogrenciler.length})</h2>
        {s.ogrenciler.length === 0 ? <p className="soluk">Henüz katılan öğrenci yok.</p> : (
          <table>
            <thead><tr><th>Ad</th><th>E-posta</th><th>Katılma</th></tr></thead>
            <tbody>
              {s.ogrenciler.map((o) => (
                <tr key={o.id}><td><Link to={`/sinif/${id}/ogrenci/${o.id}`}>{o.ad}</Link></td><td>{o.eposta}</td><td>{new Date(o.katilma).toLocaleDateString("tr-TR")}</td></tr>
              ))}
            </tbody>
          </table>
        )}
      </section>
    </div>
  );
}
