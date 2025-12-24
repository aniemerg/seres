# Validation Report (v0)

## Counts by kind
- bom: 403
- item: 1
- machine: 344
- material: 505
- part: 991
- process: 891
- recipe: 2037
- resource: 2
- scenario: 1
- schema: 1
- seed: 6

## Missing required fields
Total: 248 missing fields
- capabilities: 248

See `out/missing_fields.jsonl` for details.

## Missing data (null values)
Total: 916 null fields
- bom: 89
- process: 827

See `out/null_values.jsonl` for details.

## Warnings
- kb/units/units.yaml: unknown kind; skipped

## Queue Filtering
**Status**: Enabled
**Mode**: boms_recipes_parts_only
**Total gaps found**: 254
**Filtered out**: 248
**Added to queue**: 6
**Filtering rate**: 97.6%

## Work queue summary
Total gaps in work queue: see `out/work_queue.jsonl`