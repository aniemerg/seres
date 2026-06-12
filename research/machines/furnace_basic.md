# Machine identity

- Queue item: `machine_reality_furnace_basic`
- KB item: `furnace_basic`
- KB name: Basic furnace
- KB file: `kb/items/machines/furnace_basic.yaml`
- Current KB kind: `machine`
- Current mass: 300 kg
- Current temperature range: 200-1200 C
- Current BOM: `bom_furnace_basic_v0`
- Current recipe: `recipe_furnace_basic_v0`

# KB usage and needed function

`furnace_basic` is used across many moderate-temperature process files, including generic heating, casting, alloying, stress relief, calcination, catalyst or packed-bed regeneration, thermal extraction, ceramic casting, and some lower-temperature metallurgy. Local dedupe documentation also chose it as the general 200-1200 C furnace and consolidated `casting_furnace_v0` and `sintering_furnace_v0` into it where no special requirements were specified.

The needed function is a refractory-lined electric resistance or fuel-fired chamber/crucible furnace with temperature control. The KB BOM includes an insulated shell, refractory lining, heating elements, temperature controller, door hinge assembly, and basic control circuit board. That is a plausible baseline for a box, muffle, or small crucible furnace.

# Reality classification

Real practical machine, but a generic category.

The KB item is realistic as a general-purpose shop/lab furnace up to roughly 1200 C. It should not be treated as a universal substitute for every furnace. Processes that require controlled atmosphere/vacuum, high temperature above 1200-1300 C, glass tank operation, carbothermal reduction/offgas handling, sintering cycle control, or foundry-scale pouring hardware should use more specific furnace items.

# Evidence links

- SentroTech sells 1200 C muffle furnaces for lab and small production applications with accurate temperature control, temperature uniformity, and programmable PID heating/dwell/cooling control: https://www.sentrotech.com/products/muffle-furnaces/1200c-muffle-furnace/
- Carbolite Gero describes standard laboratory or industrial box furnaces as usually reaching 1100-1300 C, with higher-temperature models for more demanding applications: https://www.carbolite.com/products/box-furnaces/
- Nabertherm sells chamber furnaces for annealing, hardening, and brazing up to 1280 C with multilayer insulation: https://nabertherm.com/en/products/labor/chamber-furnaces/chamber-furnaces-annealing-hardening-and-brazing-1280-degc
- Nabertherm describes radiant-heated industrial furnaces for steel annealing above 900 C, with arrangements intended for good temperature uniformity: https://nabertherm.com/en/processes/metallbearbeitung-prozesse-luft/hardening-annealing-850-degc
- LAC sells electric tilting melting furnaces up to 1200 C for pouring melt into ladles or holding furnaces: https://www.lac.cz/en/furnaces-and-dryers/pts-melting-electric-tilting-furnace
- CM Furnaces sells box furnaces used from laboratory to production settings for annealing, brazing, calcining, ceramics, firing, heat treating, sintering, melting, and thermal cycling, with programmable heating and cooling: https://cmfurnaces.com/box-furnaces/

# Commercial alternatives

Commercial alternatives include:

- Muffle or box furnace for lab/shop heating and heat treatment.
- Chamber furnace for annealing, hardening, brazing, and process heating.
- Small crucible furnace for aluminum, zinc, bronze, precious metals, and similar melts.
- Kiln for ceramics and refractory firing.
- Tilting crucible furnace for easier pouring.
- Controlled-atmosphere, vacuum, reduction, glass, or high-temperature furnace when a process has stricter requirements.

# Build or open-source references

A basic furnace is locally buildable compared with many precision machines. Core requirements are:

- insulated steel shell and door,
- refractory brick, ceramic fiber, or castable lining,
- heating elements or burner system,
- thermocouple or pyrometer,
- temperature controller, contactor/SSR, wiring, and power conditioning,
- safe door/lid hardware, interlocks, grounding, and over-temperature protection,
- crucible, hearth, tray, or work support appropriate to the process.

The KB BOM captures the major furnace subassemblies. For melting/casting use, the model should include crucibles, tongs/lifting/pouring tools, mold handling, spill containment, and PPE-adjacent support equipment. For heat treatment, a quench tank or controlled cooling station may be needed. For atmospheric chemistry or reduction, this item is not enough by itself.

# Related machine research

Related local reports:

- `casting_furnace_v0.md`
- `furnace_high_temp.md`
- `glass_furnace_v0.md`
- `heat_treatment_furnace_v0.md`
- `heating_furnace.md`
- `reduction_furnace_v0.md`
- `sintering_furnace_v0.md`
- `drying_oven.md`
- `induction_forge_v0.md`

Those reports generally support keeping `furnace_basic` as the moderate-temperature generic furnace while reserving specialized furnace items for process-specific constraints.

# Recommendation for KB realism

Keep `furnace_basic` as a real, useful, generic 200-1200 C furnace.

Recommended refinements:

- Define it as a "general-purpose refractory-lined box/crucible furnace" rather than a catch-all furnace.
- Use it for moderate-temperature heating, calcination, basic annealing/stress relief, ceramic firing within its range, and simple low-scale melting where atmosphere and pouring details are not critical.
- Do not use it for high-temperature processes above roughly 1200-1300 C; use `furnace_high_temp`.
- Do not use it for reduction chemistry with offgas/reductant control; use `reduction_furnace_v0`.
- Do not use it for controlled heat-treatment cycles where metallurgy is central; use `heat_treatment_furnace_v0`.
- Do not use it for glass melting/forming where refractory chemistry, fining, tank/crucible design, and forming access matter; use `glass_furnace_v0`.
- Keep `casting_furnace_v0` deprecated only if casting processes do not need tilting, pouring, or foundry-specific handling.

# Confidence and open questions

Confidence: high that the item is real and commercially common; high that the BOM is plausible for a compact general furnace; medium on process references because some current uses may need more specific furnace equipment.

Open questions:

- Should `furnace_basic` be split into box/muffle and crucible variants?
- Which current `furnace_basic` processes actually require controlled atmosphere, quench integration, or foundry pouring equipment?
- Should the imported machine list include both `furnace_basic` and `heating_furnace`, or should `heating_furnace` be consolidated unless it has a line/preheat role?
