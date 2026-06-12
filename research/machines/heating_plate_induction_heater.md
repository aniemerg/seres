# Heating Plate Induction Heater

## Machine identity

- KB ID: `heating_plate_induction_heater`
- KB name: Heating plate induction heater
- KB file: `kb/items/machines/heating_plate_induction_heater.yaml`
- Current KB type: `machine`
- Current KB mass: 25 kg
- Current KB description: induction heating plate for thermal fitting and heat treatment, used for expanding bearing housings or shrinking shafts for interference fits.
- Current KB BOM: heating plate base, induction coil or heating element, temperature controller, power conditioning, thermal insulation, and fasteners.

## KB usage and needed function

The KB uses `heating_plate_induction_heater` for:

- `bearing_installation_basic_v0`
- `bom_plastic_extruder_v0`
- `bom_reactor_heating_cooling_system_v0`

The primary needed function is controlled local heating for thermal fits: expanding bearings, rings, housings, or toolholders so they can be mounted without excessive mechanical force. Its use inside a plastic extruder or reactor heating/cooling system is broader and may mean "small controlled heater" rather than specifically induction shrink fitting.

## Reality classification

Classification: real practical small heating machine, but name/scope is ambiguous.

Induction bearing heaters and shrink-fit induction heaters are real. Hot plate bearing heaters are also real. They are related but not identical. Induction heats the conductive part directly through electromagnetic coupling; hot plates heat by conduction from a heated surface.

The KB mass of 25 kg is plausible for a portable bearing heater, hot plate heater, or small induction shrink-fit unit. The BOM is plausible for a combined placeholder, but a real induction heater needs suitable coil/yoke geometry, power electronics, and often demagnetization or temperature control for bearings.

## Evidence links

- SKF sells induction heaters for efficiently heating bearings and workpieces, large and small. Source: https://www.skf.com/us/products/maintenance-products/bearing-heaters/heaters-for-mounting/induction-heaters
- Grainger describes bearing heaters as temporarily expanding a bearing bore so it can slide onto a shaft, with even heating and less risk of shaft damage. Source: https://www.grainger.com/category/power-transmission/bearings/bearing-heaters
- Ambrell describes induction shrink fitting, including heating gears and housings so interference-fit parts can be assembled, with faster localized heating than ovens. Source: https://www.ambrell.com/induction-heating-applications/shrink-fitting
- Schaeffler describes inductive heating devices for complete rolling bearings, inner rings, and other rotary machine elements that are thermally expanded before shaft mounting. Source: https://medias.schaeffler.us/en/plp/InductiveHeatingDevicesHEATER
- GlobalSpec lists bearing heater types as yoke style, cone style, and hot plates. Source: https://www.globalspec.com/learnmore/manufacturing_process_equipment/industrial_assembly/bearing_heaters
- IKA sells laboratory hot plates with ceramic/glass platforms, safety circuits, hot-surface indication, and temperature-control accessories. Source: https://www.ika.com/en/Products-LabEq/Hot-Plates-pg212/

## Commercial alternatives

- Induction bearing heater with yokes.
- Cone-style bearing heater.
- Flat hot-plate bearing heater.
- Induction shrink-fit machine for toolholders.
- Lab hot plate or industrial heating plate.
- Small oven/furnace for uniform heating.
- Induction forge/heater for larger billets and rings.

## Build or open-source references

A small resistive hot plate is locally buildable from a metal plate, resistive heating element, thermocouple, controller, insulation, and enclosure.

A practical induction heater needs:

- Copper induction coil or transformer/yoke.
- High-current power electronics and resonant/tank components.
- Temperature sensor and control logic.
- Electrical insulation, shielding, grounding, and cooling.
- Workpiece-specific geometry for efficient coupling.
- Demagnetization consideration for bearings where needed.

The current KB recipe allows either induction coil or resistive heating elements, which is useful but should be made explicit.

## Related machine research

Related reports already present:

- `induction_forge_v0.md`
- `heat_treatment_furnace_v0.md`
- `plastic_extruder.md`
- `hydraulic_press.md`
- `power_conditioning_equipment.md`

`induction_forge_v0` is the larger billet/bar forging heater. This item should remain a small thermal-fit or hot-plate heater.

## Recommendation for KB realism

Keep the item, but clarify the name and intended heater type.

Recommended future paths:

- If used for bearing installation, rename to `induction_bearing_heater_v0` or `thermal_fit_heater_v0`.
- If used as a general heating plate in plastic extrusion/reactors, rename to `controlled_heating_plate_v0`.
- If both functions are needed, split induction bearing heater from resistive heating plate.

Do not treat this as a general heat-treatment furnace. It is a small local heater for parts or surfaces.

## Confidence and open questions

Confidence: high that bearing/shrink-fit heaters and hot plates are real; medium that the combined KB name should remain one item.

Open questions:

- Is the intended mechanism induction, resistive hot plate, or either?
- Does bearing installation require demagnetization after induction heating?
- Should plastic extruder barrel heaters be separate from bearing thermal-fit heaters?
