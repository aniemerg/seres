# SERES Concurrent DES Runner Design (Non-Breaking)

## 1. Scope and Intent

This is a **concurrent DES runner** design, not OS/thread-level parallelism.

Goal:
- Improve utilization by submitting all work intents upfront and letting DES timing + resource conflicts resolve execution.
- Keep the current simulator stack stable and default.

Primary constraint:
- Do not break existing `sim` behavior, runbooks, or SimPlan workflows.

## 2. What We Reuse vs Add

### 2.1 Reuse Directly (no rewrite)

- `src/simulation/scheduler.py` (`Scheduler`, `EventQueue`, `EventType`)
- `src/simulation/machine_reservations.py` (`MachineReservationManager`)
- `src/simulation/dependency_graph.py`
- `src/simulation/recipe_orchestrator.py`
- Existing KB loader/validators/resolution logic

### 2.2 New Minimal Surface

- `src/simulation_parallel/intent_queue.py`
  - Deferred intent registry + per-machine waiting index.
- `src/simulation_parallel/runner.py`
  - Submit-all runner + `advance_to_completion()`.
- `src/simulation_parallel/reporting.py`
  - Utilization/bottleneck reporting from events.
- Optional:
  - `src/simulation_parallel/policy.py` (dispatch policy hooks).

No full duplicate engine/scheduler/reservation package.

## 3. Runtime Model

### 3.1 Submission Outcomes

Intent submission returns:
- `accepted`: immediately scheduled.
- `deferred`: valid but blocked by current machine/input contention.
- `rejected`: invalid definition / impossible requirements.

`deferred` is not a failure.

### 3.2 Deferred Intents

Deferred intents are stored:
- once in a global registry
- indexed by required machines for efficient promotion scans.

### 3.3 Promotion Trigger

Promotion is driven by DES events, not polling delay:
- on `PROCESS_COMPLETE`
- on `MACHINE_RELEASE` (partial reservation release)

At each trigger time, attempt promotion at the exact current sim time.

## 4. Promotion Algorithm (Concrete)

On a release-trigger event at `t`:

1. Identify machines whose availability changed.
2. Gather candidate deferred intents waiting on those machines.
3. Iterate candidates in deterministic policy order (default FIFO).
4. For each candidate intent:
   - Check all required machines reservable now.
   - Check required inputs available now.
   - If both true:
     - reserve machines,
     - schedule start at `t`,
     - remove from deferred registry/index.
   - Else keep deferred.
5. Repeat pass until no additional intents can be promoted at `t`.

Semantics:
- no partial commits
- no alternative process choice in v1
- deterministic under fixed policy

## 5. Inventory Atomicity and Contention

Inputs are consumed atomically at process start (existing model).

Implications:
- Deferred intents do not “hold” inputs while waiting.
- Competing intents are resolved by dispatch order at promotion time.
- Baseline policy is FIFO to ensure deterministic behavior.

Policy hooks can later support optimizer-controlled priorities.

## 6. `advance_to_completion()` Semantics

Runner-level helper using existing scheduler:

Loop until one terminal condition:

Success terminal:
- event queue empty
- active processes empty
- deferred intent registry empty

Blocked terminal:
- event queue empty
- active processes empty
- deferred intent registry non-empty
- no deferred intent promotable at current time

Safety fuse:
- no-progress iteration counter to prevent accidental infinite loops.

Output includes terminal status (`completed` or `blocked`) and blocked reasons.

## 7. Deadlock / Terminal Blocked Detection

Treat as blocked terminal if no events and no active work can change state, but deferred intents remain.

Report per deferred intent:
- missing machines / insufficient machine capacity
- insufficient inputs
- unsatisfiable process requirements

This enforces invariant:
- never silently end with unresolved active/deferred work.

## 8. Runner Pattern

New runner behavior:

1. Submit imports and recipe/process intents upfront.
2. Do not call phase-level `advance_until_idle` between submissions.
3. Call `advance_to_completion()` once.
4. Return result + event-derived reports.

Existing runners remain unchanged.

## 9. CLI Plan (Non-Breaking)

Add new namespace:
- `python -m src.cli sim2 ...`

Suggested commands:
- `sim2 init`
- `sim2 import`
- `sim2 submit-process`
- `sim2 submit-recipe`
- `sim2 run-to-completion`
- `sim2 status`
- `sim2 report-utilization`

`sim` commands remain untouched.

## 10. Migration Boundaries

Phase 1 does **not** support full mid-flight v1 snapshot import.

Supported initially:
- fresh runs
- optionally completed-state seeds

Unsupported in phase 1:
- importing v1 simulations with mid-execution active processes and partial elapsed durations.

If attempted, return explicit unsupported error.

## 11. Testing Strategy

### Unit
- intent defer/accept/reject transitions
- promotion correctness
- FIFO determinism
- terminal blocked detection

### Integration
- competing recipes on scarce machine
- independent recipes overlap in time
- partial reservation release triggers promotions

### Regression
- existing `src/simulation` tests remain green
- existing runbook/simplan paths unchanged

## 12. Risks and Mitigations

- Drift risk from duplicate core components
  - Mitigation: reuse v1 scheduler/reservations/orchestrator directly.
- Starvation under FIFO in edge workloads
  - Mitigation: policy abstraction; add fair/priority modes later.
- Hidden non-determinism in submission ordering
  - Mitigation: canonical ordering + explicit policy.

## 13. First Implementation Slice

Build minimum vertical slice:

1. `intent_queue.py` with deferred registry + machine index.
2. `runner.py` with submit-all + `advance_to_completion`.
3. Hook promotion on completion/release events using existing scheduler events.
4. `sim2` commands: `init`, `submit-process`, `run-to-completion`, `status`.
5. Basic utilization report from event log.

Then layer in recipe-intent convenience and optimizer integration.
