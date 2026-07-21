# EBF3 Machine Decomposition Status

Purpose: concise completion record for the whole EBF3 machine BOM. This file
tells reviewers what has actually been decomposed, what is intentionally still a
leaf, and where boundary risks remain.

Modeling policy:

- Preserve fidelity before closure.
- Keep closure gaps open until a leaf has a source-supported decomposition or a
  deliberate import/commercial-component decision.
- Do not attach local recipes to EBF3 leaves from this status file.
- Use this file to choose the next review target, not to justify new child BOMs.

Acceptance criteria for this execution pass:

- A Level-2 row is acceptable when it is source/table-aligned, explicitly
  boundary-owned, or intentionally deferred as a marker.
- A Level-2 leaf is acceptable only when the KB item note says why it is a
  software, material, single-piece precision part, small hardware part, or
  unresolved boundary marker.
- A Level-3 package split is acceptable when assembly-like Level-2 rows have
  child BOMs without claiming final geometry, electrical ratings, local
  manufacturability, or recipes.

Current validation posture:

- Last checked after cathode lunar-material review: validation issues were 0.
- Closure errors remain expected because many high-fidelity leaves intentionally
  have no local recipes.

Current high-suspicion audit result:

- No child item currently visible in the seven-subsystem EBF3 BOM was found to
  be retained solely as a weak, unsupported, or user-table-only child split.
- Previously over-specific gun-side oil-tank children and HV tank mounting/support
  children have been removed or returned to deferred status.
- Deferred standalone candidate items may still exist as KB YAML records, but
  they are not part of the active EBF3 BOM unless an owning BOM references them.

Current execution result:

- The seven EBF3 subsystem Level-2 BOMs are in a trusted presentation state for
  the current evidence set after source-row cleanup and KB leaf-note hardening.
- Assembly-like Level-2 rows have received Level-3 package child BOMs where the
  sources and boundary rules justify them.
- Remaining Level-2 leaves are intentional leaves, unresolved boundary markers,
  or items that need architecture/material/process decisions before deeper
  splitting.
- Cross-subsystem interface ownership now uses
  `organized/ebf3_interface_architecture.md` as the current readable entry
  point. That file selects ownership paths only; geometry, ratings, pinouts, and
  material/process readiness remain deferred.

## Whole-Machine Structure

| Level | Item | BOM children | Status |
| --- | --- | ---: | --- |
| Machine | `ebf3_3d_printer` | 7 | Seven-subsystem scaffold in place. |
| Subsystem | `ebf3_controls` | 13 | Level-2 trusted; 12 assembly-like rows have Level-3 package BOMs. `ebf3_control_software` remains an intentional software leaf. |
| Subsystem | `ebf3_power_supplies` | 15 | Level-2 trusted; all 15 rows have Level-3 package BOMs. Electrical ratings, semiconductor choice, and magnetic design remain deferred. |
| Subsystem | `ebf3_high_voltage_tank` | 15 | Level-2 trusted; 14 assembly-like rows have Level-3 package BOMs. `ebf3_hv_transformer_insulating_fluid` remains an intentional material leaf. |
| Subsystem | `ebf3_fixed_electron_beam_gun` | 19 | Level-2 trusted; 13 rows have Level-3 package BOMs, five precision/single-part rows remain leaves, and gun-side oil tank remains an unresolved boundary marker. |
| Subsystem | `ebf3_wire_feeder` | 28 | Level-2 trusted; 18 assembly-like rows have Level-3 package BOMs and ten small hardware rows remain intentional single-part leaves. The first 27 rows map to source-table feeder mechanics; the final row is the feeder-specific feedthrough insert. |
| Subsystem | `ebf3_four_axis_positioning_system` | 30 | Level-2 trusted; 27 assembly-like rows have Level-3 package BOMs and three precision metal rows remain intentional leaves. |
| Subsystem | `ebf3_manufacture_cabin` | 9 | Level-2 trusted; all nine passive cabin/interface rows have Level-3 package BOMs. Powered lighting and generic feedthrough inserts remain deferred. |

`source-table alignment` means current BOM rows have been aligned to the
user-provided subsystem tables and obvious row shifts/placeholders have been
removed or deferred. It does not mean each row has independent external-source
verification or local manufacturability.

## Subsystem Status

