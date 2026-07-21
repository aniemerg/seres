# Electromagnetic Lens Decomposition Plan

Status: convergence rerun complete.

Previous plan backup:

- `research/ebf3_bom_sources/organized/backups/electromagnetic_lens_decomposition_plan_2026-07-20_before_convergence_rerun.md`

Parent items:

- `ebf3_gun_main_magnetic_lens` (FG-7)
- `ebf3_gun_dynamic_magnetic_lens` (FG-6)

Source registry:

- `research/ebf3_bom_sources/sources/level_2_parts/electromagnetic_lens/electromagnetic_lens_sources.md`

Target KB BOMs:

- `kb/boms/bom_ebf3_gun_main_magnetic_lens.yaml`
- `kb/boms/bom_ebf3_gun_dynamic_magnetic_lens.yaml`

Rerun purpose:

- Verify whether the workflow converges from the same source registry and
  boundary rules after deleting the previously generated lens child items.
- Keep `LOCAL-EBF3-FG-TABLE` as user-derived candidate input only.
- Use short verbatim `Evidence:` entries and put interpretation only in `Use:`.
- Do not create KB child items until the decision matrix reaches `adopt`.
- Do not add recipes or local manufacturability closure in this pass.

Workflow and decision-status definitions:

- `research/ebf3_bom_sources/README.md`

## Source Authority Assessment

1. `LOCAL-EBF3-FG-TABLE` is user-derived and candidate-only.
2. `WEB-MYSCOPE-TEM-EM-LENSES` supports generic lens-level coil and pole-piece
   decomposition.
3. `WEB-JEOL-OBJECTIVE-LENS-GLOSSARY` and `WEB-GOOGLE-PATENT-US4419581A`
   support yoke as a real magnetic-lens component/function.
4. `WEB-GOOGLE-PATENT-US5008549A` supports keeping the coil as an internally
   complex assembly, not a single-material part.
5. `WEB-GOOGLE-PATENT-US6855938B2` supports that objective-lens packages can
   contain support/thermal details, but its geometry is patent-specific.
6. `WEB-EMLENS-MATINYAN-2025` is generic comparison evidence. It can introduce
   candidates, but it does not override EBF3 subsystem boundaries.

## Source Evidence And Use

### LOCAL-EBF3-FG-TABLE

Evidence:

- User-derived candidate entries list copper coil, pole pieces, magnetic yoke,
  bobbin, insulation, and mounting features for FG-6/FG-7.

Use:

- Introduces candidates only. It does not justify `adopt` by itself.

### WEB-MYSCOPE-TEM-EM-LENSES

Evidence:

- "a pole-piece"
- "a coil of copper wire"

Use:

- Supports adopting lens-level `coil assembly` and `pole pieces`.

### WEB-JEOL-OBJECTIVE-LENS-GLOSSARY

Evidence:

- "a polepiece"
- "a yoke to create a magnetic path"
- "a copper wire coil"
- "wound in the yoke"

Use:

- Supports yoke as a real magnetic-lens magnetic-return component.

### WEB-GOOGLE-PATENT-US4419581A

Evidence:

- "yokes 4 and 5 housing said excitation coil 2"
- "upper magnetic pole piece 6"
- "lower magnetic pole piece 7"

Use:

- Supports yoke and pole-piece terminology in a generic SEM objective-lens
  context.

### WEB-GOOGLE-PATENT-US5008549A

Evidence:

- "conductor 78 sheathed in an insulator 80"
- "embedded in a casting of potting material 82"
- "compatibility with a vacuum environment"

Use:

- Supports treating the coil as an assembly with unresolved internal conductor,
  insulation, sealing, potting, and thermal details.

### WEB-GOOGLE-PATENT-US6855938B2

Evidence:

- "coil body"
- "thermal insulation"
- "ring-shaped spacer"

Use:

- Supports deferring support/thermal details to later deeper decomposition.
  Does not justify separate lens-level mounting children for FG-6/FG-7.

### WEB-EMLENS-MATINYAN-2025

Evidence:

- "Primary solenoidal coil"
- "soft iron shroud and pole piece"
- "Beam deflection coils"
- "Stigmators"
- "Aperture"

Use:

