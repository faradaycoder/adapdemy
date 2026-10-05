import { useEffect, useRef, useState } from "react";
import { Mat } from "../Mat";
import { Link, useParams } from "react-router-dom";
import { api, type CevapT, type OturumT, type SinavSorusu } from "../api";

function base64Oku(dosya: File): Promise<string> {
  return new Promise((coz, red) => {
    const r = new FileReader();
    r.onload = () => coz(String(r.result));
    r.onerror = () => red(new Error("Dosya okunamadı."));
    r.readAsDataURL(dosya);
  });
}

function kalanSure(bitis: string, simdi: number) {
  const s = Math.max(0, Math.floor((new Date(bitis).getTime() - simdi) / 1000));
  const sa = Math.floor(s / 3600), dk = Math.floor((s % 3600) / 60), sn = s % 60;
  return { s, metin: `${sa ? `${sa}:` : ""}${String(dk).padStart(2, "0")}:${String(sn).padStart(2, "0")}` };
}

function SoruKutusu({ q, c, kilitli, kaydet, dosyaEkle, dosyaSil }: {
  q: SinavSorusu; c: CevapT | undefined; kilitli: boolean;
  kaydet: (p: Partial<CevapT>) => void; dosyaEkle: (f: File) => void; dosyaSil: (id: number) => void;
}) {
  const [metin, setMetin] = useState(c?.metin ?? "");
  const zaman = useRef<number | undefined>(undefined);
  useEffect(() => setMetin(c?.metin ?? ""), [c?.metin]);

  function yaz(v: string) {
    setMetin(v);
    window.clearTimeout(zaman.current);
    zaman.current = window.setTimeout(() => kaydet({ metin: v }), 700); // yazarken otomatik kayıt
  }

  return (
    <article className="kart o-soru">
      <h3>Soru {q.sira}</h3>
      {q.gorsel && !q.gorsel.endsWith(".pdf") ? <img src={`/api/gorsel/${q.gorsel}`} alt={`Soru ${q.sira}`} className="onizleme" /> : <p><Mat metin={q.metin} /></p>}
      {q.cevap_bicimi === "coktan_secmeli" ? (
        <div className="o-siklar">
          {q.secenekler.map((s) => (
            <label key={s.harf} className={`o-sik ${c?.secilen === s.harf ? "secili" : ""}`}>
              <input type="radio" name={`s${q.soru_id}`} disabled={kilitli} checked={c?.secilen === s.harf} onChange={() => kaydet({ secilen: s.harf })} />
              <strong>{s.harf})</strong> <Mat metin={s.metin} />
            </label>
          ))}
        </div>
      ) : (
        <label>Cevabın{q.cevap_bicimi === "kisa_cevap" ? "" : " ve çözümün (istersen kâğıtta çözüp fotoğrafını ekle)"}
          <textarea rows={q.cevap_bicimi === "kisa_cevap" ? 2 : 5} value={metin} disabled={kilitli} onChange={(e) => yaz(e.target.value)} />
        </label>
      )}
      <div className="o-dosyalar">
        {c?.dosyalar.map((d) => (
          <span key={d.id} className="o-dosya">
            {d.dosya.endsWith(".pdf") ? <a href={`/api/gorsel/${d.dosya}`} target="_blank">PDF</a> : <img src={`/api/gorsel/${d.dosya}`} alt="Yüklenen çözüm" />}
            {!kilitli && <button className="ikincil kucuk" onClick={() => dosyaSil(d.id)} title="Kaldır">✕</button>}
          </span>
        ))}
        {!kilitli && (
          <>
            <label className="dugme ikincil-dugme kucuk-etiket">📷 Fotoğraf çek
              <input type="file" accept="image/png,image/jpeg" capture="environment" hidden onChange={(e) => { const f = e.target.files?.[0]; if (f) dosyaEkle(f); e.target.value = ""; }} />
            </label>
            <label className="dugme ikincil-dugme kucuk-etiket">Dosya ekle
              <input type="file" accept="image/png,image/jpeg,application/pdf" hidden onChange={(e) => { const f = e.target.files?.[0]; if (f) dosyaEkle(f); e.target.value = ""; }} />
            </label>
          </>
        )}
      </div>
    </article>
  );
}

