# Split-Before-Route Leaf Decomposition Plan

Status: source-first review completed for the 15 leaves marked
`split_before_route` in
`research/ebf3_bom_sources/derived/ebf3_leaf_decomposition_review.csv`.
The seven rows that passed the source-first gate have been implemented as child
BOMs.

Purpose: decide which leaves are ready for child BOM creation before
material/process routing, and which must remain unresolved because the evidence
does not support a trustworthy split.

Source registry:

- `research/ebf3_bom_sources/sources/level_3_parts/split_before_route_items/split_before_route_sources.md`

Workflow:

- `research/ebf3_bom_sources/README.md`

Target leaves:

- `ebf3_cabin_access_door_hinge_set`
- `ebf3_cabin_access_door_latch_set`
- `ebf3_cabin_wall_panel_seam_set`
- `ebf3_emi_filter_choke_set`
- `ebf3_feed_liner_tube`
- `ebf3_gun_deflection_magnetic_yoke`
- `ebf3_gun_deflection_x_coil_pair`
- `ebf3_gun_deflection_y_coil_pair`
- `ebf3_gun_dynamic_lens_coil_assembly`
- `ebf3_gun_main_lens_coil_assembly`
- `ebf3_gun_side_oil_tank`
- `ebf3_matching_network_inductor_set`
- `ebf3_power_electronics_cooling_duct_or_line_set`
- `ebf3_sectioned_hv_step_up_transformer`
- `ebf3_z_axis_counterbalance_force_element`

## Source Authority Assessment

1. Local EBF3 tables and derived CSV rows identify the review target, but are
   candidate-only and cannot justify child BOMs by themselves.
2. Existing organized EBF3 plans override generic web evidence where they
   already converged. This is especially important for coil assemblies and
   gun-side oil insulation.
3. External commercial/technical sources are used only to justify generic
   construction patterns. They do not establish final EBF3 geometry, ratings,
   materials, or local manufacturability.
4. A child item can be `adopt` only when it represents a stable same-boundary
   physical function. If a source shows a family of alternatives, the current
   item is kept unresolved until an architecture choice is made.
5. Lunar deployment is treated as vacuum unless a separate pressurized enclosure
   is explicitly modeled. Air ducts or fan cooling are therefore not assumed for
   exposed lunar power electronics.

## Source Evidence And Use

### WEB-STREICHER-VACUUM-CHAMBER-ACCESSORIES

Evidence:

- "hinges, locking mechanisms, gas pistons"
- "door sizes"
- "eccentric shaft"
- "locking mechanisms"
- "welded from more plates"
- "welding neck flanges"

Use:

- Supports door hinge/latch mechanisms as real chamber-access hardware.
- Supports chamber wall panels and flanges as welded or machined vacuum
  structures.
- Does not specify EBF3 access-door hinge geometry or latch force.

### WEB-ABBESS-VACUUM-DOOR-LATCH

Evidence:

- "latch point cams"
- "common axle"
- "spring loads a return"
- "latching bar"
- "fitted to most vacuum chambers"

Use:

- Supports latch-set decomposition into actuation/cam, axle, return spring, and
  latching/catch functions.
- Does not prove the EBF3 cabin uses this exact latch topology.

### WEB-PFEIFFER-VACUUM-CONNECTIONS

Evidence:

- "weld-on flange rings"
- "deep-penetration welded"
- "sealing surface geometry"

Use:

- Supports treating vacuum wall seams as geometry and process-boundary features
  rather than as a simple discrete replacement part.

### WEB-LESKER-VACUUM-CHAMBER-TECH-NOTES

Evidence:

- "top-plate already welded"
- "metal wire seal"
- "o-ring sealed base flange"
- "cooling-water trace welded"

Use:

- Supports chamber shell/wall welding, sealing choices, and welded cooling trace
  concepts.
- Does not justify an active child BOM for `ebf3_cabin_wall_panel_seam_set`
  without an EBF3 seam architecture.

### WEB-MDC-KF-FLANGE-ASSEMBLY

Evidence:

- "two weld flanges"
- "one aluminum hinged clamp"
- "centering ring"
- "Viton"

Use:

- Supports vacuum seal assemblies as multi-part systems.
- Used only as generic evidence; access-door seams and wall-panel seams are not
  automatically KF flange assemblies.

