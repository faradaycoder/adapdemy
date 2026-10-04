import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import MKAkordeon from "../MKAkordeon";
import { RubrikAkordeon } from "../Rubrik";
import { api, CEVAP_BICIMLERI, type SoruKisa } from "../api";

export default function SoruBankasi() {
  const [sorular, setSorular] = useState<SoruKisa[]>([]);
  const [ders, setDers] = useState("");
  const [durum, setDurum] = useState("");
  const [mk, setMk] = useState("");
  const [hata, setHata] = useState("");
  const [secili, setSecili] = useState<Set<number>>(new Set());
  const [yenile, setYenile] = useState(0);

  useEffect(() => {
    const p = new URLSearchParams();
    if (ders) p.set("ders", ders);
    if (durum) p.set("durum", durum);
    if (mk.trim()) p.set("mk", mk.trim());
    api<SoruKisa[]>(`/api/sorular?${p}`).then((l) => { setSorular(l); setSecili(new Set()); }).catch((e) => setHata(e.message));
  }, [ders, durum, mk, yenile]);

  const taslaklar = sorular.filter((s) => s.durum === "taslak");

  function sec(id: number) {
    const y = new Set(secili);
    y.has(id) ? y.delete(id) : y.add(id);
    setSecili(y);
  }

  async function onayla(idler: number[]) {
    setHata("");
    try {
      await api("/api/sorular/toplu-onayla", { govde: { idler } });
      setYenile(yenile + 1);
    } catch (e) { setHata((e as Error).message); }
  }

  return (
    <div className="sayfa">
      <div className="baslik-satiri">
        <h1>Soru bankası</h1>
        <Link to="/sorular/yukle" className="dugme">+ Soru ekle</Link>
      </div>
      <div className="satir">
        <label>Ders<select value={ders} onChange={(e) => setDers(e.target.value)}><option value="">Hepsi</option><option>Fizik</option><option>Matematik</option></select></label>
        <label>Durum<select value={durum} onChange={(e) => setDurum(e.target.value)}><option value="">Hepsi</option><option value="taslak">Taslak</option><option value="onayli">Onaylı</option></select></label>
        <label>MK kodu<input value={mk} onChange={(e) => setMk(e.target.value)} placeholder="ör. Fiz04MK0133" /></label>
      </div>
      {taslaklar.length > 0 && (
        <div className="toplu">
          <label className="secenek"><input type="checkbox" checked={taslaklar.every((s) => secili.has(s.id))}
            onChange={(e) => setSecili(e.target.checked ? new Set(taslaklar.map((s) => s.id)) : new Set())} /> Tüm taslakları seç</label>
          <button disabled={secili.size === 0} onClick={() => onayla([...secili])}>Seçilenleri onayla ({secili.size})</button>
        </div>
      )}
      {hata && <p className="hata">{hata}</p>}
      {sorular.length === 0 ? (
        <p className="soluk">Henüz soru yok. "Soru ekle" ile bir soruyu fotoğraf, görsel ya da metin olarak yükle; sistem okur, çözer ve MK'lere eşler.</p>
      ) : (
        <div className="soru-liste">
          {sorular.map((s) => (
            <div key={s.id} className="soru-satir">
            {s.durum === "taslak" ? <input type="checkbox" aria-label="Onay için seç" checked={secili.has(s.id)} onChange={() => sec(s.id)} /> : <span className="bosluk" />}
            <Link to={`/sorular/${s.id}`} className="kart soru-kart">
              {s.gorsel && (s.gorsel.endsWith(".pdf") ? <span className="pdf-rozet">PDF</span> : <img src={`/api/gorsel/${s.gorsel}`} alt="" />)}
              <div>
                <p className="soru-metin">{s.metin}</p>
                <div className="etiketler">
                  <span className={`durum ${s.durum}`}>{s.durum === "onayli" ? "Onaylı" : "Taslak"}</span>
                  <span>{s.ders} · {s.sinif_duzeyi}. sınıf</span>
                  <span>{CEVAP_BICIMLERI[s.cevap_bicimi]}</span>
                  {s.zorluk != null && <span className="seviye">Zorluk {s.zorluk.toFixed(2)}</span>}
                </div>
                <MKAkordeon q={s} />
                <RubrikAkordeon soruId={s.id} />
              </div>
            </Link>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
