# ebf3_wire_feeder Mapping

Authority note: this is a first-pass scaffold mapping from a user-derived table.
It preserves candidate item IDs and high-level modeling intent, but it is not a
decomposition planning file and cannot by itself justify child BOM creation,
material selection, recipe closure, or local manufacturability.

Wire feeder leaf items mapped from the wire feeder source table; no leaf recipes yet to preserve fidelity.

| Source ID | Item ID | Modeling decision |
| --- | --- | --- |
| WF-1 | `ebf3_wire_spool` | Wire spool holding feedstock wire before feeding. |
| WF-2 | `ebf3_spool_hub` | Hub supporting spool bore and rotation. |
| WF-3 | `ebf3_spool_support_shaft` | Support shaft for spool hub rotation. |
| WF-4 | `ebf3_spool_retaining_ring` | Retaining ring preventing spool/hub axial displacement. |
| WF-5 | `ebf3_spool_brake_washer` | Brake washer adding friction to prevent spool overrun. |
| WF-6 | `ebf3_spool_brake_adjuster` | Spool tension nut or adjustment hardware for spool brake force. |
| WF-7 | `ebf3_wire_feed_gearmotor` | Wire feed drive gearmotor assembly. |
| WF-8 | `ebf3_wire_feed_motor_clamp_insulator` | Insulating clamp component for motor/electrical isolation. |
| WF-9 | `ebf3_wire_feed_motor_mount_clamp` | Clamp or bracket holding feed motor in position. |
| WF-10 | `ebf3_drive_roll_carrier` | Carrier holding each drive roll in position. |
| WF-11 | `ebf3_drive_roll_carrier_spacer` | Spacer maintaining drive-roll carrier alignment. |
| WF-12 | `ebf3_wire_feed_drive_roll` | Drive roll converting motor torque into feed force. |
| WF-13 | `ebf3_wire_feed_pressure_arm` | Pressure-arm assembly applying force between wire and drive rolls. |
| WF-14 | `ebf3_pressure_adjustment_knob` | Knob or adjuster setting drive-roll pressure. |
| WF-15 | `ebf3_pressure_spring` | Spring providing drive-roll pressure force. |
| WF-16 | `ebf3_wire_inlet_guide` | Inlet guide positioning wire into the drive-roll area. |
| WF-17 | `ebf3_intermediate_wire_guide` | Intermediate guide between wire-feed regions. |
| WF-18 | `ebf3_wire_outlet_guide_tube` | Outlet wire guide toward the liner or downstream guide. |
| WF-19 | `ebf3_anti_wear_guide` | Anti-wear guide insert near the drive rolls. |
| WF-20 | `ebf3_feed_liner` | Replaceable downstream feed liner or guide tube. |
| WF-21 | `ebf3_ebf_wire_guide_tip` | Final EBF wire guide tip near the melt pool. |
| WF-22 | `ebf3_gun_feeder_adapter` | Adapter between feeder output and gun-side/downstream guide interface. |
| WF-23 | `ebf3_wire_feed_encoder_sensor` | Digital tachometer, encoder, or feed-rate sensor. |
| WF-24 | `ebf3_wire_feeder_base` | Structural base plate for the feeder. |
| WF-25 | `ebf3_wire_feeder_base_stiffener` | Base stiffener plate or rib. |
| WF-26 | `ebf3_drive_roll_cover` | Cover for drive-roll area. |
| WF-27 | `ebf3_wire_feeder_mount_to_gun_bracket` | Bracket mounting feeder to fixed electron beam gun. |

Deferred source-related candidates:

- `ebf3_wire_feed_pressure_roll`
- `ebf3_wire_feed_roll_bearing_set`
- `ebf3_wire_feed_drive_gear_set`
- `ebf3_wire_feed_idler_arm`
- `ebf3_wire_feed_spring_tensioner`
- `ebf3_wire_straightener_guides`
- `ebf3_wire_feed_nozzle`
- `ebf3_wire_feeder_body`
- `ebf3_wire_feeder_cover`
- `ebf3_wire_feeder_vacuum_motor_wiring`
- `ebf3_wire_feeder_feedthrough_connector`
- `ebf3_wire_feeder_fasteners_small`

See `research/ebf3_bom_sources/organized/wire_feeder_level_2_audit.md` for the
source-table correction and boundary rationale.

Masses are first-pass allocations constrained to the current subsystem mass. Leaf items intentionally have no local recipes yet.
