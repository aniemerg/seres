# Cathode Variant Review

Status: active cathode package direction selected.

Purpose:

- Select the active cathode material and package direction before deeper
  cathode child BOMs are created.
- Preserve the conflict between the comparable BINP tantalum-foil cathode and
  the EBF3 LaB6 cathode without forcing either path into the current model.
- Add lunar-closure material constraints so future local manufacturing work does
  not accidentally choose a hard-to-source cathode material.
- Define what still needs source support before cathode, heater, cartridge, or
  shield children are created.

Source registry:

- `research/ebf3_bom_sources/sources/level_2_parts/cathode_cluster/cathode_cluster_sources.md`

Related plan:

- `research/ebf3_bom_sources/organized/cathode_cluster_decomposition_plan.md`

## Evidence Summary

| Source | What it supports | Limit |
| --- | --- | --- |
| `RAW-EBF-SPACE` | EBF3 used a LaB6 cathode for longer operating life. | Does not define heater, cartridge, holder, or shield geometry. |
| `RAW-BINP-60KEV-30KW` | Comparable gun used a direct-heated tantalum-foil cathode in a preliminary adjusted cartridge with stabilized heater current. | Comparable gun evidence, not the EBF3 flight-weight gun architecture. |
| Kimball/Ted Pella/BARC sources | LaB6 and tantalum cathodes can include heater rods, heater wires, bases, ferrules, cups, shields, support strips, and ceramic sleeves. | Architectures differ; they do not converge on one EBF3-specific child BOM. |
| JEOL/Kimball/3M tungsten package sources | Tungsten thermionic electron-gun sources commonly use directly heated hairpin/filament emitters, mounted bases, precision assemblies, ceramic standoffs, and support structures. | Supports package direction, not EBF3-specific dimensions or a manufacturing recipe. |
| `LOCAL-EBF3-FG-TABLE` | Introduces emitter, heater contact, holder, clamp, ceramic locator, and shield candidates. | Candidate-only; not enough to adopt child items. |
| Lunar ISRU sources and material guide | W, Ta, Nb are trace/localized; W has clearer lunar source and cathode/filament use evidence; boron is weak/localized. | Material availability does not define EBF3 gun geometry or create a local recipe. |

## Lunar Material Availability

Availability labels follow `docs/lunar_material_availability_guide.md`.

| Material path | Availability | Use in this review |
| --- | --- | --- |
| LaB6 | `import_or_recycle` / `unknown_in_kb` | Best EBF3-specific cathode material evidence, but boron is weak/localized and no lunar LaB6 route is modeled. Preserve as original EBF3 reference, not the local-closure baseline. |
| Tantalum foil | `scarce_trace` / `site_sensitive` | BINP-comparable gun detail, but Ta is trace and high-concentration sources are localized; not the active local-closure path. |
| Tungsten cathode/filament | `scarce_trace` | Selected active material direction because W has the strongest lunar-closure argument among refractory cathode candidates when limited to low-mass critical emitter use. |

Key source interpretation:

- `DOC-LUNAR-MATERIAL-AVAILABILITY` puts W/Ta/Nb in scarce trace materials and
  says refractory metals should stay limited to low-mass critical functions.
- `RAW-ELLERY-SELF-REPLICATING-2015` says W, Ta, and Nb are trace elements, but
  gives concrete W mineral routes and notes W enrichment in NiFe asteroid
  microparticle inclusions.
- `RAW-ELLERY-LUNAR-DEMANDITE-2023` lists W, Ta, Nb, and Mo as candidate cathode
  materials, then argues W should be restricted to essential uses such as
  electrodes and filaments.
- `RAW-ELLERY-NEURAL-ELECTRONICS-2022` directly uses tungsten cathodes in a
  lunar-sourced thermionic vacuum-tube material chain.
- `RAW-ELLERY-SUSTAINABLE-ISRU-2020` and
  `RAW-ELLERY-VERTICAL-CLOSURE-2025` support NiFe impact material as a localized
  source for W micro-inclusions.
- `RAW-ELLERY-PRINTED-MOTORS` shows Ta being omitted from a lunar version of a
  specialty alloy, which supports not treating Ta as an early lunar baseline.

## Selected Direction

Use a **tungsten lunar-closure cathode path** as the active material direction
for future EBF3 cathode decomposition.

Implications:

- LaB6 remains the original EBF3 source-reference cathode, but it is not the
  active local-closure baseline because the lunar La/B supply route is weak.
- BINP tantalum foil remains useful comparable-gun evidence for direct-heated
  cathode/cartridge concepts, but it is not the active local-closure baseline.
- Tungsten is selected only as a low-mass critical emitter/filament material
  direction. This does not create a manufacturing recipe or prove EBF3 geometry.
