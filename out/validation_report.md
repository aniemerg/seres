# Validation Report (v0)

## Counts by kind
- bom: 21
- machine: 18
- material: 30
- part: 62
- process: 27
- recipe: 110
- resource_type: 44
- scenario: 1

## Orphan resources (no machine provides)
Total: 26 resource_types have no provider machine
- assembly_tools_basic (needed by 1 processes)
- carbon_feed_system (needed by 1 processes)
- controlled_cooling (needed by 1 processes)
- crucible (needed by 1 processes)
- cutting_tools_general (needed by 2 processes)
- dies (needed by 1 processes)
- dust_control (needed by 2 processes)
- electrodes (needed by 1 processes)
- fiber_spinneret (needed by 1 processes)
- filler_material (needed by 1 processes)
- ... and 16 more

See `out/orphan_resources.jsonl` for details.

## Missing data (null values)
Total: 54 null fields
- process: 54

See `out/null_values.jsonl` for details.

## Warnings
- kb/schema/version.yaml: unknown kind; skipped

## Work queue summary
Total gaps in work queue: see `out/work_queue.jsonl`