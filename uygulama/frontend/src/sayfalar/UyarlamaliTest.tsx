import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { Mat, CozumMetni } from "../Mat";
import { api, gorselMi, type UyMKT, type UyOturumT, type VideoT } from "../api";
import { useOturum } from "../oturum";
import { KonuKart } from "./OgrenciSonuc";

const DURUM: Record<string, string> = { biliyor: "Biliyor", bilmiyor: "Bilmiyor", belirsiz: "Belirsiz", sorulmadi: "Sorulmadı" };

// MK satırı: olasılık çubuğu, durum ve (çıkarımsa) etiket. Öğretmen denemesinde canlı panel, sonuçta liste.
function MKSatir({ m, kok, son }: { m: UyMKT; kok: boolean; son: boolean }) {
  return (
    <li className={`uy-mk ${m.durum} ${son ? "son" : ""} ${m.cikarim || m.durum === "sorulmadi" ? "cikarim" : ""}`} title={m.ifade}>
      <code>{m.kod.replace("Mat01MK", "").replace(/^Fiz\d\dMK/, "")}</code>
      <span className="uy-mk-ifade">{m.ifade}</span>
      <span className="uy-cubuk" aria-hidden="true"><em style={{ width: `${Math.round(m.p * 100)}%` }} /></span>
      <span className="uy-mk-durum">
        <span className={`uy-d ${m.durum}`}>{DURUM[m.durum] ?? m.durum}</span>
        {m.cikarim && <small>çıkarım</small>}
        {kok && <small className="kok">kök</small>}
        {m.durum !== "sorulmadi" && !m.cikarim && <small className="soluk">%{Math.round(m.p * 100)}{m.soru_sayisi ? ` · ${m.soru_sayisi} soru` : ""}</small>}
        {m.onkosulu_eksik && m.durum !== "bilmiyor" && <small className="eksik">ön koşulu eksik</small>}
      </span>
    </li>
  );
}