| Subsystem | Review file | Current state | Main deferred work after this phase |
| --- | --- | --- | --- |
| Controls | `organized/controls_level_2_audit.md` | Level-2 trusted and Level-3 package split complete for hardware rows. | Circuit schematics, firmware/software split, board-level component values, camera model, and electronics manufacturability. |
| Power supplies | `organized/power_supplies_level_2_audit.md` | Level-2 trusted and Level-3 package split complete for current rows. | Semiconductor device choice, magnetic design, capacitor chemistry, protection topology, insulation ratings, and electronics manufacturability. |
| High-voltage tank | `organized/high_voltage_tank_level_2_audit.md` | Level-2 trusted; section-module model adopted; Level-3 package split complete except the intentional insulating-fluid leaf. | Electrical ratings, field grading, service interlock, exact transformer/rectifier topology, and tank/gun termination geometry. |
| Fixed electron beam gun | `organized/fixed_electron_beam_gun_level_2_decomposition_audit.md` | Level-2 trusted; Level-3 package split complete for obvious assemblies. Refractory electrodes, tungsten cathode, and gun-side oil marker remain leaves; HV insulator is now a package split with details deferred. | Cathode dimensions/process, electrode geometry, ceramic grade, HV ratings, diagnostics feedthrough/DAQ, and source-backed material choices. |
| Wire feeder | `organized/wire_feeder_level_2_audit.md` | Level-2 trusted; Level-3 package split complete for assembly-like feeder rows. | Feedthrough split, final guide/nozzle material, drive-roll surface/profile process, motor internals, and vacuum-compatible motor/cable readiness. |
| Four-axis positioning | `organized/four_axis_positioning_level_2_audit.md` | Level-2 trusted; Level-3 package split complete for assembly-like positioning rows. | Precision motion manufacturing, encoder technology, motor internals, feedthrough/cabling, beam-current return topology, and bearing/screw process readiness. |
| Manufacture cabin | `organized/manufacture_cabin_level_2_audit.md` | Level-2 trusted; Level-3 passive mechanical split complete for current cabin rows. | Chamber feedthrough interface split, powered lighting ownership, port seals/fasteners, vacuum material selection, build-substrate/process-tooling boundary. |

## Active Interface Risks

These are the cross-subsystem issues most likely to create duplicate ownership
or misleading Simviewer structure if deeper decomposition starts too early. The
current ownership model is summarized in
`organized/ebf3_interface_architecture.md`.

| Interface | Current owner or split | Risk | Remaining detail |
| --- | --- | --- | --- |
| HV cable to gun | HV tank owns main cable and tank-side bushing/socket marker; gun owns gun-side HV input/receiving-terminal marker. | Cable termination can duplicate gun-side feedthrough or tank-side bushing if represented inside the cable body. | Exact connector/socket geometry, cable rating, creepage, and field grading. |
| Gun-side oil tank vs main HV tank | Gun keeps only an unresolved FG-18 marker; the main HV tank owns the confirmed fluid inventory. | Could be mistaken for a confirmed second oil tank or second bulk oil volume. | Source a separate gun oil volume before adding shell/oil/seal children. |
| Cabin feedthroughs | Cabin owns passive wall openings, ports, and flanges. | Generic feedthrough item can hide feeder, positioning, controls, or gun inserts. | Specific shared plate or subsystem insert geometry. |
| Wire feeder feedthrough | Wire feeder owns feeder-specific insert marker; cabin owns only passive opening. | Can duplicate chamber port, controls acquisition, or power wiring if modeled generically. | Exact pinout, connector family, ratings, and service boundary. |
| Positioning electrical feedthrough | Positioning owns subsystem-specific insert/interface; cabin owns passive wall port. | Can duplicate controls DAQ or power wiring. | Pinout, ceramic body, connector family, and motor/sensor channel split. |
| Process monitoring lighting | Cabin owns passive lighting mount/port; controls may own powered lighting/electronics later. | Can duplicate thermal/visible monitoring or chamber hardware. | Powered-light source, wiring, heat load, and camera/illumination ownership. |
| Beam-current return strap | Positioning owns platform/substrate continuity only. | Not a full system-level HV return bus. | Physical HV return topology and platform connection policy. |
| HV current monitor | HV tank owns primary HV-side monitor; controls own acquisition. | Sensor topology and return-leg placement unresolved. | Shunt/CT/Hall choice, insulation, ratings, and acquisition isolation. |
| Motion and wire-feed controls | Controls own command/acquisition; mechanisms stay in positioning/wire feeder; drive power stays in power supplies. | Control modules can be confused with motor drivers or local mechanism hardware. | Driver channel architecture, harness routing, and low-voltage signal isolation. |

## Interface Follow-Up Priority

Use this table to choose deeper decomposition targets. A split review can still
conclude "do not split yet".

