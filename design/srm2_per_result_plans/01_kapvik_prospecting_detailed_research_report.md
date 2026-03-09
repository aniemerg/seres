# Kapvik + Prospecting Module Detailed Research Report

Date: 2026-03-03
Scope: result files `01_prospecting_module.md` and `02_magnetometer_payload.md`
Purpose: citation-grade technical basis for detailed KB updates (machines, parts, BOMs, recipes, processes)

## 1) Evidence Re-Read Summary (what must drive KB design)
Primary report details extracted:
- First-generation architecture is modular "Option A": magnetometer boom + spectral head + shallow sampler + penetrometer/thermal probe.
- Strong emphasis on LRUs, field maintenance, dust resilience, and calibration workflow.
- Mechanical interface assumptions are explicit: kinematic hard-mount, quick-disconnect behavior, deployable boom.
- Magnetometer report recommends dual-sensor fluxgate gradiometer on non-magnetic boom, baseline about 0.5-1.0 m, with station-mode acquisition.

Secondary Kapvik inferred-BOM details extracted:
- Mobility stack evidence points to six wheel modules (not four) with motor + planetary + high-ratio gear stage + encoder.
- Named reference components include motor/gear/controller/sensor families, plus rover mast/arm context.
- Power bus and rover payload capacity are uncertain in public data; KB should encode assumptions in notes and avoid hard-coded design claims beyond sourced evidence.

## 2) Policy Constraints for This Result
- No placeholder-only modeling for rover/prospecting architecture.
- No import-only defaults except semiconductor-level leaves.
- Recipes should represent multi-step construction chains; processes should represent executable operations.
- Existing rover entries are in-scope for full normalization, not just additive modules.

## 3) Canonical ID and Naming Direction
The current machine ID `kapvik_microrover_30kg_v0` should be superseded because the size suffix is not needed.

Recommended canonical machine ID:
- `kapvik_microrover_v0`

Compatibility strategy:
- Keep `kapvik_microrover_30kg_v0` as deprecated alias entry (per repo deprecated-ID policy) with pointer to `kapvik_microrover_v0`.
- Do not silently rewrite downstream recipes; force explicit migration through validator/simulator deprecation checks.

## 4) Existing KB State vs Required Fidelity
Key mismatches found now:
- Kapvik recipe is effectively monolithic single-step assembly.
- Kapvik BOM uses 4 wheels while suspension and wheel notes point to 6-wheel rocker-bogie pattern.
- Kapvik BOM omits existing rover subassemblies (`rover_chassis_structure_v0`, `rover_suspension_rocker_bogie_v0`).
- Rover avionics is import-marked and not decomposed into major assemblies.
- Prospecting capability is split across weakly-coupled placeholders (`gamma_ray_spectrometer_v0`, `nife_meteorite_magnetic_detection_v0`) without integrated rover module chain.

## 5) Target System Decomposition (authoritative for KB implementation)
### A. Rover Base Platform
- Chassis and structural interfaces
- Suspension and wheel modules
- Power generation and storage
- Avionics and motion control
- Communications and localization sensors

### B. Prospecting Payload System
- Mechanical payload interface
- Magnetometer boom subsystem
- Spectral/context sensing subsystem
- Shallow sampling and geotechnical subsystem
- Harnessing, conditioning, dust/thermal protection

### C. Operations Layer
- Prospecting site qualification process
- Traverse-mode and station-mode measurement operations
- Calibration and periodic health-check operations

## 6) Detailed BOM Plan by Major Assembly
Legend:
- `Existing`: currently in KB and reusable
- `Upgrade`: exists but needs non-placeholder decomposition
- `New`: should be added as concrete part/assembly

### 6.1 Kapvik Chassis Assembly
Target assembly ID:
- `rover_chassis_structure_v1` (or migrate existing `rover_chassis_structure_v0` in place)

| Sub-assembly | Candidate KB ID(s) | Status | Notes |
|---|---|---|---|
| Main frame rails/tubes | `aluminum_tube_stock_v0`, `aluminum_sheet_2mm` | Existing | Replace high-mass coarse assumptions with cut/welded frame bill |
| Crossmembers + deck panels | `aluminum_sheet_2mm` | Existing | Explicit panel count and cut geometry needed |
| Suspension hardpoint plates | `mounting_bracket_steel_v0` (temporary), new Al bracket IDs preferred | Upgrade/New | Should become dedicated non-generic rover hardpoint parts |
| Payload hard-mount interface | `quick_change_tool_interface` (concept), new rover payload hardpoint assembly | New | Kinematic dowel + slot interface from report |
| Dust covers and guards | new `rover_dust_guard_set_v0` | New | Hinged shield concept from report |
| Chassis harness routing hardware | `cable_drag_chain`, `assembled_wire_harness` | Existing | Add explicit route and strain-relief elements |

