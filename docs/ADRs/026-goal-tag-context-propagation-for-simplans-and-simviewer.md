# 026: Goal/Tag Context Propagation for SimPlans and SimViewer Lanes

**Status:** Proposed  
**Date:** 2026-03-10  
**Decision Makers:** Project team  
**Related ADRs:** 020 (Recipe Orchestration and Scheduling), 021 (State Persistence), 022 (Simulation Runbooks)

## Context

The simulation stack now supports recipe orchestration and per-process lifecycle events, but
high-level planning intent (what machine/goal a recipe run belongs to) has been weakly represented.

Observed issues:

- SimPlan-level metadata tags were global and not specific to each recipe run.
- Combined plans lost source-machine provenance when many machine plans were merged.
- SimViewer could not reliably group recipe timeline lanes by high-level machine goals.
- Filtering by ad-hoc tags created brittle UX and did not solve lane attribution.

The required capability is:

1. A stable, extensible goal/tag envelope attached to recipe runs and inherited by process events.
2. Per-recipe tags that can encode machine goals.
3. SimViewer recipe lanes that prioritize machine-goal attribution from tags.

## Decision

Adopt a **goal_context envelope** propagated from SimPlan recipe submission through engine events,
with explicit `tags` and `tag_policies`, and use `goal.machine_id` as primary recipe-lane grouping
signal in SimViewer.

### 1) Canonical goal context shape

Goal context is a dictionary with these reserved fields:

- `goal_id`: stable identifier for current goal scope.
- `goal_type`: coarse goal category (for example, `scenario_target`, `machine_build`).
- `goal_target_item_id`: primary target item for this run scope.
- `tags`: arbitrary key/value tags (string/number/bool values).
- `tag_policies`: optional merge policies by key.

Recommended reserved tags:

- `goal.recipe_id`
- `goal.machine_id`

### 2) Propagation model

- SimPlan runner builds a base plan goal context from `plan.metadata`.
- For each `run_recipe(...)`, runner derives recipe-specific goal context:
  - merges plan tags with per-recipe metadata tags,
  - sets `goal.recipe_id`,
  - sets `goal_target_item_id` to recipe target,
  - sets `goal.machine_id` when recipe target is a machine.
- Engine stores goal context on recipe run state and propagates it to:
  - `process_scheduled`
  - `process_start`
  - `process_complete`
  - `recipe_start`
  - `recipe_complete`
- Snapshot persistence round-trips this context for scheduler/orchestrator state.

### 3) SimPlan per-recipe metadata

`PlanRecipe` includes optional `metadata`.

When duplicate recipe entries are merged, metadata is merged conservatively:

- non-conflicting keys are retained,
- `tags` are merged key-wise,
- conflicting tag values may be represented as a multi-value string (`a|b`) to avoid data loss.

### 4) Combined plan provenance

When multiple machine-target plans are merged into one combined SimPlan:

- each merged recipe entry is stamped with `tags.goal.machine_id=<source_machine_id>`,
- target recipes injected during merge are similarly tagged.

This preserves source-machine intent in a combined run.

### 5) SimViewer interpretation

Exporter includes `goal_context` on `process_runs`.

Recipe timeline laneing rule (priority order):

1. `goal_context.tags.goal.machine_id` (first value when multi-value string),
2. recipe target machine from KB (`target_item_id`),
3. recipe id fallback.

Timeline-level free-text goal-tag filtering is intentionally not part of this ADR decision.
Primary UX is lane attribution by machine goal.

## Consequences

### Positive

- Recipe runs can be grouped by high-level machine goals in combined simulations.
- Tag system remains extensible for future runbook/optimizer tagging use cases.
- Goal provenance survives through events, snapshots, and viewer export.

### Tradeoffs

- Tag consistency becomes a cross-layer contract (plan runner, engine, exporter, viewer).
- `a|b` merged tag representation is pragmatic but not strongly typed.
- Missing or incorrect `goal.machine_id` tags still fall back to heuristic laneing.

## Implementation Notes

Implemented across:

- `scripts/analysis/simplan.py` (per-recipe metadata support)
- `scripts/analysis/simplan_runner.py` (per-recipe goal context derivation)
- `scripts/analysis/simplan_build_combined.py` (source-machine tag stamping)
- `src/simulation/*` models/engine/scheduler/orchestrator/persistence (goal_context propagation)
- `src/simviewer/exporter.py` + `src/simviewer/models.py` (goal_context export)
- `apps/simviewer/src/App.tsx` (recipe lanes keyed by `goal.machine_id`)

## Validation

Minimum expected tests:

- SimPlan runner propagates plan tags into process scheduled events.
- SimPlan runner propagates per-recipe machine-goal tags distinctly per recipe.
- Engine recipe run propagates goal context to scheduled process events.
- SimViewer exporter includes goal context on process run records.

