import { Logo } from "../Logo";

// Giriş ve kayıt sayfalarının sol paneli: EVALORA'nın misyonu ve üç adımı.
export default function GirisMarka() {
  return (
    <aside className="giris-marka">
      <Logo boyut={48} />
      <div>
        <h2>Her öğrencinin eksiğini mikro kazanım düzeyinde bul, hemen kapat.</h2>
        <p>EVALORA sınavı puandan öteye taşır: her çözüm adımını bir mikro kazanıma bağlar, öğrencinin neyi bilip neyi bilmediğini gösterir ve eksiği için doğru içeriği önerir. Son söz her zaman öğretmendedir.</p>
      </div>
      <ul>
        <li><i style={{ background: "#0ea5a4" }}>1</i><div><b>Ölç</b><small>Sorular ve rubrik adımları mikro kazanımlara eşlenir.</small></div></li>
        <li><i style={{ background: "#7c3aed" }}>2</i><div><b>Teşhis et</b><small>Her adım için biliyor, bilmiyor ya da ölçülemedi; sınıf ve öğrenci raporu.</small></div></li>
        <li><i style={{ background: "#f59e0b" }}>3</i><div><b>Telafi et</b><small>Eksik konu için kısa konu anlatımı ve benzer soru çözümü.</small></div></li>
      </ul>
    </aside>
  );
}
