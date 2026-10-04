import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api, type OgrenciSonucT, type KonuKartiT, type OgrenciSoruT, type VideoT } from "../api";

// Öğrenci: öğretmenin onayladığı sonucu öğrenci diliyle görür. Rubrik, MK kodu ve adım puanı gösterilmez.
const DURUM = {
  dogru: { isaret: "✓", ad: "Doğru" },
  kismen: { isaret: "◐", ad: "Kısmen doğru" },
  yanlis: { isaret: "✗", ad: "Yanlış" },
  bos: { isaret: "–", ad: "Boş" },
};

function SeninCevabin({ s }: { s: OgrenciSoruT }) {
  if (s.cevap_bicimi === "coktan_secmeli")
    return <p className="t-metin">{s.secilen ? `${s.secilen}) ${s.secenekler.find((x) => x.harf === s.secilen)?.metin ?? ""}` : "Boş bıraktın."}</p>;
  return (
    <>
      {s.dosyalar.map((f) => (
        <figure key={f.id} className="el-yazisi">
          {f.dosya.endsWith(".pdf")
            ? <iframe src={`/api/gorsel/${f.dosya}`} title="Senin çözümün (PDF)" />
            : <a href={`/api/gorsel/${f.dosya}`} target="_blank" title="Büyütmek için tıkla"><img src={`/api/gorsel/${f.dosya}`} alt="Senin çözümün" /></a>}
        </figure>
      ))}
      {s.senin_cevabin ? <p className="t-metin">{s.senin_cevabin}</p> : !s.dosyalar.length && <p className="soluk">Boş bıraktın.</p>}
    </>
  );
}

const zaman = (s: number) => `${Math.floor(s / 60)}:${String(s % 60).padStart(2, "0")}`;
const dakika = (s: number) => Math.max(1, Math.round(s / 60));

// Eksik bir konu için kart: öğrenci "Konuyu dinle" (anlatım) ya da "Benzer soruyu gör" (soru çözümü) seçer.
// Video yalnız ilgili kısmı (başlangıç–bitiş) oynatır. Sayfada aynı anda tek video açık olur; başkası açılınca önceki kapanır.
function KonuKart({ k, acikId, ac }: { k: KonuKartiT; acikId: number | null; ac: (v: VideoT | null) => void }) {
  const acik = [k.anlatim, k.soru].find((v) => v && v.id === acikId) ?? null;
  const kutucuk = (v: VideoT | null, tur: "anlatim" | "soru") => v && (
    <button className={`video-kutu ${tur}`} onClick={() => ac(v)} aria-label={`${v.baslik} videosunu oynat`}>
      <span className="kapak">
        <img src={`https://i.ytimg.com/vi/${v.video_id}/${v.kapak}.jpg`} alt="" loading="lazy" />
        <span className="etiket">{tur === "anlatim" ? "📘 Konuyu dinle" : "✏️ Benzer soruyu gör"}</span>
        <span className="oynat">▶</span>
        <span className="sure">{dakika(v.son - v.bas)} dk</span>
      </span>
      <span className="kutu-alt"><b>{v.baslik}</b><small>{v.kanal}</small></span>
    </button>
  );
  return (
    <div className="konu-kart">
      <div className="konu-ust"><span className="konu-ikon">🎯</span><b>{k.konu}</b></div>
      {acik ? (
        <div className="oynatici">
          <iframe src={`https://www.youtube-nocookie.com/embed/${acik.video_id}?start=${acik.bas}&end=${acik.son}&autoplay=1&rel=0`}
            title={acik.baslik} allow="autoplay; encrypted-media; picture-in-picture" allowFullScreen />
          <div className="oynatici-alt">
            <div><b>{acik.baslik}</b><small className="soluk">{acik.kanal} · {zaman(acik.bas)}–{zaman(acik.son)}</small></div>
            <div className="eylemler">
              {acik === k.anlatim && k.soru && <button className="kucuk ikincil" onClick={() => ac(k.soru)}>✏️ Şimdi benzer soruyu gör</button>}
              {acik === k.soru && k.anlatim && <button className="kucuk ikincil" onClick={() => ac(k.anlatim)}>📘 Konuyu dinle</button>}
              <button className="kucuk ikincil" onClick={() => ac(null)}>Kapat</button>
            </div>
          </div>
        </div>
      ) : (
        <div className="video-kutular">{kutucuk(k.anlatim, "anlatim")}{kutucuk(k.soru, "soru")}</div>
      )}
    </div>
  );
}

