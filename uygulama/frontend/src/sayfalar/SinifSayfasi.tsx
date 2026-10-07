import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api, ATAMA_DURUMU, tarihSaat, type AtamaT, type SinifAyrinti } from "../api";

export default function SinifSayfasi() {
  const { id } = useParams();
  const [s, setS] = useState<SinifAyrinti | null>(null);
  const [hata, setHata] = useState("");
  const [atamalar, setAtamalar] = useState<AtamaT[]>([]);

  useEffect(() => {
    api<SinifAyrinti>(`/api/siniflar/${id}`).then(setS).catch((e) => setHata(e.message));
    api<AtamaT[]>("/api/atamalar").then((x) => setAtamalar(x.filter((a) => a.sinif_id === Number(id)))).catch(() => {});
  }, [id]);

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
      <section className="kart">
        <div className="baslik-satiri"><h2>Sınavlar ve değerlendirme</h2><Link className="dugme" to={`/sinif/${id}/rapor`}>📊 Sınıf raporu</Link></div>
        {atamalar.length === 0 ? <p className="soluk">Bu sınıfa henüz sınav atanmadı. <Link to="/sinavlar">Sınavlar</Link> sayfasından bir sınavı açıp "Sınıfa ata" ile atayabilirsin.</p> : (
          <div className="liste">
            {atamalar.map((a) => {
              const bekleyen = (a.teslim ?? 0) - (a.degerlendirilen ?? 0);
              return (
                <div key={a.id} className="liste-satir">
                  <div>
                    <strong>{a.sinav_adi}</strong> <span className={`durum ${a.durum === "acik" ? "onayli" : ""}`}>{ATAMA_DURUMU[a.durum]}</span><br />
                    <small>{tarihSaat(a.baslangic)} – {tarihSaat(a.bitis)} · {a.teslim ?? 0}/{a.ogrenci ?? 0} teslim · {a.degerlendirilen ?? 0} değerlendirildi</small>
                    <div className="ilerleme"><span style={{ width: `${a.ogrenci ? ((a.degerlendirilen ?? 0) / a.ogrenci) * 100 : 0}%` }} /></div>
                  </div>
                  <div className="kucuk-dugmeler">
                    {bekleyen > 0 && <span className="durum">{bekleyen} bekliyor</span>}
                    <Link className={bekleyen > 0 ? "dugme" : "dugme ikincil"} to={`/atama/${a.id}/teslimler`}>{bekleyen > 0 ? "Değerlendir" : "Teslimler"}</Link>
                  </div>
                </div>
              );
            })}
          </div>
        )}
      </section>
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
