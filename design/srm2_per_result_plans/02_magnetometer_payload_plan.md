# 02 Magnetometer Payload - KB Integration Plan

Detailed basis:
- `design/srm2_per_result_plans/02_magnetometer_payload_detailed_research_report.md`

## Scope
- Rover-mounted vector magnetometer payload, first-generation dual-head boom architecture.

## Current KB mapping
After result 01 implementation, the following now exist and are reused:
- `fluxgate_sensor_head_v0`
- `magnetometer_afe_adc_board_v0`
- `magnetometer_calibration_set_v0`
- `magnetometer_boom_module_v0`
- `magnetometer_station_calibration_v0`

## Decision
- Add explicit standalone payload machine representation and dedicated survey process.
- Keep internals reusable as part-level chain (already implemented).

## Proposed KB deltas (result 02 execution)
- Add machine: `magnetometer_payload_v0`
- Add BOM: `bom_magnetometer_payload_v0`
- Add recipe: `recipe_magnetometer_payload_v0`
- Add material artifact: `magnetic_anomaly_map_v0`
- Add process: `magnetic_anomaly_survey_v0`
- Keep `prospecting_module_v0` integration path from result 01.

## Machine requirements for operations
- `kapvik_microrover_v0`
- `magnetometer_payload_v0`

## Key risks / open issues
- Magnetic cleanliness constraints remain note/policy-level metadata rather than hard schema.
- Exact anomaly-threshold logic belongs in simulation policy, not BOM-level modeling.
