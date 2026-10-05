import { useEffect, useState } from "react";
import { Mat } from "../Mat";
import { Link, useParams } from "react-router-dom";
import { api, type Soru } from "../api";
import { RubrikTablo } from "../Rubrik";

type SinavT = { id: number; ad: string; ders: string; sinif_duzeyi: number; sure_dk: number | null; sorular: { id: number }[] };

// Sınavın tüm soruları için çözüm ve rubrik (öğretmen için; yazdırılabilir).
export default function SinavRubrik() {
  const { id } = useParams();
  const [sinav, setSinav] = useState<SinavT | null>(null);
  const [sorular, setSorular] = useState<Soru[]>([]);
  const [hata, setHata] = useState("");

  useEffect(() => {
    api<SinavT>(`/api/sinavlar/${id}`).then(async (v) => {
      setSinav(v);
      setSorular(await Promise.all(v.sorular.map((q) => api<Soru>(`/api/sorular/${q.id}`))));
    }).catch((e) => setHata(e.message));
  }, [id]);

  if (hata) return <p className="hata sayfa">{hata}</p>;
  if (!sinav) return <p className="orta">Hazırlanıyor…</p>;
  const toplam = sorular.reduce((t, s) => t + (s.eslesme.zorluk ?? s.zorluk ?? 0), 0);

  return (
    <div className="sayfa rubrik-sayfa">
      <div className="yazdirma-cubugu">
        <span><Link to={`/sinavlar/${id}`}>← Sınav</Link> · Öğretmen için: doğru cevaplar, çözümler ve rubrik</span>
        <button onClick={() => window.print()}>Yazdır / PDF olarak kaydet</button>
      </div>
      <h1>Rubrik · {sinav.ad}</h1>
      <p className="soluk">{sinav.ders} · {sinav.sinif_duzeyi}. sınıf{sinav.sure_dk ? ` · ${sinav.sure_dk} dakika` : ""} · {sinav.sorular.length} soru · toplam {toplam.toFixed(2)} puan</p>
      <p className="soluk">Her rubrik adımı bir MK'ye bağlıdır. Değerlendirmede her adım için: Biliyor (adım puanını alır), Bilmiyor (denedi, yanlış), Ölçülemedi (boş ya da o adıma gelmedi).</p>
      {sorular.map((s, i) => (
        <section key={s.id} className="kart rubrik-soru">
          <h2>{i + 1}. soru <small className="soluk">({(s.eslesme.zorluk ?? s.zorluk ?? 0).toFixed(2)} puan)</small></h2>
          {s.gorsel && !s.gorsel.endsWith(".pdf") ? <img src={`/api/gorsel/${s.gorsel}`} alt={`Soru ${i + 1}`} className="onizleme" /> : <p className="t-metin"><Mat metin={s.metin} /></p>}
          <RubrikTablo s={s} />
        </section>
      ))}
    </div>
  );
}
