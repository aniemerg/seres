# Steel forming press

## Machine identity

- KB ID: `steel_forming_press`
- KB name: Steel forming press
- KB file: `kb/items/machines/steel_forming_press.yaml`
- KB kind: `machine`
- Current KB mass: 670 kg
- Current KB structure: a hydraulic press-style assembly with frame, hydraulic cylinder, hydraulic system, press platens, power conditioning, controls, sensors, and fasteners.

## KB usage and needed function

The KB uses `steel_forming_press` as a capacity provider for forming steel sheet or shell stock:

- `kb/processes/steel_shell_thick_forming_v0.yaml` forms `steel_sheet_3mm` into `steel_shell_thick`.
- `kb/processes/sheet_metal_forming_process_v0.yaml` forms `steel_sheet_3mm` into `steel_chassis_sheet_metal`.
- `kb/processes/electrolysis_cell_unit_shell_fabrication_v0.yaml` fabricates a 25 kg electrolysis-cell shell from 3 mm steel sheet.

The BOM and recipe both model this as a hydraulic forming press assembled from press frame, cylinder, hydraulic power/control system, platens, controls, sensors, and fasteners. That matches the needed function: apply controlled force through tooling to bend, press, draw, stamp, or shape steel parts.

## Reality classification

Classification: real practical machine category.

`steel_forming_press` is not a single standardized product name, but it maps cleanly to a real class of industrial equipment: hydraulic or servo-hydraulic metal-forming presses, including stamping/forming presses and some press-brake-like use cases. The KB item is best interpreted as a generic hydraulic metal forming press, not as a specific model number.

It is not merely a placeholder. The local BOM components are credible for a basic press architecture, though the 670 kg mass implies a modest shop or light-industrial press rather than a large production press.

## Evidence links

- Macrodyne describes a metal forming press as a machine tool that shapes or cuts metal between a punch/ram and die/bolster, and notes that hydraulic metal-forming presses are widely used for manufacturing applications. Source: https://macrodynepress.com/general-metalforming-101/
- Beckwood lists custom hydraulic and servo-electric presses for metal forming, bending/straightening, draw forming, sheet hydroforming, punching/blanking, and stamping. Source: https://beckwoodpress.com/applications/general-forming-presses/
- Beckwood separately describes press brakes as using matched punch-and-die tooling to bend sheet material, which overlaps with part of the KB's sheet-forming use case but is narrower than a generic forming press. Source: https://beckwoodpress.com/technology/press-brake-vs-sheet-hydroforming/

## Commercial alternatives

Commercial alternatives include:

- Hydraulic metal forming press from industrial press builders such as Macrodyne or Beckwood.
- Press brake, if the required operation is primarily straight-line bending of sheet metal.
- Hydraulic shop press, if the required operation is low-volume pressing, straightening, simple forming, or fixture-based bending.
- Dedicated stamping press, deep-draw press, or hydroforming press if the final KB model needs a higher-throughput or more specialized forming operation.

For the current KB processes, the generic hydraulic forming press abstraction is acceptable because the modeled operations are coarse steel sheet and shell forming rather than a detailed production line.

## Build or open-source references

Open build references exist for small hydraulic shop presses, which supports local manufacturability of the simple end of this category:

- Instructables has an "Economy Hydraulic Shop Press" build guide: https://www.instructables.com/Economy-Hydraulic-Shop-Press/
- HomemadeTools.net documents a 20 ton hydraulic press build using structural steel and a bottle jack: https://www.homemadetools.net/forum/how-make-20-ton-hydraulic-press-99916

These are not equivalent to high-precision industrial forming presses, but they show that a basic press frame plus hydraulic actuator is practical to fabricate in a workshop. The KB's control module and sensor suite make the item more capable than a purely manual shop press.

## Related machine research

Related queue items likely overlap:

- `hydraulic_press`
- `press_brake`
- `press_brake_die_set`
- `stamping_press_basic`
- `molding_press`
- `forging_press_v0`
- `power_hammer_or_press`

Those should be kept distinct only where the process physics or tooling requirements differ. For general steel sheet/shell forming, `steel_forming_press`, `hydraulic_press`, `press_brake`, and `stamping_press_basic` may be candidates for consolidation or a clearer hierarchy.

## Recommendation for KB realism

Keep the item, but consider renaming or clarifying it as `hydraulic_metal_forming_press` or adding notes that `steel_forming_press` means a generic hydraulic metal-forming press.

Do not split it immediately for the current processes. The existing KB usage needs generic forming capacity, and the BOM is plausible. If later processes require precision straight bends, high-rate stamping, deep drawing, or hot forging, use more specific machines such as `press_brake`, `stamping_press_basic`, `deep_draw_press`, or `forging_press_v0`.

Recommended local note for future KB cleanup: "Generic hydraulic metal-forming press for low-volume bending/forming/stamping of steel sheet and shell parts; not a specific commercial model."

## Confidence and open questions

Confidence: high that the machine category is real and practical; medium that the 670 kg KB machine can cover all current steel shell and sheet-forming use cases.

Open questions:

- Is the intended operation mostly press-brake bending, stamping, deep drawing, straightening, or general shop pressing?
- Should `steel_forming_press` be consolidated with `hydraulic_press` or kept as the steel/sheet-focused capacity provider?
- Are the current `qty` units in `resource_requirements` meant to represent count, unit, or machine-hours? The three processes currently use both `count` and `unit`.
