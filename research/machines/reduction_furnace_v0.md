# Reduction Furnace

## Machine identity

- KB ID: `reduction_furnace_v0`
- KB name: Reduction furnace
- KB file: `kb/items/machines/reduction_furnace_v0.yaml`
- Current KB type: `machine`
- Current KB mass: 1019.5 kg
- Current KB capabilities: `reduction_furnace`, `carbothermal_reduction`, `metal_oxide_reduction`, `high_temp_processing`
- Current KB description: high-temperature refractory-lined furnace for metal oxide reduction, with gas handling, offgas manifold, cooling loop, high-current power bus, heating elements, insulation, sensors, and control hardware.

## KB usage and needed function

The KB uses `reduction_furnace_v0` for several high-temperature chemical and metallurgical processes:

- `iron_reduction_from_ilmenite_v0`
- `magnesium_oxide_reduction_v0`
- `silicon_metal_reduction_from_purified_v0`
- `silicon_purification_mgsi_v0`
- `silicide_formation_basic_v0`
- `steel_refining_basic_v0`
- `stainless_refining_basic_v0`

It is also part of the minimal self-reproducing set and ISRU workflow documentation. The needed function is a controlled, refractory-lined, high-temperature reaction environment for reducing metal oxides or related feedstocks under carbon monoxide, hydrogen, vacuum, inert gas, or other controlled atmospheres, with offgas handling and temperature control.

The BOM shape is credible for a compact process furnace: refractory shell, high-temperature heating, insulation, gas handling, offgas manifold, cooling, power, thermocouple/control, and general sensors. The broad capability list covers several real furnace families, not one exact commercial SKU.

## Reality classification

Classification: real practical machine category, but broad.

Reduction furnaces are real equipment in powder metallurgy, refractory metal production, direct reduced iron production, hydrogen reduction, and lunar-regolith oxygen work. Industrial implementations vary substantially: shaft furnaces, rotary kilns, tube furnaces, pusher furnaces, batch box furnaces, solar carbothermal reactors, and electric arc or plasma variants can all support reduction chemistry.

The KB's 1019.5 kg mass is plausible for a pilot-scale or small industrial furnace with gas handling and refractory mass. It is too small for a commercial direct reduced iron shaft furnace, but reasonable for a compact ISRU/pilot metallurgical furnace or batch furnace.

## Evidence links

- Kleenair Products sells custom tungsten and molybdenum reduction furnaces with temperature, time, and atmosphere control for reduction processes. Source: https://www.kleenairusa.com/industrial-furnaces-ovens/tungsten-molybdenum-reduction
- International Iron Metallics Association describes direct reduction of iron ore using gas-based shaft furnaces, gas-based fluidized beds, and coal-based rotary kiln furnaces. Source: https://www.metallics.org/about-metallics/dri-production/
- Ants Global describes high-temperature hydrogen reduction tube furnaces for reduction, sintering, debinding, annealing, and thermal treatment in reducing atmospheres up to 1600 C. Source: https://antsglobal.in/tube-furnaces-standard-specialised/hydrogen-reduction-tube-furnace/
- Carbolite Gero describes modified-atmosphere laboratory and industrial furnaces using inert, reducing, or oxidizing gases to prevent oxidation or promote reactions. Source: https://www.carbolite.com/products/modified-atmosphere/introduction/
- NASA reports carbothermal oxygen extraction from lunar soil simulant and notes that a lunar carbothermal reactor must retain gases while allowing regolith to move through the reaction zone. Source: https://www.nasa.gov/centers-and-facilities/johnson/nasa-successfully-extracts-oxygen-from-lunar-soil-simulant/
- A NASA/AIP paper on lunar carbothermal reduction describes use of high temperatures, around 1625 C, to reduce ilmenite and silicates in lunar regolith using a carbonaceous source. Source: https://pubs.aip.org/aip/acp/article-pdf/746/1/1224/12174175/1224_1_online.pdf

## Commercial alternatives

- Hydrogen reduction tube furnace for lab or pilot oxide reduction.
- Batch or pusher reduction furnace for tungsten, molybdenum, copper, nickel, and powder metallurgy feedstocks.
- Rotary kiln for solid carbon or mixed feed reduction.
- Shaft furnace for large-scale direct reduced iron.
- Vacuum/inert atmosphere furnace where reduction is paired with sintering or purification.
- Solar carbothermal reactor for lunar ISRU concepts.

The current KB item is closest to a compact controlled-atmosphere reduction furnace rather than a large DRI shaft furnace.

## Build or open-source references

Open-source complete reduction-furnace builds are uncommon because the system combines high temperature, reducing gases, pressure/offgas handling, electrical power, and safety interlocks.

Buildable subassemblies and principles are well established:

- Refractory-lined furnace shell or tube furnace hot zone.
- Electric resistance, induction, arc, plasma, or concentrated solar heat input.
- Controlled reducing-gas loop using hydrogen, carbon monoxide, methane, cracked ammonia, or inert sweep gases depending on chemistry.
- Offgas manifold, condensate/particulate handling, check valves, purge logic, pressure relief, and gas monitoring.
- Thermocouples, controllers, interlocks, and data logging.

For KB realism, local manufacture of a small furnace body and insulation is plausible, but imported or high-grade components may be needed for heating elements, gas-tight seals, sensors, safety-rated valves, and control hardware.

## Related machine research

Related reports already present:

- `furnace_high_temp.md`
- `glass_furnace_v0.md`
- `heating_furnace.md`
- `casting_furnace_v0.md`
- `mre_reactor_v0.md`
- `high_temperature_power_supply_v0.md`
- `power_conditioning_equipment.md`
- `heliostat_array_system_v0.md`

The closest overlap is `furnace_high_temp`, which is a general high-temperature heat source. `reduction_furnace_v0` should remain separate if it specifically includes controlled atmosphere, reductant delivery, offgas handling, and reaction-product management.

## Recommendation for KB realism

Keep `reduction_furnace_v0` as a real machine category, but narrow the description to "compact controlled-atmosphere reduction furnace" or "pilot-scale metal oxide reduction furnace."

Do not treat one generic reduction furnace as fully interchangeable across every reduction route. Future KB work should distinguish at least:

- Batch/tube controlled-atmosphere oxide reduction furnace.
- Rotary kiln or continuous reactor for granular ore/regolith.
- Shaft furnace for direct reduced iron scale.
- Solar carbothermal regolith reactor if solar flux is part of the process.

For the current imported-machine list, the item is realistic enough to keep as a self-reproduction seed machine. Its BOM is directionally credible because it includes refractory mass, heating, gas handling, offgas handling, cooling, power, sensing, and controls.

## Confidence and open questions

Confidence: high that reduction furnaces are real and relevant; medium that the KB item's broad capabilities can be represented by one compact machine.

Open questions:

- Which reduction chemistry is primary for the self-reproducing set: hydrogen, carbon monoxide, methane/carbothermal, direct carbon, or vacuum/silicon refining?
- Is the furnace batch, tube, rotary, shaft, or solar-driven?
- Does the system need pressure-rated operation, sealed feedthroughs, and gas recycling modeled as separate subsystems?
- Should high-wear refractory liners and heating elements be maintenance consumables?
