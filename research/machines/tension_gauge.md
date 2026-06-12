# Tension gauge

## Machine identity

- KB ID: `tension_gauge`
- KB name: Tension gauge
- KB file: `kb/items/parts/tension_gauge.yaml`
- KB kind in file: `machine`
- Current KB mass: 2 kg
- Current KB scope: mechanical or electronic gauge for measuring wire, cable, belt, or fiber tension.

## KB usage and needed function

The KB uses `tension_gauge` in two ways:

- As a BOM component in `kb/boms/bom_tension_control_system_v0.yaml`.
- As a `machine_id` resource requirement in `kb/processes/belt_installation_and_tensioning_v0.yaml`.

The needed function is measurement and calibration of tension during belt installation, wire/cable setup, fiber spinning, or winding. This is narrower than `tension_control_system`, which actively regulates tension.

## Reality classification

Classification: real practical instrument/tooling item, but probably not a machine.

Tension gauges and tension meters are real commercial instruments. They can be handheld mechanical devices, electronic load-cell meters, clamp-on cable tension meters, or sonic belt tension meters. However, a tension gauge is more naturally a tool, instrument, or part of a control system than a standalone machine.

The 2 kg mass is plausible for a handheld or small bench/fixture-mounted tension gauge.

## Evidence links

- Checkline sells hand-held, fixed-mount, analog, digital, cable, yarn, wire, fiber, belt, and web tension meters and sensors. Source: https://www.checkline.com/tension_meters
- Loos & Co. sells cable tension gauges for standing rigging and architectural railings, with stated accuracy and cable/rod diameter ranges. Source: https://loosco.com/tension-gauges/
- Gates sells sonic belt tension meters for measuring belt installation tension from belt vibration/sound waves. Source: https://www.gates.com/gb/en/power-transmission/power-transmission-tools-and-merchandisers/power-transmission-tools.p.7420-000000-000009.html
- Rice Lake/MSI offers clamp-on cable tension meters for wire rope and cable measurement without changing sheaves or bobbins. Source: https://www.ricelake.com/tension-meter-landing/

## Commercial alternatives

Commercial alternatives include:

- Mechanical cable tension gauge.
- Digital handheld tension meter.
- Fixed-mount tension sensor or load cell.
- Sonic belt tension meter.
- Clamp-on cable or wire-rope tension meter.
- Inline dynamometer or force gauge for calibration.

For the KB's belt installation process, a handheld belt tension gauge or sonic belt tension meter is adequate. For continuous winding or fiber drawing, a tension sensor plus controller belongs under `tension_control_system`.

## Build or open-source references

Simple tension gauges can be built from a spring/plunger, calibrated deflection fixture, load cell, or strain gauge:

- Arduino forum discussions describe electronic tension gauges using load cells and fixed cable deflection geometry: https://forum.arduino.cc/t/electronic-tension-gauge/371309
- Electronics Stack Exchange discusses measuring rope tension with a spring-loaded plunger and calibration, or load-cell-based methods: https://electronics.stackexchange.com/questions/312460/measuring-tension-force-on-rope

DIY versions can be good enough for coarse setup and calibration. Certified lifting, safety, or high-value equipment should use calibrated/rated instruments.

## Related machine research

Related local research:

- `research/machines/tension_control_system.md`

Related KB items:

- `tension_control_system`
- `tension_control_unit`
- `wire_tensioning_mechanism`
- `coil_winding_machine`
- `fiber_drawing_tower`
- `belt_installation_and_tensioning_v0`

The gauge should remain distinct from the tension controller. The gauge measures; the control system measures and actuates.

## Recommendation for KB realism

Keep the object, but consider reclassifying it as a tool/instrument rather than a machine.

Recommended future cleanup:

- Treat `tension_gauge` as a portable measurement tool or calibration instrument.
- Use it as a component of `tension_control_system` where continuous feedback is needed.
- Avoid requiring it as a full machine unless the schema has no better tooling category.
- If KB realism demands specificity, split into `belt_tension_meter`, `wire_tension_meter`, and `cable_tension_meter` only when required by incompatible ranges or measurement methods.

For conservative mode, one generic tension gauge is acceptable across belts, cables, and wires at coarse modeling precision.

## Confidence and open questions

Confidence: high that the object is real and practical; high that it is better modeled as an instrument/tool than as a machine.

Open questions:

- Does the KB distinguish portable tools from machines in resource requirements?
- What tension range is required for belt drives versus wire/fiber handling?
- Should calibration equipment or reference weights be modeled?
- Is `tension_gauge` needed as a process resource, or should it be bundled into `assembly_tools_basic` for manual setup tasks?
