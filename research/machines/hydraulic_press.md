# Hydraulic press

## Machine identity

- KB ID: `hydraulic_press`
- KB file: `kb/items/machines/hydraulic_press.yaml`
- KB name: Hydraulic press
- KB mass: 600 kg per unit
- Current KB role: canonical general-purpose press for forming, compaction, bearing installation, pressing, straightening, and shop operations.

## KB usage and needed function

Local usage shows `hydraulic_press` is already the consolidated general press:

- It is listed in the minimal/self-reproducing machine set.
- It is used by pressing, forming, ceramic compaction, sintering prep, bearing installation, metal forming, NiFe electrode fabrication, and insulation panel forming processes.
- `docs/dedupe_decisions.md` explicitly keeps `hydraulic_press` as the primary general-purpose press and consolidates `hydraulic_press_small`, `press_hydraulic`, `power_hammer_or_press_v0`, and `pressing_tools` into it.
- Related research reports for `steel_forming_press` and `power_hammer_or_press` note overlap but preserve separate roles where mechanics differ.

The needed function is controlled high-force linear pressing using hydraulic actuation and platens or tooling.

## Reality classification

Classification: real practical machine.

Hydraulic presses are commodity shop and industrial machines. The KB's 600 kg mass is plausible for a medium shop/industrial H-frame or C-frame press, not for a small benchtop bottle-jack press or a massive production press. The item is realistic as a shared capacity provider for low-to-medium throughput pressing tasks.

## Evidence links

- Northern Tool's 20-ton hydraulic shop press manual describes pressing, bending, straightening, and forming uses in industrial repair shops: https://assets.northerntool.com/products/891/documents/manuals/89156.pdf
- Black Widow's 20-ton shop press includes a steel frame, pressure gauge, manual/air-over-hydraulic operation, adjustable table, and heel blocks: https://www.blackwidowpro.com/motorcycle/service-equipment/20-ton-air-op-press/p/bd-press-20a/
- NovoTech describes hydraulic shop presses for assembly, straightening, testing, and pressing bearings in/out: https://novotechmachinetools.com/hydraulic-press.html
- TMG Industrial describes hydraulic shop presses for controlled high-pressure force, bearing installation, bushing removal, gear pressing, and metal forming: https://www.tmgindustrial.com/collections/hydraulic-shop-presses
- Passca describes hydraulic presses for removing/installing bearings, gears, bushings, and ball joints, with adjustable work height and heavy-duty steel construction: https://www.passca.com/hydraulic-press/

## Commercial alternatives

Commercial alternatives include:

- 10-50 ton H-frame shop presses.
- Powered industrial hydraulic presses with electric hydraulic pumps.
- Arbor presses or toggle presses for smaller forces.
- Press brakes for sheet bending along straight lines.
- Stamping presses for high-volume repetitive forming.
- Forging presses or power hammers for hot forging.
- Dedicated ceramic/powder compaction presses for controlled pressure profiles.

The KB's `hydraulic_press` is a good conservative default for general pressing. More specific machines should only be used where they change the process physics, throughput, tooling, or tolerances.

## Build or open-source references

- HomemadeTools documents a 20-ton hydraulic press build using structural steel and a bottle jack: https://www.homemadetools.net/forum/how-make-20-ton-hydraulic-press-99916
- Instructables hosts instructions for building a small benchtop 20-ton hydraulic press from steel frame components and a bottle jack: https://content.instructables.com/FBZ/DUHW/KDD3JSDM/FBZDUHWKDD3JSDM.pdf
- Home Model Engine Machinist discussion documents a DIY shop press made from an old hydraulic jack and scrap/rest material: https://www.homemodelenginemachinist.com/threads/diy-hydraulic-shop-press.35098/

These support local manufacturability at shop scale. High-reliability industrial presses still require careful frame design, weld quality, hydraulic seals, pressure gauges, guarding, and overload safety.

## Related machine research

Related local reports:

- `research/machines/steel_forming_press.md`
- `research/machines/power_hammer_or_press.md`
- `research/machines/press_brake.md`

Related KB items:

- `hydraulic_press_small` (deprecated/consolidated)
- `press_hydraulic` (deprecated/consolidated)
- `pressing_mold_set`
- `press_platen_set_medium`
- `press_cylinder_medium`
- `steel_forming_press`
- `press_brake`
- `stamping_press_basic`
- `regolith_brick_press_hydraulic_v0`

No follow-up tasks were enqueued, per task constraint.

## Recommendation for KB realism

Keep `hydraulic_press` as the canonical general-purpose press.

Recommended cleanup when KB edits are allowed:

- Preserve the existing dedupe decision that consolidates smaller generic presses into this item.
- Keep it distinct from `press_brake`, `stamping_press_basic`, and forging equipment only when those specific mechanics matter.
- Document approximate capacity/tonnage if known; current mass alone does not define capability.
- Keep tooling/mold sets separate from the press frame and hydraulic system.
- Treat bearing installation and general compaction as appropriate uses.

## Confidence and open questions

Confidence: high that the machine is real and that the KB consolidation is sensible.

Open questions:

- What tonnage and daylight/stroke does the self-reproducing set require?
- Should ceramic/powder compaction use the same press with different tooling or a dedicated controlled compaction press?
- Are hydraulic fluid, seals, hoses, gauges, and safety guarding modeled adequately?
