# Cartesian 3D Printer v0

## Machine identity

- KB ID: `resource_3d_printer_cartesian_v0_machine`
- KB name: Cartesian 3D printer v0
- KB file: `kb/items/machines/resource_3d_printer_cartesian_v0.yaml`
- Current KB type: `machine`
- Current KB mass: 120 kg
- Current KB description: Cartesian 3D printer for polymer/embedded SMA printing.
- Current KB BOM: printer frame, gantry axes, extruder head, drive motors, gearboxes, bearings, printer control module, power conditioning, sensors, imported compute module, and fasteners.

## KB usage and needed function

The KB uses this printer for:

- `additive_manufacturing_polymer_v0`
- `process_3d_print_motor_sma_v0`

The KB also contains overlapping printer items:

- `3d_printer_basic_v0`
- `resource_3d_printer_basic_v0`
- `resource_3d_printer_multi_material_v0`

The needed function is FDM/FFF-style additive manufacturing using Cartesian motion and an extruder to deposit polymer or polymer-composite material. The SMA use case suggests a more specialized embedded-material printer than a normal desktop polymer printer.

## Reality classification

Classification: real practical machine, with duplicate/naming issues.

Cartesian FDM/FFF 3D printers are common commercial and open-source machines. A 120 kg mass is plausible for a large-format, enclosed, or ruggedized printer, but high for a small desktop printer. The BOM is directionally credible, though drive motors should probably be stepper/servo motors rather than generic medium drive motors and gearbox reducers.

## Evidence links

- RepRap documents the Prusa i3 as an open-source Cartesian-style printer design using NEMA17 stepper motors, an extruder, and common 3D-printer electronics. Source: https://reprap.org/wiki/Prusa_i3
- Prusa Research documents its open-source software/firmware history, including firmware based on Marlin and FreeRTOS and published source repositories. Source: https://www.prusa3d.com/page/open-source-at-prusa-research_236812/
- Stratasys describes polymer 3D printers and FDM as one of the major technologies for prototyping and end-use part production. Source: https://www.stratasys.com/en/3d-printers/printer-catalog/
- Formlabs summarizes 3D printing types, materials, and applications, showing polymer additive manufacturing as a real commercial category. Source: https://formlabs.com/3d-printers/
- OpenBuilds publishes example Cartesian 3D printer builds using extruders, hot ends, part cooling fans, and motion components. Source: https://builds.openbuilds.com/?id=272
- A Prusa Blog interview notes that Adrian Bowyer founded RepRap, which introduced self-replicating 3D printers to the open-source hardware community. Source: https://blog.prusa3d.com/adrian-bowyer_127066/

## Commercial alternatives

- Desktop Cartesian FDM printer such as Prusa i3-style machines.
- Large-format Cartesian polymer printer.
- CoreXY printer, which is mechanically different but functionally similar for many FDM uses.
- Industrial FDM printer for ABS, PC, nylon, or high-temperature polymers.
- Multi-material printer with multiple toolheads or filament switching.
- Pellet-extrusion printer for larger parts and recycled feedstocks.

## Build or open-source references

This is one of the better-supported machine classes for local/open-source construction. Common build elements include:

- Rigid frame or sheet-metal enclosure.
- Linear rails, rods, belts, screws, or wheels for X/Y/Z motion.
- Stepper motors and drivers.
- Hot end, extruder, build plate, and bed heater.
- Controller board, firmware, limit/probe sensors, and power supply.
- Slicer/CAM workflow and calibration procedures.

Open-source designs such as RepRap/Prusa-style printers make this a realistic self-reproduction candidate, though they still need precision rods/rails, motors, electronics, nozzles, heaters, and sensors.

## Related machine research

Related reports already present:

- `plastic_extruder.md`
- `control_compute_module_imported.md`
- `power_conditioning_equipment.md`
- `inspection_tools_basic.md`

Related KB items:

- `3d_printer_basic_v0`
- `resource_3d_printer_basic_v0`
- `resource_3d_printer_multi_material_v0`
- `printer_frame_generic`
- `gantry_axes_set`
- `extruder_head_basic`
- `printer_control_module`
- `stepper_motor_v0`

## Recommendation for KB realism

Keep the machine concept, but deduplicate and clarify capability.

Recommended future cleanup:

- Use one canonical basic FDM/FFF printer item unless the `resource_` prefix has a schema meaning.
- Reserve `resource_3d_printer_cartesian_v0_machine` for a specific Cartesian printer if embedded SMA printing requires special toolheads or process controls.
- Use `resource_3d_printer_multi_material_v0` for real multi-material capability.
- Replace generic drive motors/gearboxes with stepper or servo motion components where appropriate.
- Clarify whether the printer is desktop, large-format, enclosed industrial, or high-temperature.

Do not treat this as a placeholder. Cartesian FDM printers are real, buildable, and relevant to self-reproducing-system modeling.

## Confidence and open questions

Confidence: high that the machine is real; high that the KB has duplicate printer concepts; medium on whether embedded SMA printing requires a special printer variant.

Open questions:

- Should `3d_printer_basic_v0` and `resource_3d_printer_basic_v0` be merged?
- Does embedded SMA printing need multi-material deposition, wire embedding, or post-processing beyond standard FDM?
- Is 120 kg meant to represent an industrial enclosed printer rather than a desktop printer?
