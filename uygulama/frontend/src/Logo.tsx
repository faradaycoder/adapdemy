import { useId } from "react";

// EVALORA logosu. Üç renkli halka döngüyü anlatır: turkuaz Ölç, mor Teşhis et, amber Telafi et.
// İçteki yükselen düğümler MK haritasını ve öğrencinin ilerleyişini; amber uç, telafiyle ulaşılan hedefi gösterir.
export function LogoIsaret({ boyut = 36 }: { boyut?: number }) {
  const id = useId().replace(/:/g, "");
  return (
    <svg width={boyut} height={boyut} viewBox="0 0 64 64" aria-hidden="true">
      <defs><linearGradient id={id} x1="0" y1="0" x2="1" y2="1"><stop offset="0" stopColor="#1e3a8a" /><stop offset="1" stopColor="#3b5bdb" /></linearGradient></defs>
      <rect width="64" height="64" rx="16" fill={`url(#${id})`} />
      <g fill="none" strokeWidth="4.5" strokeLinecap="round">
        <path d="M33.66 13.07A19 19 0 0 1 49.22 40.03" stroke="#2dd4bf" />
        <path d="M47.56 42.90A19 19 0 0 1 16.44 42.90" stroke="#a78bfa" />
        <path d="M14.78 40.03A19 19 0 0 1 30.34 13.07" stroke="#fbbf24" />
      </g>
      <path d="M24 39 L31.5 31.5 L40.5 24" fill="none" stroke="#fff" strokeWidth="2.6" strokeLinecap="round" strokeLinejoin="round" />
      <circle cx="24" cy="39" r="3.2" fill="#fff" />
      <circle cx="31.5" cy="31.5" r="3.2" fill="#fff" />
      <circle cx="40.5" cy="24" r="4" fill="#fbbf24" stroke="#fff" strokeWidth="1.6" />
    </svg>
  );
}

export function Logo({ boyut = 36, slogan = true }: { boyut?: number; slogan?: boolean }) {
  return (
    <span className="logo-tam">
      <LogoIsaret boyut={boyut} />
      <span className="logo-yazi">
        <span className="logo-ad">EVALORA</span>
        {slogan && <span className="logo-slogan">Ölç · Teşhis et · Telafi et</span>}
      </span>
    </span>
  );
}
