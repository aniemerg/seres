# HV Electrical Interface Review

Status: boundary review completed for current HV tank protection/sensing
scaffold.

Purpose:

- Resolve current Level-2 ownership for HV-10, HV-11, HV-12, tank grounding,
  controls ADC/safety logic, power-supply controller interfaces, and current
  return candidates.
- Preserve fixed electron gun fidelity by keeping high-voltage sensing/protection
  from being hidden inside the gun HV input or generic controls.

Scope:

- `ebf3_hv_discharge_bleeder_resistor_chain` (HV-10)
- `ebf3_hv_output_voltage_divider_sensing` (HV-11)
- `ebf3_hv_output_return_current_monitor` (HV-12)
- `ebf3_hv_tank_temperature_sensor` (HV-14)
- `ebf3_hv_tank_grounding_terminal` (HV-15 partial)
- `ebf3_analog_input_adc_module` (CTL-5)
- `ebf3_sensor_interface_module` (CTL-6)
- `ebf3_safety_blocking_logic` (CTL-12)
- `ebf3_power_supply_control_board` (deferred/derived power-supply controller)
- `ebf3_accelerating_voltage_dc_supply` (deferred/derived accelerating-HV
  function)
- `ebf3_beam_current_return_strap` (FS-24)

Source registry:

- `research/ebf3_bom_sources/sources/level_2_parts/hv_electrical_interface/hv_electrical_interface_sources.md`

Related reviews:

- `research/ebf3_bom_sources/organized/hv_tank_interface_review.md`
- `research/ebf3_bom_sources/organized/hv_grounding_return_review.md`
- `research/ebf3_bom_sources/organized/high_voltage_tank_level_2_audit.md`
- `research/ebf3_bom_sources/derived/ebf3_subsystem_boundaries.md`

## Source Authority Assessment

1. `RAW-BINP-60KV-15KW-HV-TANK` supports HV source protection and sensing: output
   voltage monitoring, transformer temperature monitoring, input/output current
   protection, and the role of digital control circuitry.
2. `RAW-BINP-60KEV-30KW` supports beam current, cathode heat current, magnetic
   lens/corrector currents, and blocking current monitoring in a comparable
   electron-beam facility.
3. TT Electronics sources support high-voltage bleeder and divider resistor
   functions, but they do not specify EBF3 geometry, ratings, packaging, or oil
   immersion.
4. Spellman sources support grounding and external interlock concepts for high
   voltage power supplies; they do not directly map the physical interlock switch
   into the EBF3 tank.
5. Isabellenhuette supports Manganin as a precision/shunt resistor material
   candidate. It does not justify a local manufacturing recipe.
6. Controls and power-supply mappings are first-pass scaffold mappings. They
   define current subsystem leaves but are not decomposition evidence.

## Source Evidence And Use

### RAW-BINP-60KV-15KW-HV-TANK

Evidence:

- "Output voltage"
- "Breakdown protection controls output current"
- "Temperature of high-voltage transformer"
- "control circuit is realised in digital signal processor"
- "controller measured 7 analogue channels"

Use:

- Supports HV voltage sensing, current monitoring, temperature sensing, and
  controller/ADC boundary concepts.
- Does not make the measurement electronics a fixed-gun child item.

### RAW-BINP-60KEV-30KW

Evidence:

- "beam current, cathode heat current"
- "magnetic lens and correctors currents"
- "blocking current"
- "control computer can control"

Use:

- Supports keeping process/current measurements visible to controls.
- Does not assign beam-current return hardware to HV tank by itself.

### LOCAL-EBF3-HV-TANK-TABLE

Evidence:

- HV-10 candidate: discharge/bleeder resistor chain.
- HV-11 candidate: voltage divider/output voltage sensing hardware.
- HV-12 candidate: output or return current monitor.
- HV-15 candidate: tank grounding, shielding, and service interlock hardware.

Use:

- Introduces current scaffold items and boundary questions. It cannot justify
  local closure or deeper child BOMs by itself.

### LOCAL-EBF3-CONTROLS-MAPPING

Evidence:

- CTL-5 is analog input and ADC for voltage/current/temperature/feedback.
- CTL-6 is sensor interface electronics for isolated signal conditioning.
- CTL-12 is safety logic, alarm, and blocking/interlock module.

Use:

- Supports assigning low-voltage acquisition, conditioning, and logic to
  controls.
- Does not move HV-side divider/shunt hardware out of the HV tank.

### LOCAL-EBF3-POWER-SUPPLIES-MAPPING

Evidence:

- Power-supply control-board and accelerating-HV output concepts are retained as
  deferred/derived candidates after the power-supplies Level-2 audit.

Use:

- Supports keeping regulated HV generation functions and PSU-internal control
  functions in power supplies when they are reintroduced at a deeper
  power-electronics level.
- Does not make central machine controls part of the power-supply subsystem.

### WEB-TT-HIGH-VOLTAGE-RESISTORS

Evidence:

- "High Voltage Bleeders"
- "discharge capacitors to safe voltage levels"
- "High Voltage Dividers"

Use:

- Supports HV-10 bleeder and HV-11 divider functions as real HV hardware.
- Does not justify a child BOM or material lock.

### WEB-TT-HVD-DIVIDER-RESISTORS

Evidence:

- "High Voltage Divider Resistors"
- "Voltage ratings up to 30kV"
- "Ratio tolerance down to 0.25%"

