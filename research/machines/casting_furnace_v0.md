# Casting furnace v0

## Machine identity

- Queue item: `machine_reality_casting_furnace_v0`
- KB ID: `casting_furnace_v0`
- KB file: `kb/items/machines/casting_furnace_v0.yaml`
- KB name: Casting furnace v0
- KB kind: `machine`
- KB modeled mass: 900 kg

The KB item is already marked deprecated: its notes say it was consolidated into `furnace_basic`. It is described as a furnace for melting alloy prior to casting, with melting and heat-treatment capabilities. The BOM includes a furnace shell, burner or heater, high-temperature insulation, power conditioning, pyrometer, temperature controller, sensors, imported control module, cooling loop, and fasteners.

## KB usage and needed function

Despite the deprecation note, `casting_furnace_v0` is still referenced by many processes, including:

- `metal_ingot_cast_v0`
- `metal_casting_basic_v0` indirectly notes use of `furnace_basic` to avoid deprecated `casting_furnace_v0`
- `sand_casting_medium_v0` and `sand_casting_large_v0`
- `melting_basic_v0`
- `steel_ingot_cast_v0`
- `stainless_steel_smelting_v0`
- `steel_refining_basic_v0`
- `stainless_refining_basic_v0`
- `bronze_alloy_casting_v0`
- `magnalium_alloying_v0`
- `copper_rod_ingot_cast_v0`
- `lathe_headstock_blank_cast_v0`

The needed function is melting and holding metal charge before pouring into molds or ingot molds. In some references it is also used for alloying, refining, slag removal, and temperature control.

## Reality classification

Classification: real practical machine family, but the current KB ID should remain deprecated/consolidated.

Metal casting furnaces are real and standard foundry equipment. However, "casting furnace" is broad: crucible furnaces, induction furnaces, reverberatory furnaces, cupolas, electric arc furnaces, and holding furnaces differ substantially. The KB's 900 kg mass is plausible for a small foundry crucible/tilting furnace or compact induction unit, but not for a large cupola, large induction furnace, or steelmaking electric arc furnace.

The KB's own dedupe documentation says `casting_furnace_v0` should use `furnace_basic`. That means this imported-machine-list item is real in the world but likely should not remain a separate active KB machine unless a future model needs a specific foundry furnace subtype.

## Evidence links

- Modern Casting, "Choosing the Right Furnace for Your Operation": https://www.moderncasting.com/articles/2021/09/08/choosing-right-furnace-your-operation
  - Describes foundry furnaces as melting or holding furnaces heated by fossil fuels or electricity.
  - Lists basic furnace groups such as crucible, reverberatory, stack melter, dosing, and rotary furnaces.

- Ajax TOCCO coreless induction melting furnaces: https://www.ajaxtocco.com/products/coreless-melting-furnaces
  - Commercial induction furnace example with refractory-lined insulated copper coil, steel shell, power/electromagnetic structures, and support elements.
  - Lists designs including steel shell, steel frame, box, hand/tabletop, rollover, lab, and high power density furnaces.

- MIFCO gas-fired melting furnaces: https://mifco.com/foundry-furnaces/high-speed-melters/
  - Commercial gas-fired foundry melting furnaces for aluminum, brass, bronze, and some grey iron.
  - Describes welded steel construction, refractory linings, temperature range, capacities, burner safety components, and foundry accessories such as pyrometers, crucibles, tongs, ladles, skimmers, and flasks.

- SentroTech, "The 5 Types of Foundry Furnaces": https://www.sentrotech.com/types-of-foundry-furnaces/
  - Describes cupola, electric arc, induction, crucible, and blast furnaces.
  - Notes crucible furnaces can be small/tabletop to industrial-scale, and are used to melt/cast metals such as brass, bronze, and aluminum.

## Commercial alternatives

- Generic `furnace_basic` in the KB: likely the preferred consolidated model for small melting/heat-treatment capacity.
- Gas-fired crucible furnace: low-cost, practical for aluminum, brass, bronze, and small iron melts depending on design.
- Electric resistance crucible furnace: useful for nonferrous metals and smaller clean operations.
- Induction melting furnace: cleaner, faster, more controllable, often used for ferrous/nonferrous foundry melting.
- Holding furnace: separate from melting if the process needs stable molten metal temperature before casting.
- Cupola or electric arc furnace: real, but too specific and large for the current 900 kg generic item unless explicitly modeled.

## Build or open-source references

Small foundry furnaces are commonly built by hobbyists and small shops from refractory linings, steel shells, burners or electric heating, crucibles, lids, tongs, and pyrometers. That said, high-temperature operation, refractory failure, fuel-gas safety, molten metal handling, and ventilation are serious safety constraints.

No formal open-source industrial foundry-furnace package was needed to establish reality; the commercial sources are enough. For KB purposes, local build should be modeled as high-temperature furnace fabrication plus foundry accessories, not as a generic assembly-only task.

## Related machine research

Existing related research found:

- `research/machines/glass_furnace_v0.md`
- `research/machines/sand_casting_flask_set.md`

Related KB entries include `furnace_basic`, `blast_furnace_or_smelter`, `crucible_refractory`, `casting_mold_set`, `sand_casting_flask_set`, and `quench_tank`.

## Recommendation for KB realism

Recommendation: real machine category, but replace or keep deprecated in favor of `furnace_basic`.

Specific recommendation:

- Do not treat `casting_furnace_v0` as a fake or placeholder.
- Do treat it as over-specific or duplicate if `furnace_basic` is intended to absorb generic small furnace functions.
- Imported-machine-list cleanup should probably remove `casting_furnace_v0` as an active required import and list `furnace_basic` or a clearly named subtype instead.
- If the KB later needs more realism, split by process need rather than by old generic name: `small_crucible_furnace`, `induction_melting_furnace`, `holding_furnace`, or `cupola_furnace`.
- Existing references to `casting_furnace_v0` should eventually be migrated to `furnace_basic` or a specific furnace subtype, consistent with `docs/dedupe_decisions.md`.

## Confidence and open questions

Confidence: high that casting furnaces are real; high that this specific KB item is deprecated/duplicative based on local docs.

Open questions:

- Is `furnace_basic` already capable of all current casting-furnace references, including steel/stainless smelting and refining, or does steelmaking need a more specific high-temperature furnace?
- Should heat treatment remain a capability on a casting furnace, or should heat-treatment furnaces be separate from melting furnaces?
- Which current references require controlled atmosphere, induction stirring, slag/refining practice, or only simple crucible melting?

