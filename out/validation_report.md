# Validation Report (v0)

## Counts by kind
- bom: 101
- machine: 110
- material: 89
- part: 378
- process: 139
- recipe: 503
- resource: 2
- resource_type: 40
- scenario: 1
- unknown: 153

## Items without recipes (will be imports)
Total: 80 items need recipes or import designation
- machine: 16
- material: 18
- part: 46

See `out/missing_recipes.jsonl` for details.

## Missing data (null values)
Total: 236 null fields
- bom: 25
- process: 211

See `out/null_values.jsonl` for details.

## Warnings
- kb/schema/version.yaml: unknown kind; skipped

## Work queue summary
Total gaps in work queue: see `out/work_queue.jsonl`