# Fixed Electron Beam Gun Level-2 Decomposition Audit

Status: Level-2 audit for the current EBF3 fixed electron beam gun scaffold.

Purpose:

- Review all current FG-1 through FG-19 Level-2 items before deeper Level-3
  decomposition.
- Decide which items already have a completed Level-2 child BOM, which need a
  new Level-3 planning file, and which should remain unresolved single-part or
  variant items for now.
- Preserve fidelity by keeping closure gaps open until a later material/process
  readiness review.

Level policy:

- Level labels are research workflow labels only. Do not add `level_2` or
  `level_3` to KB item IDs.
- Current scope: `ebf3_fixed_electron_beam_gun` Level-1 subsystem children.
- Next scope after this audit: Level-3 decomposition plans for selected
  high-risk assemblies.

Source registry:

- `research/ebf3_bom_sources/sources/level_1_subsystems/fixed_electron_beam_gun/fixed_electron_beam_gun_sources.md`
- `research/ebf3_bom_sources/sources/level_2_parts/electromagnetic_lens/electromagnetic_lens_sources.md`

Related completed Level-2 plan:

- `research/ebf3_bom_sources/organized/electromagnetic_lens_decomposition_plan.md`

## Source Evidence And Use

### RAW-BINP-60KEV-30KW

Evidence:

- "direct heated cathode"
- "boundary electrode, control electrode"
- "screen electrode and the anode"
- "9-dynamic magnetic lens"
- "10-main magnetic lens"
- "11-two coordinates deflected coils"
- "12-pick-up of beam boundary"
- "13-pick-up of secondary electrons"
- "14-high voltage input"
- "15-trajectory corrector"
- "tantalum foil 0.1÷0.2 mm"
- "preliminary adjusted cartridge"
- "silicon oil"
- "Cathode heater with stabilized current"
- "beam current, cathode heat current"

Use:

- Supports the existence and boundary of the current FG-level electron-optical
  items.
- Supports treating cathode cartridge, heater leads, magnetic lenses, coils,
  pickups, HV input, and gun-side oil volume as unresolved assemblies.

### RAW-EBF-SPACE

Evidence:

- "lanthanum hexaboride (LaB6 ) cathode"
- "wire feeder is attached to the electron beam gun"
- "inserted through the top"

Use:

- Supports cathode material variant review and gun/cabin/wire-feeder boundary
  checks. It does not by itself define detailed Level-3 children.

### LOCAL-EBF3-FG-TABLE

Evidence:

- User-derived FG-1 through FG-19 candidate table.

Use:

- Introduces candidate child structures only. It cannot justify `adopt` by
  itself.

## Level-2 Item Audit

