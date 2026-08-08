# KB Schema Reference (Current)

This document is the authoritative, up-to-date summary of the KB schema and
modeling rules. It consolidates 012/013/014/016/017/027 for daily use.

## Items

### Deprecated/Upgraded IDs (ADR-025)

When an ID is upgraded, keep the deprecated entry in KB and annotate it (for
example with `deprecated`, `upgraded_to`, `upgrade_note`, `upgrade_since`).
Do not rely on silent aliasing for simulation behavior; deprecated references are
intended to fail fast at runtime so users/agents manually update references.

### Materials
Required:
- `id`, `name`, `kind: material`, `unit`, `unit_kind: bulk`, `notes`
Recommended:
- `density`, `state`, `composition`, `source_tags`
Optional:
- `is_scrap: true` to mark byproduct/offal materials that should not require recipes or closure expansion
Notes:
- Use `kind: material` for process-ready engineering materials, feedstocks,
  stock forms, powders, wires, ingots, slurries, intermediates, byproducts, and
  scrap.
- Do not use `kind: material` for natural/source-side lunar resources that still
  need beneficiation or extraction before becoming process materials. Use
  `kind: raw_material` instead.

### Raw Materials
Required:
- `id`, `name`, `kind: raw_material`, `unit`, `unit_kind: bulk`, `notes`
Recommended:
- `composition`, `source_tags`, site/provenance notes
Notes:
- Use `kind: raw_material` for natural, mined, collected, or otherwise primary
  source materials such as lunar regolith, ores, feldspar source minerals,
  meteorite source material, or volatile-bearing regolith.
- Raw materials belong under `content/kb/items/raw_materials/`.
- A material produced by a recipe from raw material, such as `regolith_powder`,
  `ilmenite_concentrate`, `alumina_powder`, `ceramic_powder`, or stock metal,
  is a `material`, not a `raw_material`.
- Imported ore/source placeholders may still be `raw_material` if the item is
  semantically an ore/source rather than an engineering material. Mark the supply
  boundary with `is_import: true`.

### Resources
Required:
- `id`, `name`, `kind: resource`, `unit`, `unit_kind: bulk`, `notes`
Notes:
- Use `kind: resource` for non-material process inputs/outputs such as energy,
  heat, solar radiation/irradiance, data-like resources, or environmental fluxes.
- Resources belong under `content/kb/items/resources/`.

### Monolithic Parts
Required:
- `id`, `name`, `kind: monolithic_part`, `unit`, `unit_kind: discrete`,
  `mass_kg` (mass per unit), `notes`
Recommended:
- `material`, `dimensions`, `source_tags`
Compatibility:
- Existing `kind: part` entries remain valid. New content should use
  `monolithic_part` for a single-piece item or `assembly_part` for an item with
  child components.
- `material` names what a part is made from. Existing `material_class` remains
  readable during migration, but should not be treated as proof that two
  materials are interchangeable.

### Assembly Parts
Required:
- `id`, `name`, `kind: assembly_part`, `unit`, `unit_kind: discrete`, `mass_kg`
  (mass per unit), `notes`
Recommended:
- `bom`, `source_tags`, `performance_requirements`
Notes:
- `assembly_part` means the item is semantically made from multiple child
  pieces, not that the KB has already decomposed it. It may appear as a leaf in
  a recursive BOM tree when its child BOM has not been modeled yet.
- Do not put a single `material` or `material_class` on assemblies. An
  assembly's material makeup is represented by its BOM components.
- A BOM component is a relationship role, not an item kind. Machines,
  assemblies, monolithic parts, and materials can all appear as BOM components.

### Machines
Required:
- `id`, `name`, `kind: machine`, `unit`, `unit_kind: discrete`, `mass_kg` (mass per unit), `notes`
Recommended:
- `bom`, `capabilities`, `power_draw_kW`, `source_tags`
Notes:
- Do not put `material` or `material_class` on machines. A machine's material
  makeup is represented by its BOM components.

### Shared Optional Item Fields

For monolithic parts, assemblies, and machines, `mass_kg` remains the nominal
mass used for count <-> mass conversion. When mass is uncertain or
scale-dependent, add:

```yaml
mass_low_kg: 0.5
mass_high_kg: 2.0
```

The range is an uncertainty bracket for review, substitution, and difficulty
estimation. It is not a replacement for `mass_kg`, and should be omitted when no
useful bound is known.

Use `performance_requirements` for critical characteristics that affect
substitution, manufacturing route selection, or simulation fidelity. Values
must be controlled term IDs from
`config/performance_requirement_vocabulary.yaml`; do not put requirement
sentences, alternatives, target values, or `review_required` placeholders in
this field. Include only categories that are relevant to the part:

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

