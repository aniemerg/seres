# Fixed Electron Beam Gun Unresolved Items

Status: consolidated tracker for unresolved fixed-gun decomposition decisions.

Purpose:

- Keep deferred and split-boundary candidates visible after each organized
  decomposition plan.
- Prevent later work from treating omissions as forgotten items.
- Give each unresolved candidate an explicit next step before it becomes a KB
  item, stays with another subsystem, or remains a manufacturing-readiness issue.

Scope:

- Current scope is the EBF3 fixed electron beam gun and its immediate interface
  items.
- Source rows come from the organized planning files listed below. This register
  does not replace those plans and does not create KB child items by itself.
- This file only tracks open issues that still need source, geometry,
  ownership, or material/process decisions. Rejected candidates, inactive
  cathode variants, and rows already owned by another subsystem are intentionally
  kept out of the register.
- Whole-machine existing-item replacement review, including `not enough
  accuracy` markings for existing KB candidates, is tracked in
  `research/ebf3_bom_sources/derived/ebf3_leaf_material_process_readiness.csv` rather
  than duplicated here.

Source plans:

- `research/ebf3_bom_sources/organized/electromagnetic_lens_decomposition_plan.md`
- `research/ebf3_bom_sources/organized/cathode_cluster_decomposition_plan.md`
- `research/ebf3_bom_sources/organized/cathode_variant_review.md`
- `research/ebf3_bom_sources/organized/hv_gun_side_insulation_decomposition_plan.md`
- `research/ebf3_bom_sources/organized/beam_diagnostics_decomposition_plan.md`
- `research/ebf3_bom_sources/organized/electrical_signal_boundary_review.md`
- `research/ebf3_bom_sources/organized/magnetic_steering_decomposition_plan.md`
- `research/ebf3_bom_sources/organized/electrode_family_decomposition_plan.md`
- `research/ebf3_bom_sources/organized/gun_column_decomposition_plan.md`
- `research/ebf3_bom_sources/organized/ebf3_interface_architecture.md`

Workflow references:

- `research/ebf3_bom_sources/README.md`
- `research/ebf3_bom_sources/derived/ebf3_subsystem_boundaries.md`

## Status Use

- `defer`: keep visible, but do not create a KB item until the unblock condition
  is satisfied.
- `split_boundary / defer`: real candidate, but both ownership and geometry are
  unresolved.
- `modeled / detail deferred`: a KB marker exists, but the next fidelity step is
  still unresolved.
- `selected package direction / defer child BOM`: architecture direction is
  selected, but the lower child split is still unresolved.

## Priority Buckets

| Bucket | Meaning | Current examples |
| --- | --- | --- |
| Architecture decision needed | Cannot proceed until a layout or implementation is selected. | Cathode package geometry, gun-side oil volume, trajectory corrector implementation. |
| Boundary decision needed | Candidate crosses subsystem or parent boundaries and ownership is still unresolved. | HV cable/gun termination, signal feedthrough, grounding/return path. |
| Later child-level plan | Candidate belongs below an already-adopted child assembly. | Only use when the child is independently supported; current gun coils are not in this bucket. |
| Source geometry needed | Function is supported, but exact EBF3 geometry is not. | Beam-boundary collector, secondary-electron collector, aperture inserts, gun-column flange. |
| Manufacturing readiness only | Candidate should not become a BOM child yet; it belongs to later material/process review. | Stainless vacuum material choices, ceramic metallization, cooling and thermal features. |

## Near-Term Recommendations

1. Do not add recipes or local closure for any item in this register.
2. Before starting HV tank decomposition, review all rows tagged `HV tank`,
   `FG-12`, `FG-13`, and `FG-18`.
3. Current interface ownership is summarized in
   `research/ebf3_bom_sources/organized/ebf3_interface_architecture.md`; use it
   before decomposing controls, power supplies, diagnostics, feedthroughs, or
   gun signal wiring.
4. Coil leaf review is recorded in
   `research/ebf3_bom_sources/organized/coil_level_decomposition_plan.md`; gun
   coils stay as leaf items. Remaining work is electrical-interface or
   material/process readiness, not child BOM creation.
