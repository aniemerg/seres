# Four-Axis Positioning Level-2 Audit

Status: review completed; source-table aligned BOM correction applied.

Purpose:

- Compare current four-axis positioning BOM leaves against the source table and
  available source evidence.
- Preserve boundaries between positioning, manufacture cabin, controls, power
  supplies, and high-voltage return/grounding.
- Keep motion hardware inside positioning while leaving chamber-side ports,
  central motion control, motor power supplies, and system-level return topology
  outside this subsystem.

Source registry:

- `research/ebf3_bom_sources/sources/level_1_subsystems/four_axis_positioning_system/four_axis_positioning_system_sources.md`

Related boundary reviews:

- `research/ebf3_bom_sources/derived/ebf3_subsystem_boundaries.md`
- `research/ebf3_bom_sources/organized/manufacture_cabin_level_2_audit.md`
- `research/ebf3_bom_sources/organized/hv_grounding_return_review.md`

## Source Use

### RAW-EBF-PATENT

Evidence:

- "moveable platform"
- "at least one positioning Subsystem motor"
- "rate and location sensors"
- "means for providing electrical continuity"
- "means for providing thermal and electrical isolation"
- "means for providing protective shielding"
- "ball screws"
- "worm gears"
- "at least one electrical feed-through"

Use:

- Supports motion platform, axis motors, sensors/encoders, beam-current
  continuity hardware at the platform, thermal/electrical isolation, protective
  shielding, ball-screw linear mechanisms, worm-gear rotary mechanism, and
  electrical feedthrough concept.
- Does not make the positioning subsystem owner of central controls, power
  supplies, chamber-side generic feedthrough ports, or complete system-level HV
  return topology.

### RAW-EBF-SPACE

Evidence:

- "three orthogonal linear axes"
- "360° of rotation"
- "attached to the floor"

Use:

- Supports the four-axis structure: three linear axes plus a rotary axis, mounted
  in the chamber.

### LOCAL-EBF3-FOUR-AXIS-TABLE

Use:

- Introduces FS-1 through FS-30 candidates and cites external motion/vacuum
  hardware references for materials and detailed motion components.
- Candidate-only until cited external sources are archived or independently
  checked.

## Main Finding

The current four-axis positioning BOM was mostly aligned with the source table.
The clear mismatch was FS-19 and FS-20:

- Source row FS-19 is **worm wheel**, but the current BOM used
  `ebf3_rotary_drive_worm_gear`.
- Source row FS-20 is **worm shaft**, but the current BOM used
  `ebf3_rotary_axis_motor`.

Because FS-9 already covers positioning axis motors, keeping a separate rotary
axis motor as a top-level row would duplicate the motor concept and obscure the
source-table rotary-drive split.

## Level-2 Decision Matrix

