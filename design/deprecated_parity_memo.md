# Deprecated -> src parity memo

## Scope
Checked deprecated code under `kbtool/`, `base_builder/`, and `simulations/` against `src/`.

## Functionality already present in `src/`
- Closure analysis ported from `kbtool/closure_analysis.py` to `src/indexer/closure_analysis.py` (adds boundary-process handling).
- KB loading and unit conversion consolidated from `base_builder/` into `src/kb_core/` (`kb_loader.py`, `unit_converter.py`).
- Simulation engine and models ported from `base_builder/` to `src/simulation/` with ADR-012..017 support.
- Auto-fix core logic lives in `src/kb_core/auto_fixer.py` (deprecated CLI still used by `src/cli.py`).

## Missing functionality in `src/`

### KB indexing and queue artifacts
- `kbtool/indexer.py` has no `src/` replacement; `src/cli.py` still dispatches to `kbtool.indexer`.
- Indexer outputs not reproduced in `src/`: `out/index.json`, `out/validation_report.md`, `out/unresolved_refs.jsonl`, `out/work_queue.jsonl`, `out/missing_recipes.jsonl`, `out/missing_fields.jsonl`, `out/orphan_resources.jsonl`, `out/missing_recipe_items.jsonl`.
- Queue filtering config (`kbtool/config.py` + `config/queue_filters.yaml` + `.kbconfig.yaml`) is not implemented in `src/`.

### Work queue + dedupe queue tooling
- `kbtool/queue_tool.py` (lease/complete/release/gc, gap registry, manual gap add, list gap types, prune/pop) has no `src/` equivalent.
- `kbtool/dedupe_tool.py` (dedupe queue lease/complete/release/gc/add/list) has no `src/` equivalent.

### Circular dependency detection/fixing
- `kbtool/circular_dependency_fixer.py` (cycle detection, classification, queue item generation, report, optional recipe edits) has no `src/` equivalent.

### Reports
- `kbtool/report.py` (inventory report from `out/index.json`) has no `src/` equivalent.

### CLI parity gaps
- `kbtool/__main__.py` commands not mirrored in `src/cli.py`:
  - `validate` (gap-id verification via re-index) is missing; `src/cli.py validate` only validates a single process/recipe by id.
  - `queue`, `dedupe`, `report`, `config` commands are missing.
- `src/cli.py auto-fix` still calls `kbtool/auto_fix.py` instead of a native `src/` CLI wrapper.

### Simulation agent tooling
- `base_builder/agent.py` (autonomous LLM runner) has no `src/` replacement.
- `base_builder/sim_tools.py` (function_tool wrappers for agent integration) has no `src/` replacement.
- `base_builder/interactive.py` (Python API for interactive sims) has no `src/` replacement.
- `base_builder/cli.py` features are not replicated in `src/simulation/cli.py` (no `start`/`continue` agent workflows or `analyze` command).

### Energy model compatibility
- `base_builder/energy.py` supports legacy energy_model types (`kWh_per_kg`, `kWh_per_kg_input`, `kWh_per_unit`, `kWh_per_unit_output`, `kWh_per_batch`, `fixed_kWh`, `total_energy_kwh`).
- `src/kb_core/calculations.py` only supports ADR-014 `per_unit` and `fixed_per_batch`, so legacy energy model calculations are not supported in `src/`.

## Notes on `simulations/`
- `simulations/` contains JSONL logs and docs, not executable code, so there is no direct code migration target in `src/`.
