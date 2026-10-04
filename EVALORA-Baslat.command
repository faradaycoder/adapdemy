#!/bin/bash
# EVALORA'yı bu bilgisayarda başlatır: arka uç (8000) ve ön yüz (5173), sonra tarayıcıyı açar.
# Çift tıklayarak çalıştırılır. Pencere açık kaldıkça uygulama çalışır; kapatınca durur.
KOK="$(cd "$(dirname "$0")" && pwd)/uygulama"
cd "$KOK/backend" && .venv/bin/uvicorn app.main:app --port 8000 &
ARKA=$!
cd "$KOK/frontend" && npm run dev -- --host 127.0.0.1 &
ON=$!
trap 'kill $ARKA $ON 2>/dev/null' EXIT INT TERM
for i in $(seq 1 30); do curl -s -o /dev/null http://localhost:5173 && break; sleep 1; done
open http://localhost:5173
echo ""
echo "EVALORA çalışıyor: http://localhost:5173  (durdurmak için bu pencereyi kapat ya da Ctrl+C)"
wait
