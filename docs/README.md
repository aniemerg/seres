# Project Onboarding

## REQUIRED READING (Before Working on Queue)

**You MUST read these documents before working on the queue:**

1. **`docs/project_overview.md`** — Project overview and high-level goals
2. **`docs/kb_schema_reference.md`** — Current schema reference (012+)
3. **`docs/knowledge_acquisition_protocol.md`** — Knowledge acquisition workflow
4. **`docs/parts_and_labor_guidelines.md`** — Parts, BOMs, and labor modeling policy (CRITICAL for recipe/BOM work)
5. **`docs/conservative_mode_guide.md`** — Queue work philosophy and decision trees (DEFAULT APPROACH)
6. **`docs/closure_error_guidance.md`** — Closure analysis error resolution (material flow gaps)
7. **`docs/fixing-template-validation-errors.md`** — Guide for fixing template process errors (4,609 errors)

These documents are **mandatory prerequisites** for contributing to the knowledge base. They define the scope, constraints, and methodology for building the self-replicating system model.

### Conservative Mode: The Default Approach

**All queue work should follow Conservative Mode** - treating queue items as potential symptoms rather than direct fix requests.

**Key principles:**
- Minimize new creation, maximize reuse
- Check for equivalents (5× magnitude rule)
- Prefer labor bot + tools over special machines
- Adapt existing items before creating new ones
- Verify references aren't erroneous
- Use `is_template: true` on generic processes when recipes define concrete inputs/outputs
  - Template processes may omit inputs/outputs; recipes must provide them explicitly

**See `conservative_mode_guide.md` for complete decision trees.**

## Additional Required Reading
- `design/build_v0.md` (pipeline/queue/index design)
- `README.md` (repo layout + commands)
 - `docs/mold_migration_notes.md` (note on migrating to part-specific mold tooling)

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
- Lease next task: `python -m src.cli queue lease --agent <name> [--ttl 900] [--priority gap1,gap2]`
  - Status becomes `leased`; expires to `pending` if TTL lapses.
- Validate gap resolved: `python -m src.cli queue verify --id <gap_type:item_id>`
- Complete: `python -m src.cli queue complete --id <gap_type:item_id> --agent <name> [--verify]`
- Release: `python -m src.cli queue release --id <gap_type:item_id> --agent <name>`
- GC (revert expired leases, optionally prune old done): `python -m src.cli queue gc [--prune-done-older-than N]`
- List counts: `python -m src.cli queue ls`
- Do not edit `work_queue.jsonl` by hand; use the CLI.
- Pruning: only removes items marked `resolved`/`superseded`; gaps persist until fixes land.
- Sources of queue items (indexer rebuilds on each run):
  - `referenced_only`: IDs referenced but not defined.
  - `unresolved_ref`: free-text refs.
  - `import_stub`: recipes with empty steps/import variants.
  - `no_recipe`: defined items (part/material/machine) missing a recipe.
    - `is_scrap: true` items are exempt from `no_recipe` and treated as byproducts.
  - `missing_field`: required field absent (e.g., energy_model/time_model).
  - `no_provider_machine`: resource_type with no machine capability.
  - `invalid_recipe_schema`: recipe steps not in the current schema.
- Workflow loop:
  1) Pop next: `python -m src.cli queue pop`.
  2) Implement one item (add YAML/recipe/process/etc.). Prefer ≥3-step recipes with time/labor/machine-hours when possible. Reference missing processes explicitly if needed so they queue.
  3) Fix all issues in the touched file before moving on (not just the queued gap).
  4) Validate the entity to ensure no remaining issues in that file: `python -m src.cli validate --id <type:id>`.
  5) Verify the gap is gone: `python -m src.cli queue verify --id <gap_type:item_id>` (or use `queue complete --verify`).
     - Note: `queue complete --verify` only checks that the gap ID no longer appears in the queue; it does not verify all issues in the file.
     - `validate` and `queue complete --verify` run the indexer internally.
  6) Inspect `out/work_queue.jsonl` and any reports (`out/unresolved_refs.jsonl`, `out/missing_recipes.jsonl`, `out/invalid_recipes.jsonl`) if needed.
  7) Repeat; only mark tasks resolved by removing/renaming queue entries if explicitly done.

### Manual Queue Addition (Discovered Issues)

