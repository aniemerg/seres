# Validation Report (v0)

## Counts by kind
- bom: 389
- machine: 317
- material: 435
- part: 933
- process: 804
- recipe: 1891
- resource: 14
- resource_type: 103
- scenario: 1
- schema: 1
- seed: 6
- unknown: 54

## Items without recipes (will be imports)
Total: 17 items need recipes or import designation
- machine: 2
- material: 3
- part: 12

See `out/missing_recipes.jsonl` for details.

## Missing required fields
Total: 253 missing fields
- capabilities: 253

See `out/missing_fields.jsonl` for details.

## Orphan resources (no machine provides)
Total: 98 resource_types have no provider machine
- 3d_printer_basic (needed by 2 processes)
- assembly_station (needed by 56 processes)
- assembly_tools_basic (needed by 38 processes)
- battery_formation (needed by 1 processes)
- bearing_grinding_machine_v0 (needed by 4 processes)
- bending_machine (needed by 0 processes)
- chemical_mixing (needed by 2 processes)
- chemical_reactor_basic (needed by 2 processes)
- core_memory_assembly (needed by 0 processes)
- cpu_core (needed by 0 processes)
- ... and 88 more

See `out/orphan_resources.jsonl` for details.

## Missing data (null values)
Total: 919 null fields
- bom: 62
- process: 857

See `out/null_values.jsonl` for details.

## Warnings
- kb/units/units.yaml: unknown kind; skipped

## Queue Filtering
**Status**: Enabled
**Mode**: boms_recipes_parts_only
**Total gaps found**: 480
**Filtered out**: 351
**Added to queue**: 129
**Filtering rate**: 73.1%

## Work queue summary
Total gaps in work queue: see `out/work_queue.jsonl`