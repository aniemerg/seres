# Power distribution bus

## Machine identity

- Queue item: `machine_reality_power_distribution_bus`
- KB ID: `power_distribution_bus`
- KB file: `kb/items/machines/power_distribution_bus.yaml`
- KB name: Power Distribution Bus
- KB kind: `machine`
- KB modeled mass: 200 kg

The KB defines this as an electrical bus bar system for distributing power to multiple loads. Its BOM includes copper bus bars, ceramic insulators, steel mounting brackets, and power output terminals. The recipe adds steel enclosure material, electrical wire/connectors, and fasteners.

## KB usage and needed function

`power_distribution_bus` is listed in the minimal/self-reproducing set and is referenced by `chloralkali_electrolysis_v0`.

The needed function is safe high-current electrical distribution from power sources or conditioning equipment to multiple loads, likely including electrolysis cells and other high-current industrial equipment. It should provide low-resistance conductors, mechanical support, insulation/clearance, terminals, and enclosure or guarding.

## Reality classification

Classification: real practical electrical infrastructure/equipment, not a manufacturing machine.

Busbars and busbar distribution systems are real and widely used in switchgear, panel boards, inverters, battery packs, industrial plants, renewable energy systems, and high-current process equipment. The KB's 200 kg mass is plausible for a substantial busbar cabinet or skid with copper, insulators, terminals, enclosure, and wiring. The `kind: machine` label is best interpreted as a simulator capacity-provider convention.

## Evidence links

- Ansys guide to electrical busbars: https://www.ansys.com/simulation-topics/what-are-electric-busbars
  - Defines a busbar as a metallic bar, strip, tube, or rod that conducts current safely with low losses.
  - Notes use instead of wires/cables for high-current power distribution, high-voltage equipment, and low-voltage battery applications.
  - Highlights design tradeoffs in safety, resistance, inductance, capacitance, mounting, and cooling.

- Eaton busbars: https://www.eaton.com/us/en-us/catalog/power-connections/busbars.html
  - Commercial busbars are used in automotive, industrial, aerospace, switchgear, panel boards, power inverters, power electronics, and high-voltage battery packs.
  - Describes copper/aluminum busbars, CNC bending, stamping, flexible laminated forms, insulation options, and testing.

- Storm Power Components insulated copper bus bars: https://stormpowercomponents.com/bus-bar/insulated-copper-bus-bars/
  - Insulated copper bus bars are used in switchgear, switchboards, and busway/bus duct installations.
  - Describes solid copper or aluminum conductors with insulation between phase conductors and ground, plus ceramic/standoff insulators and kitting.

- GRL closed busbar systems: https://www.grlgroup.com/blogs/busbar-systems/
  - Describes core components of busbar systems: busbars, enclosures, connection modules, support structures, and insulation materials.
  - Lists practical applications in industrial plants, commercial buildings, data centers, and renewable energy projects.

- Electris busbar overview: https://www.electrispower.com/blog/bus-bars-what-are-they-and-what-are-they-made-of
  - Describes bus bars as copper/aluminum power rails used in switchgear, converters, inverters, and control cabinets.
  - Notes benefits such as space savings, easy assembly/maintenance, overload/surge prevention, and flexible circuit changes.

## Commercial alternatives

- Custom copper or aluminum busbar assemblies from manufacturers such as Eaton, Storm Power Components, Electris, and other electrical fabrication shops.
- Switchgear/panelboard busbar systems with breakers, disconnects, fuses, meters, and protection devices.
- Busway/bus duct systems for longer building or plant distribution runs.
- Laminated busbars for compact power electronics, inverters, battery packs, and lower-inductance high-current circuits.
- Cable-based distribution for smaller currents or more flexible routing, though it may be heavier, less organized, or harder to expand.

## Build or open-source references

No formal open-source industrial busbar system design was needed to establish reality. Local fabrication is plausible if the KB can produce copper bars, drill/machine/bend them, make ceramic or polymer insulators, fabricate a steel enclosure, and assemble terminals/fasteners. However, safe design requires ampacity sizing, creepage/clearance, insulation, short-circuit force tolerance, thermal management, grounding, protection devices, and testing.

For KB realism, the item should not be reduced to only copper bars; enclosure, supports, insulation, protection, and terminals matter.

## Related machine research

Existing related reports:

- `research/machines/power_conditioning_equipment.md`
- `research/machines/solar_array_v0.md`
- `research/machines/high_temperature_power_supply_v0.md`

Related KB items:

- `power_conditioning_module`
- `power_conditioning_equipment`
- `bus_bar_copper`
- `center_insulator_ceramic`
- `power_output_terminals`
- `electrical_wire_and_connectors`

## Recommendation for KB realism

Keep `power_distribution_bus`, but describe it as electrical distribution infrastructure rather than a machine.

Specific recommendation:

- Keep as a real equipment item.
- Consider renaming/displaying as "power distribution busbar cabinet" or "busbar distribution assembly" if future KB edits are allowed.
- Keep separate from `power_conditioning_equipment`: busbars distribute power; inverters/rectifiers/controllers condition power.
- For `chloralkali_electrolysis_v0`, this is particularly plausible because electrolysis can require high-current DC distribution.
- Consider adding or documenting protection devices, disconnects, fuses/breakers, grounding, and thermal/short-circuit ratings if high-current realism matters.
- The current BOM is directionally realistic, but quantities should eventually be sized by voltage, current, phase/DC layout, and environment.

## Confidence and open questions

Confidence: high that the equipment is real and useful; high that it is infrastructure rather than a production machine.

Open questions:

- Is this bus AC, DC, or both?
- What voltage/current rating is required for chloralkali electrolysis and the broader seed system?
- Are fuses, breakers, disconnects, grounding bars, and enclosures modeled elsewhere or intentionally omitted?
- Should this item be part of a broader electrical distribution panel/switchgear item?

