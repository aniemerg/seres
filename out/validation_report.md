# Validation Report (v0)

## Counts by kind
- bom: 398
- item: 1
- machine: 341
- material: 566
- part: 1006
- process: 847
- recipe: 1931
- resource: 2
- scenario: 1
- schema: 1
- seed: 6

## Missing required fields
Total: 246 missing fields
- capabilities: 246

See `out/missing_fields.jsonl` for details.

## Missing data (null values)
Total: 897 null fields
- part: 10
- process: 887

See `out/null_values.jsonl` for details.

## Circular Dependencies
Total: 1 circular dependency loops detected

By type:
- self_reference: 1

Sample loops:
- [self_reference] electrical_energy → electrical_energy

See `out/circular_dependencies.jsonl` for details.

## Validation Issues (ADR-017)
Total: 4609 validation issues found

By severity:
- error: 4609

By category:
- recipe: 4607
- semantic: 2

Top validation rules triggered:
- recipe_template_missing_step_inputs: 2954
- recipe_step_input_not_satisfied: 1653
- scaling_basis_not_found: 2

See `out/validation_issues.jsonl` for details.

## Warnings
- kb/units/units.yaml: unknown kind; skipped

## Work queue summary
Total gaps in work queue: see `out/work_queue.jsonl`