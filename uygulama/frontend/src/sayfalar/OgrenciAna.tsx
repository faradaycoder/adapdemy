import { useEffect, useState, type FormEvent } from "react";
import { Link } from "react-router-dom";
import { api, ATAMA_DURUMU, tarihSaat, type AtamaT, type Sinif } from "../api";

export default function OgrenciAna() {
  const [siniflar, setSiniflar] = useState<Sinif[]>([]);
  const [kod, setKod] = useState("");
  const [hata, setHata] = useState("");
  const [atamalar, setAtamalar] = useState<AtamaT[]>([]);
  const bekleyen = atamalar.filter((a) => a.durum === "acik" && a.teslim_durumu !== "teslim");
  const sonuclar = atamalar.filter((a) => a.sonuc_yeni);

  useEffect(() => {
    api<Sinif[]>("/api/siniflar").then(setSiniflar).catch((e) => setHata(e.message));
    api<AtamaT[]>("/api/atamalar").then(setAtamalar).catch(() => {});
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

  return (
    <div className="sayfa">
      {sonuclar.length > 0 && (
        <div className="kart basari">🔔 {sonuclar.length === 1 ? `“${sonuclar[0].sinav_adi}” sınavının sonucu açıklandı.` : `${sonuclar.length} sınavının sonucu açıklandı.`} Aşağıdan "Sonucu gör"e bas.</div>
      )}
      {bekleyen.length > 0 && (
        <div className="kart uyari-bandi">🔔 {bekleyen.length} açık sınavın var. Aşağıdan "Sınava gir"e bas.</div>
      )}
      <h1>Sınavlarım</h1>
      <section className="kart">
        {atamalar.length === 0 ? (
          <p className="soluk">{siniflar.length ? "Öğretmenin bir sınav atadığında burada görünecek." : "Henüz bir sınıfa katılmadın. Aşağıdan öğretmeninin verdiği kodla katıl; sınıfına atanan sınavlar burada görünür."}</p>
        ) : (
          <div className="o-sinav-liste">
            {atamalar.map((a) => (
              <div key={a.id} className="o-sinav-satir">
                <div>
                  <strong>{a.sinav_adi}</strong>
                  <span className="soluk"> · {a.sinif_adi} · {a.soru_sayisi} soru</span>
                  <div className="soluk">{tarihSaat(a.baslangic)} – {tarihSaat(a.bitis)}</div>
                </div>
                <div className="kucuk-dugmeler">
                  {a.teslim_durumu === "teslim"
                    ? (a.sonuc_acik
                      ? <><span className="durum onayli">Sonuç açıklandı</span><Link className="dugme" to={`/sonuc/${a.id}`}>Sonucu gör</Link></>
                      : <><span className="durum onayli">Teslim edildi</span><span className="soluk">Değerlendiriliyor</span><Link to={`/sinav/${a.id}`}>Cevaplarım</Link></>)
                    : <>
                      <span className={`durum ${a.durum === "acik" ? "onayli" : ""}`}>{ATAMA_DURUMU[a.durum]}</span>
                      {a.durum === "acik" && <Link className="dugme" to={`/sinav/${a.id}`}>{a.teslim_durumu === "devam" ? "Devam et" : "Sınava gir"}</Link>}
                      {a.durum === "acik" && <Link className="dugme ikincil" to={`/sinav/${a.id}/yazdir`} target="_blank"
                        title="Kâğıda yazdırıp çöz, sonra tarayıp yükle. Yazdırma ekranını açınca süren başlar.">🖨 Yazdır</Link>}
                      {a.durum === "bitti" && <Link to={`/sinav/${a.id}`}>Gör</Link>}
                    </>}
                </div>
              </div>
            ))}
          </div>
        )}
      </section>

      <h2>Sınıflarım</h2>
      <div className="izgara">
        {siniflar.map((s) => (
          <div key={s.id} className="kart sinif">
            <strong>{s.ad}</strong>
            <span>{s.ders} · {s.sinif_duzeyi}. sınıf</span>
            <span>Öğretmen: {s.ogretmen}</span>
          </div>
        ))}
      </div>

      <details className="kart" open={siniflar.length === 0}>
        <summary><strong>Yeni bir sınıfa katıl</strong></summary>
        <form onSubmit={katil} className="katil-form">
          <label>Öğretmeninin verdiği 6 haneli kod
            <input value={kod} onChange={(e) => setKod(e.target.value.toUpperCase())} maxLength={6} minLength={6} required className="kod-girdi" />
          </label>
          {hata && <p className="hata">{hata}</p>}
          <button>Katıl</button>
        </form>
      </details>
    </div>
  );
}