- Supports candidate review. Deflection coils, stigmators, apertures, and
  current supplies remain outside these FG-6/FG-7 lens BOMs unless later
  EBF3-specific sources move them across the boundary.

## Candidate Decision Matrix

| Candidate component/function | Status | Applies to | KB representation | Decision basis |
| --- | --- | --- | --- | --- |
| Focusing coil assembly | adopt | FG-6, FG-7 | `ebf3_gun_dynamic_lens_coil_assembly`, `ebf3_gun_main_lens_coil_assembly` | Candidate introduced by LOCAL-EBF3-FG-TABLE; coil evidence from MyScope; assembly treatment supported by US5008549A. |
| Pole pieces | adopt | FG-6, FG-7 | `ebf3_gun_dynamic_lens_pole_pieces`, `ebf3_gun_main_lens_pole_pieces` | Candidate introduced by LOCAL-EBF3-FG-TABLE; supported by MyScope, JEOL, and US4419581A. |
| Magnetic yoke | adopt | FG-6, FG-7 | `ebf3_gun_dynamic_lens_yoke`, `ebf3_gun_main_lens_yoke` | Candidate introduced by LOCAL-EBF3-FG-TABLE; supported by JEOL and US4419581A. |
| Bobbin / coil former | defer | FG-6, FG-7 | None; future coil-assembly candidate | Candidate introduced by LOCAL-EBF3-FG-TABLE. Current evidence supports coil-body/support concepts but not a distinct lens-level child. |
| Electrical insulation / sealing / potting system | defer | FG-6, FG-7 | None; future coil-assembly candidate | US5008549A supports coil-internal construction details. Defer to coil-assembly decomposition. |
| Mounting structure/interface | defer | FG-6, FG-7 | None | Support hardware is plausible, but current evidence is patent-geometry-specific and does not define an EBF3 lens-level child. |
| Regulated current supply | split_boundary | FG-6, FG-7 | Power-supply scope | Lens BOM owns the load; power supplies own regulated current sources. |
| Deflection coils | split_boundary | FG-6, FG-7 | Existing `ebf3_gun_two_axis_deflection_coils` | EBF3 FG table already separates FG-8. |
| Trajectory correction coils/plates | split_boundary | FG-6, FG-7 | Existing `ebf3_gun_trajectory_corrector` | EBF3 FG table already separates FG-11. |
| Stigmator | defer | FG-6, FG-7 | None | Generic source candidate only; no current EBF3-specific support. |
| Aperture | defer / split_boundary | FG-6, FG-7 | Existing gun electrode/aperture functions | Generic lens-column candidate; current gun BOM already models aperture-like electrode functions elsewhere. |
| Cooling jacket, heat-transfer sheath, or heat sink | defer | FG-6, FG-7 | None; future coil/yoke-package candidate | Current evidence supports possible heat-transfer features but not an EBF3 FG-6/FG-7 lens-level child. |

## Adopted Child BOM Structure

### FG-7 Main Magnetic Lens

Adopted children:

- `ebf3_gun_main_lens_coil_assembly`
- `ebf3_gun_main_lens_pole_pieces`
- `ebf3_gun_main_lens_yoke`

Mass allocation is placeholder-only and sums to the current parent mass
(`2.2 kg`). It is not a source-supported mass model.

### FG-6 Dynamic Magnetic Lens

Adopted children:

- `ebf3_gun_dynamic_lens_coil_assembly`
- `ebf3_gun_dynamic_lens_pole_pieces`
- `ebf3_gun_dynamic_lens_yoke`

Mass allocation is placeholder-only and sums to the current parent mass
(`1.2 kg`). It is not a source-supported mass model.

## Convergence Check

This rerun converges with the backed-up plan: both independently produce the
same lens-level adopted children (`coil assembly`, `pole pieces`, `magnetic
yoke`) and the same main deferrals (`bobbin/former`, coil insulation/sealing,
mounting/support, stigmator, aperture, cooling/thermal features).

## Manufacturing Readiness

No adopted child is local-ready yet. Do not add recipes until a separate
material/process readiness review resolves conductor grade, insulation system,
magnetic alloy, vacuum compatibility, coil winding requirements, magnetic
material heat treatment, alignment tolerances, and inspection requirements.
