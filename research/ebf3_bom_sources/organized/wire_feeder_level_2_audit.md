# Wire Feeder Level-2 Audit

Status: review completed; source-table aligned BOM correction applied.

Purpose:

- Compare current wire-feeder BOM leaves against the source table and available
  source evidence.
- Preserve boundaries between wire feeder, manufacture cabin, fixed gun,
  controls, and power supplies.
- Keep wire-feed mechanism items separate from feedstock material, control
  electronics, chamber ports, and gun-side datums.

Source registry:

- `research/ebf3_bom_sources/sources/level_1_subsystems/wire_feeder/wire_feeder_sources.md`

Related boundary reviews:

- `research/ebf3_bom_sources/derived/ebf3_subsystem_boundaries.md`
- `research/ebf3_bom_sources/organized/manufacture_cabin_level_2_audit.md`
- `research/ebf3_bom_sources/organized/controls_level_2_audit.md`

## Source Use

### RAW-EBF-PATENT

Evidence:

- "wire feed subsystem"
- "wire feed housing"
- "drive roll"
- "feed stock guide means"
- "wire feed-rate sensing"
- "mounted to the electron beam gun"
- "at least one electrical feed-through"

Use:

- Supports a wire-feeder mechanism, housing/base, drive roll, feed guide path,
  feed-rate feedback, gun/feeder mounting interface, and electrical feedthrough
  concept.
- Does not fix detailed Miller-style part geometry or vacuum-rated materials.

### RAW-EBF-SPACE

Evidence:

- "standard 100 mm diameter welding wire spools"
- "wire feeder is attached to the electron beam gun"
- "wire is fed into a molten pool"

Use:

- Supports the spool, gun/feeder interface, and final wire guide/nozzle function.

### LOCAL-EBF3-WIRE-FEEDER-TABLE

Use:

- Introduces WF-1 through WF-27 candidates and cites external feeder manuals or
  vendor guidance for many detailed parts.
- Candidate-only until cited external sources are archived or independently
  checked.

## Main Finding

The current wire-feeder BOM had the right number of rows, but WF-10 through
WF-27 were mostly shifted or represented by older functional placeholders. This
made the top-level BOM look detailed while no longer matching the source table.

The correction below makes the top-level BOM row-for-row reviewable against
WF-1 through WF-27. Older items are kept as deferred candidates where they may
belong in later child BOMs.

## Level-2 Decision Matrix

| Source table row | Current or recommended item | Decision | Rationale |
| --- | --- | --- | --- |
| WF-1 wire spool | `ebf3_wire_spool` | keep | Space paper supports standard welding-wire spools; feedstock material inventory remains separate. |
| WF-2 spool hub | `ebf3_spool_hub` | keep | Source table and feeder mechanics support a hub. |
| WF-3 spool support shaft | `ebf3_spool_support_shaft` | keep | Source table supports shaft; material unresolved. |
| WF-4 spool retaining ring | `ebf3_spool_retaining_ring` | keep | Source table supports retaining ring. |
| WF-5 spool brake washer | `ebf3_spool_brake_washer` | keep | Source table supports brake washer. |
| WF-6 spool tension nut | `ebf3_spool_brake_adjuster` | keep / retag wording | Same function; keep current item ID but note tension-nut wording. |
| WF-7 gearmotor | `ebf3_wire_feed_gearmotor` | keep | Source table and patent support motorized wire feed. |
| WF-8 motor clamp insulator | `ebf3_wire_feed_motor_clamp_insulator` | keep | Source table supports item; vacuum material unresolved. |
| WF-9 motor base clamp | `ebf3_wire_feed_motor_mount_clamp` | keep | Source table supports item. |
| WF-10 drive roll carrier | `ebf3_drive_roll_carrier` | corrected | Current row had inlet guide; add source-row item. |
| WF-11 drive roll carrier spacer | `ebf3_drive_roll_carrier_spacer` | corrected | Use explicit carrier-spacer item instead of generic spacer. |
| WF-12 drive roll | `ebf3_wire_feed_drive_roll` | keep | Patent and source table support drive roll. |
| WF-13 pressure arm | `ebf3_wire_feed_pressure_arm` | corrected | Current row had pressure roll; source row is an arm assembly. |
| WF-14 pressure adjustment knob | `ebf3_pressure_adjustment_knob` | corrected | Source row is adjustment knob. |
| WF-15 pressure spring | `ebf3_pressure_spring` | corrected | Source row is pressure spring. |
| WF-16 inlet wire guide | `ebf3_wire_inlet_guide` | corrected row position | Existing item retained and retagged to WF-16. |
| WF-17 intermediate wire guide | `ebf3_intermediate_wire_guide` | corrected | Add source-row guide item. |
| WF-18 outlet wire guide | `ebf3_wire_outlet_guide_tube` | corrected row position | Existing outlet guide retained and retagged to WF-18. |
| WF-19 anti-wear guide | `ebf3_anti_wear_guide` | corrected | Add source-row wear guide item. |
| WF-20 feed liner | `ebf3_feed_liner` | corrected | Add source-row liner item; conventional polymer liners remain material-unresolved. |
| WF-21 EBF wire guide tip | `ebf3_ebf_wire_guide_tip` | corrected | Source row is final guide tip, not the feeder body. |
| WF-22 gun/feeder adapter | `ebf3_gun_feeder_adapter` | corrected | Add adapter; separate from chamber-side or gun-side permanent datum. |
| WF-23 digital tachometer/feed-rate encoder | `ebf3_wire_feed_encoder_sensor` | corrected row position | Existing encoder item retained and retagged to WF-23. |
| WF-24 wire feeder base | `ebf3_wire_feeder_base` | corrected | Source row is base, not feedthrough connector. |
| WF-25 base stiffener | `ebf3_wire_feeder_base_stiffener` | corrected | Add source-row stiffener. |
| WF-26 drive-roll cover | `ebf3_drive_roll_cover` | corrected | Source row is drive-roll cover, not gun bracket. |
| WF-27 mounting bracket to fixed electron beam gun | `ebf3_wire_feeder_mount_to_gun_bracket` | corrected row position | Existing bracket retained and retagged to WF-27. Cabin owns chamber-side port only. |

