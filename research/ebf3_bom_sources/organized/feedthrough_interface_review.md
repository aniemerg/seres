# Feedthrough Interface Review

Status: boundary review completed for current Level-2 scaffold.

Current interface entry point:
`research/ebf3_bom_sources/organized/ebf3_interface_architecture.md`.

Purpose:

- Decide current ownership for chamber ports, feedthrough inserts, HV cable
  terminations, motor/signal cabling, and acquisition/control interfaces.
- Prevent one generic feedthrough item from hiding gun, wire-feeder,
  positioning, controls, power-supply, or high-voltage-tank details.
- Preserve uncertainty where the physical feedthrough geometry is not sourced.

Source registry:

- `research/ebf3_bom_sources/sources/level_2_parts/feedthrough_interfaces/feedthrough_interface_sources.md`

Related reviews:

- `research/ebf3_bom_sources/derived/ebf3_subsystem_boundaries.md`
- `research/ebf3_bom_sources/organized/hv_tank_interface_review.md`
- `research/ebf3_bom_sources/organized/hv_electrical_interface_review.md`
- `research/ebf3_bom_sources/organized/manufacture_cabin_level_2_audit.md`
- `research/ebf3_bom_sources/organized/wire_feeder_level_2_audit.md`
- `research/ebf3_bom_sources/organized/four_axis_positioning_level_2_audit.md`

## Boundary Rule

Use this split unless a later source shows a real integrated part:

| Physical/function layer | Owning subsystem |
| --- | --- |
| Chamber wall opening, passive port, flange, bracket, or viewport | Manufacture cabin |
| Subsystem-specific vacuum feedthrough insert or connector body | The subsystem using the feedthrough |
| Main inter-subsystem HV cable body | High-voltage tank |
| Tank-side HV bushing/socket/termination | High-voltage tank |
| Gun-side HV receiving terminal/feedthrough/input | Fixed electron beam gun |
| Local in-chamber motor/sensor wiring attached to a motion or feeder package | That motion or feeder subsystem |
| External low-voltage acquisition, command logic, and interlock decisions | Controls |
| Motor/coil/current power source electronics | Power supplies |

## Source Use

### RAW-NASA-EBF-PATENT

Evidence:

- "at least one electrical feed-through"
- "electrical feed-throughs 24 that penetrate the wall"
- "connecting sensors and motors"
- "wire feed subsystem"
- "positioning Subsystem"

Use:

- Supports electrical feedthroughs as real chamber-boundary hardware.
- Does not make one generic feedthrough item the owner of subsystem-specific
  inserts, signal conditioning, motor power, or chamber-side ports.

### RAW-EBF-SPACE

Evidence:

- "electron beam gun is inserted through the top"
- "positioning system is attached to the floor"
- "wire feeder is attached to the electron beam gun"

Use:

- Supports separate mechanical interfaces for gun, positioning, and wire feeder.
- Does not define electrical feedthrough geometry.

### RAW-BINP-60KEV-30KW

Evidence:

- "14-high voltage input"
- "beam current, cathode heat current"
- "pick-up of beam boundary"
- "pick-up of secondary electrons"

Use:

- Supports gun-side HV input and gun-side diagnostic/signal wiring.
- Does not assign external DAQ or controls to the gun.

### RAW-BINP-60KV-15KW-HV-TANK

Evidence:

- "voltage cable"
- "Output voltage"
- "controller measured 7 analogue channels"

Use:

- Supports HV tank cable/output sensing and controls acquisition boundary.
- Does not move gun-side receiving input into the HV tank.

## Decision Matrix

| Item or interface | Decision | Rationale |
| --- | --- | --- |
| `ebf3_cabin_feedthroughs_and_wiring_ports` | Keep deferred; do not place in top-level cabin BOM now. | Real feedthroughs exist, but the generic item would duplicate feeder, positioning, gun, controls, and power/HV interfaces. |
| `ebf3_positioning_electrical_feedthrough` | Keep in positioning as FS-30 subsystem-specific feedthrough interface. | Source table has a positioning feedthrough row; cabin owns only the chamber-side opening/flange and controls own acquisition. |
| `ebf3_wire_feeder_feedthrough_connector` | Keep in wire feeder as feeder-specific feedthrough insert/interface marker. | Interface architecture now separates this insert from cabin passive ports, controls acquisition, and power-supply driver outputs. |
| `ebf3_gun_signal_wiring` | Keep in fixed gun as local pickups, internal wiring, and gun-diagnostic feedthrough/shield interface markers. | Gun diagnostics and local signal boundary hardware belong with the gun; DAQ, logic, cabinet harnessing, and chamber passive ports belong elsewhere. |
| `ebf3_gun_hv_input` | Keep in fixed gun as gun-side HV receiving/input hardware. | It is not the tank-side bushing, not the main cable body, and not a generic cabin port. |
| `ebf3_tank_side_hv_output_bushing` | Keep in HV tank. | Tank wall/oil-side HV output interface belongs with the HV tank. |
| `ebf3_hv_cable_to_gun` | Keep in HV tank. | Main HV transmission cable is owned by the HV source package until terminations are decomposed. |
| `ebf3_cabin_gun_mounting_port` | Keep in cabin. | Chamber-side structural port/flange only; gun column and gun HV input remain with fixed gun. |
| `ebf3_cabin_wire_feeder_mounting_port` | Keep in cabin. | Chamber-side passive datum only; feeder bracket, connector, and mechanism remain with wire feeder. |
| `ebf3_vacuum_compatible_motor_cabling` | Keep in positioning only for in-package/in-chamber motor cabling. | Power supplies own driver outputs; controls own commands. |
| `ebf3_vacuum_compatible_signal_cabling` | Keep in positioning only for in-package/in-chamber sensor cabling. | Controls own acquisition and signal conditioning. |

## Current KB Action

- Do not create a general `cabin feedthrough assembly` at top level.
- Do not add recipes or local closure.
- Keep the current top-level BOMs concise; feedthrough details should be
  introduced only inside the owning subsystem child decomposition.
- Update item notes so reviewers can see the boundary decision from Simviewer.

## Next Unblock Conditions

| Deferred item | What would unblock it |
| --- | --- |
| `ebf3_cabin_feedthroughs_and_wiring_ports` | A source or design decision showing a specific chamber-side port set or shared feedthrough plate. |
| `ebf3_wire_feeder_feedthrough_connector` final details | Source or design selection for exact pinout, connector family, current/signal ratings, shield policy, ceramic-to-metal construction, and service boundary. |
| `ebf3_gun_signal_wiring` final details | Source or design selection for coax/multipin/shared-plate topology, pinout, shield-ground policy, and controls-side acquisition boundary. |
| `ebf3_gun_hv_input` / `ebf3_gun_hv_insulator` final details | Source or design selection for exact connector geometry, final ceramic feedthrough integration, field-grading shape/potential, HV ratings, and service boundary. |
| `ebf3_positioning_electrical_feedthrough` final details | Source or design selection for exact pinout, connector family, current/voltage ratings, shield policy, ceramic-to-metal construction, and service boundary. |

## Manufacturing Readiness

No feedthrough/interface item is local-ready. Vacuum sealing, ceramic-to-metal
joining, high-voltage clearance, pin rating, shielding, outgassing, creepage,
connector compatibility, leak testing, and electrical test requirements all need
separate material/process readiness review.
