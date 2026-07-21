# Magnetic Steering Decomposition Plan

Status: Level-3 planning file with targeted follow-up source review completed.

Parent items:

- `ebf3_gun_two_axis_deflection_coils` (FG-8)
- `ebf3_gun_trajectory_corrector` (FG-11)

Source registry:

- `research/ebf3_bom_sources/sources/level_2_parts/magnetic_steering/magnetic_steering_sources.md`

Target KB BOMs:

- `kb/boms/bom_ebf3_gun_two_axis_deflection_coils.yaml`

Workflow and decision-status definitions:

- `research/ebf3_bom_sources/README.md`
- `research/ebf3_bom_sources/derived/ebf3_subsystem_boundaries.md`

## Source Authority Assessment

1. `RAW-BINP-60KEV-30KW` supports FG-8 and FG-11 existence in a comparable
   electron-optical system. It uses "coils" for FG-8 and separately references
   corrector currents, but it does not expose internal geometry.
2. `WEB-RIBTON-HIGH-ANGLE-BEAM-DEFLECTION` is strong external evidence for
   electron-beam 3D printing/surface-treatment deflection systems. It supports
   X/Y coil set and magnetic yoke children for FG-8.
3. Kimball, PTR, Cambridge Vacuum Engineering, and MyScope support magnetic
   deflector/alignment coil functions, but are not EBF3-specific geometry
   sources.
4. `LOCAL-EBF3-FG-TABLE` is user-derived and candidate-only.

## Source Evidence And Use

### RAW-BINP-60KEV-30KW

Evidence:

- "11-two coordinates deflected coils"
- "15-trajectory corrector"
- "magnetic lens and correctors currents"
- "deflect a beam on a work piece"

Use:

- Supports FG-8 as a fixed-gun two-coordinate deflection-coil assembly.
- Supports FG-11 as a current-driven correction function, but does not define
  whether the corrector is a distinct coil set, a trim coil integrated in
  another magnetic element, or an electrostatic alternative.

### LOCAL-EBF3-FG-TABLE

Evidence:

- User-derived FG-8 candidates include X/Y coil pairs, coil former,
  insulation, leads, mount, and optional magnetic yoke.
- User-derived FG-11 candidates include magnetic corrector coils or
  electrostatic correction plates, insulation, mount, and signal/power leads.

Use:

- Introduces candidate Level-3 children only. It cannot justify `adopt` by
  itself.

### WEB-RIBTON-HIGH-ANGLE-BEAM-DEFLECTION

Evidence:

- "3D printing impose stringent beam deflection requirements"
- "Deflection systems comprise a coil set"
- "X and Y pair of coils"
- "magnetic yoke"
- "driven with a current"
- "prototype assembly is made by winding a coil"

Use:

- Supports adopting X deflection coil pair, Y deflection coil pair, and
  magnetic yoke as FG-8 children.
- Supports deferring coil turns, winding pattern, amplifier matching, yoke
  material choice, and field optimization until coil-level design.

### WEB-KIMBALL-ELECTRON-GUN-BEAM-SYSTEMS

Evidence:

- "magnetic deflectors"
- "center and align the incoming electron beam"
- "Additional magnetic coils"
- "UHV-compatible"

Use:

- Supports magnetic deflectors/correctors as real electron-gun alignment
  hardware.
- Does not justify splitting FG-11 into specific children.

### WEB-MYSCOPE-DEFLECTOR-COILS

Evidence:

- "Rolls of wire"
- "make a magnetic field"
- "pushes the beam from side to side"

Use:

- Supports the basic magnetic-coil function of deflection coils.
- Generic SEM teaching source only; not enough for material or geometry
  adoption.

### WEB-PTR-EBW-GLOSSARY

Evidence:

- "alignment coil"
- "coincides with the column's centerline"
- "beam deflection"
- "electromagnetic deflection coil"
- "deflection coil"

Use:

- Supports trajectory/alignment correction and deflection coils as standard EBW
  gun-column functions.
- Places DAQ and current supplies outside the gun hardware BOM.

### WEB-CAMVAC-EBW-INTRO

Evidence:

- "deflection coil (electromagnetic)"
- "bottom of the column"
- "manipulate the beam"

Use:

- Supports FG-8 as an electromagnetic deflection-coil assembly in the electron
  gun column.
- Does not define child geometry beyond function.

## Candidate Decision Matrix

| Candidate component/function | Status | Applies to | KB representation | Decision basis |
| --- | --- | --- | --- | --- |
| X-axis deflection coil pair | adopt | FG-8 | `ebf3_gun_deflection_x_coil_pair` | BINP names two-coordinate deflected coils; Ribton supports X/Y coil pairs for electron-beam 3D printing/surface-treatment deflection systems. |
| Y-axis deflection coil pair | adopt | FG-8 | `ebf3_gun_deflection_y_coil_pair` | Same basis as X-axis coil pair. Keeping X and Y separate preserves two-coordinate fidelity without assuming a single monolithic coil pack. |
| Magnetic yoke | adopt | FG-8 | `ebf3_gun_deflection_magnetic_yoke` | Ribton directly supports magnetic yoke as part of a deflection system and explains its field-containment function. |
| Coil former / bobbin | defer | FG-8 | None | Plausible for winding support, but current sources do not require a separately replaceable former; yoke and winding geometry may combine this function. |
| Coil insulation | defer | FG-8 | None | Required at coil-design level, but not enough source detail to split into a separate child item now. |
| Coil leads / terminations | defer | FG-8 | None | Real electrical interface, but boundary with power-supply current driver and gun-side harness is unresolved. |
| Current amplifier / driver | split_boundary | Power supplies / controls | None under gun | Ribton emphasizes amplifier matching; drivers belong outside the gun hardware BOM. |
| Deflection mount or bracket | defer | FG-8 / gun column | None | Could belong to FG-8 or FG-17 depending on physical integration. |
| Cooling or thermal features | defer | FG-8 | None | Not adopted without source-specific heat-load evidence. |
| Trajectory-corrector magnetic coil set | defer | FG-11 | None | BINP supports corrector currents and Kimball/PTR support alignment coils, but no source defines the FG-11 coil geometry or whether it is separate from FG-8/lens hardware. |
| Trajectory-corrector electrostatic plates | reject for this pass | FG-11 | None | Current targeted sources support magnetic deflection/correction more strongly; electrostatic plates remain a possible future variant only if direct source evidence appears. |
| Corrector yoke / pole structure | defer | FG-11 | None | Do not duplicate FG-8 yoke or lens yoke without source geometry. |
| Corrector power/signal leads | split_boundary / defer | FG-11 / power supplies / controls | None | Loads may be in the gun, but regulated supplies and commands belong outside the fixed-gun BOM. |

## Current KB Action

- Create a conservative child BOM for FG-8 containing only:
  `ebf3_gun_deflection_x_coil_pair`,
  `ebf3_gun_deflection_y_coil_pair`, and
  `ebf3_gun_deflection_magnetic_yoke`.
- Do not split FG-8 coil pairs into conductor, insulation, former, leads, or
  cooling until a later coil-level plan.
- Do not create a child BOM for FG-11 in this pass.
- Tighten FG-11 wording so the current KB does not overclaim a specific magnetic
  corrector construction.

## Manufacturing Readiness

None of the adopted FG-8 child items is local-ready. Coil winding pattern,
ampere-turns, inductance, current driver matching, magnetic material choice,
vacuum compatibility, insulation, thermal loading, and field verification all
need separate review before manufacturing recipes or local closure are added.
