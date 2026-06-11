# Cement mixer small

## Machine identity

- KB ID: `cement_mixer_small`
- KB file: `kb/items/machines/cement_mixer_small.yaml`
- KB name: Cement mixer (small)
- KB mass: 309.5 kg per unit
- Current KB role: small mixer for binder preparation and refractory/cement-like material mixing.

## KB usage and needed function

Local usage indicates that `cement_mixer_small` is a supporting construction/fabrication machine:

- It is listed in `docs/self_reproducing_set.txt` and `docs/self_reproduction_imported_machines.md`.
- It is a BOM component of `refractory_installation_tools`.
- Its own BOM includes a mixer frame, mixer drum, mixer motor, controls, medium drive motor, gearbox reducer, heavy bearing set, and fasteners.
- Part-level recipe notes describe a 100-150 L steel drum with internal mixing fins/paddles.

The required function is batch mixing of cementitious or refractory binder mixtures, probably for installation of furnace linings or other mineral/construction materials. It is not being used as precision chemical processing equipment.

## Reality classification

Classification: real practical machine.

Small cement/concrete mixers are commodity construction machines. The KB's drum, frame, motor, gearbox, bearing, and fastener structure matches commercial manuals and parts lists. The KB mass of 309.5 kg is heavier than many homeowner portable mixers, but it is plausible for a rugged small industrial mixer, refractory-duty mixer, or conservative imported-mass estimate.

## Evidence links

- Multiquip lists portable concrete mixers, including small Mix-n-Go models for homeowners and small contractors: https://www.multiquip.com/multiquip/concrete-mixers.htm
- Multiquip MC3 Series manual documents portable concrete mixers and their safe operation: https://www.multiquip.com/multiquip/pdfs/Mixers_portable_multiquip_MC3_SERIES_Briggs_Electric_rev_5_manual_DataId_18820_Version_1.pdf
- Marshalltown concrete mixer operations manual and parts list covers mixer operation and components: https://marshalltown.com/documents/Concrete%20Mixer%20Operators%20Manual%20Parts.pdf
- Northern Tool electric cement mixer manual describes assembly around a gearbox motor assembly mounting frame, front frame, support legs, wheels, handles, and hardware: https://assets.northerntool.com/products/998/documents/manuals/998251.pdf
- Bartell Global concrete mixer parts book includes frame, drum, transmission, hood, and related assemblies: https://www.bartellglobal.com/wp-content/uploads/concrete-mixers-parts.pdf

## Commercial alternatives

Commercial substitutes include:

- Small electric portable mixers in the 2-6 cu ft class.
- Multiquip Mix-n-Go portable mixers with electric, battery, or engine drive options.
- Marshalltown, Bartell, TK, Kushlan, Klutch, Ryobi, and similar jobsite mixers.
- Larger JZC-style gear-driven drum mixers if the KB needs a heavier industrial analog.

For the KB's refractory/tooling role, a small drum mixer is realistic. A mortar mixer or pan mixer might be a better alternate if future recipes require stiff refractory mixes rather than normal concrete consistency.

## Build or open-source references

- Open Hardware Observatory lists homemade concrete mixer examples, including machines made from tubing, a drum, electric motor, and gearbox: https://en.oho.wiki/wiki/Category%3AConcrete_mixers
- Homemade and shop-built drum mixers are common; examples include 55-gallon drum concrete mixer builds and hydraulic/electric shop-built mixers. These are useful build analogs but have uneven documentation and should not override commercial manuals for KB structure.

The basic build path is mechanically straightforward: fabricate a frame, drum/trunnion or axle support, drive reduction, bearings, and guarding, then add power/control hardware. Wear surfaces and cleaning access matter for refractory use.

## Related machine research

Related KB items:

- `refractory_installation_tools`
- `mixer_drum_small`
- `mixer_frame_small`
- `mixer_control_basic`
- `gearbox_reducer_medium`

No follow-up tasks were enqueued, per task constraint.

## Recommendation for KB realism

Keep `cement_mixer_small` as a real practical machine.

Recommended cleanup when KB edits are allowed:

- Clarify whether this is a small portable concrete mixer, refractory mortar mixer, or ruggedized small industrial mixer.
- If the intent is a common portable 100-150 L mixer, consider reviewing the 309.5 kg mass; many commercial portable mixers are much lighter. If the intent is a conservative industrial/refractory mixer, document that assumption in the item notes.
- Consider whether both `mixer_motor_small` and `drive_motor_medium` are needed in the BOM. Commercial mixers normally have one primary motor/engine plus gearbox/transmission, not two independent drive motors unless one represents controls/accessory drive.
- Keep the drum, frame, gearbox/reducer, bearing, controls, and fasteners as realistic subsystem categories.

## Confidence and open questions

Confidence: high that the machine is real and useful for the modeled function.

Open questions:

- What batch size does the self-reproducing set actually need for refractory/binder work?
- Should this be a drum mixer, mortar mixer, or pan mixer?
- Is the current mass intended to include ruggedization, spare wear parts, or only one operating unit?
