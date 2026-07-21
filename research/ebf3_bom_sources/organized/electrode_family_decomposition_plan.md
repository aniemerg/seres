# Electrode Family Decomposition Plan

Status: Level-3 planning file with targeted follow-up source review completed.

Parent items:

- `ebf3_gun_anode` (FG-2)
- `ebf3_gun_control_electrode` (FG-3)
- `ebf3_gun_control_electrode_insulator` (FG-4)
- `ebf3_gun_screen_electrode` (FG-5)

Source registry:

- `research/ebf3_bom_sources/sources/level_2_parts/electrode_family/electrode_family_sources.md`

Target KB BOMs:

- None. This pass keeps the electrode bodies and control-electrode insulator as
  unresolved leaf items rather than adding lower-confidence child BOMs.

Workflow and decision-status definitions:

- `research/ebf3_bom_sources/README.md`
- `research/ebf3_bom_sources/derived/ebf3_subsystem_boundaries.md`

## Source Authority Assessment

1. `RAW-BINP-60KEV-30KW` supports the existence of boundary/screen/control
   electrodes, the anode, and the control-electrode insulator in a comparable
   electron-optical system.
2. Kimball and BARC support triode electron-gun electrode roles but do not
   specify the exact EBF3 fixed-gun electrode geometry.
3. Daiwa sources support refractory/vacuum-compatible material candidates for
   electron-gun parts and precision apertures, but are not EBF3 BOM drawings.
4. CeramTec supports alumina ceramic as a high-voltage/vacuum-compatible
   insulation material family, but does not define the FG-4 shape.
5. `LOCAL-EBF3-FG-TABLE` is user-derived and candidate-only.

## Source Evidence And Use

### RAW-BINP-60KEV-30KW

Evidence:

- "boundary electrode, control electrode"
- "screen electrode and the anode"
- "3-insulator control electrode"
- "4-control electrode"
- "6-screen electrode"
- "7-anode"

Use:

- Supports FG-2, FG-3, FG-4, and FG-5 as distinct fixed-gun items.
- Does not expose aperture insert, cooling, replaceable tip, metallized
  ceramic, or mounting-hardware details.

### LOCAL-EBF3-FG-TABLE

Evidence:

- User-derived FG-2 candidates include anode body, aperture, mounting face, and
  optional replaceable aperture insert.
- User-derived FG-3 candidates include shaped electrode body, aperture, mounting
  interface, and bias connection.
- User-derived FG-4 candidates include ceramic standoff, insulating sleeve,
  mounting washer, and optional metallized end.
- User-derived FG-5 candidates include shaped electrode, aperture edge, mounting
  interface, and electrical connection.

Use:

- Introduces candidate Level-3 children only. It cannot justify `adopt` by
  itself.

### WEB-KIMBALL-ELECTRON-GUN-BEAM-SYSTEMS

Evidence:

- "three electrodes"
- "cathode"
- "anode"
- "Wehnelt grid"
- "control of the electron emission"

Use:

- Supports anode and control-grid/Wehnelt roles.
- Does not justify splitting FG-3 into separate grid body, aperture insert, or
  bias connector children.

### WEB-DAIWA-ELECTRON-GUNS

Evidence:

- "Material: Kovar, Mo, Ta"
- "vacuum parts"
- "electron optics"

Use:

- Supports Kovar, molybdenum, and tantalum as candidate materials for precision
  electron-gun components.
- Material support does not create child geometry.

### WEB-DAIWA-APERTURES

Evidence:

- "Molybdenum, tantalum, tungsten"
- "stainless steel"
- "Hole diameter"
- "Straight holes, counterbored holes"

Use:

- Supports refractory and stainless material candidates for precision electron
  apertures.
- Does not prove that FG-2/FG-3/FG-5 have separately replaceable aperture
  inserts.

### WEB-BARC-ELECTRON-GUNS

Evidence:

- "three electrodes"
- "cathode (emitter), anode and a control electrode"
- "Grid or Wehnelt electrode"

Use:

- Supports keeping the anode and control electrode distinct in the KB.
- Does not define EBF3-specific subcomponents.

### WEB-CERAMTEC-CERAMASEAL-FEEDTHROUGHS

Evidence:

- "alumina ceramics"
- "electrically insulating"
- "high-vacuum"

Use:

- Supports ceramic material candidates and vacuum/HV caution for FG-4.
- Does not justify splitting metallized ends, washers, or collars under FG-4.

## Candidate Decision Matrix

| Candidate component/function | Status | Applies to | KB representation | Decision basis |
| --- | --- | --- | --- | --- |
| Anode body with beam aperture | reject as child | FG-2 | Existing `ebf3_gun_anode` remains the leaf | Splitting an anode-body child below an anode parent would duplicate the parent unless source shows FG-2 is an assembly. |
| Replaceable anode aperture insert | defer | FG-2 | None | Daiwa supports precision aperture inserts generally, but no source confirms a replaceable anode insert in this gun. |
| Anode cooling insert or heat spreader | defer | FG-2 | None | Candidate-only; no source-specific thermal design. |
| Control/Wehnelt electrode body | reject as child | FG-3 | Existing `ebf3_gun_control_electrode` remains the leaf | Current evidence supports the whole control electrode, not a separable lower body. |
| Control-electrode aperture edge or insert | defer | FG-3 | None | Aperture geometry is plausible, but no independent replaceable insert is confirmed. |
| Control-electrode bias contact | split_boundary / defer | FG-3 / power supplies / FG-19 | None | Electrode load is in the gun, bias supply is in power supplies, and wiring may belong to FG-19. Do not create a contact child until the electrical interface is modeled. |
| Control-electrode ceramic standoff/sleeve | reject as child | FG-4 | Existing `ebf3_gun_control_electrode_insulator` remains the leaf | FG-4 already represents the insulator. Child split would duplicate the parent without confirmed multi-piece construction. |
| Metallized ceramic ends/collars | defer | FG-4 | None | CeramTec supports ceramic-to-metal practice generally, but no source confirms metallized ends for FG-4. |
| Mounting washer or clamp for insulator | defer | FG-4 / gun column | None | Boundary-sensitive with gun column hardware; no source geometry. |
| Screen/boundary electrode body | reject as child | FG-5 | Existing `ebf3_gun_screen_electrode` remains the leaf | Current source names a screen/boundary electrode but does not expose subcomponents. |
| Screen-electrode aperture edge or insert | defer | FG-5 | None | Candidate-only; precision-aperture sources are generic. |
| Screen-electrode electrical connection | split_boundary / defer | FG-5 / FG-19 | None | Wiring ownership and contact geometry are not resolved. |

## Current KB Action

- Do not create child BOMs for FG-2, FG-3, FG-4, or FG-5 in this pass.
- Keep the current items as high-fidelity leaf candidates:
  refractory-metal precision electrodes for FG-2/FG-3/FG-5 and a ceramic
  insulator candidate for FG-4.
- Tighten item notes so material choices remain candidates rather than confirmed
  final manufacturing selections.
- Revisit only if a source shows replaceable aperture inserts, cooling inserts,
  metallized ceramic ends, or separable electrode mounting hardware.

## Manufacturing Readiness

No item in this family is local-ready. Final material selection, precision hole
machining, surface finish, high-voltage spacing, vacuum compatibility, thermal
loading, brazing/metallization, and beam-optics tolerances all need separate
review before recipes or local closure are added.
