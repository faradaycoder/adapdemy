import { useEffect, useRef, useState } from "react";
import { Link, useLocation } from "react-router-dom";
import { api, tarihSaat, type Bildirimler } from "./api";
import { useOturum } from "./oturum";

// Üst çubuktaki bildirim zili. 30 saniyede bir ve sayfa değiştikçe yenilenir.
export default function Zil() {
  const { kullanici } = useOturum();
  const konum = useLocation();
  const [b, setB] = useState<Bildirimler>({ sayi: 0, ogeler: [] });
  const [acik, setAcik] = useState(false);
  const kutu = useRef<HTMLDivElement>(null);

  const yukle = () => api<Bildirimler>("/api/bildirimler").then(setB).catch(() => {});
  useEffect(() => { if (kullanici) yukle(); }, [kullanici, konum.pathname]);
  useEffect(() => { const t = setInterval(yukle, 30000); return () => clearInterval(t); }, []);
  useEffect(() => {
    const kapat = (e: MouseEvent) => { if (kutu.current && !kutu.current.contains(e.target as Node)) setAcik(false); };
    document.addEventListener("mousedown", kapat);
    return () => document.removeEventListener("mousedown", kapat);
  }, []);

  async function tumunuOku() {
    await api("/api/bildirimler/okundu", { method: "POST" });
    yukle();
  }

  return (
    <div className="zil" ref={kutu}>
      <button className="ikincil zil-dugme" onClick={() => setAcik(!acik)} aria-label={`${b.sayi} bildirim`}>
        🔔{b.sayi > 0 && <span className="rozet">{b.sayi}</span>}
      </button>
      {acik && (
        <div className="zil-liste kart">
          <strong>{b.sayi ? `${b.sayi} bildirim` : "Yeni bildirim yok"}</strong>
          {b.ogeler.map((o, i) => (
            <Link key={i} to={o.baglanti} className="zil-oge" onClick={() => setAcik(false)}>
              <span>{o.metin}</span>
              <small className="soluk">{o.son ? `Son: ${tarihSaat(o.son)}` : tarihSaat(o.zaman)}</small>
            </Link>
          ))}
          {kullanici?.rol === "ogretmen" && b.sayi > 0 && <button className="ikincil kucuk" onClick={tumunuOku}>Tümünü okundu say</button>}
        </div>
      )}
    </div>
  );
}
