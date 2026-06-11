# Casting Mold Set Machine Reality Research

## Machine identity

- KB machine id: `casting_mold_set`
- KB name: Casting mold set
- KB file: `kb/items/machines/casting_mold_set.yaml`
- Current KB mass: 100 kg
- Current BOM: `bom_casting_mold_set_v0`
- Current recipe: `recipe_casting_mold_set_v0`

## KB usage and needed function

The item is broadly used by metal casting, sand casting, mold preparation, ingot casting, glass casting, motor housing casting, machine frame casting, stainless/tool steel casting, and other foundry processes.

The needed function is reusable foundry tooling: flasks/boxes, pattern equipment, gates/risers tooling, and sometimes permanent metal molds. However, the actual mold cavity is usually part-specific. A generic mold set can provide reusable infrastructure, but it cannot realistically contain finished reusable molds for every future casting geometry.

## Reality classification

Real practical tooling set, not a standalone machine.

The item is realistic if interpreted as a foundry mold tooling kit: sand-casting flasks, pattern plates, core boxes, simple ingot molds, and a few reusable permanent molds. It is less realistic if interpreted as a universal set of reusable molds for arbitrary parts.

## Evidence links

- U.S. Navy Foundry Manual describes sand molds made by shaping sand around a pattern inside a flask, then removing the pattern to leave the mold cavity: <https://maritime.org/doc/foundry/part2.php>
- Badger Alloys explains that sand-casting molds are made by packing sand around a pattern and removing the pattern, reinforcing that patterns/molds are part-specific: <https://badgeralloys.com/news/foundry-101-understanding-molds-and-cores-in-the-sand-casting-process/>
- Xometry describes permanent mold casting as using reusable steel or cast-iron two-part molds, mainly for repeatable casting of lower-melting metals such as aluminum: <https://www.xometry.com/resources/casting/permanent-mold-casting/>
- DEECO Metals describes permanent mold/gravity casting as a reusable-mold process for higher-volume uniform parts: <https://www.deecometals.com/custom-castings-permanent-mold>

## Commercial alternatives

- Sand-casting flask set plus patterns and molding sand: flexible, low-cost, good for low-volume and large parts.
- Permanent steel/iron mold set: reusable, more precise, but part-specific and higher upfront fabrication cost.
- Ingot molds: simple reusable molds for bars, pigs, and billets.
- Investment casting tooling: wax pattern tooling and ceramic shell workflow for complex precision parts.
- 3D-printed sand molds or patterns: useful for one-off or low-volume complex castings.

## Build or open-source references

Reusable flasks, pattern boards, core boxes, and simple ingot molds can be locally built from wood, steel, cast iron, or machined metal. Permanent molds require more precise design, machining, vents/gates, coatings, thermal management, draft, ejectors, and allowance for shrinkage.

The KB recipe is plausible for a starter mold toolkit if it includes flasks and pattern equipment. It should not be read as a complete set of every mold cavity needed for all cast parts.

## Related machine research

Related local reports:

- `research/machines/sand_casting_flask_set.md`
- `research/machines/casting_furnace_v0.md`
- `research/machines/dies.md`
- `research/machines/press_brake_die_set.md`

The existing `sand_casting_flask_set` report notes that flasks are safely generic, while mold cavities and patterns are usually part-specific.

## Recommendation for KB realism

Keep the item as foundry tooling, but narrow its meaning.

Recommended options:

- Treat `casting_mold_set` as a generic foundry mold tooling kit, not a universal set of molds for all geometries.
- Keep `sand_casting_flask_set` separate as reusable sand-casting support equipment.
- Add part-specific patterns/molds only when a casting process depends on a dedicated geometry, such as motor housings, machine frames, or complex fluid parts.
- Consider splitting `ingot_mold_set`, `sand_casting_pattern_set`, and `permanent_mold_set` if process realism requires it.
- If schema support allows, classify as tooling/part set rather than powered machine.

## Confidence and open questions

Confidence: high that casting molds/flasks/pattern tooling are real; medium that one generic 100 kg set can cover the current wide range of casting processes without hiding part-specific tooling.

Open questions:

- Which current casting processes need only generic flasks and patterns, and which need dedicated permanent molds?
- Should `casting_mold_set` include consumable sand/binder or only reusable frames/patterns?
- Should glass casting and metal casting share one mold set, or require material-specific mold tooling?
