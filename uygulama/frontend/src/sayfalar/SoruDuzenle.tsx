import { useEffect, useRef, useState } from "react";
import { Link, useLocation, useNavigate, useParams } from "react-router-dom";
import { api, CEVAP_BICIMLERI, type Analiz, type Esleme, type Soru, type SoruG } from "../api";

// Yeni soruda (analizden gelen) ve kayıtlı soruda aynı ekran kullanılır.
export default function SoruDuzenle() {
  const { id } = useParams();
  const konum = useLocation();
  const git = useNavigate();
  const [soru, setSoru] = useState<SoruG | null>(null);
  const [esleme, setEsleme] = useState<Esleme | null>(null);
  const [durum, setDurum] = useState<string>("taslak");
  const [saglayici, setSaglayici] = useState<string | null>(null);
  const [notlar, setNotlar] = useState<string[]>([]);
  const [hata, setHata] = useState("");
  const [bekle, setBekle] = useState(false);
  const [bilgi, setBilgi] = useState("");
  const ilk = useRef(true);

  useEffect(() => {
    if (id) {
      api<Soru>(`/api/sorular/${id}`).then((s) => { setSoru(s); setEsleme(s.eslesme); setDurum(s.durum); }).catch((e) => setHata(e.message));
    } else {
      const a = konum.state as Analiz | null;
      if (!a) { git("/sorular/yukle", { replace: true }); return; }
      setSoru(a); setEsleme(a.eslesme); setSaglayici(a.saglayici); setNotlar(a.notlar ?? []);
    }
  }, [id]);

  // Adımların MK'si ya da birincil MK değişince sorunun MK'lerini, zorluğu ve payları yeniden hesapla.
  const mkImzasi = soru ? soru.adimlar.map((a) => a.mk_kod).join(",") + "|" + soru.birincil : "";
  useEffect(() => {
    if (!soru) return;
    if (ilk.current) { ilk.current = false; return; }
    const t = setTimeout(() => {
      api<Esleme>("/api/sorular/esle", { govde: { ders: soru.ders, adimlar: soru.adimlar, birincil: soru.birincil } })
        .then(setEsleme).catch((e) => setHata(e.message));
    }, 400);
    return () => clearTimeout(t);
  }, [mkImzasi]);

  if (hata && !soru) return <p className="hata sayfa">{hata}</p>;
  if (!soru || !esleme) return <p className="orta">Yükleniyor…</p>;

  const degistir = (p: Partial<SoruG>) => setSoru({ ...soru, ...p });
  const adimDegistir = (i: number, p: Partial<SoruG["adimlar"][number]>) =>
    degistir({ adimlar: soru.adimlar.map((a, j) => (j === i ? { ...a, ...p } : a)) });

  async function kaydet(onayla: boolean) {
    setHata(""); setBilgi(""); setBekle(true);
    try {
      const govde = { ...soru, birincil: esleme?.birincil ?? soru!.birincil };
      let s = id ? await api<Soru>(`/api/sorular/${id}`, { method: "PUT", govde }) : await api<Soru>("/api/sorular", { govde });
      if (onayla) s = await api<Soru>(`/api/sorular/${s.id}/onayla`, { method: "POST" });
      git(`/sorular/${s.id}`, { replace: true });
      setSoru(s); setEsleme(s.eslesme); setDurum(s.durum);
      setBilgi(onayla ? "✓ Soru kaydedildi ve onaylandı." : "✓ Soru taslak olarak kaydedildi.");
    } catch (e) { setHata((e as Error).message); } finally { setBekle(false); }
  }

  async function sil() {
    if (!id || !confirm("Bu soru silinsin mi?")) return;
    await api(`/api/sorular/${id}`, { method: "DELETE" });
    git("/sorular");
  }

  return (
    <div className="sayfa">
      <p><Link to="/sorular">← Soru bankası</Link></p>
      <div className="baslik-satiri">
        <h1>{id ? `Soru #${id}` : "Yeni soru: incele ve onayla"}</h1>
        {id && <span className={`durum ${durum}`}>{durum === "onayli" ? "Onaylı" : "Taslak"}</span>}
      </div>
      {saglayici === "demo" && <p className="soluk">Bu analiz demo modunda hazır örnekten geldi.</p>}
      {notlar.length > 0 && <div className="kart vurgu bilgi"><ul className="notlar">{notlar.map((n) => <li key={n}>{n}</li>)}</ul></div>}

      <div className="soru-duzen">
        <section className="kart">
          <h2>Soru</h2>
          {soru.gorsel && (soru.gorsel.endsWith(".pdf")
            ? <iframe src={`/api/gorsel/${soru.gorsel}`} title="Soru PDF" className="onizleme pdf" />
            : <img src={`/api/gorsel/${soru.gorsel}`} alt="Soru görseli" className="onizleme" />)}
          <label>Okunan soru metni<textarea rows={5} value={soru.metin} onChange={(e) => degistir({ metin: e.target.value })} /></label>
          <div className="satir">
            <label>Ders<input value={soru.ders} disabled /></label>
            <label>Sınıf<input value={soru.sinif_duzeyi} disabled /></label>
            <label>Cevap biçimi
              <select value={soru.cevap_bicimi} onChange={(e) => degistir({ cevap_bicimi: e.target.value })}>
                {Object.entries(CEVAP_BICIMLERI).map(([k, v]) => <option key={k} value={k}>{v}</option>)}
              </select>
            </label>
          </div>
          {soru.cevap_bicimi === "coktan_secmeli" && (
            <div className="secenekler">
              {soru.secenekler.map((x, i) => (
                <label key={x.harf} className="secenek">
                  <input type="radio" name="dogru" checked={x.dogru}
                    onChange={() => degistir({ secenekler: soru.secenekler.map((y, j) => ({ ...y, dogru: j === i })), dogru_cevap: x.harf })} />
                  <strong>{x.harf})</strong>
                  <input value={x.metin} onChange={(e) => degistir({ secenekler: soru.secenekler.map((y, j) => (j === i ? { ...y, metin: e.target.value } : y)) })} />
                </label>
              ))}
            </div>
          )}
          <label>Doğru cevap<input value={soru.dogru_cevap} onChange={(e) => degistir({ dogru_cevap: e.target.value })} /></label>
          <label>Çözüm<textarea rows={4} value={soru.cozum} onChange={(e) => degistir({ cozum: e.target.value })} /></label>
        </section>

        <section className="kart">
          <h2>MK eşlemesi ve zorluk</h2>
          <div className="ozet-kutu">
            <div><span className="soluk">Soru zorluğu (Σ Z)</span><strong className="buyuk">{esleme.zorluk?.toFixed(2) ?? "–"}</strong></div>
            <div>
              <span className="soluk">Sorunun MK'leri (en üsttekiler)</span>
              {esleme.soru_mkleri.map((m) => (
                <label key={m.kod} className="mk-secim">
                  <input type="radio" name="birincil" checked={esleme.birincil === m.kod} onChange={() => degistir({ birincil: m.kod })} />
                  <Link to={`/mk/${m.kod}`}><code>{m.kod}</code></Link> {m.ifade}
                  <span className="seviye">Z {m.zorluk?.toFixed(2)}</span>
                  {esleme.birincil === m.kod && <span className="etiket">birincil</span>}
                </label>
              ))}
            </div>
          </div>
          {esleme.uyarilar.length > 0 && <ul className="uyarilar">{esleme.uyarilar.map((u) => <li key={u}>{u}</li>)}</ul>}

          <h3>Rubrik</h3>
          <table className="rubrik">
            <thead><tr><th>#</th><th>Adım</th><th>MK</th><th>Pay</th><th>Puan</th><th></th></tr></thead>
            <tbody>
              {soru.adimlar.map((a, i) => {
                const c = esleme.adimlar[i];
                return (
                  <tr key={i}>
                    <td>{i + 1}</td>
                    <td><textarea rows={2} value={a.aciklama} onChange={(e) => adimDegistir(i, { aciklama: e.target.value })} /></td>
                    <td>
                      <input className="mk-girdi" value={a.mk_kod} onChange={(e) => adimDegistir(i, { mk_kod: e.target.value.trim() })} />
                      {c?.mk ? <small className="soluk">{c.mk.ifade} ({c.mk.islem_turu}, v = {c.mk.v})</small> : <small className="hata">MK bulunamadı</small>}
                      {c && !c.soru_mk_mi && c.mk && <small className="etiket">ön koşul (teşhis için)</small>}
                    </td>
                    <td>{c ? `%${(c.pay * 100).toFixed(1)}` : ""}</td>
                    <td>{c && esleme.zorluk ? (c.pay * esleme.zorluk).toFixed(2) : ""}</td>
                    <td><button className="ikincil kucuk" title="Adımı sil" onClick={() => degistir({ adimlar: soru.adimlar.filter((_, j) => j !== i) })}>✕</button></td>
                  </tr>
                );
              })}
            </tbody>
          </table>
          <button className="ikincil" onClick={() => degistir({ adimlar: [...soru.adimlar, { aciklama: "", mk_kod: "" }] })}>+ Adım ekle</button>
        </section>
      </div>

      {hata && <p className="hata">{hata}</p>}
      {bilgi && <p className="basari">{bilgi} <Link to="/sorular">Soru bankasına dön</Link></p>}
      <div className="eylemler">
        {id && <span className={`durum ${durum}`}>{durum === "onayli" ? "Onaylı" : "Taslak"}</span>}
        <button className="ikincil" disabled={bekle} onClick={() => kaydet(false)}>Taslak olarak kaydet</button>
        <button disabled={bekle} onClick={() => kaydet(true)}>{bekle ? "Kaydediliyor…" : "Kaydet ve onayla"}</button>
        {id && <button className="ikincil tehlike" onClick={sil}>Sil</button>}
      </div>
    </div>
  );
}
