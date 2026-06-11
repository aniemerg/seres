# Drill Press

## Machine identity

- KB ID: `drill_press`
- KB name: Drill press
- KB file: `kb/items/machines/drill_press.yaml`
- Current KB type: `machine`
- Current KB mass: 120 kg
- Current KB description: bench or floor drill press for precision hole drilling, with column, table, spindle, motor, and depth control.
- Current KB BOM: cast column/base, spindle head, small electric motor, T-slot table, depth stop, belt and pulley set.

## KB usage and needed function

The KB uses `drill_press` for:

- `drilling_basic_v0`
- `machining_process_drilling_v0`
- `pcb_fabrication_v0`
- `sheet_metal_fabrication_v0`
- `robot_wrist_fabrication_v0`
- `bom_part_fabrication_basic_v0`

The needed function is accurate vertical drilling of holes in metal, PCB stock, sheet, and fabricated components. It is a shop machine, not field drilling equipment.

## Reality classification

Classification: real practical machine.

Bench and floor drill presses are standard metalworking and fabrication machines. The KB BOM is realistic and matches commercial drill-press architecture: column/base, table, spindle/chuck, motor, belt/pulley or gear speed control, and depth stop. A 120 kg mass is plausible for a medium floor drill press; small benchtop units are lighter and industrial metalworking units can be heavier.

## Evidence links

- JET sells metalworking drill presses for commercial and maintenance operations, emphasizing depth control and precise spacing. Source: https://jettools.com/metalworking/drilling
- Home Depot's listing for a JET 20 in floor drill press gives a 282 lb product weight and features including adjustable depth stops, variable speeds, ball-bearing spindle, and belt/pulley cover. Source: https://www.homedepot.com/p/Jet-1-5-HP-20-in-Floor-Standing-Drill-Press-with-Worklight-12-Speed-115-230-Volt-JDP-20MF-354170/204059824
- BCcampus describes drill press parts including feed lever, spindle/chuck, drive mechanism, and adjustable depth stop. Source: https://pressbooks.bccampus.ca/woodworkingmachinery/chapter/parts-of-the-drill-press/
- USC's JET drill press SOP states that a drill press is used to drill holes in metal, wood, plastic, circuit boards, and similar materials. Source: https://viterbiundergrad.usc.edu/wp-content/uploads/2020/12/BFMS-SOP-JetDrillPress.pdf
- Grainger lists a JET floor drill press with chuck, column diameter, steel drilling capacity, spindle-to-table dimensions, spindle speeds, and T-slots. Source: https://www.grainger.com/product/JET-Floor-Drill-Press-Belt-45CA74
- Baileigh/related listing describes a floor-type drill press with 2 hp motor, drilling capacity in steel and cast iron, spindle speed range, and tapping feature. Source: https://www.machinetoolproducts.com/baileigh-industrial-variable-speed-drill-press-dp-1500vs-ba9-1002923

## Commercial alternatives

- Benchtop drill press.
- Floor drill press.
- Gear-head drill press.
- Magnetic drill for field/structural drilling.
- Mill-drill or milling machine for drilled and milled features.
- CNC mill or drilling center for high repeatability and pattern drilling.
- PCB drill/router for fine circuit-board holes.

## Build or open-source references

A basic drill press is locally buildable if the system can produce:

- Rigid column/base and table.
- Accurate spindle/quill or spindle head.
- Chuck or collet system.
- Motor, belt/pulley or gear drive.
- Return spring/feed handle and depth stop.
- Workholding, clamps, and guards.

Precision depends heavily on spindle runout, table perpendicularity, column stiffness, and workholding. Cutting tools are consumables and should be separate from the machine.

## Related machine research

Related reports already present:

- `drilling_equipment_v0.md`
- `cutting_tools_general.md`
- `cnc_mill.md`
- `milling_machine_general_v0.md`
- `pcb_fab_equipment.md`

`drilling_equipment_v0` should remain a field/mining drill system. `drill_press` is the shop drilling machine.

## Recommendation for KB realism

Keep as a real machine.

The current BOM and mass are realistic enough for a medium shop drill press. Recommended future cleanup is minor: ensure PCB drilling either uses this as a coarse manual drill press or a more precise PCB drill if hole sizes/tolerances require it. Keep field drilling separate under `drilling_equipment_v0`.

## Confidence and open questions

Confidence: high.

Open questions:

- Should `pcb_fabrication_v0` use a dedicated PCB drill/router for small vias?
- Should drill bits be modeled as `cutting_tools_general` consumables?
- Does the KB need a tapping-capable drill press or only drilling?
