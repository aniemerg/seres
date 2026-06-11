# Sintering Furnace v0

## Machine identity

- KB ID: `sintering_furnace_v0`
- KB name: Sintering furnace v0
- KB file: `kb/items/machines/sintering_furnace_v0.yaml`
- Current KB type: `machine`
- Current KB mass: 1067 kg
- Current KB note: deprecated and consolidated into `furnace_basic`
- Current KB BOM: refractory shell, high-temperature heating elements, insulation, thermocouple, controller, sensors, control module, power conditioning, cooling loop, and fasteners.

## KB usage and needed function

Despite the deprecation note, `sintering_furnace_v0` is still used by active process files, including:

- `sintering_and_hot_pressing_v0`
- `spinel_synthesis_v0`
- `ferrite_toroid_sintering_v0`
- `porcelain_insulator_fabrication_v0`
- `grinding_media_alumina_fabrication_v0`
- `ferrite_sintering_process_v0`
- `tungsten_extraction_meteorite_v0`
- `ndfeb_magnet_sintering_v0`
- `regolith_sinter_block_process_v0`
- `tungsten_sintering_high_temp_v0`
- `sintering_aid_mgo_production_v0`
- `tungsten_blank_sintering_high_temp_v0`

The needed function is high-temperature consolidation and bonding of powders or green bodies below their full melting point, usually with controlled temperature profile and sometimes vacuum, inert gas, hydrogen, nitrogen, or other protective/reducing atmosphere.

## Reality classification

Classification: real practical machine category, but the current KB status is internally inconsistent.

Sintering furnaces are standard equipment for powder metallurgy, ceramics, ferrites, tungsten and refractory metals, metal injection molding, binder-jet/3D printed metal parts, and advanced materials. They may be batch, tube, vacuum, controlled-atmosphere, belt, pusher, or hot-zone furnaces.

The 1067 kg KB mass is plausible for a small production or pilot-scale furnace with refractory shell, insulation, cooling, controls, and power electronics. It is heavier than a lab muffle furnace and lighter than large continuous industrial belt or pusher lines.

## Evidence links

- Sentro Tech sells vacuum and controlled-atmosphere sintering furnaces for 3D metal printing, labs, and production, with models up to 1600-1700 C. Source: https://www.sentrotech.com/products/sintering-furnaces/
- Centorr Vacuum Industries describes high-temperature sintering furnaces for metals and ceramics, including vacuum and controlled atmosphere processing from 1000 C to 3000 C. Source: https://vacuum-furnaces.com/sintering-furnaces-metals-ceramics/
- Western Sintering describes controlled-atmosphere sintering in electric furnaces using nitrogen and hydrogen for compacted powder metal parts. Source: https://www.westernsintering.com/controlled-atmosphere-sintering/
- Abbott Furnace defines powder metal sintering as a thermal process that chemically bonds adjacent metal particles to improve compact properties. Source: https://abbottfurnace.com/sintering-fundamentals/
- CM Furnaces notes that powder metallurgy sintering can require at least 1300 C in hydrogen, with continuous or pusher furnaces common in production. Source: https://cmfurnaces.com/powder-metallurgy-sintering-considerations/
- Across International describes vacuum sintering furnaces as equipment for heating powder compacts to increase strength, density, and translucency without liquefying the material. Source: https://www.acrossinternational.com/news/post/shaping-materials-with-heat-in-vacuum-sintering-furnaces

## Commercial alternatives

- Vacuum sintering furnace for metals, tungsten, ceramics, magnets, and binder-jet metal parts.
- Controlled-atmosphere batch furnace for powder metallurgy.
- Tube furnace for small samples and reactive atmospheres.
- Continuous belt furnace for lower-temperature high-volume powder metal parts.
- Pusher furnace for higher-throughput and higher-temperature production.
- Hot press or spark plasma sintering equipment where pressure or pulsed current is required.

The current KB item is closest to a compact batch controlled-atmosphere/vacuum-capable sintering furnace, not a generic furnace_basic, if ferrites, magnets, tungsten, and ceramics are in scope.

## Build or open-source references

Small simple kilns and muffle furnaces can be built from refractory insulation, heating elements, thermocouples, controllers, and a steel shell. A realistic sintering furnace for the KB's uses is harder because it may require:

- High-temperature uniformity and ramp/soak control.
- Gas-tight chamber or retort.
- Vacuum pump or controlled gas flow.
- Hydrogen/inert atmosphere safety interlocks where reducing atmosphere is used.
- Clean hot-zone materials to avoid contamination.
- Fixtures, setters, trays, or boats compatible with the sintering material.

The BOM already captures the main furnace body, heating, insulation, control, power, and cooling pieces. It does not explicitly include vacuum hardware or process gas delivery, which may matter for metal powders, tungsten, ferrites, and NdFeB magnets.

## Related machine research

Related reports already present:

- `furnace_high_temp.md`
- `heating_furnace.md`
- `reduction_furnace_v0.md`
- `glass_furnace_v0.md`
- `casting_furnace_v0.md`
- `high_temperature_power_supply_v0.md`
- `power_conditioning_equipment.md`

The strongest overlap is with `furnace_high_temp`; however, sintering often has atmosphere, uniformity, contamination, and cycle-control requirements that justify a distinct item when powder metallurgy and ceramics are central.

## Recommendation for KB realism

Keep the concept as real, but resolve the deprecation inconsistency.

Recommended path: if all current sintering processes can tolerate a generic high-temperature furnace, replace their machine references with `furnace_basic` or `furnace_high_temp` and remove this item from the imported self-reproducing set. If any processes need controlled atmosphere, vacuum, clean hot zone, or powder/ceramic sintering cycle control, retain this item and rename it to something more specific such as `controlled_atmosphere_sintering_furnace_v0` or `vacuum_sintering_furnace_v0`.

Do not discard it as unrealistic. Sintering furnaces are real and common. The open issue is whether the KB wants a generic heat source or a dedicated sintering furnace with atmosphere/vacuum capability.

## Confidence and open questions

Confidence: high that the machine category is real and relevant; high that the current deprecated note conflicts with active usage; medium on the best consolidation target.

Open questions:

- Should ferrite, NdFeB, tungsten, alumina, porcelain, and regolith sintering all share one furnace?
- Does the KB require vacuum or reducing/protective atmosphere for these processes?
- Should hot pressing be modeled separately from sintering if pressure is required?
- If retained, should gas delivery and vacuum equipment be explicit BOM components?
