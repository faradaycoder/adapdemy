import { useId } from "react";

// EVALORA logosu: renk geçişli "e" (turkuaz Ölç → mor Teşhis et → amber Telafi et); sağ üstteki parıltılar yapay zekâ
// desteğini gösterir.
export function LogoIsaret({ boyut = 36 }: { boyut?: number }) {
  const id = useId().replace(/:/g, "");
  return (
    <svg width={boyut} height={boyut} viewBox="0 0 64 64" aria-hidden="true">
      <defs>
        <linearGradient id={`${id}z`} x1="0" y1="0" x2="1" y2="1"><stop offset="0" stopColor="#ffffff" /><stop offset="1" stopColor="#eef2ff" /></linearGradient>
        <linearGradient id={`${id}c`} gradientUnits="userSpaceOnUse" x1="14" y1="20" x2="48" y2="48">
          <stop offset="0" stopColor="#14b8a6" /><stop offset=".5" stopColor="#7c3aed" /><stop offset="1" stopColor="#f59e0b" />
        </linearGradient>
      </defs>
      <rect width="64" height="64" rx="16" fill={`url(#${id}z)`} />
      <rect x=".5" y=".5" width="63" height="63" rx="15.5" fill="none" stroke="#c7d2fe" />
      <path d="M16.5 34 H43.5 A13.5 13.5 0 1 0 41.06 41.74" fill="none" stroke={`url(#${id}c)`} strokeWidth="6.5" strokeLinecap="round" />
      <path d="M49 8 C49.784 13.04 50.96 14.216 56 15 C50.96 15.784 49.784 16.96 49 22 C48.216 16.96 47.04 15.784 42 15 C47.04 14.216 48.216 13.04 49 8Z" fill="#7c3aed" />
      <path d="M55.5 22.2 C55.8136 24.216 56.284 24.6864 58.3 25 C56.284 25.3136 55.8136 25.784 55.5 27.8 C55.1864 25.784 54.716 25.3136 52.7 25 C54.716 24.6864 55.1864 24.216 55.5 22.2Z" fill="#14b8a6" />
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
