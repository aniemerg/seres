# Self-Reproducing Set Workflow (SimPlan)

This memo documents the workflow and scripts used to iteratively converge on a minimal self-reproducing machine set using SimPlans and provenance analysis.

## Goal
Build and optimize SimPlans for a target machine set, then iteratively extract imported machines from provenance and expand the target set until the imported-machine list stabilizes.

## Core Scripts

### 1) SimPlan optimizer (per machine)
- Script: `scripts/analysis/simplan_optimizer_greedy.py`
- Purpose: Build an import-only plan, then greedily expand imported items into local recipes to improve ISRU.
- Output: optimized plan JSON (`out/simplans/<machine>_optimized.json` when used via batch runner).

Example:
```
.venv/bin/python3 scripts/analysis/simplan_optimizer_greedy.py \
  --machine-id drill_press \
  --sim-id simplan_drill_press \
  --iterations 3 \
  --max-depth 6
```

### 2) Batch optimizer
- Script: `scripts/analysis/simplan_batch_run.py`
- Purpose: Run optimizer across a list of machines, capture failures, and write summaries.
- Supports:
  - `--machine-list <file>` (one machine ID per line)
  - `--skip-existing` (do not re-optimize if plan exists)
  - `--out-dir out/simplans`

Example:
```
.venv/bin/python scripts/analysis/simplan_batch_run.py \
  --machine-list out/next_round_machines_roundN.txt \
  --skip-existing \
  --out-dir out/simplans \
  --verbose
```

### 3) Import extraction (provenance)
- One-off approach used in this work:
  - Read each optimized plan’s `sim_id`
  - Load `simulations/<sim_id>/snapshot.json`
  - Extract machines with `imported_kg > 0`
- Output: `out/next_round_machines_roundN.txt`

## Iterative Convergence Loop
1. Start with a machine list (e.g., `runbooks/machine_runbook_queue_sequential.md`).
2. Run batch optimizer to create per-machine optimized plans.
3. Extract imported machines from each simulation’s provenance (per plan `sim_id`).
4. Write next-round list (`out/next_round_machines_roundN.txt`).
5. Repeat until the list stops changing.

## Key Fixes Applied During Convergence
- **Machines as tools, not inputs**: Removed reusable machines from process/recipe inputs (moved to `resource_requirements`).
- **Placeholder intermediates**: Removed `instrument_uncalibrated` as a placeholder; inlined calibration into recipes.
- **Unit normalization**: Standardized `spring_compression_small` to kg usage across recipes/BOMs; adjusted spring recipe output slightly to avoid float underflow.
- **Recipe overrides**: Removed machine items from recipe step inputs where they were being consumed unintentionally.

## Convergence Result
- The imported-machine set stabilized at **134 machines** by round 5 and remained stable through round 10.
- The converged list is in: `docs/minimal_self_reproducing_set.md`.

## Notes
- Sim IDs used for provenance extraction should come from each plan’s `sim_id` field, not just `simplan_<machine>`.
- If a machine lacks a recipe, the optimizer hard-fails (by design).
- Use `out/next_round_machines_roundN.txt` as the canonical input for subsequent rounds.
