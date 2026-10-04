import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api, tarihSaat, TESLIM_DURUMU, type TeslimAyrinti, type TeslimSatir } from "../api";

// Öğretmen: bir atamadaki öğrencilerin teslim durumu ve cevapları (değerlendirme E aşamasında eklenecek).
export default function Teslimler() {
  const { atamaId } = useParams();
  const [satirlar, setSatirlar] = useState<TeslimSatir[]>([]);
  const [secili, setSecili] = useState<TeslimAyrinti | null>(null);
  const [hata, setHata] = useState("");

  useEffect(() => { api<TeslimSatir[]>(`/api/atamalar/${atamaId}/teslimler`).then(setSatirlar).catch((e) => setHata(e.message)); }, [atamaId]);

  async function ac(id: number) {
    try { setSecili(await api<TeslimAyrinti>(`/api/atamalar/${atamaId}/teslimler/${id}`)); } catch (e) { setHata((e as Error).message); }
  }

  return (
    <div className="sayfa">
      <p><Link to="/sinavlar">← Sınavlar</Link></p>
      <h1>Teslimler</h1>
      {hata && <p className="hata">{hata}</p>}
      <table>
        <thead><tr><th>Öğrenci</th><th>Durum</th><th>Cevaplanan</th><th>Teslim</th><th>Puan</th><th></th></tr></thead>
        <tbody>
          {satirlar.map((s) => (
            <tr key={s.ogrenci_id}>
              <td>{s.ogrenci}</td>
              <td><span className={`durum ${s.durum === "teslim" ? "onayli" : ""}`}>{TESLIM_DURUMU[s.durum]}</span></td>
              <td>{s.cevaplanan}/{s.soru_sayisi}{s.genel_dosya > 0 && <span className="soluk"> · tüm kâğıt: {s.genel_dosya} dosya</span>}</td>
              <td>{s.teslim_zamani ? tarihSaat(s.teslim_zamani) : "–"}</td>
              <td>{s.degerlendirme === "onayli" ? <b>{s.puan?.toFixed(2)} / {s.en_yuksek?.toFixed(2)}</b> : s.degerlendirme === "bekliyor" ? <span className="durum">Değerlendirilecek</span> : "–"}</td>
              <td className="kucuk-dugmeler">
                {s.teslim_id && s.durum === "teslim" && <Link className="dugme" to={`/atama/${atamaId}/teslimler/${s.teslim_id}`}>{s.degerlendirme === "onayli" ? "İncele" : "Değerlendir"}</Link>}
                {s.teslim_id && <button className="ikincil kucuk" onClick={() => ac(s.teslim_id!)}>Cevaplar</button>}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      {satirlar.length === 0 && <p className="soluk">Bu sınıfta öğrenci yok.</p>}

      {secili && (
        <section className="kart">
          <h2>{secili.ogrenci} · {TESLIM_DURUMU[secili.durum]}</h2>
          {secili.sorular.map((q) => {
            const c = secili.cevaplar.find((x) => x.soru_id === q.soru_id);
            return (
              <div key={q.soru_id} className="t-cevap">
                <strong>Soru {q.sira}</strong>
                {c?.secilen && <span> · İşaretlediği şık: <b>{c.secilen}</b></span>}
                {c?.metin && <p className="t-metin">{c.metin}</p>}
                <div className="o-dosyalar">{c?.dosyalar.map((d) => (
                  <a key={d.id} href={`/api/gorsel/${d.dosya}`} target="_blank" className="o-dosya">
                    {d.dosya.endsWith(".pdf") ? "PDF" : <img src={`/api/gorsel/${d.dosya}`} alt="Çözüm" />}
                  </a>
                ))}</div>
                {!c && <span className="soluk"> · cevap yok</span>}
              </div>
            );
          })}
        </section>
      )}
    </div>
  );
}
