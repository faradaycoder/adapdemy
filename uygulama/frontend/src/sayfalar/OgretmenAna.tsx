import { useEffect, useState, type FormEvent } from "react";
import { Link } from "react-router-dom";
import { api, selam, type OzetT, type Sinif } from "../api";
import { useOturum } from "../oturum";

// Öğretmen ana sayfası: karşılama ve hızlı eylemler, sayaçlar, değerlendirme bekleyenler, EVALORA döngüsü, sınıflar.
export default function OgretmenAna() {
  const { kullanici } = useOturum();
  const [siniflar, setSiniflar] = useState<Sinif[]>([]);
  const [ozet, setOzet] = useState<OzetT | null>(null);
  const [ad, setAd] = useState("");
  const [ders, setDers] = useState("Matematik");
  const [duzey, setDuzey] = useState(6);
  const [hata, setHata] = useState("");
  const [formAcik, setFormAcik] = useState(false);

  useEffect(() => {
    api<Sinif[]>("/api/siniflar").then(setSiniflar).catch((e) => setHata(e.message));
    api<OzetT>("/api/ozet").then(setOzet).catch(() => {});
  }, []);

  async function ac(e: FormEvent) {
    e.preventDefault();
    setHata("");
    try {
      const s = await api<Sinif>("/api/siniflar", { govde: { ad, ders, sinif_duzeyi: duzey } });
      setSiniflar([...siniflar, s]);
      setAd(""); setFormAcik(false);
    } catch (err) { setHata((err as Error).message); }
  }

  const duzeyler = ders === "Fizik" ? [9, 10, 11, 12] : [5, 6, 7, 8, 9, 10, 11, 12];
  const bekleyenToplam = ozet?.bekleyenler.reduce((t, b) => t + b.bekleyen, 0) ?? 0;

  return (
    <div className="sayfa">
      <section className="karsilama">
        <h1>{selam()}, {kullanici?.ad} 👋</h1>
        <p>{bekleyenToplam ? `Değerlendirmeni bekleyen ${bekleyenToplam} kâğıt var.` : "Bekleyen değerlendirme yok."} Ölç, teşhis et, telafi et: her öğrencinin eksik mikro kazanımını bul ve kapat.</p>
        <div className="eylemler">
          <Link className="dugme" to="/sorular/yukle">＋ Soru yükle</Link>
          <Link className="dugme ikincil" to="/sinavlar/yeni">Yeni sınav</Link>
          <button className="dugme ikincil" onClick={() => { setFormAcik(true); setTimeout(() => document.getElementById("yeni-sinif")?.scrollIntoView({ behavior: "smooth" }), 50); }}>Sınıf aç</button>
        </div>
      </section>

      <div className="sayilar">
        <div className="sayi-kutu"><b>{ozet?.sinif ?? siniflar.length}</b><span>Sınıf</span></div>
        <div className="sayi-kutu olc"><b>{ozet?.ogrenci ?? "–"}</b><span>Öğrenci</span></div>
        <Link className="sayi-kutu teshis" to="/sorular"><b>{ozet?.soru_onayli ?? "–"}</b><span>Onaylı soru{ozet?.soru_taslak ? ` · ${ozet.soru_taslak} taslak` : ""}</span></Link>
        <Link className="sayi-kutu telafi" to="/sinavlar"><b>{bekleyenToplam}</b><span>Değerlendirme bekliyor</span></Link>
      </div>

      <div className="iki-sutun">
        <section className="kart">
          <h2>Değerlendirme bekleyenler</h2>
          {!ozet?.bekleyenler.length ? <div className="bos-durum"><b>Hepsi tamam ✓</b>Öğrenciler sınav teslim ettikçe burada görünür.</div> : (
            <div className="liste">
              {ozet.bekleyenler.map((b) => (
                <div key={b.atama_id} className="liste-satir">
                  <div>
                    <strong>{b.sinav_adi}</strong><br />
                    <small>{b.sinif_adi} · {b.teslim}/{b.ogrenci} teslim · {b.bekleyen} bekliyor</small>
                    <div className="ilerleme"><span style={{ width: `${b.ogrenci ? ((b.teslim - b.bekleyen) / b.ogrenci) * 100 : 0}%` }} /></div>
                  </div>
                  <Link className="dugme" to={`/atama/${b.atama_id}/teslimler`}>Değerlendir</Link>
                </div>
              ))}
            </div>
          )}
        </section>
        <section className="kart">
          <h2>EVALORA döngüsü</h2>
          <div className="dongu">
            <Link to="/sinavlar" className="dongu-adim olc"><i>1</i><div><b>Ölç</b><small>Soruları MK'lere eşle, sınavı hazırla ve sınıfa ata.</small></div></Link>
            <Link to="/sinavlar" className="dongu-adim teshis"><i>2</i><div><b>Teşhis et</b><small>Kâğıtları rubrik adımlarıyla değerlendir; sınıf raporunda eksik MK'leri gör.</small></div></Link>
            <Link to="/mk" className="dongu-adim telafi"><i>3</i><div><b>Telafi et</b><small>Öğrenci, eksik konusu için kısa anlatım ve benzer soru videolarını izler.</small></div></Link>
          </div>
        </section>
      </div>

      <div className="bolum-baslik"><h2>Sınıflarım</h2><button className="ikincil kucuk" onClick={() => setFormAcik(!formAcik)}>＋ Sınıf aç</button></div>
      {siniflar.length === 0 && <div className="kart bos-durum"><b>Henüz sınıfın yok</b>İlk sınıfını aç; öğrencilerin sınıf koduyla katılır.</div>}
      <div className="izgara">
        {siniflar.map((s) => (
          <div key={s.id} className={`kart sinif-kart ${s.ders}`}>
            <Link to={`/sinif/${s.id}`} className="ad">{s.ad}</Link>
            <span className="bilgi">{s.ders} · {s.sinif_duzeyi}. sınıf · {s.ogrenci_sayisi} öğrenci</span>
            <div className="alt">
              {s.kod && <span className="kod-cip" title="Öğrencilerin bu kodla katılır">{s.kod}</span>}
              <span className="linkler"><Link to={`/sinif/${s.id}`}>Sınıf</Link><Link to={`/sinif/${s.id}/rapor`}>📊 Rapor</Link></span>
            </div>
          </div>
        ))}
      </div>

      {(formAcik || siniflar.length === 0) && (
        <form className="kart" id="yeni-sinif" onSubmit={ac}>
          <h2>Yeni sınıf aç</h2>
          <div className="satir">
            <label>Sınıf adı<input value={ad} onChange={(e) => setAd(e.target.value)} placeholder="ör. 6-A Matematik" required /></label>
            <label>Ders
              <select value={ders} onChange={(e) => { setDers(e.target.value); setDuzey(e.target.value === "Fizik" ? 10 : 6); }}>
                <option>Matematik</option><option>Fizik</option>
              </select>
            </label>
            <label>Sınıf düzeyi
              <select value={duzey} onChange={(e) => setDuzey(Number(e.target.value))}>
                {duzeyler.map((d) => <option key={d} value={d}>{d}</option>)}
              </select>
            </label>
          </div>
          {hata && <p className="hata">{hata}</p>}
          <button>Sınıf aç</button>
        </form>
      )}
    </div>
  );
}