// Çözüm metnini adımlara böler: cümle sonları ve "b)" gibi alt şık başları.
function adimlar(metin: string): string[] {
  return metin.split(/(?<=\.)\s+(?=[A-ZÇĞİÖŞÜ(]|[a-zçğıöşü]\()|\s+(?=[a-h]\)\s)/).map((x) => x.trim()).filter(Boolean);
}

function Cozum({ metin }: { metin: string }) {
  const a = adimlar(metin);
  return (
    <div className="cozum-kutu">
      <h3>✅ Doğru çözüm, adım adım</h3>
      {a.length > 1 ? <ol>{a.map((x, i) => <li key={i}>{x}</li>)}</ol> : <p className="t-metin">{metin}</p>}
    </div>
  );
}

export default function OgrenciSonuc() {
  const { atamaId } = useParams();
  const [d, setD] = useState<OgrenciSonucT | null>(null);
  const [hata, setHata] = useState("");
  const [acikId, setAcikId] = useState<number | null>(null);

  useEffect(() => { api<OgrenciSonucT>(`/api/teslim/${atamaId}/sonuc`).then(setD).catch((e) => setHata(e.message)); }, [atamaId]);

  if (hata) return <div className="sayfa"><p className="soluk">{hata}</p><Link to="/">← Ana sayfa</Link></div>;
  if (!d) return <p className="orta">Yükleniyor…</p>;
  const say = (x: string) => d.sorular.filter((s) => s.durum === x).length;
  const konuSayisi = d.sorular.reduce((t, s) => t + s.konular.length, 0);

  function ac(v: VideoT | null) {
    setAcikId(v?.id ?? null);
    if (v) api(`/api/video/${v.id}/izle`, { method: "POST", govde: { teslim_atama_id: Number(atamaId) } }).catch(() => {});
  }

  return (
    <div className="sayfa">
      <p><Link to="/">← Ana sayfa</Link></p>
      <div className="o-ust kart">
        <div>
          <h1>{d.sinav_adi}</h1>
          <p className="soluk">{d.sorular.length} sorudan {say("dogru")} doğru{say("kismen") ? `, ${say("kismen")} kısmen doğru` : ""}{say("yanlis") ? `, ${say("yanlis")} yanlış` : ""}{say("bos") ? `, ${say("bos")} boş` : ""}</p>
        </div>
        <span className="buyuk">{d.puan.toFixed(2)} <small className="soluk">/ {d.en_yuksek.toFixed(2)}</small></span>
      </div>
      {konuSayisi > 0 && <p className="video-ozet">🎬 Eksik kaldığın {konuSayisi} konu için kısa videolar hazır. Her sorunun altında, istersen konu anlatımını dinle, istersen benzer bir sorunun çözümünü izle.</p>}
      {d.genel_geri_bildirim && <section className="kart geri-bildirim"><h2>Öğretmeninden</h2><p className="t-metin">{d.genel_geri_bildirim}</p></section>}

      {d.sorular.map((s) => (
        <section key={s.sira} className="kart">
          <div className="baslik-satiri">
            <h2><span className={`sonuc-isaret ${s.durum}`}>{DURUM[s.durum].isaret}</span> Soru {s.sira} <small className="soluk">{DURUM[s.durum].ad}</small></h2>
            <span><b>{s.puan.toFixed(2)}</b> / {s.en_yuksek.toFixed(2)}</span>
          </div>
          {s.gorsel && !s.gorsel.endsWith(".pdf") ? <img src={`/api/gorsel/${s.gorsel}`} alt={`Soru ${s.sira}`} className="onizleme" /> : <p>{s.metin}</p>}
          <div className="yan-yana">
            <div className={`cevap-kutu ${s.durum === "dogru" ? "dogru" : "senin"}`}><h3>Senin cevabın</h3><SeninCevabin s={s} /></div>
            <div className="cevap-kutu dogru"><h3>Doğru cevap</h3>
              <p className="dogru-cevap">{s.dogru_sik ? `${s.dogru_sik}) ${s.secenekler.find((x) => x.harf === s.dogru_sik)?.metin ?? ""}` : s.dogru_cevap}</p></div>
          </div>
          {s.cozum && <Cozum metin={s.cozum} />}
          {s.aciklama && <div className="hata-aciklama"><h3>{s.durum === "dogru" ? "Öğretmeninin notu" : "Nerede hata yaptın?"}</h3><p className="t-metin">{s.aciklama}</p></div>}
          {s.konular.length > 0 && (
            <div className="izle">
              <h3>Eksiğini kapat <small className="soluk">· istersen konuyu dinle, istersen benzer bir sorunun çözümünü izle</small></h3>
              <div className="konu-liste">{s.konular.map((k) => <KonuKart key={k.konu} k={k} acikId={acikId} ac={ac} />)}</div>
            </div>
          )}
        </section>
      ))}

    </div>
  );
}
