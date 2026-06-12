# Hot Press v0

## Machine identity

- KB ID: `hot_press_v0`
- KB name: Hot press v0
- KB file: `kb/items/machines/hot_press_v0.yaml`
- Current KB type: `machine`
- Current KB mass: 950 kg
- Current KB description: hot press for sintering/consolidation.
- Current KB BOM: heavy frame, medium hydraulic system, heated platens, high-temperature heating elements, insulation, thermocouple, temperature controller, control module, sensors, power conditioning, fasteners, and bulk material.

## KB usage and needed function

The KB uses `hot_press_v0` for:

- `sintering_and_hot_pressing_v0`
- `spinel_synthesis_v0`
- `ndfeb_magnet_sintering_v0`

It is also referenced by recipes for sintered shapes, permanent neodymium magnets, and electrodes. Documentation already identifies it as a specialized capability worth keeping separate from generic presses and furnaces.

The needed function is simultaneous application of heat and uniaxial pressure to powders, green compacts, ceramics, magnets, electrodes, or diffusion-bonded parts. It combines press force, heated dies/platens or a furnace hot zone, temperature control, and often vacuum/inert/reducing atmosphere.

## Reality classification

Classification: real practical machine.

A hot press is not just a hydraulic press with a heater and not just a furnace. It is a combined mechanical and thermal consolidation machine. Commercial hot pressing systems are used for powder metallurgy, ceramics, composites, diffusion bonding, refractory materials, and advanced materials research.

The 950 kg KB mass is plausible for a small lab or pilot-scale hot press with a steel frame, hydraulic system, heated platens, insulation, controls, and power electronics. Larger vacuum hot press furnaces can be much heavier.

## Evidence links

- Centorr Vacuum Industries describes hot pressing furnaces as combining added force during sintering of high-temperature materials in vacuum or inert gas to increase density. Source: https://vacuum-furnaces.com/hot-pressing-furnaces/
- Thermal Technology describes hot press furnace systems as applying hydraulic pressing force during simultaneous high-temperature operation, with uses including sintering metal or ceramic powders and diffusion bonding. Source: https://www.thermaltechnology.com/products/hot-press/
- Thermal Technology reports a 50-ton molybdenum hot press with a 1600 C molybdenum hot zone for diffusion bonding advanced sensors, operating in inert gas, high vacuum, or other atmospheres. Source: https://www.thermaltechnology.com/thermal-technology-ships-50-ton-molybdenum-hot-press/
- Kintek describes a laboratory hot press as using heated plates/platens brought together by hydraulic or pneumatic force to shape, bond, cure, or densify material. Source: https://kinteksolution.com/faqs/how-does-a-laboratory-hot-press-work
- A powder metallurgy overview describes hot pressing as simultaneous high temperature and uniaxial pressure for compacting and densifying powdered materials, combining pressing and sintering in one step. Source: https://powdermetallurgy.com/hot-pressing/
- A NIST Materials Data Repository scan of "Forging and Hot Pressing" distinguishes hot pressing as compression of loose powder or powder compact in a die cavity with little lateral deformation. Source: https://materialsdata.nist.gov/bitstream/handle/11115/194/Forging%20and%20Hot%20Pressing.pdf?sequence=3

## Commercial alternatives

- Laboratory heated platen press for polymers, composites, and low-temperature materials.
- Vacuum hot press furnace for ceramics, metals, graphite, and refractory materials.
- Graphite hot press for high-temperature ceramic and powder metallurgy.
- Spark plasma sintering press where pulsed current assists sintering.
- Hot isostatic press for gas-pressure consolidation in all directions.
- Separate hydraulic press plus sintering furnace, where simultaneous pressure during heat is not needed.

## Build or open-source references

A simple heated platen press can be built from a hydraulic press, machined platens, cartridge heaters or resistance heaters, thermocouples, insulation, and temperature controllers.

A high-temperature ceramic or metal powder hot press is much harder. It needs:

- Rigid press frame sized for force at temperature.
- Hydraulic or screw force system with load measurement.
- High-temperature platens, dies, or graphite tooling.
- Insulation and guarded hot zone.
- Temperature, load, and displacement control.
- Vacuum or inert/reducing atmosphere hardware if oxidation-sensitive materials are processed.
- Safety interlocks for heat, pressure, hydraulics, and gas/vacuum systems.

The current KB BOM captures the basic frame, hydraulic, heated platen, heating, insulation, sensing, control, and power pieces. It may underrepresent dies, vacuum/gas chamber, load cell, displacement measurement, and safety shielding.

## Related machine research

Related reports already present:

- `hydraulic_press.md`
- `sintering_furnace_v0.md`
- `furnace_high_temp.md`
- `reduction_furnace_v0.md`
- `power_conditioning_equipment.md`
- `high_temperature_power_supply_v0.md`

`hot_press_v0` should remain distinct from `hydraulic_press` because hot pressing requires controlled heating during pressure. It should remain distinct from `sintering_furnace_v0` where pressure during heating is a required process variable.

## Recommendation for KB realism

Keep as a real specialized machine.

Recommended future wording: "pilot-scale heated platen/vacuum hot press for powder and ceramic consolidation." If the KB only requires low-temperature polymer/composite pressing, a simpler heated hydraulic press is enough. If it requires NdFeB magnets, ceramics, graphite, tungsten, or refractory materials, model it as a high-temperature hot press with explicit die/tooling, load measurement, and possibly vacuum/inert atmosphere.

Do not merge this into `hydraulic_press` or `sintering_furnace_v0` unless the process does not actually require simultaneous pressure and heat.

## Confidence and open questions

Confidence: high that hot presses are real and distinct; medium that the current BOM fully represents the required high-temperature/vacuum implementation.

Open questions:

- What maximum force, temperature, and platen/die size are assumed?
- Does `ndfeb_magnet_sintering_v0` require vacuum or inert gas hot pressing?
- Should load cells, displacement sensors, and die sets be explicit BOM components?
- Should hot isostatic pressing or spark plasma sintering be separate machine items?
