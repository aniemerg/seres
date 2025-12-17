# Validation Report (v0)

## Counts by kind
- bom: 157
- machine: 167
- material: 116
- part: 500
- process: 213
- recipe: 741
- resource: 2
- resource_type: 61
- scenario: 1
- seed: 4
- unknown: 594

## Items without recipes (will be imports)
Total: 61 items need recipes or import designation
- machine: 24
- material: 10
- part: 27

See `out/missing_recipes.jsonl` for details.

## Missing required fields
Total: 10 missing fields
- bom: 9
- capabilities: 1

See `out/missing_fields.jsonl` for details.

## Missing data (null values)
Total: 294 null fields
- bom: 60
- process: 234

See `out/null_values.jsonl` for details.

## Warnings
- kb/schema/version.yaml: unknown kind; skipped

## Work queue summary
Total gaps in work queue: see `out/work_queue.jsonl`