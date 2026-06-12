# Vibrating screen v0

## Machine identity

- KB ID: `vibrating_screen_v0`
- KB file: `kb/items/machines/vibrating_screen_v0.yaml`
- KB name: Vibrating screen v0
- KB mass: 180 kg per unit
- Current KB role: vibrating screen for regolith/mineral particle-size separation.

## KB usage and needed function

Local usage shows a concrete mineral-processing screen:

- It is listed in the minimal/self-reproducing machine set.
- It is required by `crushing_and_screening_basic_v0`, `regolith_screening_sieving_v0`, `olivine_beneficiation_v0`, and `pyroxene_separation_v0`.
- `screening_equipment` also exists and is used by many broader screening/mineral processing processes.
- BOMs and parts include `screen_deck_basic`, vibration drive/module, frame, springs, fasteners, and sensors/controls.
- `research/machines/vibratory_feeder_v0.md` and `research/machines/dust_collection_system.md` list it as related equipment.

The needed function is mechanical classification of granular material by particle size using a vibrating screen deck/mesh.

## Reality classification

Classification: real practical machine.

Vibrating screens are standard mineral-processing and bulk-material equipment. The KB item is realistic for regolith sieving and beneficiation. It may overlap with the more generic `screening_equipment` item; the useful distinction is that this is specifically a vibrating deck/screen.

## Evidence links

- JXSC describes vibrating screens for mineral screening that move raw materials over mesh to separate fine particles from larger pieces: https://www.minejxsc.com/mineral-processing-equipment/classifying-screening-machines/vibrating-screens/
- McLanahan describes multi-deck vibratory screens using eccentric motors and screen decks to produce size fractions: https://www.mclanahan.com/products/md-vibratory-screens
- IQS Directory describes vibratory screening as separating bulk solids using inertial vibrations and screen openings: https://www.iqsdirectory.com/articles/vibratory-feeder/vibratory-screening.html
- 911 Metallurgist explains a single-deck vibrating screen on springs driven by an unbalanced flywheel: https://www.911metallurgist.com/blog/vibrating-screen-working-principle/
- MDPI Applied Sciences presents an automated dry sieving mechanism for lunar regolith sorting, including anti-blocking design, natural frequencies, and adjustable sieve angles: https://www.mdpi.com/2076-3417/15/4/2227
- Komplet America describes linear vibrating screens using counter-rotating eccentric shafts or synchronized vibrator motors: https://kompletamerica.com/differences-between-linear-screen-and-circular-vibrating-screen/

## Commercial alternatives

Commercial alternatives include:

- Single-deck or multi-deck vibrating screens.
- Linear or circular vibrating screens.
- Gyratory screeners.
- Rotary trommel screens.
- Static screens for coarse, low-throughput classification.
- Air classifiers for finer dry powders.

For regolith, screen blinding, dust containment, vacuum compatibility, wear, and electrostatic effects are likely more important than Earth-normal soil screening assumptions.

## Build or open-source references

- Instructables documents converting a soil screener to electric vibration, including eccentric weights and screening tests: https://www.instructables.com/Soil-Screener-From-Gas-to-Electric/
- DIY soil/compost screeners commonly use a frame, mesh, springs or flexible supports, and an eccentric motor. These are credible low-throughput analogs, though not suitable evidence for lunar/vacuum operation.

Local fabrication is plausible with a welded frame, replaceable screen mesh/deck, vibration motor or eccentric shaft, isolating springs, dust cover, and simple controls.

## Related machine research

Related local reports:

- `research/machines/vibratory_feeder_v0.md`
- `research/machines/dust_collection_system.md`

Related KB items:

- `screening_equipment`
- `screen_deck_basic`
- `vibration_drive_module`
- `vibrator_motor_small`
- `air_classifier`
- `dust_collection_system`

No follow-up tasks were enqueued, per task constraint.

## Recommendation for KB realism

Keep as a real vibrating-screen subtype, but review overlap with `screening_equipment`.

Recommended cleanup when KB edits are allowed:

- If `screening_equipment` is intended to mean a vibrating screen, consolidate references into one canonical item.
- If both remain, document `screening_equipment` as a broader screening kit/station and `vibrating_screen_v0` as the concrete vibrating deck machine.
- Add notes for mesh size, deck area, throughput, dust containment, and screen blinding risks.
- Keep the 180 kg mass as plausible for a small industrial/regolith screen; larger aggregate/mining screens are much heavier.

## Confidence and open questions

Confidence: high that the machine is real and useful.

Open questions:

- Should `vibrating_screen_v0` and `screening_equipment` be merged?
- What particle-size cut points and throughput are required for regolith processes?
- Does lunar vacuum/dust require sealed bearings, dust covers, or alternate actuation?
