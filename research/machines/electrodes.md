# Electrodes

## Machine identity

- KB ID: `electrodes`
- KB name: Electrodes
- KB file: `kb/items/machines/electrodes.yaml`
- KB kind: `machine`
- Current KB mass: 15 kg
- Current KB structure: coarse BOM for graphite/carbon electrode stock, with recipe `recipe_electrodes_v0`.

## KB usage and needed function

The KB uses `electrodes` in two different ways:

- As an input item in multiple electrochemical extraction recipes and processes, including calcium, titanium, magnesium-silicon, ferrotitanium, and FFC/MRE-style processes.
- As a `machine_id` resource requirement in `kb/processes/oxygen_extraction_molten_regolith_electrolysis_v0.yaml`.

The intended physical function appears to be high-temperature conductive electrodes for molten regolith electrolysis or related electrochemical extraction. The item is not a standalone machine in ordinary engineering usage; it is a component, tooling set, or consumable part used by an electrolyzer/reactor.

## Reality classification

Classification: real practical item, but likely misclassified as a machine.

Carbon/graphite electrodes are real industrial items. High-temperature electrolysis and electric-arc furnace systems use electrodes as current-carrying components that can wear or be consumed. However, an electrode set by itself is not a machine. It should usually be modeled as a `part`, `tooling`, or consumable/replacement component attached to a reactor/electrolyzer machine.

The current `machine` kind likely exists because the self-reproduction imported-machine report filters only machine-kind entries. From a realism standpoint, `electrodes` should not stay in the imported machine list as though it were a capital machine.

## Evidence links

- NASA TechPort describes Molten Regolith Electrolysis as a technology for producing oxygen and metals from raw lunar or Martian regolith, supporting the context where high-temperature electrodes are required. Source: https://techport.nasa.gov/projects/116413
- MIT work on molten oxide electrolysis for lunar oxygen generation discusses inert anode materials for lunar regolith simulant electrolysis. Source: https://web.mit.edu/dsadoway/www/132.pdf
- Tokai Carbon describes graphite electrodes inside electric arc furnaces as conductive, heat-resistant components that carry large currents to melt iron. Source: https://www.tokaicarbon.co.jp/en/products/graphite/
- Weaver Industries describes custom graphite electrodes as components for high-temperature, high-performance environments and notes operational lifecycle/replacement. Sources: https://weaverind.com/electrodes-industries/ and https://weaverind.com/the-lifecycle-of-a-graphite-electrode-from-production-to-replacement/

## Commercial alternatives

Commercial alternatives include:

- Machined graphite electrode rods or blocks.
- Large electric-arc-furnace graphite electrodes.
- Custom graphite or carbon electrodes for high-temperature industrial processing.
- Refractory metal electrodes, such as tungsten, molybdenum, tantalum, or iridium-bearing anodes, where carbon contamination or oxygen evolution requires different chemistry.
- Application-specific electrode assemblies integrated into an electrolysis cell or MRE reactor.

For molten regolith electrolysis, the correct electrode material is a significant design question. Carbon/graphite is manufacturable and common, but it may be consumed or contaminate products. Inert anodes are chemically attractive but may require scarce or hard-to-manufacture materials.

## Build or open-source references

Electrode fabrication is practical as part fabrication, not machine construction:

- Graphite electrode blanks can be machined from graphite stock.
- The KB recipe `recipe_electrodes_v0` already models pressed/sintered carbon/graphite blanks, machining, and inspection.
- Informal electrolysis references often use graphite rods, but those are low-temperature/low-duty examples and should not be treated as validation for molten regolith service.

The difficult part is not whether electrodes can be made; it is choosing material, lifetime, geometry, and replacement schedule under molten oxide/regolith chemistry.

## Related machine research

Related KB entries include:

- `mre_reactor_v0`
- `electrolysis_cell_unit_v0`
- `electrode_set_mre`
- `refractory_metal_electrodes`
- `graphite_powder`
- `crucible_graphite`
- `high_temperature_power_supply_v0`

`electrodes` overlaps strongly with `electrode_set_mre`; future cleanup should decide whether `electrodes` is a generic graphite consumable set and `electrode_set_mre` is the application-specific assembly.

## Recommendation for KB realism

Do not keep `electrodes` as a machine long term.

Recommended future cleanup:

- Reclassify `electrodes` as a `part` or consumable tooling item, probably `graphite_electrode_set_v0`.
- Keep it as an input or BOM component for MRE/FFC/electrolysis equipment.
- Replace `machine_id: electrodes` resource requirements with the actual machine, such as `mre_reactor_v0` or `electrolysis_cell_unit_v0`, and list electrodes as inputs or consumable maintenance parts.
- Preserve separate material-specific electrode sets when chemistry matters: graphite/carbon, refractory metal, nickel/iron battery electrodes, copper welding electrodes, etc.

This is a real object, but its presence in an imported machine list is a schema/modeling artifact.

## Confidence and open questions

Confidence: high that electrodes are real and practical; high that they are misclassified as a machine; medium on the best replacement ID because the KB has several electrode concepts already.

Open questions:

- Are these intended to be consumable carbon electrodes, inert anodes, cathodes, or a mixed anode/cathode set?
- Which specific processes consume electrode mass versus only require installed electrode surfaces?
- Should `electrodes` be deprecated in favor of `electrode_set_mre` or retained as a generic graphite electrode set?
- What electrode lifetime should be assumed for molten regolith electrolysis at about 1600 C?
