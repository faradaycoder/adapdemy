import { createContext, useContext, useEffect, useState, type ReactNode } from "react";
import { api, jetonAl, jetonKaydet, type Kullanici } from "./api";

type Oturum = {
  kullanici: Kullanici | null;
  yukleniyor: boolean;
  girisYap: (eposta: string, sifre: string) => Promise<void>;
  kayitOl: (ad: string, eposta: string, sifre: string, rol: "ogretmen" | "ogrenci") => Promise<void>;
  cikis: () => void;
};

const Baglam = createContext<Oturum | null>(null);

export function OturumSaglayici({ children }: { children: ReactNode }) {
  const [kullanici, setKullanici] = useState<Kullanici | null>(null);
  const [yukleniyor, setYukleniyor] = useState(true);

  useEffect(() => {
    if (!jetonAl()) { setYukleniyor(false); return; }
    api<Kullanici>("/api/hesap/ben")
      .then(setKullanici)
      .catch(() => jetonKaydet(null))
      .finally(() => setYukleniyor(false));
  }, []);

  async function girisYap(eposta: string, sifre: string) {
    const r = await api<{ jeton: string; kullanici: Kullanici }>("/api/hesap/giris", { govde: { eposta, sifre } });
    jetonKaydet(r.jeton);
    setKullanici(r.kullanici);
  }

  async function kayitOl(ad: string, eposta: string, sifre: string, rol: "ogretmen" | "ogrenci") {
    const r = await api<{ jeton: string; kullanici: Kullanici }>("/api/hesap/kayit", { govde: { ad, eposta, sifre, rol } });
    jetonKaydet(r.jeton);
    setKullanici(r.kullanici);
  }

  function cikis() {
    jetonKaydet(null);
    setKullanici(null);
  }

  return <Baglam.Provider value={{ kullanici, yukleniyor, girisYap, kayitOl, cikis }}>{children}</Baglam.Provider>;
}

export function useOturum() {
  const o = useContext(Baglam);
  if (!o) throw new Error("useOturum, OturumSaglayici içinde kullanılmalı");
  return o;
}
