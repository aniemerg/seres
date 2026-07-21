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

### WEB-HEATWAVE-ELECTRON-GUN-ASSEMBLIES

Evidence:

- "Cathode/Heater Assembly"
- "Includes heat shield around cathode"

Use:

- Supports treating cathode radiation shielding as a real cathode-package
  feature in electron-gun assemblies.
- Does not define EBF3 shield material, layer count, dimensions, or mounting
  details.

### WEB-IUAC-THERMIONIC-GUN-HEAT-SHIELD

Evidence:

- "outer cylindrical tantalum heat shield"
- "forms the cathode"

Use:

- Supports heat-shield hardware as part of a thermionic cathode package.
- This is a comparable thermionic gun, not the EBF3 gun; use only to support
  retaining a package marker, not final geometry or Ta material selection.

### WEB-CERN-TEVATRON-ELECTRON-LENS-MAGNETIC-SYSTEM

Evidence:

- "coils"
- "correcting the electron beam trajectory"

Use:

- Supports magnetic coils as a real trajectory-correction method for electron
  beams.
- This does not prove the EBF3 FG-11 corrector geometry or whether correction is
  integrated with other gun-column magnetic hardware.

### WEB-PTR-EBW-GLOSSARY

Evidence:

- "high-voltage tank"
- "usually filled with insulating oil"

Use:

- Supports insulating-oil-filled high-voltage tank practice in electron-beam
  systems.
- Supports the general oil/HV insulation class, but not a separate EBF3
  gun-side oil tank shell/lid.

### WEB-JEOL-HIGH-TENSION-TANK

Evidence:

- "houses a high-voltage generator"
- "accelerate electrons"

Use:

- Supports the high-voltage tank concept in electron-optical equipment.
- Does not resolve whether the EBF3 fixed-gun-side oil tank is a separate
  package or a figure-level representation of the HV generator tank.

### WEB-BNL-HV-ELECTRON-GUN-FLUID-CONNECTOR

Evidence:

- "ceramic cone inside the gun"
- "silicone grease"
- "high dielectric strength"

Use:

- Supports dielectric fluid/grease around a high-voltage electron-gun connector
  as a real gun-side insulation strategy.
- This supports keeping an oil/fluid package marker near FG-18, but it does not
  prove EBF3 shell/lid geometry or a separate bulk oil inventory.

### WEB-US3133227A-OIL-TANK-ELECTRON-GUN-ASSEMBLY

Evidence:

- "electron gun assembly"
- "submerged in an oil tank"
- "prevent arcing"

Use:

- Supports electron-gun high-voltage hardware in an oil-tank package as a real
  architecture class.
