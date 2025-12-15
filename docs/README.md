# Project Onboarding

## Read First
- `design/memos/memo_a.md` (spec)
- `design/memos/memo_b.md` (knowledge acquisition)
- `design/build_v0.md` (pipeline/queue/index design)
- `design/memos/parts_and_labor_guidelines.md` (parts/BOM/labor rules)
- `README.md` (repo layout + commands)

## How to Work the Queue
- Queue file: `out/work_queue.jsonl`. Each line is a task with `id`, `kind`, `reason`, `context`.
- Do not assume the queue is empty; pruning only happens for items marked `resolved`/`superseded`.
- Sources of queue items (indexer):
  - `referenced_only`: IDs referenced but not defined.
  - `unresolved_ref`: free-text refs.
  - `import_stub`: recipes with empty steps/import variants.
  - `no_recipe`: defined items (part/material/machine) missing a recipe.
  - `missing_field`: required field absent (e.g., energy_model/time_model).
  - `no_provider_machine`: resource_type with no machine capability.
  - `invalid_recipe_schema`: recipe steps not in the current schema.
- Workflow loop:
  1) Pop next: `.venv/bin/python -m kbtool queue pop`.
  2) Implement one item (add YAML/recipe/process/etc.). Prefer ≥3-step recipes with time/labor/machine-hours when possible. Reference missing processes explicitly if needed so they queue.
  3) Run index: `.venv/bin/python -m kbtool index`.
  4) Inspect `out/work_queue.jsonl` and any reports (`out/unresolved_refs.jsonl`, `out/missing_recipes.jsonl`, `out/invalid_recipes.jsonl`).
  5) Repeat; only mark tasks resolved by removing/renaming queue entries if explicitly done.

## Recipes (breaking schema)
- Steps must be objects per `kbtool.models.RecipeStep` (`process_id`, optional time/labor/machine fields).
- Processes may include `est_time_hr` and `resource_requirements` with `amount`+`unit` (use `hr`).
- Aim for ≥3 steps per recipe; include mold prep/finishing where applicable; use manual/assembly processes for glue work.
- If a needed process does not exist, reference it anyway (it will queue as `referenced_only`).

## Generic Processes/Resources to Reuse
- Assembly: `assembly_basic_v0` (needs `assembly_tools_basic`, labor).
- Mold prep: `mold_preparation_basic_v0`.
- Machining: `machining_finish_basic_v0`.
- Power conditioning/distribution: `power_conditioning_basic_v0`, `power_distribution_basic_v0`.
- Grinding/drying: `sizing_grinding_basic_v0`, `drying_basic_v0`.
- Winding: `spool_winding_basic_v0`.
- Import placeholder: `import_placeholder_v0` (only if truly importing).
- Environment source: `environment_source_v0` (for natural inputs like solar, regolith in situ).
- Manual labor: use `labor_bot_general` in `resource_requirements`.

## Boundary/Terminal Processes
To prevent infinite recursion in the dependency graph, some processes are **terminal nodes** that represent boundary conditions:
- `environment_source_v0` — freely available environmental resources (solar irradiance, lunar regolith in situ)
- `import_placeholder_v0` — items imported from Earth, not manufactured locally

These processes use `energy_model: {type: boundary}` and `time_model: {type: boundary}` to indicate they are intentionally terminal and should not generate further queue items. Use these for:
- Natural resources (sunlight, raw regolith)
- Imported specialty materials (electronics, SMA wire, etc.)
- Byproducts that don't need upstream manufacturing (waste heat)

## Energy and Time Models (Machine-Readable Schema)

Processes require `energy_model` and `time_model` fields for automated calculations. These are structured objects (see `kbtool/models.py`).

### EnergyModel
```yaml
energy_model:
  type: kWh_per_kg      # or: fixed_kWh, boundary
  value: 3.5            # kWh per kg (for kWh_per_kg) or kWh per batch (for fixed_kWh)
  notes: "melting steel (~1.2 MJ/kg enthalpy + heating losses)"
```

Types:
- `kWh_per_kg` — energy scales linearly with input mass
- `fixed_kWh` — constant energy per batch/cycle
- `boundary` — terminal node (no energy consumption modeled)

### TimeModel
```yaml
time_model:
  type: linear_rate     # or: fixed_time, boundary
  hr_per_kg: 0.4        # hours per kg processed
  setup_hr: 0.1         # optional setup time
  notes: "deposition rate ~2.5 kg/hr for GMAW"
```

Or for batch processes:
```yaml
time_model:
  type: fixed_time
  hr_per_batch: 1.5
  notes: "furnace heat-up, pour, cool cycle"
```

Types:
- `linear_rate` — time = setup_hr + (mass × hr_per_kg) or time = setup_hr + (mass / rate_kg_per_hr)
- `fixed_time` — constant time per batch/cycle (use hr_per_batch)
- `boundary` — terminal node (no time modeled)

### Example Process with Models
```yaml
id: metal_casting_basic_v0
kind: process
name: Basic metal casting
energy_model:
  type: kWh_per_kg
  value: 3.5
  notes: "melting steel (~1.2 MJ/kg enthalpy + heating losses)"
time_model:
  type: fixed_time
  hr_per_batch: 1.5
  notes: "furnace heat-up, pour, cool cycle"
```

## Commands
- Index: `.venv/bin/python -m kbtool index`
- Queue: `.venv/bin/python -m kbtool queue pop`, `.venv/bin/python -m kbtool queue prune`
- Virtualenv: `uv sync` to install deps.

## Principles
- Do not hide work: placeholders/imports should queue follow-ups.
- Prefer consolidation over proliferation (shared parts/process IDs).
- Estimate masses and times (within 5× is acceptable); avoid nulls.
- Reference missing processes/items explicitly to surface work.***