export default function UyarlamaliTest() {
  const { id } = useParams();
  const { kullanici } = useOturum();
  const [o, setO] = useState<UyOturumT | null>(null);
  const [hata, setHata] = useState("");
  const [bekle, setBekle] = useState(false);
  const [acikId, setAcikId] = useState<number | null>(null);

  useEffect(() => { api<UyOturumT>(`/api/uyarlamali/${id}`).then(setO).catch((e) => setHata(e.message)); }, [id]);

  async function cevapla(harf: string) {
    if (bekle) return;
    setBekle(true); setHata("");
    try { setO(await api<UyOturumT>(`/api/uyarlamali/${id}/cevap`, { govde: { secilen: harf } })); }
    catch (e) { setHata((e as Error).message); } finally { setBekle(false); }
  }

  if (!o) return <div className="sayfa">{hata ? <p className="hata">{hata}</p> : <p className="soluk">Yükleniyor…</p>}</div>;
  const kendi = o.deneme ? kullanici?.rol === "ogretmen" : kullanici?.rol === "ogrenci";  // öğretmen öğrencinin testini yalnız izler
  const sonMK = o.gecmis.length ? o.gecmis[o.gecmis.length - 1].mk : null;
  const sira = ["bilmiyor", "belirsiz", "sorulmadi", "biliyor"];
  const siralı = [...o.mkler].sort((a, b) => sira.indexOf(a.durum) - sira.indexOf(b.durum) || a.kod.localeCompare(b.kod));

  const panel = o.mkler.length > 0 && (
    <aside className="kart uy-panel">
      <h3>Mikro kazanımlar <span className="soluk">({o.mkler.length})</span></h3>
      <p className="soluk kucuk-yazi">Çubuk: “biliyor” olasılığı. %95 ve üstü biliyor, %5 ve altı bilmiyor. Çıkarım: üstündeki MK bilindiği için sorulmadan “biliyor”.</p>
      <ul>{[...o.mkler].sort((a, b) => Number(b.kod === sonMK) - Number(a.kod === sonMK)
        || Number(b.soru_sayisi > 0 || b.cikarim) - Number(a.soru_sayisi > 0 || a.cikarim) || a.kod.localeCompare(b.kod)).map((m) => <MKSatir key={m.kod} m={m} kok={o.kokler.includes(m.kod)} son={m.kod === sonMK} />)}</ul>
    </aside>
  );

  if (o.durum === "devam" && o.soru) return (
    <div className={`sayfa uy-test ${o.mkler.length ? "panelli" : ""}`}>
      <div className="uy-ana">
        <div className="uy-ust">
          <Link to="/uyarlamali">← {o.deneme ? "Uyarlamalı test" : "Eksiğini bul"}</Link>
          <span className="soluk">{o.kazanim}{o.deneme ? " · deneme" : ""}</span>
        </div>
        <div className="uy-ilerleme" aria-label={`Soru ${o.sira}, en çok ${o.en_cok}`}>
          <span>Soru {o.sira}</span><span className="uy-ilerleme-cubuk"><em style={{ width: `${(o.sira / o.en_cok) * 100}%` }} /></span><span className="soluk">en çok {o.en_cok}</span>
        </div>
        <article className="kart uy-soru">
          {o.soru.gorsel && gorselMi(o.soru.gorsel) && <img src={`/api/gorsel/${o.soru.gorsel}`} alt="" className="onizleme" />}
          <p className="uy-soru-metin"><Mat metin={o.soru.metin} /></p>
          <div className="uy-siklar">
            {kendi && o.soru.secenekler.map((s) => (
              <button key={s.harf} className="uy-sik" disabled={bekle} onClick={() => cevapla(s.harf)}>
                <b>{s.harf}</b><span><Mat metin={s.metin} /></span>
              </button>
            ))}
          </div>
          {!kendi && <p className="soluk">Öğrenci bu soruda.</p>}
        </article>
        {hata && <p className="hata">{hata}</p>}
        {o.deneme && o.gecmis.length > 0 && (
          <ol className="uy-gecmis-kisa">{o.gecmis.map((g) => <li key={g.sira} className={g.dogru ? "d" : "y"}><code>{g.mk.replace("Mat01MK", "")}</code>{g.dogru ? "✓" : "✗"}</li>)}</ol>
        )}
      </div>
      {panel}
    </div>
  );

  return (
    <div className="sayfa uy-sonuc">
      <p><Link to="/uyarlamali">← {o.deneme ? "Uyarlamalı test" : "Eksiğini bul"}</Link></p>
      <div className="karsilama">
        <h1>{o.kokler.length ? "Eksiğinin kökü bulundu" : "Bu kazanımda eksik bulunmadı"}</h1>
        <p>{o.kazanim} · {o.kazanim_ifade} · {o.gecmis.length} soru</p>
      </div>
      {o.kokler.length > 0 && (
        <section className="kart uy-kokler">
          <h2>Önce bunları çalış</h2>
          <p className="soluk">Bu mikro kazanımları bilmiyorsun ama temelini biliyorsun. Bunlar düzelince üstlerindekiler de kolaylaşır.</p>
          <ul>{o.kokler.map((k) => { const m = o.mkler.find((x) => x.kod === k); return <li key={k}><code>{k}</code> {m?.ifade}</li>; })}</ul>
          {o.konular.length > 0 && (
            <div className="konu-liste">{o.konular.map((k) => <KonuKart key={k.konu} k={k} acikId={acikId} ac={(v: VideoT | null) => setAcikId(v?.id ?? null)} />)}</div>
          )}
        </section>
      )}
      <section className="kart">
        <h2>Mikro kazanımların durumu</h2>
        <ul className="uy-liste">{siralı.map((m) => <MKSatir key={m.kod} m={m} kok={o.kokler.includes(m.kod)} son={false} />)}</ul>
      </section>
      <section className="kart">
        <h2>Sorular ve çözümleri</h2>
        {o.gecmis.map((g) => (
          <details key={g.sira} className={`uy-gecmis ${g.dogru ? "d" : "y"}`}>
            <summary><b>{g.sira}.</b> <span className={`uy-d ${g.dogru ? "biliyor" : "bilmiyor"}`}>{g.dogru ? "Doğru" : "Yanlış"}</span> <code>{g.mk}</code> <span className="uy-gecmis-metin"><Mat metin={g.metin} /></span></summary>
            <p>Senin cevabın: <b>{g.secilen}</b>{!g.dogru && g.dogru_sik && <> · Doğru cevap: <b>{g.dogru_sik}</b></>}</p>
            {g.cozum && <div className="cozum-kutu"><CozumMetni metin={g.cozum} /></div>}
          </details>
        ))}
      </section>
    </div>
  );
}
