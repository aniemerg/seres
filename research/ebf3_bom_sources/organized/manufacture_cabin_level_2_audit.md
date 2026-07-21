# Manufacture Cabin Level-2 Audit

Status: review completed; source-table aligned BOM correction applied.

Purpose:

- Compare current manufacture-cabin BOM leaves against the source table and
  available source evidence.
- Preserve boundaries between the cabin, fixed gun, wire feeder, positioning
  system, controls, and vacuum/electrical feedthroughs.
- Keep the cabin as the passive vacuum/process envelope and structural interface
  package; do not hide subsystem-specific inserts, sensors, motors, cameras, or
  power electronics inside cabin items.

Source registry:

- `research/ebf3_bom_sources/sources/level_1_subsystems/manufacture_cabin/manufacture_cabin_sources.md`

Related boundary reviews:

- `research/ebf3_bom_sources/derived/ebf3_subsystem_boundaries.md`
- `research/ebf3_bom_sources/organized/controls_level_2_audit.md`
- `research/ebf3_bom_sources/organized/gun_column_decomposition_plan.md`

## Source Use

### RAW-EBF-SPACE

Evidence:

- "vacuum chamber is a 900 mm cube"
- "constructed of aluminum"
- "chamber walls provide adequate radiation shielding"
- "electron beam gun is inserted through the top"
- "positioning system is attached to the floor"

Use:

- Supports chamber shell/walls, gun mounting port, and floor/interface support
  for the positioning system.
- Does not define detailed door, viewport, lighting, feedthrough, or wire-feeder
  port construction.

### RAW-NASA-EBF-PATENT

Evidence:

- "a frame"
- "at least one wall"
- "at least one window"
- "at least one door"
- "at least one electrical feed-through"
- "mounting the wire feed subsystem"
- "means for providing protective shielding"
- "means for lighting"

Use:

- Supports frame, wall, window/viewport, door, electrical feedthrough concept,
  wire-feeder mounting interface, protective shield/liner, and lighting as real
  cabin-related functions.
- Does not require the cabin to own powered cameras, central lighting controls,
  feeder connector inserts, or positioning/gun internals.

### LOCAL-EBF3-MANUFACTURE-CABIN-TABLE

Use:

- Introduces MC-1 through MC-9 candidates.
- Candidate-only; it cannot justify recipes, materials, or child BOMs by itself.

## Main Finding

The current manufacture-cabin BOM had two top-level mismatches:

- Table row MC-6 is **wire-feeder mounting port**, but the current BOM had
  `ebf3_cabin_build_substrate_support`.
- Table row MC-9 is **chamber lighting fixture**, but the current BOM had
  `ebf3_cabin_feedthroughs_and_wiring_ports`.

Both older items are plausible lower-level or interface candidates, but they
should not replace the source-table top-level rows. This audit corrected the
Level-2 BOM presentation and left uncertain boundary details open.

## Level-2 Decision Matrix

| Source table row | Current or recommended item | Decision | Rationale |
| --- | --- | --- | --- |
| MC-1 chamber frame | `ebf3_cabin_frame` | keep | Patent supports a frame; cabin owns the chamber structure. |
| MC-2 chamber wall panel | `ebf3_cabin_wall_panels` | keep | Space paper and patent support aluminum chamber walls. |
| MC-3 chamber access door | `ebf3_cabin_access_door` | keep | Patent supports a door in the sealed container. |
| MC-4 chamber viewport | `ebf3_cabin_viewport` | keep | Patent supports a window for visibility/cameras. |
| MC-5 electron-gun mounting port | `ebf3_cabin_gun_mounting_port` | keep with boundary note | Cabin owns the chamber-side port; gun owns gun column/flange details. |
| MC-6 wire-feeder mounting port | `ebf3_cabin_wire_feeder_mounting_port` | corrected | Patent supports mounting the wire feed subsystem to the container; feeder-side removable bracket remains in wire feeder. |
| MC-7 interior sacrificial shield | `ebf3_cabin_sacrificial_liner` | keep | Patent supports protective shielding; material and geometry remain unresolved. |
| MC-8 build-table access and positioning-system floor interface | `ebf3_cabin_positioning_mount_interface` | keep / retag wording | Space paper supports positioning system attached to the chamber floor. Positioning hardware remains in the positioning subsystem. |
| MC-9 chamber lighting fixture | `ebf3_cabin_lighting_mount_and_port` | corrected / split boundary | Patent supports lighting. Cabin owns passive mounts, window/port, and chamber-side penetration; powered light hardware remains deferred until monitoring/cabin review. |

## Deferred Candidates

| Candidate item | Why not in top-level cabin BOM now | Next unblock condition |
| --- | --- | --- |
| `ebf3_cabin_build_substrate_support` | Build substrate/platform details are more likely part of positioning or later process tooling; MC-8 is better represented as a chamber floor/interface item. | Reintroduce only if a cabin-specific passive support is source-confirmed separate from the positioning platform. |
| `ebf3_cabin_feedthroughs_and_wiring_ports` | Primary source supports electrical feedthroughs, but this generic item can duplicate gun, wire-feeder, positioning, and controls feedthrough inserts. | Reintroduce after a feedthrough-interface review splits chamber-side ports from subsystem-specific inserts. |
| `ebf3_process_monitor_lighting` | Lighting is real, but powered lighting/electronics ownership is still unresolved between controls and cabin. | Reintroduce under controls or a lighting child BOM after monitoring/cabin interface review. |

## Applied BOM Correction

- Replaced `ebf3_cabin_build_substrate_support` with
  `ebf3_cabin_wire_feeder_mounting_port` at MC-6.
- Replaced `ebf3_cabin_feedthroughs_and_wiring_ports` with
  `ebf3_cabin_lighting_mount_and_port` at MC-9.
- Kept `ebf3_cabin_build_substrate_support` and
  `ebf3_cabin_feedthroughs_and_wiring_ports` as deferred candidates, not
  deleted.
- Kept first-pass component mass allocation for current recipe mass balance;
  this audit does not claim sourced masses for the corrected cabin leaves.

## Manufacturing Readiness

No manufacture-cabin item is local-ready. Vacuum chamber fabrication, radiation
shielding adequacy, sealed doors, viewports, feedthroughs, alignment datums,
cleanliness, leak testing, lighting vacuum compatibility, and subsystem
interface geometry all need separate material/process readiness review before
recipes are attached.
