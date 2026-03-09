# 03 Electrostatic Separator Machine - KB Integration Plan

Detailed basis:
- `design/srm2_per_result_plans/03_electrostatic_separator_machine_detailed_research_report.md`

## Scope in report
- Tribocharging + parallel-plate electrostatic separator machine for dry lunar beneficiation.
- Positioned after comminution/sizing and often after magnetic separation.

## Current KB mapping
- Existing separators: `magnetic_separator`, `magnetic_separator_drum_v0`, `gravity_separator`, `centrifugal_separator_v0`
- Existing HV-related part: `hv_rectifier_stack_v0`
- No electrostatic beneficiation machine currently present.

## Decision
- `new` machine family is justified (distinct physics, HV safety, feed conditioning).
- Reuse existing separator/HV/feed subsystems where practical.

## Proposed KB deltas
- Add machine: `electrostatic_separator_v0`
- Add BOM: `bom_electrostatic_separator_v0`
- Add recipe: `recipe_machine_electrostatic_separator_v0`
- Add key parts:
  - `tribocharger_module_v0`
  - `separator_plate_electrode_set_v0`
  - `hv_supply_module_30kv_v0`
  - `sealed_bin_carousel_v0`
- Add recipes for each new part:
  - `recipe_tribocharger_module_v0`
  - `recipe_separator_plate_electrode_set_v0`
  - `recipe_hv_supply_module_30kv_v0`
  - `recipe_sealed_bin_carousel_v0`

## Machine requirements for downstream process use
- New processes using electrostatic separation should require:
  - `electrostatic_separator_v0`
  - upstream feed prep machine(s) (existing): crusher/screener and optional magnetic separator

## Machine/BOM composition direction
- reuse in final machine BOM:
  - `separator_frame`
  - `vibratory_feeder_v0`
  - `hopper_feed_system`
  - `hv_enclosure_and_interlocks`
  - `sensor_suite_general`
  - `control_compute_module_imported`
  - `fastener_kit_medium`
- new submodules in final machine BOM:
  - `tribocharger_module_v0`
  - `separator_plate_electrode_set_v0`
  - `hv_supply_module_30kv_v0`
  - `sealed_bin_carousel_v0`

## Key risks / open issues
- HV safety interlocks may require explicit process preconditions.
- Need conservative throughput assumptions to avoid false production capacity.
- Keep local-build-first for structural/feed/HV-integration chain; avoid import-only machine placeholder.
