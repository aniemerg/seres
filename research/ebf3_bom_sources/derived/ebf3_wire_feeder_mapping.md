# ebf3_wire_feeder Mapping

Authority note: this is a first-pass scaffold mapping from a user-derived table.
It preserves candidate item IDs and high-level modeling intent, but it is not a
decomposition planning file and cannot by itself justify child BOM creation,
material selection, recipe closure, or local manufacturability.

Wire feeder leaf items mapped from V2_wire_feeder_item_table; no leaf recipes yet to preserve fidelity.

| Source ID | KB item ID | Modeling decision |
| --- | --- | --- |
| WF-1 | `ebf3_wire_spool` | Wire spool holding feedstock wire before feeding. |
| WF-2 | `ebf3_spool_hub` | Hub supporting spool bore and rotation. |
| WF-3 | `ebf3_spool_support_shaft` | Support shaft for spool hub rotation. |
| WF-4 | `ebf3_spool_retaining_ring` | Retaining ring preventing spool/hub axial displacement. |
| WF-5 | `ebf3_spool_brake_washer` | Brake washer adding friction to prevent spool overrun. |
| WF-6 | `ebf3_spool_brake_adjuster` | Adjustment hardware for spool brake force. |
| WF-7 | `ebf3_wire_feed_gearmotor` | Wire feed drive gearmotor assembly. |
| WF-8 | `ebf3_wire_feed_motor_clamp_insulator` | Insulating clamp component for motor/electrical isolation. |
| WF-9 | `ebf3_wire_feed_motor_mount_clamp` | Clamp or bracket holding feed motor in position. |
| WF-10 | `ebf3_wire_inlet_guide` | Inlet guide positioning wire into feed path. |
| WF-11 | `ebf3_wire_feed_spacer` | Spacer maintaining feed mechanism alignment. |
| WF-12 | `ebf3_wire_feed_drive_roll` | Drive roll converting motor torque into feed force. |
| WF-13 | `ebf3_wire_feed_pressure_roll` | Pressure/idler roll clamping wire against drive roll. |
| WF-14 | `ebf3_wire_feed_roll_bearing_set` | Bearing set for feed rolls. |
| WF-15 | `ebf3_wire_feed_drive_gear_set` | Gear set transmitting gearmotor torque to feed rolls. |
| WF-16 | `ebf3_wire_feed_idler_arm` | Idler arm holding pressure roll and adjustment hardware. |
| WF-17 | `ebf3_wire_feed_spring_tensioner` | Spring tensioner controlling wire pinch force. |
| WF-18 | `ebf3_wire_straightener_guides` | Guide or straightener hardware smoothing wire path. |
| WF-19 | `ebf3_wire_outlet_guide_tube` | Outlet guide tube for wire after drive rolls. |
| WF-20 | `ebf3_wire_feed_nozzle` | Nozzle delivering feedstock wire to target location. |
| WF-21 | `ebf3_wire_feeder_body` | Main structural body/housing for wire feeder mechanism. |
| WF-22 | `ebf3_wire_feeder_cover` | Protective cover for feeder mechanism. |
| WF-23 | `ebf3_wire_feeder_vacuum_motor_wiring` | Vacuum-compatible motor wiring and strain relief. |
| WF-24 | `ebf3_wire_feeder_feedthrough_connector` | Electrical feedthrough/connector for feeder motor and sensor wiring. |
| WF-25 | `ebf3_wire_feed_encoder_sensor` | Encoder or feed-rate sensor for wire feed feedback. |
| WF-26 | `ebf3_wire_feeder_mount_to_gun_bracket` | Bracket mounting feeder to electron gun or chamber interface. |
| WF-27 | `ebf3_wire_feeder_fasteners_small` | Small fasteners and retaining hardware for feeder assembly. |

Masses are first-pass allocations constrained to the current subsystem mass. Leaf items intentionally have no local recipes yet.
