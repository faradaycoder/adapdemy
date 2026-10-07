import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api, RAPOR_DURUMU, type OgrenciRaporT, type VideoT } from "../api";
import { KonuKart } from "./OgrenciSonuc";

// Öğrencinin MK raporu. Öğretmen sınıf sayfasından (MK kodlarıyla), öğrenci kendi ana sayfasından (video kartlarıyla) açar.
export default function OgrenciRapor() {
  const { id, oid } = useParams();
  const ogretmen = Boolean(id);
  const [r, setR] = useState<OgrenciRaporT | null>(null);
  const [hata, setHata] = useState("");
  const [acikId, setAcikId] = useState<number | null>(null);

  useEffect(() => {
    api<OgrenciRaporT>(ogretmen ? `/api/siniflar/${id}/ogrenciler/${oid}/rapor` : "/api/rapor").then(setR).catch((e) => setHata(e.message));
  }, [id, oid, ogretmen]);

  if (hata) return <p className="hata sayfa">{hata}</p>;
  if (!r) return <p className="orta">Yükleniyor…</p>;
  const say = (d: string) => r.mkler.filter((m) => m.durum === d).length;
  const ac = (v: VideoT | null) => {
    setAcikId(v?.id ?? null);
    if (v) api(`/api/video/${v.id}/izle`, { method: "POST", govde: {} }).catch(() => {});
  };

  return (
    <div className="sayfa">
      <p>{ogretmen ? <Link to={`/sinif/${id}/rapor`}>← Sınıf raporu</Link> : <Link to="/">← Ana sayfa</Link>}</p>
      <h1>{ogretmen ? r.ogrenci : "Konu raporum"}</h1>
      <p className="soluk">{r.teslim} sınavdan · {say("biliyor")} biliyor, {say("belirsiz")} belirsiz, {say("bilmiyor")} bilmiyor
        {say("olculemedi") ? `, ${say("olculemedi")} ölçülemedi` : ""}</p>
      {r.mkler.length === 0 ? <section className="kart"><p className="soluk">Henüz açıklanmış sınav sonucu yok.</p></section> : (
        <section className="kart">
          {r.mkler.map((m) => (
            <div key={m.kod} className="rapor-mk">
              <div className="rapor-mk-ust">
                <span className={`adim-durum ${m.durum}`}>{RAPOR_DURUMU[m.durum]}</span>
                <span>{m.ifade}</span>
              </div>
              <small className="soluk">
                {ogretmen && <><Link to={`/mk/${m.kod}`}><code>{m.kod}</code></Link> · </>}
                {m.dogru} doğru, {m.yanlis} yanlış{m.olculemedi ? `, ${m.olculemedi} boş` : ""}
                {m.p != null && ` · biliyor olasılığı %${Math.round(m.p * 100)}`}
              </small>
              {!ogretmen && m.konu && <KonuKart k={m.konu} acikId={acikId} ac={ac} />}
            </div>
          ))}
        </section>
      )}
      {r.yanilgilar.length > 0 && (
        <section className="kart">
          <h2>{ogretmen ? "Yanılgılar" : "Dikkat etmen gereken yanlış düşünceler"}</h2>
          <ul>{r.yanilgilar.map((y) => <li key={y.kod}>{y.ifade}{ogretmen && <> <code>{y.kod}</code></>}{y.sayi > 1 && ` (${y.sayi} kez)`}</li>)}</ul>
        </section>
      )}
    </div>
  );
}
