# EBF3 Interface Architecture

Status: current working architecture for cross-subsystem interfaces.

Purpose:

- Select one readable interface model for the current EBF3 BOM.
- Prevent duplicate ownership across HV tank, fixed gun, controls, power
  supplies, cabin, wire feeder, and positioning.
- Leave dimensions, ratings, connector families, feedthrough pinouts, and local
  recipes for later material/process readiness.

This file is the current entry point for interface decisions. Detailed evidence
and earlier boundary reasoning remain in the focused review files.

## Architecture Rule

Use a layered ownership model:

| Layer | Owner |
| --- | --- |
| Passive chamber wall openings, ports, flanges, viewports, brackets | Manufacture cabin |
| Main high-voltage source tank, oil-side bushing, and main HV cable body | High-voltage tank |
| Gun-side HV receiving/input hardware and local gun HV region | Fixed electron beam gun |
| In-gun pickups, collectors, and short local signal wiring | Fixed electron beam gun |
| Positioner-specific feedthrough insert and in-chamber positioner cabling | Four-axis positioning system |
| Wire-feeder mechanism and feeder-specific feedthrough insert | Wire feeder |
| Driver power stages, regulated current sources, and motor/coil power outputs | Power supplies |
| Commands, DAQ, signal conditioning, logging, and interlock decisions | Controls |

## HV Path

Current working path:

`HV tank section-module source -> internal HV leads -> tank-side output bushing
-> main shielded HV cable -> gun-side HV input -> fixed-gun HV region`

Ownership:

- HV tank owns `ebf3_internal_hv_leads_terminals`,
  `ebf3_tank_side_hv_output_bushing`, and `ebf3_hv_cable_to_gun`.
- Fixed gun owns `ebf3_gun_hv_input` and keeps `ebf3_gun_hv_insulator` as a
  separate boundary leaf.
- Main insulating fluid is `ebf3_hv_transformer_insulating_fluid` in the HV
  tank. `ebf3_gun_side_oil_tank` remains only an unresolved marker for possible
  local gun-side insulation.

Current KB representation:

- `bom_ebf3_tank_side_hv_output_bushing` represents the tank-side bushing as
  conductor, insulator body, mounting flange, and cable socket/interface package
  markers.
- `bom_ebf3_hv_cable_to_gun` represents the main cable body as conductor,
  dielectric, stress-control layer, shield, and outer jacket package markers.
- `bom_ebf3_gun_hv_input` represents the gun-side receiving input as central
  conductor, receiving terminal, and local flange/housing package markers.
- `bom_ebf3_gun_hv_insulator` represents the standalone gun-side HV insulator
  as ceramic body, metallized end-interface, mounting collar, and local
  field-grading markers.
- Field grading is represented only as local interface markers:
  `ebf3_tank_side_bushing_field_grading_shield` for HV-8 and
  `ebf3_gun_hv_insulator_field_grading_electrode_set` for FG-13.

Deferred:

- Exact tank-side and gun-side connector/socket geometry.
- Final gun-side ceramic feedthrough integration versus standalone insulator
  construction.
- Final field-grading/corona-shield geometry and potential connections.
- Cable ratings, terminations, creepage/clearance, and test procedure.

## Signal And Diagnostics Path

Current working path:

`gun pickup/collector -> short local gun wiring -> subsystem-specific
feedthrough insert or selected shared port -> controls-side ADC/signal
conditioning -> controls software/logging/interlock logic`

Ownership:

- Fixed gun owns pickup hardware and `ebf3_gun_signal_wiring` only up to the
  local gun-side signal boundary.
- Cabin owns passive port/flange/window features only.
- Controls own `ebf3_analog_input_adc_module`,
  `ebf3_sensor_interface_module`, `ebf3_data_logger_timebase`, and
  `ebf3_safety_blocking_logic`.

Current KB representation:

- `bom_ebf3_gun_signal_wiring` represents local diagnostic leads, a
  gun-diagnostic feedthrough insert/interface marker, and a local
  shield-termination interface marker.
