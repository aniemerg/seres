# Power Supplies Level-2 Audit

Status: review completed; source-table aligned BOM correction and package-level
child splits applied.

Purpose:

- Compare current power-supply BOM leaves against the user-derived table and
  available source evidence.
- Preserve the boundary between power supplies, HV tank, controls, electron gun,
  wire feeder, and positioning.
- Avoid creating child BOMs or recipes until source-tag mismatches are resolved.

Source registry:

- `research/ebf3_bom_sources/sources/level_1_subsystems/power_supplies/power_supplies_sources.md`

Related boundary reviews:

- `research/ebf3_bom_sources/derived/ebf3_subsystem_boundaries.md`
- `research/ebf3_bom_sources/organized/electrical_signal_boundary_review.md`
- `research/ebf3_bom_sources/organized/hv_grounding_return_review.md`
- `research/ebf3_bom_sources/organized/coil_level_decomposition_plan.md`

## Source Use

### RAW-BINP-60KV-15KW-HV-TANK

Evidence:

- "3-phase rectifier D1-D6"
- "electromagnetic (EMI) filter F1"
- "rectifiers filter L1 C1-C4"
- "20 kHz inverter with IGBT switches Q1-Q4"
- "impedance matching design L2, L3, C5"
- "isolation transformer T1"
- "input switch and rectifier"
- "distilled water is used to cool IGBT switches"

Use:

- Strongly supports the incoming rectifier/filter/inverter/matching/isolation
  power-chain leaves.
- Supports thermal management for power electronics.
- Does not support a generic "snubber network" as a separate Level-2 table row.

### RAW-BINP-60KEV-30KW

Evidence:

- "Modulator with cathode heater source"
- "0 to 600 V"
- "0 to 100 A"
- "magnetic lens and correctors currents"
- "control computer can control"

Use:

- Supports control-electrode bias supply, cathode heater supply, and regulated
  current outputs for lens/corrector loads.
- Confirms controls observe/command these functions, but the supply hardware
  stays in power supplies.

### RAW-NASA-EBF-PATENT

Evidence:

- "power distribution subsystem"
- "wire feed motor"
- "positioning Subsystem motor"
- "apportioning power"
- "conditioning power"

Use:

- Supports auxiliary low-voltage power distribution and motor/load power
  distribution as real EBF machine functions.
- Does not define specific driver module topology, cabinet layout, or materials.

### LOCAL-EBF3-POWER-SUPPLIES-TABLE

Use:

- Introduces PS-1 through PS-15 candidates.
- Candidate-only; it cannot justify recipes, materials, or child BOMs by itself.

## Main Finding

The current power-supply BOM does not fully match the source table.

The largest mismatches are PS-6 through PS-15:

- Table row PS-6 is a **ripple damping inductor**, but the current BOM has
  `ebf3_damping_resistor`.
- Table row PS-7 is **full-bridge inverter**, but the current BOM has
  `ebf3_snubber_network`.
- Table row PS-9 is **primary isolation transformer**, but the current BOM has
  `ebf3_full_bridge_inverter`.
- Table row PS-12 is **auxiliary low-voltage DC supply**, but the current BOM has
  `ebf3_accelerating_voltage_dc_supply`.
- Table row PS-13 is **low-voltage distribution panel**, but the current BOM has
  `ebf3_lens_corrector_current_supplies`.
- Table row PS-14 is **multi-channel driver module**, but the current BOM has
  `ebf3_power_supply_control_board`.
- Table row PS-15 is **power-electronics thermal management hardware**, while
  the current BOM partially broadens this to cabinet bus/cooling.

Because these were source-tag and meaning mismatches, this audit corrected the
Level-2 BOM presentation but does not create child BOMs yet.

## Level-2 Decision Matrix

| Source table row | Current or recommended item | Decision | Rationale |
| --- | --- | --- | --- |
| PS-1 AC input connector | `ebf3_power_input_cable_gland` | keep / retag wording | Same function; name can remain if note says AC input connector and cable gland. |
| PS-2 main disconnect switch | `ebf3_main_disconnect_switch` | keep | Source and table align. |
| PS-3 EMI filter | `ebf3_emi_filter` | keep | BINP source directly supports EMI filter. |
| PS-4 input rectifier | `ebf3_input_rectifier` | keep | BINP source directly supports rectifier. |
| PS-5 DC-link capacitor bank | `ebf3_dc_link_capacitor_bank` | keep | BINP source directly supports C1-C4 filter capacitors. |
| PS-6 ripple damping inductor | `ebf3_ripple_damping_inductor` | corrected | BINP source supports L1 inductor, not a damping resistor at this row. |
| PS-7 full-bridge inverter | `ebf3_full_bridge_inverter` | corrected | Existing inverter item retained and aligned to PS-7. |
| PS-8 matching circuit | `ebf3_inverter_matching_network` | keep | BINP source supports L2/L3/C5 matching circuit. |
| PS-9 primary isolation transformer | `ebf3_primary_isolation_transformer` | corrected | The table and BINP source support T1 isolation transformer. |
| PS-10 control-electrode bias supply | `ebf3_control_electrode_bias_supply` | keep | BINP source supports 0 to 600 V control-electrode supply. |
| PS-11 cathode heater supply | `ebf3_cathode_heater_supply` | keep | BINP source supports 0 to 100 A cathode heater source. |
| PS-12 auxiliary low-voltage DC supply | `ebf3_auxiliary_low_voltage_dc_supply` | corrected | NASA patent supports power distribution; previous accelerating-HV item is deferred to avoid overlap with HV source architecture. |
| PS-13 low-voltage distribution panel | `ebf3_low_voltage_distribution_panel` | corrected | NASA patent supports apportioning/distributing power. |
| PS-14 multi-channel driver module | `ebf3_multi_channel_driver_module` | corrected | Represents driver outputs for magnetic, deflection, feeder, and positioning loads while the loads remain in their owning subsystems. |
| PS-15 thermal management hardware | `ebf3_power_electronics_thermal_management` | corrected | BINP source supports cooling IGBT switches; busbar/cabinet details remain deferred. |
| Power-supply internal control board | `ebf3_power_supply_control_board` | deferred / not in top-level BOM | BINP source supports DSP/PLM/control circuit, but it is not a visible PS-14 row. |
| Snubber network | `ebf3_snubber_network` | deferred / not in top-level BOM | Plausible power-electronics detail, but not a visible source-table row and not needed at this level. |
| Accelerating HV DC supply | `ebf3_accelerating_voltage_dc_supply` | deferred / architecture decision needed | As a function it is real, but the present Level-2 table splits HV source across power converter and HV tank. Keeping it as a separate leaf may duplicate the sectioned HV source model. |