## Deferred Candidates

| Candidate item | Why not in top-level wire-feeder BOM now | Next unblock condition |
| --- | --- | --- |
| `ebf3_wire_feed_pressure_roll` | Not a source-table top-level row; may belong under drive-roll/pressure-arm child decomposition. | Reintroduce during drive-roll mechanism decomposition. |
| `ebf3_wire_feed_roll_bearing_set` | Plausible child detail but not a source-table top-level row. | Reintroduce during drive-roll carrier decomposition if source-supported. |
| `ebf3_wire_feed_drive_gear_set` | Gear details may be inside gearmotor or drive mechanism; top-level source row is gearmotor. | Reintroduce only after gearmotor/drive transmission review. |
| `ebf3_wire_feed_spacer` | Replaced by the source-table aligned drive-roll carrier spacer. | Reintroduce only if a later child assembly needs a broader spacer. |
| `ebf3_wire_feed_idler_arm` | Older placeholder overlaps with pressure arm. | Use only if child decomposition separates idler arm from pressure arm. |
| `ebf3_wire_feed_spring_tensioner` | Older placeholder overlaps with pressure spring and pressure adjustment knob. | Reintroduce only if tensioner assembly is source-confirmed. |
| `ebf3_wire_straightener_guides` | Not in the current source-table top-level list. | Reintroduce only if a source confirms a separate straightener in this feeder. |
| `ebf3_wire_feed_nozzle` | Overlaps with EBF wire guide tip and gun/feeder adapter. | Reintroduce only after the downstream guide/nozzle boundary is source-fixed. |
| `ebf3_wire_feeder_body` | Source row is base; body/housing may be a later base child. | Reintroduce under feeder base decomposition. |
| `ebf3_wire_feeder_cover` | Source row is drive-roll cover; general cover may be a later child. | Reintroduce under drive-roll cover/body decomposition if needed. |
| `ebf3_wire_feeder_vacuum_motor_wiring` | Wiring is real but crosses feedthrough/power/control boundaries. | Reintroduce after feedthrough and motor-power interface review. |
| `ebf3_wire_feeder_feedthrough_connector` | Feedthrough is real but must be split from chamber-side port and controls/power wiring. | Reintroduce after feedthrough-interface review. |
| `ebf3_wire_feeder_fasteners_small` | Generic fasteners are likely child details, not source-table top-level rows. | Reintroduce under specific assemblies when fastener fidelity is needed. |

## Applied BOM Correction

- Rebuilt the top-level wire-feeder BOM so its 27 components map directly to
  WF-1 through WF-27.
- Added missing source-row items and retagged existing kept items.
- Kept shifted older placeholders as deferred candidates, not deleted.
- Kept first-pass component mass allocation for current recipe mass balance;
  this audit does not claim sourced masses for corrected wire-feeder leaves.

## Manufacturing Readiness

No wire-feeder item is local-ready. Vacuum-rated motors, encoders, feedthroughs,
low-outgassing insulation, drive-roll geometry, guide materials, liner
compatibility, precision alignment, and wear testing all need separate
material/process readiness review before recipes are attached.
