# Molding Press Basic

## Machine identity

- KB ID: `molding_press_basic`
- KB name: Molding press (basic)
- KB file: `kb/items/machines/molding_press_basic.yaml`
- Current KB type: `machine`
- Current KB mass: 300 kg
- Current KB description: basic molding press for ceramic and powder metallurgy applications, forming green parts from powder mixtures.
- Current KB BOM: molding press frame, hydraulic cylinder, platen set, hydraulic power unit, molding control unit, and fasteners.

## KB usage and needed function

The KB uses `molding_press_basic` for:

- `molding_press_operation_v0`
- `molding_basic_v0`
- `molding_rubber_or_plastic_v0`
- `plastic_housing_molding_v0`
- `elastomer_molding_basic_v0`
- `silicone_rubber_vulcanization_v0`
- `tactile_sensor_silicone_cast_v0`

It is also used as a generic press for molded rubber/plastic pieces and pressed powder/ceramic components. The needed function is controlled compression of feedstock in a mold using hydraulic force and platens. Some use cases require heat, cure time, or temperature-controlled platens; powder metallurgy may require high force and precise fill/ejection tooling.

## Reality classification

Classification: real practical machine, but broad.

Basic molding presses, compression molding presses, and powder compacting presses are real industrial machines. The KB's 300 kg mass is plausible for a small lab or light shop press, but low for production powder compaction or compression molding presses. The BOM is realistic for a basic hydraulic platen press, but it does not explicitly include heated platens, mold tooling, ejectors, pressure/temperature sensors, guarding, or material-specific control features.

## Evidence links

- Williams, White describes molding presses as using controlled heat and hydraulic pressure to shape materials in matched metal molds, including thermoset, thermoplastic, BMC, and SMC applications. Source: https://williamswhite.com/hydraulic-presses/applications/molding/
- Gasbarre describes hydraulic powder press machines from 15 to 1,200 tons for carbides, powder metals, ceramics, polymers, and other particulate materials. Source: https://www.gasbarre.com/products/press/
- DORST Technologies describes axial powder and sizing presses for ceramics, hardmetal, and metal powder, including multi-platen and complex compacting features. Source: https://www.dorst-technologies.com/en/products/axial-powder-presses
- French Oil Mill describes rubber molding presses with electrically, oil, or steam heated platens for uniform heat and temperature control. Source: https://frenchoil.com/products/hydraulic-presses/rubber-molding-press/
- Alma Machinery lists used compression molding presses with heated platens, tonnage ratings, daylight, stroke, and controls for plastics, rubber, foam, and composites. Source: https://www.almamachinery.com/for-sale/used-presses/hydraulic-presses/compression-molding-presses/
- MetalPress Machinery describes powder pressing as compacting metal, ceramic, or composite powders into a green compact that is later sintered, with hydraulic presses providing force control. Source: https://metalpressmachinery.com/vcompression-molding-powder-pressing-advanced-press-technologies/

## Commercial alternatives

- Manual or hydraulic shop press with simple molds.
- Heated platen compression molding press for rubber, thermosets, composites, and some plastics.
- Powder compacting press for ceramics and powder metallurgy.
- Injection molding machine for thermoplastics where melt injection into a closed mold is required.
- Transfer molding press for rubber/thermoset parts.
- Pellet press or tablet press for small simple powder compacts.

## Build or open-source references

A simple molding press is locally buildable from:

- Welded or cast steel H-frame/four-post frame.
- Hydraulic cylinder and pump.
- Upper/lower platens and guide posts.
- Pressure gauge or load measurement.
- Basic controls and guarding.
- Mold/die sets matched to the part.

Heated compression molding requires cartridge heaters, temperature controllers, thermal insulation, platen temperature uniformity, and cooling or cure timing. Powder compaction requires more precise die/punch alignment, ejection, lubrication, and repeatable fill mass. Injection molding is a separate machine class because it needs melt plasticization and injection screw/ram hardware.

## Related machine research

Related reports already present:

- `hydraulic_power_unit_basic.md`
- `hydraulic_press.md`
- `hot_press_v0.md`
- `sintering_furnace_v0.md`
- `plastic_extruder.md`

`molding_press_basic` can be a simpler cold or modest-temperature press. `hot_press_v0` is the higher-temperature sintering/consolidation version. `plastic_extruder` and injection molding equipment are distinct polymer-processing machines.

## Recommendation for KB realism

Keep as a real machine, but clarify scope.

Recommended future wording: "basic hydraulic compression/powder molding press." If polymer housings are intended to be injection molded, do not use this as a substitute for an injection molding machine. If rubber, silicone, composites, and thermosets are intended, add heated platen capability and mold tooling. If ceramic/powder metallurgy green pressing is intended, add die/punch/ejector tooling and pressure capacity.

The KB should also reconcile the existence of `molding_press`, `molding_press_v0`, and `molding_press_basic` so the imported machine list does not count duplicates.

## Confidence and open questions

Confidence: high that the machine is real; medium that one basic press covers all current polymer, rubber, silicone, ceramic, and powder-metal uses.

Open questions:

- Is this press heated or cold?
- What force/tonnage and platen size are assumed?
- Should molds/dies be separate tooling items consumed or required by each recipe?
- Should thermoplastic housings use injection molding rather than compression molding?
