# Validation Report (v0)

## Counts by kind
- bom: 398
- item: 1
- machine: 341
- material: 538
- part: 984
- process: 871
- recipe: 1962
- resource: 2
- scenario: 1
- schema: 1
- seed: 6
- unknown: 26

## Missing required fields
Total: 247 missing fields
- capabilities: 246
- energy_model: 1

See `out/missing_fields.jsonl` for details.

## Missing recipe items
Total: 24 items referenced in recipes but not defined

### missing_recipe_target (24 items)
- air_bearing_assembly_local (used in 1 recipe(s))
- analog_test_bench_neural (used in 1 recipe(s))
- ball_screw_assembly_import (used in 1 recipe(s))
- carbon_anode_from_material (used in 1 recipe(s))
- carbon_anode_material_from_methane (used in 1 recipe(s))
- carbon_reducing_agent_import (used in 1 recipe(s))
- chemical_bath_tank_set_import (used in 1 recipe(s))
- chloralkali_gas (used in 1 recipe(s))
- cleaning_station (used in 1 recipe(s))
- crimping_tool_set_import (used in 1 recipe(s))
- ... and 14 more

See `out/missing_recipe_items.jsonl` for details.

## Missing data (null values)
Total: 829 null fields
- process: 829

See `out/null_values.jsonl` for details.

## Validation Issues (ADR-017)
Total: 1506 validation issues found

By severity:
- error: 1506

By category:
- schema: 1504
- semantic: 2

Top validation rules triggered:
- process_type_required: 622
- required_field_missing: 510
- energy_model_type_invalid: 239
- deprecated_field: 133
- non_positive_value: 2

See `out/validation_issues.jsonl` for details.

## Warnings
- kb/units/units.yaml: unknown kind; skipped

## Queue Filtering
**Status**: Enabled
**Mode**: boms_recipes_parts_only
**Total gaps found**: 1803
**Filtered out**: 246
**Added to queue**: 1557
**Filtering rate**: 13.6%

## Work queue summary
Total gaps in work queue: see `out/work_queue.jsonl`