# 025: Deprecated/Upgraded ID Enforcement with Manual Migration

**Status:** Proposed
**Date:** 2026-03-03
**Decision Makers:** Project team
**Related ADRs:** 003 (Process-Machine Refactor), 017 (Validation), 018 (Recipe I/O), 019 (BOM/Recipe), 021 (State Persistence)

## Context

The KB evolves over time. IDs for items/processes/recipes may need to be upgraded
for clarity, correctness, or schema consistency. Today:

- Backward-compat behavior exists in several places.
- There is no canonical lifecycle policy for deprecated IDs.
- Simulation behavior is inconsistent when older IDs are encountered.

For simulation correctness and user trust, deprecated references must not run
silently. The user requirement for this ADR is explicit:

1. Keep upgraded/deprecated IDs visible in KB files for readability.
2. Stop simulation when deprecated IDs are used.
3. Force manual investigation and update by users/agents (no automatic rewrite tool).

## Decision

Adopt a strict fail-fast ID lifecycle policy.

### 1) Deprecated IDs remain in KB as explicit records

Deprecated entities remain as KB entries and declare upgrade metadata in-file,
rather than being removed or auto-rewritten externally.

Recommended metadata fields on deprecated entries:

```yaml
deprecated: true
upgraded_to:
  - <new_id>
upgrade_note: "Why this ID was upgraded and how to choose replacement."
upgrade_since: "2026-03-03"
```

Notes:
- `upgraded_to` may contain multiple IDs when a split occurred.
- Keeping these records in KB preserves readability and intent.

### 2) Simulator hard-stop on deprecated ID usage

Simulation must fail immediately (before state mutation) when deprecated IDs are
encountered in:

- process start (`start_process`)
- recipe start (`run_recipe`)
- imports (`import_item`)
- recipe step resolution (`process_id` references)
- loaded simulation state containing deprecated process/item references

Failure must include a structured payload with:
- deprecated ID
- replacement candidate(s) (`upgraded_to`)
- upgrade note
- where it was referenced (entity + field path)

### 3) No automatic migration tool

The system will not auto-rewrite scenarios/snapshots/recipes from old IDs to new
IDs. Users/agents must investigate and make intentional updates.

Rationale:
- Prevents silent semantic drift.
- Forces explicit review when one old ID maps to multiple new IDs.
- Keeps model evolution auditable.

## Enforcement Model

### Runtime (hard enforcement)

- Raise deterministic error on deprecated ID detection.
- Abort command with clear operator-facing guidance.
- Do not proceed with inventory/process scheduling on failure.

### Validation/Indexing (preventive enforcement)

- Add validation rule(s) for references to `deprecated: true` entities.
- Severity should be `ERROR` for active process/recipe references.
- Validation output should mirror runtime guidance.

## Data Model Guidance

This ADR does not require an immediate strict schema migration for the metadata
fields. Existing permissive raw models (`extra=allow`) can carry these fields.
If/when formalized later, these fields can be promoted to validated models.

## Consequences

### Positive

- No silent use of stale IDs in simulations.
- KB stays readable with in-file upgrade history.
- Operators get explicit, contextual remediation guidance.

### Negative

- Existing scenarios may fail until references are updated.
- Additional validation/runtime checks add implementation work.

### Neutral

- Multiple replacement candidates remain a human decision point by design.

## Implementation Plan

1. Add deprecated-ID metadata to relevant KB entries as they are upgraded.
2. Add simulator guard methods and call sites for all entry points and loaded state.
3. Add validator rule(s) to flag references to deprecated entities.
4. Add operator-facing error format and documentation snippet in simulation guide.
5. Add tests:
   - start process with deprecated ID -> fails
   - run recipe with deprecated step process ID -> fails
   - import deprecated item ID -> fails
   - load snapshot with deprecated in-flight/process refs -> fails

## Out of Scope

- Automatic migration scripts for scenarios or saved simulations.
- Silent compatibility aliases that continue execution.
