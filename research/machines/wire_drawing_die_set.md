# Wire Drawing Die Set Machine Reality Research

## Machine identity

- KB item id: `wire_drawing_die_set`
- KB name: Wire drawing die set
- KB file: `kb/items/parts/wire_drawing_die_set.yaml`
- Current KB kind: `machine`
- Current KB mass: 2 kg
- Current BOM: `bom_wire_drawing_die_set`
- Current recipe: `recipe_wire_drawing_die_set_v0`

## KB usage and needed function

The item is used by `wire_drawing_aluminum_v0`. Most other wire drawing processes use `drawing_die_set_basic` instead.

The needed function is passive precision tooling: a die or set of dies with hardened/polished openings that reduce wire diameter as a draw bench, capstan, or other pulling machine draws wire through them. The die set alone is not an active machine and does not provide pulling force, lubrication, cooling, payoff, or take-up.

## Reality classification

Real practical tooling set, likely duplicate or near-duplicate of `drawing_die_set_basic`.

Wire drawing die sets are standard industrial tooling. The current 2 kg mass is plausible for a small die set, especially for aluminum/copper or bench-scale use. The main issue is naming and duplication: `wire_drawing_die_set` and `drawing_die_set_basic` represent the same basic function in current KB usage.

## Evidence links

Evidence already collected in `research/machines/drawing_die_set_basic.md` applies directly:

- Hyperion Materials & Technologies manufactures PCD, cemented carbide, and diamond composite wire drawing dies and blanks: <https://www.hyperionmt.com/en/products/Wire-Dies/>
- Esteves Group describes wire drawing dies as precision tools used to produce round or shaped wire to tight tolerances; die sets can range from a single die to hundreds of dies: <https://www.estevesgroup.com/solutions/science/die-profile>
- Esteves Group sells tungsten carbide drawing dies for rod-size to medium-size wire: <https://www.estevesgroup.com/products/wire-drawing-dies/tc-drawing-dies>
- Fort Wayne Wire Die offers matched elongation die sets for multiwire drawing operations: <https://www.fwwd.com/products/matched-elongation-die-sets>

## Commercial alternatives

- Hardened steel draw plate or simple die set for soft metals and low-throughput work.
- Tungsten carbide wire drawing dies for copper, aluminum, steel, and alloys.
- PCD or natural diamond dies for fine wire or high-wear industrial production.
- Matched die sets designed around a specific reduction schedule and drawing machine.

## Build or open-source references

Simple draw plates and soft-metal draw tooling can be made in small shops, but reliable industrial wire drawing dies require precise bore geometry, hard die materials, polishing, heat treatment or carbide/diamond inserts, lubrication, and wear control.

The current recipe says it derives from `drawing_die_set_basic_v0`, which reinforces that this is not a distinct machine class. It is credible as local tooling only if the KB also has precision machining/grinding/polishing and suitable die material.

## Related machine research

Related local reports:

- `research/machines/drawing_die_set_basic.md`
- `research/machines/dies.md`
- `research/machines/press_brake_die_set.md`

Related KB items:

- `drawing_die_set_basic`
- `wire_drawing_machine`
- `dies`

## Recommendation for KB realism

Prefer consolidation under Conservative Mode.

Recommended options:

- Use `drawing_die_set_basic` as the canonical generic wire drawing die set unless there is a specific reason to distinguish aluminum wire drawing from other wire drawing.
- Keep `wire_drawing_die_set` only if it is intended to represent a smaller/light-duty or aluminum-specific die set; document that scope explicitly.
- Classify conceptually as tooling/part, not a standalone machine, when schema support allows.
- Require a separate drawing machine/draw bench/capstan and lubricant in processes that actually draw wire.
- If retained separately, decide whether 2 kg versus 5 kg reflects a meaningful size/material difference or accidental duplication.

## Confidence and open questions

Confidence: high that the item is real tooling; high that it overlaps strongly with `drawing_die_set_basic`; medium on whether there is a hidden reason to keep an aluminum-specific variant.

Open questions:

- Should `wire_drawing_aluminum_v0` switch to `drawing_die_set_basic`, or should it preserve a lightweight aluminum die set?
- Does the KB need die material variants for steel/kovar/tungsten versus aluminum/copper?
- Should reusable passive tooling continue to appear under `machine_id` resource requirements?
