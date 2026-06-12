# Solar array v0

## Machine identity

- Queue item: `machine_reality_solar_array_v0`
- KB ID: `solar_array_v0`
- KB file: `kb/items/machines/solar_array_v0.yaml`
- KB name: Solar array v0
- KB kind: `machine`
- KB modeled mass: 400 kg

The KB defines this as imported PV modules on a locally produced mount. The BOM includes eight `pv_module_imported` units, an `array_mount_structure`, `power_conditioning_module`, imported control compute module, sensor suite, and fasteners.

## KB usage and needed function

`solar_array_v0` is listed in the minimal/self-reproducing seed set and is used by `solar_power_generation_basic_v0`.

The needed function is electrical power generation from sunlight, with enough mounting, wiring, power conditioning, and control/monitoring to provide usable power to the modeled system. The KB item is more like installed power infrastructure than a factory machine.

## Reality classification

Classification: real practical infrastructure/equipment, not a manufacturing machine.

Solar arrays are real and commodity-scale equipment. The KB's mass of 400 kg for eight PV modules plus racking and power electronics is plausible for a small ground or rack-mounted array. The item is correctly treated as imported if the KB assumes PV modules cannot yet be locally manufactured. The "machine" kind is likely a simulator convention for capacity/power providers rather than a literal machine classification.

## Evidence links

- University of Arizona Extension, "Solar Photovoltaic (PV) System Components": https://extension.arizona.edu/sites/extension.arizona.edu/files/pubs/az1742-2018.pdf
  - Explains that a solar array is made of multiple PV modules wired together.
  - Describes modules mounted on racks, series strings, combiner boxes, and system components.

- DOE solar PV system cost benchmarks: https://www.energy.gov/cmei/systems/solar-photovoltaic-system-cost-benchmarks
  - DOE cost model divides installed PV systems into modules, inverters, energy storage, structural balance of system, electrical balance of system, fieldwork, office work, and other costs.
  - Supports treating modules, inverter/power conditioning, racking, and wiring/BOS as distinct components.

- University of Michigan Center for Sustainable Systems, Solar PV Energy Factsheet: https://css.umich.edu/publications/factsheets/energy/solar-pv-energy-factsheet
  - Defines a PV array as electrically connected modules fastened to a rigid structure.
  - Notes BOS components include connecting wires, junction boxes, mounting hardware, and power electronics.
  - Gives typical PV module construction and weight ranges.

- Morningstar, "How Does a Solar Charge Controller Work?": https://www.morningstarcorp.com/faq/how-does-solar-charge-controller-work/
  - Describes charge controllers for off-grid/hybrid systems regulating PV array current and voltage to batteries and loads.
  - Explains MPPT/PWM regulation and protections such as reverse current, short circuit, high voltage, high temperature, and reverse polarity.

- Penn State EME 812, main components of large PV systems: https://courses.ems.psu.edu/eme812/node/681
  - Describes power conditioning and balance-of-system components, including inverters, controllers, transformers, wiring, connector boxes, switches, monitoring devices, charge regulators, and storage.
  - Notes modular PV system design and long operational-life goals.

## Commercial alternatives

- Off-grid PV kit: PV modules, racking, charge controller, battery bank, inverter, disconnects, wiring, and protections.
- Grid-tied PV system: modules, racking, string/microinverters, combiner/disconnect equipment, wiring, monitoring, and grid interconnect.
- Ground-mounted array: more realistic for a lunar/base-like setting than rooftop systems; may need dust mitigation and robust anchoring.
- Tracking array: real, but adds actuators, structure, sensors, and maintenance; not implied by the current KB item.
- Thin-film/flexible panels or space-rated arrays: real but not equivalent to commodity imported PV modules.

## Build or open-source references

PV module manufacturing is complex and likely outside current local manufacturing capability, so the KB note that modules are imported is realistic. Local assembly of mounts, wiring, and array installation is practical with metal fabrication, electrical wiring, fasteners, and power electronics.

Open-source/off-grid solar installation guides exist, but they do not make PV cells/modules locally. For KB realism, the build split should be:

- imported PV modules and probably some power electronics,
- locally fabricated support structure and mounting fixtures,
- local wiring/assembly/testing where feasible.

## Related machine research

Existing related report:

- `research/machines/power_conditioning_equipment.md`

Related KB items:

- `power_conditioning_module`
- `power_conditioning_equipment`
- `power_distribution_bus`
- `rover_solar_array_v0`
- `solar_array_cleaning_brush_v0`

## Recommendation for KB realism

Keep `solar_array_v0`, but treat it as installed power infrastructure/equipment rather than a machine.

Specific recommendation:

- Keep the item as real and practical.
- Keep PV modules imported unless the KB adds a serious photovoltaic manufacturing chain.
- Clarify scope if future KB edits are allowed: "small installed PV array with BOS" or split `solar_array_v0` into PV modules, racking/mount, power conditioning, and installation.
- Do not over-collapse with `power_conditioning_equipment`; PV generation and power conditioning are related but distinct.
- The current BOM is realistic at a coarse level, though it omits combiner/disconnects, wiring, grounding, fuses/breakers, and optional batteries.
- For lunar/regolith-heavy environments, dust cleaning and degradation should be modeled separately if operational reliability matters.

## Confidence and open questions

Confidence: high that the item is real and useful; high that it is infrastructure rather than a machine in the normal manufacturing sense.

Open questions:

- What is the intended power rating of this 400 kg array?
- Does the KB need battery storage paired with the array, or is power storage modeled elsewhere?
- Should the imported-machine list distinguish `pv_module_imported` from the assembled `solar_array_v0`?
- Is this intended for terrestrial, lunar, or generic solar conditions? Insolation, dust, angle, and day/night cycles change required sizing.