### 6.2 Suspension and Mobility Assembly
Target assembly ID:
- `rover_suspension_rocker_bogie_v1`

| Sub-assembly | Candidate KB ID(s) | Status | Notes |
|---|---|---|---|
| Left/right rocker arms | new `rocker_arm_left_v0`, `rocker_arm_right_v0` | New | Should not remain rolled into one mass-only part |
| Left/right bogie arms | new `bogie_arm_left_v0`, `bogie_arm_right_v0` | New | Distinct fabrication and QC |
| Differential linkage/bar | new `rocker_bogie_differential_link_v0` | New | Core rocker-bogie functional component |
| Pivot joints | `bearing_set_small`, `ball_bearing_steel_v0`, new pivot pin parts | Existing/New | Add pin/shaft parts explicitly |
| Hard-stop elements | new `suspension_hard_stop_set_v0` | New | Called out in inferred Kapvik design notes |
| Wheel module x6 | `rover_wheel_assembly_v0` | Upgrade | Quantities and internals must be expanded |

### 6.3 Wheel/Drive Module (x6)
Target assembly ID:
- `rover_wheel_drive_module_v0` (new), consumed by rover machine recipe

| Sub-assembly | Candidate KB ID(s) | Status | Notes |
|---|---|---|---|
| Wheel rim and cleat/tread | upgrade `rover_wheel_assembly_v0` internals | Upgrade | Include cleat geometry and hub |
| Bearing cartridge | `bearing_set_small` | Existing | Validate load class |
| Drive motor | `motor_electric_small` | Existing | Replace coarse 12 kg assumption for rover module use via variant |
| Gear reduction stage 1 | new `planetary_gearhead_small_v0` | New | Needed for explicit drivetrain chain |
| Gear reduction stage 2 | replace import-only harmonic with localizable reducer chain | New/Upgrade | Keep semiconductor exception only; gear trains should be manufacturable |
| Wheel encoder | `encoder_optical_simple_v0` or `encoder_rotary_absolute` | Existing | Select one primary and one upgrade variant |
| Motor bracket and coupler | `mounting_bracket_steel_v0`, new coupler part | Upgrade/New | Add torque path parts explicitly |

### 6.4 Power System Assembly
Target assembly ID:
- `rover_power_system_battery_v1` plus associated power-distribution assembly

| Sub-assembly | Candidate KB ID(s) | Status | Notes |
|---|---|---|---|
| Cell blocks | `nife_battery_cell` | Upgrade | Remove import-only posture by adding local manufacturing route |
| Bus bars and links | `bus_bar_copper` | Existing | Already localizable |
| Pack structure and insulation | `insulation_material`, new pack tray/case parts | Existing/New | Add tray, separators, compression hardware |
| BMS/control electronics | `battery_management_system` | Upgrade | Semiconductor exception applies to IC-level devices only |
| Charge control | `charge_controller_set` | Existing | Integrate with rover solar array and pack |
| Harness and connectors | `assembled_wire_harness`, `connector_electrical_multi_pin` | Existing | Explicit quantity per branch |

### 6.5 Avionics and Control Assembly
Target assembly ID:
- `rover_avionics_computer_v1`

| Sub-assembly | Candidate KB ID(s) | Status | Notes |
|---|---|---|---|
| Backplane/enclosure | new `rover_avionics_enclosure_v0`, `control_panel_basic` | New/Existing | Reflect removable avionics box architecture |
| Compute board | `microcontroller_or_embedded_board`, `ai_processor_module_v0` | Existing | IC-level imports acceptable; board integration local |
| Motor control modules | new `motor_controller_module_v0` | New | Do not keep as abstract imported black box |
| Sensor I/O conditioning | `signal_amplifier_module`, new I/O board parts | Existing/New | Required for load cells/mag payload |
| Communications interface | replace pure `radio_communication_module` import with assembled chain | Upgrade | Keep RF chipset-level imports only |
| Harnessing and test headers | `assembled_cable_harness`, `connector_electrical_small` | Existing | Add per-subsystem harness map |

### 6.6 Rover Solar and Surface Sensing
| Sub-assembly | Candidate KB ID(s) | Status | Notes |
|---|---|---|---|
| Solar panel array | `rover_solar_array_v0`, `solar_cell_set` | Upgrade | Keep semiconductor exception at cell level; frame/wiring local |
| Nav camera set | `machine_vision_camera_v0` | Upgrade | Decompose mounts/enclosure/cleaning interface |
| Lidar set | `lidar_sensor_module_v0`, `lidar_time_of_flight_simple_v0` | Upgrade | Keep emitter/receiver die imports, local packaging integration |
| IMU/sun-sensor package | split out from `sensor_suite_general` | New | Replace generic lumped sensor suite with explicit IDs |