- FG-14 heater leads, FG-15 cartridge, and FG-16 radiation shield remain
  unresolved Level-2 leaves until detailed base/contact/insulation/cartridge
  geometry is selected.

## Selected Package Shape

Use a **direct-heated tungsten hairpin/filament electron-gun package** as the
active cathode package direction.

Reason:

- JEOL and Kimball sources support tungsten wire or hairpin filament as a common
  directly heated thermionic electron-gun cathode.
- BINP supports a direct-heated cathode and cartridge pattern in a comparable
  electron-beam gun. Use this as architecture analogy only; do not adopt its
  tantalum material.
- 3M and Kimball support treating high-vacuum electron guns as precision
  cathode/electron-gun packages with mounting structures, ceramic standoffs,
  support structures, and vacuum-compatible assembly constraints.

Modeling effect:

- `ebf3_gun_cathode` is the active tungsten hairpin/filament emitter. The
  emitter and heater are the same hot tungsten conductor in this direction.
- `ebf3_gun_cathode_heater_leads` owns the current path from supply-side wiring
  to the hot filament contacts; it should not introduce a separate heater
  filament child unless a later source selects an indirectly heated package.
- `ebf3_gun_cathode_cartridge` remains the replaceable base/holder/alignment
  package for the filament and contacts.
- `ebf3_gun_cathode_radiation_shield` now has a package-marker child BOM for
  foil stack, spacers, and clips. Current tungsten hairpin sources still do not
  justify specific EBF3 shield geometry, material thickness, or mounting detail.

## Adopted Level-3 Shape

The first geometry split is intentionally narrow:

| Parent | Child item | Why adopted now |
| --- | --- | --- |
| `ebf3_gun_cathode_cartridge` | `ebf3_gun_cathode_cartridge_base` | Cartridge/package support is source-backed, but dimensions remain unknown. |
| `ebf3_gun_cathode_cartridge` | `ebf3_gun_cathode_hot_contact_pair` | A directly heated filament requires two hot contacts. |
| `ebf3_gun_cathode_cartridge` | `ebf3_gun_cathode_ceramic_standoff_set` | Electron-gun packages need ceramic isolation/support around high-voltage hot contacts. |
| `ebf3_gun_cathode_cartridge` | `ebf3_gun_cathode_locating_clamp` | Replaceable mounted cathode packages require retention/alignment hardware. |
| `ebf3_gun_cathode_heater_leads` | `ebf3_gun_cathode_current_lead_pair` | Makes the stabilized heater-current path explicit without duplicating the filament. |
| `ebf3_gun_cathode_heater_leads` | `ebf3_gun_cathode_lead_termination_set` | Keeps lead-to-contact boundaries visible for later weld/clamp/feedthrough decisions. |

Not adopted:

- No child under `ebf3_gun_cathode`; FG-1 is already the filament emitter.
- No shield children under `ebf3_gun_cathode_radiation_shield`; current
  tungsten hairpin sources do not support them.

## Modeling Decision

| Candidate | Decision | Reason |
| --- | --- | --- |
| Tungsten direct-heated hairpin/filament package | Selected active package direction | W is scarce trace, but lunar ISRU sources support low-mass critical tungsten cathode/filament uses more strongly than Ta; electron-gun sources support directly heated tungsten filaments. |
| LaB6 cathode variant | Preserve as source-reference / not active | Best EBF3-specific material evidence, but no lunar LaB6 route is modeled. |
| Tantalum-foil cathode variant | De-prioritize / not active | Strong comparable-gun evidence, but Ta is not a good early lunar baseline. |
| Heater contact, hot leads, ceramic sleeves | Defer | Real features in external sources, but their form depends on cathode architecture. |
| Cartridge holder, clamp, electrical contact | Defer | Cartridge existence is supported; internal construction is not. |
| Radiation shield sheets, spacers, clips | Defer | Plausible high-temperature cathode detail, but still not EBF3-specific. |

## Current Action

- Keep the fixed-gun top-level BOM structure unchanged.
- Update item notes so the cathode is visibly selected as a direct-heated
  tungsten hairpin/filament package while detailed geometry and process remain
  unresolved.
- Add only the minimal child BOMs for FG-14 and FG-15; do not add local recipes
  for cathode-related items.
- Do not reuse existing `tungsten_cathode_*` items for EBF3 yet. They are
  lower-resolution vacuum-tube/thermionic-converter cathode items, not
  source-backed EBF3 gun cathode geometry.
- Next unblocker: source or select the package geometry: filament/base form,
  hot contacts, ceramic insulation/standoffs, cartridge locating features, and
  whether any shield is actually present.