| Source table row | Current or recommended item | Decision | Rationale |
| --- | --- | --- | --- |
| FS-1 positioning base frame | `ebf3_positioning_base_frame` | keep | Patent supports structural connection to sealed container. |
| FS-2 axis mounting plate | `ebf3_positioning_axis_base_plate` | keep | Space paper supports floor attachment; cabin owns passive chamber floor interface. |
| FS-3 linear guide rail | `ebf3_linear_guide_rails` | keep | Space paper supports three linear axes; source table supports rails. |
| FS-4 linear guide carriage | `ebf3_linear_guide_carriages` | keep | Source table supports carriage assemblies. |
| FS-5 ball screw shaft | `ebf3_ball_screw_shafts` | keep | Patent supports ball screws. |
| FS-6 ball nut | `ebf3_ball_nuts` | keep | Ball screw drive requires nut assembly; source table supports it. |
| FS-7 fixed-side screw bearing block | `ebf3_fixed_side_screw_bearing_blocks` | keep | Source table supports screw support hardware. |
| FS-8 floating-side screw bearing block | `ebf3_floating_side_screw_bearing_blocks` | keep | Source table supports screw support hardware. |
| FS-9 axis motor | `ebf3_axis_motors` | keep | Patent supports positioning subsystem motors; includes linear and rotary drive motors at this level. |
| FS-10 motor coupling | `ebf3_motor_couplings` | keep | Source table supports motor-to-screw coupling. |
| FS-11 motor mount bracket | `ebf3_motor_mount_brackets` | keep | Source table supports motor mounts. |
| FS-12 linear encoder scale | `ebf3_linear_encoder_scales` | keep | Patent supports rate/location sensors. |
| FS-13 axis home sensor | `ebf3_axis_home_sensors` | keep | Sensor hardware remains positioning-local; controls owns acquisition logic. |
| FS-14 axis travel limit switch | `ebf3_axis_travel_limit_switches` | keep | Sensor hardware remains positioning-local. |
| FS-15 Z-axis brake | `ebf3_z_axis_brake` | keep | Source table supports holding mechanism. |
| FS-16 Z-axis counterbalance | `ebf3_z_axis_counterbalance` | keep | Source table supports load-reduction mechanism. |
| FS-17 rotary axis table | `ebf3_rotary_axis_table` | keep | Space paper supports 360 degree rotation. |
| FS-18 cross-roller rotary bearing | `ebf3_rotary_axis_bearing` | keep / retag wording | Existing item is the rotary bearing assembly; source table wording is cross-roller rotary bearing. |
| FS-19 worm wheel | `ebf3_rotary_worm_wheel` | corrected | Source table splits the worm gear pair; add explicit worm wheel item. |
| FS-20 worm shaft | `ebf3_rotary_worm_shaft` | corrected | Source table splits the worm gear pair; rotary motor remains covered by FS-9. |
| FS-21 rotary encoder | `ebf3_rotary_encoder` | keep | Patent supports rate/location sensors; source table supports rotary encoder. |
| FS-22 moveable platform | `ebf3_moveable_build_platform` | keep | Patent directly supports moveable platform. |
| FS-23 substrate clamp | `ebf3_substrate_clamp` | keep | Patent supports means for clamping a base plate. |
| FS-24 beam-current return strap | `ebf3_beam_current_return_strap` | keep with boundary note | Positioning owns platform/substrate continuity; system-level return topology remains deferred. |
| FS-25 thermal/electrical isolation block | `ebf3_thermal_isolation_standoffs` | keep / retag wording | Existing item covers isolation blocks/standoffs; material and geometry unresolved. |
| FS-26 bellows cover | `ebf3_positioning_bellows_cover` | keep | Patent supports protective shielding. |
| FS-27 sacrificial sheet-metal shield | `ebf3_spatter_shielding` | keep / retag wording | Existing item covers sacrificial protection from metal vapor/spatter. |
| FS-28 vacuum-compatible motor cable | `ebf3_vacuum_compatible_motor_cabling` | keep with boundary note | Positioning owns local/in-chamber motor cabling; power supplies own source outputs. |
| FS-29 vacuum-compatible sensor cable | `ebf3_vacuum_compatible_signal_cabling` | keep with boundary note | Positioning owns local signal cabling; controls own acquisition and decision logic. |
| FS-30 electrical feedthrough interface | `ebf3_positioning_electrical_feedthrough` | keep with boundary note | Keep as positioning-specific feedthrough insert/interface; cabin owns generic chamber-side port/flange. |

## Deferred Candidates

| Candidate item | Why not in top-level positioning BOM now | Next unblock condition |
| --- | --- | --- |
| `ebf3_rotary_drive_worm_gear` | Too broad for FS-19/FS-20 because the source table separates worm wheel and worm shaft. | Reintroduce only as a parent assembly if a rotary-drive child BOM is created. |
| `ebf3_rotary_axis_motor` | Duplicates FS-9 axis motor at the top level. | Reintroduce only inside an axis-motor or rotary-drive decomposition if source-fixed. |

## Applied BOM Correction

- Replaced `ebf3_rotary_drive_worm_gear` with `ebf3_rotary_worm_wheel` at FS-19.
- Replaced `ebf3_rotary_axis_motor` with `ebf3_rotary_worm_shaft` at FS-20.
- Kept the older broad worm-gear and rotary-motor items as deferred candidates,
  not deleted.
- Kept first-pass component mass allocation for current recipe mass balance;
  this audit does not claim sourced masses for corrected positioning leaves.

## Manufacturing Readiness

No four-axis positioning item is local-ready. Precision rails, carriages, ball
screws, bearings, vacuum motors, encoders, feedthroughs, flexible cabling,
lubrication/dry-film choices, isolation blocks, thermal distortion, alignment,
and closed-loop calibration all need separate material/process readiness review
before recipes are attached.
