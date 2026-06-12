# Drawing die set basic

## Machine identity

- KB ID: `drawing_die_set_basic`
- KB file: `kb/items/machines/drawing_die_set_basic.yaml`
- KB name: Drawing die set (basic)
- KB mass: 5 kg per unit
- Current KB role: reusable die tooling for wire/rod drawing processes.

## KB usage and needed function

Local usage shows this item is process tooling, not an active powered machine:

- It is listed in the minimal/self-reproducing machine set under forming tooling.
- It is required by `wire_drawing_process_v0`, `metal_wire_drawing_process_v0`, `wire_drawing_basic_v0`, `kovar_wire_drawing_v0`, and `metal_wire_drawing_v0`.
- The item notes describe drawing dies for wire reduction.
- There is a related `wire_drawing_die_set` under `kb/items/parts`, which may overlap with this machine item.

The needed function is a progressive set of hardened die openings used to reduce wire or rod diameter by pulling material through them. It must be paired with a tensile pulling mechanism, draw bench, capstan, or wire drawing machine; the die set alone does not provide actuation.

## Reality classification

Classification: real practical tooling set.

Drawing dies are standard industrial tooling. They are often made from tungsten carbide, polycrystalline diamond, natural diamond, or hardened tool steel depending on wire material and throughput. The KB item is realistic, but its `kind: machine` classification may be a simulator-driven convenience rather than a literal machine classification.

## Evidence links

- Hyperion Materials & Technologies manufactures PCD, cemented carbide, and diamond composite wire drawing dies and blanks: https://www.hyperionmt.com/en/products/Wire-Dies/
- Esteves Group describes wire drawing dies as precision tools used to produce round or shaped wire to tight tolerances; die sets can range from a single die to hundreds of dies: https://www.estevesgroup.com/solutions/science/die-profile
- Esteves Group also sells tungsten carbide drawing dies for rod-size to medium-size wire: https://www.estevesgroup.com/products/wire-drawing-dies/tc-drawing-dies
- Fort Wayne Wire Die offers matched elongation die sets for multiwire drawing operations: https://www.fwwd.com/products/matched-elongation-die-sets
- Expometals explains drawing dies as tools that reduce wire cross-section and discusses friction, heat, cooling, and die wear: https://www.expometals.net/en/metal-working-basics/drawing-dies-the-basics
- Society of American Silversmiths describes wire drawing as pulling metal through a die by tensile force, with radial compressive forces producing deformation: https://www.silversmithing.com/wire-drawing.htm

## Commercial alternatives

Commercial alternatives include:

- Tungsten carbide die sets for steel, copper, aluminum, and alloy wire.
- PCD or natural diamond dies for high-wear or fine-wire applications.
- Hardened steel draw plates for low-throughput soft-metal work.
- Matched elongation die sets designed for a specific wire drawing machine.

For early KB modeling, a basic steel/carbide die set is plausible. For steel wire or high-throughput use, carbide/diamond inserts and cooling/lubrication should be modeled eventually.

## Build or open-source references

- Jewelry and small-shop draw plates demonstrate manual wire drawing with a hardened plate and draw tongs: https://pmcsupplies.com/collections/metal-drawing
- Ganoksin documents practical hand wire drawing with drawplates and tongs: https://www.ganoksin.com/article/wire-drawing-hints/
- Simple draw plates can be made from hardened steel for soft metals, but industrial dies require precision bore geometry, polishing, hard die materials, and wear control.

These references support low-tech manufacturability for soft metals. They do not prove that high-quality steel wire drawing dies are easy to make locally.

## Related machine research

Related KB items:

- `wire_drawing_die_set`
- `wire_drawing_machine`
- `drawing_die_set_basic`
- `dies`
- `casting_mold_set`

No follow-up tasks were enqueued, per task constraint.

## Recommendation for KB realism

Keep the item as real tooling, but consider consolidation and classification cleanup.

Recommended cleanup when KB edits are allowed:

- Compare `drawing_die_set_basic` with `wire_drawing_die_set`; they appear likely duplicate or near-duplicate under Conservative Mode.
- Prefer a single canonical die-set ID unless the KB needs distinct die materials or size ranges.
- If simulator constraints allow, classify this as a part/tooling item rather than a machine. If reusable capacity must stay under `resource_requirements`, keep `kind: machine` but document that it is passive tooling.
- Add a note that a drawing die set must be used with a pulling machine/draw bench/capstan and lubricant, not by itself.
- Keep the 5 kg mass for a small basic set; industrial multi-pass die sets can be heavier or much more numerous.

## Confidence and open questions

Confidence: high that the item represents real practical tooling; medium that the current KB classification is the best one.

Open questions:

- Should `drawing_die_set_basic` and `wire_drawing_die_set` be merged?
- What wire materials are expected: copper/aluminum, steel, kovar, tungsten, or precious metals?
- Does the KB also need a powered wire drawing machine/capstan distinct from the die tooling?