5. Cathode variant review is recorded in
   `research/ebf3_bom_sources/organized/cathode_variant_review.md`; the active
   package direction is now direct-heated tungsten hairpin/filament for lunar
   closure. LaB6 is preserved as original EBF3 reference evidence, and tantalum
   is de-prioritized for early lunar closure.

## Register

| ID | Candidate | Status | Applies to | Blocker / reason not modeled now | Next unblock condition | Source plan |
| --- | --- | --- | --- | --- | --- | --- |
| FG-D-002A | Direct-heated tungsten hairpin/filament package | selected package direction / defer child BOM | FG-1 / FG-14 / FG-15 | Lunar ISRU sources support W for low-mass cathode/filament use more strongly than Ta, and electron-gun sources support directly heated tungsten filaments. Existing KB tungsten cathode items are too low-resolution for direct reuse. | Source or select filament base, hot contacts, ceramic insulation/standoffs, and cartridge locating geometry. | cathode variant review |
| FG-D-004 | Heater contact / hot-side contact | modeled / detail deferred | FG-1 / FG-14 / FG-15 | Modeled as `ebf3_gun_cathode_hot_contact_pair` under the cartridge; exact material and joint geometry are not EBF3-confirmed. | Select contact material and weld/clamp/service geometry. | cathode cluster |
| FG-D-005 | Heater leads / hot-side conductor details | modeled / detail deferred | FG-14 | Modeled as `ebf3_gun_cathode_current_lead_pair` plus `ebf3_gun_cathode_lead_termination_set`; specific conductor and termination details remain unresolved. | Select lead material, gauge, thermal transition, and termination method. | cathode cluster |
| FG-D-006 | Ceramic beads/sleeves or standoffs | modeled / detail deferred | FG-14 / FG-15 | Modeled as `ebf3_gun_cathode_ceramic_standoff_set`; exact geometry and metallization remain unresolved. | Source/select heater-lead or cartridge insulation geometry. | cathode cluster |
| FG-D-007 | Cartridge body / holder | modeled / detail deferred | FG-15 | Modeled as `ebf3_gun_cathode_cartridge_base`; cartridge datum geometry remains unresolved. | Find cartridge drawing or service description. | cathode cluster |
| FG-D-008 | Clamp or locating seat | modeled / detail deferred | FG-15 | Modeled as `ebf3_gun_cathode_locating_clamp`; exact locating/retention mechanism remains unresolved. | Source cartridge locating/retention mechanism. | cathode cluster |
| FG-D-009 | Cartridge electrical contact | modeled / detail deferred | FG-15 / FG-14 | Ownership assigned to cartridge via `ebf3_gun_cathode_hot_contact_pair`; lead side terminates into FG-14 child items. | Resolve exact lead-to-contact joint geometry. | cathode cluster |
| FG-D-010 | Cathode radiation shield sheet set | modeled / detail deferred | FG-16 | Modeled as `ebf3_gun_cathode_radiation_shield_foil_stack`; HeatWave and IUAC sources support cathode heat-shield hardware in electron-gun/thermionic-gun packages. EBF3 geometry remains unresolved. | Source shield geometry in selected cathode architecture. | cathode cluster |
| FG-D-011 | Radiation shield spacers/clips | modeled / detail deferred | FG-16 | Modeled as shield spacer/clip children only as package markers. Sources support the heat-shield class, but exact support details remain unresolved. | Source shield support details. | cathode cluster |
| FG-D-012 | Replaceable anode aperture insert | defer | FG-2 | Precision aperture sources are generic; EBF3 anode insert not confirmed. | Find anode drawing or source explicitly showing replaceable insert. | electrode family |
| FG-D-013 | Anode cooling insert / heat spreader | defer | FG-2 | Candidate-only; no source-specific heat-load design. | Add anode thermal/cooling source. | electrode family |
| FG-D-015 | Control-electrode aperture edge or insert | defer | FG-3 | Aperture is plausible, but independent insert is not confirmed. | Source control-electrode geometry. | electrode family |
| FG-D-016 | Control-electrode bias contact | split_boundary / defer | FG-3 / FG-19 / power supplies | Electrode load, wiring, and bias supply cross boundaries. | Model electrical interface across gun wiring and power supplies. | electrode family |
| FG-D-018 | Metallized ceramic ends/collars | defer | FG-4 | Generic ceramic-to-metal practice; not confirmed for FG-4. | Source insulator construction. | electrode family |
| FG-D-019 | Mounting washer or clamp for insulator | defer | FG-4 / FG-17 | Boundary-sensitive with gun column hardware. | Source mechanical mount layout. | electrode family |
| FG-D-020 | Screen-electrode aperture edge or insert | defer | FG-5 | Candidate-only; generic aperture source. | Source screen/boundary electrode geometry. | electrode family |
| FG-D-021 | Screen-electrode electrical connection | split_boundary / defer | FG-5 / FG-19 | Contact geometry and wiring ownership unresolved. | Resolve local gun wiring/contact interface. | electrode family |
| FG-D-022 | Lens coil material/process readiness | material/process readiness | FG-6 / FG-7 | Coil leaf review treats the lens coil as the BOM leaf. Bobbin/former/potting should not become child items unless a later source shows distinct hardware. | Select conductor, insulation, winding method, vacuum compatibility, and test requirements. | electromagnetic lens; coil leaf review |
| FG-D-023 | Lens coil electrical interface | split_boundary / defer | FG-6 / FG-7 / FG-19 / power supplies | Coil pigtail, gun wiring, and regulated current supply ownership are not yet selected. | Resolve coil-to-gun-wiring and coil-to-current-supply boundary. | electromagnetic lens; coil leaf review |
| FG-D-024 | Lens mounting structure/interface | defer | FG-6 / FG-7 / FG-17 | Source is generic or patent-geometry-specific; boundary with gun column. | Source EBF3 lens mounting layout. | electromagnetic lens |
| FG-D-028 | Stigmator | defer | FG-6 / FG-7 | Generic candidate only. | Need EBF3-specific or comparable gun source. | electromagnetic lens |
| FG-D-029 | Lens aperture | split_boundary / defer | FG-6 / FG-7 / electrodes | Aperture-like functions already exist in electrode family. | Revisit only if source shows aperture integrated into lens package. | electromagnetic lens |
| FG-D-030 | Lens cooling jacket / heat sink | defer | FG-6 / FG-7 | Generic thermal candidate; not EBF3 lens-level evidence. | Source thermal design or coil-level heat-load requirement. | electromagnetic lens |
| FG-D-031 | Deflection coil material/process readiness | material/process readiness | FG-8 | Coil leaf review treats X/Y coil pairs as BOM leaves. Bobbin/former/potting should not become child items unless a later source shows distinct hardware. | Select conductor, insulation, winding pattern, vacuum compatibility, inductance/current limits, and test requirements. | magnetic steering; coil leaf review |
| FG-D-032 | Deflection magnetic-core/yoke boundary | split_boundary / defer | FG-8 | Patent-specific magnetic core/bobbin language may overlap the already-modeled `ebf3_gun_deflection_magnetic_yoke`. | Source EBF3 deflection magnetic circuit geometry before changing the yoke/coil boundary. | magnetic steering; coil leaf review |
| FG-D-033 | Deflection coil electrical interface | split_boundary / defer | FG-8 / FG-19 / power supplies | Coil leaf review confirmed electrical boundary with driver and gun harness remains unresolved. | Resolve coil load-to-driver interface. | magnetic steering; coil leaf review |
| FG-D-035 | Deflection mount or bracket | split_boundary / defer | FG-8 / FG-17 | Mount/bracket ownership remains unresolved with gun column. | Source physical mounting layout. | magnetic steering; coil leaf review |
| FG-D-036 | Deflection cooling / thermal features | defer | FG-8 | Do not model separate cooling hardware unless heat-load evidence requires it. | Source coil thermal design if needed. | magnetic steering; coil leaf review |
| FG-D-037 | Trajectory-corrector magnetic coil set | modeled / detail deferred | FG-11 | Modeled as `ebf3_gun_trajectory_corrector_coil_set`; external electron-lens source supports coils for correcting electron-beam trajectory. Corrector geometry and magnetic-versus-electrostatic architecture remain unresolved. | Source EBF3 corrector implementation or decide architecture. | magnetic steering |
| FG-D-039 | Corrector yoke / pole structure | defer | FG-11 | Would risk duplicating FG-8 or lens yokes. | Source FG-11-specific geometry. | magnetic steering |
| FG-D-040 | Corrector power/signal leads | split_boundary / defer | FG-11 / power supplies / controls | Load may be in gun; regulated source and commands are outside gun. | Resolve driver/control ownership. | magnetic steering |
| FG-D-041 | Beam-boundary collector / intercept surface | modeled / detail deferred | FG-9 | Modeled as `ebf3_gun_beam_boundary_collector_electrode`; destructive/edge/partial-intercept geometry and heat load remain unknown. | Source EBF3 or comparable boundary pickup geometry. | beam diagnostics |
| FG-D-042 | Beam dump / heat sink body | defer | FG-9 | Faraday-cup references may over-model FG-9. | Source heat-load and interception design. | beam diagnostics |
| FG-D-043 | Ground shield / guard cylinder | defer | FG-9 | Generic Faraday-cup shield, not EBF3 pickup-specific. | Source pickup shielding layout. | beam diagnostics |
| FG-D-044 | Suppression or bias electrode | defer | FG-9 / FG-10 / power supplies | Real diagnostic option, but bias supply crosses boundary. | Source pickup bias design and assign supply owner. | beam diagnostics |
| FG-D-045 | Diagnostic ceramic/high-resistance insulator | modeled / detail deferred | FG-9 / FG-10 | Modeled as local pickup insulators under FG-9 and FG-10; feedthrough insulation remains unresolved. | Source pickup/feedthrough construction. | beam diagnostics |
| FG-D-046 | Secondary-electron ring collector | modeled / detail deferred | FG-10 | Modeled as `ebf3_gun_secondary_electron_ring_collector` based on EBW secondary-current sources; BINP still does not define EBF3 geometry. | Source EBF3 secondary pickup shape. | beam diagnostics |
| FG-D-047 | Secondary-electron plate collector | defer | FG-10 | User-derived candidate; current web sources support ring more than plate. | Add source for plate collector or drop in later review. | beam diagnostics |
| FG-D-048 | Local diagnostic signal lead | modeled / detail deferred | FG-9 / FG-10 / FG-19 | Modeled as `ebf3_gun_local_diagnostic_signal_lead_set` under FG-19; cable class and exact pickup-to-feedthrough routing remain unresolved. | Select physical pickup-to-feedthrough routing and in-vacuum cable class. | beam diagnostics |
| FG-D-049 | Vacuum signal feedthrough insert | modeled / detail deferred | FG-19 / cabin / controls | Modeled as `ebf3_gun_diagnostic_signal_feedthrough_insert` under FG-19. Cabin owns passive port/flange or shared plate, and controls own acquisition. Coax/multipin/shared-plate topology and pinout remain unresolved. | Select physical feedthrough topology, pinout, connector family, and service boundary. | beam diagnostics; interface architecture |
| FG-D-051 | Diagnostic grounding/shield termination | modeled / detail deferred | FG-19 / controls | Modeled as `ebf3_gun_signal_shield_termination_interface` under FG-19. This keeps signal shielding separate from protective ground, HV return, beam-current continuity, and controls acquisition. Final termination policy is still not selected. | Source/select instrumentation shield termination, isolation, and grounding policy. | beam diagnostics; HV grounding return; interface architecture |
| FG-D-052 | HV input central conductor | modeled / detail deferred | FG-12 | Modeled as `ebf3_gun_hv_input_central_conductor`; material, diameter, creepage clearance, and joint details remain unresolved. | Select conductor material, geometry, clearance, and joint method. | HV gun-side insulation; HV tank interface |
| FG-D-053 | HV input ceramic feedthrough body | modeled / detail deferred | FG-12 / FG-13 | Current interface architecture keeps FG-12 as gun-side HV input and models FG-13 as the standalone HV-insulator package. Final ceramic feedthrough integration versus standalone construction is still unresolved. | Source/select final FG-12/FG-13 ceramic integration geometry before material/process closure. | HV gun-side insulation; HV tank interface; interface architecture |
| FG-D-054 | HV input metal flange/housing | modeled / detail deferred | FG-12 / FG-17 / cabin | Modeled as `ebf3_gun_hv_input_flange_housing`; overlap with gun column and chamber-side interface remains unresolved. | Select physical HV input layout and flange/gun-column boundary. | HV gun-side insulation; HV tank interface |
| FG-D-055 | HV cable-side / gun-side termination | modeled / detail deferred | FG-12 / HV tank | Current HV path is selected. Tank-side receiving interface is represented by `ebf3_tank_side_bushing_cable_socket_interface`; gun-side receiving interface is represented by `ebf3_gun_hv_input_receiving_terminal`. Exact connector/socket geometry, stress-control transition, and service boundary remain unresolved. | Source tank-side connector/socket and gun-side receiving-terminal geometry before material/process closure or connector-family split. | HV gun-side insulation; HV tank interface; interface architecture |
| FG-D-056 | Corona shield / field-grading shield | modeled / detail deferred | FG-12 / FG-13 / HV-8 | Current BOM has local field-grading markers under HV-8 and FG-13. Final shield/ring geometry, potential connection, and whether cable-side stress control needs separate parts remain unresolved. | Source HV input/insulator/bushing field-grading geometry before material/process closure or further split. | HV gun-side insulation; HV tank interface; interface architecture |
| FG-D-057 | Standalone HV ceramic insulator body | modeled / detail deferred | FG-13 | Modeled as `ebf3_gun_hv_insulator_ceramic_body` under `bom_ebf3_gun_hv_insulator`. Exact geometry, ceramic grade, dielectric rating, and manufacturing process remain unresolved. | Source/select FG-13 construction. | HV gun-side insulation; HV tank interface |
| FG-D-058 | HV insulator metallized ends/collars | modeled / detail deferred | FG-13 | Modeled as metallized end-interface and mounting collar markers under FG-13. Metallization stack, joining method, collar geometry, and vacuum/HV test details remain unresolved. | Source/select metallized insulator construction. | HV gun-side insulation; HV tank interface |
| FG-D-059 | Gun-side oil volume | defer | FG-18 / HV tank | BINP lists oil tank/silicon oil; PTR/JEOL support oil-filled or high-voltage tank practice; BNL supports high-dielectric fluid around a gun HV connector; US3133227A supports an electron-gun assembly submerged in an oil tank. These support the package class, but not a separate EBF3 gun-side bulk oil inventory. | Source EBF3-specific separate gun-side oil volume before creating a child item or using for material closure. | HV gun-side insulation; HV tank interface |
| FG-D-060 | Gun-side oil tank shell/lid | defer | FG-18 | Sources support electron-gun/HV oil-tank package class, but not EBF3-specific shell/lid geometry. Removed previous child items to avoid overclaiming. | Source separate gun-side oil shell/lid geometry. | HV gun-side insulation; HV tank interface |
| FG-D-061 | Silicone oil under gun-side oil tank | split_boundary / defer | FG-18 / HV tank | Current interface architecture assigns the confirmed main insulating fluid to the HV tank. No second gun-side bulk-fluid inventory is confirmed. | Confirm separate gun-side oil volume before treating it as material closure. | HV gun-side insulation; HV tank interface; interface architecture |
| FG-D-062 | Oil-compatible seals/supports | defer | FG-18 | Oil-tank package class is supported, but seal material and geometry remain unresolved. Removed previous child item to avoid overclaiming. | Source oil-tank package design. | HV gun-side insulation; HV tank interface |
| FG-D-063 | HV/gun grounding interface | split_boundary / defer | FG-18 / FG-17 / HV tank | Current interface architecture separates protective bonding, HV source return/reference, beam-current continuity, and low-voltage sensing. Physical gun-to-tank conductor topology remains unresolved. | Source/select gun-to-tank grounding and return topology. | HV gun-side insulation; HV tank interface; HV grounding return; interface architecture |
| FG-D-064 | Gun-side mating flange or datum | modeled / detail deferred | FG-17 / MC-5 | Gun-side flange modeled as `ebf3_gun_column_gun_side_mating_flange`; chamber-side port remains MC-5. Gasket/bolts/interface geometry remain unresolved. | Source gun/chamber interface drawing. | gun column |
| FG-D-066 | Vacuum gasket/seal at gun/chamber interface | split_boundary / defer | MC-5 / FG-17 | Seal ownership and service kit boundary unknown. | Source interface hardware or define serviceable seal policy. | gun column |
| FG-D-067 | Bolt pattern / interface fasteners | split_boundary / defer | MC-5 / FG-17 | Bolted flange concept exists; ownership unresolved. | Source interface drawing. | gun column |
| FG-D-068 | Internal electrode/lens support brackets | modeled / detail deferred | FG-17 / electrodes / lenses | Modeled as `ebf3_gun_column_internal_support_frame`; individual electrode/lens brackets remain unresolved to avoid duplication. | Source internal column layout. | gun column |
| FG-D-069 | Optical-axis locating datum | modeled / detail deferred | FG-17 | Modeled as `ebf3_gun_column_optical_axis_datum_set`; exact datum geometry and tolerances remain unresolved. | Source alignment/datum layout. | gun column |
| FG-D-070 | Grounding structure or return path | split_boundary / defer | FG-17 / HV tank / power supplies / positioning | Current interface architecture separates return/grounding roles across subsystems, but the physical return conductor, cabinet bus, chamber bond, and platform connection topology are not source-fixed. | Source/select physical return path before adding gun-column child hardware. | gun column; HV grounding return; interface architecture |
| FG-D-071 | Gun-side wire-feeder mounting datum | split_boundary / defer | FG-17 / WF-26 | Feeder attaches to gun, but removable vs integral datum unknown. | Source feeder/gun mechanical interface. | gun column |
| FG-D-073 | HV-input mounting boss/flange | split_boundary / defer | FG-17 / FG-12 | FG-12 now owns local HV input flange/housing; any column-side boss remains unresolved. | Source HV input mounting geometry. | gun column |
| FG-D-074 | Signal/feedthrough mounting points | defer | FG-17 / FG-19 / cabin | Boundary-sensitive with diagnostics and cabin feedthroughs. | Resolve signal feedthrough ownership. | gun column |
| FG-D-075 | Air-cooling jacket, fins, or duct | defer | FG-17 / cabin / controls | EBF3 source says air-cooled, but hardware geometry/ownership unknown. | Source cooling hardware layout. | gun column |

