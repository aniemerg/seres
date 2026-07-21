# EBF3 Subsystem Boundary Audit

Status: draft boundary policy for the current seven-subsystem EBF3 scaffold.

Purpose: preserve BOM fidelity while preventing subsystem assemblies from becoming
implicit low-resolution substitutes for true bottom-level parts. This document is
about ownership boundaries only; it is not a local manufacturability closure plan.

## Fidelity Policy

- Do not attach local manufacturing recipes to EBF3 leaf items until the item has
  been decomposed to single-material, single-process parts or intentionally
  declared as an imported/commercial component.
- Closure gaps on these leaf items are expected during high-fidelity BOM
  expansion. They should not be fixed by linking to generic low-resolution KB
  parts.
- Use existing KB parts only after checking that their resolution, material
  specificity, geometry/function, and process assumptions are compatible with the
  EBF3 leaf item.
- Treat interface items as first-class audit targets. If an item crosses a
  subsystem boundary, split it into a port, insert/feedthrough, cable, bracket, or
  mating hardware rather than hiding the boundary inside one generic item.

## General Ownership Rules

1. The subsystem that performs the primary physical function owns the functional
   part.
2. The subsystem that provides the envelope or mounting datum owns the passive
   port, opening, flange, or chamber-side bracket.
3. The subsystem that provides electrical power owns the source or supply.
   The subsystem that consumes power owns the load.
4. Signal acquisition and decision logic belong to controls. Beam, motion, or
   feeder hardware that produces the signal remains with the relevant subsystem.
5. Vacuum-boundary penetrations should be split when fidelity matters:
   chamber port/flange belongs to the manufacture cabin; feedthrough insert,
   internal lead, or subsystem-specific connector belongs to the subsystem that
   uses it.
6. Cables and hoses should be owned by the subsystem whose package they are part
   of, unless the cable is the main inter-subsystem transmission element.
7. If an item would be difficult to remove, inspect, or replace independently in
   the real machine, it is probably not a good boundary item and should be split.

## Subsystem Boundary Definitions

### Manufacture Cabin

Owns the vacuum/process envelope: chamber shell, doors, windows, viewports,
generic chamber ports, chamber-side flanges, structural penetrations, internal
mounting datums, and cabin-level vacuum hardware.

Does not own the internals of the electron gun, wire feeder, four-axis stage,
high-voltage tank, or power/control cabinets. For subsystem penetrations, the
cabin owns the chamber-side opening and structural flange only.

### Fixed Electron Beam Gun

Owns electron source and beamline hardware: cathode, anode, control/screen
electrodes, gun-side insulators, magnetic lenses, deflection coils, trajectory
corrector, beam diagnostics near the gun, local gun-side HV input hardware, and
gun-side oil/insulation volume if it is physically part of the gun column.

Does not own the main high-voltage tank, main accelerating supply, main HV cable
run, chamber mounting port, or central control electronics.

### High Voltage Tank

Owns the oil-filled high-voltage supply enclosure and its internal HV generation
chain: tank shell, insulating oil, transformer/rectifier/filter sections,
tank-side bushings, HV cable to the gun, oil-side supports, service hardware, and
tank monitoring sensors.

Does not own gun-internal electrodes, gun-side local insulators, or central
controls. If a gun-side oil tank is physically integrated into the gun column, it
should remain with the fixed electron beam gun.

### Power Supplies

Owns non-tank electrical conversion hardware and regulated outputs: input
rectifier, DC link, inverter, cathode heater supply, control-electrode bias
supply, lens/corrector current supplies, wire-feeder/motion power modules, local
power-supply control boards, bus bars, cabinet cooling, and power cabinet
harnessing.

Does not own the central control computer/software, process monitoring logic, or
the loads inside the gun, feeder, and positioning systems.

### Controls

Owns central machine control and instrumentation: control computer, software,
DAQ, safety/interlock logic, operator interface, central cabinet wiring,
high-level motion/beam/feed commands, process monitoring camera and lighting
electronics, and control network hardware.

Does not own power-conversion hardware merely because it has a controller board.
Internal supply controllers remain in power supplies unless they are the central
machine controller.

