# Simviewer Implementation Plan

Date: 2026-03-04
Status: Approved for implementation

## Goal
Build a static, shareable simulation viewer for a single simulation (`sim-id`) per build, with:
- Timeline-first Gantt investigation UX
- KB + authored articles in a unified browser
- Exported data baked into a static frontend build

## Decisions Locked
1. One `sim-id` per build.
2. Gantt rows are machine instances (synthesized lanes if true instance IDs are unavailable).
3. Inventory snapshots use periodic checkpoints + forward deltas.
4. Articles are sourced from configurable folders in a build config.
5. Wiki-link syntax is `[[id]]` (no type prefix required).
6. Categories come from KB `category` field.
7. Failed processes are shown in timeline with distinct status/color.
8. Build output is static with data baked into build output directory.

## Architecture

### Export Pipeline (Python)
New module: `src/simviewer/`
- `config.py`: load/validate `simviewer.config.yaml`
- `models.py`: typed export models
- `exporter.py`: simulation + KB + article export
- `articles.py`: markdown/frontmatter/wiki-link parsing and backlink generation

New CLI command:
- `python -m src.cli sim export-view --sim-id <id> --out <dir> [--config simviewer.config.yaml]`

### Frontend (React)
New app: `apps/simviewer/`
- Vite + React + TypeScript
- Hash routing
- Views: Home, Gantt, KB Browser
- Data loaded from local `dist/data/*.json`

## Data Contract (v1)

Output directory:
- `dist/data/sim_data.json`
- `dist/data/kb_entities.json`
- `dist/data/backlinks.json`
- `dist/data/articles.json`
- `dist/data/warnings.json`

### `sim_data.json` (v1)
- `sim_id`
- `summary`: time, energy, imports, counts
- `machine_lanes`: synthesized lane definitions
- `process_runs`: start/end/duration/status/energy/inputs/outputs/machine_lane
- `inventory_checkpoints`: full snapshots at configured cadence
- `inventory_deltas`: per-process deltas

### `kb_entities.json` (v1)
- flattened entities keyed by ID
- `kind`, `category`, key metadata
- sim activity rollups per entity

### `backlinks.json` (v1)
- target ID -> list of pages/articles that reference it

### `articles.json` (v1)
- article metadata + rendered/parsed content references

### `warnings.json` (v1)
- unresolved wiki links
- missing KB categories
- undefined KB references encountered during build

## Machine Lane Strategy
Because stable machine instance IDs are not guaranteed in current events:
- group process runs by machine type
- assign each run to earliest non-overlapping lane
- produce deterministic `machine_type#lane_n` IDs

## Inventory Strategy
Configurable defaults:
- `checkpoint_every_processes: 150`
- `checkpoint_every_hours: 24`
- always snapshot at sim start/end

At render time:
- locate nearest checkpoint
- replay forward deltas to requested timestamp/process

## Error Handling
- Build should **warn**, not fail, for unresolved `[[id]]` links.
- Undefined target pages should still be routable and rendered as “Undefined Entry”.

## Configuration (`simviewer.config.yaml`)
Planned fields:
- `sim_id`
- `article_paths` (globs)
- `checkpoint_every_processes`
- `checkpoint_every_hours`
- `homepage_article_id`
- `strict` (default false)

## Implementation Phases
1. Exporter MVP + CLI command + schema stubs.
2. Article ingest + backlinks + warnings.
3. Frontend shell + routing + Home.
4. Gantt + lanes + status colors + detail drawer.
5. KB browser templates + wiki-link routing.
6. Performance tuning and packaging docs.

## Acceptance Criteria (Phase 1)
- `sim export-view` runs for a valid `sim-id`.
- Emits all v1 JSON files with stable schema.
- Emits warnings file and does not fail on unresolved links.

