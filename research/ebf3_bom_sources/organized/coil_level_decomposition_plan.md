# Coil-Level Decomposition Plan

Status: Level-3 planning file with targeted source review completed.

Parent items:

- `ebf3_gun_main_lens_coil_assembly`
- `ebf3_gun_dynamic_lens_coil_assembly`
- `ebf3_gun_deflection_x_coil_pair`
- `ebf3_gun_deflection_y_coil_pair`

Related parent assemblies:

- `ebf3_gun_main_magnetic_lens` (FG-7)
- `ebf3_gun_dynamic_magnetic_lens` (FG-6)
- `ebf3_gun_two_axis_deflection_coils` (FG-8)
- `ebf3_gun_signal_wiring` (FG-19)
- `ebf3_multi_channel_driver_module`

Source registry:

- `research/ebf3_bom_sources/sources/level_3_parts/coil_assemblies/coil_assembly_sources.md`

Target KB BOMs:

- None yet. This pass resolves the first coil-level review by keeping adopted
  lens/deflection coil assemblies intact until source geometry and electrical
  interface ownership are stronger.

Workflow and decision-status definitions:

- `research/ebf3_bom_sources/README.md`
- `research/ebf3_bom_sources/derived/ebf3_subsystem_boundaries.md`
- `research/ebf3_bom_sources/organized/fixed_electron_beam_gun_unresolved_items.md`

## Source Authority Assessment

1. `RAW-BINP-60KEV-30KW` supports the existence of dynamic/main magnetic lenses,
   two-coordinate deflection coils, and magnetic/corrector currents in a
   comparable electron-beam gun, but it does not expose coil construction.
2. Diamond Light Source supports the generic electromagnetic-lens split between
   coil and magnetic circuit. This reinforces existing Level-2 lens BOMs but
   does not expose coil-internal child parts.
3. Ribton supports X/Y deflection coil sets, magnetic yoke, and current-driven
   deflection for electron-beam 3D printing/surface-treatment systems. This
   reinforces the existing FG-8 child BOM but does not expose wire insulation,
   terminals, or mounting details.
4. CN103406657A supports an electron-beam deflection scanning coil architecture
   with magnetic core/bobbin and coil winding. It is patent-specific and its
   core/bobbin may overlap the already-modeled `ebf3_gun_deflection_magnetic_yoke`.
5. JEOL/Kimball sources support deflection electromagnets/coils and clarify that
   power supplies or controllers are outside the coil hardware.
6. Local lens and magnetic-steering plans are the current adopted BOM basis for
   the parent items. The unresolved-items register is tracking-only.

## Source Evidence And Use

### RAW-BINP-60KEV-30KW

Evidence:

- "dynamic electromagnetic lens"
- "10-main magnetic lens"
- "11-two coordinates deflected coils"
- "magnetic lens and correctors currents"

Use:

- Supports coil-bearing FG-6, FG-7, and FG-8 parent functions.
- Does not define coil windings, bobbins, insulation, potting, leads, cooling, or
  mounting geometry.

### WEB-DIAMOND-TEM-LENS-LECTURE

Evidence:

- "consist of a coil"
- "electrical current flows"
- "magnetic circuit"
- "specific shape"

Use:

- Supports the existing lens split into coil assembly plus magnetic circuit
  children.
- Does not justify splitting the lens coil assembly below the coil level.

### WEB-RIBTON-HIGH-ANGLE-BEAM-DEFLECTION

Evidence:

- "X and Y pair of coils"
- "magnetic yoke"
- "driven with a current"
- "frequency response"

Use:

- Supports the current FG-8 child BOM: X coil pair, Y coil pair, and magnetic
  yoke.
- Reinforces that current driver/amplifier matching is important, but outside
  the coil child BOM.

### WEB-CN103406657A-DEFLECTION-SCANNING-COIL

Evidence:

- "magnetic core bobbin"
- "coil winding"
- "magnetic ring"
- "magnetic pole"
- "soft magnetic materials"
- "number of turns"

Use:

- Supports coil winding and magnetic core/bobbin as real electron-beam
  deflection-coil construction concepts.
- Does not directly map onto the current EBF3 FG-8 model because the patent's
  magnetic core/bobbin may combine functions already represented by
  `ebf3_gun_deflection_magnetic_yoke`.

### WEB-JEOL-BS60-ELECTRON-BEAM-SOURCE

Evidence:

- "built-in deflection electromagnet"
- "EB source power supply"
- "without venting the vacuum chamber"

Use:

- Supports deflection electromagnet as gun/source-side hardware.
- Reinforces that field control/power-supply functions are outside the coil
  child BOM.

### WEB-KIMBALL-ELECTRON-GUN-BEAM-SYSTEMS

Evidence:

- "magnetic coils"
- "deflect the beam"
- "electromagnetic coils around the gun"
- "X and Y power supplies"

Use:

