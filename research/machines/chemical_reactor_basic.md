# Basic Chemical Reactor Machine Reality Research

## Machine identity

- KB machine id: `chemical_reactor_basic`
- KB name: Basic chemical reactor
- KB file: `kb/items/machines/chemical_reactor_basic.yaml`
- Current KB mass: 500 kg
- Current BOM: `bom_chemical_reactor_basic`
- Current recipe: `recipe_chemical_reactor_basic_v0`

## KB usage and needed function

The machine is widely used across chemical processes: acid/base reactions, sulfuric/nitric/HCl chemistry, Rochow chemistry, selenium refining, carbon monoxide oxidation, boudouard reaction, coil insulation production, high-temperature additive synthesis, and general chemical synthesis.

The needed function is a small general reactor unit with vessel, heat input/removal, agitation/mixing, gas inlet/outlet, pressure relief, temperature measurement/control, insulation, frame, and fittings. The local BOM mostly matches that concept via `chemical_reactor_vessel_v0`, heating jacket, agitator/mixer, manifolds, pressure relief, temperature controller, thermocouples, and frame.

## Reality classification

Real practical machine category, but broad.

Small stirred/jacketed chemical reactors are real, commercially available, and appropriate as a coarse KB capability. The 500 kg mass is plausible for a small pilot-scale steel or stainless reactor skid. The realism issue is that one "basic" reactor cannot safely or efficiently cover all possible chemistry without limits on pressure, temperature, corrosion resistance, catalyst handling, gas flow, solids handling, and materials of construction.

## Evidence links

- Syrris describes jacketed reactors for lab, pilot-plant, and industrial processes with temperature control, pressure control, and mixing: <https://www.syrris.com/jacketed-reactors/>
- Savannah Tank builds custom reactor vessels for mixing, heating, cooling, and controlled chemical reactions, including jackets, internal coils, agitation systems, and finishes: <https://savannahtank.com/reactors/>
- GMM Pfaudler describes alloy reactors made from stainless steel, duplex/super-duplex, Hastelloy, Monel, titanium, and cladded construction for chemical process industries, illustrating material-specific reactor selection: <https://www.gmmpfaudler.com/alloy-equipment-systems/alloy-reactors>
- University of Michigan's Visual Encyclopedia describes CSTRs as stirred tank reactors where materials enter and leave under steady-state conditions, supporting the stirred reactor concept but also showing that reactor mode matters: <https://encyclopedia.che.engin.umich.edu/cstr/>

## Commercial alternatives

- Jacketed stirred tank reactor for general liquid-phase synthesis and neutralization.
- Glass-lined or alloy reactor for corrosive acid/chloride service.
- High-pressure autoclave reactor for gas reactions and hydrogenation.
- Packed-bed or tubular reactor for catalytic gas/solid reactions.
- Molten-salt or high-temperature refractory reactor for salts, oxides, and thermal reactions.
- Bench/lab reactor system for small batches and process development.

## Build or open-source references

The current KB build path is plausible at a coarse level for a simple steel reactor: welded vessel, machined openings, instrumentation, piping/fittings, insulation, pressure testing, and final assembly.

For a real pressure or hazardous-chemistry reactor, local build would also need pressure-vessel design, certified welds, relief sizing, leak/pressure testing, corrosion-compatible materials, seals/gaskets, agitator seals, control interlocks, and process-specific hazard review. The generic recipe should be treated as a simplified placeholder, not a complete code-rated reactor fabrication plan.

## Related machine research

Related local reports:

- `research/machines/chemical_reactor_vessel_v0.md`
- `research/machines/generic_chemical_reactor_v0.md`
- `research/machines/chemical_separation_equipment.md`
- `research/machines/mre_reactor_v0.md`

These support keeping the assembled reactor distinct from the bare vessel and from generic high-temperature/electrochemical reactors.

## Recommendation for KB realism

Keep `chemical_reactor_basic` as a real coarse machine, but narrow its implied service envelope.

Recommended options:

- Define it as a small stirred/jacketed batch or semi-batch reactor, not a universal chemical plant.
- Use `chemical_reactor_basic` where the process needs moderate temperature, mixing, gas ports, and ordinary steel/stainless compatibility.
- Use more specific reactors for acid-lined, high-pressure, high-temperature molten salt, packed-bed catalytic, electrochemical, or refractory service.
- Avoid duplicating it with `generic_chemical_reactor_v0`; either make `generic_chemical_reactor_v0` the abstract placeholder and `chemical_reactor_basic` the concrete stirred/jacketed reactor, or consolidate references.
- Add service notes to hazardous processes: pressure, temperature, materials, corrosion, gas handling, and catalyst/solid compatibility.

## Confidence and open questions

Confidence: high that the machine category is real and useful; medium that it is adequate for all current KB processes.

Open questions:

- What default pressure and temperature rating should `chemical_reactor_basic` imply?
- Is the intended material carbon steel, stainless steel, glass-lined steel, or interchangeable lining?
- Which current processes should be moved to more specialized reactor classes instead of this basic reactor?
