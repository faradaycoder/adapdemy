import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api, type DegerlendirmeT } from "../api";
import { AdimSatiri, CevapGorunumu, DogruCevap, MKOzeti } from "../Sonuc";

// Öğretmen: bir öğrencinin teslimini rubrik adımlarına göre değerlendirir ve onaylar.
export default function Degerlendir() {
  const { atamaId, teslimId } = useParams();
  const [d, setD] = useState<DegerlendirmeT | null>(null);
  const [notlar, setNotlar] = useState<Record<number, string>>({});
  const [genel, setGenel] = useState("");
  const [hata, setHata] = useState("");
  const [bilgi, setBilgi] = useState("");
  const yol = `/api/atamalar/${atamaId}/teslimler/${teslimId}`;

  useEffect(() => { api<DegerlendirmeT>(`${yol}/degerlendirme`).then(yukle).catch((e) => setHata(e.message)); }, [yol]);

  function yukle(v: DegerlendirmeT) {
    setD(v);
    setNotlar(Object.fromEntries(v.sorular.map((s) => [s.soru_id, s.ogretmen_notu])));
    setGenel(v.genel_geri_bildirim);
  }

  async function karar(soruId: number, kararlar: Record<number, string>, not?: string) {
    setHata(""); setBilgi("");
    try { yukle(await api<DegerlendirmeT>(`${yol}/soru/${soruId}`, { method: "PUT", govde: { kararlar, ...(not !== undefined ? { not } : {}) } })); }
    catch (e) { setHata((e as Error).message); }
  }

  async function genelKaydet() {
    setHata("");
    try { yukle(await api<DegerlendirmeT>(`${yol}/genel`, { method: "PUT", govde: { metin: genel } })); }
    catch (e) { setHata((e as Error).message); }
  }

  async function onayla(geriAl = false) {
    setHata(""); setBilgi("");
    try {
      yukle(await api<DegerlendirmeT>(`${yol}/${geriAl ? "geri-al" : "onayla"}`, { method: "POST" }));
      setBilgi(geriAl ? "Onay geri alındı; sonuç öğrenciden gizlendi." : "✓ Değerlendirme onaylandı; sonuç öğrenciye açıldı.");
    } catch (e) { setHata((e as Error).message); }
  }

  if (hata && !d) return <p className="hata sayfa">{hata}</p>;
  if (!d) return <p className="orta">Yükleniyor…</p>;
  const bekleyen = d.sorular.filter((s) => !s.tamam).length;

  return (
    <div className="sayfa">
      <p><Link to={`/atama/${atamaId}/teslimler`}>← Teslimler</Link></p>
      <div className="o-ust kart">
        <div>
          <h1>{d.ogrenci}</h1>
          <p className="soluk">{d.sinav_adi}</p>
        </div>
        <div className="o-durum">
          <span className="buyuk">{d.puan.toFixed(2)} <small className="soluk">/ {d.en_yuksek.toFixed(2)}</small></span>
          <span className={`durum ${d.degerlendirme === "onayli" ? "onayli" : ""}`}>{d.degerlendirme === "onayli" ? "Onaylandı" : bekleyen ? `${bekleyen} soru bekliyor` : "Onaya hazır"}</span>
        </div>
      </div>
      <p className="soluk">Çoktan seçmeli sorular teslimde otomatik değerlendirildi. Yazılı ve kâğıt cevaplarda her rubrik adımı için karar ver: <b>Biliyor</b> (doğru yaptı), <b>Bilmiyor</b> (denedi ama yanlış), <b>Ölçülemedi</b> (adıma gelmedi ya da boş). Otomatik kararları da değiştirebilirsin.</p>

      {d.genel_dosyalar.length > 0 && (
        <section className="kart vurgu-kart">
          <h2>Sınavın tamamı için yüklenen kâğıt ({d.genel_dosyalar.length} dosya)</h2>
          <p className="soluk">Öğrenci kâğıdın tamamını tek seferde yükledi. Her soruyu değerlendirirken buradaki sayfalara bak. (API anahtarı ve QR okuma gelince sayfalar sorulara otomatik ayrılacak.)</p>
          <div className="o-dosyalar">{d.genel_dosyalar.map((f, i) => (
            <a key={f.id} href={`/api/gorsel/${f.dosya}`} target="_blank" className="o-dosya buyuk-onizleme">
              {f.dosya.endsWith(".pdf") ? <span className="pdf-rozet">PDF {i + 1}</span> : <img src={`/api/gorsel/${f.dosya}`} alt={`Sayfa ${i + 1}`} />}
            </a>
          ))}</div>
        </section>
      )}

      {d.sorular.map((s) => (
        <section key={s.soru_id} className="kart">
          <div className="baslik-satiri">
            <h2>Soru {s.sira}</h2>
            <span><b>{s.puan.toFixed(2)}</b> / {s.zorluk.toFixed(2)} {!s.tamam && <span className="durum">karar bekliyor</span>}</span>
          </div>
          <div className="yan-yana">
            <div className="yan-sol">
              <h3>Soru ve doğru cevap</h3>
              <DogruCevap s={s} />
            </div>
            <div className="yan-sag">
              <h3>Öğrencinin çözümü</h3>
              <CevapGorunumu s={s} />
            </div>
          </div>
          <table className="rubrik">
            <thead><tr><th>#</th><th>Rubrik adımı</th><th>Karar</th><th>Puan</th></tr></thead>
            <tbody>{s.adimlar.map((a) => <AdimSatiri key={a.adim_id} a={a} duzenle={(durum) => karar(s.soru_id, { [a.adim_id]: durum })} />)}</tbody>
          </table>
          <div className="eylemler">
            <button className="ikincil kucuk" onClick={() => karar(s.soru_id, Object.fromEntries(s.adimlar.map((a) => [a.adim_id, "biliyor"])))}>Hepsi biliyor</button>
            <button className="ikincil kucuk" onClick={() => karar(s.soru_id, Object.fromEntries(s.adimlar.map((a) => [a.adim_id, "olculemedi"])))}>Hepsi ölçülemedi</button>
          </div>
          <label>Öğrenciye açıklama: nerede hata yaptı? <small className="soluk">(öğrenci yalnız bunu görür; rubrik ve MK kodları gösterilmez)</small>
            {s.aciklama_kaynak === "sistem" && s.ogretmen_notu && <span className="taslak-rozet">Sistem taslağı: düzenleyebilir ya da olduğu gibi bırakabilirsin</span>}
            <textarea rows={3} value={notlar[s.soru_id] ?? ""} onChange={(e) => setNotlar({ ...notlar, [s.soru_id]: e.target.value })}
              onBlur={() => notlar[s.soru_id] !== s.ogretmen_notu && karar(s.soru_id, {}, notlar[s.soru_id] ?? "")} />
          </label>
        </section>
      ))}

      <MKOzeti d={d} />
      <section className="kart">
        <label>Öğrenciye genel geri bildirim <small className="soluk">(sonuç ekranının en üstünde görünür)</small>
          {d.genel_kaynak === "sistem" && d.genel_geri_bildirim && <span className="taslak-rozet">Sistem taslağı</span>}
          <textarea rows={3} value={genel} onChange={(e) => setGenel(e.target.value)} onBlur={() => genel !== d.genel_geri_bildirim && genelKaydet()} />
        </label>
      </section>
      {hata && <p className="hata">{hata}</p>}
      {bilgi && <p className="basari">{bilgi}</p>}
      <div className="eylemler">
        {d.degerlendirme === "onayli"
          ? <button className="ikincil" onClick={() => onayla(true)}>Onayı geri al</button>
          : <button onClick={() => onayla()}>{bekleyen ? `Onayla (karar verilmeyen ${bekleyen} sorudaki adımlar ölçülemedi sayılır)` : "Değerlendirmeyi onayla ve öğrenciye aç"}</button>}
      </div>
    </div>
  );
}
