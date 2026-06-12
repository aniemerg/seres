# Milling Machine General v0

## Machine identity

- KB ID: `milling_machine_general_v0`
- KB name: Milling machine (general) v0
- KB file: `kb/items/machines/milling_machine_general_v0.yaml`
- Current KB type: `machine`
- Current KB mass: 370 kg
- Current KB note: deprecated and consolidated into `cnc_mill`
- Current KB BOM: milling table, spindle head, drive motor, gearbox, heavy bearings, cutting tools, fasteners, power conditioning, imported control compute module, and sensors.

## KB usage and needed function

The KB still uses `milling_machine_general_v0` in many machining and fabrication processes, including:

- `machining_rough_v0`
- `machining_finish_basic_v0`
- `machining_raw_to_machined_part_v0` and `v1`
- `metal_cutting_basic_v0`
- `metal_cutting_process_v0`
- `steel_shaft_machining_v0` and `v1`
- `aluminum_housing_machining_v0` and `v1`
- `pump_housing_machining_v0`
- `gear_cutting_basic_v0`, `spur_gear_cutting_basic_v0`, `helical_gear_cutting_basic_v0`, `bevel_gear_cutting_basic_v0`, `worm_gear_cutting_basic_v0`, and `gear_cutting_v0`
- `robot_arm_link_fabrication_v0`
- `robot_wrist_fabrication_v0`
- `cooling_loop_basic_fabrication_v0`
- `flywheel_vacuum_housing_machining_v0`
- `surface_finishing_am_parts_v0`

The needed function is general subtractive milling: a rotating cutter removes material from a clamped workpiece to create flat surfaces, slots, holes, pockets, gear features, and accurately located geometry.

## Reality classification

Classification: real practical machine, but currently a deprecated duplicate/consolidation target.

Manual vertical/knee mills, horizontal mills, toolroom mills, and CNC mills are real machine classes. The KB item looks closer to a small manual or semi-manual general-purpose mill than a full CNC machining center. However, the BOM includes an imported control compute module and sensor suite, which blurs it toward CNC or digitally assisted milling.

The 370 kg KB mass is plausible for a small benchtop or light floor mill, but low for a Bridgeport-class knee mill. Typical vertical knee mills are often over 1000 kg. If this item is intended to cover serious steel gear cutting and machine-tool fabrication, the mass and stiffness may be understated.

## Evidence links

- Bridgeport describes the Series I Standard Knee Mill as a versatile milling, drilling, and boring machine with over 400,000 built over more than 70 years. Source: https://bridgeportmachinetools.com/product/milling/series-1/
- LeBlond describes vertical knee mills with work tables, X/Y motion, quill Z motion, spindle speeds, and a listed example net weight of 3350 lb (1520 kg). Source: https://leblondusa.com/vertical-knee-mill/
- Clausing describes manual knee mills as versatile machine tools that remove material from a workpiece using different cutting tools. Source: https://clausing-industrial.com/mills/standard-knee-mills/
- Summit Machine Tool describes knee mills as vertical milling machines used for cutting, surfacing, slotting, and drilling, with the workpiece clamped to a moving table and the cutting tool moving via quill. Source: https://summitmt.com/9-things-to-consider-before-buying-a-vertical-knee-mill/
- Xometry describes milling as a subtractive process using a rotating multi-edge cutter and controlled workpiece movement along axes. Source: https://www.xometry.com/resources/machining/what-is-milling-in-machining/
- DATRON distinguishes manual machining from CNC machining: manual machine tools are controlled by handwheels/levers, while CNC emphasizes programmed motion, precision, and repeatability. Source: https://www.datron.com/resources/blog/cnc-machining-vs-manual-machining/

## Commercial alternatives

- Manual vertical knee mill, Bridgeport-style.
- Manual horizontal mill.
- Benchtop mill or mill-drill for small work.
- Toolroom mill with digital readout and power feeds.
- CNC knee mill or retrofit manual mill.
- CNC vertical machining center, represented in the KB by `cnc_mill`.

## Build or open-source references

A usable milling machine is difficult but plausible to build locally once casting, precision machining, scraping/grinding, spindle bearing fitting, leadscrews, motor drives, and metrology exist. Critical subassemblies are:

- Rigid cast or welded base/column.
- Precision table and ways.
- Spindle head with high-quality bearings and tool taper.
- Feed screws or ballscrews.
- Motor, drive, belts/gears, and speed control.
- Workholding, vises, clamps, and cutting tools.
- Alignment and calibration with straightedges, indicators, squares, and test cuts.

The current BOM is directionally credible but light. It omits a machine column/base as an explicit large structural mass unless included in `milling_table`, and the imported compute module is unnecessary for a true manual mill.

## Related machine research

Related reports already present:

- `cnc_mill.md`
- `hydraulic_press.md`
- `inspection_tools_basic.md`
- `work_rest_adjustable.md`
- `saw_or_cutting_tool.md`
- `spinning_machine_v0.md`

The `cnc_mill.md` report already supports `cnc_mill` as the canonical milling machine and notes that `milling_machine_general_v0` is deprecated/consolidated. This report adds that a manual mill is real and may be useful as a separate lower-complexity tool if the KB wants a non-CNC machining stage.

## Recommendation for KB realism

Do not mark the concept unrealistic. Manual/general milling machines are real and foundational.

For the current KB, pick one of two coherent paths:

- If the self-reproducing set wants one canonical milling machine, finish consolidation into `cnc_mill` and update remaining process references away from `milling_machine_general_v0`.
- If the KB wants to distinguish manual and CNC capability, keep this item but rename it to `manual_milling_machine_v0` or `vertical_knee_mill_v0`, remove the deprecated note, clarify lower precision/automation than `cnc_mill`, and adjust mass/BOM for a realistic machine frame.

Because many active processes still reference it, the current state is inconsistent: deprecated in the item file but operationally required across machining workflows.

## Confidence and open questions

Confidence: high that the machine class is real; high that the KB has a consolidation inconsistency; medium on whether the intended model should keep manual and CNC milling separate.

Open questions:

- Should early self-reproduction include a manual mill before a CNC mill?
- Is 370 kg intended to represent a benchtop/light mill, or should the item represent a Bridgeport-class knee mill over 1000 kg?
- Are gear-cutting processes assumed to use this mill with indexing/dividing-head tooling?
- Should the imported compute module be removed if this remains a manual mill?