- Cabin feedthrough items remain passive port/flange/shared-plate candidates.
- Controls DAQ, signal conditioning, logging, and interlock logic remain under
  controls items, not under the fixed gun.

Deferred:

- Whether the diagnostic signal feedthrough becomes coaxial, multipin, part of a
  shared feedthrough plate, or several subsystem-specific connectors.
- Final shield termination policy.
- Bias/suppression electrode topology for beam diagnostics.
- DAQ channel count, isolation, calibration, and electronics design.

## Motion And Feedthrough Path

Current working path:

`power-supply driver output -> subsystem in-chamber cable -> subsystem-specific
feedthrough insert -> motor/sensor/load package`

Ownership:

- Power supplies own driver output hardware in `ebf3_multi_channel_driver_module`.
- Positioning owns `ebf3_vacuum_compatible_motor_cabling`,
  `ebf3_vacuum_compatible_signal_cabling`, and
  `ebf3_positioning_electrical_feedthrough`.
- Wire feeder owns feeder mechanism and the feeder-specific feedthrough insert.
- Cabin owns only passive chamber openings and mounting ports.

Current KB representation:

- `bom_ebf3_positioning_electrical_feedthrough` represents the
  positioning-specific insert as motor-power pins, signal pins, insulator body,
  flange, vacuum-side connector, air-side connector, and shield termination
  interface.
- `bom_ebf3_wire_feeder_feedthrough_connector` represents the
  wire-feeder-specific insert with the same power/signal/insulator/flange/
  connector/shield-interface split.

Deferred:

- Motor current ratings and connector families.
- Feedthrough pinout and ceramic-to-metal construction.
- Final wire-feeder feedthrough pinout, connector family, and service boundary.
- External cabinet harness routing.

## Grounding And Return

Current working model separates four paths:

1. Protective bonding: chassis, tank enclosure, cabin, cabinets, and service
   safety bonds.
2. HV source return/reference: electrical reference/return for the accelerating
   high-voltage source.
3. Beam-current continuity: substrate/platform current path represented at the
   platform by `ebf3_beam_current_return_strap`.
4. Low-voltage sensing: isolated scaled signals into controls.

Ownership:

- HV tank owns `ebf3_hv_tank_grounding_terminal` as protective tank bonding.
- Positioning owns `ebf3_beam_current_return_strap` as platform/substrate
  continuity hardware.
- HV tank owns the primary HV current-monitor package
  `ebf3_hv_output_return_current_monitor`.
- Controls own isolated acquisition and interpretation.

Current KB representation:

- `bom_ebf3_hv_tank_grounding_terminal` represents protective tank bonding with
  a ground lug and bonding anchor.
- `bom_ebf3_hv_output_return_current_monitor` represents the primary HV-side
  current monitor with sensing element, insulating mount, and signal lead.
- `bom_ebf3_beam_current_return_strap` represents platform/substrate
  beam-current continuity with flexible conductor, lugs, and local fastener
  interface.
- `ebf3_gun_signal_shield_termination_interface` represents the gun-side
  diagnostic signal shield boundary, not a global return path.

Deferred:

- Whether the physical HV return is a dedicated cable, cabinet bus, chamber
  bond, platform connection, or combined topology.
- Current monitor sensor type and exact return-leg placement.
- Ground-fault and service-discharge behavior.
- Signal shield termination.

## Current KB Action

- Do not add a generic global feedthrough assembly, global return bus, or second
  gun-side oil inventory.
- Do not move driver electronics into mechanisms or DAQ electronics into the
  fixed gun.
- Keep current Level-3 package BOMs as package markers until geometry, ratings,
  and material/process readiness are reviewed.

## Follow-Up Order

1. HV cable/bushing/gun-input geometry and field grading.
2. Diagnostic signal feedthrough and shield termination.
3. Grounding/HV-return physical topology.
4. Positioning and wire-feeder feedthrough pinout and connector architecture.
5. Material/process readiness for cables, ceramics, feedthroughs, sensors,
   drivers, and vacuum-compatible wiring.