### WEB-MURATA-COMMON-MODE-CHOKE

Evidence:

- "two conducting wires"
- "single core"
- "four terminals"
- "wrapped around the core"

Use:

- Supports splitting an EMI common-mode choke into core, windings, terminals,
  and insulation/support when the parent is a choke set.

### WEB-SCHAFFNER-RB-CHOKE-APPNOTE

Evidence:

- "common-mode (CM) chokes"
- "two identical windings"
- "ferrite cores"
- "bobbins"
- "base plates"
- "convection cooling"

Use:

- Supports choke-level child functions for EMI filters and matching/network
  inductor packages.
- Provides current/cooling/rating sensitivity, so child BOMs must not imply
  local-ready manufacturing.

### WEB-BINZEL-MIG-LINER

Evidence:

- "tube or helically wound wire"
- "conduit to guide the welding wire"
- "match the type and size"
- "Steel MIG Gun Liners"
- "Plastic MIG Gun Liners"
- "Neck Liners"

Use:

- Supports keeping `ebf3_feed_liner_tube` unresolved until a liner architecture
  is selected: tube, helically wound wire, plastic/PTFE, steel, insulated steel,
  neck liner, or other vacuum-ready variant.

### LOCAL-COIL-LEVEL-DECOMPOSITION-PLAN

Evidence:

- Coil leaf review keeps lens and deflection coil items as BOM leaves.
- Candidate internal items such as bobbin/former, insulation, lead
  terminations, mounting, and cooling are not adopted as lower child BOMs.

Use:

- Overrides the derived CSV suggestion for coil assemblies. These four coil
  leaves should be routed as single leaf items; remaining work belongs to
  material/process readiness or interface ownership.

### LOCAL-MAGNETIC-STEERING-PLAN

Evidence:

- Existing FG-8 adopted children are X coil pair, Y coil pair, and magnetic
  yoke.
- Coil former, insulation, leads, bracket, and cooling were deferred.

Use:

- Keeps `ebf3_gun_deflection_magnetic_yoke`,
  `ebf3_gun_deflection_x_coil_pair`, and
  `ebf3_gun_deflection_y_coil_pair` from being split below their current
  boundary without stronger geometry evidence.

### LOCAL-HV-GUN-SIDE-INSULATION-PLAN

Evidence:

- Gun-side oil tank is a boundary marker.
- Notes say not to decompose into shell, lid, oil, or seals until separate
  gun-side oil-volume evidence is found.

Use:

- Overrides generic tank evidence. `ebf3_gun_side_oil_tank` remains unresolved
  and should not receive child BOMs now.

### RAW-BINP-60KV-15KW-HV-TANK

Evidence:

- Comparable HV tank source with transformer, rectifier, oil, and bushing
  context in the current EBF3 source registry.

Use:

- Supports the existence of an HV tank/transformer package, but the exact EBF3
  sectioned transformer internals still require cautious treatment.

### WEB-CNCCOOKBOOK-Z-COUNTERBALANCE

Evidence:

- "Counterweight"
- "gas springs"
- "air-over-oil system"
- "cables or roller chain"
- "force exerted by the spring"

Use:

- Supports multiple Z-axis counterbalance architectures.
- Because the force element could be counterweight, gas spring, hydraulic, or
  spring, no child BOM should be adopted until the architecture is selected.

### WEB-ASRAYMOND-COUNTERBALANCE

Evidence:

- "Gas Springs"
- "Mechanical Struts"
- "spring rate"
- "force"

Use:

- Supports gas/mechanical struts as real counterbalance options.
- Does not choose the EBF3 force element architecture.

### WEB-ATS-LIQUID-COLD-PLATES

Evidence:

- "localized cooling of power electronics"
- "high-powered semiconductors"
- "transferring heat from the device to a liquid"
- "remote heat exchanger"

Use:

- Supports treating power-electronics cooling lines/ducts as part of a thermal
  architecture, not a simple generic tube.

## Candidate Decision Matrix

