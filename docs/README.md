# Project Onboarding

## REQUIRED READING (Before Working on Queue)

**You MUST read these documents before working on the queue:**

1. **`design/meta-memo.md`** — Project overview and high-level goals
2. **`design/memo_a.md`** — Formal specification and design principles
3. **`design/memo_b.md`** — Knowledge acquisition methodology and constraints
4. **`docs/parts_and_labor_guidelines.md`** — Parts, BOMs, and labor modeling policy (CRITICAL for recipe/BOM work)

These documents are **mandatory prerequisites** for contributing to the knowledge base. They define the scope, constraints, and methodology for building the self-replicating system model.

## Additional Required Reading
- `design/build_v0.md` (pipeline/queue/index design)
- `README.md` (repo layout + commands)

## Before Creating Parts or BOMs: Check Inventory First

**CRITICAL: Always check existing parts before creating new ones.** Part reuse is essential for keeping the knowledge base tractable.

**📖 FULL DOCUMENTATION**: See **`docs/parts_and_labor_guidelines.md`** for comprehensive guidelines on:
- Part reuse policy and equivalence criteria
- Material class system (enables generic substitution)
- BOM best practices
- Labor modeling approach
- Workflow for creating parts/BOMs

### Quick Workflow for Part Selection

1. **Check the inventory report**: `out/reports/inventory.md`
   - Regenerate if stale: `.venv/bin/python -m kbtool report inventory`
   - Search for the component type: `grep -i "motor\|bearing\|wire" out/reports/inventory.md`

2. **Prefer existing parts** — Reuse an existing part if it is "reasonably equivalent" (within ~5× magnitude, same material compatibility)

3. **Only create new parts** if no reasonably equivalent part exists

### Key Equivalence Rule

Parts within **~5× magnitude** (mass, size, capability) are considered equivalent:
- 5 kW motor ≈ 10 kW motor → **reuse same part**
- 2 kg component ≈ 8 kg component → **reuse same part**
- **EXCEPTION**: Materials incompatible (steel ≠ plastic) or process requirements conflict → create new part

See **`docs/parts_and_labor_guidelines.md`** for detailed criteria and examples.

## How to Work the Queue (multi-agent)
- Queue file: `out/work_queue.jsonl`. IDs are stable: `id = "<gap_type>:<item_id>"` with fields `gap_type`, `item_id`, `reason`, `context`, `status`, `lease_id`, `lease_expires_at`.
- Lease next task: `.venv/bin/python -m kbtool queue lease --agent <name> [--ttl 900] [--priority gap1,gap2]`
  - Status becomes `leased`; expires to `pending` if TTL lapses.
- Complete: `.venv/bin/python -m kbtool queue complete --id <gap_type:item_id> --agent <name>`
- Release: `.venv/bin/python -m kbtool queue release --id <gap_type:item_id> --agent <name>`
- GC (revert expired leases, optionally prune old done): `.venv/bin/python -m kbtool queue gc [--prune-done-older-than N]`
- List counts: `.venv/bin/python -m kbtool queue ls`
- Do not edit `work_queue.jsonl` by hand; use the CLI.
- Pruning: only removes items marked `resolved`/`superseded`; gaps persist until fixes land.
- Sources of queue items (indexer rebuilds on each run):
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

## Dedupe Queue (tool consolidation workflow)
- Separate file: `out/dedupe_queue.jsonl`; mirror commands:
  - Lease: `.venv/bin/python -m kbtool dedupe lease --agent <name> [--ttl 900]`
  - Complete/Release: `.venv/bin/python -m kbtool dedupe complete|release --id <id> --agent <name>`
  - GC/list: `.venv/bin/python -m kbtool dedupe gc|ls`
- Add tasks: `.venv/bin/python -m kbtool dedupe add --file <json_or_jsonl>` (entries need `id` and optional `kind`, `reason`, `candidate_ids`, `notes`, `hints`, `refs`, `category`).
- Suggested staging for add files: drop JSON/JSONL under `dedupe_tasks/` and add via the CLI for auditability.
- Seeding: manual/agent review (e.g., `out/reports/inventory.md`); no auto-population yet.
- Decisions and precedents: log in `docs/dedupe_decisions.md`; annotate items with `alternatives`/`dedupe_candidate` (to be adopted as schema fields).

## Seed Files (System-Level Roadmaps)

**Seed files** are special `kind: seed` YAML files in `kb/seeds/` that define large subsystems and seed the work queue with all their required components.

### What is a Seed File?
- A seed file has `kind: seed` and lists all items needed for a complete subsystem in `requires_ids`
- When the indexer runs, all referenced items become work queue entries
- Seed files act as "roadmaps" that break down large systems into manageable work items

### Seed File Context in Work Queue
When you lease a work item, check the `context.seed_files` field:
```json
{
  "id": "referenced_only:battery_cell_nife",
  "context": {
    "seed_files": ["battery_system_nife_v0", "thermionic_system_roadmap_v0"]
  }
}
```

**If `seed_files` is present**, read the corresponding design documents:
- `battery_system_nife_v0` → Read `design/battery-design.md`
- `thermionic_system_roadmap_v0` → Read `design/solar_thermionics_report.md`

The seed file's `notes` section contains worker instructions and references to technical documentation.

### Current Seed Files
- **`kb/seeds/battery_system_nife_v0.yaml`** - Nickel-Iron battery manufacturing system
  - Technical specs: `design/battery-design.md`
  - ~40 items to implement
- **`kb/seeds/thermionic_system_roadmap_v0.yaml`** - Solar thermionic power generation
  - Technical specs: `design/solar_thermionics_report.md`
  - Implementation plan: `.claude/plans/bright-wondering-pearl.md`
  - ~67 items to implement

### Why Seed Files Matter
- They provide **context** for why an item is needed
- They link to **technical documentation** with specifications
- They ensure **coordinated implementation** of subsystems
- They prevent working on orphan items disconnected from system goals

**Always check `context.seed_files` when working queue items** - it tells you which design documents to consult for technical specifications.

## Recipes (breaking schema)
- Steps must be objects per `kbtool.models.RecipeStep` (`process_id`, optional time/labor/machine fields).
- Processes may include `est_time_hr` and `resource_requirements` with `amount`+`unit` (use `hr`).
- Aim for ≥3 steps per recipe; include mold prep/finishing where applicable; use manual/assembly processes for glue work.
- If a needed process does not exist, reference it anyway (it will queue as `referenced_only`).
- Multiple variants can live in the same recipe file (e.g., `variant_id: simple`, `variant_id: additive`, `variant_id: precision`). Use a `preferred_variant` hint on the item to mark the default/simple path (schema update pending; follow convention in notes until field lands).

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
- Reference missing processes/items explicitly to surface work.
- Avoid collisions: always lease a task before editing; do not modify items you haven’t leased. If two agents touch the same item, reconcile (merge components/notes) rather than overwrite, and leave context in `notes`.
