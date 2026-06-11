# Mixer or Blender Machine Reality Research

## Machine identity

- KB machine id: `mixer_or_blender`
- KB name: Mixer or blender
- KB file: `kb/items/machines/mixer_or_blender.yaml`
- Current KB mass: 80 kg
- Current BOM: `bom_mixer_or_blender`
- Current recipe: `recipe_machine_mixer_or_blender_v0`

## KB usage and needed function

The item is used by `mixing_basic_v0`, `mixing_and_blending_v0`, `refractory_castable_mixing_v0`, and `lubricant_compounding_high_temp_v0`.

The needed function is general small-batch mixing/blending of powders, granules, pastes, castables, or compounded materials. The exact machine differs by material: dry powders may use ribbon/V/tumble blenders; pastes and high-viscosity materials may use sigma/kneader or planetary mixers; refractory castables may need mortar/concrete-style mixers.

## Reality classification

Real practical machine category, but broad.

Industrial mixers and blenders are real, and the KB's 80 kg mass is plausible for a lab/pilot mixer or small industrial batch blender. The "or" name is acceptable as a coarse abstraction, but process-specific mixing quality may require distinctions by material class, viscosity, dust containment, heat, vacuum, and shear.

## Evidence links

- ROSS describes ribbon blenders as batch machines for bulk solids processing across pharmaceutical, chemical, plastic, agricultural, and food powders; lab through large sizes are available: <https://www.mixers.com/products/ribbon-blenders/ribbon-blender/>
- J R Boone sells lab and pilot-scale universal mixers for powders, granules, pastes, slurries, and liquids: <https://www.jrboone.com/lab-mixers>
- Matcon describes pilot-scale industrial powder blenders from 50 L to 200 L for recipe development and low-volume batches: <https://www.matconibc.com/products/industrial-mixer>
- PerMix describes ribbon mixers from lab-scale to large industrial batches for food, chemical, pharmaceutical, and cosmetic uses: <https://www.permixmixers.com/ribbon-mixers/>

## Commercial alternatives

- Ribbon blender for powders, granules, and dry bulk solids.
- V-blender or tumble blender for gentle dry blending.
- Sigma/Z-blade mixer or kneader for high-viscosity pastes.
- Planetary mixer for pastes, adhesives, and filled polymers.
- Mortar/concrete/refractory mixer for castables and aggregate-containing mixes.
- Chemical mixing tank for liquids, slurries, and controlled reactions.

## Build or open-source references

A simple mixer can be built from a vessel/trough, shaft, bearings, motor, gearbox, blades/ribbons/paddles, seals, discharge, and controls. The design becomes process-specific when materials are abrasive, dusty, sticky, reactive, high-temperature, or require high shear.

The KB recipe is plausible for a generic small mixer, but not for every process. Refractory castables and high-temperature lubricants may need tougher or more specific mixer designs than ordinary powder blending.

## Related machine research

Related local reports:

- `research/machines/powder_mixer.md`
- `research/machines/epoxy_synthesis_unit.md`
- `research/machines/plastic_extruder.md`
- `research/machines/cement_mixer_small.md`

Related KB item:

- `mixing_station`

## Recommendation for KB realism

Keep `mixer_or_blender` as the generic lab/pilot default, but document scope.

Recommended options:

- Use this item for low-detail mixing/blending where material behavior is not central.
- Keep `powder_mixer` separate only if dry powder uniformity, dust containment, or powder metallurgy quality matters.
- Use `mixing_station` for formulation/potting workflows if it includes dispensing, containers, ventilation, and cleanup beyond the mixer itself.
- Use a refractory/cement mixer for abrasive castables if aggregate handling matters.
- Avoid assuming one generic blender handles liquids, slurries, powders, high-viscosity pastes, and hot/reactive materials equally well.

## Confidence and open questions

Confidence: high that the machine category is real; medium that a single 80 kg generic mixer covers all current uses.

Open questions:

- Which current processes need high-shear, low-shear, dry, wet, vacuum, heated, or abrasive mixing?
- Should `powder_mixer` and `mixer_or_blender` be consolidated or separated by dry-powder specificity?
- Should `refractory_castable_mixing_v0` use a cement/refractory mixer instead?
