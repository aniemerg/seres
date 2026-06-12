# Metal forming basic v0

## Machine identity

- Queue item: `machine_reality_metal_forming_basic_v0`
- KB ID: `metal_forming_basic_v0`
- KB file: `kb/items/machines/metal_forming_basic_v0.yaml`
- KB name: blank in imported-machine list
- KB kind: `machine`
- KB modeled mass: 1102 kg

The KB item represents a basic metal forming equipment set. Its BOM combines a heavy frame, hydraulic cylinders, hydraulic pump, press frame, roller set, drive motor, anvil block, fixture mounting plates, control panel, and fasteners. The item notes explicitly call it a "press/roll/fixture" set.

## KB usage and needed function

`metal_forming_basic_v0` is used both as a machine and as a process ID, which makes the imported-machine-list identity ambiguous.

As a machine, it is referenced by processes including:

- `frame_fabrication_basic_v0`
- `part_fabrication_basic_v0`
- `ventilation_hood_fabrication_v0`
- `tape_drive_mechanism_fabrication_v0`

As a process, it appears in many recipes for formed parts, sheet metal, jackets, mounts, drums, pressure vessels, vacuum chambers, springs, and related fabricated components.

The needed function is general low-volume metal forming: pressing, bending, rolling, fixture-supported forming, and possibly light forging or anvil work. It is not one exact commercial machine.

## Reality classification

Classification: generic equipment set / placeholder bundle made from real machines.

The functions are real, but `metal_forming_basic_v0` is not a standard machine category like "press brake", "hydraulic press", "plate rolling mill", or "power hammer". It is a coarse KB abstraction bundling several real capabilities into one machine item. That can be acceptable for early closure, but for imported-machine realism it should be treated as a shop forming cell or equipment set rather than a single practical machine.

The 1102 kg mass is plausible for a small combined shop cell with a hydraulic press, rollers, fixtures, anvil block, and controls. It is not a reliable proxy for capability because forming capacity depends on tonnage, roll width/diameter, frame stiffness, tooling, and material thickness.

## Evidence links

- OSHA SIC 3542, machine tools, metal forming types: https://www.osha.gov/sic-manual/3542
  - Lists many metal forming machine types, including arbor presses, bending/forming machines, brakes, die-casting machines, drop hammers, forging machinery, headers, and other forming tools.
  - Supports the idea that "metal forming" is a broad industrial class, not one specific machine.

- Japan Forming Machinery Association overview: https://www.j-fma.or.jp/pen/4tan/tanatsukikai.html
  - Distinguishes press brakes, bending machines, bending rolls, pipe benders, shearing machines, punching presses, laser/plasma cutting, and other sheet-metal processing machines.
  - This supports splitting specific functions when the KB needs realism.

- G.E. Mathis, press brake forming vs. roll forming: https://www.gemathis.com/press-brake-forming-vs-roll-forming/
  - Explains that press brakes and roll forming machines can both bend metal but have different properties, benefits, and applications.
  - Press brake forming uses a punch and V-shaped die; roll forming uses rolling equipment for different production needs.

- Metal Supermarkets, metal forming processes: https://www.metalsupermarkets.com/metal-forming-processes-explained-comprehensive-guide-to-techniques-and-applications/
  - Describes rolling as a forming operation for plate, sheet, and sections, including round tanks and vessels.
  - Notes multiple rolling machine types depending on sheet width and tube/bar/angle/flat profiles.

- Existing local research reports:
  - `research/machines/hydraulic_press.md`
  - `research/machines/press_brake.md`
  - `research/machines/plate_rolling_mill.md`
  - `research/machines/power_hammer_or_press.md`

These local reports document real specific machines that overlap with this generic bundle.

## Commercial alternatives

Real commercial alternatives depend on the exact forming operation:

- Hydraulic press: general pressing, straightening, bearing installation, compaction, and simple forming with tooling.
- Press brake: straight-line sheet/plate bending with punch and die.
- Plate rolling mill or plate roll/bending machine: flat rolling/reduction or cylindrical/conical shell forming, depending on the intended operation.
- Power hammer or forging press: hot forging and impact/press forging.
- English wheel, bead roller, slip roll, shear/brake/roll combination machine: lighter sheet metal shaping.
- Stamping press: high-volume repetitive sheet forming/punching.

`metal_forming_basic_v0` is best understood as a low-volume shop cell containing several of these functions, not as a substitute for a high-throughput production line.

## Build or open-source references

The component machines have common DIY/shop-build precedents: shop hydraulic presses, simple press-brake tooling, plate/slip rolls, anvils, fixture plates, and small power hammers. However, combining them into one 1102 kg "metal forming basic" machine is a KB modeling abstraction.

For build realism, the KB should model structural frame stiffness, hydraulic components, hardened dies/rollers, bearings, alignment, guards, and interchangeable fixtures. Labor bots plus fixtures can handle some setup and low-force forming, but high-force pressing/rolling requires actual machinery.

## Related machine research

Existing related reports:

- `research/machines/hydraulic_press.md`
- `research/machines/press_brake.md`
- `research/machines/plate_rolling_mill.md`
- `research/machines/power_hammer_or_press.md`
- `research/machines/steel_forming_press.md`
- `research/machines/spinning_machine_v0.md`

These should be used as more specific references if imported-machine realism cleanup proceeds.

## Recommendation for KB realism

Recommendation: mark as a generic forming equipment set or replace with specific machines where possible.

Specific recommendation:

- Do not treat `metal_forming_basic_v0` as a fake machine; it represents real shop capabilities.
- Do treat it as a generic bundle, not a standard purchasable machine.
- Give it a display name such as "Basic metal forming equipment set" if future edits are allowed.
- Prefer specific existing machines when the process tells you the actual operation:
  - `hydraulic_press` for pressing/compaction/straightening
  - `press_brake` for straight-line sheet bending
  - `plate_rolling_mill` or a plate roll for rolling operations
  - `power_hammer_or_press` for hot forging
- Keep this item only as a conservative catch-all for low-volume miscellaneous forming where the exact forming mode is not worth modeling.
- Review process/item ID collision risk: `metal_forming_basic_v0` exists as both a machine item and process ID. That may be intentional in this KB, but it can confuse imported-machine analysis.

## Confidence and open questions

Confidence: high that the underlying capabilities are real; high that the current item is a generic equipment-set abstraction rather than a single machine.

Open questions:

- Should `metal_forming_basic_v0` remain in the minimal self-reproducing machine list, or should it be replaced by specific items already researched?
- Which process references actually require rolling, which require pressing, and which could use labor bot plus fixtures?
- Does the KB need a single "forming cell" abstraction for scheduling/capacity, separate from the component machines?

