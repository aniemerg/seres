# Gun Column Decomposition Plan

Status: Level-3 planning file with boundary review completed.

Parent item:

- `ebf3_gun_column` (FG-17)

Closely related boundary items:

- `ebf3_cabin_gun_mounting_port` (MC-5)
- `ebf3_wire_feeder_mount_to_gun_bracket` (WF-26)
- `ebf3_gun_hv_input` (FG-12)
- `ebf3_gun_signal_wiring` (FG-19)

Source registry:

- `research/ebf3_bom_sources/sources/level_2_parts/gun_column/gun_column_sources.md`

Target KB BOMs:

- None yet. This pass records boundary decisions but does not create a child BOM
  because current evidence supports gun/chamber/feeder interfaces, not detailed
  gun-column internal geometry.

Workflow and decision-status definitions:

- `research/ebf3_bom_sources/README.md`
- `research/ebf3_bom_sources/derived/ebf3_subsystem_boundaries.md`

## Source Authority Assessment

1. `RAW-EBF-SPACE` is primary machine-level evidence that the electron beam gun
   is inserted through the chamber top and that the wire feeder is attached to
   the electron beam gun.
2. `RAW-EBF-US-PATENT` is primary machine-level evidence that a portion of the
   electron beam gun protrudes into the sealed container while another portion
   remains outside, and that flange-style container connections exist in the
   system.
3. USPAS/Pfeiffer/Cambridge Vacuum/Kimball sources support vacuum-compatible
   stainless-steel and vacuum-fitting considerations, but they do not define
   EBF3 gun-column geometry.
4. `LOCAL-EBF3-FG-TABLE`, `LOCAL-EBF3-MC-TABLE`, and `LOCAL-EBF3-WF-TABLE` are
   user-derived and candidate-only.

## Source Evidence And Use

### RAW-EBF-SPACE

Evidence:

- "inserted through the top"
- "air-cooled"
- "wire feeder is attached"
- "stationary electron beam gun and wire feeder"

Use:

- Supports the current gun/cabin boundary: the gun is a fixed package inserted
  through the chamber top, while the chamber owns the opening.
- Supports a wire-feeder-to-gun interface, but does not show whether the bracket
  is a removable feeder bracket or an integral gun-column datum.
- Air cooling is a system feature; it does not justify a gun-column cooling child
  without airflow/duct geometry.

### RAW-EBF-US-PATENT

Evidence:

- "portion of the electron beam gun"
- "inserted into the container"
- "protruding into the sealed container"
- "extending outside of the sealed container"
- "bolted flange"

Use:

- Supports treating the gun column as a cross-boundary physical package with
  internal and external portions.
- Supports a bolted/flanged interface concept, but not a specific child split
  between gun-side flange, chamber-side port, gasket, and fasteners.

### LOCAL-EBF3-FG-TABLE

Evidence:

- User-derived FG-17 candidates include gun body, column tube, flanges, mounting
  datum, internal brackets, and grounding structure.

Use:

- Introduces candidate Level-3 children only. It cannot justify `adopt` by
  itself.

### LOCAL-EBF3-MC-TABLE

Evidence:

- User-derived MC-5 candidates include top port flange, bolt pattern, locating
  datum, seal, and stiffening ring.

Use:

- Reinforces that chamber-side port/flange features must remain with the
  manufacture cabin unless a source identifies them as gun-owned.

### LOCAL-EBF3-WF-TABLE

Evidence:

- User-derived WF-26 candidates include bracket, dowel pins, screws, and slotted
  adjustment holes.

Use:

- Supports the need to keep wire-feeder alignment features visible, but the
  bracket remains a wire-feeder item unless source evidence shows it is integral
  to the gun column.

### WEB-USPAS-VACUUM-MATERIALS

Evidence:

- "Stainless steels"
- "vacuum construction materials"
- "excellent weldability"
- "excellent formability"

Use:

- Supports stainless steel as a plausible vacuum structural material family.
- Does not justify selecting a final gun-column alloy or manufacturing route.

### WEB-PFEIFFER-VACUUM-MATERIALS

Evidence:

- "Stainless steel"
- "construction of chambers or components"
- "flange connections"
- "vacuum-tight"

Use:

- Supports stainless steel and flange/weld considerations for vacuum hardware.
- Does not define EBF3 gun-column child parts.

