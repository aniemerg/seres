# Validation Report (v0)

## Counts by kind
- bom: 470
- machine: 412
- material: 584
- part: 966
- process: 853
- recipe: 1951
- resource: 2
- scenario: 1
- schema: 1
- seed: 6
- unknown: 1

## Missing required fields
Total: 306 missing fields
- capabilities: 306

See `out/missing_fields.jsonl` for details.

## Missing data (null values)
Total: 2 null fields
- machine: 2

See `out/null_values.jsonl` for details.

## Validation Issues (ADR-017 and ADR-020)
Total: 1 validation issues found

By severity:
- error: 1

By category:
- item: 1

Top validation rules triggered:
- unit_missing: 1

See `out/validation_issues.jsonl` for details.

## Warnings
- kb/units/units.yaml: unknown kind; skipped

## Queue Filtering
**Status**: Enabled
**Mode**: boms_recipes_parts_only
**Total gaps found**: 311
**Filtered out**: 306
**Added to queue**: 5
**Filtering rate**: 98.4%

## Work queue summary
Total gaps in work queue: see `out/work_queue.jsonl`