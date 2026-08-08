# 027: Item Performance Requirements and Mass Estimate Ranges

**Status:** Proposed
**Date:** 2026-07-23
**Decision Makers:** Project team
**Related ADRs:** 016 (Unit Conversion), 017 (Validation), 019 (BOM/Recipe), 023 (Material Provenance)

## Context

The KB originally treated item mass mostly as a single value (`mass_kg`) and
captured performance-sensitive requirements in free-text notes. That is usable
for simple inventory accounting, but it becomes weak when the model is used to
estimate lunar self-replication feasibility.

The project needs to answer several distinct questions:

1. Whether a lunar self-replication industrial chain can exist.
2. Whether a proposed design is a lower-difficulty path.
3. How much mass must be imported or manufactured.
4. How much energy and time lunar manufacturing requires.
5. Whether an existing KB item can stand in for a newly modeled item without
   hiding critical technical requirements.

Single-point mass and prose-only performance notes are not enough for those
questions. Many item masses are provisional estimates derived from analogies,
catalog parts, rough geometry, or incomplete decomposition. Likewise, two items
with similar names and similar mass may not be interchangeable if one requires a
vacuum seal, precision bearing fit, optical/electron-beam alignment, or a
specific surface finish.

The earlier "within roughly 5x mass" reuse rule remains useful as a conservative
first-pass inventory heuristic, but it is not sufficient as a replacement rule
for precision, vacuum, electrical, or high-performance machine parts. A lower
mass or simpler BOM is only meaningful when the resulting item can still perform
the required function.

## Decision

Add optional item-level fields for mass uncertainty and performance-sensitive
requirements. These fields are general KB schema features, not EBF3-specific
metadata.

### 1) Mass estimate range

For discrete parts and machines:

```yaml
mass_kg: 1.0
mass_low_kg: 0.5
mass_high_kg: 2.0
```

Rules:

- `mass_kg` remains the nominal mass used for count <-> mass conversion.
- `mass_low_kg` and `mass_high_kg` are optional review bounds.
- If all three fields are present, the nominal `mass_kg` should normally fall
  inside the low/high interval.
- The interval represents a defensible engineering bracket, not a statistical
  confidence interval.
- Do not add placeholder nulls. Omit the range when there is no useful bound.
- Notes should explain the basis when the range is non-obvious, for example
  catalog analogy, area * wall thickness * density, length * cross-section *
  density, or power/rating scale.

Why:

- Feasibility estimates should not pretend provisional masses are exact.
- Reuse review needs to know whether a candidate item is plausibly within the
  modeled scale, not merely whether its nominal value happens to be close.
- Difficulty estimates can later use low/nominal/high scenarios without changing
  the item identity.
- This avoids encoding uncertainty in ad-hoc fields such as `mass_confidence`
  when the actionable information is the bracket itself.

### 2) Performance requirements

For parts and machines whose manufacturability or substitution depends on
function-level requirements:

```yaml
performance_requirements:
  geometrical_tolerances:
    form:
    - circularity
    runout:
    - circular_runout
  surface_integrity:
    surface_texture:
    - surface_roughness
  material_properties:
    mechanical:
    - hardness
    - fatigue_strength
```

Rules:

- `performance_requirements` is optional.
- Populate only characteristics that are critical to the item's role.
- Use only category, subgroup, and term IDs defined in
  `config/performance_requirement_vocabulary.yaml`.
- Leave unrelated categories absent instead of adding nulls or generic quality
  requirements.
- Do not store prose sentences, alternatives, numeric targets, or
  `review_required` placeholders in this field.
- A listed term means that the characteristic matters; it does not claim that a
  manufacturing route achieves it.
- Quantitative targets require a separate source-backed representation before
  they can support process-capability closure.

Why:

- Material and process choice depends on required performance, not only item
  name or mass.
- Existing item reuse must not hide precision, sealing, alignment, electrical,
  vacuum, or surface requirements.
- Structured requirements make it easier to audit when a general item is good
  enough and when a dedicated item must remain separate.
- Manufacturing simulations need to distinguish "can produce roughly the same
  shape" from "can produce the required functional surface/interface."

## Interpretation

These fields support review and simulation fidelity. They do not by themselves
prove that an item can be manufactured locally.

Approval to reuse an existing item should require:

- same functional role,
- compatible unit kind or explicit quantity normalization,
- candidate mass inside or defensibly near the target mass range,
- compatible material and process assumptions,
- enough performance requirements exposed to avoid hiding critical difficulty.

If those checks are not met, the existing item may still be useful as a coarse
proxy or material/process hint, but it should not count as local-closure evidence
until the hidden assumptions are modeled.

## Consequences

### Positive

- Keeps uncertainty explicit without multiplying item IDs.
- Separates nominal simulation mass from engineering uncertainty.
- Makes high-precision and vacuum-sensitive reuse decisions auditable.
- Helps compare lower-difficulty design options without lowering technical
  fidelity.
- Provides a natural place to migrate important requirements currently buried in
  item notes.

### Tradeoffs

- Adds optional fields that reviewers must learn to interpret consistently.
- Some characteristics will remain qualitative IDs until stronger sources
  support quantitative acceptance targets.
- Validation can initially only check field shape and obvious mass ordering; it
  cannot judge whether a tolerance or leak-rate target is technically correct.

### Non-goals

- This ADR does not require filling these fields for every item.
- This ADR does not require decomposing every assembly before assigning a mass
  range.
- This ADR does not replace recipes, process requirements, or material
  provenance.
- This ADR does not make lower-resolution proxy items acceptable for high-fidelity
  simulation unless the performance requirements are also compatible.

## Implementation Notes

Initial implementation:

- Add `mass_low_kg`, `mass_high_kg`, and `performance_requirements` to raw and
  validated item schema models.
- Document the fields in the KB schema reference.
- Use generated review matrices to surface missing requirements before bulk YAML
  edits.

Validation checks:

- reject `mass_low_kg > mass_high_kg` and negative or non-numeric bounds,
- warn when `mass_kg` is outside the declared low/high range,
- reject malformed `performance_requirements` and unknown controlled term IDs.

Existing content without these optional fields remains valid. Content migration
is intentionally separate from parser and validator support.

## Validation

Minimum expected checks after implementation:

- Schema parsing accepts items with `mass_low_kg`, `mass_high_kg`, and
  `performance_requirements`.
- Existing items without these optional fields continue to validate.
- Targeted item validation still passes for existing machine items.