### 6.7 Prospecting Module Top Assembly
Target assembly IDs:
- `prospecting_module_v0`
- submodules below as discrete parts

| Submodule | Candidate KB ID(s) | Status | Notes |
|---|---|---|---|
| Payload frame + mount | new `prospecting_mount_frame_v0` | New | Kinematic mount requirements from report |
| Magnetometer boom module | new `magnetometer_boom_module_v0` | New | Must include non-magnetic structure and dual-head baseline option |
| Spectral/context head | new `spectral_context_head_v0` | New | Camera + VNIR/SWIR + calibration target |
| Sampler/geotech head | new `shallow_sampler_geotech_head_v0` | New | Auger, cup carousel, penetrometer, thermal probe |
| Dust/thermal protection | new `prospecting_dust_thermal_protection_v0` | New | Covers, seals, optional heaters |
| Module harness/power | `assembled_wire_harness`, `connector_electrical_multi_pin` | Existing | Explicit to avoid hidden wiring assumptions |

### 6.8 Magnetometer Boom Detailed Sub-BOM (from result 02)
| Sub-assembly | Candidate KB ID(s) | Status | Notes |
|---|---|---|---|
| Fluxgate head outer | new `fluxgate_sensor_head_v0` | New | Can remain partially imported at semiconductor/materials leaf level |
| Fluxgate head inner | new `fluxgate_sensor_head_v0` qty 2 | New | Dual-sensor subtraction architecture |
| Boom tube and hinge | new `magnetometer_boom_structure_v0` | New | Non-magnetic materials and deploy latch |
| AFE/ADC board | new `magnetometer_afe_adc_board_v0` | New | PCB assembly local, IC imports allowed |
| Temperature sensors and calibration coil | new `magnetometer_calibration_set_v0` | New | Required for drift correction workflow |
| Shielded harness and connectors | `coaxial_cable_low_loss`, `coaxial_connector_n_type`, `assembled_cable_harness` | Existing | Select final wire standard in implementation phase |

## 7) Process and Recipe Architecture (non-placeholder)
### 7.1 Build Recipes (multi-step)
For each top-level assembly, recipes should include at least:
1. structural fabrication
2. subassembly integration
3. wiring/electronics integration
4. alignment/calibration
5. acceptance test

Targets:
- `recipe_kapvik_microrover_v0`
- `recipe_rover_chassis_structure_v1`
- `recipe_rover_suspension_rocker_bogie_v1`
- `recipe_rover_power_system_battery_v1`
- `recipe_rover_avionics_computer_v1`
- `recipe_prospecting_module_v0`
- `recipe_magnetometer_boom_module_v0`

### 7.2 Operational Processes
Distinct operational processes to add:
- `rover_traverse_mode_operation_v0`
- `prospecting_station_measurement_v0`
- `prospecting_site_qualification_v0`
- `magnetometer_station_calibration_v0`

Each operation process should require machine capacity via `resource_requirements` and should not be conflated with build recipes.

## 8) Semiconductor Exception Boundary (explicit)
Allowed import exceptions:
- integrated circuits
- image sensor dies
- specialized RF/MMIC dies
- ADC/DAC high-performance chips

Not allowed as permanent import-only black boxes:
- mechanical reducers/gearheads
- structural frames and mounts
- harness assemblies
- battery pack structure and interconnect
- sensor housings and boom assemblies

## 9) Immediate KB Delta Checklist for Result 01
### 9.1 ID normalization
- Add `kapvik_microrover_v0` machine entry.
- Mark `kapvik_microrover_30kg_v0` deprecated with upgrade pointer.

### 9.2 Upgrade existing rover chains
- Rewrite `bom_kapvik_microrover_30kg_v0` (or new canonical BOM) with six wheel-drive modules and explicit rover subsystems.
- Rewrite `recipe_kapvik_microrover_30kg_v0` (or canonical replacement) into multi-step recipe with subsystem inputs.
- Upgrade `rover_chassis_structure_v0`, `rover_suspension_rocker_bogie_v0`, `rover_power_system_battery_v0`, `rover_avionics_computer_v0` into explicit sub-BOM-driven assemblies.

### 9.3 Add full prospecting chain
- Add top module plus all first-generation submodules listed above.
- Add magnetometer detailed module and associated calibration/operation processes.
- Integrate module as required part/capability in prospecting operation processes.

## 10) Reference for Future Agents
When updating rover/prospecting KB entries, cite:
- `design/srm2_bom_research_results/01_prospecting_module.md`
- `design/srm2_bom_research_results/02_magnetometer_payload.md`
- this report: `design/srm2_per_result_plans/01_kapvik_prospecting_detailed_research_report.md`

This file is the high-detail decision baseline intended to prevent low-fidelity placeholder additions.
