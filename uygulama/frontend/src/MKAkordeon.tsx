import { useState } from "react";
import { Link } from "react-router-dom";
import type { SoruKisa } from "./api";

// Sorunun MK'leri: kapalıyken kodlar, tıklanınca açıklamalarıyla. Bağlantı içinde de çalışır (tıklama yukarı taşmaz).
export default function MKAkordeon({ q }: { q: SoruKisa }) {
  const [acik, setAcik] = useState(false);
  if (!q.mk_detay.length) return null;
  return (
    <div className={`mk-akordeon ${acik ? "acik" : ""}`}>
      <button type="button" className="mk-akordeon-baslik" aria-expanded={acik}
        onClick={(e) => { e.preventDefault(); e.stopPropagation(); setAcik(!acik); }}>
        <span className="ok">{acik ? "▾" : "▸"}</span>
        <span>Ölçtüğü MK'ler ({q.mk_detay.length})</span>
        {!acik && q.mk_detay.map((m) => <code key={m.kod} title={m.ifade} className={m.kod === q.birincil ? "birincil" : ""}>{m.kod}</code>)}
      </button>
      {acik && (
        <div className="mk-akordeon-icerik" onClick={(e) => e.stopPropagation()}>
          <ul>
            {q.mk_detay.map((m) => (
              <li key={m.kod}>
                <Link to={`/mk/${m.kod}`} onClick={(e) => e.stopPropagation()}><code className={m.kod === q.birincil ? "birincil" : ""}>{m.kod}</code></Link>
                <span>{m.ifade}</span>
                {m.zorluk != null && <small className="soluk">Z {m.zorluk.toFixed(2)}</small>}
              </li>
            ))}
          </ul>
          {q.onkosul_detay.length > 0 && (<>
            <p className="soluk mk-akordeon-alt">Rubrikte teşhis için geçen ön koşullar:</p>
            <ul className="onkosul">
              {q.onkosul_detay.map((m) => (
                <li key={m.kod}>
                  <Link to={`/mk/${m.kod}`} onClick={(e) => e.stopPropagation()}><code>{m.kod}</code></Link>
                  <span>{m.ifade}</span>
                </li>
              ))}
            </ul>
          </>)}
        </div>
      )}
    </div>
  );
}
