# ADR 024 — Universal Waste Sink

**Status:** Proposed  
**Date:** 2026-01-25  
**Decision Makers:** Project team  
**Related ADRs:** 016 (Unit Conversion), 017 (Validation), 018 (Recipe I/O), 019 (BOM/Recipe)

## Context

Mass-balance validation exposes many cases where recipes need to account for
offcuts, machining losses, and assembly scrap. Creating a new scrap item for
every material stream is noisy and increases KB complexity. We already have
infrastructure for terminal byproducts via `is_scrap: true`, but no universal
item to use as a generic sink.

We also need to avoid “fixing” mass balance by changing discrete outputs to
`kg` or by using fractional discrete counts.

## Decision

Introduce a **universal `waste` item** as a generic mass sink:

1. **`waste` is a material** (bulk, `unit: kg`, `unit_kind: bulk`).
2. **`waste` is terminal** (`is_scrap: true`), so it is excluded from closure
   analysis and `no_recipe` work queue items.
3. **`waste` may appear in step outputs/byproducts only**, not in recipe-level
   outputs.
4. **Provenance/ISRU reports ignore `waste`** (not counted in overall ISRU or
   per-item breakdowns).

## Rationale

- Keeps the KB tractable by avoiding proliferation of scrap items.
- Provides a conservative, explicit mass sink for loss accounting.
- Preserves discrete item integrity (no fractional unit workarounds).
- Aligns with existing `is_scrap` terminal behavior.

## Implementation

### KB
- Add `kb/items/materials/waste.yaml`:
  - `id: waste`, `kind: material`, `unit: kg`, `unit_kind: bulk`,
    `material_class: waste`, `is_scrap: true`.

### Validation
- Add rule: **recipe outputs must not include `waste`**.
  - Allowed in step outputs or step byproducts only.

### Simulation / Provenance
- Exclude `is_scrap: true` items from provenance totals and per-item output.

## Consequences

- Recipes can close mass balance by emitting `waste` at step level.
- Closure and ISRU statistics remain focused on productive mass.
- Future material-specific scrap streams can be added as `is_scrap: true`
  without changing this decision.

## Open Questions

None for initial rollout. If desired later, add optional typed scrap streams
for detailed recycling/reuse modeling.