export default function OgrenciSinav() {
  const { atamaId } = useParams();
  const [o, setO] = useState<OturumT | null>(null);
  const [hata, setHata] = useState("");
  const [simdi, setSimdi] = useState(Date.now());
  const [kaydediliyor, setKaydediliyor] = useState(false);

  useEffect(() => { api<OturumT>(`/api/teslim/${atamaId}/basla`, { method: "POST" }).then(setO).catch((e) => setHata(e.message)); }, [atamaId]);
  useEffect(() => { const t = setInterval(() => setSimdi(Date.now()), 1000); return () => clearInterval(t); }, []);

  if (hata && !o) return <div className="sayfa"><p className="hata">{hata}</p><Link to="/">← Ana sayfa</Link></div>;
  if (!o) return <p className="orta">Sınav açılıyor…</p>;

  const kalan = kalanSure(o.bitis, simdi);
  const kilitli = o.durum !== "devam" || kalan.s === 0;
  const cevap = (id: number) => o.cevaplar.find((c) => c.soru_id === id);
  const guncelle = (c: CevapT) => setO({ ...o, cevaplar: [...o.cevaplar.filter((x) => x.soru_id !== c.soru_id), c] });

  async function istek(fn: () => Promise<CevapT | void>) {
    setHata(""); setKaydediliyor(true);
    try { const c = await fn(); if (c) guncelle(c); } catch (e) { setHata((e as Error).message); } finally { setKaydediliyor(false); }
  }

  const cevaplanan = o.sorular.filter((q) => { const c = cevap(q.soru_id); return c && (c.secilen || c.metin.trim() || c.dosyalar.length); }).length;

  async function genelEkle(dosyalar: File[]) {
    setHata(""); setKaydediliyor(true);
    try {
      let son: OturumT | null = null;
      for (const f of dosyalar) son = await api<OturumT>(`/api/teslim/${atamaId}/dosya`, { govde: { dosya_base64: await base64Oku(f) } });
      if (son) setO(son);
    } catch (e) { setHata((e as Error).message); } finally { setKaydediliyor(false); }
  }

  async function teslimEt() {
    const genel = o!.genel_dosyalar.length ? ` Ayrıca sınavın tamamı için ${o!.genel_dosyalar.length} dosya yükledin.` : "";
    if (!confirm(`${o!.sorular.length} sorudan ${cevaplanan} tanesini cevapladın.${genel} Teslim edilsin mi? Teslimden sonra cevaplar değiştirilemez.`)) return;
    try { setO(await api<OturumT>(`/api/teslim/${atamaId}/gonder`, { method: "POST" })); } catch (e) { setHata((e as Error).message); }
  }

  return (
    <div className="sayfa o-sinav">
      <div className="o-ust kart">
        <div>
          <h1>{o.sinav_adi}</h1>
          {o.aciklama && <p className="soluk">{o.aciklama}</p>}
        </div>
        <div className="o-durum">
          {o.durum === "teslim" ? <span className="durum onayli">Teslim edildi</span>
            : kalan.s === 0 ? <span className="durum">Süre doldu</span>
            : <span className={`sayac ${kalan.s < 300 ? "az" : ""}`}>⏱ {kalan.metin}</span>}
          <span className="soluk">{cevaplanan}/{o.sorular.length} cevaplandı{kaydediliyor ? " · kaydediliyor…" : ""}</span>
        </div>
      </div>
      {hata && <p className="hata">{hata}</p>}

      <section className="kart genel-yukleme">
        <div className="baslik-satiri">
          <h2>Sınavın tamamını tek seferde yükle</h2>
          {o.durum !== "teslim" && <Link className="dugme ikincil" to={`/sinav/${atamaId}/yazdir`} target="_blank">🖨 Sınavı yazdır</Link>}
        </div>
        <p className="soluk">Bütün soruları kâğıtta çözdüysen, kâğıdın tamamını burada yükleyebilirsin: tek bir PDF ya da her sayfanın fotoğrafı (en fazla 20). Böyle yaparsan sorulara ayrı ayrı yüklemen gerekmez; öğretmenin hangi sayfanın hangi soru olduğunu görür.</p>
        <div className="o-dosyalar">
          {o.genel_dosyalar.map((d, i) => (
            <span key={d.id} className="o-dosya">
              {d.dosya.endsWith(".pdf") ? <a href={`/api/gorsel/${d.dosya}`} target="_blank" className="pdf-rozet">PDF {i + 1}</a> : <img src={`/api/gorsel/${d.dosya}`} alt={`Sayfa ${i + 1}`} />}
              {!kilitli && <button className="ikincil kucuk" title="Kaldır" onClick={async () => { try { setO(await api<OturumT>(`/api/teslim/${atamaId}/dosya/${d.id}`, { method: "DELETE" })); } catch (e) { setHata((e as Error).message); } }}>✕</button>}
            </span>
          ))}
          {!kilitli && (<>
            <label className="dugme ikincil-dugme kucuk-etiket">📷 Sayfa fotoğrafı çek
              <input type="file" accept="image/png,image/jpeg" capture="environment" hidden onChange={(e) => { const f = e.target.files?.[0]; if (f) genelEkle([f]); e.target.value = ""; }} />
            </label>
            <label className="dugme ikincil-dugme kucuk-etiket">PDF ya da fotoğraflar seç
              <input type="file" accept="image/png,image/jpeg,application/pdf" multiple hidden onChange={(e) => { const f = [...(e.target.files ?? [])]; if (f.length) genelEkle(f); e.target.value = ""; }} />
            </label>
          </>)}
          {kilitli && o.genel_dosyalar.length === 0 && <span className="soluk">Yüklenmedi.</span>}
        </div>
      </section>

      {o.sorular.map((q) => (
        <SoruKutusu key={q.soru_id} q={q} c={cevap(q.soru_id)} kilitli={kilitli}
          kaydet={(p) => istek(() => api<CevapT>(`/api/teslim/${atamaId}/cevap/${q.soru_id}`, { method: "PUT", govde: { secilen: p.secilen ?? cevap(q.soru_id)?.secilen ?? null, metin: p.metin ?? cevap(q.soru_id)?.metin ?? "" } }))}
          dosyaEkle={(f) => istek(async () => api<CevapT>(`/api/teslim/${atamaId}/cevap/${q.soru_id}/dosya`, { govde: { dosya_base64: await base64Oku(f) } }))}
          dosyaSil={(id) => istek(async () => {
            await api(`/api/teslim/${atamaId}/cevap/${q.soru_id}/dosya/${id}`, { method: "DELETE" });
            const c = cevap(q.soru_id);
            if (c) guncelle({ ...c, dosyalar: c.dosyalar.filter((d) => d.id !== id) });
          })} />
      ))}
      <div className="eylemler">
        {o.durum === "devam" && <button onClick={teslimEt}>Sınavı teslim et</button>}
        <Link to="/">← Ana sayfa</Link>
      </div>
    </div>
  );
}
