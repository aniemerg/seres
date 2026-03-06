# 07 Wheatstone Bridge Module - KB Integration Plan

Detailed basis:
- `design/srm2_per_result_plans/07_wheatstone_bridge_module_detailed_research_report.md`

## Scope in report
- A reusable bridge module for resistive sensors/load-cell style instrumentation.

## Current KB mapping
- Existing nearby parts/processes:
  - `load_cell_strain_gauge_v0`
  - `signal_amplifier_module`
  - `potentiometer_wirewound_v0`
  - `sensor_wired_assembly`
- No dedicated `wheatstone_bridge_module` item currently found.

## Decision
- `new` part is justified as reusable instrumentation building block.
- Reuse existing resistive sensor parts and generic assembly process where possible.

## Proposed KB deltas
- Add part: `wheatstone_bridge_module_v0`
- Add process: `wheatstone_bridge_module_assembly_v0`
- Add recipe: `recipe_wheatstone_bridge_module_v0`
- Optional updates:
  - add this module as explicit input in `recipe_wheel_load_cell_system_v0` if beneficial

## Machine requirements for new process
- `assembly_station`
- Optional calibration/test dependency:
  - `signal_generator_analog_v0`

## Key risks / open issues
- Keep module generic enough to avoid one-module-per-sensor proliferation.
- Determine whether module should be represented as a physical board only, or board + trim/calibration state.
