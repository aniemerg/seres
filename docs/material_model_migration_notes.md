# Material Model Migration Notes

## Problem

The current KB uses `material_class` on many items and parts. This mixes two
different concepts:

- the actual material an item is made from
- whether that material can substitute for another material

That shortcut was useful for early generic substitution experiments, but it is
too vague for higher-fidelity part review. Values such as `metal`, `steel`,
`composite`, `electronic`, and `ceramic` are not consistently the same kind of
thing: sometimes they mean a real material family, sometimes a functional
category, and sometimes a substitution bucket.

## Preferred Direction

Use `material` on the item/part itself to describe what it is actually made
from.

Example:

```yaml
id: vacuum_chamber_bracket_v0
kind: monolithic_part
material: stainless_steel
```

Handle substitution separately through a canonical material list and explicit
material groups.

Example material entry:

```yaml
id: stainless_steel
name: Stainless steel
aliases:
  - corrosion_resistant_steel
family: ferrous_alloy
properties:
  density_kg_m3: 8000
```

Example substitution group:

```yaml
id: structural_steel_group
members:
  - carbon_steel
  - stainless_steel
  - tool_steel
allowed_for:
  - frames
  - brackets
  - housings
not_allowed_for:
  - cathodes
  - precision_electrodes
  - electrical_conductors
```

## Rationale

`material` should answer: what is this item made from?

Substitution groups should answer: what can replace what, under which use
context?

Keeping those separate makes the KB easier to audit. It also avoids pretending
that broad classes such as `metal` are safe substitutes everywhere.

## Migration Plan

1. Add `material` as a supported item field in the schema.
2. Create a canonical material list, likely under
   `content/kb/items/materials/` or another dedicated directory.
3. Create explicit material substitution groups, with context limits.
4. Change validators so parts prefer `material` while accepting legacy
   `material_class` during migration.
5. Remove `material_class` from current KB item files.
6. Migrate old KB parts from `material_class` to reviewed `material` values.
7. Update simulation/indexer substitution logic to use material groups instead
   of item-level `material_class`.
8. Keep parser fallback only as compatibility for older external data, not as a
   field agents should write.

## Important Caution

Do not mechanically rename every `material_class` to `material` without review.
Many existing values are broad classes or functional buckets, not real material
names. For example:

- `metal` should usually become a reviewed material such as `carbon_steel`,
  `stainless_steel`, `aluminum`, or `copper`.
- `electronic` is not a material; it likely needs a part category, not a
  material.
- `composite` may need a specific composite system or a temporary unknown
  material marker.

## Current State

Engine-side support has started:

- `docs/kb_schema_reference.md` documents `part.material` as preferred.
- `src/kb_core/schema.py` supports `material` on raw and strict item models.
- `src/indexer/indexer.py` accepts either `material` or legacy
  `material_class` while content repositories migrate independently.
- No engine commit should claim that a separately versioned content repository
  has completed migration. That must be established against its exact content
  commit.
