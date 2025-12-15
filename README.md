# Self-Replicating System Modeling (v0)

Minimal setup to run the KB indexer and iterate on YAML data.

## Quick start
- Install deps with uv: `uv sync` (creates `.venv`).
- Run indexer: `.venv/bin/python -m kbtool index`
  - Outputs: `out/index.json`, `out/validation_report.md`, `out/unresolved_refs.jsonl`, `out/work_queue.jsonl`.
- Queue helpers:
  - Prune completed items: `.venv/bin/python -m kbtool queue prune`
  - Pop next item: `.venv/bin/python -m kbtool queue pop`

## Repo layout (current)
- `design/` — memos, notes.
- `kb/` — YAML knowledge base (processes seeded; items/resources/recipes next).
- `kbtool/` — Python tooling (models + indexer CLI).
- `out/` — generated index, reports, work queue.

## Next steps
- Populate materials/resources/recipes so unresolved references in `out/unresolved_refs.jsonl` shrink.
- Keep writing one YAML per work item (see `out/work_queue.jsonl` for the seeded round-robin list).
- Rerun `python -m kbtool index` after each addition to refresh the index and unresolved refs list.
