# Chemical separation equipment

## Machine identity

- KB ID: `chemical_separation_equipment`
- KB file: `kb/items/machines/chemical_separation_equipment.yaml`
- KB name: Chemical separation equipment
- KB mass: 402 kg per unit
- Current KB role: modular chemical/hydrometallurgy separation skid for leaching, precipitation, solvent extraction, chloride recycling, and metal refining steps.

## KB usage and needed function

Local usage shows this item is a broad process-equipment bundle:

- It is listed in the minimal/self-reproducing machine set.
- It is required by `chloride_recycling_to_hcl_v0`, `nickel_extraction_meteorite_v0`, `cobalt_sulfate_extraction_v0`, and `ree_extraction_kreep_v0`.
- The item notes describe a modular chemical separation skid for leaching, precipitation, and solvent extraction, with corrosion-resistant tankage, agitation, filters, pump, heat tracing, and instrumentation.
- The BOM includes `chemical_bath_tank_set`, `agitation_pump_small`, `piping_and_valves_set`, `heating_element_set_basic`, temperature control, control board, level sensor, and a medium frame.

The needed function is not one exact machine. It is a small chemical-process skid supporting wet chemistry: leach tanks, pumps, filtration/solid-liquid separation, precipitation vessels, controls, and possibly mixer-settler solvent extraction modules.

## Reality classification

Classification: real practical equipment category / modular skid, not a single specific machine.

The KB item is realistic if interpreted as a small modular hydrometallurgy process skid. It is too broad if interpreted as one universal separator that can perform all chemical separations. The existing BOM is consistent with an early, coarse model for a flexible lab/pilot-scale chemical separation module.

## Evidence links

- SX Kinetics designs and manufactures hydrometallurgical pilot plant equipment including solvent extraction circuits and leach tanks: https://www.sxkinetics.com/hydrometplants.htm
- IAEA guidebook discusses acid leach, CCD, and solvent extraction pilot plant equipment for uranium ore processing: https://www-pub.iaea.org/MTCD/Publications/PDF/trs314_web.pdf
- An MDPI Minerals paper on demonstration plant scale-up describes leaching, filtering, leachate handling, and mixer-settler solvent extraction equipment: https://www.mdpi.com/2075-163X/5/2/298
- OSTI report on pilot-scale leaching and solvent extraction for rare earth recovery discusses process control, instrumentation, and pilot plant equipment: https://www.osti.gov/biblio/1984667
- Sulzer describes skid-mounted process plants as preassembled modular units integrating process equipment, pumps, separators, heat exchangers, and instrumentation: https://solutions.sulzer.com/post/rapid-reliable-modular-why-skid-mounted-plants-are-the-future-of-the-process-industry
- Mott filtration skids show the commercial pattern of integrating filters with piping, valves, instrumentation, controls, and programming: https://www.mottcorp.com/product/process-filters-skids-elements/filtration-skids/

## Commercial alternatives

Commercial alternatives depend on the exact chemistry:

- Hydrometallurgical pilot plants with leach tanks, pumps, mixer-settlers, filters, precipitation tanks, and electrowinning cells.
- Modular process skids for dosing, blending, heating, liquid handling, filtration, extraction, and reaction.
- Mixer-settler trains or extraction columns for solvent extraction.
- Filter press or membrane filtration skids for solid/liquid separation.
- Dedicated precipitation, crystallization, or ion-exchange skids.

For the KB's current resolution, a modular skid is acceptable. For later high-fidelity models, split by operation: leach tank, filter/clarifier, solvent extraction mixer-settler, precipitation reactor, electrowinning cell, and acid recycling unit.

## Build or open-source references

Open-source, safety-qualified build references are limited because chemical separation skids handle corrosive, toxic, flammable, or reactive fluids. Useful build analogs are engineering references and pilot-plant descriptions rather than hobby plans:

- Pilot plant publications show typical equipment trains and controls.
- Modular skid vendors show practical layout: tankage, pumps, piping, valves, sensors, controls, frame/skid, and containment.
- Small laboratory setups can be assembled from corrosion-compatible tanks, peristaltic/diaphragm pumps, filters, heaters, pH/temperature/level sensors, and secondary containment, but process-specific safety engineering is required.

## Related machine research

Related KB items:

- `chemical_bath_station`
- `chemical_reactor_basic`
- `chemical_reactor_vessel_v0`
- `generic_chemical_reactor_v0`
- `agitation_pump_small`
- `chemical_bath_tank_set`
- `piping_and_valves_set`

No follow-up tasks were enqueued, per task constraint.

## Recommendation for KB realism

Keep the item only as an explicitly generic modular chemical separation skid.

Recommended cleanup when KB edits are allowed:

- Rename display name to "Modular hydrometallurgy separation skid" or "Chemical separation skid" to make the bundle nature explicit.
- Add notes that this is a coarse placeholder for a process train, not one universal machine.
- Keep current BOM categories as a first-order skid model.
- Split into specific machines only when a process requires materially different equipment: solvent extraction mixer-settlers, filter presses, precipitation tanks, ion exchange columns, or electrowinning cells.
- Review processes that use this item twice, such as `ree_extraction_kreep_v0`, to determine whether the duplicate resource requirement means two modules, two stages, or an accidental duplicate.

## Confidence and open questions

Confidence: medium-high. The equipment class is real, but the KB ID is broad.

Open questions:

- Which exact separation methods are required for nickel/cobalt/REE workflows: acid leach plus precipitation, solvent extraction, ion exchange, electrowinning, or several of these?
- Does the 402 kg mass represent one skid, a train of small modules, or a compact laboratory/pilot plant?
- What corrosion-resistant materials are assumed for acids, chlorides, organic solvents, and elevated temperatures?
