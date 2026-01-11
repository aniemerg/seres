# ADR 001 — Dedupe Initiative (Tool/Process Consolidation)

**Status:** Proposed  
**Date:** 2024-XX-XX  
**Owner:** kb/ops
**Update 2026-01-11:** References updated to `src/` equivalents; dedupe CLI is not yet implemented in `src/`.

## Context / Problem
- The current KB keeps adding machines/processes/recipes, causing fan-out and a growing core replication graph.
- Goal: shrink the “default/minimal” self-replicating toolchain by preferring fewer, more adaptable tools (e.g., additive, manual/labor) while keeping all data (no deletions).
- Need a repeatable workflow (queue + annotations) to propose, review, and apply consolidations without losing provenance or breaking existing files.

## Decision / Direction
- Introduce a **dedupe workflow** (separate queue) to surface and evaluate consolidation candidates (processes, machines, parts, recipes).
- Add **annotations** to items/processes/recipes to record alternatives and preferences without deleting anything.
- Support **recipe variants** (e.g., `simple`, `additive`, `precision`) with a default variant hint; keep parallel paths but prefer the simplest in the minimal graph.
- Encode **heuristics** for flexible tech (3D printing, labor/manual assembly) to be used aggressively for long-tail/small/medium-complexity parts; avoid massive/simple-plate items by default.
- Log **precedents/decisions** in a dedicated doc; items can carry `alternatives`/`dedupe_candidate` flags for local context.

## Planned Data/Schema Additions (to implement in follow-up)
- Items/Processes/Recipes (now supported in schema):
  - `alternatives`: list of preferred IDs + rationale (why prefer X over Y).
  - `dedupe_candidate`: boolean (flag for review).
  - `preferred_variant`: recipe variant ID to treat as the default/simple path.
- Recipes:
  - Multiple `variant_id`s allowed (e.g., `simple`, `additive`, `precision`); keep current schema but document the convention.
- (Future) Optional `graph_class` is deferred until we have a maintainable minimal set.

## Dedupe Queue (new, separate)
- File: `out/dedupe_queue.jsonl`
- Entries (draft): `{id, kind: process|machine|item|recipe, reason, candidate_ids[], status, lease_id, lease_expires_at, notes, hints, refs, category}`
- CLI (mirror existing queue semantics): pending in `src/` (no current CLI).
- Seeding: manual/agent review of `out/reports/inventory.md` and other reports; no auto-population in v0.

## Heuristics / Guidance (document-only for now)
- Prefer **flexible tools**: 3D printing for small/medium parts; use material-appropriate printers. Avoid very large items by default; simple items are fine if additive is still reasonable.
- Prefer **labor/manual** for long-tail/low-volume items; specialized tools only when items are common/high-volume or labor is unreasonable.
- Candidate triggers: overlapping capabilities, low usage frequency, availability of a more general substitute, or explicit similarity.
- Never delete items; instead, retarget recipes/BOMs to preferred tools and mark alternatives on the deprecated ones.

## Documentation / Logging
- Create `docs/dedupe_decisions.md` to log decisions (item(s), decision, rationale, date/agent).
- Update README/docs to describe the dedupe queue and annotations once implemented.

## Implementation Plan (phased)
1) **Docs & Conventions** (this ADR): establish fields, queue concept, heuristics, logging approach.
2) **Queue Infrastructure**: add `dedupe` CLI mirroring the work-queue commands; persist to `out/dedupe_queue.jsonl`; no auto-seeding.
3) **Schema/Model Updates**: add support for `alternatives`, `dedupe_candidate`, `preferred_variant`; document recipe variant conventions.
4) **Reporting Support**: (optional) extend `report inventory` to include overlap signals to aid manual seeding.
5) **Seeding & Execution**: agents scan `out/reports/inventory.md`, add dedupe tasks, process them, retarget recipes/BOMs to preferred tools, and record decisions in `docs/dedupe_decisions.md` and item notes/alternatives.

## Out of Scope (for now)
- Automatic selection of minimal graph.
- Automated de-dupe task generation.
- Enforcing aggressive additive/labor substitution in code (documented heuristic only).
