import { Link } from "react-router-dom";
import { Mat } from "./Mat";
import { ADIM_DURUMU, type AdimSonuc, type DegerlendirmeT, type SoruSonuc } from "./api";

// Değerlendirme sonucunun ortak görünümü: öğretmen ekranında düzenlenebilir, öğrenci ekranında salt okunur.

export function DurumRozeti({ durum }: { durum: string | null }) {
  return <span className={`adim-durum ${durum ?? "yok"}`}>{durum ? ADIM_DURUMU[durum] : "Karar yok"}</span>;
}

export function MKOzeti({ d }: { d: DegerlendirmeT }) {
  const say = (x: string) => d.mkler.filter((m) => m.durum === x).length;
  return (
    <section className="kart">
      <h2>MK teşhisi</h2>
      <p className="soluk">Biliyor {say("biliyor")} · Bilmiyor {say("bilmiyor")} · Ölçülemedi {say("olculemedi")}</p>
      <ul className="mk-ozet">
        {[...d.mkler].sort((a, b) => ["bilmiyor", "olculemedi", "biliyor"].indexOf(a.durum) - ["bilmiyor", "olculemedi", "biliyor"].indexOf(b.durum)).map((m) => (
          <li key={m.kod}><DurumRozeti durum={m.durum} /> <code>{m.kod}</code> {m.ifade}</li>
        ))}
      </ul>
    </section>
  );
}

const OKUNAN = "[Yüklenen kâğıttan okundu] ";

export function CevapGorunumu({ s }: { s: SoruSonuc }) {
  const okunan = s.metin_cevap.startsWith(OKUNAN);
  const metin = okunan ? s.metin_cevap.slice(OKUNAN.length) : s.metin_cevap;
  return (
    <div className="cevap-gorunum">
      {s.cevap_bicimi === "coktan_secmeli" && (
        <p>İşaretlenen: <b>{s.secilen ?? "boş"}</b> · Doğru: <b>{s.secenekler.find((x) => x.dogru)?.harf}</b>
          {s.yanilgi && <span className="uyari-metin"> · Yanılgı: {s.yanilgi}</span>}</p>
      )}
      {s.dosyalar.map((f) => (
        <figure key={f.id} className="el-yazisi">
          {f.dosya.endsWith(".pdf")
            ? <iframe src={`/api/gorsel/${f.dosya}`} title="Öğrencinin çözümü (PDF)" />
            : <a href={`/api/gorsel/${f.dosya}`} target="_blank" title="Büyütmek için tıkla"><img src={`/api/gorsel/${f.dosya}`} alt="Öğrencinin çözümü" /></a>}
          <figcaption className="soluk">{f.kaynak === "kagittan" ? "Öğrencinin yüklediği kâğıttan, bu sorunun bölümü" : "Öğrencinin bu soruya yüklediği"} · büyütmek için tıkla</figcaption>
        </figure>
      ))}
      {s.cevap_bicimi !== "coktan_secmeli" && (metin
        ? <div className="okunan"><span className="soluk">{okunan ? "Sistemin okuduğu (el yazısıyla karşılaştır):" : "Öğrencinin yazdığı:"}</span><p className="t-metin">{metin}</p></div>
        : !s.dosyalar.length && <p className="soluk">Cevap yazılmadı.</p>)}
    </div>
  );
}

export function DogruCevap({ s }: { s: SoruSonuc }) {
  return (
    <div>
      {s.gorsel && !s.gorsel.endsWith(".pdf") ? <img src={`/api/gorsel/${s.gorsel}`} alt={`Soru ${s.sira}`} className="onizleme" /> : <p><Mat metin={s.metin} /></p>}
      <div className="dogru-kutu">
        <span className="soluk">Doğru cevap</span>
        <p className="dogru-cevap"><Mat metin={s.dogru_cevap} /></p>
        {s.cozum && <><span className="soluk">Çözüm</span><p><Mat metin={s.cozum} /></p></>}
      </div>
    </div>
  );
}

export function AdimSatiri({ a, duzenle }: { a: AdimSonuc; duzenle?: (durum: string) => void }) {
  return (
    <tr>
      <td>{a.sira}</td>
      <td><Mat metin={a.aciklama} /><div><Link to={`/mk/${a.mk_kod}`}><code>{a.mk_kod}</code></Link> <small className="soluk">{a.mk_ifade}{a.soru_mk_mi ? "" : " (ön koşul)"}</small></div>
        {a.gerekce && <small className={a.kaynak === "sistem" ? "oneri" : "soluk"}>{a.kaynak === "otomatik" ? "Otomatik: " : a.kaynak === "sistem" ? "Sistem önerisi: " : ""}{a.gerekce}</small>}</td>
      <td>{duzenle ? (
        <div className="adim-secim">
          {(["biliyor", "bilmiyor", "olculemedi"] as const).map((d) => (
            <button key={d} className={`kucuk ${a.durum === d ? `secili ${d}` : "ikincil"}`} onClick={() => duzenle(d)}>{ADIM_DURUMU[d]}</button>
          ))}
        </div>
      ) : <DurumRozeti durum={a.durum} />}</td>
      <td>{a.puan.toFixed(2)} / {a.en_yuksek.toFixed(2)}</td>
    </tr>
  );
}
