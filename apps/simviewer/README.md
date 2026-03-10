# SERES Simviewer (MVP)

React + Vite static simulation viewer.

## Requirements
- Node via `nvm` (Node 24 recommended)
- Python venv with project deps (`.venv`)

## Install
```bash
cd apps/simviewer
source ~/.nvm/nvm.sh
nvm use 24
npm install
```

## Export simulation data into viewer public dir
From repo root:
```bash
.venv/bin/python -m src.cli sim export-view --sim-id runbook_queue_sequential --out apps/simviewer/public
```

For sim2 runs:
```bash
.venv/bin/python -m src.cli sim2 export-view --sim-id <sim_id> --sim-root simulations_parallel --out apps/simviewer/public
```

`npm run build` and `npm run preview` use `apps/simviewer/public/data/*` as the source dataset.

## Run dev server
```bash
cd apps/simviewer
source ~/.nvm/nvm.sh
nvm use 24
npm run dev
```

## Build static artifact
```bash
cd apps/simviewer
source ~/.nvm/nvm.sh
nvm use 24
npm run build
```

Built output:
- `apps/simviewer/dist/index.html`
- `apps/simviewer/dist/data/*.json`

Do not open `dist/index.html` via `file://` in Chromium/Brave (module scripts are blocked).
Serve `dist/` over HTTP instead:

```bash
cd apps/simviewer
source ~/.nvm/nvm.sh
nvm use 24
npm run preview
```

Then open the printed local URL (typically `http://localhost:4173/`).
