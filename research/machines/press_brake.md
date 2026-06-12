# Press brake

## Machine identity

- KB ID: `press_brake`
- KB file: `kb/items/machines/press_brake.yaml`
- KB name: Press brake
- KB mass: 846 kg per unit
- Current KB role: sheet and plate bending machine for enclosures, ducts, motor housings, brackets, fastener fabrication, and general metal fabrication.

## KB usage and needed function

Local usage shows `press_brake` is an important but already dedupe-sensitive forming machine:

- It appears in the minimal/self-reproducing machine lists.
- It is required by `motor_housing_forming_v0`, `metal_forming_basic_shop_v0`, `fastener_kit_medium_production_v0`, `sheet_metal_forming_v0`, `welding_and_fabrication_v0`, and `metal_fabrication_welding_v0`.
- `press_brake_die_set` is modeled separately as hardened steel punch/die tooling.
- `docs/dedupe_decisions.md` says the plate rolling/press brake family was reviewed, with `press_brake` retained as a specialized sheet bending tool and `press_brake_or_roller` deprecated.
- `research/machines/steel_forming_press.md` notes that `press_brake` should remain distinct when precision straight bends or matched punch-and-die bending are required.

The needed function is controlled bending of sheet or plate stock along straight bend lines, using a punch and die. This is narrower than a generic hydraulic press, stamping press, or plate rolling mill.

## Reality classification

Classification: real practical machine.

A press brake is a standard metal fabrication machine. The KB's separation between the base machine and die set is realistic: commercial practice uses press-brake machines with interchangeable tooling, clamps, gauges, controls, and punches/dies. The KB mass is plausible for a light industrial or shop-built hydraulic press brake, though commercial units range from small benchtop/shop machines to multi-ton CNC machines.

## Evidence links

- Wilson Tool sells press brake punch, die, tooling, and clamping systems: https://wilsontool.com/en-us/solutions/bending
- The Fabricator describes press brake tool selection, including V-die openings relative to material thickness: https://www.thefabricator.com/thefabricator/article/bending/the-rules-of-press-brake-tool-selection
- G.E. Mathis describes press brake forming as forcing metal into a V-shaped die with a punch, distinct from roll forming: https://www.gemathis.com/press-brake-forming-vs-roll-forming/
- Full Spectrum Laser sells CNC hydraulic press brakes with welded steel frames, gooseneck punches, multi-V dies, safety curtains, hydraulic synchronization, and programmable axes: https://fslaser.com/products/cnc-press-brake-metal-bender
- Beckwood compares press brakes with sheet hydroforming and identifies press brakes as matched punch-and-die bending equipment: https://beckwoodpress.com/technology/press-brake-vs-sheet-hydroforming/

## Commercial alternatives

Commercial alternatives include:

- CNC hydraulic press brakes from machine tool vendors such as Amada, Trumpf, Accurpress, Cincinnati-style suppliers, Full Spectrum Laser, and similar manufacturers.
- Manual or hydraulic shop press-brake attachments for low-volume bends.
- Plate rolling mills for curved shells or cylinders.
- Stamping presses for high-volume repetitive forming.
- Sheet metal folders/brakes for lighter gauge manual work.

Under Conservative Mode, keep `press_brake` only where the straight-bend punch/die operation matters. Prefer `plate_rolling_mill`, `steel_forming_press`, or generic forming resources when the model only needs broad sheet forming capacity.

## Build or open-source references

- Instructables documents a 40-ton hydraulic press brake build, showing that low-volume shop-built machines are practical: https://www.instructables.com/Building-a-40-Ton-Hydraulic-Press-Brake-Machine/
- Hobby-machinist and shop forums discuss DIY press-brake tooling for hydraulic shop presses: https://www.hobby-machinist.com/threads/a-diy-press-brake-for-a-hydraulic-shop-press.7267/
- Commercial and DIY press-brake build plans exist for hydraulic shop-style machines; these are useful for rough manufacturability assumptions, but production accuracy depends heavily on frame stiffness, die quality, ram alignment, and bend allowance control.

## Related machine research

Related local report:

- `research/machines/steel_forming_press.md`

Related KB items:

- `press_brake_die_set`
- `plate_rolling_mill`
- `steel_forming_press`
- `stamping_press_basic`
- `hydraulic_press`
- `press_brake_or_roller` (deprecated/consolidated)

No follow-up tasks were enqueued, per task constraint.

## Recommendation for KB realism

Keep `press_brake` as a real practical machine, but continue treating it as a specialized forming resource.

Recommended cleanup when KB edits are allowed:

- Keep the item distinct from `plate_rolling_mill` for straight-line bending and matched punch/die work.
- Avoid using it as a catch-all forming press. For generic pressing, use a hydraulic/forming press; for curved plates, use a roller; for high-volume stamped parts, use a stamping press.
- Keep `press_brake_die_set` as a separate tooling part.
- Preserve the dedupe notes already present in KB documentation.
- Review the 846 kg mass only after choosing a target bend length and tonnage. It is plausible for a light industrial unit but too low for many full-size CNC press brakes and high for a small benchtop brake.

## Confidence and open questions

Confidence: high that the machine is real and that the KB function is plausible.

Open questions:

- What tonnage and bend length does the self-reproducing set need?
- Are the fastener and motor-housing processes actually straight-bend press-brake operations, or could some use a simpler manual brake/folder?
- Does the KB need one press brake size, or will future throughput/plate-thickness needs exceed the 5x reuse rule?
