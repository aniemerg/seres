# Material Model and Legacy Material Class

**Status**: Legacy note

## Current Rule

New KB item files should prefer `material` when naming what a part is made
from. Existing content that uses `material_class` remains supported during
migration.

- Parts use `material` for what the part is actually made from.
- Machines do not carry material fields; their material makeup comes from BOM
  components.
- Material items are themselves materials; describe them with fields such as
  `composition`, `state`, `density`, source notes, and future material-group
  metadata.

## Substitution

Automatic material substitution is currently disabled in the simulation engine.
Recipe inputs must match exact item IDs.

Future substitution should be modeled with explicit material groups that state
which materials can substitute for which use contexts. Do not encode
substitution by putting broad buckets such as `metal`, `electronic`, or
`composite` into item-level `material_class`.

## Historical Context

Earlier versions used `material_class` to connect generic flows, such as
allowing one regolith item to satisfy a process that requested another regolith
item. That shortcut mixed item identity with substitution rules and made part
audits ambiguous. It is kept here only as historical context for older notes and
archived experiments. Each independently versioned content repository can
migrate after its own review.
