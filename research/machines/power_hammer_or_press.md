# Power Hammer Or Press

## Machine identity

- KB ID: `power_hammer_or_press`
- KB name: Power hammer or press
- KB file: `kb/items/machines/power_hammer_or_press.yaml`
- Current KB type: `machine`
- Current KB mass: 545 kg
- Current KB description: power hammer or mechanical press for hot forging and metal forming.

## KB usage and needed function

The KB uses this item in hot forging processes such as `forging_basic_v0`, `forging_bearing_ring_blanks_v0`, and `forging_rolls_basic_v0`. The required function is assisted hot deformation of steel billet/stock after heating in `induction_forge_v0`, with tooling support from `anvil_or_die_set`.

The BOM for `power_hammer_or_press` is hammer-like: frame, hammer head, drive motor, anvil block, controls, sensors, power conditioning, and fasteners. The item therefore appears to represent an assisted forging hammer more than a generic hydraulic metal-forming press.

## Reality classification

Classification: real practical machine category, but broad/ambiguous name.

Power hammers and forging presses are both real industrial forging machines. They are not identical: a power hammer delivers repeated impact blows, while a forging press applies controlled pressure. Both can form hot metal with dies, but they differ in force delivery, control, tooling, and suitability for different forging operations.

For the current KB, the item is acceptable as a conservative coarse abstraction for low-volume assisted hot forging. For realism, it should eventually be clarified as either a `forging_power_hammer` or a `forging_press`, depending on the intended process physics. The existing BOM favors `forging_power_hammer`.

## Evidence links

- The Crucible, "How To Use a Power Hammer": describes power hammers as mechanically powered forging instruments that raise and strike a hammer, serving the same basic purpose as manual hammering with greater efficiency and accuracy. Source: https://www.thecrucible.org/guides/blacksmithing/power-hammer/
- Anyang, "FP Power Hammer for Blacksmith": commercial self-contained pneumatic power hammers with tup sizes from 15 kg to 110 kg, intended for blacksmith forging. Source: https://www.anyanghammer.com/products/Blacksmith-Forging-Equipment/Blacksmith-Power-Hammer.html
- Big Blu, "Power Hammers": commercial blacksmith power hammer product line for metalworking shops. Source: https://secure.bigbluhammer.com/coreapp/equipment/power-hammers/big-blu-power-hammers
- Coal Iron Works, "Forging Machines": sells forging presses, induction forges, and self-contained power hammers, showing that hammers and presses are related but distinct shop forging machine categories. Source: https://coaliron.com/collections/forging-macines
- Ficep, "Hammer vs. Screw Press for Closed Die Forging": compares hammers and screw presses for closed-die forging, noting that both are accepted forging equipment choices with different efficiency and precision tradeoffs. Source: https://ficepgroup.com/en/hammer-vs-screw-press-for-closed-die-forging/

## Commercial alternatives

- Self-contained pneumatic power hammers from Anyang, Big Blu, and other blacksmith/forging equipment suppliers.
- Hydraulic forging presses from Coal Iron Works, Big Blu, and industrial press builders.
- Screw presses, mechanical forging presses, or hydraulic die-forging hammers for higher-throughput or more controlled closed-die forging.

For the KB's low-volume fabrication role, a small self-contained pneumatic hammer or compact hydraulic forging press is a realistic commercial analogue.

## Build or open-source references

Workshop-scale power hammers and forging presses are frequently shop-built. Public references include:

- Forum and maker build discussions for DIY power hammers and hydraulic presses, such as I Forge Iron power hammer build threads: https://www.iforgeiron.com/topic/63678-power-hammer-build/
- Public video build guides for homemade power hammers, for example "Building a DIY Power Hammer Machine": https://www.youtube.com/watch?v=9dQjpadr58k

These are not rigorous open-source industrial packages, but they show that small assisted forging machines can be fabricated from steel frame members, motor/drive components, bearings, springs or pneumatics, and anvil/die hardware. Safety guarding, foundation stiffness, controls, and die alignment remain serious requirements.

## Related machine research

Related local research:

- `research/machines/steel_forming_press.md` covers a hydraulic metal-forming press for sheet/shell forming. That should remain distinct from this item because the current `power_hammer_or_press` usage is hot forging.

Related KB items:

- `forging_press_v0`
- `hydraulic_press`
- `steel_forming_press`
- `anvil_or_die_set`
- `induction_forge_v0`
- `hammer_frame_basic`, `hammer_head_basic`, `anvil_block_basic`, and `hammer_drive_motor`

## Recommendation for KB realism

Keep for now, but rename or clarify.

Best recommendation: interpret the current item as `forging_power_hammer_basic` because the BOM includes a hammer frame, hammer head, drive motor, and anvil block. If the KB later needs sustained-pressure forging or closed-die press forging, model that separately as `forging_press_basic` or reuse an existing `hydraulic_press`/`forging_press_v0` after dedupe review.

Do not replace this with labor bot plus hand tools. Labor can handle setup, heating, and manipulation, but repeated impact or high forging force is the core machine function.

## Confidence and open questions

Confidence: high that the equipment category is real and relevant; medium that the current combined "hammer or press" ID is the cleanest KB abstraction.

Open questions:

- Should current forging processes require impact hammering specifically, or would a hydraulic forging press be more appropriate?
- Should `power_hammer_or_press_v0` references and recipes be migrated or fully deprecated in favor of `power_hammer_or_press`?
- Should `forging_press_v0`, `hydraulic_press`, and this item be consolidated into a clearer hierarchy of forming/forging equipment?
