#!/bin/bash
# EVALORA'yı bu bilgisayarda başlatır: arka uç (8000) ve ön yüz (5173), sonra tarayıcıyı açar.
# Çift tıklayarak çalıştırılır. Pencere açık kaldıkça uygulama çalışır; kapatınca durur.
# Pencere açıkken birkaç dakikada bir GitHub'daki main dalından yenilikleri çeker ve ice_aktarma/ altına gelen yeni
# soru setlerini (bulutta hazırlanan sınavlar) öğretmenin bankasına kendiliğinden aktarır.
EV="$(cd "$(dirname "$0")" && pwd)"
KOK="$EV/uygulama"
export GIT_TERMINAL_PROMPT=0  # şifre sorup beklemesin; giriş yoksa sessizce atlar

guncelle() {
  cd "$EV" || return
  if git fetch -q origin main 2>/dev/null && ! git merge-base --is-ancestor FETCH_HEAD HEAD; then
    if git merge -q --no-edit FETCH_HEAD >/dev/null 2>&1; then
      echo "$(date +%H:%M) GitHub'dan yenilikler alındı."
    else
      git merge --abort 2>/dev/null
      echo "$(date +%H:%M) GitHub'daki yenilikler bu bilgisayardaki değişikliklerle çakıştı; alınmadı."
    fi
  fi
  (cd "$KOK/backend" && .venv/bin/python -m app.otomatik_aktar)
}

guncelle
cd "$KOK/backend" && .venv/bin/uvicorn app.main:app --port 8000 &
ARKA=$!
cd "$KOK/frontend" && npm run dev -- --host 127.0.0.1 &
ON=$!
(while sleep 120; do guncelle; done) &
GUNCEL=$!
trap 'kill $ARKA $ON $GUNCEL 2>/dev/null' EXIT INT TERM
for i in $(seq 1 30); do curl -s -o /dev/null http://localhost:5173 && break; sleep 1; done
open http://localhost:5173
echo ""
echo "EVALORA çalışıyor: http://localhost:5173  (durdurmak için bu pencereyi kapat ya da Ctrl+C)"
wait
