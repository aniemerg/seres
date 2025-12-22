# Validation Report (v0)

## Counts by kind
- bom: 402
- item: 1
- machine: 367
- material: 436
- part: 928
- process: 858
- recipe: 1871
- resource: 2
- scenario: 1
- schema: 1
- seed: 6
- unknown: 388

## Items without recipes (will be imports)
Total: 60 items need recipes or import designation
- machine: 53
- material: 5
- part: 2

See `out/missing_recipes.jsonl` for details.

## Missing required fields
Total: 277 missing fields
- capabilities: 277

See `out/missing_fields.jsonl` for details.

## Missing data (null values)
Total: 973 null fields
- bom: 62
- process: 911

See `out/null_values.jsonl` for details.

## Warnings
- kb/units/units.yaml: unknown kind; skipped

## Queue Filtering
**Status**: Enabled
**Mode**: boms_recipes_parts_only
**Total gaps found**: 762
**Filtered out**: 277
**Added to queue**: 485
**Filtering rate**: 36.4%

## Work queue summary
Total gaps in work queue: see `out/work_queue.jsonl`