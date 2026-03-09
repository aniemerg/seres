# Quartz Piezo Sensor Fabrication Detailed Research Report

Date: 2026-03-04
Scope: `design/srm2_bom_research_results/06_quartz_piezo_sensor_fabrication.md`
Purpose: map quartz piezo fabrication content into concrete KB part/process/recipe updates.

## 1) Source extraction summary
Report 06 recommends a first-generation preloaded compression quartz puck architecture:
- quartz shaping + face preparation
- thin electrode formation
- insulated/preloaded mechanical stack
- calibration and acceptance test

## 2) Existing KB mapping
Reusable existing IDs:
- `quartz_crystal`
- `signal_amplifier_module`
- machines already present for support: `crystallization_unit_v0`, `polishing_station`, `signal_generator_analog_v0`

Gap:
- no explicit quartz piezo sensor part/process/recipe in KB

## 3) Recommended KB updates
- add part: `piezo_sensor_quartz_v0`
- add process: `quartz_piezo_sensor_fabrication_v0`
- add recipe: `recipe_piezo_sensor_quartz_v0`

## 4) Process design intent
`quartz_piezo_sensor_fabrication_v0` should represent:
- prepared quartz input
- metallization/stack assembly/calibration as one fabrication operation
- explicit machine requirements for polishing, assembly, and test/calibration support

## 5) Validation checklist
- `python -m src.cli validate --id process:quartz_piezo_sensor_fabrication_v0`
- `python -m src.cli validate --id item:piezo_sensor_quartz_v0`
- full index after applying 06 changes.

