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

- `bom_ebf3_gun_cathode_cartridge`
- `bom_ebf3_gun_cathode_heater_leads`

This pass creates only the minimal Level-3 children supported by the selected
direct-heated tungsten hairpin/filament package. It does not create a local
recipe, dimensions, or detailed fabrication process.

Related selected-material review:

- `research/ebf3_bom_sources/organized/cathode_variant_review.md`

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
7. `cathode_variant_review.md` selects a direct-heated tungsten
   hairpin/filament package as the active cathode package direction. LaB6
   remains the original EBF3 source reference, and BINP tantalum remains
   comparable-gun evidence only.

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
| Tungsten hairpin/filament cathode package | selected package direction / defer detailed geometry | FG-1 / FG-14 / FG-15 | Existing Level-2 leaves stay in place | Lunar ISRU review selects W as the material direction, and JEOL/Kimball support directly heated tungsten filament electron-gun sources. Exact base, contacts, cartridge, and insulation geometry still need source/design selection. |
| Tantalum foil cathode variant | not active / defer | FG-1 | None; preserve as reference variant | BINP supports tantalum foil for a comparable gun, and Kimball supports tantalum cathode heater/base features in a different architecture. Lunar material review de-prioritizes Ta for early local closure. |
| LaB6 cathode variant | source reference / defer | FG-1 | None; preserve as original EBF3 reference | EBF-space supports LaB6 for EBF3, but no lunar LaB6 route is modeled. Use only if the modeling goal returns to exact source-machine reconstruction or explicit alternative variants. |
| Cathode emitter as standalone child | reject for this pass | FG-1/FG-15 | Existing `ebf3_gun_cathode` parent remains the filament emitter item | Under the selected direct-heated package, emitter and heater filament are the same hot tungsten conductor. A child emitter would duplicate FG-1. |
| Heater contact / hot-side contact | adopted / detail deferred | FG-1/FG-14/FG-15 | `ebf3_gun_cathode_hot_contact_pair` | Contacts are required by the selected direct-heated package. Exact material, weld/clamp method, and service geometry remain deferred. |
| Heater leads / hot-side conductor | adopted / detail deferred | FG-14 | `ebf3_gun_cathode_current_lead_pair`, `ebf3_gun_cathode_lead_termination_set` | FG-14 remains the lead/contact assembly feeding current into the directly heated filament. Conductor alloy, gauge, thermal transition, and termination details remain deferred. |
| Ceramic beads/sleeves or standoffs | adopted / detail deferred | FG-14 / FG-15 | `ebf3_gun_cathode_ceramic_standoff_set` | 3M/Kimball support ceramic standoffs and vacuum-compatible support constraints. Exact insulation geometry remains deferred. |
| Cartridge body / holder | adopted / detail deferred | FG-15 | `ebf3_gun_cathode_cartridge_base` | BINP supports a preliminary adjusted cartridge; electron-gun package sources support mounted cathode assemblies. Datum and base geometry remain deferred. |
| Clamp or locating seat | adopted / detail deferred | FG-15 | `ebf3_gun_cathode_locating_clamp` | Cartridge replacement and mounted cathode assemblies need retention. Exact locating seat and fastener geometry remain deferred. |
| Cartridge electrical contact | adopted / detail deferred | FG-15 | `ebf3_gun_cathode_hot_contact_pair` | Contact ownership is assigned to the cartridge so heater leads can terminate into it without duplicating the filament emitter. |
| Cathode radiation shield sheet set | defer | FG-16 | None | BARC supports heat shields for one LaB6 assembly, but current tungsten hairpin sources do not justify an EBF3 shield child. |
| Radiation shield spacers/clips | defer | FG-16 | None | No selected tungsten package source confirms separate shield support hardware. |

## Current KB Action

- Keep FG-1 as the tungsten hairpin/filament emitter leaf; do not create an
  emitter child below it.
- Create child BOMs for FG-14 and FG-15 only:
  `bom_ebf3_gun_cathode_heater_leads` and
  `bom_ebf3_gun_cathode_cartridge`.
- Keep FG-16 as a deferred shield candidate because current tungsten hairpin
  sources do not justify independent shield children.
- Tighten FG-16 wording so it is clearly an inferred shielding candidate, not a
  source-confirmed refractory-metal sheet set.
- Revisit this cluster after selecting dimensions, contact/joint method,
  ceramic geometry, and whether a shield is present.

## Manufacturing Readiness

No item in this cluster is local-ready. Tungsten filament stock, hot-side current
leads, ceramic insulation, precision cartridge alignment, high-temperature
contacts, and high-vacuum compatibility all need separate material/process
review.
