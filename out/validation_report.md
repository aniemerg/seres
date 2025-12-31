# Validation Report (v0)

## Counts by kind
- bom: 398
- item: 1
- machine: 341
- material: 572
- part: 1008
- process: 872
- recipe: 1996
- resource: 2
- scenario: 1
- schema: 1
- seed: 6

## Items without recipes (will be imports)
Total: 1 items need recipes or import designation
- material: 1

See `out/missing_recipes.jsonl` for details.

## Missing required fields
Total: 246 missing fields
- capabilities: 246

See `out/missing_fields.jsonl` for details.

## Missing data (null values)
Total: 906 null fields
- part: 10
- process: 896

See `out/null_values.jsonl` for details.

## Validation Issues (ADR-017)
Total: 52 validation issues found

By severity:
- error: 51
- warning: 1

By category:
- recipe: 50
- reference: 1
- semantic: 1

Top validation rules triggered:
- recipe_inputs_not_resolvable: 48
- recipe_outputs_not_resolvable: 2
- boundary_machine_missing: 1
- process_not_found: 1

See `out/validation_issues.jsonl` for details.

## Warnings
- kb/units/units.yaml: unknown kind; skipped

## Queue Filtering
**Status**: Enabled
**Mode**: boms_recipes_parts_only
**Total gaps found**: 299
**Filtered out**: 246
**Added to queue**: 53
**Filtering rate**: 82.3%

## Work queue summary
Total gaps in work queue: see `out/work_queue.jsonl`