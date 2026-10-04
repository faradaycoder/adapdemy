import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { api, type Analiz, type Ornek } from "../api";

function base64Oku(dosya: File): Promise<string> {
  return new Promise((coz, red) => {
    const r = new FileReader();
    r.onload = () => coz(String(r.result));
    r.onerror = () => red(new Error("Dosya okunamadı."));
    r.readAsDataURL(dosya);
  });
}

export default function SoruYukle() {
  const git = useNavigate();
  const [ders, setDers] = useState("Fizik");
  const [duzey, setDuzey] = useState(10);
  const [metin, setMetin] = useState("");
  const [dosya, setDosya] = useState<File | null>(null);
  const [onizleme, setOnizleme] = useState<string | null>(null);
  const [saglayici, setSaglayici] = useState<{ ad: string; ornekler: Ornek[] } | null>(null);
  const [bekle, setBekle] = useState(false);
  const [hata, setHata] = useState("");

  useEffect(() => { api<{ ad: string; ornekler: Ornek[] }>("/api/sorular/saglayici").then(setSaglayici).catch(() => {}); }, []);

  async function analizEt(govde: Record<string, unknown>) {
    setHata(""); setBekle(true);
    try {
      const a = await api<Analiz>("/api/sorular/analiz", { govde });
      git("/sorular/yeni", { state: a });
    } catch (e) { setHata((e as Error).message); } finally { setBekle(false); }
  }

  async function gonder() {
    const gorsel_base64 = dosya ? await base64Oku(dosya) : null;
    analizEt({ ders, sinif_duzeyi: duzey, gorsel_base64, metin: metin || null });
  }

  function dosyaSec(f: File | null) {
    setDosya(f);
    setOnizleme(f ? URL.createObjectURL(f) : null);
  }

  const duzeyler = ders === "Fizik" ? [9, 10, 11, 12] : [5, 6, 7, 8, 9, 10, 11, 12];

  return (
    <div className="sayfa">
      <h1>Soru ekle</h1>
      {saglayici?.ad === "azure-okuma" && (
        <div className="kart vurgu bilgi">
          <strong>Azure okuma modu.</strong> Yüklediğin görsel ya da PDF Azure ile okunur ve metne çevrilir; sistem kelime
          benzerliğiyle aday MK'ler önerir. Çözümü, rubrik adımlarını ve MK'leri sen tamamlarsın. (Yapay zekâ kotası gelince
          bunlar da otomatik olacak.) Hazır örnekler yine tanınır.
        </div>
      )}
      {saglayici?.ad === "azure" && (
        <div className="kart vurgu bilgi"><strong>Azure yapay zekâ modu.</strong> Soru okunur, çözülür ve MK'lere eşlenir; sen kontrol edip kaydedersin.</div>
      )}
      {saglayici?.ad === "demo" && (
        <div className="kart vurgu bilgi">
          <strong>Demo modu.</strong> API anahtarı eklenene kadar sistem yalnız aşağıdaki örnek soruları tanır.
          Örneklerden birini seç ya da örnek görsellerden birini yükle.
        </div>
      )}

      <section className="kart">
        <h2>Kendi sorunu yükle</h2>
        <div className="satir">
          <label>Ders<select value={ders} onChange={(e) => { setDers(e.target.value); setDuzey(e.target.value === "Fizik" ? 10 : 8); }}><option>Fizik</option><option>Matematik</option></select></label>
          <label>Sınıf<select value={duzey} onChange={(e) => setDuzey(Number(e.target.value))}>{duzeyler.map((d) => <option key={d} value={d}>{d}</option>)}</select></label>
        </div>
        <div className="satir">
          <label>Fotoğraf çek (telefonda kamera açılır)
            <input type="file" accept="image/png,image/jpeg" capture="environment" onChange={(e) => dosyaSec(e.target.files?.[0] ?? null)} />
          </label>
          <label>ya da dosya seç (PNG, JPEG, PDF)
            <input type="file" accept="image/png,image/jpeg,application/pdf" onChange={(e) => dosyaSec(e.target.files?.[0] ?? null)} />
          </label>
        </div>
        {onizleme && (dosya?.type === "application/pdf"
          ? <iframe src={onizleme} title="Yüklenen PDF" className="onizleme pdf" />
          : <img src={onizleme} alt="Yüklenen soru" className="onizleme" />)}
        <label>ya da soru metni
          <textarea value={metin} onChange={(e) => setMetin(e.target.value)} rows={4} placeholder="Soruyu buraya yazabilir ya da yapıştırabilirsin." />
        </label>
        {hata && <p className="hata">{hata}</p>}
        <button disabled={bekle || (!dosya && !metin.trim())} onClick={gonder}>{bekle ? "Okunuyor ve eşleniyor…" : "Oku, çöz ve MK'lere eşle"}</button>
      </section>

      {saglayici && (
        <section className="kart">
          <h2>Örnek sorular</h2>
          <div className="izgara">
            {saglayici.ornekler.map((o) => (
              <button key={o.anahtar} className="ikincil ornek" disabled={bekle}
                onClick={() => analizEt({ ders: o.ders, sinif_duzeyi: o.sinif_duzeyi, ornek: o.anahtar })}>
                <strong>{o.baslik}</strong>
                <span>{o.ders} · {o.sinif_duzeyi}. sınıf{o.gorsel ? " · görsel" : " · metin"}</span>
              </button>
            ))}
          </div>
        </section>
      )}
    </div>
  );
}
