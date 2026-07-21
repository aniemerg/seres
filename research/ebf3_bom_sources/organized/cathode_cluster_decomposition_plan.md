# Cathode Cluster Decomposition Plan

Status: Level-3 planning file with targeted follow-up source review completed.

Parent items:

- `ebf3_gun_cathode` (FG-1)
- `ebf3_gun_cathode_heater_leads` (FG-14)
- `ebf3_gun_cathode_cartridge` (FG-15)
- `ebf3_gun_cathode_radiation_shield` (FG-16)

Source registry:

- `research/ebf3_bom_sources/sources/level_2_parts/cathode_cluster/cathode_cluster_sources.md`

Target KB BOMs:

- None yet. This pass records decomposition decisions but does not create child
  BOMs because current evidence does not pass the adoption gate for independent
  Level-3 children.

Workflow and decision-status definitions:

- `research/ebf3_bom_sources/README.md`

## Source Authority Assessment

1. `RAW-BINP-60KEV-30KW` is an external source for EBF3, but directly describes
   a comparable direct-heated electron gun and cathode cartridge.
2. `RAW-EBF-SPACE` is primary machine-level EBF3 evidence for the LaB6 cathode
   variant.
3. `LOCAL-EBF3-FG-TABLE` is user-derived and candidate-only.
4. Kimball/Ted Pella cathode sources are external commercial cathode
   construction references. They support plausible emitter/heater/base
   structures but are not EBF3-specific.
5. `WEB-BARC-ELECTRON-GUNS-2012` is an external industrial electron-gun source
   that supports heat shields, ceramic sleeves, heater filament, and support
   rods for one LaB6 cathode assembly architecture.
6. `WEB-NASA-MODULAR-CATHODE-GUN` is generic modular cathode/electron-gun
   evidence. It supports modular subassembly patterns but not the EBF3 fixed-gun
   cathode details.

## Source Evidence And Use

### RAW-BINP-60KEV-30KW

Evidence:

- "direct heated cathode"
- "5-cathode"
- "tantalum foil 0.1÷0.2 mm"
- "preliminary adjusted cartridge"
- "Cathode heater with stabilized current"

Use:

- Supports the current FG-1 cathode, FG-14 heater path, and FG-15 cartridge
  boundaries.
- Supports tantalum foil as a cathode material variant for the comparable BINP
  gun.
- Does not expose enough cartridge, heater-lead, contact, clamp, or insulation
  geometry to create reliable Level-3 child items.

### RAW-EBF-SPACE

Evidence:

- "lanthanum hexaboride (LaB6 ) cathode"
- "longer operating life"

Use:

- Supports a LaB6 cathode variant for EBF3.
- Does not define the emitter holder, heater lead, cartridge, or shield
  structure.

### LOCAL-EBF3-FG-TABLE

Evidence:

- User-derived candidates include emitter foil/filament/crystal, clamp or holder
  interface, heater contact, heater leads, hot-side conductor, bus, ceramic
  insulation, emitter holder, clamp, locating seat, electrical contact, ceramic
  locator, and radiation shield sheets/spacers.

Use:

- Introduces candidate Level-3 children only. It cannot justify `adopt` by
  itself.

### WEB-KIMBALL-LAB6-CATHODES

Evidence:

- "single-piece, stress-free, carbon heater rod"
- "held in place by a carbon ferrule"
- "heating current goes up one side"

Use:

- Supports that LaB6 cathode implementations can combine emitter, heater path,
  ferrule/holder, and mounting geometry.
- Reinforces that FG-1 material variants should not be collapsed into one
  assumed structure.

### WEB-KIMBALL-TA-ES044

Evidence:

- "tungsten 3% rhenium heater wire"
- "heavy copper leads are recommended"
- "mounted on ... bases"

Use:

- Supports heater wire/leads/base as real cathode construction features in one
  tantalum cathode architecture.
- Does not justify adopting these as EBF3-specific child items because BINP's
  tantalum-foil cathode geometry is not the same as this commercial disc
  cathode.

### WEB-BARC-ELECTRON-GUNS-2012

Evidence:

- "cups and heat shields"
- "Tantalum and Rhenium sheets"
- "filament is spot welded"
- "ceramic sleeves"