| Leaf item | Status | Candidate child functions | Decision basis |
| --- | --- | --- | --- |
| `ebf3_cabin_access_door_hinge_set` | implemented | hinge leaf/bracket set; hinge pin/shaft; bearing/bushing or sliding contact; fastener/interface set | Vacuum chamber sources support hinges and alignment shafts. These children are same-boundary mechanical functions, but exact bearing/lubrication remains material-process deferred. |
| `ebf3_cabin_access_door_latch_set` | implemented | latch/cam or handle mechanism; common axle/pivot; return spring; catch/strike bar; fastener/interface set | Abbess supports cams, common axle, return spring, and latching bar in vacuum door latch hardware. EBF3 topology remains approximate, so keep wording function-level. |
| `ebf3_cabin_wall_panel_seam_set` | defer | weld land/bead; seal land; inspection/leak-test feature | Sources support welds/flanges/sealing surfaces, but this is likely a seam geometry/process boundary rather than a stable discrete child assembly. Do not create child BOM yet. |
| `ebf3_emi_filter_choke_set` | implemented | magnetic/ferrite core set; conductor winding set; bobbin/insulation support; terminal lead set; mounting/base plate | Murata and Schaffner support core, multiple windings, bobbin/base plate, and terminals. Ratings and material route remain deferred. |
| `ebf3_feed_liner_tube` | route_as_single_leaf | replaceable metallic guide tube with bore/surface-finish requirements | Architecture selected: use a replaceable metallic guide tube baseline, not polymer/PTFE or helical wound liner. Bore, finish, wear behavior, and alloy remain material/process readiness issues. |
| `ebf3_gun_deflection_magnetic_yoke` | defer | yoke body; pole/return geometry; mounting/alignment interface | Dedicated magnetic steering and coil-level plans already defer lower yoke details. Avoid duplicating yoke, bobbin, and pole functions. |
| `ebf3_gun_deflection_x_coil_pair` | route_as_single_leaf | X-axis coil pair | Coil leaf review treats the coil pair as the BOM leaf. Material/process readiness and electrical interface remain open. |
| `ebf3_gun_deflection_y_coil_pair` | route_as_single_leaf | Y-axis coil pair | Same as X coil pair. |
| `ebf3_gun_dynamic_lens_coil_assembly` | route_as_single_leaf | dynamic-lens copper coil leaf | Coil leaf review treats the lens coil as the BOM leaf. Material/process readiness and electrical interface remain open. |
| `ebf3_gun_main_lens_coil_assembly` | route_as_single_leaf | main-lens copper coil leaf | Same as dynamic lens coil. |
| `ebf3_gun_side_oil_tank` | defer | shell; lid; oil volume; seal; feedthrough support | Existing gun-side HV plan explicitly says not to decompose until separate gun-side oil-volume evidence is found. |
| `ebf3_matching_network_inductor_set` | implemented | magnetic core set; conductor winding set; insulation/bobbin support; terminal lead set; mounting/base plate | Schaffner/Murata support inductor/choke construction patterns. Exact topology and ratings remain deferred. |
| `ebf3_power_electronics_cooling_duct_or_line_set` | implemented | conductive cooling line or strap set; cold-plate port/interface set; remote radiator/heat-exchanger connection marker; support clamp set | Architecture selected: lunar-vacuum baseline uses conduction/cold-plate heat transfer, not air duct cooling, unless a future pressurized electronics enclosure is explicitly modeled. |
| `ebf3_sectioned_hv_step_up_transformer` | implemented | magnetic core set; primary/secondary winding set; inter-winding insulation/barrier set; internal HV leads; section support/mount; oil interface marker | HV transformer leaf is large and hides core/winding/insulation/leads. This supersedes the older HV tank core plan only at the function-level child-shape layer; exact section count, geometry, materials, ratings, and local manufacturability remain deferred. |
| `ebf3_z_axis_counterbalance_force_element` | implemented | metal spring force element; spring end seat/retainer set; preload or adjustment interface | Architecture selected: use a metal spring baseline, not gas spring, hydraulic, or air-over-oil counterbalance. Spring material, fatigue, preload, and guide integration remain material/process readiness issues. |

## Implemented Child BOM Shapes

These shapes are now written to KB as child items, child BOMs, and assembly
recipes. They remain function-level decomposition only; they do not claim local
manufacturing readiness.

### `ebf3_cabin_access_door_hinge_set`

- `ebf3_cabin_access_door_hinge_leaf_or_bracket_set`
- `ebf3_cabin_access_door_hinge_pin_or_shaft_set`
- `ebf3_cabin_access_door_hinge_bushing_or_bearing_set`
- `ebf3_cabin_access_door_hinge_fastener_interface_set`

