# KB Schema Reference (Current)

This document is the authoritative, up-to-date summary of the KB schema and
modeling rules. It consolidates ADR-012/013/014/016/017 for daily use.

## Items

### Materials
Required:
- `id`, `name`, `kind: material`, `unit`, `notes`
Recommended:
- `material_class`, `density`, `state`, `composition`, `source_tags`

### Parts
Required:
- `id`, `name`, `kind: part`, `mass`, `material_class`, `notes`
Recommended:
- `dimensions`, `source_tags`

### Machines
Required:
- `id`, `name`, `kind: machine`, `mass`, `notes`
Recommended:
- `bom`, `capabilities`, `power_draw_kW`, `source_tags`

## Processes

Required:
- `id`, `name`, `kind: process`
- `process_type: continuous | batch`
- `inputs`, `outputs`
- `time_model` (required by ADR-012)
- `energy_model` (required by ADR-014)

### Time Model (ADR-012)

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

### Energy Model (ADR-014)

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

Override rules (ADR-013):
- If `time_model.type` or `energy_model.type` is provided in a step, it is a
  complete override and must include all required fields.
- If `type` is omitted, the step partially overrides the process model.

Recipe-level `inputs`/`outputs` may be used to bind quantities for generic
processes (see `docs/closure_error_guidance.md`).

## Units and Conversions (ADR-016)

- Compound units use `numerator/denominator` (e.g., `kg/hr`, `kWh/kg`).
- Unit conversion is implicit where supported and validated.
- Conversions may require `density` (mass <-> volume) or `mass` (count <-> mass).

## Validation (ADR-017)

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
- `environment_source_v0`
- `import_placeholder_v0`

## References

- `docs/ADRs/ADR-012-process-types-and-time-model.md`
- `docs/ADRs/ADR-013-recipe-override-mechanics.md`
- `docs/ADRs/ADR-014-energy-model-redesign.md`
- `docs/ADRs/ADR-016-unit-conversion-system.md`
- `docs/ADRs/ADR-017-validation-and-error-detection.md`
