# ISRU Plan Automation (RunbookPlan)

This document describes the new **RunbookPlan** automation scripts for building,
running, and optimizing simulations without editing Markdown runbooks directly.
Plans can still be exported later, but the internal plan is the primary API.

## Goals

- Define a machine target once and generate a simulation plan programmatically.
- Execute the plan directly via `SimulationEngine` (no runbook parsing required).
- Incrementally improve ISRU by expanding imported items into local recipes.

## Files

- `scripts/analysis/runbook_plan.py`  
  Defines the RunbookPlan data structure and JSON serialization.

- `scripts/analysis/plan_builder_import_only.py`  
  Builds an import-only plan from the machine's recipe inputs (or BOM if no recipe).

- `scripts/analysis/plan_runner.py`  
  Executes a RunbookPlan directly and reports target-machine ISRU.

- `scripts/analysis/plan_optimizer_greedy.py`  
  Greedy optimizer that expands imported items into local recipes, re-plans,
  and re-runs to measure ISRU improvement.

## RunbookPlan Summary

A plan includes:

- `sim_id`: Simulation identifier
- `target_machine_id`: Machine to build
- `target_recipe_id`: (optional) Recipe used to produce target machine
- `imports`: Dict of item imports and quantities
- `recipes`: List of recipe runs (non-target)
- `build_machine`: Whether to build via BOM (used when no target recipe)
- `notes`: Freeform notes for traceability

## Phase A: Import-Only Plan

Build a baseline plan that imports all recipe inputs and required machines.

```bash
.venv/bin/python scripts/analysis/plan_builder_import_only.py \
  --machine-id reduction_furnace_v0 \
  --sim-id rf_import_only
```

Output:
```
out/plan_reduction_furnace_v0_import_only.json
```

## Phase B: Execute a Plan

Run the plan directly and get provenance-based ISRU for the target machine:

```bash
.venv/bin/python scripts/analysis/plan_runner.py \
  --plan out/plan_reduction_furnace_v0_import_only.json \
  --reset
```

## Phase C: Greedy Optimization

Expand imported items into local recipes, one step at a time.

```bash
.venv/bin/python scripts/analysis/plan_optimizer_greedy.py \
  --machine-id reduction_furnace_v0 \
  --sim-id rf_opt \
  --iterations 3
```

Optional flags:
- `--candidate <item_id>`: Force a specific import to expand
- `--verbose`: Show plan diffs (added/removed imports and recipes)
- `--max-depth <n>`: Limit recursive expansion depth

Optimizer behavior:
- Recipes are executed in dependency order (producer → consumer).
- Shared input demand is aggregated before execution.
- Trial plans are saved to `out/plan_<machine>_trial_<n>.json` for inspection.

## Notes

- Plans run directly against `SimulationEngine` and the current KB.
- The optimizer avoids KB fixes and only uses existing recipes.
- The plan runner orders recipes by dependency (producer -> consumer) to prevent
  missing-input failures.
