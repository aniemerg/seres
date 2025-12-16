# Validation Report (v0)

## Counts by kind
- bom: 121
- machine: 129
- material: 104
- part: 450
- process: 177
- recipe: 642
- resource: 2
- resource_type: 43
- scenario: 1
- seed: 2
- unknown: 105

## Items without recipes (will be imports)
Total: 49 items need recipes or import designation
- machine: 9
- material: 10
- part: 30

See `out/missing_recipes.jsonl` for details.

## Missing required fields
Total: 10 missing fields
- bom: 10

See `out/missing_fields.jsonl` for details.

## Missing data (null values)
Total: 243 null fields
- bom: 31
- process: 212

See `out/null_values.jsonl` for details.

## Warnings
- kb/schema/version.yaml: unknown kind; skipped

## Work queue summary
Total gaps in work queue: see `out/work_queue.jsonl`