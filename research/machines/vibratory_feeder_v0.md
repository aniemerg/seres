# Vibratory feeder v0

## Machine identity

- KB ID: `vibratory_feeder_v0`
- KB file: `kb/items/machines/vibratory_feeder_v0.yaml`
- KB name: Vibratory feeder v0
- KB mass: 240 kg per unit
- Current KB role: imported/manufactured machine for controlled feeding and metering of granular or powdered material into beneficiation and processing equipment.

## KB usage and needed function

Local references show that `vibratory_feeder_v0` is a practical feed-metering subsystem, not just a name placeholder:

- It is included in `kb/scenarios/min_seed.yaml`.
- It is required by `beneficiation_magnetic_basic_v0`, `beneficiate_regolith_magnetic_v0`, and `electrostatic_beneficiation_regolith_v0`.
- It appears as a BOM component in `bom_electrostatic_separator_v0`, `bom_magnetic_separator_drum_v0`, and `bom_selective_solar_sinterer_v0`.
- Its own BOM uses a feeder trough, vibration motor set, welded support frame, controls, sensors, power conditioning, and fasteners.

The needed function is continuous, controllable delivery of regolith powder or other granular feedstock at a steady rate into downstream separators or sintering equipment. The KB BOM is consistent with a pan/trough-style industrial vibratory feeder rather than a small parts-orienting bowl feeder.

## Reality classification

Classification: real practical machine.

Vibratory feeders are standard industrial bulk-material handling machines. Commercial machines commonly use a trough or pan, electromagnetic or motor-driven vibration, springs/support structure, and a controller. The KB item is more specific than a generic category because it has a concrete BOM and mass estimate, but its name could be clearer as a bulk-material vibratory feeder.

## Evidence links

- Carrier Vibrating Equipment describes industrial vibratory feeders that meter bulk solids at controlled feed rates and offers multiple drive designs: https://carriervibrating.com/equipment/feeders/vibrating/
- Syntron Material Handling lists volumetric feeder systems with vibrating trough options, electromagnetic vibrators, and variable power control: https://syntronmh.com/en/products/feeder-systems
- General Kinematics describes vibrating feeders for bulk-material flow control, with a material-transporting trough or platform driven by a vibratory force system: https://www.generalkinematics.com/vibrating-feeders-for-stockpile-and-reclaim-gk-feeders/
- Sinfonia Technology's vibrating feeder catalog describes electromagnetic feeders as troughs, electromagnets, and leaf springs controlled electrically: https://www.sinfo-t.com/application/files/4117/1392/3553/E93-001.pdf
- Automation Devices sells amplitude controllers for vibratory feeder systems, supporting the KB inclusion of control electronics: https://www.autodev.com/vibratory-feeder-amplitude-controllers

## Commercial alternatives

Commercially available substitutes include:

- Carrier industrial vibrating feeders for bulk solids metering.
- Syntron volumetric feeder machines with flat pan, V-shaped, tubular, or screening troughs.
- General Kinematics feeders for stockpile, reclaim, and process-feed applications.
- Sinfonia electromagnetic feeders for controlled material handling.

These are commercially mature and support keeping the imported machine as a realistic item. For lunar/regolith modeling, an industrial trough or pan feeder is a better analog than a vibratory bowl feeder, which is optimized for orienting small discrete parts.

## Build or open-source references

- Bruce's Makes documents a simple linear vibratory feeder built with 3D printed parts and a frequency-control circuit: https://www.brucesmakes.com/projects/linear-vibratory-feeder
- ByTechLab documents a DIY vibratory bowl feeder prototype using printed parts, an electromagnet, springs, and tuning/adjustment: https://bytechlab.com/2018/07/smd-parts-bowl-feeder-prototype/
- Washington University student project brief on vibratory parts feeders describes modular, tunable vibratory feeders for moving parts: https://openscholarship.wustl.edu/cgi/viewcontent.cgi?article=1045&context=jme410

These build references support manufacturability of the basic mechanism, but they are mostly small parts-feeder examples. A KB-scale regolith feeder should retain heavier steel trough/support components and industrial controls.

## Related machine research

No existing `research/machines` reports were present at the start of this task. Related KB machines that may benefit from cross-checking later include:

- `magnetic_separator_drum_v0`
- `electrostatic_separator_v0`
- `screening_equipment`
- `selective_solar_sinterer_v0`

No follow-up tasks were enqueued, per task constraint.

## Recommendation for KB realism

Keep `vibratory_feeder_v0` as a real imported/manufacturable machine.

Recommended cleanup when KB edits are allowed:

- Rename or annotate display name as "Bulk-material vibratory feeder" or "Vibratory trough feeder" to distinguish it from small parts-orienting bowl feeders.
- Keep the current BOM structure. The trough, vibration motor set, welded frame, controller/sensor package, power conditioning, and fasteners are realistic subsystem categories.
- Keep mass at 240 kg as plausible for a small industrial trough feeder with frame and controls. The exact value depends heavily on trough size, liner, throughput, and regolith abrasion assumptions.
- In process notes, describe its role as metering granular regolith into separators, not sorting/orienting discrete parts.

## Confidence and open questions

Confidence: high that the item represents a real practical machine and that the KB usage is plausible.

Open questions:

- Required throughput for lunar regolith beneficiation is not specified in the feeder item. Feeder mass and motor power should eventually scale with target kg/hr, trough dimensions, and abrasion/wear allowance.
- The KB item does not yet separate feeder sizes. Under Conservative Mode, keep one shared feeder unless future throughput differs by more than about 5x or material compatibility requires a different construction.
- Lunar dust abrasion and vacuum operation may require sealed bearings, different motor/control packaging, or replaceable liners; those are refinements, not reasons to remove the item.
