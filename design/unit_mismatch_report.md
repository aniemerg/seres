# Unit/Mass Mismatch Report (Runbooks + KB)

## Summary

We are hitting unit mismatches (kg vs unit) during runbook execution. The engine *can*
convert between `unit` and `kg` for items that have an explicit mass, but the current
KB recipes and process steps sometimes produce the wrong item IDs/units, which prevents
those conversions from being used where we expect them.

This is showing up most clearly in the delta robot runbooks:

- `recipe_machine_delta_robot_v0` expects several inputs as `unit`, while many of the
  upstream recipes output those items as `kg` or output **different** generic items.
- Even when a part has a mass and should be convertible, the recipe steps often output
  placeholder IDs (`machined_part_raw`, `assembled_equipment`, etc.) that never become
  the final target part (e.g., `machine_frame_small`).

## What the engine actually does with units

The engine uses `UnitConverter` to allow conversions if the item has a mass:

- `kg <-> unit` conversions are supported when the item definition provides
  `mass_kg`/`mass` (`src/kb_core/unit_converter.py`).
- This is already used in import `--ensure` and inventory checks.

So *in principle* it is valid for a part to have a mass and be referenced as `1 unit`
in a recipe. The conversion can work as long as the item’s `mass` is defined and the
recipe is actually asking for the same item ID.

## Where the mismatch is happening (concrete examples)

1) **Machine frame recipe produces the wrong item**

`recipe_machine_frame_small_v0` targets `machine_frame_small` and defines outputs in kg,
but the steps reference generic processes whose outputs are *not* `machine_frame_small`.

- `kb/recipes/recipe_machine_frame_small_v0.yaml`
- `kb/processes/machining_finish_basic_v0.yaml`

Result: the recipe does not yield `machine_frame_small` in inventory, so `sim.import`
with `ensure: true` still imports it later. This is not a unit conversion issue; it is
an output mapping issue.

2) **Delta robot recipe asks for `unit`, upstream parts are `kg`**

`recipe_machine_delta_robot_v0` inputs use `unit` for parts like:

- `machine_frame_small`
- `robot_arm_link_aluminum`
- `electric_parallel_gripper`
- `power_distribution_board`
- `assembled_cable_harness`

But the item definitions for several of these are in `kg`:

- `kb/items/parts/machine_frame_small.yaml` (kg)
- `kb/items/parts/robot_arm_link_aluminum.yaml` (kg)
- `kb/items/parts/electric_parallel_gripper.yaml` (kg)
- `kb/items/parts/power_distribution_board.yaml` (kg)
- `kb/items/parts/assembled_cable_harness.yaml` (kg)

This can be converted if the item has a mass, but in practice the chain often fails
because recipe steps don’t yield the final item IDs in the expected unit.

3) **Mixed-unit inventory shows fractional units**

When conversion is applied, we end up with fractional units or “unit” quantities
converted from kg (e.g., `0.75 unit`). This is mathematically correct, but it makes
inventory hard to interpret and creates confusion about discrete parts vs bulk.

## Why this matters for mass tracking (imports vs ISRU)

The project goal is to track import mass versus ISRU. That goal can still be met with
either of these patterns:

1) **Discrete parts tracked as `unit` + mass per unit**, and mass is derived.
2) **All parts tracked in `kg`**, and any “unit” references are avoided.

The issue today is *not* that mass tracking is impossible; it is that the system is
inconsistent, so the conversion logic is frequently bypassed by mismatched item IDs.

## Possible solutions (with tradeoffs)

### Option A: Standardize on `unit` for discrete parts

- Keep mass in item definitions for conversion + accounting.
- Update recipes to use `unit` for discrete parts consistently.
- Ensure recipe steps produce the final item IDs in `unit`.

Pros:
- Aligns with “one part” semantics.
- Easy to reason about counts.

Cons:
- Existing recipes/items in kg must be adjusted.
- Requires more careful mass conversion when reporting.

### Option B: Standardize on `kg` for parts and assemblies

- Treat parts as materialized mass objects.
- Update recipes (including `recipe_machine_delta_robot_v0`) to use `kg`.
- Keep units for true countable machines only.

Pros:
- Mass tracking is direct and unambiguous.
- Fewer conversions.

Cons:
- “Count of parts” becomes indirect.
- Some recipes conceptually need discrete parts (motors, grippers).

### Option C: Keep mixed units but fix the mapping

- Ensure every recipe step outputs the target item ID (override outputs).
- Normalize item IDs so steps produce the correct target items, then conversions can
  happen correctly.
- Add validation to flag recipes whose steps never output target IDs.

Pros:
- Minimal conceptual change.
- Leaves unit vs kg choice flexible per item.

Cons:
- Still allows confusing mixed-unit inventory.
- Requires careful QA to avoid hidden mismatches.

## Proposed policy: discrete-vs-bulk unit flag (standardize units)

We will standardize on:

- **Discrete parts:** `unit` (e.g., motors, frames, grippers, circuit boards).
- **Bulk materials:** `kg` (e.g., regolith, ores, stock metals, adhesives).

