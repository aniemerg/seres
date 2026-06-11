# Refractory Crucible Machine Reality Research

## Machine identity

- KB item id: `crucible_refractory`
- KB name: Refractory crucible
- KB file: `kb/items/machines/crucible_refractory.yaml`
- Current KB kind: `machine`
- Current KB mass: 15 kg
- Current BOM: `bom_crucible_refractory_v0`
- Current recipe: `recipe_crucible_refractory_v0`

## KB usage and needed function

The item is used by many high-temperature processes including basic melting, metal casting, iron smelting/reduction, silicon reduction/purification, stainless steel smelting, alloy remelting, brazing alloy synthesis, and solder paste casting.

The needed function is high-temperature containment of molten metal, glass, slag, or reactive melt inside a furnace or heating system. It does not provide heat, atmosphere control, stirring, pouring motion, or safe handling by itself. It should be paired with a furnace, tongs/handling tools, molds, protective equipment, and process-specific flux/atmosphere controls.

## Reality classification

Real practical consumable/tooling item, not a standalone machine.

Refractory crucibles are standard foundry and laboratory consumables. The KB's 15 kg mass is plausible for a moderate small foundry crucible, but not universal: lab alumina crucibles may weigh grams, while large foundry crucibles can be much heavier. The current temperature range is plausible for alumina, silicon carbide, clay-graphite, or similar refractory materials, but material compatibility is process-specific.

## Evidence links

- Foseco lists molten-metal crucibles in many shapes and sizes using materials such as silicon carbide and graphite, tailored to thermal and operational performance: <https://www.foseco.com/en/about-us/molten-metal-systems>
- Final Advanced Materials sells sintered alumina crucibles and states that sintered alumina can be used up to 1700 C for very high-temperature applications: <https://www.final-materials.com/gb/389-sintered-alumina-crucible>
- AEM Deposition describes refractory crucibles made from graphite, alumina, zirconia, tantalum, and other high-temperature materials: <https://www.aemdeposition.com/blog/what-are-refractory-crucibles.html>
- Morgan/Molten Metal Systems literature describes carbon-bonded silicon carbide crucibles for non-ferrous melting applications: <https://www.morganthermalceramics.com/media/kxuh2o0u/01-excel-himelt.pdf>

## Commercial alternatives

- Clay-graphite crucible for common nonferrous foundry work.
- Silicon carbide crucible for higher durability and thermal shock resistance in foundry service.
- High-purity alumina crucible for lab, ceramics, sapphire, and high-temperature oxide work.
- Graphite crucible for nonferrous metals, glass, and some reducing-atmosphere work.
- Zirconia or specialty ceramic crucible for aggressive melts or very high-temperature service.

## Build or open-source references

Local manufacture is plausible for coarse refractory crucibles if the KB has refractory raw materials, forming, drying, and kiln/furnace firing capability. The existing recipe's forming, slow drying, firing, and inspection steps are realistic at a coarse level.

However, reliable crucibles require material formulation, controlled drying, firing schedules, thermal shock resistance, porosity control, and compatibility with the melt. A generic locally made ceramic crucible should not silently cover all silicon, steel, glass, alkali, acid, and reducing-atmosphere processes.

## Related machine research

Related local reports:

- `research/machines/casting_furnace_v0.md`
- `research/machines/glass_furnace_v0.md`
- `research/machines/electrodes.md`

Related KB items include `crucible_graphite`, `crucible_ceramic_refractory`, `crucible_graphite_small`, `crucible_graphite_large`, and `crucible_set`.

## Recommendation for KB realism

Keep the item, but reclassify it conceptually as consumable refractory ware or tooling.

Recommended options:

- Avoid presenting `crucible_refractory` as a machine. It is a replaceable container used by furnaces and casting operations.
- Consolidate duplicate crucible names where possible under Conservative Mode. `crucible_refractory`, `crucible_ceramic_refractory`, and parts of `crucible_set` may overlap.
- Keep material-specific variants only when process compatibility matters: alumina/ceramic, clay-graphite, silicon carbide, graphite, or fused silica.
- Preserve `crucible_graphite` as a distinct item where reducing atmosphere, thermal shock, or carbon compatibility matters.
- Add process notes where a generic refractory crucible is probably insufficient, especially molten silicon, steelmaking, alkali melts, high-purity glass, and sapphire/Czochralski processes.

## Confidence and open questions

Confidence: high that refractory crucibles are real and necessary; high that the current item should not be treated as a standalone machine; medium on the 15 kg mass as a generic placeholder.

Open questions:

- Should the simulator support required consumables/tooling separately from `machine_id` resources?
- Which current processes need a graphite, alumina, silica, silicon-carbide, or clay-graphite crucible specifically?
- Should crucible lifetime and replacement rate be modeled for repeated high-temperature cycles?
