# EBF3 Machine Level-2 Status

Purpose: concise status index for the whole EBF3 machine BOM. This file points
reviewers to the current Level-2 audit state without replacing the detailed
source registries, audit files, boundary reviews, or unresolved registers.

Modeling policy:

- Preserve fidelity before closure.
- Keep closure gaps open until a leaf has a source-supported decomposition or a
  deliberate import/commercial-component decision.
- Do not attach local recipes to EBF3 leaves from this status file.
- Use this file to choose the next review target, not to justify new child BOMs.

Current validation posture:

- Last checked after the four-axis positioning update: validation issues were 0.
- Closure errors remain expected because many high-fidelity leaves intentionally
  have no local recipes.

## Whole-Machine Structure

| Level | Item | BOM children | Status |
| --- | --- | ---: | --- |
| Machine | `ebf3_3d_printer` | 7 | Seven-subsystem scaffold in place. |
| Subsystem | `ebf3_controls` | 13 | Level-2 source-table alignment complete. |
| Subsystem | `ebf3_power_supplies` | 15 | Level-2 source-table alignment complete. |
| Subsystem | `ebf3_high_voltage_tank` | 16 | Level-2 scaffold cleaned; concise section-module model adopted for core HV internals. |
| Subsystem | `ebf3_fixed_electron_beam_gun` | 19 | Level-2 audit complete; selected Level-3 plans and child BOMs started. |
| Subsystem | `ebf3_wire_feeder` | 27 | Level-2 source-table alignment complete. |
| Subsystem | `ebf3_four_axis_positioning_system` | 30 | Level-2 source-table alignment complete. |
| Subsystem | `ebf3_manufacture_cabin` | 9 | Level-2 source-table alignment complete. |

## Subsystem Status

| Subsystem | Review file | Current state | Main deferred work |
| --- | --- | --- | --- |
| Controls | `organized/controls_level_2_audit.md` | Corrected CTL-9 to thermal imaging and CTL-13 to controls cabinet. | Lighting support and cabinet harness stay below top-level controls until monitoring/cabin or cabinet decomposition. |
| Power supplies | `organized/power_supplies_level_2_audit.md` | Corrected the power-chain rows and kept non-source-table functional placeholders out of the top-level BOM. | Semiconductor modules, internal supply control board, busbar/cabinet wiring, and electronics readiness. |
| High-voltage tank | `organized/high_voltage_tank_level_2_audit.md` | Added missing HV protection/sensing scaffold rows and adopted `ebf3_hv_section_module_set` for transformer/rectifier/filter internals. | HV-13/HV-15 service/protection detail, HV output/current-monitor topology, and tank/gun cable termination. |
| Fixed electron beam gun | `organized/fixed_electron_beam_gun_level_2_decomposition_audit.md` | Level-2 audit complete; magnetic lens and steering child BOM work has begun. | Cathode cluster, HV/gun-side insulation, diagnostics, signal wiring, gun column, and unresolved material variants. |
| Wire feeder | `organized/wire_feeder_level_2_audit.md` | Rebuilt top-level row alignment to WF-1 through WF-27. | Feedthrough split, motor wiring, guide/nozzle boundary, pressure-roll children, feeder base/body details. |
| Four-axis positioning | `organized/four_axis_positioning_level_2_audit.md` | Corrected FS-19/FS-20 into worm wheel and worm shaft; rotary motor deferred under motor/drive decomposition. | Feedthrough split, motor/signal cable boundaries, beam-current return topology, precision motion readiness. |
| Manufacture cabin | `organized/manufacture_cabin_level_2_audit.md` | Corrected MC-6 to chamber-side wire-feeder mounting port and MC-9 to cabin-side lighting mount/port. | Chamber feedthrough interface split, powered lighting ownership, build-substrate/process-tooling boundary. |

## Active Interface Risks

These are the cross-subsystem issues most likely to create duplicate ownership
or misleading Simviewer structure if deeper decomposition starts too early.

| Interface | Current owner or split | Risk | Next review |
| --- | --- | --- | --- |
| HV cable to gun | HV tank owns main cable; gun owns gun-side HV input. | Cable termination can duplicate gun-side feedthrough or tank-side bushing. | HV tank/gun interface review. |
| Gun-side oil tank vs main HV tank | Gun owns local gun-side oil volume only. | Could be mistaken for the main HV tank subsystem. | HV/gun-side insulation review. |
| Cabin feedthroughs | Cabin owns chamber-side passive ports only when split. | Generic feedthrough item can hide feeder, positioning, controls, or gun inserts. | Feedthrough interface review. |
| Wire feeder feedthrough | Deferred outside top-level wire-feeder BOM. | Needs split between chamber port, feeder insert, motor power, and signals. | Feedthrough interface review. |
| Positioning electrical feedthrough | Positioning owns subsystem-specific insert/interface; cabin owns generic wall port. | Can duplicate controls DAQ or power wiring. | Feedthrough interface review. |
| Process monitoring lighting | Cabin owns passive lighting mount/port; controls may own powered lighting/electronics later. | Can duplicate thermal/visible monitoring or chamber hardware. | Monitoring/cabin interface review. |
| Beam-current return strap | Positioning owns platform/substrate continuity only. | Not a full system-level HV return bus. | Grounding/return review. |
| HV current monitor | HV tank owns primary HV-side monitor; controls own acquisition. | Sensor topology and return-leg placement unresolved. | Grounding/return review. |
| Motion and wire-feed controls | Controls own command/acquisition; mechanisms stay in positioning/wire feeder; drive power stays in power supplies. | Control modules can be confused with motor drivers or local mechanism hardware. | Controls/power/load interface review. |

## Recommended Next Work

1. Use `organized/feedthrough_interface_review.md` as the current ownership rule
   for cabin, gun, wire feeder, positioning, controls, and power/HV wiring.
2. Update affected item notes when deeper child decomposition touches:
   `ebf3_cabin_feedthroughs_and_wiring_ports`,
   `ebf3_wire_feeder_feedthrough_connector`,
   `ebf3_positioning_electrical_feedthrough`,
   `ebf3_gun_signal_wiring`, and `ebf3_gun_hv_input`.
3. Return to fixed electron beam gun Level-3 work, starting with the
   cathode cluster or HV/gun-side insulation cluster.
4. Material/process readiness reviews come after ownership and decomposition are
   stable. Do not use generic lower-resolution local parts to close EBF leaves.

## Review Rule

If a future change makes Simviewer simpler but hides one of the interface risks
above, keep the item deferred or split it across subsystem boundaries instead of
collapsing it into a generic component.