**When to fix directly vs. queue:**
- **Fix directly** if the issue is in the file you're currently editing AND you have sufficient information to make the change
- **Queue the work** if it requires special research, working in other files, or is outside your current task scope

When you discover issues that need separate attention, add them to the queue for another agent:

**Add a single gap:**
```bash
python -m src.cli queue add \
  --gap-type quality_concern \
  --item-id steel_melting_v0 \
  --description "Energy model shows 1.2 kWh/kg but Ellery 2023 paper indicates 3.5 kWh/kg" \
  --context '{"paper_ref": "ellery_2023.pdf", "section": "Table 4"}'
```

**Add multiple gaps from a file:**
```bash
python -m src.cli queue add --file queue_tasks/discovered_issues.jsonl
```

File format (JSONL):
```json
{"gap_type": "quality_concern", "item_id": "foo_v0", "description": "..."}
{"gap_type": "needs_consolidation", "item_id": "bar_v0", "description": "Found duplicates: bar_v1, bar_alt"}
```

**Common gap types for manual addition:**
- `quality_concern` - Incorrect data, unrealistic estimates, conflicts with papers
- `needs_consolidation` - Multiple similar items should be merged
- `needs_review` - Requires domain expertise or verification
- `missing_dependency` - Found reference to undefined item not caught by indexer
- `data_inconsistency` - Values don't match across related items

**Create new gap types** by using a descriptive name (e.g., `energy_model_mismatch`). View all types with:
```bash
python -m src.cli queue gap-types
```

**For agents:** Use the `queue_add_gap` tool to add discovered issues programmatically. See `queue_agents/kb_tools.py` for API documentation.

## Verification (how it works across gap types)

**Canonical rule:** verification always means "run the indexer and ensure the gap id no longer appears in `out/work_queue.jsonl`." The queue is rebuilt from scratch each run, so absence is the definitive signal.

Supporting reports by gap type (optional, for debugging):
- `referenced_only`: only in `out/work_queue.jsonl` (no dedicated report)
- `unresolved_ref`: `out/unresolved_refs.jsonl`
- `import_stub`: `out/import_stubs.jsonl`
- `no_recipe`: `out/missing_recipes.jsonl`
- `missing_field`: `out/missing_fields.jsonl`
- `no_provider_machine`: `out/orphan_resources.jsonl`
- `invalid_recipe_schema`: `out/invalid_recipes.jsonl`

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
- Recipe steps can include `time_model`/`energy_model` overrides per 013 (complete override when `type` is present).
- `resource_requirements` uses `machine_id` with `qty` + `unit` (use `hr` for time).
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
- Import items: Add `is_import: true` to item definition (per ADR-007, no recipe needed).
- Environment source: `environment_source_v0` (legacy generic placeholder; prefer explicit `process_type: boundary` processes for in-situ collection).
- Manual labor: use `labor_bot_general` in `resource_requirements`.

## Boundary/Terminal Processes
To prevent infinite recursion in the dependency graph, some processes are **terminal nodes** that represent in-situ boundary conditions (no upstream inputs).
Use `process_type: boundary` only for **in-situ resource collection** (e.g., regolith and ice collection, solar irradiance).

**Imports are not boundary processes.** Model imports via `is_import: true` on the item (per ADR-007). Import items don't need recipes.

Boundary processes:
- Must have `inputs: []` and at least one output.
- Use standard 012/014 models (`time_model.type: batch|linear_rate`, `energy_model.type: fixed_per_batch|per_unit`).
- Should include `resource_requirements` for the collecting machine.

## Energy and Time Models (Machine-Readable Schema) - **NEW 012/014 FORMAT**

⚠️ **SCHEMA UPDATE IN PROGRESS**: The KB is transitioning to new time and energy model schemas per 012 and 014. See `docs/ADRs/` for full specification.

**All new processes MUST use the new schema. Old schema will cause validation errors.**

### Process Type (012) - **REQUIRED**

Every process must specify its type:

```yaml
process_type: continuous  # or: batch, boundary
```

**Semantics:**
- **`continuous`** — Rate-based production (kg/hr, L/hr, unit/hr), linear scaling, steady-state operation
  - Examples: crushing, electrolysis, distillation, machining (one part after another)
