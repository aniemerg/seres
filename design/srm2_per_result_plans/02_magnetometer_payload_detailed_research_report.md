# Magnetometer Payload Detailed Research Report

Date: 2026-03-04
Scope: `design/srm2_bom_research_results/02_magnetometer_payload.md`
Purpose: provide citation-grade decomposition for magnetometer payload KB entries.

## 1) Re-read extraction summary
The source report specifies:
- DC to low-frequency vector sensing (about 0-10 Hz).
- Dual-sensor fluxgate gradiometer as first-generation preferred architecture.
- Sensor spacing (about 0.5-1.0 m) and station-mode operation as contamination control.
- Required subsystems:
  - field sensing heads
  - low-noise AFE + ADC
  - thermal/dust robustness
  - magnetic cleanliness constraints
  - calibration and compensation workflow
- Operations should include traverse-mode trend mapping and station-mode gating-quality data.

## 2) Existing KB coverage from result 01
Already implemented and reusable:
- `fluxgate_sensor_head_v0`
- `magnetometer_afe_adc_board_v0`
- `magnetometer_calibration_set_v0`
- `magnetometer_boom_module_v0`
- `magnetometer_station_calibration_v0` process
- Prospecting stack integration through `prospecting_module_v0`

Gap remaining for result 02:
- explicit standalone magnetometer payload machine representation
- dedicated anomaly-survey process output artifact

## 3) Recommended KB structure for result 02
### Payload machine layer
- `magnetometer_payload_v0` (machine)
- `bom_magnetometer_payload_v0`
- `recipe_magnetometer_payload_v0`

### Operation layer
- `magnetic_anomaly_survey_v0` process
- output artifact material `magnetic_anomaly_map_v0`

### Why this split
- Keeps build complexity in recipes.
- Keeps operational usage in process entries.
- Allows use both as standalone rover payload and as submodule within broader `prospecting_module_v0`.

## 4) Detailed payload BOM (first-generation)
1. `magnetometer_boom_module_v0` - deployable dual-head sensor geometry
2. `magnetometer_afe_adc_board_v0` - low-noise interface and digitization
3. `magnetometer_calibration_set_v0` - calibration coil and thermal reference support
4. `coaxial_cable_low_loss` - shielded signal wiring path
5. `connector_electrical_multi_pin` - serviceable rover interface
6. `prospecting_mount_frame_v0` - non-magnetic mount frame / alignment base
7. `fastener_kit_small` - assembly hardware

## 5) Operations and data products
### Station-mode anomaly survey (`magnetic_anomaly_survey_v0`)
- Inputs: local regolith sample context mass token
- Outputs:
  - `magnetic_anomaly_map_v0` (primary)
  - optional characterized regolith stream for downstream routing
- Resource requirements:
  - `kapvik_microrover_v0`
  - `magnetometer_payload_v0`
- Batch-style process with fixed-duration acquisition to reflect "stop-and-sense" use.

## 6) Semiconductor exception boundary
Allowed imported leaves:
- ADC ICs
- precision analog ICs
- specialized magnetic sensing IC internals

Not import-only by default:
- boom/mount structure
- harness and connectors
- housings and brackets
- payload-level integration

## 7) Validation targets
After implementing 02 payload machine/process:
- `python -m src.cli validate --id item:magnetometer_payload_v0`
- `python -m src.cli validate --id process:magnetic_anomaly_survey_v0`
- full index should not introduce new validation errors.
