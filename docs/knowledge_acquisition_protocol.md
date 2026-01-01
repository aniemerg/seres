# Knowledge Acquisition Protocol (Current)

This protocol replaces the older memo-based workflow. It keeps extraction
structured, conservative, and compatible with the current schema.

## Goals

- Extract structure before precision.
- Preserve provenance and uncertainty.
- Keep the KB runnable even with gaps.
- Avoid uncontrolled growth through reuse and consolidation.

## Core Principles

- Processes before machines.
- Use existing items whenever reasonable (see `docs/conservative_mode_guide.md`).
- Unknowns are explicit, not hidden.
- Model what matters first (top mass/energy/time contributors).

## Source Extraction Workflow

Use three passes per source:

1) Process skeletons
- List process modules (IDs + 1-sentence description).
- List materials, consumables, and implied equipment.

2) Coarse quantification
- Throughput ranges, energy intensity ranges, batch vs continuous.
- Provide provenance tags for each numeric field.

3) Closure and gaps
- Identify missing upstream processes and missing items.
- Capture undefined consumables or equipment.

## Schema Compatibility Rules

- All new processes must use 012 time_model and 014 energy_model.
- Use flexible units and scaling_basis as required by 012/014/016.
- Recipe overrides follow 013 (complete override if `type` is set).
- Validation is authoritative (017).

## Provenance and Uncertainty

For any estimate, add notes such as:
- `source_tags: [ai_estimate]`
- `notes: "Estimate based on similar process; within 5x."`

Avoid nulls when a conservative estimate is reasonable.

## When to Stop and Import

Prefer imports when:
- The item is not a top contributor to mass/energy/time.
- Modeling effort is high relative to impact.
- The item is outside current capability scope.

Mark items with `is_import: true` (per ADR-007). Import items don't need recipes.

## Consolidation and Reuse

Before creating anything new:
- Search for equivalents by function and material_class.
- Apply the 5x magnitude rule.
- Prefer labor bots + tools over bespoke machines for low-throughput tasks.

## Output Expectations

Each extraction yields:
- YAML deltas for processes/items/recipes.
- A short assumptions list with provenance.
- A gap list for follow-up queue items.

## References

- `docs/kb_schema_reference.md`
- `docs/conservative_mode_guide.md`
- `docs/parts_and_labor_guidelines.md`