- Supports magnetic deflection coils as a real option in electron guns.
- Also shows electrostatic alternatives, so it should not be used alone to
  over-specify FG-8 or FG-11 coil internals.

### LOCAL-ELECTROMAGNETIC-LENS-PLAN

Evidence:

- Adopted lens child BOMs contain coil assembly, pole pieces, and yoke.
- Lens bobbin/former, insulation/sealing/potting, mounting, and cooling were
  deferred.

Use:

- Defines the starting point for this coil-level review.

### LOCAL-MAGNETIC-STEERING-PLAN

Evidence:

- Adopted FG-8 child BOM contains X-axis coil pair, Y-axis coil pair, and
  magnetic yoke.
- Deflection coil former, insulation, leads, mount, and cooling were deferred.

Use:

- Defines the starting point for this coil-level review.

## Candidate Decision Matrix

| Candidate component/function | Status | Applies to | KB representation | Decision basis |
| --- | --- | --- | --- | --- |
| Lens coil winding pack | defer | main/dynamic lens coil assemblies | None | Diamond supports a coil at the lens level, but the current parent item already is the coil assembly. No source confirms a separately serviceable winding pack. |
| Lens bobbin / former | defer | main/dynamic lens coil assemblies | None | Candidate remains plausible, but current sources do not show a distinct EBF3 lens bobbin/former. |
| Lens coil insulation / sealing / potting | defer | main/dynamic lens coil assemblies | None | Required in practice, but no EBF3 geometry, material, or vacuum compatibility basis yet. |
| Lens lead terminations | split_boundary / defer | lens coil assemblies / FG-19 / power supplies | None | Real electrical interface, but ownership between coil pigtail, gun wiring, and regulated current supply is unresolved. |
| Lens cooling feature | defer | lens coil assemblies / gun column | None | Thermal feature is plausible but source-specific heat load and cooling method are missing. |
| Deflection coil winding below X/Y pair | defer | X/Y deflection coil pairs | None | CN103406657A supports coil winding generally, but adopting a winding child below a coil-pair parent would duplicate the parent unless the winding layout is source-defined. |
| Deflection magnetic core/bobbin | split_boundary / defer | X/Y deflection coil pairs / deflection yoke | Existing `ebf3_gun_deflection_magnetic_yoke` owns yoke-level magnetic circuit | Patent supports magnetic core/bobbin, but this may be the same physical magnetic circuit currently represented by the yoke. Do not create a second overlapping child. |
| Deflection coil insulation | defer | X/Y deflection coil pairs | None | Coil-level material/process detail; no EBF3 vacuum-compatible insulation source yet. |
| Deflection coil leads / terminations | split_boundary / defer | X/Y deflection coil pairs / FG-19 / power supplies | None | Electrical interface to current driver is unresolved. |
| Deflection mount or bracket | split_boundary / defer | FG-8 / FG-17 | None | Could belong to the coil pair, deflection yoke, or gun column. Needs physical mounting source. |
| Deflection cooling or thermal feature | defer | FG-8 | None | No source-specific heat-load evidence. |
| Current driver / amplifier | split_boundary | power supplies / controls | None under gun coil items | Ribton, JEOL, and Kimball reinforce driver importance, but source/supply/control ownership is outside coil BOM. |
| Coil conductor material | defer | all coil parent items | None | Copper is likely for coils, but this review is not a material/process readiness review and no EBF3 coil material is specified. |
| Coil manufacturing recipe | reject for this pass | all coil parent items | None | Local closure would be premature without winding pattern, conductor specification, insulation, vacuum compatibility, and test requirements. |

## Current KB Action

- Do not create child BOMs for the four coil parent items in this pass.
- Keep `ebf3_gun_main_lens_coil_assembly`,
  `ebf3_gun_dynamic_lens_coil_assembly`,
  `ebf3_gun_deflection_x_coil_pair`, and
  `ebf3_gun_deflection_y_coil_pair` as unresolved coil assemblies.
- Update notes to point to this plan and state that lower coil details remain
  deferred after review, not forgotten.
- Do not model current drivers, power supplies, or control electronics under the
  coil assemblies.

## Register Updates

Rows addressed by this plan remain unresolved:

- FG-D-022 and FG-D-031: bobbin/former remains deferred until a source shows a
  distinct physical former at the relevant parent level.
- FG-D-023 and FG-D-032: insulation/sealing/potting remains deferred to
  material/process readiness.
- FG-D-033: coil leads/terminations remain split-boundary/defer pending an
  electrical interface plan.
- FG-D-035: deflection mount/bracket remains boundary-sensitive with gun column.
- FG-D-036: deflection cooling remains deferred pending thermal design evidence.

## Manufacturing Readiness

No coil item reviewed here is local-ready. Winding geometry, conductor cross
section, insulation system, vacuum compatibility, impregnation or potting,
thermal path, lead termination, electrical test, magnetic field verification,
and current-driver matching all need separate material/process and interface
review before recipes or local closure are added.
