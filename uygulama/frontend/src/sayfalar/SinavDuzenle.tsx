import { useEffect, useState } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";
import MKAkordeon from "../MKAkordeon";
import { RubrikAkordeon } from "../Rubrik";
import { api, ATAMA_DURUMU, tarihSaat, type Sinif, type SinavT, type SoruKisa } from "../api";

function yerelTarih(d: Date) {
  const p = (n: number) => String(n).padStart(2, "0");
  return `${d.getFullYear()}-${p(d.getMonth() + 1)}-${p(d.getDate())}T${p(d.getHours())}:${p(d.getMinutes())}`;
}

export default function SinavDuzenle() {
  const { id } = useParams();
  const git = useNavigate();
  const [ad, setAd] = useState("");
  const [ders, setDers] = useState("Fizik");
  const [duzey, setDuzey] = useState(10);
  const [sure, setSure] = useState<number | "">(40);
  const [aciklama, setAciklama] = useState("");
  const [secilen, setSecilen] = useState<SoruKisa[]>([]);
  const [banka, setBanka] = useState<SoruKisa[]>([]);
  const [sinav, setSinav] = useState<SinavT | null>(null);
  const [cikti, setCikti] = useState("");
  const [mkler, setMkler] = useState("");
  const [siniflar, setSiniflar] = useState<Sinif[]>([]);
  const [atamaSinif, setAtamaSinif] = useState<number | "">("");
  const [bas, setBas] = useState(yerelTarih(new Date()));
  const [bit, setBit] = useState(yerelTarih(new Date(Date.now() + 7 * 864e5)));
  const [hata, setHata] = useState("");
  const [bilgi, setBilgi] = useState("");

  useEffect(() => {
    api<Sinif[]>("/api/siniflar").then(setSiniflar).catch(() => {});
    if (id) api<SinavT>(`/api/sinavlar/${id}`).then(yukle).catch((e) => setHata(e.message));
  }, [id]);

  useEffect(() => {
    api<SoruKisa[]>(`/api/sorular?ders=${ders}`).then(setBanka).catch((e) => setHata(e.message));
  }, [ders]);

  function yukle(s: SinavT) {
    setSinav(s); setAd(s.ad); setDers(s.ders); setDuzey(s.sinif_duzeyi); setSure(s.sure_dk ?? ""); setAciklama(s.aciklama);
    setSecilen(s.sorular);
  }

  const ekle = (q: SoruKisa) => !secilen.some((x) => x.id === q.id) && setSecilen([...secilen, q]);
  const cikar = (qid: number) => setSecilen(secilen.filter((x) => x.id !== qid));
  const tasi = (i: number, d: number) => {
    const y = [...secilen]; const j = i + d;
    if (j < 0 || j >= y.length) return;
    [y[i], y[j]] = [y[j], y[i]]; setSecilen(y);
  };

  async function oner() {
    setHata("");
    try {
      const o = await api<SoruKisa[]>("/api/sinavlar/oneri", { govde: {
        ders, sinif_duzeyi: duzey, ogrenme_ciktisi: cikti.trim() || null,
        mk_kodlari: mkler.split(/[\s,;]+/).filter(Boolean), adet: 10 } });
      if (!o.length) setBilgi("Bu ölçüte uyan onaylı soru bulunamadı.");
      setSecilen([...secilen, ...o.filter((q) => !secilen.some((x) => x.id === q.id))]);
    } catch (e) { setHata((e as Error).message); }
  }

  async function kaydet() {
    setHata(""); setBilgi("");
    try {
      const govde = { ad, ders, sinif_duzeyi: duzey, aciklama, sure_dk: sure === "" ? null : sure, soru_idler: secilen.map((q) => q.id) };
      const s = id ? await api<SinavT>(`/api/sinavlar/${id}`, { method: "PUT", govde }) : await api<SinavT>("/api/sinavlar", { govde });
      yukle(s);
      setBilgi("✓ Sınav kaydedildi.");
      if (!id) git(`/sinavlar/${s.id}`, { replace: true });
    } catch (e) { setHata((e as Error).message); }
  }

  async function ata() {
    if (!sinav || !atamaSinif) return;
    setHata(""); setBilgi("");
    try {
      await api(`/api/sinavlar/${sinav.id}/ata`, { govde: { sinif_id: atamaSinif, baslangic: new Date(bas).toISOString(), bitis: new Date(bit).toISOString() } });
      yukle(await api<SinavT>(`/api/sinavlar/${sinav.id}`));
      setBilgi("✓ Sınav sınıfa atandı.");
    } catch (e) { setHata((e as Error).message); }
  }

  async function atamaSil(aid: number) {
    if (!sinav || !confirm("Bu atama kaldırılsın mı?")) return;
    await api(`/api/atamalar/${aid}`, { method: "DELETE" });
    yukle(await api<SinavT>(`/api/sinavlar/${sinav.id}`));
  }

  async function sil() {
    if (!id || !confirm("Sınav silinsin mi?")) return;
    await api(`/api/sinavlar/${id}`, { method: "DELETE" });
    git("/sinavlar");
  }

  const toplam = secilen.reduce((t, q) => t + (q.zorluk ?? 0), 0);
  const taslaklar = secilen.filter((q) => q.durum !== "onayli");

  async function taslaklariOnayla() {
    setHata(""); setBilgi("");
    try {
      await api("/api/sorular/toplu-onayla", { govde: { idler: taslaklar.map((q) => q.id) } });
      setSecilen(secilen.map((q) => ({ ...q, durum: "onayli" })));
      if (sinav) yukle(await api<SinavT>(`/api/sinavlar/${sinav.id}`));
      setBilgi(`✓ ${taslaklar.length} soru onaylandı.`);
    } catch (e) { setHata((e as Error).message); }
  }
  const duzeyler = ders === "Fizik" ? [9, 10, 11, 12] : [5, 6, 7, 8, 9, 10, 11, 12];
  const kayitli = !!sinav && sinav.sorular.map((q) => q.id).join() === secilen.map((q) => q.id).join();

  return (
    <div className="sayfa">
      <p><Link to="/sinavlar">← Sınavlar</Link></p>
      <h1>{id ? ad || "Sınav" : "Yeni sınav"}</h1>

      <section className="kart">
        <div className="satir">
          <label>Sınav adı<input value={ad} onChange={(e) => setAd(e.target.value)} placeholder="ör. Enerji ve Hareket yoklaması" /></label>
          <label>Ders<select value={ders} onChange={(e) => { setDers(e.target.value); setDuzey(e.target.value === "Fizik" ? 10 : 8); }}><option>Fizik</option><option>Matematik</option></select></label>
          <label>Sınıf<select value={duzey} onChange={(e) => setDuzey(Number(e.target.value))}>{duzeyler.map((d) => <option key={d} value={d}>{d}</option>)}</select></label>
          <label>Süre (dk)<input type="number" min={1} value={sure} onChange={(e) => setSure(e.target.value ? Number(e.target.value) : "")} /></label>
        </div>
        <label>Açıklama (öğrenci görür)<textarea rows={2} value={aciklama} onChange={(e) => setAciklama(e.target.value)} /></label>
      </section>

      <div className="soru-duzen">
        <section className="kart">
          <h2>Soru seç</h2>
          <p className="soluk">Bankadaki {ders} soruları (taslaklar da seçilebilir; atamadan önce onaylanmalı). Kazanım ya da MK verirsen sistem o MK'leri ve öncüllerini ölçen soruları kapsamı geniş tutarak önerir.</p>
          <div className="satir">
            <label>Kazanım<input value={cikti} onChange={(e) => setCikti(e.target.value)} placeholder="ör. FİZ.12.2.4" /></label>
            <label>MK kodları<input value={mkler} onChange={(e) => setMkler(e.target.value)} placeholder="ör. Fiz04MK0133" /></label>
          </div>
          <button className="ikincil" onClick={oner}>Soru öner</button>
          <div className="mk-liste banka">
            {banka.map((q) => (
              <button key={q.id} className="banka-soru" disabled={secilen.some((x) => x.id === q.id)} onClick={() => ekle(q)}>
                <span className="soru-metin">#{q.id} {q.metin}</span>
                <span className="etiketler"><span>{q.sinif_duzeyi}. sınıf</span>{q.durum !== "onayli" && <span className="durum taslak">Taslak</span>}<span className="seviye">Zorluk {q.zorluk?.toFixed(2)}</span>{q.mk_detay.map((m) => <code key={m.kod} title={m.ifade}>{m.kod}</code>)}</span>
              </button>
            ))}
            {banka.length === 0 && <p className="soluk">Bankada {ders} sorusu yok.</p>}
          </div>
        </section>

        <section className="kart">
          <h2>Sınavdaki sorular ({secilen.length})</h2>
          <p>Toplam zorluk: <strong>{toplam.toFixed(2)}</strong></p>
          {taslaklar.length > 0 && (
            <div className="kart uyari-bandi">
              Bu sınavda {taslaklar.length} onaylanmamış (taslak) soru var. Sınav kaydedilebilir, ama öğrenciye atanmadan önce soruların onaylanması gerekir.
              <div className="eylemler"><button className="kucuk" onClick={taslaklariOnayla}>Taslak soruları onayla</button>
              <span className="soluk">ya da önce soru bankasında tek tek incele</span></div>
            </div>
          )}
          <ol className="secilen">
            {secilen.map((q, i) => (
              <li key={q.id}>
                <span className="soru-metin">{q.metin}</span>
                <span className="etiketler"><span className="seviye">{q.zorluk?.toFixed(2)}</span>{q.durum !== "onayli" && <Link to={`/sorular/${q.id}`} className="durum taslak">Taslak</Link>}</span>
                <MKAkordeon q={q} />
                <RubrikAkordeon soruId={q.id} />
                <span className="kucuk-dugmeler">
                  <button className="ikincil kucuk" onClick={() => tasi(i, -1)} title="Yukarı">↑</button>
                  <button className="ikincil kucuk" onClick={() => tasi(i, 1)} title="Aşağı">↓</button>
                  <button className="ikincil kucuk" onClick={() => cikar(q.id)} title="Çıkar">✕</button>
                </span>
              </li>
            ))}
          </ol>
          {sinav && kayitli && sinav.kapsam.length > 0 && (<>
            <h3>Sınavın ölçtüğü MK'ler ({sinav.kapsam.length})</h3>
            <ul className="kapsam">{sinav.kapsam.map((m) => <li key={m.kod}><Link to={`/mk/${m.kod}`}><code>{m.kod}</code></Link> {m.ifade} <span className="soluk">({m.soru_sayisi} soru)</span></li>)}</ul>
          </>)}
        </section>
      </div>

      {hata && <p className="hata">{hata}</p>}
      {bilgi && <p className="basari">{bilgi}</p>}
      <div className="eylemler">
        <button disabled={!ad.trim() || secilen.length === 0} onClick={kaydet}>{id ? "Değişiklikleri kaydet" : "Sınavı kaydet"}</button>
        {(!ad.trim() || secilen.length === 0) && (
          <span className="soluk">
            {!ad.trim() && secilen.length === 0 ? "Kaydetmek için yukarıya sınav adı yaz ve soldaki listeden en az bir soru seç (soruya tıkla ya da \"Soru öner\")."
              : !ad.trim() ? "Kaydetmek için yukarıya sınav adı yaz."
              : "Kaydetmek için soldaki listeden en az bir soru seç (soruya tıkla ya da \"Soru öner\")."}
          </span>
        )}
        {id && <button className="ikincil tehlike" onClick={sil}>Sınavı sil</button>}
      </div>

      {sinav && (
        <section className="kart">
          <h2>Sınıfa ata ve yazdır</h2>
          <div className="satir">
            <label>Sınıf<select value={atamaSinif} onChange={(e) => setAtamaSinif(e.target.value ? Number(e.target.value) : "")}>
              <option value="">Seç</option>
              {siniflar.map((s) => <option key={s.id} value={s.id}>{s.ad}</option>)}
            </select></label>
            <label>Başlangıç<input type="datetime-local" value={bas} onChange={(e) => setBas(e.target.value)} /></label>
            <label>Bitiş<input type="datetime-local" value={bit} onChange={(e) => setBit(e.target.value)} /></label>
          </div>
          <div className="eylemler">
            <button disabled={!atamaSinif || !kayitli} onClick={ata}>Ata</button>
            <Link className="dugme ikincil-dugme" to={`/sinavlar/${sinav.id}/yazdir`} target="_blank">Boş kopya yazdır</Link>
            <Link className="dugme ikincil-dugme" to={`/sinavlar/${sinav.id}/rubrik`} target="_blank">📋 Rubrik (cevap anahtarı)</Link>
          </div>
          {!kayitli && <p className="soluk">Önce soru değişikliklerini kaydet.</p>}
          {sinav.atamalar.length > 0 && (
            <table>
              <thead><tr><th>Sınıf</th><th>Başlangıç</th><th>Bitiş</th><th>Durum</th><th></th></tr></thead>
              <tbody>
                {sinav.atamalar.map((a) => (
                  <tr key={a.id}>
                    <td>{a.sinif_adi}</td><td>{tarihSaat(a.baslangic)}</td><td>{tarihSaat(a.bitis)}</td>
                    <td><span className={`durum ${a.durum === "acik" ? "onayli" : ""}`}>{ATAMA_DURUMU[a.durum]}</span></td>
                    <td className="kucuk-dugmeler">
                      <Link to={`/atama/${a.id}/teslimler`}>Teslimler</Link>
                      <Link to={`/sinavlar/${sinav.id}/yazdir?atama=${a.id}`} target="_blank">Öğrenci kopyalarını yazdır</Link>
                      <button className="ikincil kucuk" onClick={() => atamaSil(a.id)}>Kaldır</button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </section>
      )}
    </div>
  );
}