Use:

- Supports divider resistor chains as a real measurement hardware class.
- EBF3/BINP voltage scale is higher than one 30 kV element, so final design would
  need series architecture or supplier selection before decomposition.

### WEB-SPELLMAN-SL2KW-MANUAL

Evidence:

- "High voltage power supplies must always be grounded"
- "Capacitance of both the load and power supply is discharged"

Use:

- Supports grounding and discharge as high-voltage safety requirements.
- Does not define EBF3 tank grounding hardware geometry.

### WEB-SPELLMAN-EXTERNAL-INTERLOCKS

Evidence:

- "external interlock points"
- "low impedance connection"
- "HV ON mode"

Use:

- Supports interlock loop/interface concepts.
- Decision logic and interlock state handling belong to controls; physical
  service switches may belong to HV tank or power-supply cabinet depending on
  location.

### WEB-ISABELLENHUETTE-MANGANIN

Evidence:

- "standard material for precision"
- "shunt resistors"
- "low temperature coefficient"

Use:

- Supports Manganin as a candidate shunt material for HV-12.
- Does not justify child BOM or recipe selection.

## Boundary Decision Matrix

| Function/candidate | Decision | Owning item/subsystem | Rationale |
| --- | --- | --- | --- |
| HV discharge / bleeder resistor chain | Keep in HV tank | `ebf3_hv_discharge_bleeder_resistor_chain` | Discharges HV tank/output capacitance and is part of tank-side HV safety/protection hardware. |
| Bleeder resistor elements, supports, shields | Defer | HV-10 | Need voltage, energy, oil/air placement, creepage, discharge time, and serviceability. |
| HV output voltage divider high-voltage resistor chain | Keep in HV tank | `ebf3_hv_output_voltage_divider_sensing` | HV-side scaling hardware belongs near the HV output/tank interface. |
| Low-voltage ADC reading scaled voltage | Split boundary to controls | `ebf3_analog_input_adc_module` / `ebf3_sensor_interface_module` | Controls own signal acquisition and conditioning. |
| HV output/return current sensor primary element | Keep in HV tank, unresolved exact type | `ebf3_hv_output_return_current_monitor` | HV tank table identifies monitor hardware, but shunt vs current transformer vs Hall sensor is unresolved. |
| Beam-current return strap/platform return | Split boundary to positioning | `ebf3_beam_current_return_strap` | `hv_grounding_return_review` keeps only platform/substrate continuity hardware in positioning; system-level return topology remains deferred. |
| Current-monitor low-voltage signal conditioning | Split boundary to controls | `ebf3_sensor_interface_module` / `ebf3_analog_input_adc_module` | Controls own acquisition and signal conditioning, not the HV-side primary sensor. |
| Transformer/oil temperature sensor primary element | Keep in HV tank | `ebf3_hv_tank_temperature_sensor` | Sensor physically measures HV tank/transformer condition. |
| Temperature ADC / alarm logic | Split boundary to controls | `ebf3_sensor_interface_module` / `ebf3_safety_blocking_logic` | Controls own signal conditioning and decision logic. |
| Tank grounding terminal | Keep in HV tank | `ebf3_hv_tank_grounding_terminal` | Grounding/bonding terminal is part of HV tank enclosure safety. |
| Global ground/current-return architecture | Defer / split boundary | HV tank / power supplies / positioning / gun / controls | Documented in `hv_grounding_return_review`; physical return topology remains unresolved. |
| Service interlock switch physically mounted on HV tank | Defer under HV tank | HV-15 future child | HV-15 supports service interlock hardware, but physical switch location is not confirmed. |
| Interlock loop logic and blocking decision | Split boundary to controls | `ebf3_safety_blocking_logic` | Controls own logic, alarms, and blocking/interlock decisions. |
| PSU-internal analog/digital interface board | Defer as power-supply child detail | `ebf3_power_supply_control_board` | Internal PSU controller is not central controls, but it is no longer a source-table Level-2 row. |
| Accelerating HV regulated output generation | Defer as power-supply/HV-source function | `ebf3_accelerating_voltage_dc_supply` | Power supplies own regulated source functions, but the Level-2 BOM now presents the source chain through source-table converter items and HV tank section-module hardware. |

## KB Action

- Do not create child BOMs for HV-10, HV-11, or HV-12 in this pass.
- Keep HV-10/HV-11/HV-12 as unresolved HV tank leaf items.
- Update notes on HV-10/HV-11/HV-12, controls acquisition/logic items, power
  supply controller/output items, and the beam-current return strap to point to
  this boundary review.
- Keep current return topology and interlock physical switches unresolved until a
  source drawing or explicit design selection defines the physical path.

## Manufacturing Readiness

No HV electrical-interface item is local-ready. Bleeder energy rating, voltage
divider ratio and insulation, shunt/current-sensor architecture, grounding
topology, interlock loop design, signal isolation, ADC input range, oil/vacuum
compatibility, test procedure, and safety certification all need separate review
before recipes or local closure are added.

## Next Work

1. `hv_oil_service_review`: resolve HV-13 fill/drain, pressure relief, level
   indicator, seals, and oil service hardware.
2. `controls_signal_boundary_review`: use this plan and
   `hv_grounding_return_review` when reviewing ADC, sensor
   interface, safety logic, and central control ownership.