| Priority | Scope | Candidate parents | Why this priority | Current action |
| --- | --- | --- | --- | --- |
| 1 | HV tank / fixed-gun interface | `ebf3_tank_side_hv_output_bushing`, `ebf3_hv_cable_to_gun`, `ebf3_gun_hv_input`, `ebf3_gun_hv_insulator` | Highest duplicate-ownership risk across HV tank and gun. | Tank-side bushing, cable body, gun-side input, standalone gun HV insulator, and local field-grading package markers are modeled; now resolve exact connector geometry, ceramic/feedthrough integration, oil-volume evidence, and HV ratings. |
| 2 | Diagnostics and signal path | `ebf3_gun_beam_boundary_pickup`, `ebf3_gun_secondary_electron_pickup`, `ebf3_gun_signal_wiring`, controls DAQ items | Affects gun, controls, cabin feedthroughs, and grounding. | Gun-side feedthrough/shield interface markers are modeled; now resolve coax/multipin/shared-plate topology, final shield policy, bias/suppression, DAQ channels, and isolation. |
| 3 | Power supplies internal electronics | `ebf3_full_bridge_inverter`, `ebf3_control_electrode_bias_supply`, `ebf3_cathode_heater_supply`, `ebf3_multi_channel_driver_module` | Defines drivers/current sources for gun loads and motion/feed systems. | Driver ownership selected; now resolve channel architecture, semiconductor choices, magnetics, protection, and ratings. |
| 4 | Positioning and wire-feeder feedthroughs | `ebf3_positioning_electrical_feedthrough`, `ebf3_wire_feeder_feedthrough_connector`, `ebf3_vacuum_compatible_motor_cabling`, `ebf3_vacuum_compatible_signal_cabling` | Can duplicate controls acquisition or power-driver outputs. | Positioning and feeder insert package markers are modeled; now resolve pinout, connector family, motor/sensor split, ratings, and cable materials. |
| 5 | Wire-feeder mechanism details | drive roll, pressure arm, guide/liner/tip, feeder mount bracket | Mechanically rich, but lower cross-subsystem risk than HV and controls. | Pressure-arm, drive-roll-carrier, feed-liner, and adapter child BOMs added; keep drive-roll profile, final guide tip/nozzle, feedthrough, and permanent gun/cabin interface deferred. |
| 6 | Cabin passive interfaces | frame, walls, door, viewport, liner, gun port, wire-feeder port, positioning mount, lighting mount/port | Cabin owns passive openings and mounts; powered inserts belong elsewhere. | Passive ownership selected; keep powered lighting, feedthrough inserts, seals/fasteners, and subsystem-side brackets as follow-up details. |
| 7 | Cathode cluster | `ebf3_gun_cathode`, heater leads, cartridge, radiation shield | High fidelity impact and local-closure impact. | Direct-heated tungsten hairpin/filament selected; minimal FG-14/FG-15 child BOMs added. Material/process and shield details remain deferred. |

## Recommended Next Work

1. Use `organized/ebf3_interface_architecture.md` as the current interface
   entry point for cabin, gun, wire feeder, positioning, controls, power
   supplies, and HV tank boundaries.
2. Update affected item notes when deeper child decomposition touches:
   `ebf3_cabin_feedthroughs_and_wiring_ports`,
   `ebf3_wire_feeder_feedthrough_connector`,
   `ebf3_positioning_electrical_feedthrough`,
   `ebf3_gun_signal_wiring`, and `ebf3_gun_hv_input`.
3. Fixed-gun cathode child BOMs now follow the direct-heated tungsten
   hairpin/filament package direction. Next cathode work should refine material,
   dimensions, contact/joint method, ceramic geometry, and whether a separate
   shield exists; do not add local recipes yet.
4. HV/cable geometry now has minimal package markers under HV-8, HV-9, FG-12,
   and FG-13. Exact connector geometry, ceramic/feedthrough integration,
   field-grading geometry, and HV ratings still need source or design selection.
5. Material/process readiness reviews come after ownership and decomposition are
   stable. Do not use generic lower-resolution local parts to close EBF leaves.

## Remaining Intentional Leaves

These Level-2 items do not currently need child BOMs unless later evidence shows
they are multi-part assemblies:

- `ebf3_control_software`
- `ebf3_hv_transformer_insulating_fluid`
- Gun refractory or ceramic precision parts: cathode, anode, control electrode,
  control-electrode insulator, and screen electrode.
- Small wire-feeder single-material parts: spool hub, support shaft, retaining
  ring, brake washer, motor clamp insulator, carrier spacer, pressure spring,
  inlet guide, outlet guide tube, base stiffener.
- Positioning single-piece or still architecture-dependent metal parts:
  positioning axis base plate, rotary worm wheel, rotary worm shaft.

The main unresolved work is now not "add a child BOM everywhere"; it is to
replace placeholder child splits with sourced geometry/material/process choices
where fidelity matters most.

## Review Rule

If a future change makes Simviewer simpler but hides one of the interface risks
above, keep the item deferred or split it across subsystem boundaries instead of
collapsing it into a generic component.
