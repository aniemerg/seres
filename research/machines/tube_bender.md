# Tube Bender Machine Reality Research

## Machine identity

- KB machine id: `tube_bender`
- KB name: Tube bending machine
- KB file: `kb/items/machines/tube_bender.yaml`
- Current KB mass: 200 kg
- Current BOM: `bom_tube_bender_v0`
- Current recipe: `recipe_machine_tube_bender_v0`

## KB usage and needed function

The item is required by `tube_bending_and_cutting_v0`, `tube_forming_process_v0`, and `tube_stock_forming_v0`. It supports local fabrication of piping assemblies, tube coils, fittings, and bent tube sections.

The needed function is controlled bending of metal tube without unacceptable collapse, wrinkling, flattening, or radius error. Important parameters are outside diameter, wall thickness, bend radius, material, bend angle, mandrel use, die set, and repeatability.

## Reality classification

Real practical machine.

Tube benders are standard fabrication equipment. The KB's stated 6-50 mm tube range is realistic for bench, hydraulic, electric, or small CNC tube benders. The 200 kg mass is plausible for a hydraulic or light industrial bender, heavier than hand benders but lighter than production CNC machines.

## Evidence links

- Kaka Industrial sells a JTB-50 tube/profile bending machine for steel tubes up to 48.3 mm, close to the KB's 50 mm upper range: <https://www.kakaindustrial.com/products/kaka-industrial-jtb-50-tube-bending-machine>
- Winton Machine describes rotary draw tube benders, with and without mandrels, using die sets with constant centerline radius and programmable bend jobs: <https://www.wintonmachine.com/tube-fabrication/rotary-draw-tube-benders>
- BLM Group lists CNC tube bending machines for small-to-medium diameter tubes and coil-fed tube processing: <https://www.blmgroup.com/en-us/tube-bending-machines>
- Swagelok lists hand, benchtop, and electric tube benders covering tube outside diameters from small instrument tubing up to 50 mm for electric benders: <https://products.swagelok.com/en/all-products/tubing-tube-accessories/tube-benders/c/803>

## Commercial alternatives

- Hand tube bender for small soft tubing.
- Benchtop bender for instrument tubing and small production.
- Hydraulic tube/pipe bender for shop fabrication.
- Rotary draw mandrel bender for tight-radius or thin-wall tube.
- CNC tube bender for repeatable multi-bend parts and production quantities.

## Build or open-source references

Simple tube benders can be locally fabricated from a rigid frame, forming die, follower die/pressure shoe, pivot/rotary arm, hydraulic cylinder or screw drive, and angle stop. More precise machines require matched tooling, mandrels, wiper dies, clamps, lubrication, and controls.

The KB recipe is plausible for a basic hydraulic/light industrial bender, but bend quality depends heavily on die sets and mandrels. Those may need separate tooling if the KB uses thin-wall tubing, tight radii, or pressure/vacuum piping.

## Related machine research

Related local reports:

- `research/machines/metal_forming_basic_v0.md`
- `research/machines/metal_shear_or_saw.md`
- `research/machines/press_brake.md`
- `research/machines/hydraulic_press.md`

## Recommendation for KB realism

Keep `tube_bender` as a real, distinct machine.

Recommended options:

- Keep separate from `press_brake`; tube bending and sheet bending use different tooling and constraints.
- Add or document tube bending die sets/mandrels where bend quality matters.
- Use hand/benchtop/hydraulic/CNC variants only if process scale or tolerance requires it.
- Pair with cutting/deburring tools and leak testing for piping assemblies.
- Keep 200 kg as a plausible light industrial default.

## Confidence and open questions

Confidence: high that this is real and appropriate; medium on whether the KB needs mandrel/CNC features for all current tube processes.

Open questions:

- What tube wall thickness and minimum bend radius are assumed?
- Should mandrels, wiper dies, and tube-specific die sets be modeled separately?
- Are these bends for low-pressure frames/coils or leak-tight pressure piping?
