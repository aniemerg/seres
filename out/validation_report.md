# Validation Report (v0)

## Counts by kind
- bom: 470
- machine: 412
- material: 585
- part: 965
- process: 853
- recipe: 1961
- resource: 2
- scenario: 1
- schema: 1
- seed: 6
- unknown: 4

## Missing required fields
Total: 306 missing fields
- capabilities: 306

See `out/missing_fields.jsonl` for details.

## Missing recipe items
Total: 3 items referenced in recipes but not defined

### pure_intermediate (2 items)
- abrasive_mixture (used in 1 recipe(s))
- fired_ceramic_parts (used in 1 recipe(s))

### unused_recipe_output (1 items)
- volatiles_off_gas (used in 1 recipe(s))

See `out/missing_recipe_items.jsonl` for details.

## Missing data (null values)
Total: 7 null fields
- machine: 2
- part: 5

See `out/null_values.jsonl` for details.

## Validation Issues (ADR-017 and ADR-020)
Total: 2 validation issues found

By severity:
- error: 2

By category:
- item: 1
- semantic: 1

Top validation rules triggered:
- boundary_outputs_required: 1
- unit_missing: 1

See `out/validation_issues.jsonl` for details.

## Warnings
- kb/units/units.yaml: unknown kind; skipped

## Queue Filtering
**Status**: Enabled
**Mode**: boms_recipes_parts_only
**Total gaps found**: 324
**Filtered out**: 306
**Added to queue**: 18
**Filtering rate**: 94.4%

## Work queue summary
Total gaps in work queue: see `out/work_queue.jsonl`