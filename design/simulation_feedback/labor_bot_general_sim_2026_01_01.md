# Simulation Feedback: labor_bot_general_v0 build attempt
**Sim ID:** moss_uplift_80
**Date:** 2026-01-01
**Goal:** Build labor_bot_general_v0 via CLI simulation (plan + recipe + build-machine)

## What I did (CLI)
- `sim plan --recipe recipe_machine_labor_bot_general_v0`
- `sim init --sim-id moss_uplift_80`
- `sim run-recipe --sim-id moss_uplift_80 --recipe recipe_machine_labor_bot_general_v0`
- `sim build-machine --sim-id moss_uplift_80 --machine labor_bot_general_v0`

## Findings

### 1) sim plan reports labor_bot_general_v0 as import-only
**Output:**
- Plan shows target as `[IMPORT]` with "No recipe defined" even though `kb/recipes/recipe_machine_labor_bot_general_v0.yaml` exists.

**Impact:**
- Planner does not surface the existing assembly recipe, so it recommends import-only rather than assembly.

**Suspected cause:**
- Recipe has no explicit inputs/outputs and only a single `assembly_basic_v0` step, so planner treats it as empty.

### 2) sim run-recipe fails: no inputs
**Error:**
```
Recipe recipe_machine_labor_bot_general_v0 has no inputs (neither explicit nor inferred from steps). Fix the recipe or process definitions.
```

**Impact:**
- Cannot run the assembly recipe for labor_bot_general_v0 at all.

**Note:**
- `kb/recipes/recipe_machine_labor_bot_general_v0.yaml` has no `inputs:` or `outputs:` and relies on BOM in notes.

### 3) sim build-machine fails immediately on missing components
**Error:**
```
Insufficient component 'machine_frame_small': need 1 count
```

**Impact:**
- Build-machine route is blocked unless all BOM parts are in inventory. There is no helper to list missing components or preflight the BOM.

## Suggestions
1) **Planner should not mark target as import-only if a recipe exists.** Instead, report the recipe but flag it as incomplete (missing inputs/outputs).
2) **Add a validation rule**: recipe with steps must declare inputs/outputs or be inferred from process steps; otherwise warn clearly in `sim plan`.
3) **Add `sim build-machine --preflight` (or similar)** to list missing components and their quantities before failing.
4) **Optionally: auto-generate recipe inputs/outputs from BOM** when a recipe is assembly-only and target item has a BOM.

## Files involved
- `kb/recipes/recipe_machine_labor_bot_general_v0.yaml`
- `kb/boms/bom_labor_bot_general_v0.yaml`
- `docs/SIMULATION_GUIDE.md`
- `src/simulation/cli.py`
