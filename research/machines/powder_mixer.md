# Powder mixer

## Machine identity

- Queue item: `machine_reality_powder_mixer`
- KB ID: `powder_mixer`
- KB file: `kb/items/machines/powder_mixer.yaml`
- KB name: Powder mixer
- KB kind: `machine`
- KB modeled mass: 80 kg

The KB defines this as a steel powder mixing machine for blending metal or ceramic powders with binders. The BOM points to a small mixer frame, drum, motor, agitator shaft and paddles, basic controls, and fasteners.

## KB usage and needed function

`powder_mixer` is used by:

- `batching_and_mixing_basic_v0`
- `powder_processing_v0`

The needed function is batch blending of dry powders, granular materials, and powder-plus-binder mixtures for downstream powder metallurgy, ceramic forming, pressing, or sintering operations. The KB notes specifically mention homogeneous tungsten powder preparation for thermionic system manufacturing.

## Reality classification

Classification: real practical machine, but generic category rather than one exact design.

Powder mixers are standard industrial and lab equipment. The KB item is practical and its 80 kg mass is plausible for a small shop/pilot mixer, although real machines range from benchtop laboratory mixers to large industrial ribbon blenders and IBC tumble blenders. The KB's "tumbler or ribbon mixer" note is reasonable but ambiguous; those are different mechanisms with different cleanout, shear, segregation, and batch-size behavior.

## Evidence links

- ROSS Ribbon Blenders and Mixers: https://www.mixers.com/products/ribbon-blenders/ribbon-blender/
  - Commercial ribbon blenders are used for bulk solids processing across powders and granules, including chemical and plastic materials.
  - The described machine architecture includes a U-shaped trough, agitator shaft, inner and outer helical ribbons, and a gearmotor drive.

- Powder & Bulk Solids, "Selecting the Appropriate Powder Blender": https://www.powderbulksolids.com/mixers-blenders/selecting-the-appropriate-powder-blender
  - Identifies ribbon blenders, vertical blenders, and tumble blenders as common powder blender types.
  - Explains how ribbon, vertical, and tumble designs differ in mixing action, discharge, cleaning, material damage, and cost.

- Matcon industrial powder mixers: https://www.matconibc.com/products/industrial-mixer
  - Commercial IBC tumble blending equipment exists for contained powder mixing, with pilot-scale and production-scale options.
  - The source distinguishes gentle tumble blending from higher-shear mixing and liquid-addition options.

- Hosokawa Micron Labomixer: https://www.hmicronpowder.com/brochures-and-videos/video/laboratory-mixer-for-dry-powders-hosokawa-micron-labomixer/
  - Commercial lab-scale conical screw mixer for dry powders and liquid additives in 2.5 L batches.
  - Supports the reality of small laboratory/pilot powder mixers.

- Powder metallurgy blending overview: https://powdermetallurgy.com/blending-in-powder-metallurgy/
  - Describes powder metallurgy blending as combining metal powders, alloying elements, lubricants, and binders before compaction and sintering.
  - Mentions V mixers and controlled time/speed to avoid demixing, and notes dust/ventilation concerns.

## Commercial alternatives

- Ribbon blender: good general-purpose choice for many dry powders and some powders with small liquid additions; higher shear than tumble blending.
- V blender or double-cone/tumble blender: gentler and often better for fragile powders or minor additions, but usually needs more space and careful fill fraction.
- Conical screw/Nauta-style mixer: gentle mixing for powders and liquid additives, available from lab to industrial scale.
- IBC/tote blender: useful when containment, dust control, and fast cleanout/changeover matter.
- High-shear mixer/granulator: separate category for binder addition, granulation, or deliberate agglomerate breakdown.

## Build or open-source references

No robust open-source powder-mixer build package was found during this task. A small tumbler mixer is mechanically simple enough to fabricate from a rotating sealed drum, motor, speed reduction, frame, guards, and controls. A ribbon blender is more fabrication-intensive because it needs a trough, close-clearance ribbon agitator, shaft seals/bearings, discharge gate, and dust containment.

For KB realism, local construction should be represented as normal mechanical fabrication plus motor/control integration, with dust sealing and cleaning/contamination control as important requirements for metal and ceramic powders.

## Related machine research

Existing related research found:

- `research/machines/cement_mixer_small.md`

Related KB items to compare in future realism cleanup:

- `mixer_or_blender`
- `cement_mixer_small`
- `pellet_press`
- `molding_press`

The most important consolidation question is whether `powder_mixer` should remain separate from `mixer_or_blender`. It can remain separate if dry powder uniformity, dust containment, binder/lubricant addition, or powder metallurgy feedstock quality matters.

## Recommendation for KB realism

Keep `powder_mixer` as a real machine, but clarify the subtype if future KB edits are allowed.

Recommended interpretation:

- Keep as a small powder blender for metal/ceramic powders.
- Do not collapse into `cement_mixer_small`; concrete/cement mixing and powder metallurgy blending have different contamination, dust, uniformity, and cleaning requirements.
- Consider consolidation with `mixer_or_blender` only if the KB wants a single generic mixer category. If retained separately, rename/notes could specify "small powder blender, ribbon/tumble type".
- Preserve motor, drum/vessel, agitator, frame, and controls in the BOM. Add dust cover/seals or containment as a future realism improvement if powder safety matters.
- For binder addition or granulation, consider a separate high-shear mixer/granulator process rather than assuming the same low-shear powder mixer covers every feedstock operation.

## Confidence and open questions

Confidence: high that powder mixers are real and that the KB item is plausible; medium on whether this should be a distinct imported machine rather than a variant of a broader mixer item.

Open questions:

- Should the intended subtype be ribbon blender, tumbler/V blender, conical screw mixer, or high-shear mixer?
- Are metal powder dust hazards and contamination controls important enough to model as separate requirements?
- Is 80 kg intended as a lab/pilot machine? That mass is too small for many industrial mixers but plausible for a compact shop-scale unit.

