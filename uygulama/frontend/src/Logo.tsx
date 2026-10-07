import { useId } from "react";

// EVALORA logosu: renk geçişli "e" (turkuaz Ölç → mor Teşhis et → amber Telafi et) ve ucundaki ok döngüyü anlatır:
// telafiden sonra yeniden ölçülür. Sağ üstteki parıltılar yapay zekâ desteğini gösterir.
export function LogoIsaret({ boyut = 36 }: { boyut?: number }) {
  const id = useId().replace(/:/g, "");
  return (
    <svg width={boyut} height={boyut} viewBox="0 0 64 64" aria-hidden="true">
      <defs>
        <linearGradient id={`${id}z`} x1="0" y1="0" x2="1" y2="1"><stop offset="0" stopColor="#ffffff" /><stop offset="1" stopColor="#eef2ff" /></linearGradient>
        <linearGradient id={`${id}c`} gradientUnits="userSpaceOnUse" x1="14" y1="22" x2="46" y2="48">
          <stop offset="0" stopColor="#2dd4bf" /><stop offset=".5" stopColor="#8b5cf6" /><stop offset="1" stopColor="#f59e0b" />
        </linearGradient>
      </defs>
      <rect width="64" height="64" rx="16" fill={`url(#${id}z)`} />
      <rect x=".5" y=".5" width="63" height="63" rx="15.5" fill="none" stroke="#c7d2fe" />
      <path d="M16.5 34 H43.5 A13.5 13.5 0 1 0 40.34 42.68" fill="none" stroke={`url(#${id}c)`} strokeWidth="6.5" strokeLinecap="round" />
      <path d="M43.88 38.46 L42.59 46.53 L36.16 41.13Z" fill="#f59e0b" stroke="#f59e0b" strokeWidth="1.5" strokeLinejoin="round" />
      <path d="M49 7.5 C49.84 12.9 51.1 14.16 56.5 15 C51.1 15.84 49.84 17.1 49 22.5 C48.16 17.1 46.9 15.84 41.5 15 C46.9 14.16 48.16 12.9 49 7.5Z" fill="#8b5cf6" />
      <path d="M55.5 22 C55.836 24.16 56.34 24.664 58.5 25 C56.34 25.336 55.836 25.84 55.5 28 C55.164 25.84 54.66 25.336 52.5 25 C54.66 24.664 55.164 24.16 55.5 22Z" fill="#2dd4bf" opacity=".9" />
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
