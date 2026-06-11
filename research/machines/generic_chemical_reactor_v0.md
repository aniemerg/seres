# Generic chemical reactor v0

## Machine identity

- KB ID: `generic_chemical_reactor_v0`
- KB file: `kb/items/machines/generic_chemical_reactor_v0.yaml`
- KB name: Generic chemical reactor
- KB mass: 250 kg per unit
- Current KB role: coarse shared reactor capacity for many chemical synthesis, acid/base, gas-phase, reduction, hydrolysis, and polymerization processes.

## KB usage and needed function

Local usage confirms the item is a broad closure placeholder:

- It is listed in the minimal/self-reproducing machine set.
- The item notes explicitly say it is a placeholder generic chemical reactor to support KB closure.
- It is referenced by many processes: silicone precursor/polymer synthesis, methanol synthesis, reverse water-gas shift, Sabatier/Bosch reactions, chlorination routes, nitric/sulfuric acid dilution, nickel/cobalt carbonyl steps, alumina/mineral reactions, and other chemistry.
- Related machines include `chemical_reactor_basic`, `chemical_reactor_vessel_v0`, `chemical_reactor_unit_v1`, `acid_reactor_v0`, and `chemical_separation_equipment`.

The needed function is currently "some reactor for chemistry." That is useful for coarse closure, but it combines incompatible requirements: corrosive acids, high pressure gases, high temperature reductions, catalytic packed beds, stirred liquid reactors, and polymerization vessels.

## Reality classification

Classification: real equipment category / placeholder, not a single practical universal machine.

Chemical reactors are real, but a generic reactor that safely handles all current KB processes is not realistic as one physical machine. Interpreted conservatively, `generic_chemical_reactor_v0` can stand for a small stirred/jacketed batch reactor with generic heat, agitation, pressure, and control capability. It should not silently cover every chemistry without notes.

## Evidence links

- Essential Chemical Industry describes common reactor categories including tubular, fixed bed, fluid bed, and continuous stirred tank reactors: https://www.essentialchemicalindustry.org/processes/chemical-reactors.html
- University of Michigan's Visual Encyclopedia describes CSTR design as a tank with stirring system plus feed and exit pipes: https://encyclopedia.che.engin.umich.edu/cstr/
- Mettler Toledo describes a CSTR as a vessel where reagents flow in and product exits while contents are stirred: https://www.mt.com/us/en/home/applications/L1_AutoChem_Applications/L2_ReactionAnalysis/continuous-stirred-tank-reactor-cstr.html
- Thermopedia describes heat transfer in agitated vessels using external jackets or internal coils: https://www.thermopedia.com/content/547/
- EPCM Holdings summarizes chemical reactor types and operations, including CSTRs, packed beds, and tubular reactors: https://epcmholdings.com/chemical-reactors-types-and-operations/
- GlasKeller describes jacketed reactors as vessels with an inner reaction chamber and outer heat-transfer jacket for temperature control: https://www.glaskeller.ch/en/jacketed-reactors-a-comprehensive-guide/

## Commercial Alternatives

Commercial alternatives depend on chemistry:

- Jacketed stirred batch reactors for liquid chemistry and polymerization.
- CSTRs for continuous stirred liquid reactions.
- Tubular/plug-flow reactors for high-temperature or gas-phase chemistry.
- Packed-bed reactors for catalytic gas/liquid reactions.
- Fluidized-bed reactors for solids/gas reactions and high heat/mass transfer.
- Acid-resistant glass-lined or polymer-lined reactors for corrosive acid chemistry.
- Pressure reactors/autoclaves for pressurized hydrogenation, carbonyl chemistry, or gas reactions.

The KB should only keep one generic reactor while process detail remains coarse. Specific reactor types become necessary when pressure, corrosion, temperature, catalyst geometry, or safety envelope changes materially.

## Build or open-source references

Open-source build references are not generally appropriate for pressure or hazardous chemical reactors. Practical build analogs are:

- Non-pressure mixing tanks with agitators and heating/cooling jackets.
- Laboratory glassware reactors for low-pressure chemistry.
- Welded steel vessels with agitation and jacket/coil heat transfer for low-risk processes.

Pressure, high-temperature, corrosive, or flammable reactions require qualified pressure-vessel design, compatible seals/liners, relief systems, controls, and hazard review. Those requirements should not be hidden under a generic item.

## Related machine research

Related local reports:

- `research/machines/chemical_separation_equipment.md`
- `research/machines/mre_reactor_v0.md`

Related KB items:

- `chemical_reactor_basic`
- `chemical_reactor_vessel_v0`
- `chemical_reactor_unit_v1`
- `acid_reactor_v0`
- `generic_chemical_reactor_pressure_v0`
- `chemical_separation_equipment`

No follow-up tasks were enqueued, per task constraint.

## Recommendation for KB realism

Keep `generic_chemical_reactor_v0` as a temporary coarse placeholder, but make its limits explicit.

Recommended cleanup when KB edits are allowed:

- Annotate as "generic stirred/jacketed reactor placeholder" rather than a universal reactor.
- Prefer `chemical_reactor_basic` where the existing basic reactor BOM fits.
- Use or create specific reactor types only when required: acid-resistant reactor, pressure reactor, packed-bed catalyst reactor, high-temperature tube reactor, or gas absorption reactor.
- Audit high-pressure carbonyl, Sabatier/Bosch/RWGS, sulfuric/nitric acid, and hydrothermal/mineral reactions before assuming this one reactor is compatible.
- Consider consolidating with `chemical_reactor_basic` if both are serving the same coarse role.

## Confidence and open questions

Confidence: high that chemical reactors are real; medium-low that this specific generic item is realistic across all current process references.

Open questions:

- What pressure, temperature, corrosion, and catalyst requirements should define the first canonical reactor variants?
- Should `generic_chemical_reactor_v0` be deprecated after references are sorted into specific reactor classes?
- Does the 250 kg mass include heating/cooling jacket, agitator, seals, controls, relief valves, and corrosion lining?
