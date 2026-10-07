import { useId } from "react";

// EVALORA logosu: birbirinin içinden geçen üç parçalı "e" döngüsü (turkuaz Ölç → mor Teşhis et → amber Telafi et);
// sağ üstteki parıltılar yapay zekâ desteğini gösterir.
export function LogoIsaret({ boyut = 36 }: { boyut?: number }) {
  const id = useId().replace(/:/g, "");
  // Üç parça (turkuaz Ölç, mor Teşhis et, amber Telafi et) birbirinin içinden geçer: dönen döngü.
  const parca = (d: string, renk: string) => <><path d={d} fill="none" stroke="#fff" strokeWidth="9.7" strokeLinecap="round" /><path d={d} fill="none" stroke={renk} strokeWidth="6.5" strokeLinecap="round" /></>;
  return (
    <svg width={boyut} height={boyut} viewBox="0 0 64 64" aria-hidden="true">
      <defs><linearGradient id={`${id}z`} x1="0" y1="0" x2="1" y2="1"><stop offset="0" stopColor="#ffffff" /><stop offset="1" stopColor="#eef2ff" /></linearGradient></defs>
      <rect width="64" height="64" rx="16" fill={`url(#${id}z)`} />
      <rect x=".5" y=".5" width="63" height="63" rx="15.5" fill="none" stroke="#c7d2fe" />
      {parca("M22.69 44.64 A13.5 13.5 0 0 0 42.19 41.55", "#f59e0b")}
      {parca("M24.25 22.31 A13.5 13.5 0 0 0 24.25 45.69", "#7c3aed")}
      {parca("M44.50 34.00 A13.5 13.5 0 0 0 22.69 23.36", "#14b8a6")}
      <path d="M18.5 34 H44.5" stroke="#14b8a6" strokeWidth="6.5" strokeLinecap="round" />
      <path d="M50 6.5 C50.728 11.18 51.82 12.272 56.5 13 C51.82 13.728 50.728 14.82 50 19.5 C49.272 14.82 48.18 13.728 43.5 13 C48.18 12.272 49.272 11.18 50 6.5Z" fill="#7c3aed" />
      <path d="M56 19.9 C56.2912 21.772 56.728 22.2088 58.6 22.5 C56.728 22.7912 56.2912 23.228 56 25.1 C55.7088 23.228 55.272 22.7912 53.4 22.5 C55.272 22.2088 55.7088 21.772 56 19.9Z" fill="#14b8a6" />
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
