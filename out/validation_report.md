# Validation Report (v0)

## Counts by kind
- bom: 291
- machine: 283
- material: 365
- part: 802
- process: 593
- recipe: 1344
- resource: 8
- resource_type: 88
- scenario: 1
- schema: 1
- seed: 6
- unknown: 123

## Items without recipes (will be imports)
Total: 319 items need recipes or import designation
- machine: 59
- material: 111
- part: 149

See `out/missing_recipes.jsonl` for details.

## Missing required fields
Total: 23 missing fields
- bom: 21
- capabilities: 2

See `out/missing_fields.jsonl` for details.

## Orphan resources (no machine provides)
Total: 16 resource_types have no provider machine
- 3d_printer_basic (needed by 3 processes)
- bending_machine (needed by 2 processes)
- chemical_reactor (needed by 8 processes)
- chemical_reactor_basic (needed by 4 processes)
- epoxy_synthesis_unit (needed by 1 processes)
- filtration_unit (needed by 1 processes)
- forging_press (needed by 1 processes)
- hip_press_unit (needed by 0 processes)
- lab_assistant (needed by 2 processes)
- labor_bot_electronics (needed by 3 processes)
- ... and 6 more

See `out/orphan_resources.jsonl` for details.

## Missing data (null values)
Total: 560 null fields
- bom: 60
- part: 2
- process: 498

See `out/null_values.jsonl` for details.

## Warnings
- kb/recipes/recipe_cooling_water_jacket_import_v0.yaml: failed to parse (mapping values are not allowed here
  in "kb/recipes/recipe_cooling_water_jacket_import_v0.yaml", line 6, column 11)

## Work queue summary
Total gaps in work queue: see `out/work_queue.jsonl`