- This is not an EBF3 source, so it supports keeping the FG-18 package marker
  but not final shell/lid geometry, dimensions, or exact oil inventory.

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
| FG-8 | `ebf3_gun_two_axis_deflection_coils` | child BOM added / detail deferred | Later coil-level review | Source supports the item; X/Y coil pairs and yoke are modeled, while leads, insulation, former, and driver matching remain deferred. |
| FG-9 | `ebf3_gun_beam_boundary_pickup` | child BOM added / detail deferred | Later pickup/feedthrough review | Source supports pickup existence; collector/insulator are modeled, while heat load, feedthrough, and DAQ remain deferred. |
| FG-10 | `ebf3_gun_secondary_electron_pickup` | child BOM added / detail deferred | Later pickup/feedthrough review | Source supports secondary-electron pickup existence; ring collector/insulator are modeled, while exact geometry and signal path remain unresolved. |
| FG-11 | `ebf3_gun_trajectory_corrector` | package child BOM added / detail deferred | Revisit after steering architecture is selected | BINP supports corrector existence; external electron-lens source supports coils for electron-beam trajectory correction. Current split does not settle geometry or electrostatic variants. |
| FG-12 | `ebf3_gun_hv_input` | child BOM added / boundary deferred | Revisit with HV-8/FG-13 interface geometry | HV interface is high-risk and crosses tank/gun boundary; conductor/terminal/flange are modeled, while ceramic/body/field grading remain deferred. |
| FG-13 | `ebf3_gun_hv_insulator` | child BOM added / detail deferred | Later HV insulator material/process review | Source supports high-voltage insulator; ceramic body, metallized end-interface, mounting collar, and field-grading markers are modeled, while final geometry and HV rating remain unresolved. |
| FG-14 | `ebf3_gun_cathode_heater_leads` | child BOM added / detail deferred | Later cathode material/process review | Source supports cathode heater current; current leads and termination are modeled, while material/gauge/joints remain unresolved. |
| FG-15 | `ebf3_gun_cathode_cartridge` | child BOM added / detail deferred | Later cartridge geometry review | BINP supports a preliminary adjusted cartridge; base, contacts, standoffs, and clamp are modeled, while datum geometry remains unresolved. |
| FG-16 | `ebf3_gun_cathode_radiation_shield` | package child BOM added / detail deferred | Revisit when cathode thermal architecture is selected | HeatWave and IUAC sources support cathode heat-shield hardware in electron-gun/thermionic-gun assemblies. Shield geometry, layer count, material, and mounting remain unresolved. |
| FG-17 | `ebf3_gun_column` | child BOM added / detail deferred | Later structural/interface review | Body shell, internal support, datum set, and mating flange are modeled; cabin port/seal/fasteners remain outside or unresolved. |
| FG-18 | `ebf3_gun_side_oil_tank` | unresolved boundary marker | Revisit with HV tank/gun oil-volume evidence | BINP figure lists oil tank and silicon oil; PTR/JEOL support HV tanks and insulating oil/fluid practice; BNL supports high-dielectric fluid in a gun HV connector; US3133227A supports an electron-gun assembly submerged in an oil tank. These sources support the package class but do not justify separate EBF3 shell/lid/oil/seal children. |
| FG-19 | `ebf3_gun_signal_wiring` | child BOM added / boundary deferred | Later signal detail review | Local diagnostic lead set, gun-diagnostic feedthrough insert marker, and shield termination interface marker are modeled; controls owns DAQ/logic and cabin owns passive ports. |

## Recommended Level-3 Planning Order

1. Electrode and ceramic family: FG-2, FG-3, FG-4, FG-5, FG-13.
2. Cathode material/process details: FG-1 plus FG-14/FG-15/FG-16 children.
3. HV/gun-side insulation details: FG-12, FG-13, FG-18, and HV-8 boundary.
4. Beam diagnostics signal/feedthrough path: FG-9, FG-10, FG-19.
5. Magnetic steering coil-level details: FG-8 and FG-11.
6. Gun column mounting/cooling details: FG-17.
7. Lens coil assemblies from completed FG-6/FG-7 child BOMs.

This order prioritizes high-temperature emitter fidelity, high-voltage boundary
clarity, and diagnostics interfaces before lower-risk structural decomposition.

## KB Action From This Audit

- Keep FG-6/FG-7 child BOMs created by the convergence rerun.
- Keep later package-level child BOMs for FG-8 through FG-12 and FG-14 through
  FG-19 as provisional adopted/detail-deferred splits.
- Do not add recipes or local closure.
- Use this audit to choose the next focused deep review; do not treat current
  package children as final material/process BOM leaves.

## Batch Child Split Review

| Parent scope | Current status | Rationale |
| --- | --- | --- |
| Magnetic optics and steering | adopt / detail deferred | Lenses and deflection coils have source-supported package children. FG-11 trajectory corrector now has external support for magnetic trajectory-correction coils, but exact implementation remains architecture-deferred. |
| Cathode support and radiation shield | adopt / detail deferred | Cartridge and heater-lead children are source-supported by cartridge/heater evidence. Radiation shield children now have external cathode heat-shield support, but exact EBF3 shield geometry/material remains unresolved. |
| HV input and gun-side oil tank | FG-12 adopted; FG-18 deferred | FG-12 children clarify gun-side HV input. FG-18 has external source support for electron-gun/HV oil-tank package class, but the shell/lid/oil/seal child split was removed because EBF3-specific package geometry is not confirmed. |
| Diagnostics and signal wiring | adopt / detail deferred | Pickup collectors/insulators, local signal leads, gun-diagnostic feedthrough insert marker, and shield termination interface marker are modeled; bias, DAQ, final pinout, and shield policy remain deferred across cabin/controls/power boundaries. |
| Precision electrodes and ceramics | keep leaf | Cathode, anode, control electrode, control-electrode insulator, screen electrode, and HV insulator remain single-material or architecture-sensitive leaves until geometry/material source review. |