- **`batch`** — Discrete batches, setup per batch, batch size from outputs
  - Examples: assembly, firing, heat treatment, molding
- **`boundary`** — In-situ collection with no upstream inputs
  - Examples: regolith mining, polar ice extraction, solar irradiance collection

### Time Model (012)

#### For Continuous Processes

```yaml
process_type: continuous
time_model:
  type: linear_rate
  rate: 10.0                    # Numeric value
  rate_unit: kg/hr              # Compound unit: <unit>/<time_unit>
  scaling_basis: input_material  # Which input/output drives time (REQUIRED)
  notes: "Continuous crushing at 10 kg/hr throughput"
```

**Key features:**
- **Flexible units**: `kg/hr`, `unit/hr`, `L/hr`, `m/hr`, `L/min` (any unit, not just kg)
- **Required `scaling_basis`**: Explicitly specifies which input or output item drives the time calculation
- **Compound rate_unit**: Format is `numerator/denominator` (e.g., `kg/hr`, `unit/min`)
- **Natural count rates**: Use `12 unit/hr` (not `0.083 hr/unit`)

#### For Batch Processes

```yaml
process_type: batch
time_model:
  type: batch
  setup_hr: 0.1        # Optional, defaults to 0
  hr_per_batch: 0.9    # Required
  notes: "Assembly of 1 motor per batch"
```

**Key features:**
- Type is `batch` (not `fixed_time` - old name)
- `setup_hr` is optional (defaults to 0)
- Batch size implicit from process `outputs` (not duplicated in time_model)
- No `scaling_basis` - batch size defined by outputs

### Energy Model (014)

#### For Per-Unit Energy

```yaml
energy_model:
  type: per_unit
  value: 0.3                    # Numeric value
  unit: kWh/kg                  # Compound unit: <energy_unit>/<scaling_unit>
  scaling_basis: input_material  # Which input/output drives energy (REQUIRED)
  notes: "Bond work index for lunar regolith comminution"
```

**Key features:**
- **Flexible energy units**: `kWh`, `MWh`, `MJ`, `GJ`, `BTU`
- **Flexible scaling units**: `kg`, `unit`, `L`, `m`, etc.
- **Required `scaling_basis`**: Explicitly specifies which input or output item drives energy
- **Compound unit format**: `kWh/kg`, `kWh/unit`, `MJ/L`, etc.

**Supported energy units** (normalized to kWh internally):
- `kWh` = 1.0, `MWh` = 1000.0, `Wh` = 0.001
- `MJ` = 0.2778, `GJ` = 277.8, `BTU` = 0.000293

#### For Fixed Energy Per Batch

```yaml
energy_model:
  type: fixed_per_batch
  value: 120.0
  unit: kWh              # Simple energy unit (no denominator)
  notes: "Kiln firing energy independent of load within 5-15 kg range"
```

**Key features:**
- Type is `fixed_per_batch` (not `kWh_per_batch` - old name)
- No `scaling_basis` - batch size implicit from process outputs
- Energy unit flexible (`kWh`, `MJ`, etc.), but NO compound unit (no `/kg` part)

### Scaling Basis Rules

**Purpose:** Explicitly specify which input or output drives time/energy calculation.

**Examples:**
```yaml
# Single input - unambiguous but still required
inputs:
  - item_id: regolith_coarse
    qty: 1.0
    unit: kg
time_model:
  scaling_basis: regolith_coarse  # Must specify

# Multiple inputs - MUST specify which one drives time
inputs:
  - item_id: steel_sheet
    qty: 10.0
    unit: kg
  - item_id: lubricant
    qty: 0.5
    unit: L
time_model:
  scaling_basis: steel_sheet  # Explicitly steel, not lubricant

# Output scaling (less common but valid)
time_model:
  scaling_basis: aluminum_pure  # Output drives time
```

### Complete Example: Continuous Process

```yaml
id: regolith_crushing_grinding_v0
kind: process
process_type: continuous

inputs:
  - item_id: regolith_coarse_fraction
    qty: 1.0
    unit: kg

outputs:
  - item_id: regolith_powder
    qty: 1.0
    unit: kg

time_model:
  type: linear_rate
  rate: 10.0
  rate_unit: kg/hr
  scaling_basis: regolith_coarse_fraction
  notes: "Continuous crushing at 10 kg/hr throughput"

energy_model:
  type: per_unit
  value: 0.3
  unit: kWh/kg
  scaling_basis: regolith_coarse_fraction
  notes: "Bond work index for lunar regolith comminution"
```

