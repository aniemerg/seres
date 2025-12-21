# Validation Report (v0)

## Counts by kind
- bom: 296
- machine: 291
- material: 370
- part: 808
- process: 607
- recipe: 1372
- resource: 9
- resource_type: 88
- scenario: 1
- schema: 1
- seed: 6
- unknown: 114

## Items without recipes (will be imports)
Total: 311 items need recipes or import designation
- machine: 58
- material: 111
- part: 142

See `out/missing_recipes.jsonl` for details.

## Missing required fields
Total: 336 missing fields
- bom: 17
- capabilities: 319

See `out/missing_fields.jsonl` for details.

## Orphan resources (no machine provides)
Total: 87 resource_types have no provider machine
- 3d_printer_basic (needed by 2 processes)
- assembly_tools_basic (needed by 33 processes)
- bending_machine (needed by 0 processes)
- chemical_mixing (needed by 1 processes)
- chemical_reactor_basic (needed by 1 processes)
- core_memory_assembly (needed by 0 processes)
- cpu_core (needed by 0 processes)
- cryogenic_chiller_v0 (needed by 0 processes)
- cutting_tools_general (needed by 12 processes)
- electrolysis_cell (needed by 0 processes)
- ... and 77 more

See `out/orphan_resources.jsonl` for details.

## Missing data (null values)
Total: 773 null fields
- bom: 60
- part: 2
- process: 711

See `out/null_values.jsonl` for details.

## Warnings
- kb/recipes/recipe_cooling_water_jacket_import_v0.yaml: failed to parse (mapping values are not allowed here
  in "kb/recipes/recipe_cooling_water_jacket_import_v0.yaml", line 6, column 11)
- kb/units/units.yaml: unknown kind; skipped

## Queue Filtering
**Status**: Enabled
**Mode**: boms_recipes_parts_only
**Total gaps found**: 1059
**Filtered out**: 406
**Added to queue**: 653
**Filtering rate**: 38.3%

## Work queue summary
Total gaps in work queue: see `out/work_queue.jsonl`