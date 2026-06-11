# Chemical Reactor Vessel v0 Machine Reality Research

## Machine identity

- KB item id: `chemical_reactor_vessel_v0`
- KB name: Chemical reactor vessel v0
- KB file: `kb/items/machines/chemical_reactor_vessel_v0.yaml`
- Current KB kind: `machine`
- Current KB mass: 120 kg
- Current BOM: `bom_chemical_reactor_vessel_v0`
- Current recipe: `recipe_chemical_reactor_vessel_v0`

## KB usage and needed function

The item is a component of `bom_chemical_reactor_basic`, where it is combined with a heating jacket, agitator/mixer, gas manifolds, pressure relief, temperature controls, thermocouples, frame, and fasteners.

It is also directly required by `chemical_synthesis_process_v0`, where it appears as a machine resource. That usage probably treats the vessel as shorthand for a complete reaction capability.

The needed function is a chemically compatible vessel or pressure vessel with ports, fittings, sensors, seals, and possibly pressure/temperature rating. By itself, a vessel does not provide agitation, heat transfer, pressure relief, feed control, or process control.

## Reality classification

Real practical equipment component, but not a complete machine.

Chemical reactor vessels and pressure vessels are standard industrial items. The current KB item is best interpreted as the shell/subassembly of a reactor, not as a standalone chemical reactor. Its 120 kg mass is plausible for a small pilot-scale steel or stainless vessel with ports and fittings, but too generic for all KB chemistry because material compatibility, pressure, temperature, corrosion resistance, and code compliance vary widely.

## Evidence links

- Pope Scientific sells stainless steel portable pressure vessels, reactors, blenders, and turnkey processing systems, showing the distinction between a vessel and an assembled process system: <https://www.popeinc.com/equipment/pressure-vessels-reactors/>
- Syrris describes jacketed reactors as vessels for controlled temperature, pressure, and mixing in lab, pilot, and industrial processes: <https://www.syrris.com/jacketed-reactors/>
- Savannah Tank describes custom reactor vessels engineered for mixing, heating, cooling, and controlled chemical reactions, with jackets, internal coils, agitation systems, and finishes: <https://savannahtank.com/reactors/>
- High Pressure Equipment Company manufactures pressure vessels and reactors for bench-scale and pilot-plant use, including ASME-code options across size, material, pressure, and temperature ranges: <https://www.highpressure.com/products/reactors-pressure-vessels/>

## Commercial alternatives

- Stainless steel pressure vessel or portable reactor vessel for general pilot work.
- Jacketed stirred-tank reactor for controlled heating/cooling and mixing.
- Glass-lined or PTFE-lined reactor vessel for corrosive chemistry.
- High-pressure autoclave reactor for elevated-pressure hydrogenation or gas reactions.
- Custom ASME pressure vessel with specified material, pressure rating, relief devices, nozzles, and instrumentation.

## Build or open-source references

No open-source design suitable for a safe pressure-rated chemical reactor vessel was identified in this pass. Simple atmospheric tanks can be fabricated locally, but pressure vessels require design calculations, certified welding practices, inspection, hydrostatic testing, pressure relief, and material traceability.

The current KB recipe is acceptable only as a placeholder for a low-pressure or non-code vessel. For pressure, high-temperature, acid, oxidizer, hydrogen, or vacuum service, the recipe should require more specific fabrication and inspection steps than generic `metal_parts_fabrication_v0`.

## Related machine research

Related local reports:

- `research/machines/generic_chemical_reactor_v0.md`
- `research/machines/chemical_separation_equipment.md`
- `research/machines/mre_reactor_v0.md`

Those reports support treating generic chemical equipment as a family of specific vessel, heating, mixing, gas-handling, and separation capabilities rather than one universal machine.

## Recommendation for KB realism

Keep the item, but make its component role explicit.

Recommended options:

- Reclassify or annotate as `reactor_vessel_subassembly` or `chemical_reactor_vessel_shell` if schema support allows.
- Avoid using it directly as a process machine unless the process only needs a passive vessel; most reactions should require `chemical_reactor_basic`, `generic_chemical_reactor_v0`, or a more specific reactor unit.
- Split future variants by service class when needed: atmospheric tank, pressure vessel, jacketed stirred vessel, acid-lined vessel, high-temperature refractory vessel, or high-pressure gas reactor.
- Add pressure/temperature/material compatibility notes where the vessel is used for hazardous or aggressive chemistry.
- Keep the 120 kg mass only for a small pilot-scale vessel; do not use it as an industrial production reactor by default.

## Confidence and open questions

Confidence: high that reactor vessels are real and that this item is better modeled as a component than a full machine; medium on the current 120 kg mass because volume, pressure rating, and material are not specified.

Open questions:

- Is `chemical_synthesis_process_v0` intended to require a full reactor unit rather than only the vessel?
- Should the KB distinguish ASME/code pressure vessels from non-pressure or low-pressure reactor tanks?
- Which chemistries in the KB actually require corrosion-resistant linings, glass lining, nickel alloys, refractory lining, or high-pressure construction?
