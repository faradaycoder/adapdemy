import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { api, type SinavKisa } from "../api";

export default function Sinavlar() {
  const [sinavlar, setSinavlar] = useState<SinavKisa[]>([]);
  const [hata, setHata] = useState("");

  useEffect(() => { api<SinavKisa[]>("/api/sinavlar").then(setSinavlar).catch((e) => setHata(e.message)); }, []);

  return (
    <div className="sayfa">
      <div className="baslik-satiri">
        <h1>Sınavlar</h1>
        <Link to="/sinavlar/yeni" className="dugme">+ Yeni sınav</Link>
      </div>
      {hata && <p className="hata">{hata}</p>}
      {sinavlar.length === 0 ? (
        <p className="soluk">Henüz sınav yok. "Yeni sınav" ile bankadaki onaylı sorulardan bir sınav oluştur.</p>
      ) : (
        <div className="izgara">
          {sinavlar.map((s) => (
            <Link key={s.id} to={`/sinavlar/${s.id}`} className="kart sinif">
              <strong>{s.ad}</strong>
              <span>{s.ders} · {s.sinif_duzeyi}. sınıf</span>
              <span>{s.soru_sayisi} soru · toplam zorluk {s.toplam_zorluk.toFixed(2)}</span>
              <span className="soluk">{s.atama_sayisi ? `${s.atama_sayisi} sınıfa atandı` : "Atanmadı"}</span>
            </Link>
          ))}
        </div>
      )}
    </div>
  );
}
