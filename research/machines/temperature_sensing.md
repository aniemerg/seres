# Machine identity

- Queue item: `machine_reality_temperature_sensing`
- KB item: `temperature_sensing`
- KB name: Temperature sensing equipment
- KB file: `kb/items/parts/temperature_sensing.yaml`
- Current KB kind: `machine`
- Current mass: 2 kg
- Current status: `deprecated: true`
- Replacement items:
  - `thermocouple_contact_temperature_sensor_v0`
  - `rtd_contact_temperature_sensor_v0`
  - `optical_pyrometer_temperature_sensor_v0`
  - `temperature_controller_module`

# KB usage and needed function

`temperature_sensing` is a deprecated generic bundle. Local search found the KB has already moved toward more specific temperature sensing assemblies:

- Thermocouple contact temperature sensor assembly for furnaces, casting furnaces, sintering furnaces, hot presses, and general high-temperature feedback.
- RTD contact temperature sensor assembly for lower/medium temperature precision monitoring.
- Optical pyrometer temperature sensor assembly for non-contact high-temperature and molten-material measurement.
- Temperature controller module for PID/control electronics and relay/SSR output.

The needed function is real: measure temperature and feed control/monitoring loops for furnaces, reactors, hot presses, drying ovens, chillers, hydraulics, electronics bays, and molten-material processes. The issue is that the generic `temperature_sensing` item combines several different sensor technologies with different ranges, accuracies, manufacturability, and process constraints.

# Reality classification

Real practical instrumentation category, but not a machine and not a good single imported item.

Thermocouples, RTDs, thermistors, infrared thermometers, and optical pyrometers are all real. The KB's current replacement mapping is the right realism direction because contact thermocouples, precision RTDs, non-contact pyrometers, and controller electronics should not be treated as interchangeable.

# Evidence links

- NI overview of temperature sensors describes common sensor varieties including thermocouples, RTDs, and thermistors, each with different operating principles, benefits, and drawbacks: https://www.jlab.org/div_dept/physics_division/dsg/technical_documentation/Hall_C/NPS_3/Readings/overview_of_temperature_sensors.pdf
- Omega Engineering explains thermocouples and common probe/junction styles, including grounded, ungrounded, and exposed junctions: https://www.omegaengineering.cn/prodinfo_eng/thermocouples.html
- Weschler Instruments describes RTDs as resistance temperature detectors and notes RTDs are accurate and stable industrial sensors, commonly using platinum, nickel, or copper elements: https://www.weschler.com/reference/guides/guide-to-temperature-measuring-sensors/
- Fluke Process Instruments describes spot pyrometers as fixed thermal sensors for measuring single points on high-temperature surfaces, often in furnaces or kilns, using emitted thermal radiation: https://www.flukeprocessinstruments.com/en-us/products/infrared-temperature-solutions/spot-pyrometers
- AMETEK Land sells fixed spot non-contact thermometers and pyrometers for temperature measurement/control up to 2600 C: https://www.ametek-land.com/products/non-contact-infrared-thermometers-pyrometers
- Watlow compares sensor types and summarizes the common tradeoff that thermocouples handle high temperatures while RTDs are more accurate and stable in their range: https://www.watlow.com/blog/posts/ultimate-guide-to-sensor-types-applications-temperature-ranges-and-recommendations

# Commercial alternatives

Commercial alternatives should be chosen by use case:

- Type K/N/S/B thermocouple probes, extension wire, connectors, ceramic or metal protection sheaths, and thermocouple input modules.
- RTD probes such as Pt100/Pt1000 or nickel RTDs for lower/medium temperature measurement where stability/accuracy matter.
- Thermistors for low-cost lower-temperature electronics and environmental sensing.
- Infrared thermometers or fixed optical pyrometers for high-temperature, moving, molten, corrosive, or inaccessible targets.
- PID temperature controllers, SSRs/relays, signal conditioners, and data acquisition modules.

# Build or open-source references

Local build feasibility differs by sensor type:

- Basic thermocouple assemblies are plausible if the KB has suitable alloy wire, wire drawing, junction welding, insulation, sheaths, connectors, and calibration.
- RTDs are harder to make accurately because stable resistance elements, encapsulation, lead attachment, and precision calibration matter.
- Optical pyrometers are much harder early imports because they require optics, detectors, emissivity handling/calibration, sight tubes/viewports, and signal electronics.
- Temperature controller modules are electronic parts/subassemblies, not sensors; they should remain separate from the probe technology.

The KB's current replacement structure already reflects this split.

# Related machine research

Related local reports:

- `heating_furnace.md`
- `sintering_furnace_v0.md`
- `hot_press_v0.md`
- `reduction_furnace_v0.md`
- `glass_furnace_v0.md`
- `drying_oven.md`
- `multimeter_set.md`

Those machines/processes depend on temperature sensing but should require the appropriate specific sensor type.

# Recommendation for KB realism

Treat `temperature_sensing` as superseded. Do not keep it in an imported machine list as a real machine.

Recommended handling:

- Remove `temperature_sensing` from imported-machine lists once references are migrated.
- Use `thermocouple_contact_temperature_sensor_v0` plus `temperature_controller_module` for ordinary furnace/platen/shell feedback.
- Use `rtd_contact_temperature_sensor_v0` plus `temperature_controller_module` for low/medium temperature precision monitoring.
- Use `optical_pyrometer_temperature_sensor_v0` plus controller/DAQ electronics for molten glass, molten regolith, very high-temperature surfaces, and inaccessible targets.
- Keep pyrometers and high-quality RTDs as imports unless the KB explicitly models precision optics/detectors/calibration or precision resistance-element fabrication.
- Preserve the deprecated item only as a migration alias if the queue/indexer needs backward compatibility.

# Confidence and open questions

Confidence: high that the category is real; high that it should remain deprecated and replaced with specific sensor assemblies; high that it is instrumentation rather than a machine.

Open questions:

- Are any processes still requiring `temperature_sensing` directly, or has the migration already removed live references?
- Should temperature control electronics be modeled as one shared `temperature_controller_module` or split into low-power PID modules, furnace safety controllers, and DAQ-only modules?
- Does the simulation distinguish measured process temperature from shell/guard/heater feedback?
