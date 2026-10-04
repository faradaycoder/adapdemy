import { useState } from "react";
import { Link } from "react-router-dom";
import { api, type Soru } from "./api";

// Sorunun çözüm rubriği: doğru cevap, çözüm ve adım adım rubrik (adım → MK, puan).
export function RubrikTablo({ s }: { s: Soru }) {
  const z = s.eslesme.zorluk ?? s.zorluk ?? 0;
  return (
    <div className="rubrik-detay">
      <p><b>Doğru cevap:</b> {s.cevap_bicimi === "coktan_secmeli" ? s.secenekler.find((x) => x.dogru)?.harf : s.dogru_cevap}</p>
      {s.cozum && <div className="cozum-kutu"><h3>Çözüm</h3><p className="t-metin">{s.cozum}</p></div>}
      <table className="rubrik">
        <thead><tr><th>#</th><th>Rubrik adımı (öğrenci ne yapmalı)</th><th>MK</th><th>Puan</th></tr></thead>
        <tbody>
          {s.eslesme.adimlar.map((a, i) => (
            <tr key={i}>
              <td>{i + 1}</td>
              <td>{a.aciklama}</td>
              <td><Link to={`/mk/${a.mk_kod}`} onClick={(e) => e.stopPropagation()}><code>{a.mk_kod}</code></Link>
                {a.mk && <small className="soluk"> {a.mk.ifade}{a.soru_mk_mi ? "" : " (ön koşul)"}</small>}</td>
              <td className="sayi">{(a.pay * z).toFixed(2)}</td>
            </tr>
          ))}
        </tbody>
        <tfoot><tr><td colSpan={3}>Toplam</td><td className="sayi"><b>{z.toFixed(2)}</b></td></tr></tfoot>
      </table>
    </div>
  );
}

// Liste içinde açılır "Çözüm ve rubrik": soru ilk açılışta getirilir.
export function RubrikAkordeon({ soruId }: { soruId: number }) {
  const [acik, setAcik] = useState(false);
  const [s, setS] = useState<Soru | null>(null);
  const [hata, setHata] = useState("");
  function ac(e: React.MouseEvent) {
    e.preventDefault(); e.stopPropagation();
    if (!acik && !s) api<Soru>(`/api/sorular/${soruId}`).then(setS).catch((x) => setHata(x.message));
    setAcik(!acik);
  }
  return (
    <div className={`mk-akordeon ${acik ? "acik" : ""}`}>
      <button type="button" className="mk-akordeon-baslik rubrik-baslik" aria-expanded={acik} onClick={ac}>
        <span className="ok">{acik ? "▾" : "▸"}</span><span>Çözüm ve rubrik</span>
      </button>
      {acik && (
        <div className="mk-akordeon-icerik" onClick={(e) => e.stopPropagation()}>
          {hata ? <p className="hata">{hata}</p> : s ? <RubrikTablo s={s} /> : <p className="soluk">Yükleniyor…</p>}
        </div>
      )}
    </div>
  );
}
