# Injection molding machine v0

## Machine identity

- KB ID: `injection_molding_machine_v0`
- Proposed KB file: `kb/items/machines/injection_molding_machine_v0.yaml`
- Role: dedicated thermoplastic injection molding machine for small housings and molded plastic parts.

## Research summary

Injection molding is distinct from compression molding and extrusion. The machine combines a plasticizing/injection unit, heated barrel/screw/nozzle, a clamping unit with platens, mold mounting/ejection support, hydraulic or electric drives, temperature control, cooling, and controls.

Reference summaries:

- MD Plastics describes core injection-molding-machine components as injection unit, clamping unit, mold, control system, drive system, cooling system, and ejector system: https://mdplastics.com/feeds/blog/injection-molding-machine-components
- Polymer Molding describes the injection unit as hopper, barrel, screw, and nozzle that heat and deliver molten plastic into the mold: https://www.polymermolding.com/a-brief-guide-to-plastic-injection-molding-machines/
- University of Maryland training material divides the process into injection unit, mold, and clamping unit, with clamping opening/closing the mold and ejecting the finished product: https://dozuki.umd.edu/Wiki/Injection_molding_process
- General injection-molding references describe pellets fed into a heated barrel, plasticized by a screw or ram, injected into a cooled mold cavity, packed/held, cooled, and ejected.

## KB modeling decision

Create `injection_molding_machine_v0` as the machine resource for pellet-to-molded thermoplastic housings and small parts. Scope it as a small shop/lab thermoplastic injection molding machine, not a general `molding_press_basic` and not a `plastic_extruder`.

Boundaries:

- `molding_press_basic`: compression/cold or modest-temperature platen pressing; no screw plasticization or melt injection.
- `plastic_extruder`: continuous profile/sheet/filament extrusion through a die; no closed mold clamping/ejection cycle.
- `injection_molding_machine_v0`: pellet feed, plasticizing screw/barrel/nozzle, high-pressure injection into a closed mold, clamp/platens, cooling, and ejection support.

Use this resource for `plastic_housing_molding_v0` and similar pellet-to-housing routes when the intended operation is true injection molding.