Add a KB-level flag that declares the canonical unit category per item. This makes
the expected unit *explicit* rather than inferred, and it allows validation to be
deterministic.

Suggested KB field (name can be finalized in schema/ADR):

- `unit_kind: discrete|bulk`

Rules:

- If `unit_kind: discrete`, then the item’s canonical unit is `unit`. It may also
  declare `mass`/`mass_kg` as **mass per unit**, so conversions to/from kg are possible.
- If `unit_kind: bulk`, then the item’s canonical unit is `kg`, and it should not
  appear in recipes as `unit` (unless there is a specific conversion and intent).

This policy preserves mass tracking (every discrete part still has `mass`) while
improving clarity in runbooks and recipes.

### Mass handling under this policy

- **Discrete parts:** `mass_kg` is required and is interpreted as **mass per unit**.
  This keeps import-vs-ISRU accounting intact while using `unit` as the canonical
  recipe quantity.
- **Bulk parts:** `mass_kg` is optional. If present, it should represent mass per kg
  (typically `1.0`) and is mostly useful for derived units; otherwise omit it.
- **Conversions:** `UnitConverter` already supports `unit <-> kg` when `mass_kg`
  exists, so mass tracking remains consistent across inventory, imports, and recipes.

## Impact on the simulation system

### KB schema and validation

- **Schema update:** add a `unit_kind` (or similar) field to item definitions.
  This should be documented in `docs/kb_schema_reference.md`.
- **Validation update:** new checks should verify that:
  - Item definitions use `unit` when `unit_kind: discrete` and `kg` when
    `unit_kind: bulk`.
  - Recipe inputs/outputs for an item use the canonical unit (unless conversion
    is explicitly allowed by mass).
  - If conversion is used, it must be **convertible** and intentional (the
    validator can emit a warning when a recipe uses a non-canonical unit even
    if convertible).

### Runtime behavior and inventory

- **No runtime changes required** to `UnitConverter`: it already supports kg/unit
  conversion when `mass` is present.
- **Clearer inventory semantics:** inventory will show discrete parts in `unit` and
  bulk in `kg`, reducing fractional “unit” values for discrete parts.
- **Imports with `--ensure`:** behave the same, but now discrepancies will be
  flagged earlier by validation if units do not match the item’s `unit_kind`.

### Recipe authoring expectations

- Recipes should *prefer* the canonical unit for an item.
- For discrete items:
  - Steps should output the discrete item ID in `unit`.
  - If a process inherently yields `kg`, explicitly override outputs to `unit`
    to preserve canonical units (conversion remains possible for accounting).
- For bulk items:
  - Steps and recipes should stay in `kg`.

## ADR and documentation updates required

- **ADR-016 (Unit conversion system):** add explicit line items:
  - Define `unit_kind` (`discrete|bulk`) and canonical unit per kind.
  - Specify **mass-per-unit** semantics for discrete parts (`mass_kg` required).
  - Allow conversions when `mass_kg` exists, but treat non-canonical usage as
    validation warnings or errors depending on policy.
- **ADR-018 (Recipe inputs/outputs validation):** add explicit line items:
  - Validate item unit matches its `unit_kind` canonical unit.
  - Validate recipe inputs/outputs prefer canonical unit; warn on non-canonical
    but convertible units.
  - Keep/extend the target-output-produced check from this report.
- **ADR-020 (Recipe orchestration and scheduling):** no direct change needed, but
  note that validations may block scheduling for unit_kind mismatches.
- **KB schema reference:** add `unit_kind` field with allowed values and examples.
- **Runbook authoring guidance (if any doc exists):** recommend canonical unit use.

## Tests and tooling impacts

### Validator tests (new or updated)

- Items with `unit_kind: discrete` but `unit: kg` -> error.
- Items with `unit_kind: discrete` and missing `mass_kg` -> error.
- Items with `unit_kind: bulk` but `unit: unit` -> error.
- Recipe input uses non-canonical unit where conversion is not possible -> error.
- Recipe input uses non-canonical unit where conversion is possible -> warning or
  info (policy choice).

### Indexer/queue impact

- New validation rules will create additional queue items; expect a spike in
  `validation_*` gaps until KB is normalized.
- Work queue behavior is unchanged, but downstream prioritization may need to
  group unit-kind mismatches for batch cleanup.

## Updated suggested path forward (with unit_kind policy)

1) **Add `unit_kind` to item definitions** (discrete vs bulk).
2) **Align item units** to canonical units (discrete -> `unit`, bulk -> `kg`).
3) **Update recipes and steps** so outputs match the target item ID and canonical
   unit.
4) **Add validator checks**:
   - Target output produced (existing plan).
   - Unit convertibility (existing plan).
   - Unit-kind alignment (new).
5) **Normalize runbooks** to import in canonical units (using `--ensure`).

## Design risks to be aware of

- **Silent fallback to imports:** If a local recipe yields the wrong item ID, `ensure`
  will import the item even if you “built” something nearby.
