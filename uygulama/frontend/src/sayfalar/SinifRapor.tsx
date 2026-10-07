import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api, RAPOR_DURUMU, type SinifRaporT } from "../api";

// Sınıf raporu: öğrenci × MK ısı haritası (onaylanmış sınavlardan), MK MK sınıf durumu ve yanılgı dağılımı.
export default function SinifRapor() {
  const { id } = useParams();
  const [r, setR] = useState<SinifRaporT | null>(null);
  const [hata, setHata] = useState("");

  useEffect(() => { api<SinifRaporT>(`/api/siniflar/${id}/rapor`).then(setR).catch((e) => setHata(e.message)); }, [id]);

  if (hata) return <p className="hata sayfa">{hata}</p>;
  if (!r) return <p className="orta">Yükleniyor…</p>;
  const kisa = (kod: string) => kod.replace(/^([A-Z][a-z]{2})(\d\d)MK0*/, "$1$2·");

  return (
    <div className="sayfa genis">
      <p><Link to={`/sinif/${id}`}>← {r.sinif}</Link></p>
      <h1>Sınıf raporu</h1>
      <p className="soluk">{r.ders} · {r.sinif_duzeyi}. sınıf · Yalnız onayladığın sınav sonuçları sayılır. Bir MK için kanıt yetmediğinde
        durum "belirsiz" olur: o MK'yi ölçen bir soru daha sorulmalı.</p>
      {r.mkler.length === 0 ? <section className="kart"><p className="soluk">Henüz onaylanmış sınav sonucu yok.</p></section> : <>
        <section className="kart">
          <h2>Isı haritası</h2>
          <div className="lejant">{Object.entries(RAPOR_DURUMU).map(([k, v]) => <span key={k}><i className={`hucre ${k}`} /> {v}</span>)}</div>
          <div className="isi-kap">
            <table className="isi">
              <thead><tr><th>Öğrenci</th>{r.mkler.map((m) => <th key={m.kod} title={`${m.kod}: ${m.ifade}`}><Link to={`/mk/${m.kod}`}>{kisa(m.kod)}</Link></th>)}</tr></thead>
              <tbody>
                {r.ogrenciler.map((o) => (
                  <tr key={o.id}>
                    <td className="ad"><Link to={`/sinif/${id}/ogrenci/${o.id}`}>{o.ad}</Link> <small className="soluk">{o.teslim} sınav</small></td>
                    {r.mkler.map((m) => {
                      const h = o.mkler[m.kod];
                      const d = h?.durum ?? "olculemedi";
                      return <td key={m.kod} className={`hucre ${d}`} title={`${o.ad} · ${m.kod}: ${RAPOR_DURUMU[d]}${h?.p != null ? ` (%${Math.round(h.p * 100)})` : ""}`} />;
                    })}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>
        <section className="kart">
          <h2>MK'ler (temelden üste)</h2>
          <table>
            <thead><tr><th>MK</th><th>Sınıfın durumu</th></tr></thead>
            <tbody>
              {r.mkler.map((m) => {
                const n = r.ogrenciler.length || 1;
                return (
                  <tr key={m.kod}>
                    <td><Link to={`/mk/${m.kod}`}><code>{m.kod}</code></Link> <small>{m.ifade}</small></td>
                    <td className="cubuk-hucre">
                      <div className="cubuk">{(["biliyor", "belirsiz", "bilmiyor", "olculemedi"] as const).map((k) => m[k] > 0 &&
                        <span key={k} className={`hucre ${k}`} style={{ width: `${(m[k] / n) * 100}%` }} title={`${RAPOR_DURUMU[k]}: ${m[k]}`}>{m[k]}</span>)}</div>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </section>
      </>}
      <section className="kart">
        <h2>Yanılgılar</h2>
        {r.yanilgilar.length === 0 ? <p className="soluk">Çeldiricilerden yanılgı kaydı yok.</p> : (
          <table>
            <thead><tr><th>Yanılgı</th><th>Öğrenci</th></tr></thead>
            <tbody>{r.yanilgilar.map((y) => <tr key={y.kod}><td><code>{y.kod}</code> {y.ifade}</td><td>{y.sayi} · <small>{y.ogrenciler.join(", ")}</small></td></tr>)}</tbody>
          </table>
        )}
      </section>
    </div>
  );
}
