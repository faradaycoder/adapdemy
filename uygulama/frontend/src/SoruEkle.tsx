import { useEffect, useMemo, useState } from "react";
import { api, gorselMi, type MufredatT, type SoruKisa } from "./api";
import { Mat } from "./Mat";

// Sınava soru ekleme paneli: sınıf → ders → ünite/tema → kazanım → mikro kazanım seçilir; o seçime bağlı bankadaki
// sorular (sorunun MK'si ya da bir rubrik adımı seçilen MK'lerden biri olanlar) sıralanır.
export default function SoruEkle({ ders: d0, duzey: s0, secili, ekle, kapat }: {
  ders: string; duzey: number; secili: number[]; ekle: (q: SoruKisa) => void; kapat: () => void;
}) {
  const [ders, setDers] = useState(d0);
  const [duzey, setDuzey] = useState(s0);
  const [agac, setAgac] = useState<MufredatT>([]);
  const [unite, setUnite] = useState<number | "">("");
  const [kazanim, setKazanim] = useState("");
  const [mk, setMk] = useState("");
  const [sorular, setSorular] = useState<SoruKisa[] | null>(null);
  const [hata, setHata] = useState("");

  useEffect(() => {
    setUnite(""); setKazanim(""); setMk("");
    api<MufredatT>(`/api/mufredat?ders=${ders}&sinif=${duzey}`).then(setAgac).catch((e) => setHata(e.message));
  }, [ders, duzey]);

  const u = agac.find((x) => x.no === unite);
  const k = u?.kazanimlar.find((x) => x.kod === kazanim);
  const mkKumesi = useMemo(() => mk ? [mk] : k ? k.mkler.map((m) => m.kod) : u ? u.kazanimlar.flatMap((x) => x.mkler.map((m) => m.kod)) : [], [mk, k, u]);

  useEffect(() => {
    setSorular(null);
    const q = new URLSearchParams({ ders, sinif: String(duzey) });
    if (mkKumesi.length) q.set("mkler", mkKumesi.join(","));
    api<SoruKisa[]>(`/api/sorular?${q}`).then(setSorular).catch((e) => setHata(e.message));
  }, [ders, duzey, mkKumesi]);

  const duzeyler = ders === "Fizik" ? [9, 10, 11, 12] : [5, 6, 7, 8, 9, 10, 11, 12];
  const say = (kodlar: string[]) => kodlar.length;
  const bagli = (q: SoruKisa) => [...q.mk_detay, ...q.onkosul_detay].filter((m) => mkKumesi.includes(m.kod));

  return (
    <div className="panel-zemin" onClick={kapat}>
      <div className="panel" onClick={(e) => e.stopPropagation()} role="dialog" aria-label="Soru ekle">
        <div className="panel-ust"><h2>Soru ekle</h2><button className="ikincil kucuk" onClick={kapat}>Kapat ✕</button></div>
        <div className="panel-icerik">
          <aside className="secimler">
            <label>Sınıf<select value={duzey} onChange={(e) => setDuzey(Number(e.target.value))}>{duzeyler.map((x) => <option key={x} value={x}>{x}. sınıf</option>)}</select></label>
            <label>Ders<select value={ders} onChange={(e) => { setDers(e.target.value); setDuzey(e.target.value === "Fizik" ? Math.max(9, duzey) : duzey); }}><option>Matematik</option><option>Fizik</option></select></label>
            <label>{ders === "Fizik" ? "Ünite" : "Tema"}
              <select value={unite} onChange={(e) => { setUnite(e.target.value ? Number(e.target.value) : ""); setKazanim(""); setMk(""); }}>
                <option value="">Hepsi</option>
                {agac.map((x) => <option key={x.no} value={x.no}>{x.no}. {x.ad}</option>)}
              </select></label>
            <label>Kazanım (öğrenme çıktısı)
              <select value={kazanim} disabled={!u} onChange={(e) => { setKazanim(e.target.value); setMk(""); }}>
                <option value="">{u ? "Hepsi" : "Önce ünite seç"}</option>
                {u?.kazanimlar.map((x) => <option key={x.kod} value={x.kod}>{x.kod} {x.ifade}</option>)}
              </select></label>
            {k && <p className="secim-aciklama">{k.ifade}</p>}
            <label>Mikro kazanım
              <select value={mk} disabled={!k} onChange={(e) => setMk(e.target.value)}>
                <option value="">{k ? `Hepsi (${say(k.mkler.map((m) => m.kod))} MK)` : "Önce kazanım seç"}</option>
                {k?.mkler.map((m) => <option key={m.kod} value={m.kod}>{m.soru_sayisi ? `● ${m.soru_sayisi} soru · ` : ""}{m.kod} {m.ifade}</option>)}
              </select></label>
            <p className="soluk kucuk-yazi">● yanındaki sayı, bankanda o mikro kazanımı ölçen soru sayısı.</p>
          </aside>
          <section className="sonuclar">
            <div className="sonuc-ust"><b>{sorular ? `${sorular.length} soru` : "Yükleniyor…"}</b>
              <span className="soluk">{mk ? `${mk} ile bağlı` : k ? `${k.kod} kazanımına bağlı` : u ? `${u.ad} ünitesine bağlı` : `${duzey}. sınıf ${ders} sorularının hepsi`}</span></div>
            {hata && <p className="hata">{hata}</p>}
            {sorular?.length === 0 && <div className="bos-durum"><b>Bu seçime bağlı soru yok</b>Bankaya soru yükleyebilir ya da başka bir kazanım seçebilirsin.</div>}
            <div className="aday-liste">
              {sorular?.map((q) => {
                const var_ = secili.includes(q.id);
                return (
                  <div key={q.id} className={`aday ${var_ ? "eklendi" : ""}`}>
                    {gorselMi(q.gorsel) ? <img src={`/api/gorsel/${q.gorsel}`} alt="" loading="lazy" /> : <p className="aday-metin"><Mat metin={q.metin} /></p>}
                    <div className="aday-alt">
                      <div className="etiketler">
                        {q.durum !== "onayli" && <span className="durum taslak">Taslak</span>}
                        <span className="seviye">Zorluk {q.zorluk?.toFixed(1)}</span>
                        {(mkKumesi.length ? bagli(q) : q.mk_detay).slice(0, 3).map((m) => <code key={m.kod} title={m.ifade}>{m.kod}</code>)}
                      </div>
                      <button className={var_ ? "ikincil kucuk" : "kucuk"} disabled={var_} onClick={() => ekle(q)}>{var_ ? "✓ Eklendi" : "＋ Ekle"}</button>
                    </div>
                  </div>
                );
              })}
            </div>
          </section>
        </div>
      </div>
    </div>
  );
}
