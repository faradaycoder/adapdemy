import { useId } from "react";

// EVALORA logosu: ortada beyin (öğrenme ve yapay zekâ desteği), çevresinde dönen döngü:
// mavi Ölç (grafik) → turkuaz Teşhis et (büyüteç) → mor Telafi et (oynat). koyuZemin: beyin çizgileri beyaz.
export const RENK = { olc: "#2563eb", teshis: "#14b8a6", telafi: "#8b5cf6", lacivert: "#13306a" };

export function LogoIsaret({ boyut = 36, koyuZemin = false }: { boyut?: number; koyuZemin?: boolean }) {
  const id = useId().replace(/:/g, "");
  const cizgi = koyuZemin ? "#fff" : RENK.lacivert;
  const gec = (ad: string, x1: number, y1: number, x2: number, y2: number, r1: string, r2: string) => (
    <linearGradient id={`${id}${ad}`} gradientUnits="userSpaceOnUse" x1={x1} y1={y1} x2={x2} y2={y2}>
      <stop offset="0" stopColor={r1} /><stop offset="1" stopColor={r2} />
    </linearGradient>
  );
  const ok = (ad: string, yay: string, uc: string) => (
    <g stroke={`url(#${id}${ad})`} fill={`url(#${id}${ad})`}>
      <path d={yay} fill="none" strokeWidth="3.6" strokeLinecap="round" />
      <path d={uc} strokeWidth="1" strokeLinejoin="round" />
    </g>
  );
  return (
    <svg width={boyut} height={boyut} viewBox="2 2 60 60" aria-hidden="true">
      <defs>
        {gec("a", 41.9, 15.1, 52.3, 35.9, "#3b82f6", "#14b8a6")}
        {gec("b", 42.6, 50.6, 19.4, 49.2, "#14b8a6", "#8b5cf6")}
        {gec("c", 11.5, 33.4, 24.3, 14, "#a855f7", "#3b82f6")}
        {gec("o", 25, 6, 39, 19, "#3b82f6", "#1d4ed8")}
        {gec("t", 43, 37, 57, 50, "#2dd4bf", "#0d9488")}
        {gec("l", 7, 37, 21, 50, "#a855f7", "#6d28d9")}
      </defs>
      {ok("a", "M41.94 15.07 A20.5 20.5 0 0 1 52.50 32.64", "M52.30 35.85 L56.10 32.58 L48.90 32.71Z")}
      {ok("b", "M42.56 50.57 A20.5 20.5 0 0 1 22.06 50.93", "M19.38 49.15 L20.32 54.08 L23.81 47.78Z")}
      {ok("c", "M11.50 33.36 A20.5 20.5 0 0 1 21.44 15.43", "M24.32 13.99 L19.59 12.34 L23.30 18.51Z")}
      <circle cx="32" cy="12.5" r="8.3" fill={`url(#${id}o)`} />
      <g fill="#fff"><rect x="28.4" y="13.4" width="1.9" height="2.8" rx=".4" /><rect x="31.05" y="11.6" width="1.9" height="4.6" rx=".4" /><rect x="33.7" y="9.8" width="1.9" height="6.4" rx=".4" /></g>
      <circle cx="49.75" cy="43.25" r="8.3" fill={`url(#${id}t)`} />
      <g stroke="#fff" fill="none" strokeLinecap="round"><circle cx="49.1" cy="42.6" r="2.7" strokeWidth="1.4" /><path d="M51.1 44.6 L53 46.5" strokeWidth="1.7" /></g>
      <circle cx="14.25" cy="43.25" r="8.3" fill={`url(#${id}l)`} />
      <path d="M12.7 40.2 L17.8 43.25 L12.7 46.3Z" fill="#fff" stroke="#fff" strokeWidth=".8" strokeLinejoin="round" />
      <g stroke={cizgi} strokeWidth="1.25" fill="none" strokeLinecap="round" strokeLinejoin="round">
        <path d="M31.4 26 C29.8 24.8 27.4 25.2 26.8 27 C24.6 26.8 23.3 28.8 24 30.5 C22.4 31.5 22.6 34.4 24.3 35.2 C23.6 37.4 25.6 39.4 27.6 38.7 C28.3 40.5 30.5 41 31.4 39.6 V26" />
        <path d="M27 29.4 c1.2 0 1.8 .8 1.6 1.8 M25.8 33.6 c1.2 -.3 2.2 .3 2.4 1.3 M29.6 35.6 c.4 .8 .2 1.6 -.5 2.1" />
        <path d="M32.6 26 C34.2 24.8 36.6 25.2 37.2 27 C39.4 26.8 40.7 28.8 40 30.5 C41.6 31.5 41.4 34.4 39.7 35.2 C40.4 37.4 38.4 39.4 36.4 38.7 C35.7 40.5 33.5 41 32.6 39.6 V26" />
        <path d="M32.6 30 H34.8 L36.1 28.7 M32.6 33.2 H36.3 M32.6 36.4 H34.4 L35.7 37.7" />
        <circle cx="36.7" cy="28.1" r=".85" /><circle cx="37.15" cy="33.2" r=".85" /><circle cx="36.3" cy="38.3" r=".85" />
      </g>
    </svg>
  );
}

// Yazı: EVALORA, A'lar çizgisiz (Λ), ilk A'nın içinde turkuaz üçgen (logodaki gibi).
export function Logo({ boyut = 36, slogan = true, koyuZemin = false }: { boyut?: number; slogan?: boolean; koyuZemin?: boolean }) {
  return (
    <span className="logo-tam">
      <LogoIsaret boyut={boyut} koyuZemin={koyuZemin} />
      <span className="logo-yazi">
        <span className="logo-ad" aria-label="EVALORA"><span aria-hidden="true">EV<span className="logo-a">Λ</span>LORΛ</span></span>
        {slogan && <span className="logo-slogan">Ölç · Teşhis et · Telafi et</span>}
      </span>
    </span>
  );
}
