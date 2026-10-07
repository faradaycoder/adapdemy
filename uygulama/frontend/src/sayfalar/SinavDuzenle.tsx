import { useEffect, useState } from "react";
import { Mat } from "../Mat";
import { Link, useNavigate, useParams } from "react-router-dom";
import MKAkordeon from "../MKAkordeon";
import { RubrikAkordeon } from "../Rubrik";
import { api, ATAMA_DURUMU, gorselMi, tarihSaat, type Sinif, type SinavT, type SoruKisa } from "../api";
import SoruEkle from "../SoruEkle";

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
  const [panel, setPanel] = useState(false);
  const [surukle, setSurukle] = useState<number | null>(null);
  const [sinav, setSinav] = useState<SinavT | null>(null);
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

  const birak = (hedef: number) => {
    if (surukle === null || surukle === hedef) return;
    const y = [...secilen]; const [x] = y.splice(surukle, 1); y.splice(hedef, 0, x);
    setSecilen(y); setSurukle(null);
  };

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
    <div className="sayfa genis sinav-duzen">
      <p><Link to="/sinavlar">← Sınavlar</Link></p>

      <section className="kart sinav-baslik">
        <input className="sinav-ad" value={ad} onChange={(e) => setAd(e.target.value)} placeholder="Sınav adı (ör. 6-A bölünebilme yoklaması)" aria-label="Sınav adı" />
        <div className="satir">
          <label>Ders<select value={ders} onChange={(e) => { setDers(e.target.value); setDuzey(e.target.value === "Fizik" ? 10 : 6); }}><option>Matematik</option><option>Fizik</option></select></label>
          <label>Sınıf<select value={duzey} onChange={(e) => setDuzey(Number(e.target.value))}>{duzeyler.map((d) => <option key={d} value={d}>{d}. sınıf</option>)}</select></label>
          <label>Süre (dk)<input type="number" min={1} value={sure} onChange={(e) => setSure(e.target.value ? Number(e.target.value) : "")} /></label>
        </div>
        <label>Açıklama (öğrenci görür)<textarea rows={2} value={aciklama} onChange={(e) => setAciklama(e.target.value)} placeholder="ör. Soruları kâğıtta çözüp fotoğrafını yükleyebilirsin." /></label>
      </section>

      <div className="sinav-ozet">
        <span><b>{secilen.length}</b> soru</span>
        <span>Toplam zorluk <b>{toplam.toFixed(1)}</b></span>
        {sinav && kayitli && <span><b>{sinav.kapsam.length}</b> MK ölçülüyor</span>}
        <span className="bosluk" />
        {hata && <span className="hata">{hata}</span>}
        {bilgi && <span className="basari-yazi">{bilgi}</span>}
        {id && <button className="ikincil tehlike kucuk" onClick={sil}>Sınavı sil</button>}
        <button disabled={!ad.trim() || secilen.length === 0} onClick={kaydet}
          title={!ad.trim() ? "Önce sınav adı yaz" : secilen.length === 0 ? "Önce soru ekle" : ""}>{id ? (kayitli ? "✓ Kaydedildi" : "Değişiklikleri kaydet") : "Sınavı kaydet"}</button>
      </div>

      {taslaklar.length > 0 && (
        <div className="kart uyari-bandi">
          Bu sınavda {taslaklar.length} onaylanmamış (taslak) soru var. Öğrenciye atanmadan önce onaylanmalı.
          <div className="eylemler"><button className="kucuk" onClick={taslaklariOnayla}>Taslak soruları onayla</button></div>
        </div>
      )}

      <ol className="sinav-sorulari">
        {secilen.map((q, i) => (
          <li key={q.id} className={`kart sinav-soru ${surukle === i ? "surukleniyor" : ""}`} draggable
            onDragStart={() => setSurukle(i)} onDragEnd={() => setSurukle(null)}
            onDragOver={(e) => e.preventDefault()} onDrop={() => birak(i)}>
            <div className="soru-kenar">
              <span className="tutamac" title="Sürükleyerek sırasını değiştir">⠿</span>
              <span className="soru-no">{i + 1}</span>
              <button className="ikincil kucuk" disabled={i === 0} onClick={() => tasi(i, -1)} title="Yukarı taşı">↑</button>
              <button className="ikincil kucuk" disabled={i === secilen.length - 1} onClick={() => tasi(i, 1)} title="Aşağı taşı">↓</button>
            </div>
            <div className="soru-govde">
              {gorselMi(q.gorsel) ? <img className="soru-gorsel" src={`/api/gorsel/${q.gorsel}`} alt={`Soru ${i + 1}`} /> : <p className="soru-yazi"><Mat metin={q.metin} /></p>}
              <div className="etiketler">
                {q.durum !== "onayli" && <Link to={`/sorular/${q.id}`} className="durum taslak">Taslak</Link>}
                <span className="seviye">Zorluk {q.zorluk?.toFixed(2)}</span>
                <Link to={`/sorular/${q.id}`} className="soluk">Soruyu düzenle</Link>
              </div>
              <MKAkordeon q={q} />
              <RubrikAkordeon soruId={q.id} />
            </div>
            <button className="ikincil kucuk cikar" onClick={() => cikar(q.id)} title="Sınavdan çıkar">✕</button>
          </li>
        ))}
      </ol>
      {secilen.length === 0 && <div className="kart bos-durum"><b>Sınavda henüz soru yok</b>Aşağıdaki düğmeyle sınıf, ünite, kazanım ve mikro kazanım seçerek soru ekle.</div>}
      <button className="soru-ekle-dugme" onClick={() => setPanel(true)}>＋ Soru ekle</button>
      {panel && <SoruEkle ders={ders} duzey={duzey} secili={secilen.map((q) => q.id)} ekle={ekle} kapat={() => setPanel(false)} />}

      {sinav && kayitli && sinav.kapsam.length > 0 && (
        <details className="kart">
          <summary><b>Sınavın ölçtüğü MK'ler ({sinav.kapsam.length})</b></summary>
          <ul className="kapsam">{sinav.kapsam.map((m) => <li key={m.kod}><Link to={`/mk/${m.kod}`}><code>{m.kod}</code></Link> {m.ifade} <span className="soluk">({m.soru_sayisi} soru)</span></li>)}</ul>
        </details>
      )}

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
