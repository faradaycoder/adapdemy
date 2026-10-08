// EVALORA logosu: Murat'ın logosundan (2026-10-08) kesilmiş parçalar, public/ içinde:
//   logo-isaret.png  ortada beyin, çevresinde Ölç (mavi) → Teşhis et (turkuaz) → Telafi et (mor) döngüsü
//   logo-yazi.png    EVALORA yazısı (A'nın içinde turkuaz üçgen)
//   logo-tam.png     işaret + yazı + slogan + açılım (giriş paneli)
// Zeminler şeffaf; koyu zeminde işaret beyaz bir rozetin içine alınır, yazı beyaza çevrilir.
export const RENK = { olc: "#2563eb", teshis: "#14b8a6", telafi: "#8b5cf6", lacivert: "#13306a" };

export function LogoIsaret({ boyut = 36, koyuZemin = false }: { boyut?: number; koyuZemin?: boolean }) {
  return (
    <span className={`logo-isaret ${koyuZemin ? "rozet" : ""}`} style={{ width: boyut, height: boyut }}>
      <img src="/logo-isaret.png" alt="" width={boyut} height={boyut} />
    </span>
  );
}

export function Logo({ boyut = 36, slogan = true, koyuZemin = false }: { boyut?: number; slogan?: boolean; koyuZemin?: boolean }) {
  return (
    <span className={`logo-tam ${koyuZemin ? "koyu" : ""}`}>
      <LogoIsaret boyut={boyut} koyuZemin={koyuZemin} />
      <span className="logo-yazi">
        <img className="logo-ad-img" src="/logo-yazi.png" alt="EVALORA" style={{ height: Math.round(boyut * 0.42) }} />
        {slogan && <span className="logo-slogan">Ölç · Teşhis et · Telafi et</span>}
      </span>
    </span>
  );
}
