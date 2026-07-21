# ebf3_manufacture_cabin Mapping

Authority note: this is a first-pass scaffold mapping from a user-derived table.
It preserves candidate item IDs and high-level modeling intent, but it is not a
decomposition planning file and cannot by itself justify child BOM creation,
material selection, recipe closure, or local manufacturability.

Manufacture cabin leaf items mapped from V1_manufacture cabin item table; no leaf recipes yet to preserve fidelity.

| Source ID | Item ID | Modeling decision |
| --- | --- | --- |
| MC-1 | `ebf3_cabin_frame` | Structural skeleton of the sealed manufacturing chamber. |
| MC-2 | `ebf3_cabin_wall_panels` | Vacuum boundary wall panels and stiffened chamber shell surfaces. |
| MC-3 | `ebf3_cabin_access_door` | Service access door assembly with latch, hinge, and vacuum seal interface. |
| MC-4 | `ebf3_cabin_viewport` | Viewport or optical window for process observation. |
| MC-5 | `ebf3_cabin_gun_mounting_port` | Top/side chamber port and flange interface for fixed electron beam gun insertion. |
| MC-6 | `ebf3_cabin_wire_feeder_mounting_port` | Chamber-side wire-feeder mounting port or passive datum. |
| MC-7 | `ebf3_cabin_sacrificial_liner` | Replaceable liner or shield protecting cabin walls from condensate, spatter, and deposition debris. |
| MC-8 | `ebf3_cabin_positioning_mount_interface` | Chamber floor/access interface for the four-axis positioning subsystem. |
| MC-9 | `ebf3_cabin_lighting_mount_and_port` | Cabin-side passive lighting mount, optical access, or chamber penetration. |

Deferred source-related candidates:

- `ebf3_cabin_build_substrate_support`
- `ebf3_cabin_feedthroughs_and_wiring_ports`

See `research/ebf3_bom_sources/organized/manufacture_cabin_level_2_audit.md`
for the source-table correction and boundary rationale.

Masses are first-pass allocations constrained to the current subsystem mass. Leaf items intentionally have no local recipes yet.
