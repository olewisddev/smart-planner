#!/bin/bash
set -e

. /venv/bin/activate

cd /app/backend
uv run ./app/main.py &

cd /app/frontend
npm run dev &

wait
