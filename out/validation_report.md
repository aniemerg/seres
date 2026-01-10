# Validation Report (v0)

## Counts by kind
- bom: 408
- machine: 420
- material: 581
- part: 957
- process: 847
- recipe: 1943
- resource: 2
- scenario: 1
- schema: 1
- seed: 6

## Items without recipes (will be imports)
Total: 1 items need recipes or import designation
- machine: 1

See `out/missing_recipes.jsonl` for details.

## Missing required fields
Total: 410 missing fields
- bom: 77
- capabilities: 333

See `out/missing_fields.jsonl` for details.

## Missing data (null values)
Total: 3 null fields
- machine: 3

See `out/null_values.jsonl` for details.

## Warnings
- kb/units/units.yaml: unknown kind; skipped

## Queue Filtering
**Status**: Enabled
**Mode**: boms_recipes_parts_only
**Total gaps found**: 491
**Filtered out**: 333
**Added to queue**: 158
**Filtering rate**: 67.8%

## Work queue summary
Total gaps in work queue: see `out/work_queue.jsonl`