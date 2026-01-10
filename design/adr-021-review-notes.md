# ADR-021 review notes for author

## Purpose
This memo consolidates review concerns about ADR-021 (Simulation State Persistence and Reconstruction) and its alignment with ADR-020. It focuses on state loss across CLI commands and design improvements to prevent it.

## Executive summary
ADR-021 identifies the correct persistence gap, but the proposed design risks new state-loss and semantic drift unless it aligns with ADR-020’s lifecycle events and adds stronger reconstruction rules (especially for partial reservations and recipes). The CLI-first workflow requires more than active-process persistence to avoid losing orchestration state between commands.

## Critical alignment issues with ADR-020
1. Event semantics mismatch
   - ADR-020 defines a three-state lifecycle with distinct `process_scheduled`, `process_start`, and `process_complete` events.
   - ADR-021 proposes logging a `process_start` event at schedule time and reusing it to rebuild scheduler state. This collapses the lifecycle and makes “start” ambiguous once scheduled processes exist.
   - Recommendation: introduce an explicit `process_scheduled` event and log `process_start` only at actual activation. If you cannot introduce a new event immediately, add `scheduled_start` and `actual_start` fields and document precedence.

2. Partial reservation reconstruction is incorrect after reload
   - ADR-021 reconstructs machine reservations using `end_time=end_time` for all reservations, then schedules a partial release in the future.
   - If the simulation is loaded after `release_time`, the partial reservation should already be released, but the reconstruction retains it until `end_time`.
   - Recommendation: for `reservation_type == PARTIAL`, use `release_time` as the reservation end time and skip restoring it if `release_time <= current_time`.

3. Machine reservation schema loses fidelity
   - ADR-021 stores `machines_reserved` as a dict keyed by `machine_id` with a single reservation payload.
   - This loses information if the same machine has multiple reservation segments or both full-duration and partial reservations.
   - Recommendation: store a list of reservations per process run, each with `machine_id`, `start_time`, `end_time`, `qty`, `unit`, and `reservation_type`.

## State-loss risks across CLI commands
1. Recipe orchestration persistence is explicitly deferred
   - ADR-021 Phase 1 only restores active processes; scheduled steps and recipe state are lost between CLI commands.
   - If the goal is “no state loss between CLI commands,” recipe state must persist at least minimally.
   - Recommendation: add minimal persistence for recipe runs and scheduled steps, even if full dependency graph reconstruction is deferred.

2. Event fields omit unit fidelity for materials
   - `inputs_consumed` and `outputs_pending` are defined as `Dict[str, float]` with no units.
   - If ADR-016 conversions are used or inventory supports multiple units, reloads may misinterpret quantities.
   - Recommendation: persist material quantities with explicit units or serialize `InventoryItem` payloads.

## Reconstruction robustness gaps
1. Duplicate event logging and event ordering
   - ADR-021 removes duplicate `process_start` logging from `advance_time`, but does not define how to resolve discrepancies between scheduled start and activation time.
   - Recommendation: keep separate events for scheduling and activation, and reconstruct scheduler state from scheduling while reconstructing “active” state based on activation events and current time.

2. Field consistency checks
   - `ends_at` is redundant with `start_time + duration_hours`, but no validation is defined for mismatches.
   - Recommendation: treat `ends_at` as derived; log errors or reconcile on load if inconsistent.

## Suggested ADR-021 improvements (minimal changes)
1. Add `process_scheduled` event and restore scheduler state from it.
2. Keep `process_start` for activation only; include `actual_start_time` in event.
3. Persist reservations as a list with explicit `start_time/end_time` per reservation.
4. Restore partial reservations using `release_time` and skip expired ones at load.
5. Add minimal recipe persistence: `recipe_run` event + step state events for scheduled/active/completed steps.
6. Include units in `inputs_consumed` and `outputs_pending`.
7. Add load-time validation that reconciles `ends_at` vs `start_time + duration_hours`.

## Notes on CLI-first workflow
- The CLI flow implies frequent save/load cycles between commands, so persistence must handle “in-flight” scheduled processes and blocked steps, not just active processes.
- A daemon is not required if event logs are sufficiently expressive to reconstruct scheduler state reliably.

## Open questions for the author
1. Should ADR-021 explicitly align event types with ADR-020 to avoid semantic drift?
2. Is recipe persistence intentionally deferred despite CLI-first requirements, or should a minimal version be included in Phase 1?
3. Are inventory quantities strictly canonical units? If not, how should units be persisted?
4. Should reconstruction treat scheduled steps separately from active processes to avoid falsely marking not-yet-started steps as active?

## References
- ADR-020: Recipe Orchestration and Scheduling
- ADR-021: Simulation State Persistence and Reconstruction
