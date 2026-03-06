# 06 Quartz Piezo Sensor Fabrication - KB Integration Plan

Detailed basis:
- `design/srm2_per_result_plans/06_quartz_piezo_sensor_fabrication_detailed_research_report.md`

## Scope in report
- Fabrication chain for quartz-based piezo sensing element/module.

## Current KB mapping
- Existing quartz chain:
  - `quartz_crystal` + `quartz_crystal_synthesis_v0`
- Existing sensor assembly infrastructure:
  - `sensor_element_with_gauges`, `sensor_wired_assembly`
  - `signal_amplifier_module`
- No explicit quartz piezo sensor item/process.

## Decision
- `new` sensor part with strong reuse of existing quartz and sensor assembly chains.

## Proposed KB deltas
- Add part: `piezo_sensor_quartz_v0`
- Add process: `quartz_piezo_sensor_fabrication_v0`
- Add recipe: `recipe_piezo_sensor_quartz_v0`
- Optional higher-level module:
  - `piezo_sensor_module_v0` if packaging/electronics are modeled separately

## Machine requirements for new process
- `crystallization_unit_v0` (existing quartz growth context)
- `assembly_station`
- Optional finishing/calibration:
  - `polishing_station`
  - `signal_generator_analog_v0` (if modeled as calibration machine dependency)

## Key risks / open issues
- Need conservative assumptions on electrode deposition and packaging method.
- Keep electronics abstraction aligned with existing sensor module patterns.
