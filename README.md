# Self-Replicating System Modeling (v0)

Minimal setup to run the KB indexer and iterate on YAML data.

## Quick start
- Install deps with uv: `uv sync` (creates `.venv`).
- Run indexer: `.venv/bin/python -m kbtool index`
  - Outputs: `out/index.json`, `out/validation_report.md`, `out/work_queue.jsonl`, etc.
- Queue helpers:
  - Prune (only explicit resolved/superseded): `.venv/bin/python -m kbtool queue prune`
  - Pop next item: `.venv/bin/python -m kbtool queue pop`
- See `docs/` for onboarding and workflow details.

## Repo layout (current)
- `design/` — memos, notes, reference papers.
- `kb/` — YAML knowledge base (processes, items, resources, recipes, BOMs, scenarios).
- `kbtool/` — Python tooling (models + indexer CLI).
- `out/` — generated index, reports, work queue.

## Indexer outputs
| File | Description |
|------|-------------|
| `index.json` | Full dependency graph of all KB entries |
| `validation_report.md` | Comprehensive gap summary + warnings |
| `work_queue.jsonl` | All gaps needing attention (rebuilt each run) |
| `null_values.jsonl` | Fields with null data (qty, amount, mass) |
| `missing_recipes.jsonl` | Items (parts/materials) without recipes |
| `missing_fields.jsonl` | Required fields not populated (energy_model, time_model, material_class) |
| `orphan_resources.jsonl` | Resource types with no machine providing them |
| `unresolved_refs.jsonl` | Free-text `requires_text` entries needing resolution |
| `import_stubs.jsonl` | Recipes marked as imports (empty steps) |

## Work queue behavior
The work queue is **rebuilt from scratch** on each indexer run, reflecting all current gaps:
- `no_recipe` — parts/materials without manufacturing recipes (will be imports)
- `missing_field` — required fields not populated (energy_model, time_model, material_class)
- `no_provider_machine` — resource_types with no machine capability
- `referenced_only` — IDs referenced but not defined
- `unresolved_ref` — free-text requirements needing definition
- `import_stub` — machines/items with import recipes needing local manufacturing

When you fix a gap, the next indexer run automatically removes it from the queue.

## Current state (as of last index)
- 209 total gaps in work queue
- 83 items without recipes (27 materials + 56 parts)
- 100 missing required fields (19 energy_model + 19 time_model + 62 material_class)
- 26 orphan resource_types (no machine provides them)
- 57 null values in processes

## Next steps
1. Add recipes for materials (most are outputs of processes, need to link them)
2. Add `material_class` to parts (e.g., steel, ceramic, glass)
3. Add `energy_model` and `time_model` to processes
4. Create machines for orphan resource_types (or mark as consumables)
5. Fill in null qty/amount values in processes
6. Rerun `python -m kbtool index` after changes to refresh all outputs.
