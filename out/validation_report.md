# Validation Report (v0)

## Counts by kind
- bom: 403
- item: 1
- machine: 344
- material: 493
- part: 980
- process: 877
- recipe: 2012
- resource: 2
- scenario: 1
- schema: 1
- seed: 6
- unknown: 1

## Items without recipes (will be imports)
Total: 1 items need recipes or import designation
- part: 1

See `out/missing_recipes.jsonl` for details.

## Missing required fields
Total: 248 missing fields
- capabilities: 248

See `out/missing_fields.jsonl` for details.

## Missing data (null values)
Total: 1015 null fields
- bom: 89
- process: 926

See `out/null_values.jsonl` for details.

## Circular Dependencies
Total: 8 circular dependency loops detected

By type:
- default: 7
- self_reference: 1

Sample loops:
- [default] hydrogen_gas → sodium_chloride → salt_contingency_nacl → hydrochloric_acid → hydrogen_gas
- [default] sodium_chloride → salt_contingency_nacl → hydrochloric_acid → chlorine_gas → sodium_chloride
- [default] sodium_chloride → salt_contingency_nacl → sodium_hydroxide → sodium_chloride
- [default] copper_scrap_v0 → copper_rod_ingot → copper_scrap_v0
- [default] epoxy_precursor_block_v0 → epoxy_monomer_v0 → epoxy_precursor_block_v0
- ... and 3 more

See `out/circular_dependencies.jsonl` for details.

## Warnings
- kb/units/units.yaml: unknown kind; skipped

## Queue Filtering
**Status**: Enabled
**Mode**: boms_recipes_parts_only
**Total gaps found**: 548
**Filtered out**: 248
**Added to queue**: 300
**Filtering rate**: 45.3%

## Work queue summary
Total gaps in work queue: see `out/work_queue.jsonl`