Use:

- Supports that LaB6 electron-gun cathode assemblies can include cups, heat
  shields, heater filament, rods, and ceramic sleeves.
- Strengthens the need for a future cathode architecture decision before
  creating child BOMs.

### WEB-TEDPELLA-KIMBALL-LAB6

Evidence:

- "carbon heater rod"
- "mounting strips"
- "sub-base provides rigidity"

Use:

- Supports LaB6 mounting/base candidates.
- Does not define the EBF3 fixed-gun cartridge architecture.

### WEB-NASA-MODULAR-CATHODE-GUN

Evidence:

- "four subassemblies"
- "the cathode"
- "the header"
- "electrical feedthroughs"

Use:

- Supports modular cathode/electron-gun decomposition as a general pattern.
- Does not override the current EBF3/BINP FG boundaries.

## Candidate Decision Matrix

| Candidate component/function | Status | Applies to | KB representation | Decision basis |
| --- | --- | --- | --- | --- |
| Tantalum foil cathode variant | defer | FG-1 | None; material variant candidate | BINP supports tantalum foil for a comparable gun, and Kimball supports tantalum cathode heater/base features in a different architecture. EBF3 also has a LaB6 variant, so do not split FG-1 into one material path yet. |
| LaB6 cathode variant | defer | FG-1 | None; material variant candidate | EBF-space supports LaB6 for EBF3; Kimball/Ted Pella/BARC sources show LaB6 cathode mounting/heater architectures vary. Defer until variant policy is explicit. |
| Cathode emitter as standalone child | reject for this pass | FG-1/FG-15 | Existing `ebf3_gun_cathode` parent remains the emitter item | Splitting an emitter child below `ebf3_gun_cathode` would duplicate the parent unless FG-1 is redefined as a cathode assembly. |
| Heater contact / hot-side contact | defer | FG-1/FG-14/FG-15 | None | New sources support contacts/heater paths as real cathode features, but architecture differs between tantalum disc, LaB6 carbon-rod, and BARC coil-filament designs. Do not adopt a generic contact child yet. |
| Heater leads / hot-side conductor | defer | FG-14 | None | Kimball supports heater wire and heavy leads; BARC supports filament-to-rod construction. These sources justify FG-14 as a real assembly but not a specific EBF3 child structure. |
| Ceramic beads/sleeves for heater leads | defer | FG-14 | None | BARC supports ceramic sleeves in one LaB6 cathode assembly. Defer because EBF3 heater-lead insulation geometry is not confirmed. |
| Cartridge body / holder | defer | FG-15 | None | BINP supports a preliminary adjusted cartridge; Kimball/Ted Pella support base/ferrule/mounting structures. Evidence is enough to keep FG-15 as an assembly, not enough to split exact children. |
| Clamp or locating seat | defer | FG-15 | None | Candidate remains plausible, but sources do not converge on an EBF3-specific clamp/seat architecture. |
| Cartridge electrical contact | defer | FG-15 | None | Boundary-sensitive with FG-14 heater leads and FG-1 emitter. Defer until a cartridge architecture source is added. |
| Cathode radiation shield sheet set | defer | FG-16 | None | BARC supports tantalum/rhenium heat shields for one LaB6 electron-gun cathode assembly. Defer because EBF3/BINP FG-16 is still inference-heavy. |
| Radiation shield spacers/clips | defer | FG-16 | None | BARC supports heat-shield support strips in one architecture, but not enough to create EBF3 shield spacer/clip children. |

## Current KB Action

- Do not create child BOMs for FG-1, FG-14, FG-15, or FG-16 in this pass.
- Keep cathode material choices unresolved in KB rather than forcing either
  tantalum foil or LaB6 as the single local model.
- Tighten FG-16 wording so it is clearly an inferred shielding candidate, not a
  source-confirmed refractory-metal sheet set.
- Revisit this cluster only after adding cartridge/heater/cathode construction
  sources that match the selected EBF3 cathode architecture.

## Manufacturing Readiness

No item in this cluster is local-ready. Tantalum foil, LaB6 cathodes, hot-side
heater leads, ceramic insulation, precision cartridge alignment, and
high-temperature vacuum compatibility all need separate material/process review.