## Next Work Queue From This Register

1. `hv_oil_service_review`: resolve the HV-13 split items before decomposing
   fill/drain, pressure relief, level indicator, seals, and oil service
   hardware.
2. Use `hv_grounding_return_review` before adding grounding or return child
   items. It resolves ownership rules, not physical return topology.
3. `electrical_signal_boundary_followup`: use `ebf3_interface_architecture` as
   the ownership baseline. FG-D-049 and FG-D-051 now have minimal interface
   markers under FG-19. FG-D-016, FG-D-021, FG-D-040, and FG-D-074 remain
   deferred; create child items only after physical contact, driver, mount, or
   feedthrough geometry is selected.
4. `beam_diagnostics_detail_review`: FG-D-041, FG-D-045, FG-D-046, FG-D-048,
   FG-D-049, and FG-D-051 now have minimal Level-3 KB representation. FG-D-042,
   FG-D-043, FG-D-044, and FG-D-047 remain deferred.
5. `tungsten_cathode_package_review`: FG-D-002A now selects direct-heated
   tungsten hairpin/filament as the package direction. FG-D-004 through FG-D-009
   have minimal Level-3 KB representation, but material, dimensions, contact
   method, and ceramic geometry remain deferred. FG-D-010 and FG-D-011 now have
   modeled shield package markers, but shield geometry/material details remain
   unresolved.
6. `hv_gun_side_input_detail_review`: FG-D-052 through FG-D-058 now have
   minimal Level-3 KB representation across HV-8, FG-12, and FG-13. Final
   connector geometry, ceramic/feedthrough integration, field-grading geometry,
   and HV material/process readiness remain deferred. FG-D-059 through FG-D-062 are deferred; the previous
   package child split was removed because package-class sources are not enough
   to justify EBF3-specific shell/lid/oil/seal children.
7. `manufacture_cabin_interface_review`: address FG-D-064, FG-D-066, and
   FG-D-067 before deeper cabin/gun interface decomposition.
8. `gun_column_detail_review`: FG-D-064, FG-D-068, and FG-D-069 now have
   minimal Level-3 KB representation. FG-D-066, FG-D-067, FG-D-070 through
   FG-D-075 remain deferred or split-boundary.
9. `coil_material_process_readiness_review`: address FG-D-022, FG-D-023,
   FG-D-031, FG-D-032, FG-D-033, FG-D-035, and FG-D-036 as coil leaf readiness
   and interface work. Do not use these rows as permission to create lower
   coil child BOMs.
