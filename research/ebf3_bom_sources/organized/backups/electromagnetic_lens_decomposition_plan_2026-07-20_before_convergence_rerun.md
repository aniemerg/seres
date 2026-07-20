# Electromagnetic Lens Decomposition Plan

Status: rerun planning file used to generate the EBF3 main and dynamic magnetic
lens child BOMs.

Rerun note:

- Rerun after review found that `engineering_inference` had been used too
  broadly for bobbin/former, insulation, and mounting children.
- Targeted follow-up source search was performed for coil internal structure,
  vacuum-compatible coil insulation, and objective-lens support hardware.
- Result: the added sources support keeping `coil assembly` as an assembly with
  unresolved internal structure. They do not justify separate lens-level child
  items for bobbin/former, insulation set, or mounting hardware.

Parent items:

- `ebf3_gun_main_magnetic_lens` (FG-7)
- `ebf3_gun_dynamic_magnetic_lens` (FG-6)

Source registry:

- `research/ebf3_bom_sources/sources/level_2_parts/electromagnetic_lens/electromagnetic_lens_sources.md`

Target KB BOMs:

- `kb/boms/bom_ebf3_gun_main_magnetic_lens.yaml`
- `kb/boms/bom_ebf3_gun_dynamic_magnetic_lens.yaml`

## Source Authority Assessment

1. `LOCAL-EBF3-FG-TABLE` is user-derived and unverified. It can introduce
   candidate components and boundary hypotheses, but it cannot by itself justify
   `adopt`.
2. `WEB-MYSCOPE-TEM-EM-LENSES` supports generic electromagnetic lens
   construction: magnetic pole pieces and copper coil. `WEB-ISU-ELECTRON-LENSES-PDF`
   is retained for later detailed review but is not used as an independent
   adoption basis in this plan.
3. `WEB-JEOL-OBJECTIVE-LENS-GLOSSARY` and `WEB-GOOGLE-PATENT-US4419581A`
   support yoke as a real magnetic-lens component/function.
4. `WEB-GOOGLE-PATENT-US5008549A` supports treating the lens coil as an
   internally complex, vacuum-compatible assembly with unresolved conductor,
   insulation, sealing, potting, and heat-transfer details.
5. `WEB-GOOGLE-PATENT-US6855938B2` supports that electron-microscopy objective
   lenses can have specific coil-body, sheath, spacer, screw, and thermal
   insulation details, but those details are patent-specific and do not by
   themselves define the EBF3 FG-6/FG-7 lens package.
6. `WEB-EMLENS-MATINYAN-2025` is generic comparison evidence. It can introduce
   candidate functions for review, but it does not override the EBF3 FG table.

Workflow and decision-status definitions:

- `research/ebf3_bom_sources/README.md`

## Source Evidence And Use

### LOCAL-EBF3-FG-TABLE

Source status: user-derived / unverified. The rows below only introduce
candidates. Each candidate still needs external or primary-source support before
it can become `adopt`.

Candidate entries reviewed:

- FG-6: copper coil, pole pieces, magnetic yoke, bobbin, insulation, mounting
  structure.
- FG-7: copper coil, pole pieces, magnetic yoke, bobbin, insulation, mounting
  interface.

Boundary implication:

- FG-8 separately owns two-coordinate deflection coils.
- FG-11 separately owns the trajectory corrector.
- Power-supply hardware is outside FG-6/FG-7.

### WEB-MYSCOPE-TEM-EM-LENSES

Evidence:

- "a pole-piece"
- "a coil of copper wire"

Use:

- Supports adopting pole-piece and coil children for FG-6/FG-7. The source is
  generic TEM training material, not EBF3-specific.

### WEB-ISU-ELECTRON-LENSES-PDF

Evidence:

- Not quoted in this plan; retained in the source registry for later detailed
  review.

Use:

- Not used as an independent adoption basis in this plan.

### WEB-EMLENS-MATINYAN-2025

Evidence:

- "Primary solenoidal coil"
- "soft iron shroud and pole piece"
- "Beam deflection coils"
- "Stigmators"
- "Aperture"

Use:

- Supports considering soft-iron shroud/shell language as a generic comparison
  candidate. It does not directly support the EBF3 `yoke` term.
- Introduces stigmator/aperture/current-supply candidates, which are not adopted
  into these BOMs without EBF3-specific support.

### WEB-JEOL-OBJECTIVE-LENS-GLOSSARY

Evidence:

- "a polepiece"
- "a yoke to create a magnetic path"
- "a copper wire coil"
- "wound in the yoke"

Use:

- Supports treating yoke as a real magnetic-lens component/function, not just a
  user-table term.

### WEB-GOOGLE-PATENT-US4419581A

Evidence:

- "yokes 4 and 5 housing said excitation coil 2"
- "upper magnetic pole piece 6"
- "lower magnetic pole piece 7"

Use:

- Supports yoke as a plausible magnetic-lens structural/magnetic-return
  component. This is generic SEM objective-lens evidence, not EBF3-specific
  evidence.

### WEB-GOOGLE-PATENT-US5008549A

Evidence:

