# TIG welding unit v0

## Machine identity

- KB ID: `welding_tig_unit_v0`
- KB name: TIG welding unit v0
- KB file: `kb/items/machines/welding_tig_unit_v0.yaml`
- KB kind: `machine`
- Current KB mass: 169.9 kg
- Current KB structure: TIG torch assembly, welding power supply, shielding gas cylinder/regulator/controller, gas manifolds, coolant loop, coolant pump, and control panel.

## KB usage and needed function

The KB uses `welding_tig_unit_v0` for precision TIG/GTAW joining:

- `kb/processes/welding_tig_basic_v0.yaml` is a template process for precision joining, stainless/aluminum welding, high-quality welds, and leak-tight pressure-vessel or cryogenic equipment joints.
- `kb/processes/welding_process_tig_v0.yaml` joins bent pipe sections and machined valve bodies into a `piping_and_valves_set`.
- Multiple recipes reference TIG welding for pipe assemblies, coolant jackets, storage tanks, heat exchangers, and sealed components.

The required function is a controlled arc welding system with inert shielding gas and suitable torch/power controls for clean, leak-tight welds. That is exactly what TIG/GTAW equipment provides.

## Reality classification

Classification: real practical machine.

`welding_tig_unit_v0` represents a real machine category: a TIG/GTAW welding system. The `_v0` suffix and placeholder note indicate that the KB is not modeling a specific commercial model, but the physical equipment class is standard and practical.

The 169.9 kg mass is plausible for a complete stationary or cart-mounted TIG setup including power source, gas cylinder, cooler, pump, torch, and controls. It is high for a small portable inverter alone, but reasonable for a complete integrated welding station.

## Evidence links

- Miller lists commercial TIG/GTAW welding machines for aluminum, stainless steel, mild steel, and specialty metals, including Syncrowave, Dynasty, and Maxstar product families. Source: https://www.millerwelds.com/equipment/welders/tig-gtaw
- Lincoln Electric lists TIG welding equipment for GTAW, including AC/DC TIG welding on aluminum and other metals. Source: https://www.lincolnelectric.com/en/Products/Equipment/Welding-Equipment/TIG-Welding-Equipment
- Standard GTAW descriptions identify required equipment as a non-consumable tungsten-electrode torch, constant-current welding power supply, and inert shielding gas source. Source: https://en.wikipedia.org/wiki/Gas_tungsten_arc_welding
- Welding Tips and Tricks describes a scratch-start TIG setup from a DC power source, ground clamp, air-cooled TIG torch, flowmeter, and argon, supporting the minimal-build end of the category. Source: https://www.weldingtipsandtricks.com/homemade-tig-welder.html

## Commercial alternatives

Commercial alternatives include:

- Portable DC TIG/stick inverter for steel and stainless work.
- AC/DC TIG welder for aluminum plus steel/stainless.
- Water-cooled TIG station for higher-current or high-duty-cycle welding.
- Automated orbital TIG welding equipment for repeatable pipe/tube welding.
- General multi-process welder if TIG is only occasional and precision requirements are modest.

For the KB's leak-tight pipe, tank, and cryogenic-service joints, TIG/GTAW is a credible process choice. If throughput rather than weld cleanliness becomes the goal, MIG/GMAW or automated welding variants may be more appropriate.

## Build or open-source references

Open build references exist for simple TIG capability:

- Instructables has a scratch-start TIG welder build: https://www.instructables.com/How-to-Make-a-TIG-Welder-Scratch-Start/
- Welding Tips and Tricks documents converting a DC power source into a basic scratch-start TIG setup using torch, flowmeter, and argon: https://www.weldingtipsandtricks.com/homemade-tig-welder.html

These references support the possibility of locally assembling a simple TIG unit from a welding power source and gas/torch hardware. They do not replace the need for high-quality power electronics, gas regulators, safety controls, and coolant management in a more capable KB machine.

## Related machine research

Related KB machines and queue items likely include:

- `welding_power_supply_v0`
- `welding_tools_set`
- `welding_consumables`
- `welding_arc_welder_v0`
- `welding_spot_welder_v0`
- `power_supply_benchtop`
- `test_bench_electrical`

`welding_tig_unit_v0` should stay separate from generic welding tools and welding consumables because it provides a specific GTAW process capability. It may share components with general arc welding power supplies.

## Recommendation for KB realism

Keep the item.

Recommended clarification: describe it as a complete TIG/GTAW welding station rather than only a "unit." The current BOM is realistic at the functional level, but it mixes gas cylinder inventory, manifolds, cooling, power electronics, and controls into one machine. That is acceptable for the current conservative KB model.

Future cleanup should decide whether shielding gas cylinders are consumable/import materials or reusable equipment. For lunar or closed-loop environments, argon supply and recovery may become the limiting realism issue, not the welder hardware.

## Confidence and open questions

Confidence: high that the machine is real and practical; high that it matches the KB's current welding processes.

Open questions:

- Is the KB assuming argon, helium, nitrogen, or another shielding gas for each material? TIG commonly uses argon or helium, while nitrogen is not a universal substitute.
- Should `welding_tig_unit_v0` include an explicit water cooler only for high-duty-cycle operation, or be split into air-cooled and water-cooled variants?
- Are tungsten electrodes, filler rods, cups, collets, and shielding gas modeled as consumables elsewhere, or hidden inside `welding_consumables`?
