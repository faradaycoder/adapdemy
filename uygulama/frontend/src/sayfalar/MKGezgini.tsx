import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api, type MKAyrinti, type MKKisa } from "../api";

function MKSatir({ m }: { m: MKKisa }) {
  return (
    <Link to={`/mk/liste/${m.kod}`} className="mk-satir">
      <code>{m.kod}</code>
      <span className="ifade">{m.ifade}</span>
      <span className="etiket">{m.islem_turu}</span>
      {m.zorluk != null && <span className={`seviye s${Math.min(m.seviye ?? 1, 7)}`}>Z {m.zorluk.toFixed(2)} · S{m.seviye}</span>}
    </Link>
  );
}

export default function MKGezgini() {
  const { kod } = useParams();
  const [ders, setDers] = useState("Fizik");
  const [sinif, setSinif] = useState("");
  const [q, setQ] = useState("");
  const [liste, setListe] = useState<MKKisa[]>([]);
  const [secili, setSecili] = useState<MKAyrinti | null>(null);
  const [hata, setHata] = useState("");

  useEffect(() => {
    const p = new URLSearchParams({ ders, limit: "200" });
    if (sinif) p.set("sinif", sinif);
    if (q.trim()) p.set("q", q.trim());
    const t = setTimeout(() => api<MKKisa[]>(`/api/mk?${p}`).then(setListe).catch((e) => setHata(e.message)), 250);
    return () => clearTimeout(t);
  }, [ders, sinif, q]);

  useEffect(() => {
    if (!kod) { setSecili(null); return; }
    api<MKAyrinti>(`/api/mk/${kod}`).then(setSecili).catch((e) => setHata(e.message));
  }, [kod]);

  return (
    <div className="sayfa mk-duzen">
      <section>
        <div className="baslik-satiri"><h1>MK listesi</h1><Link to="/mk" className="dugme ikincil">🗺️ Haritaya dön</Link></div>
        <div className="satir">
          <label>Ders<select value={ders} onChange={(e) => { setDers(e.target.value); setSinif(""); }}><option>Fizik</option><option>Matematik</option></select></label>
          <label>Sınıf<select value={sinif} onChange={(e) => setSinif(e.target.value)}>
            <option value="">Hepsi</option>
            {(ders === "Fizik" ? [9, 10, 11, 12] : [5, 6, 7, 8, 9, 10, 11, 12]).map((d) => <option key={d}>{d}</option>)}
          </select></label>
          <label>Ara<input value={q} onChange={(e) => setQ(e.target.value)} placeholder="kod ya da ifade" /></label>
        </div>
        {hata && <p className="hata">{hata}</p>}
        <p className="soluk">{liste.length === 200 ? "İlk 200 sonuç" : `${liste.length} MK`}</p>
        <div className="mk-liste">{liste.map((m) => <MKSatir key={m.kod} m={m} />)}</div>
      </section>

      {secili && (
        <aside className="kart mk-ayrinti">
          <code>{secili.kod}</code>
          <h2>{secili.ifade}</h2>
          <dl>
            <dt>Tür</dt><dd>{secili.tur} · {secili.bilissel_duzey}</dd>
            <dt>İşlem türü</dt><dd>{secili.islem_turu} (v = {secili.v})</dd>
            <dt>Zorluk</dt><dd>{secili.zorluk?.toFixed(2)} · Seviye {secili.seviye}</dd>
            <dt>Ölçme</dt><dd>{secili.olcme_turleri} · {secili.ustalik_olcutu}</dd>
            <dt>Kazanımlar</dt><dd>{secili.eslemeler.map((e) => `${e.ogrenme_ciktisi} (${e.surec_bileseni})`).join(", ")}</dd>
          </dl>
          <h3>Ön koşullar ({secili.on_kosullar.length})</h3>
          {secili.on_kosullar.length ? secili.on_kosullar.map((m) => <MKSatir key={m.kod} m={m} />)
            : <p className="soluk">Kök MK. {secili.on_kosul_diger}</p>}
          <h3>Bu MK'ye dayananlar ({secili.ardillar.length})</h3>
          {secili.ardillar.map((m) => <MKSatir key={m.kod} m={m} />)}
          {secili.yanilgilar.length > 0 && (<>
            <h3>Yanılgılar</h3>
            <ul>{secili.yanilgilar.map((y) => <li key={y.kod}><code>{y.kod}</code> {y.ifade}</li>)}</ul>
          </>)}
        </aside>
      )}
    </div>
  );
}