- "conductor 78 sheathed in an insulator 80"
- "embedded in a casting of potting material 82"
- "compatibility with a vacuum environment"

Use:

- Supports modeling `Focusing coil assembly` as an assembly rather than a
  single-material part.
- Supports deferring coil insulation, sealing, potting, and heat-transfer
  materials to a later coil-assembly decomposition instead of adopting separate
  lens-level child items now.

### WEB-GOOGLE-PATENT-US6855938B2

Evidence:

- "coil body"
- "thermal insulation"
- "ring-shaped spacer"

Use:

- Supports that lens packages can contain mechanical and thermal support
  hardware.
- Does not support adopting a generic `mounting structure/interface` child for
  EBF3 FG-6/FG-7 because the details are tied to a specific objective-lens
  patent geometry.

## Candidate Decision Matrix

Adoption-gate note: each adopted row below records direct source support.
Engineering inference can preserve unresolved internal structure in this plan,
but it does not by itself justify a separate KB child item.

| Candidate component/function | Status | Applies to | KB representation | Decision basis |
| --- | --- | --- | --- | --- |
| Focusing coil assembly | adopt | FG-6, FG-7 | `ebf3_gun_dynamic_lens_coil_assembly`, `ebf3_gun_main_lens_coil_assembly` | Candidate introduced by LOCAL-EBF3-FG-TABLE and externally supported by MyScope. US5008549A adds support for treating the coil as an internally complex vacuum-compatible assembly. |
| Pole pieces | adopt | FG-6, FG-7 | `ebf3_gun_dynamic_lens_pole_pieces`, `ebf3_gun_main_lens_pole_pieces` | Candidate introduced by LOCAL-EBF3-FG-TABLE and externally supported by MyScope. |
| Magnetic yoke | adopt | FG-6, FG-7 | `ebf3_gun_dynamic_lens_yoke`, `ebf3_gun_main_lens_yoke` | Candidate introduced by LOCAL-EBF3-FG-TABLE and externally supported by JEOL and US4419581A as a real magnetic-lens yoke/magnetic-path component. MatinyanLab supports only the generic shroud/shell comparison, not the yoke term. |
| Bobbin / coil former | defer | FG-6, FG-7 | None; future coil-assembly decomposition candidate | Candidate introduced by LOCAL-EBF3-FG-TABLE. Follow-up search found coil-body and winding-support concepts, but not enough support for a distinct bobbin/former child at the lens BOM level. Keep inside unresolved coil assembly for now. |
| Electrical insulation / sealing / potting system | defer | FG-6, FG-7 | None; future coil-assembly decomposition candidate | Candidate introduced by LOCAL-EBF3-FG-TABLE and externally supported by US5008549A as coil-internal vacuum-compatible construction. Defer because it belongs in a later coil-assembly child BOM, not directly under the lens assembly. |
| Mounting structure/interface | defer | FG-6, FG-7 | None; unresolved lens-package interface | Candidate introduced by LOCAL-EBF3-FG-TABLE. US6855938B2 shows that objective lenses can include support hardware, but the details are geometry-specific and do not define an EBF3 FG-6/FG-7 child item. |
| Regulated current supply | split_boundary | FG-6, FG-7 | Existing power-supply scope, not lens BOM | Generic sources discuss lens current, but supply hardware belongs to power supplies; lens BOM owns the load. |
| Deflection coils | reject for this BOM / split_boundary | FG-6, FG-7 | Existing `ebf3_gun_two_axis_deflection_coils` | EBF3 FG table separates FG-8; adding deflection coils to lens BOM would duplicate ownership. |
| Trajectory correction coils/plates | reject for this BOM / split_boundary | FG-6, FG-7 | Existing `ebf3_gun_trajectory_corrector` | EBF3 FG table separates FG-11. |
| Stigmator | defer | FG-6, FG-7 | None | Generic source candidate only; no current EBF3-specific support. |
| Aperture | defer/reject for this BOM | FG-6, FG-7 | Existing gun electrode/aperture functions remain separate | Generic lens-column candidate, but EBF3 already models anode/control/screen electrode aperture functions. |
| Cooling jacket, heat-transfer sheath, or heat sink | defer | FG-6, FG-7 | None; future coil-assembly or yoke-package candidate | US5008549A and US4419581A show heat-transfer/cooling features can exist in magnetic lens packages, but current EBF3 FG-6/FG-7 sources do not define a separate child item. |

## Adopted Child BOM Structure

Naming note:

- Yoke item names are intentionally unified across FG-6 and FG-7:
  `ebf3_gun_dynamic_lens_yoke` and `ebf3_gun_main_lens_yoke`.
- The original user-derived table used "yoke" for FG-6 and "yoke/shell" for
  FG-7, but current KB naming avoids implying a source-supported difference
  between those magnetic return structures.

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

## Manufacturing Readiness

No adopted child is local-ready yet. Do not add recipes until a separate
material/process readiness review resolves conductor grade, insulation system,
magnetic alloy, vacuum compatibility, coil winding requirements, magnetic
material heat treatment, alignment tolerances, and inspection requirements.
