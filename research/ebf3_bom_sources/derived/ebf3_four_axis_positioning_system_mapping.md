# ebf3_four_axis_positioning_system Mapping

Authority note: this is a first-pass scaffold mapping from a user-derived table.
It preserves candidate item IDs and high-level modeling intent, but it is not a
decomposition planning file and cannot by itself justify child BOM creation,
material selection, recipe closure, or local manufacturability.

Four-axis positioning leaf items mapped from V2_four-axis_positioning_system_item_table; no leaf recipes yet to preserve fidelity.

| Source ID | Item ID | Modeling decision |
| --- | --- | --- |
| FS-1 | `ebf3_positioning_base_frame` | Structural frame for positioning system. |
| FS-2 | `ebf3_positioning_axis_base_plate` | Base plate and datum surface for linear axes. |
| FS-3 | `ebf3_linear_guide_rails` | Precision linear guide rail set. |
| FS-4 | `ebf3_linear_guide_carriages` | Linear guide carriage/block assemblies. |
| FS-5 | `ebf3_ball_screw_shafts` | Ball screw shafts for linear motion. |
| FS-6 | `ebf3_ball_nuts` | Ball nut assemblies for screw drive. |
| FS-7 | `ebf3_fixed_side_screw_bearing_blocks` | Fixed-side screw support bearing blocks. |
| FS-8 | `ebf3_floating_side_screw_bearing_blocks` | Floating-side screw support bearing blocks. |
| FS-9 | `ebf3_axis_motors` | Axis motor assemblies for positioning system. |
| FS-10 | `ebf3_motor_couplings` | Motor-to-screw couplings. |
| FS-11 | `ebf3_motor_mount_brackets` | Brackets aligning motors with screw drives. |
| FS-12 | `ebf3_linear_encoder_scales` | Linear encoder scale/readhead assemblies. |
| FS-13 | `ebf3_axis_home_sensors` | Home sensors and targets for axes. |
| FS-14 | `ebf3_axis_travel_limit_switches` | Travel limit switch assemblies. |
| FS-15 | `ebf3_z_axis_brake` | Z-axis brake or holding mechanism. |
| FS-16 | `ebf3_z_axis_counterbalance` | Counterbalance or load-reduction mechanism for vertical axis. |
| FS-17 | `ebf3_rotary_axis_table` | Rotary build table mounted on linear axes. |
| FS-18 | `ebf3_rotary_axis_bearing` | Rotary bearing assembly supporting build table. |
| FS-19 | `ebf3_rotary_worm_wheel` | Worm wheel for the rotary-axis worm-drive pair. |
| FS-20 | `ebf3_rotary_worm_shaft` | Worm shaft for the rotary-axis worm-drive pair. |
| FS-21 | `ebf3_rotary_encoder` | Rotary encoder for angular position feedback. |
| FS-22 | `ebf3_moveable_build_platform` | Moveable platform carrying substrate through motion path. |
| FS-23 | `ebf3_substrate_clamp` | Clamp securing substrate to build platform. |
| FS-24 | `ebf3_beam_current_return_strap` | Grounding/current return strap for platform and beam current. |
| FS-25 | `ebf3_thermal_isolation_standoffs` | Thermal/electrical isolation standoffs for process zone. |
| FS-26 | `ebf3_positioning_bellows_cover` | Bellows/protective cover for axes near process debris. |
| FS-27 | `ebf3_spatter_shielding` | Shielding against metal vapor, spatter, and process-zone debris. |
| FS-28 | `ebf3_vacuum_compatible_motor_cabling` | Vacuum-compatible motor power cabling. |
| FS-29 | `ebf3_vacuum_compatible_signal_cabling` | Vacuum-compatible encoder and sensor signal cabling. |
| FS-30 | `ebf3_positioning_electrical_feedthrough` | Feedthrough passing motor/sensor signals through chamber wall. |

Deferred source-related candidates:

- `ebf3_rotary_drive_worm_gear`
- `ebf3_rotary_axis_motor`

See `research/ebf3_bom_sources/organized/four_axis_positioning_level_2_audit.md`
for the source-table correction and boundary rationale.

Masses are first-pass allocations constrained to the current subsystem mass. Leaf items intentionally have no local recipes yet.
