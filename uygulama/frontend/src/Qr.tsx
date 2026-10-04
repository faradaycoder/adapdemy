import { useEffect, useState } from "react";
import QRCode from "qrcode";

// QR kod: taranan sayfanın hangi atama, öğrenci ve soruya ait olduğunu taşır (SinavYazdir.tsx).
// Hata düzeltme düzeyi M: kâğıt hafif kirlense ya da fotoğraf eğik çekilse de okunur.
export default function Qr({ veri, boyut = 72 }: { veri: string; boyut?: number }) {
  const [src, setSrc] = useState<string | null>(null);
  useEffect(() => {
    QRCode.toDataURL(veri, { errorCorrectionLevel: "M", margin: 1, width: boyut * 3 }).then(setSrc).catch(() => setSrc(null));
  }, [veri, boyut]);
  return (
    <span className="qr">
      {src ? <img src={src} alt={veri} width={boyut} height={boyut} /> : <span className="qr-yer">{veri}</span>}
      <small>{veri.replace("EVALORA:", "")}</small>
    </span>
  );
}
