# Validation Report (v0)

## Counts by kind
- bom: 403
- item: 1
- machine: 344
- material: 490
- part: 981
- process: 877
- recipe: 2010
- resource: 2
- scenario: 1
- schema: 1
- seed: 6
- unknown: 6

## Items without recipes (will be imports)
Total: 2 items need recipes or import designation
- material: 2

See `out/missing_recipes.jsonl` for details.

## Missing required fields
Total: 248 missing fields
- capabilities: 248

See `out/missing_fields.jsonl` for details.

## Recipes with no inputs
Total: 1877 recipes have steps but no inputs defined
- recipe_basalt_fiber_v0 (target: basalt_fiber, 3 step(s))
- recipe_carbon_reductant_v0 (target: carbon_reductant, 3 step(s))
- recipe_cast_metal_parts_v0 (target: cast_metal_parts, 3 step(s))
- crushing_jaw_set_v0 (target: None, 1 step(s))
- recipe_cutting_tool_set_basic_v0 (target: cutting_tool_set_basic, 3 step(s))
- recipe_electrical_energy_v0 (target: electrical_energy, 3 step(s))
- recipe_glass_bulk_v0 (target: glass_bulk, 1 step(s))
- recipe_ilmenite_concentrate_v0 (target: ilmenite_concentrate, 1 step(s))
- recipe_iron_product_v0 (target: iron_product, 1 step(s))
- recipe_lunar_regolith_in_situ_v0 (target: lunar_regolith_in_situ, 1 step(s))
- ... and 1867 more

See `out/recipes_no_inputs.jsonl` for details.

## Missing data (null values)
Total: 1019 null fields
- bom: 89
- process: 930

See `out/null_values.jsonl` for details.

## Circular Dependencies
Total: 22 circular dependency loops detected

By type:
- default: 7
- self_reference: 15

Sample loops:
- [default] copper_scrap_v0 → copper_rod_ingot → copper_scrap_v0
- [default] sodium_chloride → salt_contingency_nacl → hydrochloric_acid → chlorine_gas → sodium_chloride
- [default] sodium_chloride → salt_contingency_nacl → hydrochloric_acid → hydrogen_gas → sodium_chloride
- [default] sodium_chloride → salt_contingency_nacl → sodium_hydroxide → sodium_chloride
- [self_reference] nitrogen_gas → nitrogen_gas
- ... and 17 more

See `out/circular_dependencies.jsonl` for details.

## Warnings
- kb/units/units.yaml: unknown kind; skipped

## Queue Filtering
**Status**: Enabled
**Mode**: boms_recipes_parts_only
**Total gaps found**: 2155
**Filtered out**: 248
**Added to queue**: 1907
**Filtering rate**: 11.5%

## Work queue summary
Total gaps in work queue: see `out/work_queue.jsonl`