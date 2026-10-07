import { useState } from "react";
import { Link, useParams } from "react-router-dom";

// MK ön koşul haritası (araclar/harita_uret.py'nin ürettiği etkileşimli HTML) uygulama içinde. /mk/<KOD> ile açılınca
// harita o MK'yi seçer ve ortalar; ders koddan anlaşılır (Mat… / Fiz…).
const kodDersi = (kod?: string) => kod?.startsWith("Fiz") ? "Fizik" : kod?.startsWith("Mat") ? "Matematik" : null;

export default function MKHarita() {
  const { kod } = useParams();
  const [secilen, setSecilen] = useState<string>(() => {
    try { return localStorage.getItem("evalora_harita_ders") || "Matematik"; } catch { return "Matematik"; }
  });
  const ders = kodDersi(kod) ?? secilen;
  const sec = (d: string) => { setSecilen(d); try { localStorage.setItem("evalora_harita_ders", d); } catch { /* yok say */ } };
  return (
    <div className="mk-harita-sayfa">
      <div className="mk-harita-ust">
        <h1>MK haritası</h1>
        <div className="filtre-grup">
          {["Matematik", "Fizik"].map((d) => (
            kod && kodDersi(kod) !== d
              ? <Link key={d} to="/mk" onClick={() => sec(d)} className="filtre-cip-baglanti">{d}</Link>
              : <button key={d} type="button" className={`filtre-cip ${ders === d ? "aktif" : ""}`} aria-pressed={ders === d} onClick={() => sec(d)}>{d}</button>
          ))}
        </div>
        <span className="soluk mk-harita-ipucu">Kutuya tıkla: ön koşul zinciri ve dayananlar. Tekerlek: yakınlaştır · sürükle: kaydır · Ctrl+F: ara</span>
        <Link to="/mk/liste" className="dugme ikincil kucuk">☰ Liste görünümü</Link>
      </div>
      <iframe key={ders} className="mk-harita" title={`${ders} mikro kazanım haritası`} src={`/api/harita/${ders}${kod && kodDersi(kod) === ders ? `#${kod}` : ""}`} />
    </div>
  );
}