### Wire Feeder

Owns the wire path and feed package: spool, brake, guide tubes, drive rolls,
tensioning hardware, motor/gearbox, encoder, nozzle, wire outlet geometry,
local feeder harness, feedthrough connector insert if feeder-specific, and
mount-to-gun bracket if it is part of the feeder package.

Does not own generic chamber ports or gun structural ports. If the feeder bracket
is a permanent gun-column feature rather than a removable feeder package feature,
split the item and move the gun-side mounting datum to the electron gun.

### Four-Axis Positioning System

Owns workpiece motion hardware: X/Y/Z/rotary axes, slides, bearings, screws,
motors, encoders, limit switches, substrate platform, clamp, motor cabling inside
the motion package, positioning-specific feedthrough inserts, and beam current
return hardware attached to the platform/substrate path.

Does not own the central motion controller if that controller is part of the
machine controls, or generic chamber ports if they are part of the cabin wall.

## Interface Item Audit

| Item | Current owner | Boundary risk | Decision | Follow-up |
| --- | --- | --- | --- | --- |
| `ebf3_hv_cable_to_gun` | High voltage tank | Cable terminates at gun, but main function is HV transmission from tank. | Keep in high voltage tank. | Later split into tank-side termination, cable body, and gun-side termination if detailed cable BOM is needed. |
| `ebf3_gun_side_oil_tank` | Fixed electron beam gun | Could be confused with the main high-voltage tank or a second confirmed oil inventory. | Keep only as an unresolved gun-side insulation marker; main confirmed fluid inventory belongs to `ebf3_hv_transformer_insulating_fluid`. | Do not split into shell/lid/oil/seals until EBF3-specific gun-side oil-package evidence is found. |
| `ebf3_gun_hv_input` | Fixed electron beam gun | Interface between HV tank/cable and gun. | Keep in electron gun as gun-side receiving/feedthrough hardware. | If decomposed, split into central conductor, ceramic insulator, flange, and cable-side termination. |
| `ebf3_control_electrode_bias_supply` | Power supplies | Electrically tied to gun control electrode. | Keep in power supplies; gun owns the electrode load. | Cross-reference gun control electrode in notes instead of nesting it into gun BOM. |
| `ebf3_cathode_heater_supply` | Power supplies | Cathode heater is in gun; supply is separate. | Keep in power supplies. | Decompose heater leads in gun separately from regulated heater supply. |
| `ebf3_multi_channel_driver_module` | Power supplies | Supplies drive gun magnetic, deflection, feeder, and positioning loads. | Keep in power supplies; loads remain in their owning subsystems. | Add explicit load references later if schema supports electrical interfaces. |
| `ebf3_power_supply_control_board` | Power supplies | Could be mistaken for central controls. | Keep out of the top-level BOM as a deferred power-supply internal controller candidate. | Reintroduce only inside a later power-electronics child decomposition. |
| `ebf3_visible_camera` | Controls | Camera sees inside cabin but is an instrumentation/control device. | Keep in controls. | Cabin owns viewport/window or camera port, not camera electronics. |
| `ebf3_thermal_imaging_monitoring_system` | Controls | Thermal camera sees inside cabin but is an instrumentation/control device. | Keep in controls. | Cabin owns viewport/window or camera port, not camera electronics. |
| `ebf3_process_monitor_lighting` | Controls / cabin | Lighting is plausible monitoring support but is not the source-table CTL-9 top-level item. | Keep deferred until monitoring/cabin interface review. | If adopted later, controls owns powered lighting/electronics and cabin owns passive mounts/ports. |
| `ebf3_cabin_lighting_mount_and_port` | Manufacture cabin | Lighting crosses cabin/controls if modeled as a powered fixture. | Keep in cabin only as passive mount, optical access, shield, or chamber-side penetration. | Powered light source, wiring control, and monitoring logic remain deferred. |
| `ebf3_cabin_feedthroughs_and_wiring_ports` | Manufacture cabin | Can duplicate feeder, positioning, gun, or sensor feedthroughs. | Keep deferred; if reintroduced, cabin owns chamber-side passive openings, flanges, or shared port plates only. | Use `organized/ebf3_interface_architecture.md` before adding child items. |
| `ebf3_wire_feeder_feedthrough_connector` | Wire feeder | Penetrates chamber boundary and overlaps controls/power wiring. | Keep as feeder-specific feedthrough insert/interface marker. | Cabin owns passive port; controls own acquisition; power supplies own driver outputs. Final pinout, connector family, ratings, and service boundary remain deferred. |
| `ebf3_positioning_electrical_feedthrough` | Four-axis positioning system | Penetrates chamber boundary. | Keep positioning-specific feedthrough insert in positioning system. | Cabin owns generic port/flange; split if physical BOM shows shared multi-pin feedthrough. |
| `ebf3_vacuum_compatible_motor_cabling` | Four-axis positioning system | Could be counted as controls harness. | Keep if cabling is inside/attached to motion package. | Controls owns external command/signal cabinet harness. |
| `ebf3_signal_cabling` | Four-axis positioning system | Generic name overlaps with controls. | Keep only if it is positioner sensor/motor signal cabling. | Rename or note as positioning signal cabling in a later cleanup. |
| `ebf3_wire_feeder_mount_to_gun_bracket` | Wire feeder | Mechanical interface to electron gun. | Keep in wire feeder if removable feeder package includes the bracket. | If bracket is integral to gun column or cabin port, split gun-side/cabin-side datum accordingly. |
| `ebf3_cabin_gun_mounting_port` | Manufacture cabin | Directly interfaces with gun. | Keep in cabin as the chamber-side structural port. | Electron gun owns gun column/flange that mates to this port. |
| `ebf3_cabin_wire_feeder_mounting_port` | Manufacture cabin | Directly interfaces with wire feeder. | Keep in cabin as the chamber-side passive mounting port/datum. | Wire feeder owns removable bracket and feeder-side hardware. |
| `ebf3_beam_current_return_strap` | Four-axis positioning system | Could be mistaken for a complete HV return bus. | Keep as platform/substrate beam-current continuity hardware only. | System-level return conductor/topology remains deferred in `hv_grounding_return_review`. |
| `ebf3_hv_tank_grounding_terminal` | High voltage tank | Could be mistaken for beam-current return. | Keep as protective tank bonding terminal only. | Do not hide beam-current return or HV source reference inside this item. |
| `ebf3_hv_output_return_current_monitor` | High voltage tank | Current sensor may sit on output or return leg. | Keep HV-side primary monitor in HV tank, type unresolved. | Low-voltage acquisition belongs to controls; shunt/CT/Hall topology deferred. |
| `ebf3_gun_side_sensing_signal_wiring` | Fixed electron beam gun | Signal wiring ends in controls. | Keep gun-side pickups/internal wiring in electron gun. | Controls owns DAQ and external signal processing. |

