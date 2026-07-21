# HV Gun-Side Insulation Decomposition Plan

Status: Level-3 planning file with targeted follow-up source review completed.

Parent items:

- `ebf3_gun_hv_input` (FG-12)
- `ebf3_gun_hv_insulator` (FG-13)
- `ebf3_gun_side_oil_tank` (FG-18)

Source registry:

- `research/ebf3_bom_sources/sources/level_2_parts/hv_gun_side_insulation/hv_gun_side_insulation_sources.md`

Target KB BOMs:

- None yet. This pass records boundary and decomposition decisions but does not
  create child BOMs because current evidence does not safely assign independent
  Level-3 children across the gun/HV-tank boundary.

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
| HV input central conductor | defer | FG-12 | None | Generic feedthrough sources support conductors, but EBF3 geometry/current path and boundary with HV cable termination are unresolved. |
| HV input ceramic feedthrough body | split_boundary / defer | FG-12/FG-13 | Existing `ebf3_gun_hv_insulator` remains separate | Generic sources support ceramic-to-metal feedthroughs, but adopting this under FG-12 would duplicate FG-13 unless the parent boundaries are redefined. |
| HV input metal flange/housing | defer | FG-12 | None | Plausible feedthrough feature; needs EBF3/source geometry to avoid duplicating gun column flange or chamber/gun interface. |
| HV cable-side termination | split_boundary | FG-12 / HV tank | None | The main HV cable is owned by `ebf3_high_voltage_tank`; gun-side receiving termination may belong to FG-12, but source detail is not enough to split. |
| Corona shield / field-grading shield | defer | FG-12/FG-13 | None | Generic HV design concern; no current EBF3/BINP child detail. |
| Standalone HV ceramic insulator body | defer | FG-13 | None | Source supports high-voltage insulator existence and generic alumina use, but not specific single-material geometry or metallization. |
| Metallized ends / collars | defer | FG-13 | None | Candidate-only plus generic ceramic-to-metal practice. Needs source confirmation before child BOM. |
| Gun-side oil volume | defer | FG-18 | None | BINP supports oil tank and silicone oil, but gun-side vs main tank ownership remains source-ambiguous. Keep FG-18 as a boundary marker, not a decomposed oil subsystem. |
| Oil tank shell/lid | defer | FG-18 | None | Candidate-only for gun-side package. Main HV tank shell belongs to high-voltage tank subsystem. |
| Silicone oil as child material | split_boundary / defer | FG-18 / HV tank | Existing HV tank insulating-fluid item owns main tank fluid | BINP supports silicone oil; do not add a second oil item under FG-18 unless source confirms a separate gun-side oil volume. |
| Oil-compatible seals/supports | defer | FG-18 | None | Plausible but not source-specific and boundary-sensitive. |
| Grounding interface | defer | FG-18 / gun column | None | Candidate-only; may belong to gun column or main HV tank grounding depending on physical package. |

## Current KB Action

- Do not create child BOMs for FG-12, FG-13, or FG-18 in this pass.
- Keep FG-12 as gun-side HV receiving/input assembly.
- Keep FG-13 as the separate high-voltage insulator marker until source evidence
  decides whether it is part of the feedthrough or a separate structural
  insulator.
- Keep FG-18 as a boundary marker for a possible local gun-side oil volume, not
  as a decomposed duplicate of the main high-voltage tank.
- Do not add a second silicone-oil child item under FG-18 without source
  confirmation of a separate oil volume.

## Manufacturing Readiness

No item in this cluster is local-ready. High-voltage ceramic-to-metal seals,
field grading, vacuum compatibility, oil compatibility, dielectric clearances,
and HV test requirements need separate material/process review.