**Calculation example (100 kg input):**
- Time: 100 kg / 10 kg/hr = 10 hours
- Energy: 100 kg × 0.3 kWh/kg = 30 kWh
- Average power: 30 kWh / 10 hr = 3 kW

### Complete Example: Batch Process

```yaml
id: motor_final_assembly_v0
kind: process
process_type: batch

inputs:
  - item_id: stator_rotor_lamination_set
    qty: 5.0
    unit: kg
  # ... more inputs

outputs:
  - item_id: motor_electric_small
    qty: 1.0
    unit: unit

time_model:
  type: batch
  setup_hr: 0.1
  hr_per_batch: 0.9
  notes: "Assembly of 1 motor per batch"

energy_model:
  type: per_unit
  value: 0.2
  unit: kWh/unit
  scaling_basis: motor_electric_small  # Output drives energy
  notes: "Testing and tool energy per motor"
```

**Calculation example (10 motors):**
- Batches: 10 motors / 1 motor per batch = 10 batches
- Time: 10 × (0.1 + 0.9) = 10 hours
- Energy: 10 unit × 0.2 kWh/unit = 2 kWh

### Boundary/Terminal Processes

Boundary processes are now supported via `process_type: boundary`. Example (in-situ regolith collection):

```yaml
process_type: boundary
outputs:
  - item_id: regolith_lunar_mare
    qty: 100
    unit: kg
time_model:
  type: linear_rate
  rate: 100
  rate_unit: kg/hr
  scaling_basis: regolith_lunar_mare
energy_model:
  type: per_unit
  value: 0.05
  unit: kWh/kg
  scaling_basis: regolith_lunar_mare
resource_requirements:
  - machine_id: labor_bot_general_v0
    qty: 1
    unit: count
notes: "In-situ boundary process; no upstream inputs."
```

### Migration from Old Schema

**DEPRECATED formats (will cause validation errors):**

```yaml
# OLD - Don't use:
time_model:
  type: linear_rate
  rate_kg_per_hr: 10.0  # ❌ Deprecated
  hr_per_kg: 0.1         # ❌ Deprecated

energy_model:
  type: kWh_per_kg       # ❌ Deprecated type name
  value: 0.3

time_model:
  type: fixed_time       # ❌ Deprecated, use 'batch'
  hr_per_batch: 1.5
```

**NEW formats (required):**

```yaml
# NEW - Use this:
process_type: continuous  # ✅ Required
time_model:
  type: linear_rate
  rate: 10.0              # ✅ New format
  rate_unit: kg/hr        # ✅ Compound unit
  scaling_basis: input_item  # ✅ Required

energy_model:
  type: per_unit          # ✅ New type name
  value: 0.3
  unit: kWh/kg            # ✅ Compound unit
  scaling_basis: input_item  # ✅ Required

# For batch:
process_type: batch       # ✅ Required
time_model:
  type: batch             # ✅ New name (was 'fixed_time')
  hr_per_batch: 1.5
```

**See `docs/ADRs/012-process-types-and-time-model.md` and `docs/ADRs/014-energy-model-redesign.md` for complete specifications.**

## Validation Rules (017)

The indexer validates all processes against 012/014/017 schemas. Validation issues are categorized by severity:

| Level | Meaning | Action |
|-------|---------|--------|
| **ERROR** | Schema violation, cannot be used in simulation | Blocks simulation, must fix |
| **WARNING** | Missing recommended field | Should fix, allows use |
| **INFO** | Suggestion for improvement | Optional |

### Common Validation Errors

#### Schema Violations (ERROR)

1. **`process_type_required`** - Missing `process_type` field
   ```yaml
   # ❌ ERROR:
   kind: process
   time_model: ...

   # ✅ FIX: Add process_type
   kind: process
   process_type: continuous  # or batch
   time_model: ...
   ```

2. **`energy_model_type_invalid`** - Using old energy model type names
   ```yaml
   # ❌ ERROR:
   energy_model:
     type: kWh_per_kg  # Old format

   # ✅ FIX: Use new format
   energy_model:
     type: per_unit
     value: 0.3
     unit: kWh/kg
     scaling_basis: input_item
   ```

