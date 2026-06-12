# CNC Mill

## Machine identity

- KB ID: `cnc_mill`
- KB name: CNC Milling Machine
- KB file: `kb/items/machines/cnc_mill.yaml`
- Current KB type: `machine`
- Current KB mass: 785 kg
- Current KB description: consolidated CNC milling machine with 3-axis or multi-axis motion control, spindle speeds up to 10,000+ RPM, CNC controller, servo motors, and tool changer.

## KB usage and needed function

The KB uses `cnc_mill` for `machining_basic_v0`, `machining_process_milling_v0`, `machining_precision_v0`, `mechanical_stage_xy_fabrication_v0`, and `substrate_preparation_basic_v0`. It is also listed in the minimal self-reproducing set as the precision milling resource.

Local dedupe notes already identify `cnc_mill` as the canonical milling machine and consolidate `milling_machine_general_v0` into it. That is consistent with the conservative-mode preference for reuse.

The needed function is subtractive machining with a rotating cutter and controlled workpiece/tool motion, including precision surfaces, slots, bores, enclosures, stages, fixtures, and machine components.

## Reality classification

Classification: real practical machine.

CNC mills and vertical machining centers are standard industrial and shop equipment. The KB description fits a compact CNC mill or small vertical machining center. The 785 kg mass is plausible for a serious compact mill, but lower than many enclosed commercial vertical machining centers and higher than small desktop CNC mills.

This is not a placeholder. It is a high-value enabling machine for local manufacturing and precision work.

## Evidence links

- Haas Automation, "Mini Mills": describes compact CNC machining centers with 3/4/5 axis configurations, 6,000-15,000 RPM spindles, and 10-31 tool capacity, matching the KB's compact CNC mill concept. Source: https://www.haascnc.com/machines/vertical-mills/mini-mills.html
- Haas, "Mini Mill": lists a compact 40-taper vertical machining center with 3 axes, 10k RPM spindle in some variants, and automatic tool changer options. Source: https://www.haascnc.com/machines/vertical-mills/mini-mills/models/minimill.html
- Tormach, "PCNC 440 CNC Mill": commercial compact CNC mill with about 600 lb system weight, showing the low end of real CNC mill mass and footprint. Source: https://tormach.com/machines/mills/pcnc-440.html
- Tormach technical specifications: lists PCNC 440 travel, table capacity, and typical system weight. Source: https://tormach.com/support/mill/pcnc-440-technical-specifications
- Haas VF series price/spec list: shows larger 3-axis CNC vertical mills with 30 x 16 x 20 inch travels, 8.1k RPM spindle, and 20-tool capacity, illustrating the production VMC class above the KB item. Source: https://www.haascnc.com/shop/category/pricelist.html

## Commercial alternatives

- Compact CNC mills: Tormach PCNC 440/770/1100 class.
- Small vertical machining centers: Haas Mini Mill, Haas Super Mini Mill, similar compact VMCs from other builders.
- Larger production VMCs: Haas VF series and equivalents.
- CNC routers or gantry mills for softer materials and large sheets, but these should not replace a metalworking CNC mill where rigidity and precision are required.

## Build or open-source references

DIY/open-source CNC machines exist, but most are closer to routers or light mills than full industrial metalworking VMCs.

Examples:

- PrintNC is a community-supported steel-frame DIY CNC router/mill project often used for aluminum and light-duty work. Source: https://wiki.printnc.info/
- OpenBuilds hosts many open CNC builds and controller patterns. Source: https://builds.openbuilds.com/
- MIT Center for Bits and Atoms historically published low-cost CNC concepts such as MTM Snap, but these are far below industrial VMC capability.

The KB recipe should treat locally building a CNC mill as difficult but plausible if precision linear rails, ballscrews, spindle, controller, motors, and measurement/calibration equipment are available. The hardest parts are stiffness, precision alignment, spindle/tooling quality, controls, and metrology.

## Related machine research

Related KB items:

- `milling_machine_general_v0` is deprecated/consolidated into `cnc_mill`.
- `precision_lathe` or other lathe entries should remain separate because turning and milling are different operations.
- `surface_grinder`, `bench_grinder`, and other finishing tools should remain separate from milling.
- `coordinate_measuring_machine` and metrology tools are important complements for precision CNC work.

## Recommendation for KB realism

Keep `cnc_mill` as the canonical milling machine.

The current ID is realistic and correctly useful. Consider documenting the mass as compact-shop scale, not a full production machining center. Do not split by 3-axis versus 5-axis yet; the KB can use process notes or capability tags unless a specific process requires true 5-axis simultaneous machining.

Do not replace precision milling with labor bot plus hand tools. Labor can load, fixture, and inspect parts, but CNC milling is the machine capability that provides repeatable precision, tool motion, spindle power, and controlled feeds.

## Confidence and open questions

Confidence: high that this is a real practical machine and a good canonical KB item.

Open questions:

- Should the 785 kg mass be revised upward if the KB expects a fully enclosed VMC with tool changer and coolant?
- Should the capabilities distinguish rough milling, precision milling, and multi-axis machining?
- How should the KB represent consumables such as cutting tools, coolant, workholding, and calibration artifacts?
