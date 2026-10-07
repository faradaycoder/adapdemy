import { useEffect, useMemo, useState } from "react";
import { Mat } from "../Mat";
import { Link } from "react-router-dom";
import { RubrikTablo } from "../Rubrik";
import { api, CEVAP_BICIMLERI, gorselMi, type Soru, type SoruKisa } from "../api";

// Soru bankası: üstte filtreler (arama, ders, sınıf, durum, MK), altta soru kartları. Her kartta üç büyük düğme:
// MK'ler, Zorluk (MK zorluklarından soru zorluğuna) ve Çözüm ve rubrik; tıklanan, kartın altında açılır.
type Panel = "mk" | "zorluk" | "rubrik";

export default function SoruBankasi() {
  const [sorular, setSorular] = useState<SoruKisa[]>([]);
  const [yuklendi, setYuklendi] = useState(false);
  const [ders, setDers] = useState("");
  const [sinif, setSinif] = useState("");
  const [durum, setDurum] = useState("");
  const [mk, setMk] = useState("");
  const [ara, setAra] = useState("");
  const [sira, setSira] = useState<"yeni" | "zor" | "kolay">("yeni");
  const [hata, setHata] = useState("");
  const [secili, setSecili] = useState<Set<number>>(new Set());
  const [yenile, setYenile] = useState(0);

  useEffect(() => {
    const p = new URLSearchParams();
    if (ders) p.set("ders", ders);
    if (sinif) p.set("sinif", sinif);
    if (durum) p.set("durum", durum);
    if (mk.trim()) p.set("mk", mk.trim());
    api<SoruKisa[]>(`/api/sorular?${p}`).then((l) => { setSorular(l); setSecili(new Set()); setYuklendi(true); }).catch((e) => setHata(e.message));
  }, [ders, sinif, durum, mk, yenile]);

  const gorunen = useMemo(() => {
    const a = ara.trim().toLocaleLowerCase("tr");
    const l = a ? sorular.filter((s) => s.metin.toLocaleLowerCase("tr").includes(a)
      || s.mk_detay.some((m) => m.kod.toLowerCase().includes(a) || m.ifade.toLocaleLowerCase("tr").includes(a))) : sorular;
    return sira === "yeni" ? l : [...l].sort((x, y) => ((x.zorluk ?? 0) - (y.zorluk ?? 0)) * (sira === "zor" ? -1 : 1));
  }, [sorular, ara, sira]);
  const taslaklar = gorunen.filter((s) => s.durum === "taslak");
  const enZor = Math.max(10, ...sorular.map((s) => s.zorluk ?? 0));
  const siniflar = ders === "Fizik" ? [9, 10, 11, 12] : ders === "Matematik" ? [5, 6, 7, 8, 9, 10, 11, 12] : [5, 6, 7, 8, 9, 10, 11, 12];

  function sec(id: number) {
    const y = new Set(secili);
    y.has(id) ? y.delete(id) : y.add(id);
    setSecili(y);
  }

  async function onayla(idler: number[]) {
    setHata("");
    try {
      await api("/api/sorular/toplu-onayla", { govde: { idler } });
      setYenile(yenile + 1);
    } catch (e) { setHata((e as Error).message); }
  }

  const cip = (deger: string, aktif: string, ayarla: (x: string) => void, ad: string) =>
    <button type="button" className={`filtre-cip ${aktif === deger ? "aktif" : ""}`} aria-pressed={aktif === deger} onClick={() => ayarla(deger)}>{ad}</button>;

  return (
    <div className="sayfa soru-bankasi">
      <div className="baslik-satiri">
        <div>
          <h1>Soru bankası</h1>
          <p className="soluk banka-ozet">{gorunen.length} soru{taslaklar.length ? ` · ${taslaklar.length} taslak onay bekliyor` : ""}</p>
        </div>
        <Link to="/sorular/yukle" className="dugme buyuk-dugme">＋ Soru ekle</Link>
      </div>

      <div className="kart banka-filtre">
        <input className="banka-ara" type="search" value={ara} onChange={(e) => setAra(e.target.value)} placeholder="Soru metninde, MK kodunda ya da MK ifadesinde ara…" />
        <div className="filtre-satir">
          <div className="filtre-grup"><span>Ders</span>{cip("", ders, (x) => { setDers(x); setSinif(""); }, "Hepsi")}{cip("Matematik", ders, (x) => { setDers(x); setSinif(""); }, "Matematik")}{cip("Fizik", ders, (x) => { setDers(x); setSinif(""); }, "Fizik")}</div>
          <div className="filtre-grup"><span>Durum</span>{cip("", durum, setDurum, "Hepsi")}{cip("taslak", durum, setDurum, "Taslak")}{cip("onayli", durum, setDurum, "Onaylı")}</div>
          <label className="filtre-grup"><span>Sınıf</span>
            <select value={sinif} onChange={(e) => setSinif(e.target.value)}><option value="">Hepsi</option>{siniflar.map((x) => <option key={x} value={x}>{x}. sınıf</option>)}</select></label>
          <label className="filtre-grup"><span>MK kodu</span><input value={mk} onChange={(e) => setMk(e.target.value)} placeholder="ör. Mat01MK0065" /></label>
          <label className="filtre-grup"><span>Sırala</span>
            <select value={sira} onChange={(e) => setSira(e.target.value as typeof sira)}><option value="yeni">En yeni</option><option value="zor">En zor</option><option value="kolay">En kolay</option></select></label>
        </div>
      </div>

      {taslaklar.length > 0 && (
        <div className="toplu banka-toplu">
          <label className="secenek"><input type="checkbox" checked={taslaklar.every((s) => secili.has(s.id))}
            onChange={(e) => setSecili(e.target.checked ? new Set(taslaklar.map((s) => s.id)) : new Set())} /> Tüm taslakları seç</label>
          <button disabled={secili.size === 0} onClick={() => onayla([...secili])}>✓ Seçilenleri onayla ({secili.size})</button>
        </div>
      )}
      {hata && <p className="hata">{hata}</p>}
      {yuklendi && gorunen.length === 0 ? (
        <div className="bos-durum"><b>{sorular.length ? "Aramaya uyan soru yok" : "Henüz soru yok"}</b>
          {sorular.length ? "Filtreleri değiştirebilir ya da aramayı temizleyebilirsin." : "\"Soru ekle\" ile bir soruyu fotoğraf, görsel ya da metin olarak yükle; sistem okur, çözer ve MK'lere eşler."}</div>
      ) : (
        <div className="banka-liste">
          {gorunen.map((s, i) => <SoruKarti key={s.id} s={s} no={i + 1} enZor={enZor} secili={secili.has(s.id)} sec={() => sec(s.id)} />)}
        </div>
      )}
    </div>
  );
}

