// Metindeki LaTeX'i KaTeX ile çizer: $...$ satır içi, $$...$$ ayrı satırda. KaTeX index.html'den (CDN) gelir;
// yüklenemezse metin olduğu gibi görünür. Sorular, çözümler ve rubrik adımları bu biçimde yazılabilir.
declare global {
  interface Window { katex?: { renderToString(tex: string, secenek?: object): string } }
}

const PARCA = /(\$\$[\s\S]+?\$\$|\$[^$\n]+?\$)/g;

function matMi(p: string): "blok" | "satir" | null {
  if (p.length > 4 && p.startsWith("$$") && p.endsWith("$$")) return "blok";
  if (p.length > 2 && p.startsWith("$") && p.endsWith("$")) return "satir";
  return null;
}

export function Mat({ metin }: { metin: string | null | undefined }) {
  const k = window.katex;
  if (!metin) return null;
  if (!k || !metin.includes("$")) return <>{metin}</>;
  return <>{metin.split(PARCA).map((p, i) => {
    const tur = matMi(p);
    if (!tur) return p;
    const html = k.renderToString(p.slice(tur === "blok" ? 2 : 1, tur === "blok" ? -2 : -1), { throwOnError: false, displayMode: tur === "blok" });
    return <span key={i} dangerouslySetInnerHTML={{ __html: html }} />;
  })}</>;
}

// Metni ayraçla böler ama $...$ içindeki ayraçlara dokunmaz (çözümü adımlara ayırırken formül bölünmesin).
export function matDisindaBol(metin: string, ayrac: RegExp): string[] {
  const parcalar: string[] = [];
  let simdiki = "";
  for (const p of metin.split(PARCA)) {
    if (matMi(p)) { simdiki += p; continue; }
    const b = p.split(ayrac);
    simdiki += b[0];
    for (const x of b.slice(1)) { parcalar.push(simdiki); simdiki = x; }
  }
  parcalar.push(simdiki);
  return parcalar.map((x) => x.trim()).filter(Boolean);
}

// Çözüm metnini adımlara ayırır (cümle sonları ve a) b) şıkları); tek adımsa metni olduğu gibi gösterir.
export function cozumAdimlari(metin: string): string[] {
  return matDisindaBol(metin, /(?<=\.)\s+(?=[A-ZÇĞİÖŞÜ(]|[a-zçğıöşü]\()|\s+(?=[a-h]\)\s)/);
}

export function CozumMetni({ metin }: { metin: string }) {
  const a = cozumAdimlari(metin);
  return a.length > 1 ? <ol className="cozum-adimlari">{a.map((x, i) => <li key={i}><Mat metin={x} /></li>)}</ol> : <p className="t-metin"><Mat metin={metin} /></p>;
}