This block identifies which characteristics are critical; it does not state a
numeric acceptance target or prove that a process can achieve it. Quantitative
targets require a separate, source-backed representation. Leave unrelated
categories absent instead of adding nulls or generic quality statements. See
ADR-027 for the rationale.

Use `trust_tags` when an item needs explicit trust/audit status:

```yaml
trust_tags:
- untrusted_global_kb
```

Trust tags are project-policy annotations. They do not by themselves prove or
invalidate manufacturability.

Use `future_improvements` for known modeling gaps that should not be mixed into
general notes. Keep `notes` for current assumptions/rationale; put backlog items
such as missing part-specific tooling, unresolved mass bounds, missing material
selection, route blockers, or required future decomposition here:

```yaml
future_improvements:
- Add part-specific punch/die tooling before treating stamping as locally closed.
- Replace coarse item specification with explicit material, geometry/interface
  requirements, and lower/upper mass bounds.
```

This field is advisory metadata. It does not change simulation routing or prove
manufacturing closure unless the referenced BOMs, recipes, processes, and
resource requirements are also updated.

## Processes

Required:
- `id`, `name`, `kind: process`
- `process_type: continuous | batch`
- `inputs`, `outputs`
- `time_model` (required by 012)
- `energy_model` (required by 014)

Optional:
- `is_template: true` for generic processes where recipes define concrete
  inputs/outputs. Validation skips undefined item references for template
  processes. Template processes may omit inputs/outputs; recipes must supply
  them explicitly. Use sparingly and prefer real items when possible.

### Time Model (012)

Continuous:
```yaml
process_type: continuous
time_model:
  type: linear_rate
  rate: 10.0
  rate_unit: kg/hr
  scaling_basis: input_item_id
```

Batch:
```yaml
process_type: batch
time_model:
  type: batch
  setup_hr: 0.1
  hr_per_batch: 0.9
```

### Energy Model (014)

Per-unit:
```yaml
energy_model:
  type: per_unit
  value: 0.3
  unit: kWh/kg
  scaling_basis: input_item_id
```

Fixed per batch:
```yaml
energy_model:
  type: fixed_per_batch
  value: 120.0
  unit: kWh
```

### Resource Requirements

Use explicit machines in `resource_requirements`:
```yaml
resource_requirements:
  - machine_id: labor_bot_general_v0
    qty: 2.0
    unit: hr
```
Machines are not consumable inputs. Do not list reusable machines in
`inputs`/`outputs`; put them in `resource_requirements` so the simulator treats
them as capacity requirements rather than materials.

## Recipes

Required:
- `id`, `target_item_id`, `variant_id`, `steps`

Steps reference processes and may include overrides:
```yaml
steps:
  - process_id: crushing_basic_v0
    time_model:
      rate: 50.0  # Partial override (type omitted)
```

Override rules (013):
- If `time_model.type` or `energy_model.type` is provided in a step, it is a
  complete override and must include all required fields.
- If `type` is omitted, the step partially overrides the process model.

Recipe-level `inputs`/`outputs` may be used to bind quantities for generic
processes (see `docs/closure_error_guidance.md`).

## Units and Conversions (016)

- Compound units use `numerator/denominator` (e.g., `kg/hr`, `kWh/kg`).
- Unit conversion is implicit where supported and validated.
- Conversions may require `density` (mass <-> volume) or `mass_kg` (count <-> mass).
- Discrete items use `unit` with `mass_kg` as mass per unit; bulk items use
  continuous units (typically `kg`).

## Validation (017)

Validation runs at index time and produces queue items for errors. Common errors:
- Missing `process_type`
- Deprecated time/energy fields
- Missing `scaling_basis` or invalid compound units
- Unit conversion not possible

Validate specific entries:
```bash
python -m src.cli validate --id process:crushing_basic_v0
```

## Boundary Processes

Use boundary models for terminal nodes:
```yaml
energy_model:
  type: boundary
time_model:
  type: boundary
```

Common boundaries:
- `environment_source_v0` (for in-situ resource collection)
- For imports: Use `is_import: true` on items (per ADR-007), not a process

## References

- `docs/ADRs/012-process-types-and-time-model.md`
- `docs/ADRs/013-recipe-override-mechanics.md`
- `docs/ADRs/014-energy-model-redesign.md`
- `docs/ADRs/016-unit-conversion-system.md`
- `docs/ADRs/017-validation-and-error-detection.md`
- `docs/ADRs/025-deprecated-id-enforcement-and-manual-migration.md`
