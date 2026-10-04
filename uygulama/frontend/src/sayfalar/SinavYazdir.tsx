import { useEffect, useState } from "react";
import { Link, useParams, useSearchParams } from "react-router-dom";
import { api, type Yazdir } from "../api";
import Qr from "../Qr";

// Yazdırılabilir sınav. Atamalı açılırsa sınıftaki her öğrenci için ayrı kopya üretilir.
// Her sorunun yanındaki QR kod, taranan sayfanın hangi öğrenci, atama ve soruya ait olduğunu söyler:
//   EVALORA:A<atama>:O<öğrenci>:S<soru>   (öğrenciye özel kopya)
//   EVALORA:X<sınav>:S<soru>              (boş kopya; öğrenci yüklerken kendini seçer)
// Öğrenci kipi (/sinav/:atamaId/yazdir): önce sınav başlatılır (süre işlemeye başlar), sonra öğrencinin kendi kopyası gelir.
export default function SinavYazdir() {
  const { id, atamaId } = useParams();
  const [p] = useSearchParams();
  const atama = p.get("atama");
  const [v, setV] = useState<Yazdir | null>(null);
  const [hata, setHata] = useState("");

  useEffect(() => {
    const yukle = atamaId
      ? api(`/api/teslim/${atamaId}/basla`, { method: "POST" }).then(() => api<Yazdir>(`/api/teslim/${atamaId}/yazdir`))
      : api<Yazdir>(`/api/sinavlar/${id}/yazdir${atama ? `?atama_id=${atama}` : ""}`);
    yukle.then(setV).catch((e) => setHata(e.message));
  }, [id, atama, atamaId]);

  if (hata) return <p className="hata sayfa">{hata}</p>;
  if (!v) return <p className="orta">Hazırlanıyor…</p>;

  const kopyalar = v.ogrenciler.length ? v.ogrenciler : [null];

  return (
    <div className="yazdir">
      <div className="yazdirma-cubugu">
        {atamaId
          ? <span>Kâğıtta çöz, sonra sayfaları tara ya da fotoğrafla ve <Link to={`/sinav/${atamaId}`}>sınav sayfasında</Link> "Sınavın tamamını tek seferde yükle" bölümünden yükle. Süren işliyor.</span>
          : <span>{v.ogrenciler.length ? `${v.ogrenciler.length} öğrenci kopyası (${v.sinif_adi})` : "Boş kopya"} · {v.sorular.length} soru</span>}
        <button onClick={() => window.print()}>Yazdır / PDF olarak kaydet</button>
      </div>
      {kopyalar.map((o, n) => (
        <section key={o?.id ?? "bos"} className={`kopya ${n > 0 ? "yeni-sayfa" : ""}`}>
          <header className="kopya-ust">
            <div>
              <h1>{v.ad}</h1>
              <p>{v.ders} · {v.sinif_duzeyi}. sınıf{v.sinif_adi ? ` · ${v.sinif_adi}` : ""}{v.sure_dk ? ` · ${v.sure_dk} dakika` : ""}</p>
              {v.aciklama && <p className="soluk">{v.aciklama}</p>}
            </div>
            <div className="ogrenci-alani">{o ? <strong>{o.ad}</strong> : <>Ad soyad: ______________________<br />Numara: __________</>}</div>
          </header>
          {v.sorular.map((q) => (
            <article key={q.soru_id} className="y-soru">
              <div className="y-soru-ust">
                <strong>{q.sira}.</strong>
                <Qr veri={o && v.atama_id ? `EVALORA:A${v.atama_id}:O${o.id}:S${q.soru_id}` : `EVALORA:X${v.sinav_id}:S${q.soru_id}`} />
              </div>
              {q.gorsel && !q.gorsel.endsWith(".pdf")
                ? <img src={`/api/gorsel/${q.gorsel}`} alt={`Soru ${q.sira}`} />
                : <p>{q.metin}</p>}
              {q.secenekler.length > 0 && !q.gorsel && (
                <div className="y-secenekler">{q.secenekler.map((s) => <span key={s.harf}>{s.harf}) {s.metin}</span>)}</div>
              )}
              {q.cevap_bicimi === "coktan_secmeli"
                ? <div className="y-isaret">Cevap: {q.secenekler.map((s) => <span key={s.harf} className="daire">{s.harf}</span>)}</div>
                : <div className="y-cozum-alani">Çözüm:</div>}
            </article>
          ))}
        </section>
      ))}
    </div>
  );
}