### WEB-CAMVAC-EBW-INTRO

Evidence:

- "electron gun"
- "mounted on, or in"
- "high vacuum chamber"

Use:

- Supports electron gun to vacuum chamber mounting as a standard EB machine
  boundary.
- Does not resolve gun-side versus chamber-side ownership.

### WEB-KIMBALL-ELECTRON-GUN-BEAM-SYSTEMS

Evidence:

- "ultra-high-vacuum electron and ion optics"
- "vacuum chambers and fittings"
- "UHV-compatible"

Use:

- Supports vacuum-compatibility caution for gun-column fittings and internal
  supports.
- Does not provide EBF3 column geometry.

## Candidate Decision Matrix

| Candidate component/function | Status | Applies to | KB representation | Decision basis |
| --- | --- | --- | --- | --- |
| Gun column/body shell | reject as child for this pass | FG-17 | Existing `ebf3_gun_column` remains parent | Splitting a column body child under a gun-column parent duplicates the parent unless FG-17 is redefined as a larger mechanical assembly. |
| Gun-side mating flange or datum | split_boundary / defer | FG-17 / MC-5 | None | Primary sources support insertion/protrusion and flange-style mounting, but not enough to separate gun-side flange from cabin-side port/flange. |
| Chamber-side gun mounting port/flange | split_boundary | MC-5 | Existing `ebf3_cabin_gun_mounting_port` | Boundary policy assigns chamber opening and structural flange to cabin. Do not add this under gun column. |
| Vacuum gasket or seal at gun/chamber interface | split_boundary / defer | MC-5 / FG-17 | None | Seals are real, but source does not define whether the seal is part of chamber port hardware, gun service hardware, or a consumable interface kit. |
| Bolt pattern / interface fasteners | split_boundary / defer | MC-5 / FG-17 | None | Patent supports bolted flange concept; ownership and replaceability are unresolved. |
| Internal electrode/lens support brackets | defer | FG-17 / electrode/lens items | None | User-derived candidate only. Could duplicate electrode, lens, or coil mounting if created too early. |
| Optical-axis locating datum | defer | FG-17 | None | Plausible and important, but not source-defined enough for a child item. |
| Grounding structure or return path | split_boundary / defer | FG-17 / HV tank / power supplies / positioning | None | Candidate-only and electrically cross-subsystem. Do not hide return-path ownership inside the gun column. |
| Gun-side wire-feeder mounting datum | split_boundary / defer | FG-17 / WF-26 | None | EBF source supports feeder attached to gun. Current boundary keeps removable bracket with wire feeder and defers any integral gun-side datum. |
| Wire-feeder removable bracket | split_boundary | WF-26 | Existing `ebf3_wire_feeder_mount_to_gun_bracket` | Keep in wire feeder unless later source shows the bracket is integral to the gun column. |
| HV-input mounting boss/flange | defer | FG-17 / FG-12 | None | Boundary-sensitive with HV input feedthrough and gun-side insulation; no source geometry. |
| Signal/feedthrough mounting points | defer | FG-17 / FG-19 / cabin | None | Boundary-sensitive with diagnostic signal wiring and cabin feedthroughs. |
| Air-cooling jacket, fins, or duct | defer | FG-17 / cabin / controls | None | EBF-space supports air-cooled gun but not the cooling hardware geometry or ownership. |

## Current KB Action

- Do not create child BOMs for FG-17 in this pass.
- Keep `ebf3_gun_column` as a mechanical boundary assembly, not as a generic
  low-resolution substitute for internal electrodes, lenses, diagnostics, HV
  input, or wiring.
- Update notes so:
  - the gun owns the gun-side structural column/body and mating datum candidates;
  - the cabin owns the chamber-side port/opening/flange;
  - the wire feeder owns the removable feeder bracket unless source evidence
    shows it is integral to the gun column.
- Revisit FG-17 only after a source provides an actual gun-column section view,
  mounting drawing, or serviceable hardware breakdown.

## Manufacturing Readiness

`ebf3_gun_column` is not local-ready. Vacuum-compatible material selection,
precision alignment datums, weldments/flanges, sealing surfaces, grounding,
thermal management, and serviceability all need separate review before recipes
or local closure are added.
