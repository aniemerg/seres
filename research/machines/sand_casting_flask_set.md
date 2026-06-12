# Sand Casting Flask Set

## Machine identity

- KB ID: `sand_casting_flask_set`
- KB name: Sand casting flask set
- KB file: `kb/items/machines/sand_casting_flask_set.yaml`
- Current KB type: `machine`
- Current KB mass: 40 kg
- Current KB description: metal cope and drag flask frames for sand casting, in various sizes.

## KB usage and needed function

The KB uses this item as reusable foundry tooling for `sand_casting_medium_v0` and `sand_casting_large_v0`. It also appears as a component of `casting_mold_set` and in recipes for casting-dependent machinery such as `power_hammer_or_press_v0` and `tuyere_assembly`.

The needed function is to hold and align packed molding sand around a pattern during sand-casting mold preparation and pouring. It is not a powered machine; it is a reusable tool/set of frames.

## Reality classification

Classification: real practical tooling set, not a machine in the ordinary sense.

Sand casting flasks are standard foundry tooling. A flask normally has two principal sections: the cope and drag. These frames support molding sand, keep mold halves aligned, and allow the mold to be handled and poured. Metal flasks are realistic for repeated industrial use; wood or aluminum flasks are also common at small scale.

The KB's 40 kg mass is plausible for a set of steel flasks covering modest casting sizes. The current `kind: machine` is a schema/modeling convenience, but the real-world object is better described as reusable foundry tooling.

## Evidence links

- Fountain Foundry, "Molds and Cores": defines cope and drag as the top and bottom parts of a two-part casting flask and describes the flask as a wood or metal frame that contains and supports molding sand during pouring. Source: https://fountainfoundry.com/molds-and-cores
- U.S. Navy Foundry Manual, Part 2: states that a flask is made of cope and drag sections, with cheeks added for more complex or larger castings. Source: https://maritime.org/doc/foundry/part2.php
- MIFCO, "10 x 10 Sand Mold Steel Foundry Flask": commercial heavy-gauge steel cope-and-drag flask set. Source: https://mifco.com/shop/flasks/10-x-10-steel-flask-4in-cope-drag/
- Made-in-China foundry casting flask listing: describes sand boxes/flasks as tools for molding and transporting sand molds in manual and automatic molding lines. Source: https://qdhuaxingroup.en.made-in-china.com/product/fEsrbVuKHXRg/China-Foundry-Casting-Flask-Cope-and-Drag-for-Moulding-Line.html

## Commercial alternatives

- Heavy-gauge steel cope-and-drag flasks from foundry equipment suppliers such as MIFCO.
- Cast iron, aluminum, or steel jewelry/small-part flask sets.
- Custom welded steel flasks for larger foundry work.
- Wooden flasks for light-duty or low-temperature hobby foundry work.

## Build or open-source references

Sand casting flasks are among the simpler foundry tools to fabricate. Public build references include:

- Backyard Foundry guide to making a casting flask: https://www.backyard-foundry.com/how-to-make-a-flask-for-metal-casting.html
- Instructables, "Flask Making for Sand Casting Metals": https://www.instructables.com/Flask-Making-for-Sand-Casting-Metals/
- Myfordboy molding flask notes: https://myfordboy.blogspot.com/p/making-moulding-flasks.html

Simple versions can be made from wood, but a self-reproducing industrial system would likely prefer welded or cast/machined metal flasks for durability and dimensional stability.

## Related machine research

Related KB items:

- `casting_mold_set`
- `sand_casting_medium_v0`
- `sand_casting_large_v0`
- `prepared_mold`
- `permanent_mold_steel_set`
- `brick_mold_steel_set`

The local `docs/mold_migration_notes.md` warns that generic mold tooling can be physically inaccurate because molds are usually part-specific. A flask set is more reusable than a mold cavity, so it can remain generic more safely than `casting_mold_set`.

## Recommendation for KB realism

Keep the concept, but clarify it as reusable foundry tooling.

Recommended future KB wording: "Reusable cope/drag flask tooling for sand casting; not consumed by the process." If schema flexibility allows, this would be better as `kind: part` or `kind: tooling`, but under the current resource requirement model it is acceptable as a machine-like capacity provider.

Do not split by exact flask size yet. The 5x magnitude rule supports one generic flask set for coarse modeling, with size notes on specific casting recipes where needed.

## Confidence and open questions

Confidence: high that this is real practical foundry tooling and appropriate for sand casting.

Open questions:

- Should reusable tooling such as flasks remain `kind: machine`, or should the KB eventually add a tooling category?
- Should `casting_mold_set` be decomposed into reusable flask tooling plus part-specific molds/patterns?
- Is 40 kg intended to cover one medium steel flask or a family of several flask sizes?