| FG | KB item | Current Level-2 decision | Next action | Reasoning |
| --- | --- | --- | --- | --- |
| FG-1 | `ebf3_gun_cathode` | keep as unresolved variant/single-part candidate | Create cathode material-variant plan before recipe | BINP supports tantalum foil; EBF-space supports LaB6 option. Do not split emitter/holder here because holder is represented by FG-15 cartridge and heater path by FG-14. |
| FG-2 | `ebf3_gun_anode` | keep as unresolved precision electrode | Create electrode-family plan after cathode cluster | Source supports anode existence; insert/cooling/aperture details are not confirmed enough for child BOM. |
| FG-3 | `ebf3_gun_control_electrode` | keep as unresolved precision electrode | Include in electrode-family plan | Source supports control electrode existence and function; separate bias supply belongs to power supplies. |
| FG-4 | `ebf3_gun_control_electrode_insulator` | keep as unresolved ceramic part/possible small assembly | Include in insulator/feedthrough plan if interfaces are decomposed | Source supports control-electrode insulator; metallized ends or collars need source confirmation. |
| FG-5 | `ebf3_gun_screen_electrode` | keep as unresolved precision electrode | Include in electrode-family plan | Source supports screen electrode; do not merge with anode/control electrode because functions differ. |
| FG-6 | `ebf3_gun_dynamic_magnetic_lens` | Level-2 decomposition completed | Keep current child BOM; later create coil-assembly Level-3 plan | Convergence rerun adopted coil assembly, pole pieces, and yoke only. |
| FG-7 | `ebf3_gun_main_magnetic_lens` | Level-2 decomposition completed | Keep current child BOM; later create coil-assembly Level-3 plan | Convergence rerun adopted coil assembly, pole pieces, and yoke only. |
| FG-8 | `ebf3_gun_two_axis_deflection_coils` | needs Level-3 planning | Create deflection-coil decomposition plan | Source supports the item; likely coil pairs/leads/supports are internal but need evidence before child BOM. |
| FG-9 | `ebf3_gun_beam_boundary_pickup` | needs Level-3 planning | Create beam-diagnostic pickup plan with FG-10 | Source supports pickup existence; collector/insulator/signal/feedthrough details need diagnostics-specific evidence. |
| FG-10 | `ebf3_gun_secondary_electron_pickup` | needs Level-3 planning | Create beam-diagnostic pickup plan with FG-9 | Source supports secondary-electron pickup existence; collector geometry and signal path unresolved. |
| FG-11 | `ebf3_gun_trajectory_corrector` | needs Level-3 planning | Create trajectory-corrector plan after FG-8 | Source supports corrector existence; magnetic vs electrostatic implementation must stay unresolved until sourced. |
| FG-12 | `ebf3_gun_hv_input` | needs Level-3 planning | Create HV input/feedthrough plan with FG-13/FG-18 boundary review | HV interface is high-risk and crosses tank/gun boundary; split conductor/ceramic/flange/termination only after source evidence. |
| FG-13 | `ebf3_gun_hv_insulator` | keep as unresolved ceramic part/possible assembly | Include in HV input/feedthrough plan | Source supports high-voltage insulator; metallized ends and mounting collars are deferred. |
| FG-14 | `ebf3_gun_cathode_heater_leads` | needs Level-3 planning | Create cathode cluster plan with FG-1/FG-15/FG-16 | Source supports cathode heater current; hot leads, insulation, and terminals need material/source review. |
| FG-15 | `ebf3_gun_cathode_cartridge` | needs Level-3 planning | Create cathode cartridge plan with FG-1/FG-14/FG-16 | BINP supports a preliminary adjusted cartridge; holder, clamp, contact, and locator candidates need evidence. |
| FG-16 | `ebf3_gun_cathode_radiation_shield` | defer as inferred feature | Keep out of child BOM until high-temperature cathode plan | Radiation shield is plausible but still inference-heavy; do not deepen until source confirms independent shield structure. |
| FG-17 | `ebf3_gun_column` | needs Level-3 planning, lower priority | Create gun-column structural plan after HV/cathode/diagnostics | Structural body likely contains flanges, datum surfaces, brackets, and mounting interfaces; boundary with cabin port must remain explicit. |
| FG-18 | `ebf3_gun_side_oil_tank` | needs Level-3 planning with boundary risk | Create gun-side oil/HV boundary plan | BINP figure lists oil tank and silicon oil, but this must not duplicate the main HV tank subsystem. |
| FG-19 | `ebf3_gun_signal_wiring` | needs Level-3 planning, lower priority | Create gun-side instrumentation wiring plan after diagnostics | Source supports monitored currents; controls owns DAQ/logic while gun owns local pickups/internal wiring. |

## Recommended Level-3 Planning Order

1. Cathode cluster: FG-1, FG-14, FG-15, FG-16.
2. HV/gun-side insulation cluster: FG-12, FG-13, FG-18.
3. Beam diagnostics cluster: FG-9, FG-10, FG-19.
4. Magnetic steering cluster: FG-8, FG-11.
5. Electrode family: FG-2, FG-3, FG-4, FG-5.
6. Gun column: FG-17.
7. Lens coil assemblies from completed FG-6/FG-7 child BOMs.

This order prioritizes high-temperature emitter fidelity, high-voltage boundary
clarity, and diagnostics interfaces before lower-risk structural decomposition.

## KB Action From This Audit

- Keep FG-6/FG-7 child BOMs created by the convergence rerun.
- Do not create additional Level-3 child items from this audit alone.
- Do not add recipes or local closure.
- Use this audit to choose the next focused organized planning file.
