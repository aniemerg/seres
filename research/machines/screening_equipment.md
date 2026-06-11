# Screening Equipment

## Machine identity

- KB ID: `screening_equipment`
- KB name: Screening equipment
- KB file: `kb/items/machines/screening_equipment.yaml`
- Current KB type: `machine`
- Current KB mass: 56 kg
- Current KB description: vibrating screen or classifier for particle-size separation, removing agglomerates and achieving uniform particle size distribution.

## KB usage and needed function

The KB uses `screening_equipment` for particle-size classification in:

- `screening_basic_v0`
- `regolith_screening_sieving_v0`
- `mineral_processing_basic_v0`
- `powder_processing_v0`
- `electrostatic_beneficiation_regolith_v0`
- `troilite_concentration_v0`
- `extraction_raw_formation_control_material_v0_v0`

It is also included in powder quality analysis equipment. The needed function is reusable size separation of crushed ore, regolith, powders, or granular feedstock using screens, sieves, vibration, and collection fractions.

## Reality classification

Classification: real practical machine category.

Vibrating screens, sieve shakers, industrial sieves, and classifiers are standard equipment in mineral processing, aggregate handling, powder processing, recycling, food/pharma powder handling, and laboratory particle-size analysis.

The 56 kg KB mass is plausible for a small vibratory screener/sieve shaker or compact classifier. It is not enough for a large mining screen, but it is reasonable for the current small-scale regolith/powder processing model.

## Evidence links

- IQS Directory, "Vibratory Screening": describes vibratory screening as separating bulk solid materials using inertial vibration so particles pass through screen openings or move across screen mesh. Source: https://www.iqsdirectory.com/articles/vibratory-feeder/vibratory-screening.html
- 911Metallurgist, "Ore, Rock & Aggregate Screening": states that the common vibrating-screen application is separating a conglomerate of materials into size fractions, with uses including scalping, washing, dewatering, and dedusting. Source: https://www.911metallurgist.com/blog/screening/
- Xinhai, "What Are Vibrating Screens?": describes vibrating screens as crucial mineral-processing equipment for particle-size separation. Source: https://www.xinhaimining.com/newp/what-are-vibrating-screens.html
- VibraScreener: commercial supplier of round/rectangular screeners, vibratory sieves, and gyratory sifters for product quality and screening applications. Source: https://vibrascreener.com/
- Elcan Industries, "Powder Sieving Machines": describes industrial sieving/classifier equipment for powder screening, including metal powders, battery materials, and additive manufacturing. Source: https://elcanindustries.com/screening-technology/

## Commercial alternatives

- Laboratory sieve shakers for particle-size analysis.
- Compact vibratory sieve machines for powders.
- Rectangular vibrating screens for aggregate/mineral processing.
- Multi-deck screens for several size fractions.
- Air classifiers or cyclone classifiers for very fine powders where mesh screening is ineffective.

## Build or open-source references

Simple screening equipment is locally buildable: a frame, screen deck or sieve mesh, springs or compliant mounts, eccentric/vibration motor, hoppers/collection bins, and dust control.

Examples:

- Digitalfire, "Make your own sieve shaker": describes a low-cost vibrating sieve built from a vibration motor, steel parts, welded support, 3D-printed collars, and a bucket. Source: https://digitalfire.com/project/47
- Instructables, "$25 Vibrating Garden Sifter": a simple vibrating sifter for separating stones from dirt/soil. Source: https://www.instructables.com/25-Vibrating-Garden-Sifter/

These are small-scale examples, but the principle scales to industrial machines with stronger frames, dust control, replaceable screen decks, and tuned vibration drives.

## Related machine research

Related KB items:

- `screen_deck_basic`
- `vibrator_motor_small`
- `vibration_drive_module_v0`
- `metal_powder_sieving_system_v0`
- `vibratory_feeder_v0`
- `dust_collection_system`
- `rock_crusher_basic`
- `gravity_separator`
- `magnetic_separator`

`screening_equipment` can be a generic small screener, while `metal_powder_sieving_system_v0` may be a more specific powder-grade subsystem. Avoid duplicating both unless the powder system has specialized fine-mesh, ultrasonic, inert, or contamination-control features.

## Recommendation for KB realism

Keep as a real generic screening/sieving machine.

Recommended future wording: "Compact vibratory screen/sieve classifier for regolith, aggregate, and powder size fractions." If the KB later needs high-throughput mining screens or fine metal-powder classification, add scale/capability variants or use `metal_powder_sieving_system_v0` for powder-specific needs.

Do not replace with labor bot plus hand sieve for continuous processing. Labor can load, clean, and inspect screens, but vibration/classification is the machine function for repeatable throughput.

## Confidence and open questions

Confidence: high that the equipment is real and appropriate; medium that one 56 kg item covers all current scale and powder/aggregate use cases.

Open questions:

- Should the item represent a lab-scale sieve shaker or a process-scale vibratory screen?
- Does powder processing need inert/dust-controlled sieving distinct from regolith/aggregate screening?
- Should screen decks be consumable/replacement parts due to wear and blinding?
