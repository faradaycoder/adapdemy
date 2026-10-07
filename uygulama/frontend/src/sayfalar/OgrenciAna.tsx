import { useEffect, useState, type FormEvent } from "react";
import { Link } from "react-router-dom";
import { api, ATAMA_DURUMU, selam, tarihSaat, type AtamaT, type OzetT, type Sinif } from "../api";
import { useOturum } from "../oturum";

// Öğrenci ana sayfası: karşılama ve konu durumu, açık sınavlar, sonuçlar, sınıflar ve sınıfa katılma.
export default function OgrenciAna() {
  const { kullanici } = useOturum();
  const [siniflar, setSiniflar] = useState<Sinif[]>([]);
  const [kod, setKod] = useState("");
  const [hata, setHata] = useState("");
  const [atamalar, setAtamalar] = useState<AtamaT[]>([]);
  const [ozet, setOzet] = useState<OzetT | null>(null);

  useEffect(() => {
    api<Sinif[]>("/api/siniflar").then(setSiniflar).catch((e) => setHata(e.message));
    api<AtamaT[]>("/api/atamalar").then(setAtamalar).catch(() => {});
    api<OzetT>("/api/ozet").then(setOzet).catch(() => {});
  }, []);

  async function katil(e: FormEvent) {
    e.preventDefault();
    setHata("");
    try {
      const s = await api<Sinif>("/api/siniflar/katil", { govde: { kod } });
      if (!siniflar.some((x) => x.id === s.id)) setSiniflar([...siniflar, s]);
      setKod("");
    } catch (err) { setHata((err as Error).message); }
  }

  const acik = atamalar.filter((a) => a.durum === "acik" && a.teslim_durumu !== "teslim");
  const digerleri = atamalar.filter((a) => !acik.includes(a));
  const yeniSonuc = atamalar.filter((a) => a.sonuc_yeni).length;
  const mk = ozet?.mk ?? {};

  return (
    <div className="sayfa">
      <section className="karsilama">
        <h1>{selam()}, {kullanici?.ad?.split(" ")[0]} 👋</h1>
        <p>{acik.length ? `${acik.length} açık sınavın var.` : "Şu an açık sınavın yok."}{yeniSonuc ? ` ${yeniSonuc} yeni sonucun açıklandı.` : ""} Her sınavdan sonra hangi konuları bildiğini, hangilerini tekrar etmen gerektiğini görürsün.</p>
        <div className="eylemler"><Link className="dugme" to="/rapor">📊 Konu raporum</Link></div>
      </section>

      <div className="sayilar">
        <Link className="sayi-kutu biliyor" to="/rapor"><b>{mk.biliyor ?? 0}</b><span>Bildiğin konu</span></Link>
        <Link className="sayi-kutu belirsiz" to="/rapor"><b>{mk.belirsiz ?? 0}</b><span>Biraz daha çalış</span></Link>
        <Link className="sayi-kutu bilmiyor" to="/rapor"><b>{mk.bilmiyor ?? 0}</b><span>Tekrar etmen gereken</span></Link>
      </div>

      <div className="bolum-baslik"><h2>Açık sınavlar</h2></div>
      {acik.length === 0 ? (
        <div className="kart bos-durum"><b>Şimdilik sınav yok</b>{siniflar.length ? "Öğretmenin bir sınav atadığında burada görünecek." : "Önce aşağıdan öğretmeninin verdiği kodla sınıfına katıl."}</div>
      ) : (
        <div className="sinav-kartlar">
          {acik.map((a) => (
            <div key={a.id} className="kart sinav-kart">
              <div className="ust-satir"><strong>{a.sinav_adi}</strong><span className="durum onayli">{a.teslim_durumu === "devam" ? "Devam ediyor" : "Açık"}</span></div>
              <small className="soluk">{a.sinif_adi} · {a.soru_sayisi} soru · Son: {tarihSaat(a.bitis)}</small>
              <div className="eylemler">
                <Link className="dugme" to={`/sinav/${a.id}`}>{a.teslim_durumu === "devam" ? "Devam et" : "Sınava gir"}</Link>
                <Link className="dugme ikincil" to={`/sinav/${a.id}/yazdir`} target="_blank" title="Kâğıda yazdırıp çöz, sonra fotoğrafını yükle. Yazdırma ekranını açınca süren başlar.">🖨 Yazdır</Link>
              </div>
            </div>
          ))}
        </div>
      )}

      {digerleri.length > 0 && <>
        <div className="bolum-baslik"><h2>Sonuçlar ve geçmiş</h2></div>
        <section className="kart">
          <div className="liste">
            {digerleri.map((a) => (
              <div key={a.id} className="liste-satir">
                <div><strong>{a.sinav_adi}</strong><br /><small>{a.sinif_adi} · {tarihSaat(a.baslangic)}</small></div>
                <div className="kucuk-dugmeler">
                  {a.sonuc_acik ? <>{a.sonuc_yeni && <span className="durum">Yeni</span>}<Link className="dugme" to={`/sonuc/${a.id}`}>Sonucu gör</Link></>
                    : a.teslim_durumu === "teslim" ? <><span className="durum onayli">Teslim edildi</span><small>Değerlendiriliyor</small></>
                    : <><span className="durum">{ATAMA_DURUMU[a.durum]}</span>{a.durum === "bitti" && <Link to={`/sinav/${a.id}`}>Gör</Link>}</>}
                </div>
              </div>
            ))}
          </div>
        </section>
      </>}

      <div className="bolum-baslik"><h2>Sınıflarım</h2></div>
      <div className="izgara">
        {siniflar.map((s) => (
          <div key={s.id} className={`kart sinif-kart ${s.ders}`}>
            <span className="ad">{s.ad}</span>
            <span className="bilgi">{s.ders} · {s.sinif_duzeyi}. sınıf</span>
            <span className="bilgi">Öğretmen: {s.ogretmen}</span>
          </div>
        ))}
        <form onSubmit={katil} className="kart sinif-kart katil-form">
          <span className="ad">Yeni sınıfa katıl</span>
          <label>Öğretmeninin verdiği 6 haneli kod
            <input value={kod} onChange={(e) => setKod(e.target.value.toUpperCase())} maxLength={6} minLength={6} required className="kod-girdi" placeholder="ABC123" />
          </label>
          {hata && <p className="hata">{hata}</p>}
          <button>Katıl</button>
        </form>
      </div>
    </div>
  );
}
