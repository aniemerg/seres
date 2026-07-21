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

Source plans:

- `research/ebf3_bom_sources/organized/electromagnetic_lens_decomposition_plan.md`
- `research/ebf3_bom_sources/organized/cathode_cluster_decomposition_plan.md`
- `research/ebf3_bom_sources/organized/hv_gun_side_insulation_decomposition_plan.md`
- `research/ebf3_bom_sources/organized/beam_diagnostics_decomposition_plan.md`
- `research/ebf3_bom_sources/organized/magnetic_steering_decomposition_plan.md`
- `research/ebf3_bom_sources/organized/electrode_family_decomposition_plan.md`
- `research/ebf3_bom_sources/organized/gun_column_decomposition_plan.md`

Workflow references:

- `research/ebf3_bom_sources/README.md`
- `research/ebf3_bom_sources/derived/ebf3_subsystem_boundaries.md`

## Status Use

- `defer`: keep visible, but do not create a KB item until the unblock condition
  is satisfied.
- `split_boundary`: keep out of the fixed-gun BOM unless the owning subsystem or
  parent item is changed by a later boundary review.
- `split_boundary / defer`: real candidate, but both ownership and geometry are
  unresolved.
- `reject_for_this_parent`: do not create this as a child under the current
  parent. It may still be represented by the existing parent item or by a later
  variant review.

## Priority Buckets

| Bucket | Meaning | Current examples |
| --- | --- | --- |
| Architecture decision needed | Cannot proceed until a variant or layout is selected. | Cathode architecture, gun-side oil volume, trajectory corrector implementation. |
| Boundary decision needed | Candidate crosses subsystem or parent boundaries. | HV cable/gun termination, chamber gun port, signal feedthrough, DAQ, current drivers. |
| Later child-level plan | Candidate belongs below an already-adopted child assembly. | Lens coil insulation, deflection coil insulation, bobbin/former, coil leads. |
| Source geometry needed | Function is supported, but exact EBF3 geometry is not. | Beam-boundary collector, secondary-electron collector, aperture inserts, gun-column flange. |
| Manufacturing readiness only | Candidate should not become a BOM child yet; it belongs to later material/process review. | Stainless vacuum material choices, ceramic metallization, cooling and thermal features. |

## Near-Term Recommendations

1. Do not add recipes or local closure for any item in this register.
2. Before starting HV tank decomposition, review all rows tagged `HV tank`,
   `FG-12`, `FG-13`, and `FG-18`.
3. Before starting controls decomposition, review rows tagged `controls`,
   `DAQ`, `signal`, `driver`, and `bias`.
4. Coil-level review is recorded in
   `research/ebf3_bom_sources/organized/coil_level_decomposition_plan.md`; its
   unresolved rows should feed a later electrical-interface or material/process
   readiness review, not immediate child BOM creation.
5. Before deeper cathode decomposition, choose or explicitly model cathode
   variants instead of mixing tantalum-foil, LaB6 carbon-rod, and LaB6
   cup/filament architectures.

## Register

