# Power Conditioning Equipment

## Machine identity

- KB ID: `power_conditioning_equipment`
- KB name: Power conditioning equipment
- KB file: `kb/items/machines/power_conditioning_equipment.yaml`
- Current KB type: `machine`
- Current KB mass: 80 kg
- Current KB description: inverters, voltage regulators, and DC-AC converters for solar power integration.

## KB usage and needed function

The KB uses this item in:

- `solar_power_generation_basic_v0`
- `power_conditioning_basic_v0`
- `load_testing_and_commissioning_v0`
- Thermionic power system recipes and BOMs, including `recipe_machine_thermionic_power_system_v0` and `recipe_thermionic_topping_cycle_v0`

The needed function is electrical power conversion, regulation, stabilization, and integration between variable generation sources and useful loads. In the solar case this means converting or regulating PV DC output. In the thermionic case it likely means DC/DC conversion, voltage/current regulation, switching/protection, and load matching.

## Reality classification

Classification: real practical equipment category / bundled electrical subsystem.

Power conditioning equipment is real, but it is a broad category rather than one universal machine. It can include inverters, charge controllers, DC/DC converters, AC/DC rectifiers, voltage regulators, isolation transformers, filters, surge suppression, switchgear, monitoring, and controls. The KB's 80 kg mass is plausible for a modest power-conditioning cabinet or rack, depending strongly on power level and cooling requirements.

The current item is acceptable as a coarse subsystem for a minimal self-reproducing set. More detailed modeling should split by function and power level: PV inverter, DC/DC converter, high-current rectifier, voltage regulator, UPS/line conditioner, or thermionic converter power electronics.

## Evidence links

- U.S. Department of Energy, "Solar Integration: Inverters and Grid Services Basics": describes an inverter as a key solar-energy component that converts DC electricity from solar panels to AC electricity used by the grid. Source: https://www.energy.gov/cmei/systems/solar-integration-inverters-and-grid-services-basics
- Penn State AE 868, "Why Power Conditioning Units for PV?": explains that power from a source must be shaped to match load properties and discusses PV power conditioning unit configurations. Source: https://courses.ems.psu.edu/ae868/node/903
- Sinovoltaics, "Power Conditioning System": describes a PV power conditioning system as integrated equipment consisting of solar charge controller, inverter, and grid charger to meet load demands. Source: https://sinovoltaics.com/learning-center/components/power-conditioning-system/
- Trystar, "Power Conditioning": commercial power-conditioning transformers and voltage regulators for noise attenuation, transient suppression, and stable power for sensitive loads. Source: https://www.trystar.com/products/power-conditioning/
- AMETEK Solidstate Controls, "Power Conditioners": industrial power conditioners integrating precision line voltage regulator and shielded isolation transformer in one enclosure. Source: https://www.solidstatecontrolsinc.com/products/power-conditioners

## Commercial alternatives

- Solar inverter/charger and charge-controller systems.
- Industrial DC/DC converters and rectifier cabinets.
- Line voltage regulators, isolation transformers, surge suppressors, and power conditioners.
- UPS or double-conversion power systems where ride-through and clean AC are required.
- Custom thermionic or electrochemical process power electronics where source/load voltages are unusual.

## Build or open-source references

Low-power power-conditioning circuits can be built from published reference designs, but an 80 kg industrial subsystem is more like an engineered electrical cabinet. It requires power semiconductors, magnetics, control boards, bus bars, fusing/breakers, thermal management, shielding, grounding, and safety interlocks.

The KB has related lower-level items such as `power_conditioning_module`, `inverter_dc_to_ac_v0`, `power_supply_dc_high_current_v0`, `hv_rectifier_stack`, and `welding_power_supply_v0`. Those are better candidates for local subcomponent modeling than attempting a single open-source build reference for all power conditioning.

No complete open-source industrial PCU build covering the KB's solar and thermionic use cases was identified in this pass.

## Related machine research

Related KB items:

- `power_conditioning_module`
- `inverter_dc_to_ac_v0`
- `power_supply_dc_high_current_v0`
- `power_supply_benchtop`
- `high_temperature_power_supply_v0`
- `welding_power_supply_v0`
- `thermionic_power_system`
- `solar_array_v0`

The item overlaps with many specific power-supply and converter entries. Keep it as a system-level cabinet only where a process needs integrated power conditioning rather than a specific supply topology.

## Recommendation for KB realism

Keep as a system-level imported or locally assembled subsystem, but clarify scope.

Recommended future wording: "Integrated power conditioning cabinet for solar/thermionic generation: inverters, DC/DC conversion, voltage regulation, protection, filters, and controls." If future recipes require a specific electrical function, use a specific item (`inverter_dc_to_ac_v0`, `power_supply_dc_high_current_v0`, etc.) rather than this broad umbrella.

The item should not be replaced by labor bot plus tools because power conversion and regulation are active electrical functions. Labor is appropriate for installation, wiring, and commissioning only.

## Confidence and open questions

Confidence: high that the equipment category is real; medium that the single 80 kg generic item is the right abstraction for all current uses.

Open questions:

- What power rating does the 80 kg item represent?
- Is the output primarily AC, regulated DC, or both?
- Should thermionic converter power conditioning be split from solar PV/grid-style conditioning?
- Should `power_conditioning_module` be the reusable subcomponent and `power_conditioning_equipment` the assembled cabinet?