function SoruKarti({ s, no, enZor, secili, sec }: { s: SoruKisa; no: number; enZor: number; secili: boolean; sec: () => void }) {
  const [panel, setPanel] = useState<Panel | null>(null);
  const [tam, setTam] = useState<Soru | null>(null);
  const [hata, setHata] = useState("");
  const ac = (p: Panel) => {
    if (p === "rubrik" && !tam) api<Soru>(`/api/sorular/${s.id}`).then(setTam).catch((e) => setHata(e.message));
    setPanel(panel === p ? null : p);
  };
  const z = s.zorluk ?? 0;
  const dolu = Math.max(1, Math.round((z / enZor) * 5));
  return (
    <article className={`kart bk-kart ${s.durum} ${secili ? "secili" : ""}`}>
      <div className="bk-ust">
        {s.durum === "taslak" && <input type="checkbox" aria-label="Onay için seç" checked={secili} onChange={sec} />}
        <span className="bk-no">#{no}</span>
        <span className={`durum ${s.durum}`}>{s.durum === "onayli" ? "Onaylı" : "Taslak"}</span>
        <span className="bk-meta">{s.ders} · {s.sinif_duzeyi}. sınıf · {CEVAP_BICIMLERI[s.cevap_bicimi]}</span>
        <Link to={`/sorular/${s.id}`} className="dugme ikincil kucuk bk-duzenle">✎ Aç ve düzenle</Link>
      </div>
      <Link to={`/sorular/${s.id}`} className="bk-govde">
        {s.gorsel && (gorselMi(s.gorsel) ? <img src={`/api/gorsel/${s.gorsel}`} alt="" loading="lazy" /> : <span className="pdf-rozet">PDF</span>)}
        <div className="bk-metin"><Mat metin={s.metin} /></div>
      </Link>
      <div className="bk-araclar" role="tablist">
        <button type="button" role="tab" aria-selected={panel === "mk"} className={`bk-arac mk ${panel === "mk" ? "aktif" : ""}`} onClick={() => ac("mk")}>
          <i>🎯</i><span><small>Mikro kazanımlar</small><b>{s.mk_detay.length} MK{s.onkosul_detay.length ? ` + ${s.onkosul_detay.length} ön koşul` : ""}</b></span>
        </button>
        <button type="button" role="tab" aria-selected={panel === "zorluk"} className={`bk-arac zorluk ${panel === "zorluk" ? "aktif" : ""}`} onClick={() => ac("zorluk")}>
          <i>📶</i><span><small>Soru zorluğu</small><b>{s.zorluk != null ? z.toFixed(2) : "–"}</b></span>
          <span className="bk-olcek" aria-hidden="true">{[1, 2, 3, 4, 5].map((k) => <em key={k} className={k <= dolu ? "dolu" : ""} />)}</span>
        </button>
        <button type="button" role="tab" aria-selected={panel === "rubrik"} className={`bk-arac rubrik ${panel === "rubrik" ? "aktif" : ""}`} onClick={() => ac("rubrik")}>
          <i>🧩</i><span><small>Çözüm ve</small><b>Rubrik</b></span>
        </button>
      </div>
      {panel === "mk" && (
        <div className="bk-panel mk">
          <ul className="bk-mkler">
            {s.mk_detay.map((m) => (
              <li key={m.kod}>
                <Link to={`/mk/${m.kod}`}><code className={m.kod === s.birincil ? "birincil" : ""}>{m.kod}</code></Link>
                <span>{m.ifade}{m.kod === s.birincil && <em className="bk-birincil">birincil</em>}</span>
                {m.zorluk != null && <small>Z {m.zorluk.toFixed(2)}</small>}
              </li>
            ))}
          </ul>
          {s.onkosul_detay.length > 0 && (<>
            <p className="bk-alt-baslik">Rubrikte teşhis için geçen ön koşullar</p>
            <ul className="bk-mkler onkosul">
              {s.onkosul_detay.map((m) => <li key={m.kod}><Link to={`/mk/${m.kod}`}><code>{m.kod}</code></Link><span>{m.ifade}</span>{m.zorluk != null && <small>Z {m.zorluk.toFixed(2)}</small>}</li>)}
            </ul>
          </>)}
        </div>
      )}
      {panel === "zorluk" && (
        <div className="bk-panel zorluk">
          <p className="soluk">Soru zorluğu, sorunun ölçtüğü MK'lerin zorluklarının toplamıdır (b = ΣZ). Bir MK'nin zorluğu, eklediği adım ile ön koşul zincirinden gelir.</p>
          <ul className="bk-zorluk-liste">
            {s.mk_detay.map((m) => (
              <li key={m.kod}>
                <code>{m.kod}</code><span>{m.ifade}</span>
                <span className="bk-cubuk"><em style={{ width: `${Math.min(100, ((m.zorluk ?? 0) / Math.max(z, 1)) * 100)}%` }} /></span>
                <b>{m.zorluk != null ? m.zorluk.toFixed(2) : "–"}</b>
              </li>
            ))}
            <li className="toplam"><span>Toplam (soru zorluğu)</span><b>{z.toFixed(2)}</b></li>
          </ul>
        </div>
      )}
      {panel === "rubrik" && (
        <div className="bk-panel rubrik">
          {hata ? <p className="hata">{hata}</p> : tam ? <RubrikTablo s={tam} /> : <p className="soluk">Yükleniyor…</p>}
        </div>
      )}
    </article>
  );
}