| ID | Candidate | Status | Applies to | Blocker / reason not modeled now | Next unblock condition | Source plan |
| --- | --- | --- | --- | --- | --- | --- |
| FG-D-001 | Tantalum foil cathode variant | defer | FG-1 | BINP supports tantalum foil in a comparable gun, while EBF3 space source supports LaB6. | Decide cathode variant policy or model explicit cathode variants. | cathode cluster |
| FG-D-002 | LaB6 cathode variant | defer | FG-1 | EBF3 source supports LaB6, but external LaB6 architectures differ. | Add architecture-specific source or variant policy. | cathode cluster |
| FG-D-003 | Cathode emitter child below FG-1 | reject_for_this_parent | FG-1 / FG-15 | Would duplicate `ebf3_gun_cathode` unless FG-1 is redefined as an assembly. | Redefine FG-1 as cathode assembly, or keep FG-1 as emitter leaf. | cathode cluster |
| FG-D-004 | Heater contact / hot-side contact | defer | FG-1 / FG-14 / FG-15 | Real in sources, but architecture varies across cathode types. | Select cathode architecture and source its heater/contact geometry. | cathode cluster |
| FG-D-005 | Heater leads / hot-side conductor details | defer | FG-14 | FG-14 is justified, but specific leads are not EBF3-confirmed. | Add EBF3-like heater lead/cartridge drawing or source. | cathode cluster |
| FG-D-006 | Ceramic beads/sleeves for heater leads | defer | FG-14 | Supported in one LaB6 gun architecture, not confirmed for EBF3. | Source heater-lead insulation geometry for selected cathode. | cathode cluster |
| FG-D-007 | Cartridge body / holder | defer | FG-15 | BINP supports cartridge existence, not exact child structure. | Find cartridge drawing or service description. | cathode cluster |
| FG-D-008 | Clamp or locating seat | defer | FG-15 | Candidate remains plausible but not source-converged. | Source cartridge locating/retention mechanism. | cathode cluster |
| FG-D-009 | Cartridge electrical contact | defer | FG-15 / FG-14 | Boundary-sensitive with heater leads and emitter. | Resolve cathode cartridge and heater-lead boundary. | cathode cluster |
| FG-D-010 | Cathode radiation shield sheet set | defer | FG-16 | Supported generically for high-temperature cathodes; FG-16 remains inference-heavy. | Source shield geometry in selected cathode architecture. | cathode cluster |
| FG-D-011 | Radiation shield spacers/clips | defer | FG-16 | External architecture does not justify EBF3 child items. | Source shield support details. | cathode cluster |
| FG-D-012 | Replaceable anode aperture insert | defer | FG-2 | Precision aperture sources are generic; EBF3 anode insert not confirmed. | Find anode drawing or source explicitly showing replaceable insert. | electrode family |
| FG-D-013 | Anode cooling insert / heat spreader | defer | FG-2 | Candidate-only; no source-specific heat-load design. | Add anode thermal/cooling source. | electrode family |
| FG-D-014 | Anode body child under anode parent | reject_for_this_parent | FG-2 | Would duplicate `ebf3_gun_anode`. | Redefine FG-2 as a larger anode assembly if source requires. | electrode family |
| FG-D-015 | Control-electrode aperture edge or insert | defer | FG-3 | Aperture is plausible, but independent insert is not confirmed. | Source control-electrode geometry. | electrode family |
| FG-D-016 | Control-electrode bias contact | split_boundary / defer | FG-3 / FG-19 / power supplies | Electrode load, wiring, and bias supply cross boundaries. | Model electrical interface across gun wiring and power supplies. | electrode family |
| FG-D-017 | Control-electrode ceramic body child | reject_for_this_parent | FG-4 | Would duplicate `ebf3_gun_control_electrode_insulator`. | Only revisit if FG-4 is redefined as an assembly. | electrode family |
| FG-D-018 | Metallized ceramic ends/collars | defer | FG-4 | Generic ceramic-to-metal practice; not confirmed for FG-4. | Source insulator construction. | electrode family |
| FG-D-019 | Mounting washer or clamp for insulator | defer | FG-4 / FG-17 | Boundary-sensitive with gun column hardware. | Source mechanical mount layout. | electrode family |
| FG-D-020 | Screen-electrode aperture edge or insert | defer | FG-5 | Candidate-only; generic aperture source. | Source screen/boundary electrode geometry. | electrode family |
| FG-D-021 | Screen-electrode electrical connection | split_boundary / defer | FG-5 / FG-19 | Contact geometry and wiring ownership unresolved. | Resolve local gun wiring/contact interface. | electrode family |
| FG-D-022 | Lens bobbin / coil former | defer | FG-6 / FG-7 | Coil-level review found no source-confirmed distinct EBF3 former. | Source distinct lens-coil former geometry. | electromagnetic lens; coil-level |
| FG-D-023 | Lens coil insulation / sealing / potting | defer | FG-6 / FG-7 | Coil-level review keeps this as material/process readiness, not a child BOM item. | Material/process review for vacuum-compatible coil insulation. | electromagnetic lens; coil-level |
| FG-D-024 | Lens mounting structure/interface | defer | FG-6 / FG-7 / FG-17 | Source is generic or patent-geometry-specific; boundary with gun column. | Source EBF3 lens mounting layout. | electromagnetic lens |
| FG-D-025 | Lens regulated current supply | split_boundary | FG-6 / FG-7 / power supplies | Load belongs to lens; regulated source belongs to power supplies. | Handle in power-supplies subsystem. | electromagnetic lens |
| FG-D-026 | Deflection coils as lens child | split_boundary | FG-6 / FG-7 / FG-8 | Already represented by FG-8. | Keep separate unless source merges lens and deflection package. | electromagnetic lens |
| FG-D-027 | Trajectory correction coils/plates as lens child | split_boundary | FG-6 / FG-7 / FG-11 | Already represented by FG-11. | Keep separate unless source merges corrector into lens package. | electromagnetic lens |
| FG-D-028 | Stigmator | defer | FG-6 / FG-7 | Generic candidate only. | Need EBF3-specific or comparable gun source. | electromagnetic lens |
| FG-D-029 | Lens aperture | defer / split_boundary | FG-6 / FG-7 / electrodes | Aperture-like functions already exist in electrode family. | Revisit only if source shows aperture integrated into lens package. | electromagnetic lens |
| FG-D-030 | Lens cooling jacket / heat sink | defer | FG-6 / FG-7 | Generic thermal candidate; not EBF3 lens-level evidence. | Source thermal design or coil-level heat-load requirement. | electromagnetic lens |
| FG-D-031 | Deflection coil former / bobbin | defer | FG-8 | Coil-level review found patent-specific magnetic core/bobbin may overlap existing deflection yoke. | Source EBF3 deflection coil pair geometry or revise yoke/core boundary. | magnetic steering; coil-level |
| FG-D-032 | Deflection coil insulation | defer | FG-8 | Coil-level review keeps this as material/process readiness, not a child BOM item. | Material/process review for vacuum-compatible coil insulation. | magnetic steering; coil-level |
| FG-D-033 | Deflection coil leads / terminations | split_boundary / defer | FG-8 / FG-19 / power supplies | Coil-level review confirmed electrical boundary with driver and gun harness remains unresolved. | Resolve coil load-to-driver interface. | magnetic steering; coil-level |
| FG-D-034 | Deflection current amplifier / driver | split_boundary | FG-8 / power supplies / controls | Driver is outside fixed-gun hardware BOM. | Handle in power supplies or controls. | magnetic steering |
| FG-D-035 | Deflection mount or bracket | split_boundary / defer | FG-8 / FG-17 | Coil-level review keeps mount/bracket boundary unresolved with gun column. | Source physical mounting layout. | magnetic steering; coil-level |
| FG-D-036 | Deflection cooling / thermal features | defer | FG-8 | Coil-level review found no source-specific heat-load evidence. | Source coil thermal design. | magnetic steering; coil-level |
| FG-D-037 | Trajectory-corrector magnetic coil set | defer | FG-11 | Corrector function is supported, geometry is not. | Source corrector implementation or decide architecture. | magnetic steering |
| FG-D-038 | Trajectory-corrector electrostatic plates | reject_for_this_parent | FG-11 | Current targeted sources support magnetic correction more strongly. | Reopen only if direct electrostatic-corrector source appears. | magnetic steering |
| FG-D-039 | Corrector yoke / pole structure | defer | FG-11 | Would risk duplicating FG-8 or lens yokes. | Source FG-11-specific geometry. | magnetic steering |
| FG-D-040 | Corrector power/signal leads | split_boundary / defer | FG-11 / power supplies / controls | Load may be in gun; regulated source and commands are outside gun. | Resolve driver/control ownership. | magnetic steering |
| FG-D-041 | Beam-boundary collector / intercept surface | defer | FG-9 | Pickup exists, but destructive/edge/partial-intercept geometry unknown. | Source EBF3 or comparable boundary pickup geometry. | beam diagnostics |
| FG-D-042 | Beam dump / heat sink body | defer | FG-9 | Faraday-cup references may over-model FG-9. | Source heat-load and interception design. | beam diagnostics |
| FG-D-043 | Ground shield / guard cylinder | defer | FG-9 | Generic Faraday-cup shield, not EBF3 pickup-specific. | Source pickup shielding layout. | beam diagnostics |
| FG-D-044 | Suppression or bias electrode | defer | FG-9 / FG-10 / power supplies | Real diagnostic option, but bias supply crosses boundary. | Source pickup bias design and assign supply owner. | beam diagnostics |
| FG-D-045 | Diagnostic ceramic/high-resistance insulator | defer | FG-9 / FG-10 / FG-19 | Insulation is real; form and feedthrough ownership unresolved. | Source pickup/feedthrough construction. | beam diagnostics |
| FG-D-046 | Secondary-electron ring collector | defer | FG-10 | EBW source supports ring collector; BINP does not define FG-10 geometry. | Source EBF3 secondary pickup shape. | beam diagnostics |
| FG-D-047 | Secondary-electron plate collector | defer | FG-10 | User-derived candidate; current web sources support ring more than plate. | Add source for plate collector or drop in later review. | beam diagnostics |
| FG-D-048 | Local diagnostic signal lead | defer | FG-9 / FG-10 / FG-19 | Plausible, but feedthrough and DAQ ownership unresolved. | Resolve local pickup-to-feedthrough signal path. | beam diagnostics |
| FG-D-049 | Vacuum signal feedthrough insert | split_boundary / defer | FG-19 / cabin / controls | Cabin owns port/flange, gun owns local wiring, controls owns acquisition. | Decide physical feedthrough insert ownership. | beam diagnostics |
| FG-D-050 | External ammeter / digitizer / DAQ | split_boundary | controls | External measurement electronics are not gun hardware. | Handle in controls subsystem. | beam diagnostics |
| FG-D-051 | Diagnostic grounding/shield termination | defer | FG-19 / controls | Boundary with controls harness and chamber ground remains unresolved after system return review. | Source/select instrumentation shield termination policy. | beam diagnostics; HV grounding return |
| FG-D-052 | HV input central conductor | defer | FG-12 | HV tank interface review keeps this under gun-side input, but construction is not sourced. | Source gun-side HV input construction. | HV gun-side insulation; HV tank interface |
| FG-D-053 | HV input ceramic feedthrough body | split_boundary / defer | FG-12 / FG-13 | HV tank interface review confirms duplication risk between FG-12 and FG-13 remains. | Decide FG-12 vs FG-13 ownership from source geometry. | HV gun-side insulation; HV tank interface |
| FG-D-054 | HV input metal flange/housing | defer | FG-12 / FG-17 / cabin | HV tank interface review keeps this deferred due to overlap with gun column and chamber interface. | Source physical HV input layout. | HV gun-side insulation; HV tank interface |
| FG-D-055 | HV cable-side termination | split_boundary | FG-12 / HV tank | HV tank interface review keeps main cable in HV tank and gun-side receiving termination under FG-12. | Source tank-side and gun-side termination geometry before child split. | HV gun-side insulation; HV tank interface |
| FG-D-056 | Corona shield / field-grading shield | defer | FG-12 / FG-13 / HV-8 | HV tank interface review confirms this may belong tank-side or gun-side. | Source HV input/insulator/bushing field grading geometry. | HV gun-side insulation; HV tank interface |
| FG-D-057 | Standalone HV ceramic insulator body | defer | FG-13 | HV tank interface review keeps FG-13 as unresolved standalone-vs-feedthrough marker. | Source FG-13 construction. | HV gun-side insulation; HV tank interface |
| FG-D-058 | HV insulator metallized ends/collars | defer | FG-13 | Generic ceramic-to-metal practice; not EBF3-specific. | Source metallized insulator construction. | HV gun-side insulation; HV tank interface |
| FG-D-059 | Gun-side oil volume | defer | FG-18 / HV tank | HV tank interface review keeps FG-18 as boundary marker only; main oil belongs to HV tank. | Source separate gun-side oil volume. | HV gun-side insulation; HV tank interface |
| FG-D-060 | Gun-side oil tank shell/lid | defer | FG-18 | No separate gun-side oil volume package sourced. | Source separate gun-side oil shell/lid geometry. | HV gun-side insulation; HV tank interface |
| FG-D-061 | Silicone oil under gun-side oil tank | split_boundary / defer | FG-18 / HV tank | HV tank interface review assigns main silicone oil to `ebf3_hv_transformer_insulating_fluid`. | Add only if separate gun-side oil volume is confirmed. | HV gun-side insulation; HV tank interface |
| FG-D-062 | Oil-compatible seals/supports | defer | FG-18 | Plausible but no separate gun-side oil package source. | Source oil-tank package design. | HV gun-side insulation; HV tank interface |
| FG-D-063 | HV/gun grounding interface | split_boundary / defer | FG-18 / FG-17 / HV tank | HV grounding return review confirms protective grounding, HV return, and beam-current return must remain separate. | Source/select gun-to-tank grounding and return topology. | HV gun-side insulation; HV tank interface; HV grounding return |
| FG-D-064 | Gun-side mating flange or datum | split_boundary / defer | FG-17 / MC-5 | Insertion/flange concept supported, but gun-side/chamber-side split unknown. | Source gun/chamber interface drawing. | gun column |
| FG-D-065 | Chamber-side gun mounting port/flange | split_boundary | MC-5 | Owned by manufacture cabin. | Handle in manufacture-cabin decomposition. | gun column |
| FG-D-066 | Vacuum gasket/seal at gun/chamber interface | split_boundary / defer | MC-5 / FG-17 | Seal ownership and service kit boundary unknown. | Source interface hardware or define serviceable seal policy. | gun column |
| FG-D-067 | Bolt pattern / interface fasteners | split_boundary / defer | MC-5 / FG-17 | Bolted flange concept exists; ownership unresolved. | Source interface drawing. | gun column |
| FG-D-068 | Internal electrode/lens support brackets | defer | FG-17 / electrodes / lenses | User-derived only and may duplicate child mounting features. | Source internal column layout. | gun column |
| FG-D-069 | Optical-axis locating datum | defer | FG-17 | Important but not source-defined. | Source alignment/datum layout. | gun column |
| FG-D-070 | Grounding structure or return path | split_boundary / defer | FG-17 / HV tank / power supplies / positioning | Electrical return spans subsystems; system boundary model exists but topology is not source-fixed. | Source/select physical return path before adding gun-column child hardware. | gun column; HV grounding return |
| FG-D-071 | Gun-side wire-feeder mounting datum | split_boundary / defer | FG-17 / WF-26 | Feeder attaches to gun, but removable vs integral datum unknown. | Source feeder/gun mechanical interface. | gun column |
| FG-D-072 | Wire-feeder removable bracket | split_boundary | WF-26 | Owned by wire feeder unless proven integral to gun column. | Handle in wire-feeder decomposition. | gun column |
| FG-D-073 | HV-input mounting boss/flange | defer | FG-17 / FG-12 | Boundary-sensitive with HV input and gun-side insulation. | Source HV input mounting geometry. | gun column |
| FG-D-074 | Signal/feedthrough mounting points | defer | FG-17 / FG-19 / cabin | Boundary-sensitive with diagnostics and cabin feedthroughs. | Resolve signal feedthrough ownership. | gun column |
| FG-D-075 | Air-cooling jacket, fins, or duct | defer | FG-17 / cabin / controls | EBF3 source says air-cooled, but hardware geometry/ownership unknown. | Source cooling hardware layout. | gun column |

## Next Work Queue From This Register

1. `hv_oil_service_review`: resolve the HV-13 split items before decomposing
   fill/drain, pressure relief, level indicator, seals, and oil service
   hardware.
2. Use `hv_grounding_return_review` before adding grounding or return child
   items. It resolves ownership rules, not physical return topology.
3. `controls_signal_boundary_review`: address FG-D-016, FG-D-021, FG-D-040,
   FG-D-049, FG-D-050, FG-D-051, and FG-D-074 before decomposing controls.
4. `cathode_variant_review`: address FG-D-001 through FG-D-011 before creating
   cathode child BOMs.
5. `manufacture_cabin_interface_review`: address FG-D-064 through FG-D-067 and
   FG-D-065 before cabin decomposition.
6. `coil_material_process_readiness_review`: address FG-D-022, FG-D-023,
   FG-D-031, FG-D-032, FG-D-033, FG-D-035, and FG-D-036 after coil electrical
   interface ownership is clearer.
