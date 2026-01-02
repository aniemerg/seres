# Labor Bot General v0 CLI Simulation Feedback - 2026-01-02

## Simulation Summary

**Goal**: Build `labor_bot_general_v0` using the simulation CLI (no manual BOM parsing).

**Simulation ID**: `cobalt_kite_731`

**Result**: ❌ **FAILED** - Could not build via recipe or `build-machine` due to planning/output issues and missing components.

---

## Commands Used

```bash
.venv/bin/python -m src.cli sim init --sim-id cobalt_kite_731
.venv/bin/python -m src.cli sim plan --recipe recipe_machine_labor_bot_general_v0
.venv/bin/python -m src.cli sim run-recipe --sim-id cobalt_kite_731 --recipe recipe_machine_labor_bot_general_v0 --quantity 1
.venv/bin/python -m src.cli sim build-machine --sim-id cobalt_kite_731 --machine labor_bot_general_v0
.venv/bin/python -m src.cli sim plan --process assembly_basic_v0
```

---

## Issues Found

### 1) `sim plan --recipe` ignores an existing recipe

**Observed output**:
```
DEPENDENCY TREE:

├─ General labor bot (automation) (1.00 kg, ~120.00 kg)  [IMPORT]
  ⚠ No recipe defined
```

**Expected**: The plan should detect `recipe_machine_labor_bot_general_v0` and show its steps/requirements (or at least acknowledge it exists).

**Impact**: Users conclude there is no recipe and are pushed to import the robot, even though a recipe exists.

---

### 2) `sim run-recipe` rejects the labor bot recipe as invalid

**Command**:
```
.venv/bin/python -m src.cli sim run-recipe --sim-id cobalt_kite_731 --recipe recipe_machine_labor_bot_general_v0 --quantity 1
```

**Error**:
```
Recipe recipe_machine_labor_bot_general_v0 has no inputs (neither explicit nor inferred from steps).
```

**Context**: The recipe has a step (`assembly_basic_v0`). That process has inputs and resource requirements. The inference logic does not treat step inputs as recipe inputs and rejects the recipe entirely.

**Impact**: The only recipe for `labor_bot_general_v0` cannot be executed via CLI.

---

### 3) Circular resource requirement blocks assembly

`assembly_basic_v0` requires `labor_bot_general_v0` for 0.5 hr.

**Impact**: The labor bot is required to assemble itself, which blocks bootstrap unless a separate minimal assembly path or alternate machine requirement is available.

---

## Suggestions

1. **Fix `sim plan --recipe` to acknowledge existing recipes**
   - Detect recipe by ID and show steps/requirements rather than falling back to “No recipe defined.”

2. **Allow step-input inference for recipes with only process steps**
   - If a recipe has steps, infer inputs/requirements from those steps instead of rejecting as “no inputs.”
   - Alternatively, allow `run-recipe` when steps exist and defer validation to execution.

3. **Resolve bootstrap circularity**
   - Provide a bootstrap assembly path that does not require `labor_bot_general_v0`, or
   - Allow `assembly_basic_v0` to accept a simpler machine/toolset for minimal assembly.

---

## Notes

`sim build-machine` fails as expected due to missing BOM components (first missing: `machine_frame_small`). This is fine, but there is no CLI guidance on how to produce/import missing parts from the BOM without manual parsing.
