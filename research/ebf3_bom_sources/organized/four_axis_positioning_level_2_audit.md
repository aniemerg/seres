# Four-Axis Positioning Level-2 Audit

Status: review completed; source-table aligned BOM correction and first
mechanical child splits applied.

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
- `research/ebf3_bom_sources/organized/electrical_signal_boundary_review.md`
- `research/ebf3_bom_sources/organized/feedthrough_interface_review.md`
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

### WEB-PI-VACUUM-POSITIONING

Evidence:

- "cables, motors, scaling systems, connectors or limit switches"
- "Vacuum cable insulation is made of PTFE or FEP"
- "polyimide (Kapton) or PEEK"

Use:

- Supports vacuum-specific treatment of positioning motors, sensors, connectors,
  and cables.
- Does not select a specific EBF3 cable bundle, connector family, feedthrough
  pinout, or motor technology.

### WEB-LESKER-KAPTON-WIRE

Evidence:

- "high & ultra-high vacuum applications"
- "low outgassing rates"
- "Max. Current depends strongly on use"

Use:

- Supports Kapton/polyimide wire as a plausible in-vacuum cabling material
  class.
- Reinforces that current, heating, and continuous-use ratings must be selected
  before splitting motor-power cable children.

### WEB-VACOM-ELECTRICAL-FEEDTHROUGHS

Evidence:

- "transmission of electric power into or out of a vacuum chamber"
- "Multipin feedthroughs"
- "measurement & control applications"
- "High Voltage and Power Feedthroughs"

Use:

- Supports separate signal/multipin and power-feedthrough choices.
- Does not prove whether EBF3 FS-30 is a single mixed feedthrough, separate
  motor/sensor inserts, or part of a shared chamber feedthrough plate.

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

## Mechanical Child Splits

Child BOMs were added for positioning assemblies whose physical boundaries are
useful for review. The splits are package-level only; precision geometry,
ratings, materials, and local manufacturing routes remain unresolved:

| Parent | Child BOM | Current boundary |
| --- | --- | --- |
| `ebf3_positioning_base_frame` | `bom_ebf3_positioning_base_frame` | Rail set, crossmember set, and mounting feet. |
| `ebf3_linear_guide_carriages` | `bom_ebf3_linear_guide_carriages` | Carriage block, rolling elements, and retainers. |
| `ebf3_fixed_side_screw_bearing_blocks` | `bom_ebf3_fixed_side_screw_bearing_blocks` | Fixed-side block bodies, angular-contact bearing set, and retainers. |
| `ebf3_floating_side_screw_bearing_blocks` | `bom_ebf3_floating_side_screw_bearing_blocks` | Floating-side block bodies, radial bearing set, and retainers. |
| `ebf3_rotary_axis_table` | `bom_ebf3_rotary_axis_table` | Table plate, hub, and mounting pattern. |
| `ebf3_moveable_build_platform` | `bom_ebf3_moveable_build_platform` | Platform plate, clamp slots, and local return contact pad. |
| `ebf3_substrate_clamp` | `bom_ebf3_substrate_clamp` | Clamp jaws, screws, and local insulating pads. |
| `ebf3_ball_screw_shafts` | `bom_ebf3_ball_screw_shafts` | X/Y/Z shaft set marker; screw profile and grinding/rolling process remain unresolved. |
| `ebf3_ball_nuts` | `bom_ebf3_ball_nuts` | Nut body, rolling balls, recirculation insert, and wiper/seal set. |
| `ebf3_axis_motors` | `bom_ebf3_axis_motors` | Motor body set, housings, leads, and mounting features; motor internals remain deferred. |
| `ebf3_motor_couplings` | `bom_ebf3_motor_couplings` | Hubs, flexible element, and clamp screws. |
| `ebf3_motor_mount_brackets` | `bom_ebf3_motor_mount_brackets` | Bracket plates, spacers, and fastener interfaces. |
| `ebf3_linear_encoder_scales` | `bom_ebf3_linear_encoder_scales` | Scale strips, read heads, and mounting brackets. |
| `ebf3_axis_home_sensors` | `bom_ebf3_axis_home_sensors` | Sensor bodies, targets, and leads. |
| `ebf3_axis_travel_limit_switches` | `bom_ebf3_axis_travel_limit_switches` | Switch bodies, actuators, and leads. |
| `ebf3_z_axis_brake` | `bom_ebf3_z_axis_brake` | Brake body, friction disc, and mount. |
| `ebf3_z_axis_counterbalance` | `bom_ebf3_z_axis_counterbalance` | Force element, anchors, and guide/link. |
| `ebf3_rotary_axis_bearing` | `bom_ebf3_rotary_axis_bearing` | Bearing rings, rolling elements, and retainer. |
| `ebf3_rotary_encoder` | `bom_ebf3_rotary_encoder` | Read head, scale ring, and signal lead. |
| `ebf3_beam_current_return_strap` | `bom_ebf3_beam_current_return_strap` | Flexible conductor, lugs, and fastener interfaces. |
| `ebf3_thermal_isolation_standoffs` | `bom_ebf3_thermal_isolation_standoffs` | Insulating standoffs/washers and local fastener interfaces. |
| `ebf3_positioning_bellows_cover` | `bom_ebf3_positioning_bellows_cover` | Folded cover, end retainers, and mounting tabs. |
| `ebf3_spatter_shielding` | `bom_ebf3_spatter_shielding` | Shield panels, retainers, and mounting tabs. |
| `ebf3_vacuum_compatible_motor_cabling` | `bom_ebf3_vacuum_compatible_motor_cabling` | Conductors, insulation, shield, and terminations. |
| `ebf3_vacuum_compatible_signal_cabling` | `bom_ebf3_vacuum_compatible_signal_cabling` | Conductors, insulation, shield, and terminations. |
| `ebf3_positioning_electrical_feedthrough` | `bom_ebf3_positioning_electrical_feedthrough` | Motor-power pins, signal pins, ceramic body, flange, vacuum-side connector, air-side connector, and shield termination interface. |