- **Fractional unit confusion:** Mixed units can yield fractional “unit” quantities,
  which is correct but not intuitive for discrete parts.
- **Validation blind spots:** The current validators don’t guarantee that recipe steps
  actually produce the recipe target item (or the right unit).

## Suggested path forward (aligned with mass tracking)

If the priority is tracking ISRU vs imports by mass, the safest approach is:

1) **Make item unit conventions explicit**:
   - `kg` for bulk materials and structural parts.
   - `unit` for discrete machines or highly discrete components.
2) **Update recipes to match those conventions**:
   - Ensure steps output the target item IDs in the correct unit.
3) **Add validator checks**:
   - Flag recipes where no step outputs the target item ID.
   - Flag unit mismatches when conversion is impossible.

This keeps mass tracking accurate while preventing the silent fallback-to-import
behavior that we’re seeing now.

## Validation implementation plan (queue + indexer + tests)

### Where the checks should live

- **Core rules:** `src/kb_core/validators.py` so they run in both indexer and runtime validation.
- **Queue integration:** `src/indexer/indexer.py` already converts validation issues into
  work queue items. New rules will show up as `validation_<rule>` gaps.
- **Documentation/queue behavior:** `docs/README.md` describes queue semantics; no new
  queue mechanics required.

### Check 1: Recipe target output check

Goal: ensure at least one step (after overrides are resolved) produces the recipe
`target_item_id` (or provides a convertible output that matches the target item).

Implementation details:

1) **Add rule in validators**
   - File: `src/kb_core/validators.py`
   - New helper (name suggestion):
     - `validate_recipe_target_produced(recipe, kb, converter)`
   - Logic:
     - Resolve each step with `resolve_recipe_step_with_kb`.
     - Collect step outputs/byproducts item_id + unit.
     - If any output item_id == target_item_id -> pass.
     - If output item_id == target_item_id but unit differs, require
       `converter.can_convert(output_unit, target_unit, item_id=target_item_id)`.
     - If no match, emit **ERROR** (or WARNING if you want a softer rollout) with:
       - `rule`: `recipe_target_not_produced`
       - `field_path`: `steps`
       - `fix_hint`: add/override outputs in at least one step to produce target.

2) **Wire into validate_recipe**
   - Call from `validate_recipe` once `converter` is available (we need KB access).
   - This ensures the indexer captures it and work queue items are created.

3) **Queue impact**
   - New gaps appear as `validation_recipe_target_not_produced`.
   - These will surface in `out/validation_issues.jsonl` and `out/work_queue.jsonl`.

### Check 2: Unit convertibility check (recipes)

Goal: catch cases where the recipe/steps expect the same item in incompatible units
or where recipe inputs/outputs cannot be converted to step-level units.

Implementation details:

1) **Add rule in validators**
   - File: `src/kb_core/validators.py`
   - New helper (name suggestion):
     - `validate_recipe_unit_convertibility(recipe, kb, converter)`
   - Logic (minimal first pass):
     - For each recipe-level input/output, compare against any step-level
       input/output with the same item_id but different unit.
     - If `converter.can_convert(from_unit, to_unit, item_id)` is False,
       emit **ERROR**:
         - `rule`: `recipe_unit_not_convertible`
         - `field_path`: `inputs` or `outputs` (and include step index in message)
     - Optionally: also check target_item_id unit vs produced unit if target exists.

2) **Wire into validate_recipe**
   - Same as above; needs converter for `can_convert`.

3) **Queue impact**
   - New gaps appear as `validation_recipe_unit_not_convertible`.

### Tests to add

- File: `test/unit/test_validators.py`
  - **Target output check**
    - Recipe with steps that never output target item -> expect `recipe_target_not_produced`.
    - Recipe where a step outputs target item -> no error.
    - Recipe where step outputs target item in a convertible unit (kg <-> unit) -> no error.
    - Recipe where step outputs target item in non-convertible unit -> error.
  - **Unit convertibility check**
    - Same item_id appears at recipe level in kg and step in unit with mass present -> no error.
    - Same item_id appears in kg and step in unit with missing mass -> error.

- Optional: `test/unit/test_indexer_validation.py` if you want to confirm queue item
  creation in indexer (not strictly required since indexer already emits all
  validation issues).

### Rollout order (safe + reversible)

1) Implement checks in `validators.py` with **WARNING** severity.
2) Run indexer and inspect queue volume.
3) If volume is manageable, promote to **ERROR**.

### Known interactions

- These checks overlap with ADR-018 input/output resolvability, but they add a
  stronger guarantee: the recipe actually produces its target and the units are
  convertible.
- Template processes are already guarded by `validate_recipe_step_inputs`; target
  output check should still run (it depends on resolved step outputs).

## Open questions

- Do we want `machine_frame_small` to be a discrete “unit” (one frame), or a mass
  commodity? Either is workable, but it needs to be consistent across recipes.
- Should runbooks prefer `kg` everywhere for parts (to make ISRU mass accounting
  simpler), or `unit` for discrete assemblies (to make counts simpler)?
