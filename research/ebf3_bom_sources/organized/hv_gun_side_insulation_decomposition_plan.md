# HV Gun-Side Insulation Decomposition Plan

Status: Level-3 planning file with gun-side HV input and standalone HV
insulator package splits completed.

Parent items:

- `ebf3_gun_hv_input` (FG-12)
- `ebf3_gun_hv_insulator` (FG-13)
- `ebf3_gun_side_oil_tank` (FG-18)

Source registry:

- `research/ebf3_bom_sources/sources/level_2_parts/hv_gun_side_insulation/hv_gun_side_insulation_sources.md`

Target KB BOMs:

- `bom_ebf3_gun_hv_input`
- `bom_ebf3_gun_hv_insulator`

This pass creates the minimal FG-12 children that clearly remain on the gun side
of the HV interface and a standalone FG-13 package split. FG-18 stays as an
unresolved marker because splitting it now would risk duplicating the main
oil-filled HV tank.

Workflow and decision-status definitions:

- `research/ebf3_bom_sources/README.md`
- `research/ebf3_bom_sources/derived/ebf3_subsystem_boundaries.md`

## Source Authority Assessment

1. `RAW-BINP-60KEV-30KW` supports FG-12/FG-13/FG-18 existence in a comparable
   electron-optical system but does not expose their internal construction.
2. `RAW-BINP-60KV-15KW-HV-TANK` supports oil-filled high-voltage tank design and
   silicone oil use on the supply side, not gun-side ownership.
3. CeramTec/Nor-Cal/Kimball sources support generic ceramic-to-metal vacuum
   feedthrough and UHV material practices.
4. `WEB-GOOGLE-PATENT-US20130134324A1` supports alumina/high-voltage insulator
   considerations in electron guns, but the geometry is patent-specific.
5. `LOCAL-EBF3-FG-TABLE` is user-derived and candidate-only.

## Source Evidence And Use

### RAW-BINP-60KEV-30KW

Evidence:

- "1-oil tank"
- "2-high voltage insulator"
- "14-high voltage input"
- "The silicon oil [2] is used"

Use:

- Supports keeping FG-12, FG-13, and FG-18 as named gun-side high-voltage items
  in the current fixed-gun scaffold.
- Does not define whether the oil tank is local to the gun column or the main HV
  supply package, so boundary caution remains.

### RAW-BINP-60KV-15KW-HV-TANK

Evidence:

- "oil-filled tank"
- "The silicon oil [1] is used"

Use:

- Supports silicone oil and oil-filled high-voltage tank concepts.
- Reinforces the boundary risk: main HV tank internals belong to
  `ebf3_high_voltage_tank`, not FG-18.

### WEB-CERAMTEC-CERAMASEAL-FEEDTHROUGHS

Evidence:

- "alumina ceramics"
- "Kovar"
- "stainless steel"
- "flashover"
- "corona breakdown"

Use:

- Supports material/function candidates for ceramic-to-metal HV feedthroughs.
- Does not identify which elements belong specifically to EBF3 FG-12 versus
  FG-13.

### WEB-CERAMTEC-FEEDTHROUGH-PDF

Evidence:

- "transfer of electrical power"
- "hermetic seal"
- "electrical isolation"

Use:

- Supports treating FG-12 as a feedthrough/input assembly rather than a
  single-material part.

### WEB-NORCAL-HIGH-CURRENT-FEEDTHROUGHS

Evidence:

- "high alumina ceramic insulators"
- "OFHC copper"
- "304 stainless steel flanges"

Use:

- Supports generic feedthrough material candidates.
- Does not justify assigning these materials to EBF3 without voltage/current and
  geometry constraints.

### WEB-GOOGLE-PATENT-US20130134324A1

Evidence:

- "high-voltage insulators"
- "alumina ceramic"
- "maximum electric field"

Use:

- Supports high-voltage electron-gun insulator concerns.
- Does not justify adopting a specific compact-gun insulator geometry for EBF3.

### WEB-KIMBALL-ELECTRON-GUN-BEAM-SYSTEMS

Evidence:

- "Feedthrough insulators are made of ceramic"
- "not UHV vacuum compatible"

Use:

- Supports ceramic feedthrough insulator and vacuum-material caution.
- Reinforces that local wiring/seal materials should not be accepted without
  vacuum compatibility review.

### LOCAL-EBF3-FG-TABLE

Evidence:

- User-derived FG-12 candidates include central conductor, ceramic insulator,
  metal flange/housing, shield, and cable-side termination.
- User-derived FG-13 candidates include ceramic insulator body and optional
  metallized ends/collars.
- User-derived FG-18 candidates include oil tank shell, lid, oil volume, seals,
  internal support, and grounding interface.

Use:

- Introduces candidate children only. It cannot justify `adopt` by itself.

## Candidate Decision Matrix

| Candidate component/function | Status | Applies to | KB representation | Decision basis |
| --- | --- | --- | --- | --- |
| HV input central conductor | adopted / detail deferred | FG-12 | `ebf3_gun_hv_input_central_conductor` | Generic feedthrough/input sources require a conductor path. Keep it under FG-12 as gun-side conductor only; material, diameter, clearance, and joint details remain deferred. |
| HV input ceramic feedthrough body | modeled / detail deferred | FG-12/FG-13 | `bom_ebf3_gun_hv_insulator` owns the standalone insulator package | Generic sources support ceramic-to-metal feedthroughs, and the current interface architecture keeps the ceramic HV insulator under FG-13 rather than duplicating it inside FG-12. Final feedthrough integration remains unresolved. |
| HV input metal flange/housing | adopted / detail deferred | FG-12 | `ebf3_gun_hv_input_flange_housing` | Plausible local mounting envelope for the gun-side HV input. Keep separate from chamber-side gun port, tank-side bushing, and gun-column structural flange. |
| Gun-side receiving terminal | adopted / detail deferred | FG-12 / HV tank | `ebf3_gun_hv_input_receiving_terminal` | The main HV cable is owned by `ebf3_high_voltage_tank`; the receiving terminal belongs to the gun-side input. Connector and shield-termination geometry remain deferred. |
| Tank-side cable termination | split_boundary / defer | HV-8 / HV-9 | None | Owned by HV tank interface, not the fixed gun. Needs connector/socket geometry. |
| Corona shield / field-grading shield | modeled / detail deferred | FG-12/FG-13/HV-8 | `ebf3_gun_hv_insulator_field_grading_electrode_set`; tank-side marker in HV-8 | Generic HV design sources support flashover/corona/electric-field concerns. Current BOM uses interface-local markers only; final geometry and potential connection remain unresolved. |
| Standalone HV ceramic insulator body | adopted / detail deferred | FG-13 | `ebf3_gun_hv_insulator_ceramic_body` | Source supports high-voltage insulator existence and generic alumina use. Current modeling keeps it in FG-13; exact shape, grade, and dielectric rating remain unresolved. |
| Metallized ends / collars | adopted / detail deferred | FG-13 | `ebf3_gun_hv_insulator_metallized_end_interface_set`, `ebf3_gun_hv_insulator_mounting_collar_set` | Generic ceramic-to-metal practice supports the interface class. Metallization stack, collar geometry, and joining process remain unresolved. |
| Gun-side oil volume | defer | FG-18 | None | BINP supports oil tank and silicone oil; PTR/JEOL support HV tank/oil practice; BNL supports high-dielectric fluid in a gun HV connector; US3133227A supports an electron-gun assembly submerged in an oil tank. These support the package class, but gun-side vs main tank ownership remains source-ambiguous. |
| Oil tank shell/lid | defer | FG-18 | None | Oil-tank package class is supported, but not EBF3-specific separate gun-side shell/lid geometry. Main HV tank shell belongs to high-voltage tank subsystem. |
| Silicone oil as child material | split_boundary / defer | FG-18 / HV tank | Existing HV tank insulating-fluid item owns main tank fluid | BINP/PTR support insulating oil and BNL/US3133227A support gun-side high-dielectric fluid/oil-tank practice; do not create a gun-side oil child unless source confirms a separate gun-side oil volume. |
| Oil-compatible seals/supports | defer | FG-18 | None | Oil-tank package class is supported, but seal material and geometry remain unresolved. |
| Grounding interface | defer | FG-18 / gun column | None | Candidate-only; may belong to gun column or main HV tank grounding depending on physical package. |

## Current KB Action

- Create `bom_ebf3_gun_hv_input` with only gun-side receiving/input children:
  central conductor, receiving terminal, and local flange/housing.
- Create `bom_ebf3_gun_hv_insulator` as the current standalone insulator package
  with ceramic body, metallized end-interface, mounting collar, and local
  field-grading markers.
- Keep any final FG-12/FG-13 feedthrough integration deferred until source or
  design geometry is selected.
- Keep FG-18 as an unresolved boundary marker for a possible local gun-side oil
  package. Do not create shell/lid/oil/seal child items until EBF3-specific
  evidence confirms a separate gun-side oil package.
- Do not add local recipes for FG-12 children; creepage, dielectric clearance,
  vacuum/oil sealing, and HV test details are unresolved.

## Manufacturing Readiness

No item in this cluster is local-ready. High-voltage ceramic-to-metal seals,
field grading, vacuum compatibility, oil compatibility, dielectric clearances,
and HV test requirements need separate material/process review.