Still deferred:

- Motor electromagnetic internals, encoder technology, limit/home sensor type,
  pinout, shielding scheme, and feedthrough connector family remain deferred
  because they cross controls, power, and cabin interface boundaries.
- Precision rail/ball-screw race geometry, preload, lubrication/dry-film
  strategy, and calibration remain material/process readiness issues.

## Cabling / Feedthrough Follow-Up

Target: decide whether FS-28, FS-29, and FS-30 should be split now into motor
power pins, signal pins, ceramic body, flange, internal connector, external
connector, shield termination, and cable material children.

Decision: split package layers only; keep topology and ownership-sensitive
details deferred.

Reasoning:

- The source table and EBF patent support motor/sensor wiring and electrical
  feedthroughs as real positioning interfaces.
- External vacuum-motion and feedthrough sources support vacuum-compatible
  cables, connectors, and power/signal feedthrough classes.
- No source currently fixes the EBF3 pinout, connector family, motor current,
  sensor signal type, shielding scheme, or whether FS-30 is one mixed
  feedthrough or several inserts.
- Package-level children are acceptable because they preserve the difference
  between cable conductor, insulation, shield, termination, motor-power pins,
  signal pins, ceramic body, flange, vacuum-side connector, air-side connector,
  and shield termination without selecting final topology.

Current action:

- Keep FS-28 and FS-29 as positioning-owned local/in-chamber cabling assemblies
  with child BOMs for cable layers.
- Keep FS-30 as the positioning-specific feedthrough interface assembly with a
  package-level child BOM. The previous generic pin and connector-side markers
  have been replaced by motor-power pins, signal pins, vacuum-side connector,
  air-side connector, and shield-termination markers.
- Keep CTL-10 as controls-side motion command/control hardware, not a duplicate
  of positioning motors or power driver outputs.
- Revisit only after a physical cable/feedthrough topology is selected.

## Batch Child Split Review

| Parent scope | Current status | Rationale |
| --- | --- | --- |
| Ball screws and nuts | adopt / detail deferred | Thomson and Steinmeyer support ball screw/nut assemblies and ball-return/wiper concepts. Screw profile, preload, material, and manufacturing route remain unresolved. |
| Motors, brakes, encoders, sensors | adopt / package only | The EBF source supports motorized positioning and controls feedback; child BOMs stop at body/lead/target/read-head package boundaries. Electromagnetic internals and signal architecture remain deferred. |
| Bearings, couplings, brackets, shields | adopt / detail deferred | These are physically coherent motion-system assemblies. Bearing class, preload, lubrication, coupling style, and shield geometry remain unresolved. |
| Cabling/feedthrough | adopt package split / split-boundary guarded | Positioning owns in-chamber cable packages and positioning-specific insert; cabin owns passive port/flange, controls own acquisition, and power supplies own drive outputs. |
| Worm wheel/shaft and base plate | keep leaf | Current names can represent single-piece precision metal parts; split only after worm-drive geometry or process source is selected. |

## Manufacturing Readiness

No four-axis positioning item is local-ready. Precision rails, carriages, ball
screws, bearings, vacuum motors, encoders, feedthroughs, flexible cabling,
lubrication/dry-film choices, isolation blocks, thermal distortion, alignment,
and closed-loop calibration all need separate material/process readiness review
before recipes are attached.
