# Validation Report (v0)

## Counts by kind
- bom: 398
- item: 1
- machine: 341
- material: 538
- part: 984
- process: 870
- recipe: 1962
- resource: 2
- scenario: 1
- schema: 1
- seed: 6

## Missing required fields
Total: 246 missing fields
- capabilities: 246

See `out/missing_fields.jsonl` for details.

## Missing data (null values)
Total: 829 null fields
- process: 829

See `out/null_values.jsonl` for details.

## Warnings
- kb/units/units.yaml: unknown kind; skipped

## Queue Filtering
**Status**: Enabled
**Mode**: boms_recipes_parts_only
**Total gaps found**: 246
**Filtered out**: 246
**Added to queue**: 0
**Filtering rate**: 100.0%

## Work queue summary
Total gaps in work queue: see `out/work_queue.jsonl`