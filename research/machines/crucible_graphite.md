# Machine identity

- Queue item: `machine_reality_crucible_graphite`
- KB item: `crucible_graphite`
- KB name: Graphite crucible
- KB file: `kb/items/parts/crucible_graphite.yaml`
- Current KB kind: `machine`
- Current mass: 10 kg
- Current BOM: `bom_crucible_graphite_v0`
- Current recipe: `recipe_crucible_graphite_v0`

# KB usage and needed function

`crucible_graphite` is used in high-temperature glass and metal processes including `glass_envelope_forming_v0`, `glass_casting_v0`, `glass_casting_process_v0`, `fused_silica_production_v0`, and `nickel_extraction_meteorite_v0`. It is also listed in the minimal/self-reproducing set as high-temperature containment.

The needed function is passive containment of molten material in a furnace or heating process. It is not a machine by itself. It is a reusable but finite-life crucible/tooling component whose suitability depends strongly on melt chemistry, temperature, atmosphere, oxidation risk, and contamination tolerance.

# Reality classification

Real practical crucible/tooling component, not a machine.

Graphite crucibles are standard foundry and laboratory consumables. The KB's 10 kg mass is plausible for a small-to-moderate crucible, but crucibles vary from gram-scale lab cups to heavy foundry vessels. The item should stay distinct from generic refractory/alumina crucibles where graphite's thermal shock resistance, thermal conductivity, reducing behavior, electrical conductivity, or carbon contamination risk matters.

# Evidence links

- Foseco/Molten Metal Systems lists crucibles in many shapes and sizes using silicon carbide and graphite, tailored for thermal and operational performance: https://www.foseco.com/en/about-us/molten-metal-systems
- Morgan/Thermal Ceramics literature describes carbon-bonded silicon carbide crucibles for non-ferrous melting applications, showing commercial carbon/graphite-related crucible families: https://www.morganthermalceramics.com/media/kxuh2o0u/01-excel-himelt.pdf
- IQS Directory describes graphite crucibles as high-temperature crucibles for precious and industrial metal processing in vacuum and atmospheric conditions: https://www.iqsdirectory.com/articles/graphite-machining/graphite-crucible.html
- AEM Deposition describes graphite crucibles as lightweight, thermal-shock-resistant crucibles that can handle very high temperatures and are used for metal casting, gold refining, and aluminum melting: https://www.aemdeposition.com/blog/what-are-refractory-crucibles.html
- CDOCAST notes a key limitation: graphite oxidizes rapidly at high temperature in oxidizing atmospheres, while inert gas or vacuum greatly extends high-temperature service: https://www.cdocast.com/graphite-crucible/
- ORNL crucible handbook notes graphite can be stable at high temperatures and electrically conductive, but also notes short life in some high-temperature use and tendencies to reduce oxides or form carbides: https://www.osti.gov/servlets/purl/4389738

# Commercial alternatives

Commercial alternatives include:

- Pure graphite crucible for nonferrous melting, precious metals, some glass/material processing, induction susceptor use, or reducing/inert atmospheres.
- Clay-graphite crucible for common foundry melting.
- Carbon-bonded silicon carbide crucible for nonferrous foundry service and improved oxidation/thermal-shock behavior.
- Alumina, zirconia, fused silica, or other ceramic crucibles for oxide/glass/high-purity work where carbon contamination is unacceptable.
- Platinum, molybdenum, tungsten, or specialty crucibles for specialized laboratory and crystal-growth processes.

# Build or open-source references

The KB recipe forms graphite powder into a crucible, sinters/bakes it, and machines the interior/rim. That is a plausible high-level route, but industrial graphite crucibles usually depend on controlled raw material particle sizes, binders/pitches, pressing/isostatic forming, baking, graphitization or high-temperature treatment, impregnation/coatings where needed, machining, and quality inspection.

Local manufacture may be plausible only after the KB has a reliable graphite powder/carbon processing route and high-temperature furnace capability. Early bootstrap scenarios should import graphite crucibles or use locally fired refractory crucibles where chemistry permits.

# Related machine research

Related local reports:

- `crucible_refractory.md`
- `casting_furnace_v0.md`
- `glass_furnace_v0.md`
- `furnace_high_temp.md`
- `reduction_furnace_v0.md`
- `sintering_furnace_v0.md`
- `electrodes.md`

The existing `crucible_refractory.md` report already recommends preserving `crucible_graphite` where graphite-specific properties matter.

# Recommendation for KB realism

Keep `crucible_graphite`, but treat it as a crucible/tooling/consumable component.

Recommended cleanup:

- Reclassify from `kind: machine` to part/tooling/consumable if schema allows.
- Preserve distinction from `crucible_refractory` and `crucible_ceramic_refractory`; graphite is not universally interchangeable with alumina, clay, silicon carbide, or fused silica.
- Add atmosphere notes: graphite service near high temperatures is much more realistic in inert, vacuum, or reducing environments than in oxidizing air.
- Add contamination notes where needed: graphite can reduce oxides, add carbon, or form carbides; it may be inappropriate for some glass, oxide ceramic, silicon, and high-purity processes.
- Consolidate duplicate names such as `graphite_crucible_v0`, `crucible_graphite_small`, and `crucible_graphite_large` only if size/capability differences are within the project's conservative 5x rule or can be represented as variants.

# Confidence and open questions

Confidence: high that graphite crucibles are real and useful; high that the KB should not treat them as machines; medium on the 10 kg mass because size and capacity are unspecified.

Open questions:

- Which processes require graphite specifically rather than generic refractory containment?
- Should crucible lifetime/replacement rate be modeled for repeated high-temperature cycles?
- Is graphite compatible with the KB's glass/fused silica processes, or should those prefer silica/alumina/zirconia crucibles?
