import { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { api, tarihSaat, type UyKazanimT, type UyOturumKisaT, type UyOturumT } from "../api";
import { useOturum } from "../oturum";

// Uyarlamalı test girişi. Öğrenci: "Eksiğini bul" (kazanım seçer, test cevaplarına göre soru sorar). Öğretmen: aynı testi
// deneme olarak çözer (MK olasılıklarını canlı görür) ve öğrencilerinin testlerini listeler.
export default function Uyarlamali() {
  const { kullanici } = useOturum();
  const ogretmen = kullanici?.rol === "ogretmen";
  const git = useNavigate();
  const [kazanimlar, setKazanimlar] = useState<UyKazanimT[] | null>(null);
  const [oturumlar, setOturumlar] = useState<UyOturumKisaT[]>([]);
  const [hata, setHata] = useState("");

  useEffect(() => {
    api<UyKazanimT[]>("/api/uyarlamali/kazanimlar").then(setKazanimlar).catch((e) => setHata(e.message));
    api<UyOturumKisaT[]>("/api/uyarlamali/oturumlar").then(setOturumlar).catch(() => {});
  }, []);

  async function basla(kod: string) {
    setHata("");
    try { const o = await api<UyOturumT>("/api/uyarlamali", { govde: { kazanim: kod } }); git(`/uyarlamali/${o.id}`); }
    catch (e) { setHata((e as Error).message); }
  }

  return (
    <div className="sayfa uy">
      <div className="karsilama uy-karsilama">
        <h1>{ogretmen ? "Uyarlamalı test" : "Eksiğini bul"}</h1>
        <p>{ogretmen
          ? "Her soru, öğrencinin önceki cevaplarına göre seçilir: yanlışta ön koşula iner, doğruda yukarı çıkar ve eksiğin kökünü bulur. Deneme yaparken her adımda mikro kazanım olasılıklarını görürsün."
          : "Sorular cevaplarına göre seçilir. Bir soruyu yapamazsan sana daha temel bir soru gelir; böylece eksiğinin nerede başladığını buluruz ve sana o konunun videolarını öneririz."}</p>
      </div>
      {hata && <p className="hata">{hata}</p>}
      <div className="bolum-baslik"><h2>Kazanımlar</h2></div>
      {kazanimlar === null ? <p className="soluk">Yükleniyor…</p> : kazanimlar.length === 0 ? (
        <div className="bos-durum"><b>Henüz uyarlamalı test yok</b>{ogretmen ? "Soru havuzundaki sorular onaylanınca kazanımlar burada görünür." : "Öğretmenin soru havuzu hazırladığında burada görünecek."}</div>
      ) : (
        <div className="uy-kazanimlar">
          {kazanimlar.map((k) => (
            <div key={k.kod} className="kart uy-kazanim">
              <div className="uy-kazanim-ust"><code>{k.kod}</code><span className="soluk">{k.ders} · {k.sinif_duzeyi}. sınıf</span></div>
              <h3>{k.ifade}</h3>
              <p className="soluk">{k.mk_sayisi} mikro kazanım · havuzda {k.soru_sayisi} soru · en çok 20 soru</p>
              <button onClick={() => basla(k.kod)}>{ogretmen ? "▶ Dene" : "▶ Başla"}</button>
            </div>
          ))}
        </div>
      )}
      {oturumlar.length > 0 && <>
        <div className="bolum-baslik"><h2>{ogretmen ? "Öğrencilerin testleri" : "Testlerim"}</h2></div>
        <div className="kart tablo-kap">
          <table>
            <thead><tr>{ogretmen && <th>Öğrenci</th>}<th>Kazanım</th><th>Tarih</th><th>Soru</th><th>Eksiğin kökü</th><th></th></tr></thead>
            <tbody>
              {oturumlar.map((o) => (
                <tr key={o.id}>
                  {ogretmen && <td>{o.ogrenci}</td>}
                  <td><code>{o.kazanim}</code></td>
                  <td>{tarihSaat(o.baslama)}</td>
                  <td>{o.soru}</td>
                  <td>{o.durum === "devam" ? <span className="durum">Devam ediyor</span> : o.kokler.length ? o.kokler.map((k) => <code key={k} className="uy-kok">{k}</code>) : <span className="durum onayli">Eksik bulunmadı</span>}</td>
                  <td><Link className="dugme ikincil kucuk" to={`/uyarlamali/${o.id}`}>{o.durum === "devam" && !ogretmen ? "Devam et" : "Aç"}</Link></td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </>}
    </div>
  );
}
