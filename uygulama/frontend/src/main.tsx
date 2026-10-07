import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter, Link, Navigate, Route, Routes } from "react-router-dom";
import { OturumSaglayici, useOturum } from "./oturum";
import Giris from "./sayfalar/Giris";
import Kayit from "./sayfalar/Kayit";
import OgretmenAna from "./sayfalar/OgretmenAna";
import OgrenciAna from "./sayfalar/OgrenciAna";
import SinifSayfasi from "./sayfalar/SinifSayfasi";
import MKGezgini from "./sayfalar/MKGezgini";
import SoruBankasi from "./sayfalar/SoruBankasi";
import SoruYukle from "./sayfalar/SoruYukle";
import SoruDuzenle from "./sayfalar/SoruDuzenle";
import Sinavlar from "./sayfalar/Sinavlar";
import SinavDuzenle from "./sayfalar/SinavDuzenle";
import SinavYazdir from "./sayfalar/SinavYazdir";
import SinavRubrik from "./sayfalar/SinavRubrik";
import OgrenciSinav from "./sayfalar/OgrenciSinav";
import Teslimler from "./sayfalar/Teslimler";
import Degerlendir from "./sayfalar/Degerlendir";
import OgrenciSonuc from "./sayfalar/OgrenciSonuc";
import SinifRapor from "./sayfalar/SinifRapor";
import OgrenciRapor from "./sayfalar/OgrenciRapor";
import Zil from "./Zil";
import "./stil.css";

function Ust() {
  const { kullanici, cikis } = useOturum();
  return (
    <header className="ust">
      <Link to="/" className="logo" title="Micro-skill based assessment, diagnosis and remediation · Mikro kazanım temelli ölçme, teşhis ve telafi">EVALORA <span>Measure. Diagnose. Remediate.</span></Link>
      {kullanici && (
        <nav>
          {kullanici.rol === "ogretmen" && <><Link to="/sorular">Soru bankası</Link><Link to="/sinavlar">Sınavlar</Link><Link to="/mk">MK haritası</Link></>}
          <Zil />
          <span className="kim">{kullanici.ad}</span>
          <button className="ikincil" onClick={cikis}>Çıkış</button>
        </nav>
      )}
    </header>
  );
}

function Anasayfa() {
  const { kullanici } = useOturum();
  if (!kullanici) return <Navigate to="/giris" replace />;
  return kullanici.rol === "ogretmen" ? <OgretmenAna /> : <OgrenciAna />;
}

function Korumali({ children }: { children: React.ReactNode }) {
  const { kullanici } = useOturum();
  return kullanici ? <>{children}</> : <Navigate to="/giris" replace />;
}

function Uygulama() {
  const { yukleniyor } = useOturum();
  if (yukleniyor) return <p className="orta">Yükleniyor…</p>;
  return (
    <>
      <Ust />
      <main>
        <Routes>
          <Route path="/" element={<Anasayfa />} />
          <Route path="/giris" element={<Giris />} />
          <Route path="/kayit" element={<Kayit />} />
          <Route path="/sinif/:id" element={<Korumali><SinifSayfasi /></Korumali>} />
          <Route path="/sinif/:id/rapor" element={<Korumali><SinifRapor /></Korumali>} />
          <Route path="/sinif/:id/ogrenci/:oid" element={<Korumali><OgrenciRapor /></Korumali>} />
          <Route path="/rapor" element={<Korumali><OgrenciRapor /></Korumali>} />
          <Route path="/sorular" element={<Korumali><SoruBankasi /></Korumali>} />
          <Route path="/sorular/yukle" element={<Korumali><SoruYukle /></Korumali>} />
          <Route path="/sorular/yeni" element={<Korumali><SoruDuzenle /></Korumali>} />
          <Route path="/sorular/:id" element={<Korumali><SoruDuzenle /></Korumali>} />
          <Route path="/sinavlar" element={<Korumali><Sinavlar /></Korumali>} />
          <Route path="/sinavlar/yeni" element={<Korumali><SinavDuzenle /></Korumali>} />
          <Route path="/sinavlar/:id" element={<Korumali><SinavDuzenle /></Korumali>} />
          <Route path="/sinavlar/:id/yazdir" element={<Korumali><SinavYazdir /></Korumali>} />
          <Route path="/sinavlar/:id/rubrik" element={<Korumali><SinavRubrik /></Korumali>} />
          <Route path="/sinav/:atamaId" element={<Korumali><OgrenciSinav /></Korumali>} />
          <Route path="/sinav/:atamaId/yazdir" element={<Korumali><SinavYazdir /></Korumali>} />
          <Route path="/atama/:atamaId/teslimler" element={<Korumali><Teslimler /></Korumali>} />
          <Route path="/atama/:atamaId/teslimler/:teslimId" element={<Korumali><Degerlendir /></Korumali>} />
          <Route path="/sonuc/:atamaId" element={<Korumali><OgrenciSonuc /></Korumali>} />
          <Route path="/mk" element={<Korumali><MKGezgini /></Korumali>} />
          <Route path="/mk/:kod" element={<Korumali><MKGezgini /></Korumali>} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </main>
    </>
  );
}

createRoot(document.getElementById("kok")!).render(
  <StrictMode>
    <BrowserRouter>
      <OturumSaglayici>
        <Uygulama />
      </OturumSaglayici>
    </BrowserRouter>
  </StrictMode>,
);
