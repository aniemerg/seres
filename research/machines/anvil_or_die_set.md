# Anvil Or Die Set

## Machine identity

- KB ID: `anvil_or_die_set`
- KB name: Anvil or die set
- KB file: `kb/items/parts/anvil_or_die_set.yaml`
- Current KB type: `machine`
- Current KB mass: 25 kg
- Current KB capabilities: `forging_support`, `die_set_forming`
- Current KB description: anvil/die set for press/forging.

## KB usage and needed function

The KB uses `anvil_or_die_set` for:

- `forging_basic_v0`
- `forging_bearing_ring_blanks_v0`
- `forging_rolls_basic_v0`

It pairs with `induction_forge_v0` and `power_hammer_or_press` in forging workflows. The needed function is passive forging tooling: hardened surfaces, bottom dies, top dies, swages, fullers, V-dies, flat dies, or anvil tooling that shape hot metal under hammer or press force.

## Reality classification

Classification: real practical tooling set, not a standalone machine.

Anvils, forging dies, and hammer/press die sets are standard forging tooling. They do not provide heat or force by themselves. They need a hammer, press, hand hammer, or power hammer plus a heated workpiece.

The KB's 25 kg mass is plausible for a small die/tooling set or compact anvil/tool set, but low for a primary blacksmith anvil or industrial power-hammer dies plus anvil block. There is also a near-duplicate `anvil_and_die_set` and a separate `anvil_block_basic`.

## Evidence links

- Scot Forge describes open-die forging as shaping heated metal between a top die attached to a ram and a bottom die attached to a hammer, anvil, or bolster. Source: https://www.scotforge.com/customized-solutions/why-forging-1/advantages-of-forgings-forging-processes/open-die-forging-advantages
- Canton Drop Forge explains open-die forging as striking or pressing metal on a stationary anvil or between simple dies, with simple die shapes such as flat, semi-round, and V-shaped. Source: https://cantondropforge.com/open-vs-closed-die-forging/
- TFG USA describes open-die forging as shaping hot metal between flat or contoured dies using repeated hammer or press forces. Source: https://www.tfgusa.com/what-is-open-die-forging/
- Milwaukee Forge describes open-die forging as shaping metal by hammering or pressing it between flat or simple contour dies. Source: https://www.milwaukeeforge.com/difference-between-open-die-and-closed-die-forging/
- Big BLU sells commercial power hammer die sets with crowned drawing surfaces and fuller surfaces. Source: https://secure.bigbluhammer.com/coreapp/equipment/power-hammers/power-hammer-dies/sets
- Trick Tools sells power hammer dies for ProLine, Dake, and Pullmax-style machines, supporting commercial availability of interchangeable forming tooling. Source: https://www.trick-tools.com/tools/Power-Hammer-Dies

## Commercial alternatives

- Blacksmith anvil.
- Hardy tools, fullers, swages, bending tools, and cut-off tools.
- Power hammer die set.
- Hydraulic forging press dies.
- Open-die flat and V-die tooling.
- Closed/impression forging dies for specific parts.
- Separate `anvil_block_basic` for the heavy fixed anvil mass.

## Build or open-source references

Simple forging tooling can be locally made from medium/high-carbon steel or tool steel:

- Forge or machine die blanks.
- Heat treat and temper working faces for impact resistance.
- Grind faces flat or to required contours.
- Add mounting features for hammer/press slots, wedges, dovetails, or hardy holes.

Closed dies and precision impression dies are harder because they need cavity design, die steel, heat treatment, precision machining, and wear allowances.

The current KB recipe is suspect because it uses forging processes that already require `anvil_or_die_set` to produce `anvil_or_die_set`. A more realistic seed route would cast or machine a simple anvil/die from steel stock, then heat treat and grind it.

## Related machine research

Related reports already present:

- `power_hammer_or_press.md`
- `induction_forge_v0.md`
- `forging_press_v0.md`
- `metal_forming_basic_v0.md`
- `dies.md`
- `press_brake_die_set.md`

Related KB items:

- `anvil_and_die_set`
- `anvil_block_basic`
- `hammer_head_basic`
- `pressing_mold_set`

## Recommendation for KB realism

Keep the concept, but reclassify as tooling and deduplicate.

Recommended future cleanup:

- Decide whether `anvil_or_die_set` and `anvil_and_die_set` are the same item.
- Keep `anvil_block_basic` for the heavy fixed anvil block if needed.
- Model this item as interchangeable forging tooling, not a machine.
- Replace the current self-referential forging route with cast/machined/heat-treated tooling production.

Do not remove it from forging processes; forging needs tooling. But do not count it as a powered imported machine.

## Confidence and open questions

Confidence: high that the item is real and useful; high that it is tooling rather than a machine; medium on the correct mass and dedupe target.

Open questions:

- Should this be a small general hand-forging tool set or power-hammer/press dies?
- Should the heavy anvil mass be `anvil_block_basic` while this item is only interchangeable dies?
- Which forging processes require closed/impression dies rather than open-die tooling?
