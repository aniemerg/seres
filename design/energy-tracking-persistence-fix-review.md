# Review notes: energy tracking persistence fix plan

## Purpose
This memo captures issues and gaps in `design/energy-tracking-persistence-fix.md` so the author can refine the plan without breaking ADR-020 persistence or scheduler behavior.

## Summary
The plan correctly identifies that per-process energy is lost across CLI command boundaries, but it proposes changes that risk double-counting totals, diverging from current scheduler data structures, and overstating the scope of the bug. The minimal fix should persist energy alongside `process_scheduled` and propagate it into `ProcessRun` for completion logging, without changing scheduler schema or recomputing totals on load.

## Findings
1. **Double-count risk on load**
   - The plan proposes adding `energy_kwh` from `process_scheduled` to `total_energy_kwh` during load for completed processes.
   - `state_snapshot.total_energy_kwh` is already authoritative after any `advance_time()`. Adding energy again will inflate totals.
   - Recommendation: never sum scheduled energy into total if a snapshot exists; only use scheduled energy to support per-process completion logging or to seed in-flight processes.

2. **ProcessRun schema mismatch**
   - The plan changes `ProcessRun` to use `scheduled_start_time/scheduled_end_time` and `machine_reservations` list.
   - The current scheduler uses `start_time/end_time` and a machine dict, and the engine relies on that structure.
   - Recommendation: keep `ProcessRun` shape intact; only add `energy_kwh` as an optional field. Large schema changes should be an explicit refactor plan.

3. **Problem scope overstated**
   - The plan claims `total_energy_kwh` in state snapshots is zero for all runs. In ADR-020, energy is booked at `process_start` and snapshots occur after advancement, so totals should persist.
   - The real persistence gap is per-process energy in `process_complete` after reload (because `_process_energy` is in-memory).
   - Recommendation: narrow the problem statement to focus on per-process event energy and visualization, not total energy unless proven otherwise.

4. **Recipe overrides are not accounted for**
   - Energy is calculated at scheduling time using the base process definition. If recipe steps override energy models, the scheduled energy will be wrong.
   - Recommendation: if overrides are supported, energy must be calculated using the resolved step definition or the plan should explicitly defer override-aware energy.

5. **Event data propagation is incomplete**
   - The plan depends on `ProcessRun.energy_kwh`, but the scheduler event data does not currently carry energy, and reconstruction doesn’t set it.
   - Recommendation: include `energy_kwh` in `process_scheduled` data and attach it to `ProcessRun` when scheduling/reconstructing.

6. **Backward compatibility can be better than zero**
   - The plan defaults missing `energy_kwh` to 0.0 for old logs.
   - Optional improvement: when `process_scheduled` lacks energy, recompute at completion using stored inputs/outputs and the current process definition, while keeping totals unchanged.

## Recommended minimal fix (non-breaking)
- Add `energy_kwh` to `ProcessScheduledEvent`.
- Compute `energy_kwh` at schedule time and store in the event.
- Propagate `energy_kwh` into `ProcessRun` (when scheduled and when reconstructed in `load()`).
- Use `ProcessRun.energy_kwh` when logging `process_complete`.
- Do **not** modify `ProcessRun` field names or machine reservation structures.
- Do **not** add scheduled energy to `total_energy_kwh` during load if snapshots exist.

## Open questions for the author
1. Are recipe-step energy overrides currently supported in `start_process()` scheduling? If yes, how is the resolved model passed in?
2. Is `total_energy_kwh` ever incorrect after a reload with valid snapshots? If so, provide a reproduction to confirm the scope.
3. Should energy be recalculated for legacy logs without `energy_kwh` to improve backward compatibility?

## References
- `design/energy-tracking-persistence-fix.md`
- `docs/ADRs/021-simulation-state-persistence.md`
- `src/simulation/engine.py` (energy booking and completion logging)
- `src/simulation/scheduler.py` (ProcessRun structure)