## Recommended BOM Correction

Use the source table as the Level-2 presentation because it is the user's visible
review artifact. Keep source-backed extra concepts only as derived or deferred
rows.

Applied concise target shape:

1. Keep PS-1 through PS-5 as-is.
2. Replace `ebf3_damping_resistor` with a ripple-damping inductor item.
3. Retag `ebf3_full_bridge_inverter` as PS-7.
4. Keep `ebf3_inverter_matching_network` as PS-8.
5. Add a PS-9 isolation-transformer leaf.
6. Keep PS-10 and PS-11.
7. Replace PS-12/PS-13 with auxiliary low-voltage supply and low-voltage
   distribution panel leaves.
8. Decide whether PS-14 should be one concise multi-channel driver module or
   split into supply modules by load family.
9. Keep PS-15 as thermal management, but do not hide all cabinet wiring/busbars
   there unless a cabinet integration item is intentionally added.
10. Leave `ebf3_power_supply_control_board`, `ebf3_snubber_network`, and
    `ebf3_accelerating_voltage_dc_supply` out of the top-level BOM as deferred
    candidates unless a later power-electronics decomposition justifies them.

## Presentation Decision

The source-table aligned model is now the active Level-2 presentation:

- The power-supply BOM matches source-table rows PS-1 through PS-15.
- Extra functional leaves such as accelerating HV output, snubber network, and
  power-supply internal control board are kept out of the top-level BOM as
  deferred candidates.
- Those deferred candidates may be reintroduced later inside a
  power-electronics child decomposition if source evidence and boundaries justify
  them.

## Load/Driver Follow-Up

Target: decide whether PS-14 should be split now by load family, such as lens
current drivers, corrector drivers, deflection drivers, wire-feed motor drivers,
and positioning motor drivers.

Decision: do not split yet.

Reasoning:

- The current boundary model assigns loads to their owning subsystems and
  driver/current-source hardware to power supplies.
- BINP supports magnetic lens and corrector currents, and NASA supports power
  distribution to motors, but the present sources do not define separate driver
  boards, channel counts, connectors, current ratings, or cabinet packaging.
- Splitting PS-14 now would duplicate existing load items or imply a driver
  topology that has not been selected.

Current action:

- Keep `ebf3_multi_channel_driver_module` as the concise Level-2 driver-output
  item, now with a package-level child BOM.
- Keep `ebf3_lens_corrector_current_supplies` as a deferred functional
  candidate, not a top-level BOM child.
- Revisit only after a load/channel architecture is selected.

## Batch Child Split Review

| Parent scope | Current status | Rationale |
| --- | --- | --- |
| AC input, disconnect, EMI filter, rectifier, DC link | adopt package split / detail deferred | BINP supports the power-chain functions. Infineon power-converter references support package children such as EMI filters, driver/power stages, DC-link capacitors, busbars, and heatsinks. Ratings and component values remain unresolved. |
| Inductors, matching network, isolation transformer | adopt package split / detail deferred | BINP supports L/C matching and isolation-transformer functions. Child BOMs preserve winding/core/insulation/mount boundaries without selecting magnetic design. |
| Inverter and driver modules | adopt package split / detail deferred | Infineon references support power modules, gate-driver boards, DC link, and cooling hardware as package-level structures. Semiconductor type, gate-drive topology, snubbers, and isolation ratings remain unresolved. |
| Bias, heater, auxiliary DC, distribution panel | adopt package split / detail deferred | BINP and NASA sources support gun supply and machine power-distribution functions. Converter board, terminal, filter, enclosure, and heatsink children are retained without claiming local manufacturability. |
| Thermal management | adopt package split / detail deferred | BINP explicitly supports cooling IGBT switches. Heat sinks, cooling plates, fan/pump module, thermal interfaces, and ducts/lines are package children; coolant type and lunar manufacturability remain unresolved. |
| Load-family split under PS-14 | defer | Separate lens/corrector/deflection/motion/feed driver outputs need channel architecture before modeling as separate top-level or child supply modules. |

## Manufacturing Readiness

No power-supply item is local-ready. Semiconductor modules, isolation
transformers, HV bias supplies, high-current heater supplies, cooling, insulation,
ratings, EMI behavior, grounding/return topology, and safety certification all
need separate material/process and electrical-design reviews before recipes are
attached.