## Current Recommendation

No subsystem YAML should be removed solely because closure errors increased.
The increase is expected after adding high-fidelity leaf items without local
recipes. Deletion or movement should be based on boundary ambiguity, duplicate
ownership, or source evidence that an item belongs in another physical package.

For the report, keep all seven subsystems in place and describe them as a
fidelity scaffold. The next cleanup should be limited to clarifying ambiguous
interface item names and notes, not collapsing the BOM back into lower-resolution
parts.

Current interface ownership is summarized in
`research/ebf3_bom_sources/organized/ebf3_interface_architecture.md`. Use the
older focused boundary reviews as evidence/detail files, not as separate current
entry points.

## Next Work Items

1. Add short boundary notes to the highest-risk interface YAML items listed above.
2. Rename generic items only when the name causes ownership ambiguity, for
   example `ebf3_signal_cabling` to `ebf3_positioning_signal_cabling`.
3. Split chamber penetrations into cabin-side ports and subsystem-side
   feedthrough inserts when source detail supports it.
4. Begin leaf decomposition from the fixed electron beam gun, because it has the
   clearest source-backed hierarchy and the highest risk of fidelity loss if
   mapped too early to generic KB parts.
5. Keep no_recipe closure gaps open until each leaf item has a bottom-level
   decomposition or an explicit import/commercial-component decision.
