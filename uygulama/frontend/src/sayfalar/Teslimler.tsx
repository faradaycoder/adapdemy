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

  async function karar(id: number, karar: "ver" | "reddet") {
    setHata("");
    const govde = karar === "ver" ? { karar, dk: Number(dk[id] ?? 10) } : { karar };
    try { setSatirlar(await api<TeslimSatir[]>(`/api/atamalar/${atamaId}/teslimler/${id}/uzatma`, { govde })); } catch (e) { setHata((e as Error).message); }
  }
  const [dk, setDk] = useState<Record<number, string>>({});
  const talepler = satirlar.filter((s) => s.uzatma === "bekliyor").length;

  async function ac(id: number) {
    try { setSecili(await api<TeslimAyrinti>(`/api/atamalar/${atamaId}/teslimler/${id}`)); } catch (e) { setHata((e as Error).message); }
  }

  return (
    <div className="sayfa">
      <p><Link to="/sinavlar">← Sınavlar</Link></p>
      <h1>Teslimler</h1>
      {hata && <p className="hata">{hata}</p>}
      {talepler > 0 && <p className="uzatma-bant">⏱ {talepler} öğrenci süre uzatma istiyor. Ek süreyi dakika olarak girip "Süre ver"e bas ya da reddet.</p>}
      <table>
        <thead><tr><th>Öğrenci</th><th>Durum</th><th>Cevaplanan</th><th>Teslim</th><th>Süre uzatma</th><th>Puan</th><th></th></tr></thead>
        <tbody>
          {satirlar.map((s) => (
            <tr key={s.ogrenci_id} className={s.uzatma === "bekliyor" ? "talep-var" : ""}>
              <td>{s.ogrenci}</td>
              <td><span className={`durum ${s.durum === "teslim" ? "onayli" : ""}`}>{TESLIM_DURUMU[s.durum]}</span>
                {s.otomatik_teslim && <> <span className="durum otomatik" title="Süre dolunca kendiliğinden teslim edildi">{s.cevaplanan || s.genel_dosya ? "Süre doldu" : "Boş kâğıt"}</span></>}</td>
              <td>{s.cevaplanan}/{s.soru_sayisi}{s.genel_dosya > 0 && <span className="soluk"> · tüm kâğıt: {s.genel_dosya} dosya</span>}</td>
              <td>{s.teslim_zamani ? tarihSaat(s.teslim_zamani) : "–"}</td>
              <td>{s.uzatma === "bekliyor" && s.teslim_id ? (
                <div className="uzatma-talep">
                  <b>Uzatma istiyor</b>{s.uzatma_notu && <q>{s.uzatma_notu}</q>}
                  <div className="satir-ic">
                    <input type="number" min={1} max={1440} value={dk[s.teslim_id] ?? "10"} aria-label="Ek süre (dakika)"
                      onChange={(e) => setDk({ ...dk, [s.teslim_id!]: e.target.value })} /> dk
                    <button className="kucuk" onClick={() => karar(s.teslim_id!, "ver")}>Süre ver</button>
                    <button className="ikincil kucuk" onClick={() => karar(s.teslim_id!, "reddet")}>Reddet</button>
                  </div>
                </div>
              ) : s.uzatma === "verildi" ? <span className="soluk">+{s.uzatma_dk} dk verildi</span>
                : s.uzatma === "reddedildi" ? <span className="soluk">Reddedildi</span> : "–"}</td>
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