### `ebf3_cabin_access_door_latch_set`

- `ebf3_cabin_access_door_latch_handle_or_cam_set`
- `ebf3_cabin_access_door_latch_pivot_axle_set`
- `ebf3_cabin_access_door_latch_return_spring_set`
- `ebf3_cabin_access_door_latch_strike_or_bar_set`
- `ebf3_cabin_access_door_latch_fastener_interface_set`

### `ebf3_emi_filter_choke_set`

- `ebf3_emi_filter_choke_core_set`
- `ebf3_emi_filter_choke_winding_set`
- `ebf3_emi_filter_choke_bobbin_or_insulation_set`
- `ebf3_emi_filter_choke_terminal_set`
- `ebf3_emi_filter_choke_mounting_base_set`

### `ebf3_matching_network_inductor_set`

- `ebf3_matching_network_inductor_core_set`
- `ebf3_matching_network_inductor_winding_set`
- `ebf3_matching_network_inductor_bobbin_or_insulation_set`
- `ebf3_matching_network_inductor_terminal_set`
- `ebf3_matching_network_inductor_mounting_base_set`

### `ebf3_power_electronics_cooling_duct_or_line_set`

Lunar-vacuum baseline: conduction/cold-plate thermal path. Do not model an air
duct unless a pressurized electronics enclosure is later added.

- `ebf3_power_electronics_conductive_cooling_line_or_strap_set`
- `ebf3_power_electronics_cold_plate_port_interface_set`
- `ebf3_power_electronics_cooling_line_support_clamp_set`

The earlier remote heat exchanger connection marker should not be a separate
manufacturable leaf in the first simulation. Its mass and interface requirement
are folded into `ebf3_power_electronics_cold_plate_port_interface_set`; the
remote radiator topology remains a future architecture requirement.

### `ebf3_sectioned_hv_step_up_transformer`

This child shape is a function-level refinement of the earlier HV tank core
plan. It does not override that plan's deferral of exact section count,
geometry, materials, voltage ratings, insulation design, or process readiness.

- `ebf3_hv_transformer_magnetic_core_set`
- `ebf3_hv_transformer_primary_winding_set`
- `ebf3_hv_transformer_secondary_winding_set`
- `ebf3_hv_transformer_interwinding_insulation_set`
- `ebf3_hv_transformer_internal_hv_lead_set`
- `ebf3_hv_transformer_section_support_structure`
- `ebf3_hv_transformer_oil_interface_marker`

### `ebf3_z_axis_counterbalance_force_element`

Architecture selected: metal spring force element. Gas spring, hydraulic, and
air-over-oil options remain rejected for this baseline because they introduce
sealed pressure systems and imported-fluid complexity.

- `ebf3_z_axis_counterbalance_metal_spring_element`
- `ebf3_z_axis_counterbalance_spring_end_seat_set`
- `ebf3_z_axis_counterbalance_preload_adjustment_interface`

## Architecture Selected Without Child BOM

### `ebf3_feed_liner_tube`

Architecture selected: replaceable metallic guide tube. Treat the current leaf
as a terminal part for the next material/process readiness pass. Do not split
into polymer liner, helical wound liner, neck liner, or coating sub-items unless
later source evidence or wire-feed performance requirements require those
variants.

## Deferred Or Architecture-Choice Items

These rows should remain in the unresolved/deferred state until a source or
design choice narrows the architecture:

- `ebf3_cabin_wall_panel_seam_set`: seam/process geometry, not stable child BOM.
- `ebf3_gun_deflection_magnetic_yoke`: lower yoke geometry deferred by
  magnetic-steering plan.
- `ebf3_gun_side_oil_tank`: separate gun-side oil volume not source-fixed.

## KB Action For This Pass

- Created child items, child BOMs, and assembly recipes for the seven rows
  marked `implemented`.
- `ebf3_feed_liner_tube` should remain a single leaf for the next
  material/process readiness pass unless later evidence reopens its
  architecture.
- Do not add recipes or local closure for any child created from this plan until
  a separate material/process readiness review resolves materials, ratings,
  vacuum compatibility, tolerances, and test requirements.

## Validation Note

Targeted validation passed for `ebf3_3d_printer` and for all seven implemented
parent items after applying the child BOMs.