3. **`required_field_missing`** - Missing required fields
   ```yaml
   # ❌ ERROR - Missing scaling_basis:
   time_model:
     type: linear_rate
     rate: 10.0
     rate_unit: kg/hr
     # Missing scaling_basis!

   # ✅ FIX:
   time_model:
     type: linear_rate
     rate: 10.0
     rate_unit: kg/hr
     scaling_basis: input_material  # Required!
   ```

4. **`deprecated_field`** - Using deprecated field names
   ```yaml
   # ❌ ERROR:
   time_model:
     type: linear_rate
     rate_kg_per_hr: 10.0  # Deprecated

   # ✅ FIX:
   time_model:
     type: linear_rate
     rate: 10.0
     rate_unit: kg/hr
     scaling_basis: input_item
   ```

#### Semantic Errors (ERROR)

1. **`scaling_basis_not_found`** - scaling_basis references non-existent input/output
   ```yaml
   # ❌ ERROR:
   inputs:
     - item_id: steel_sheet
       qty: 10.0
       unit: kg
   time_model:
     scaling_basis: aluminum  # Not in inputs or outputs!

   # ✅ FIX:
   time_model:
     scaling_basis: steel_sheet  # Must match actual input/output
   ```

2. **`invalid_compound_unit`** - Malformed compound unit
   ```yaml
   # ❌ ERROR:
   time_model:
     rate_unit: kg per hour  # Invalid format

   # ✅ FIX:
   time_model:
     rate_unit: kg/hr  # Use "/" separator
   ```

3. **`setup_hr_in_continuous`** - Continuous process with setup time
   ```yaml
   # ❌ ERROR:
   process_type: continuous
   time_model:
     type: linear_rate
     setup_hr: 0.5  # Not allowed in continuous!

   # ✅ FIX: Either remove setup_hr or change to batch
   process_type: batch  # Change to batch if setup is needed
   time_model:
     type: batch
     setup_hr: 0.5
     hr_per_batch: 2.0
   ```

### Validation Workflow

When you encounter validation errors:

1. **Check validation report**: `out/validation_report.md`
2. **Find specific errors**: `out/validation_issues.jsonl`
3. **Fix the issue** in the YAML file
4. **Re-validate**: `python -m src.cli validate --id process:regolith_mining_highlands_v0`
   - (Find process IDs: `ls kb/processes/` or `grep "^id:" kb/processes/*.yaml`)
5. **Verify fix**: Error should disappear from `validation_issues.jsonl`

**See `docs/ADRs/017-validation-and-error-detection.md` for complete validation rules.**

## Commands (New Unified CLI)

**KB Core Tools** (`python -m src.cli`):
- **Index**: `python -m src.cli index` — Build KB index with validation
  - Outputs: `out/index.json`, `out/validation_report.md`, `out/work_queue.jsonl`, etc.
- **Validate**: `python -m src.cli validate --id <type:id>` — Validate specific KB item
  - Example: `python -m src.cli validate --id process:regolith_mining_highlands_v0`
- **Auto-fix**: `python -m src.cli auto-fix [--dry-run] [--max-fixes N] [--rule RULE]`
  - Automatically fix validation issues
  - Use `--dry-run` to preview fixes without writing
  - Example: `python -m src.cli auto-fix --dry-run --rule process_type_required`
- **Closure analysis**: `python -m src.cli closure --machine <id>` or `--all`
  - Analyze material closure for machines (ISRU vs import breakdown)
  - Example: `python -m src.cli closure --all --output out/closure_report.txt`

**Queue Commands** (`python -m src.cli`):
- Queue: `python -m src.cli queue pop`, `python -m src.cli queue prune`

**Environment**:
- Virtualenv: `uv sync` to install deps.

## Principles
- Do not hide work: placeholders/imports should queue follow-ups.
- Prefer consolidation over proliferation (shared parts/process IDs).
- Estimate masses and times (within 5× is acceptable); avoid nulls.
- Reference missing processes/items explicitly to surface work.
- Avoid collisions: always lease a task before editing; do not modify items you haven’t leased. If two agents touch the same item, reconcile (merge components/notes) rather than overwrite, and leave context in `notes`.
