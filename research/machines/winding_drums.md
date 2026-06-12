# Winding Drums Machine Reality Research

## Machine identity

- KB item id: `winding_drums`
- KB name: Winding drums set
- KB file: `kb/items/parts/winding_drums.yaml`
- Current KB kind: `machine`
- Current KB mass: 51 kg
- Current BOM: `bom_winding_drums`
- Current recipe: `recipe_winding_drums_v0`

## KB usage and needed function

The item is used by `basalt_fiber_production_v0` and `spool_winding_basic_v0`. It is also a BOM component of `winding_machine_v0`.

The needed function is a set of rotating drums/spindles with shafts, bearings, and tension/traverse support for winding continuous material such as fiber, wire, cable, or strip onto spools. This is a subassembly of a winder, not a full winding machine by itself.

## Reality classification

Real practical subassembly/tooling set, not a standalone machine.

Winding drums, take-up spindles, creels, and traverse/tension systems are real. The KB's 51 kg mass is plausible for a set of small-to-medium drums with shafts and bearings. The main realism issue is classification: this should be a component of a winding machine or winding station, not counted as an independent imported machine unless the simulator needs it as a resource provider.

## Evidence links

- International Rolling Mills lists a custom traverse winding machine for precision spooling of wire, strip, ribbon, and continuous materials using controlled traverse winding: <https://www.introllingmills.com/ko/equipment/9053981-custom-traverse-winding-machine-traverse-winding-machines>
- Engineering Technology Corporation describes filament winders with wet winding drums and creel tensioners for controlled fiber winding: <https://etcwinders.com/standard-filament-winders/sc-filament-winder/>
- Amacoil explains that traverse drives guide material back and forth across a take-up spool and must coordinate pitch with spool rotation: <https://www.amacoil.com/news-articles/traverse-selection-winding-system/>
- Ridgway Machines describes coil manufacturing equipment where a drum stand rotates under motor/drive control: <https://www.ridgwayeng.com/coil-manufacturing-and-winding/>

## Commercial alternatives

- Simple manual spool stand/take-up drum.
- Motorized take-up winder with traverse guide.
- Precision coil winding machine for electrical coils.
- Filament winding machine with creel, tensioner, resin bath, mandrel/drum, and controls.
- Cable drum take-up machine with hydraulic lift and traverse.

## Build or open-source references

The drums themselves can be machined from steel or aluminum with shafts, bearings, mounts, and surface finish suitable for the material. Real winding quality also needs tension control, traverse mechanism, braking/drive control, spool mounting, guarding, and sometimes resin bath or heating/drying.

The KB recipe is plausible for drum subassemblies, but not enough for a complete coil/fiber/cable winding machine.

## Related machine research

Related local reports:

- `research/machines/coil_winding_machine.md`
- `research/machines/tension_gauge.md`

Related KB items:

- `coil_winding_machine`
- `coil_winding_machine_v0`
- `winding_machine_v0`
- `wire_tensioning_system`

## Recommendation for KB realism

Keep as a subassembly or tooling set, not a complete machine.

Recommended options:

- Treat `winding_drums` as a component of `winding_machine_v0` or fiber/wire take-up equipment.
- For electrical coils, use `coil_winding_machine` rather than bare winding drums.
- For basalt fiber, pair winding drums with tension control, traverse, speed control, and upstream fiber production equipment.
- Reclassify from `machine` to part/subassembly when schema support allows.
- Consider whether `spool_winding_basic_v0` should require a complete winding machine rather than only drums.

## Confidence and open questions

Confidence: high that winding drums are real; high that they are a subassembly rather than a standalone machine; medium on whether 51 kg matches the intended fiber/cable scale.

Open questions:

- Are these drums driven, braked, or passive?
- Should `winding_drums` include traverse/tension mechanisms, or should those be separate items?
- Does basalt fiber production need precision tension control beyond simple take-up winding?
