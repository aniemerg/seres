# Furnace High Temp

## Machine identity

- KB ID: `furnace_high_temp`
- KB name: High temperature furnace
- KB file: `kb/items/machines/furnace_high_temp.yaml`
- Current KB type: `machine`
- Current KB mass: 800 kg
- Current KB description: 1600-3000 C high-temperature furnace for carbothermal reduction, sintering, and materials processing, with refractory-lined chamber and resistance heating or solar concentration.

## KB usage and needed function

The KB uses this item across many high-temperature processes, including carbothermal reduction, thermite reduction, graphitization, high-temperature ceramic firing, fused silica/glass work, calcium/barium oxide extraction, glass/fiber processing, nickel extraction, and regolith volatile extraction.

Local dedupe notes already preserve `furnace_high_temp` as a distinct ultra-high-temperature furnace and consolidate `high_temp_furnace_v0` into it. The same notes keep heat-treatment furnaces separate because controlled metal heat treatment at around 1000 C is a different duty from 1600-3000 C specialized chemistry.

## Reality classification

Classification: real practical machine category.

High-temperature furnaces are real industrial and laboratory equipment. Furnaces up to 1600-1800 C are common for ceramics, sintering, calcination, and materials research. Furnaces approaching 2500-3000 C are more specialized graphite, vacuum, inert-gas, hydrogen, or tungsten/molybdenum hot-zone furnaces used for graphitization, refractory-metal sintering, and advanced materials processing.

The KB item is realistic as a broad high-temperature furnace family, but the 1600-3000 C span covers more than one practical design class. A 1600 C SiC/MoSi2 furnace and a 3000 C graphite/vacuum furnace should eventually be distinguished if process fidelity matters.

## Evidence links

- Nabertherm, high-temperature furnaces with SiC rod heating: laboratory muffle furnaces up to 1550-1600 C for high-temperature lab use. Source: https://nabertherm.com/en/products/labor/high-temperature/high-temperature-furnaces-sic-rod-heating-1600-degc
- Nabertherm, high-temperature furnaces up to 1800 C: compact stand-alone laboratory furnaces for precise high-temperature processes. Source: https://nabertherm.com/en/products/laboratory/high-temperature
- Sentro Tech, sintering furnaces: vacuum and controlled-atmosphere sintering furnaces up to 1600-1700 C for 3D metal printing, labs, and production. Source: https://www.sentrotech.com/products/sintering-furnaces/
- Carbolite, graphitization furnaces: graphite furnaces up to 3000 C for temperature-intensive graphitization and high-temperature treatment of carbon materials. Source: https://www.carbolite.com/products/graphitization-furnace/
- Thermal Technology, vacuum furnaces: lists vacuum furnaces including hydrogen furnaces for tungsten 3000 C sintering and heat treating. Source: https://www.thermaltechnology.com/products/vacuum-furnaces/
- Across International, vacuum tungsten sintering furnace: describes furnaces for high-melting-point materials requiring oxygen-free heat treatment, including tungsten, molybdenum, tantalum, ceramics, graphite, and composites. Source: https://www.acrossinternational.com/vacuum-tungsten-sinteringfurnace.html

## Commercial alternatives

- 1600-1800 C muffle or chamber furnaces using SiC or MoSi2 heating elements.
- Vacuum or controlled-atmosphere sintering furnaces for powder metallurgy and ceramics.
- Graphite hot-zone furnaces for graphitization and ultra-high-temperature processing up to 3000 C.
- Hydrogen/inert atmosphere furnaces for refractory metals and oxygen-sensitive materials.
- Solar concentrator or solar furnace systems for high-temperature thermal processing where sunlight and optical concentration are available.

## Build or open-source references

Simple kilns and lower-temperature furnaces can be built locally, but 1600-3000 C furnaces are much harder. Local construction needs refractory insulation, high-temperature heating elements or graphite/tungsten hot zones, power control, temperature measurement, chamber seals, gas/vacuum handling, cooling, and safety interlocks.

The KB can plausibly model local fabrication of the shell, refractory lining, insulation, and controls. The most difficult imported or high-skill components are ultra-high-temperature heating elements, vacuum/hydrogen-compatible hot-zone materials, pyrometry, seals, and power electronics.

No single open-source design suitable for the full 1600-3000 C range was identified in this pass.

## Related machine research

Related KB items:

- `furnace_basic`
- `heat_treatment_furnace_v0`
- `high_temp_furnace_v0` is deprecated/consolidated into `furnace_high_temp`
- `vacuum_furnace_v0`
- `sintering_furnace_v0`
- `induction_furnace_v0`
- `solar_concentrator_fresnel`
- `mre_reactor_v0`

`furnace_high_temp` should remain distinct from `furnace_basic` and `drying_oven`. It may overlap with `vacuum_furnace_v0` or specialized sintering furnaces only when the process needs controlled atmosphere or vacuum.

## Recommendation for KB realism

Keep as a real, important machine category.

Recommended future refinement:

- Clarify whether this represents a 1600-1800 C high-temperature furnace or a 2500-3000 C graphite/vacuum furnace.
- Use `furnace_basic` for general heating/melting up to around 1200 C.
- Use `heat_treatment_furnace_v0` for controlled metal heat-treatment cycles.
- Use `vacuum_furnace_v0` or a future `graphite_ultra_high_temp_furnace` for oxygen-free 2500-3000 C refractory-metal and graphitization work.

Do not replace this with labor bot plus tools. High-temperature containment, heating, atmosphere control, and safety are core machine capabilities.

## Confidence and open questions

Confidence: high that the machine category is real and necessary; medium that one 800 kg generic item should cover every 1600-3000 C use case.

Open questions:

- Which processes truly require 2500-3000 C rather than 1600-1800 C?
- Should tungsten sintering and graphitization require vacuum/inert/hydrogen atmosphere explicitly?
- Should solar concentration be a separate heat source feeding a furnace/receiver rather than part of the furnace item?
- Are current recipes incorrectly using `furnace_high_temp` where `drying_oven` or `furnace_basic` would be more realistic?
