import { useEffect, useMemo, useState } from "react";
import { api, gorselMi, type MufredatT, type SoruKisa } from "./api";
import { Mat } from "./Mat";

// Sınava soru ekleme paneli: sınıf → ders → ünite/tema → kazanım seçilir, kazanımın MK'leri işaretlenir (istendiği kadar,
// farklı kazanımlardan da). Seçilen MK'ler listelenir; bankadaki o MK'leri ölçen sorular (sorunun MK'si ya da bir rubrik
// adımı) sıralanır. MK seçilmemişken seçili kazanım ya da ünitenin soruları gösterilir.
export default function SoruEkle({ ders: d0, duzey: s0, secili, ekle, kapat }: {
  ders: string; duzey: number; secili: number[]; ekle: (q: SoruKisa) => void; kapat: () => void;
}) {
  const [ders, setDers] = useState(d0);
  const [duzey, setDuzey] = useState(s0);
  const [agac, setAgac] = useState<MufredatT>([]);
  const [unite, setUnite] = useState<number | "">("");
  const [kazanim, setKazanim] = useState("");
  const [secilen, setSecilen] = useState<{ kod: string; ifade: string }[]>([]);
  const [sorular, setSorular] = useState<SoruKisa[] | null>(null);
  const [hata, setHata] = useState("");

  useEffect(() => {
    setUnite(""); setKazanim(""); setHata("");
    api<MufredatT>(`/api/mufredat?ders=${ders}&sinif=${duzey}`).then(setAgac).catch((e) => setHata(e.message === "Not Found"
      ? "Müfredat alınamadı: sunucu eski sürümde çalışıyor. EVALORA penceresini kapatıp EVALORA-Baslat'ı yeniden aç." : e.message));
  }, [ders, duzey]);

  const u = agac.find((x) => x.no === unite);
  const k = u?.kazanimlar.find((x) => x.kod === kazanim);
  const mkKumesi = useMemo(() => secilen.length ? secilen.map((m) => m.kod) : k ? k.mkler.map((m) => m.kod)
    : u ? u.kazanimlar.flatMap((x) => x.mkler.map((m) => m.kod)) : [], [secilen, k, u]);
  const secili_mi = (kod: string) => secilen.some((m) => m.kod === kod);
  const degistir = (m: { kod: string; ifade: string }) =>
    setSecilen((l) => l.some((x) => x.kod === m.kod) ? l.filter((x) => x.kod !== m.kod) : [...l, { kod: m.kod, ifade: m.ifade }]);
  const hepsi = k ? k.mkler.every((m) => secili_mi(m.kod)) : false;
  const hepsiniDegistir = () => k && setSecilen((l) => hepsi ? l.filter((x) => !k.mkler.some((m) => m.kod === x.kod))
    : [...l, ...k.mkler.filter((m) => !l.some((x) => x.kod === m.kod)).map((m) => ({ kod: m.kod, ifade: m.ifade }))]);

  useEffect(() => {
    setSorular(null);
    const q = new URLSearchParams({ ders, sinif: String(duzey) });
    if (mkKumesi.length) q.set("mkler", mkKumesi.join(","));
    api<SoruKisa[]>(`/api/sorular?${q}`).then(setSorular).catch((e) => setHata(e.message));
  }, [ders, duzey, mkKumesi]);

  const duzeyler = ders === "Fizik" ? [9, 10, 11, 12] : [5, 6, 7, 8, 9, 10, 11, 12];
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
              <select value={unite} onChange={(e) => { setUnite(e.target.value ? Number(e.target.value) : ""); setKazanim(""); }}>
                <option value="">Hepsi</option>
                {agac.map((x) => <option key={x.no} value={x.no}>{x.no}. {x.ad}</option>)}
              </select></label>
            <label>Kazanım (öğrenme çıktısı)
              <select value={kazanim} disabled={!u} onChange={(e) => setKazanim(e.target.value)}>
                <option value="">{u ? "Hepsi" : "Önce ünite seç"}</option>
                {u?.kazanimlar.map((x) => <option key={x.kod} value={x.kod}>{x.kod} {x.ifade}</option>)}
              </select></label>
            {k && <p className="secim-aciklama">{k.ifade}</p>}
            {k && (
              <fieldset className="mk-liste">
                <legend>Mikro kazanımlar <span className="soluk">({k.mkler.length})</span>
                  <button type="button" className="bag" onClick={hepsiniDegistir}>{hepsi ? "Seçimi kaldır" : "Hepsini seç"}</button></legend>
                {k.mkler.map((m) => (
                  <label key={m.kod} className={`mk-satir ${secili_mi(m.kod) ? "secili" : ""}`}>
                    <input type="checkbox" checked={secili_mi(m.kod)} onChange={() => degistir(m)} />
                    <span><code>{m.kod}</code> {m.ifade}</span>
                    {m.soru_sayisi > 0 && <em title="Bankanda bu MK'yi ölçen soru sayısı">{m.soru_sayisi} soru</em>}
                  </label>
                ))}
              </fieldset>
            )}
            {!k && <p className="soluk kucuk-yazi">Bir kazanım seçince ona eşli mikro kazanımlar burada listelenir; istediğin kadarını işaretle.</p>}
          </aside>
          <section className="sonuclar">
            {secilen.length > 0 && (
              <div className="secilen-mkler">
                <div className="sonuc-ust"><b>Seçilen MK'ler ({secilen.length})</b><button className="bag" onClick={() => setSecilen([])}>Temizle</button></div>
                <div className="mk-cipler">{secilen.map((m) => (
                  <span key={m.kod} className="mk-cip" title={m.ifade}><code>{m.kod}</code> {m.ifade}<button aria-label={`${m.kod} kaldır`} onClick={() => degistir(m)}>✕</button></span>
                ))}</div>
              </div>
            )}
            <div className="sonuc-ust"><b>{sorular ? `${sorular.length} soru` : "Yükleniyor…"}</b>
              <span className="soluk">{secilen.length ? `seçilen ${secilen.length} MK'den en az birini ölçen` : k ? `${k.kod} kazanımına bağlı` : u ? `${u.ad} ünitesine bağlı` : `${duzey}. sınıf ${ders} sorularının hepsi`}</span></div>
            {hata && <p className="hata">{hata}</p>}
            {sorular?.length === 0 && <div className="bos-durum"><b>Bu seçime bağlı soru yok</b>Bankaya soru yükleyebilir ya da başka mikro kazanımlar seçebilirsin.</div>}
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
