# Work Rest Adjustable

## Machine identity

- KB ID: `work_rest_adjustable`
- KB name: Work rest (adjustable)
- KB file: `kb/items/parts/work_rest_adjustable.yaml`
- Current KB type: `machine`
- Current KB mass: 10 kg
- Current KB description: adjustable support for workpieces during grinding or turning, with height and position adjustment to reduce deflection.

## KB usage and needed function

The KB uses `work_rest_adjustable` as a component of:

- `bom_bench_grinder`
- `bom_polishing_station_v0`
- `recipe_machine_bench_grinder_v0`
- `recipe_polishing_station_v0`

It is also listed as a required machine for `grinding_and_finishing_v0`, and appears in the self-reproducing machine list.

The needed function is local support and controlled positioning of a workpiece or tool near a grinder/polisher wheel, or support of a long rotating workpiece during machining. In the current KB, the strongest usage is grinder/polisher work support. The notes also mention lathes, but a lathe support is usually called a steady rest or follow rest, not simply a grinder work rest.

## Reality classification

Classification: real practical accessory/tooling item, not a standalone powered machine.

Adjustable work rests are required/standard accessories on bench and pedestal grinders and common accessories on belt grinders, disk grinders, and polishing stations. They are also a safety feature because the gap to the grinding wheel must stay small as the wheel wears.

The KB item is realistic as a reusable machined/fabricated steel accessory. The 10 kg mass is plausible for a heavy adjustable rest, especially for a polishing or grinding station. However, the item should probably be modeled as a part/tooling accessory rather than as an independent machine. If it is meant for lathe workpiece support, it should be renamed or split into `steady_rest_adjustable` or `follow_rest_adjustable`.

## Evidence links

- OSHA 29 CFR 1910.215 states that offhand grinding machines must use rigid, adjustable work rests kept close to the wheel and securely clamped after adjustment. Source: https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.215
- OSHA 1926.303 similarly requires floor and bench-mounted grinders to have rigid, readily adjustable work rests. Source: https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.303
- Beaumont Metal Works sells an adjustable work rest for a horizontal disk grinder, with quick-action levers, removable table, tilt, in-out, and up-down adjustment, made from steel. Source: https://beaumontmetalworks.com/product/adjustable-work-rest-for-disk-grinder/
- Home Depot lists adjustable bench grinder tool rests for 6 in. and 8 in. grinders with height and angle adjustment. Source: https://www.homedepot.com/p/SKYSHALO-Adjustable-Bench-Grinder-Tool-Rest-for-6-in-or-8-in-with-Miter-Slide-for-0-2-5-in-Blades-and-Chisels-Replacement-Jig-MCZSJJ090000FZ9D1001V0-SK0428/336113110
- Kitagawa describes steady rests as supports for long or flexible workpieces in turning, grinding, and milling to reduce deflection and vibration. Source: https://kitagawa.global/en/products/steady-rests
- LeBlond describes lathe steady rests as supports for long, slender workpieces during turning or machining. Source: https://leblondusa.com/what-are-lathe-steady-rests/

## Commercial alternatives

- Stock grinder work rest built into a bench grinder.
- Aftermarket adjustable grinder tool rest or sharpening jig.
- Disk grinder or belt grinder adjustable table/rest.
- Centerless grinder work-rest blade and support assembly.
- Lathe steady rest or follow rest for long shaft work.

These alternatives are not all interchangeable. A bench grinder work rest supports offhand grinding near an abrasive wheel; a lathe steady rest supports a rotating cylindrical workpiece from multiple points.

## Build or open-source references

This item is locally buildable with ordinary shop processes:

- Steel or cast iron base.
- Slotted adjustment bracket or dovetail/slide.
- Pivoting or tilting table/arm.
- Locking screws, clamps, or cam levers.
- Hardened or replaceable contact surface where wear matters.

Public workshop examples commonly show replacement bench-grinder rests fabricated from steel plate, bar, slots, and locking knobs. Precision matters mainly for rigidity, repeatable angle setting, and the ability to hold adjustment under vibration.

## Related machine research

Related reports already present:

- `bench_grinder` is not present as a report, but `work_rest_adjustable` is a BOM component of the bench grinder.
- `polishing_station_v0` is not present as a report, but this item is a component.
- `hand_tools_basic.md`
- `saw_or_cutting_tool.md`
- `tension_gauge.md`
- `metal_forming_basic_v0.md`

Related KB items:

- `lathe_carriage_simple`
- `lathe_tool_post_basic`
- `bench_grinder`
- `polishing_station_v0`

## Recommendation for KB realism

Keep the concept, but treat it as a tooling/accessory component rather than an independent machine.

Recommended KB realism change for later work: keep the current ID if it is specifically a grinder/polisher rest, and revise wording to "adjustable grinder/polisher work rest." If the lathe-support function is important, split a separate `steady_rest_adjustable` item for turning and cylindrical grinding. Do not merge this into labor-bot tooling because it is a physical safety and accuracy component, not just an operator action.

The current imported-machine list should not imply this is a complex imported machine. It is a small fabricated accessory that can likely be locally made once basic machining and fastening are available.

## Confidence and open questions

Confidence: high that adjustable work rests are real and relevant; high that the KB item is over-classified as a machine; medium on whether the intended scope includes lathe steady rests.

Open questions:

- Is the KB item meant only for grinders/polishers, or also for lathe steady/follow rests?
- Should `grinding_and_finishing_v0` require the bench grinder/polisher and list the work rest as tooling rather than a separate machine?
- Should the BOM use replaceable contact plates or wear strips?
