# Press Brake Die Set Machine Reality Research

## Machine identity

- KB item id: `press_brake_die_set`
- KB name: Press brake die set
- KB file: `kb/items/parts/press_brake_die_set.yaml`
- Current KB kind: `machine`
- Current KB mass: 40 kg
- Current BOM: `bom_press_brake_die_set`
- Current recipe: `recipe_press_brake_die_set_v0`

## KB usage and needed function

The item is required by `sheet_metal_forming_v0` alongside `press_brake` and `labor_bot_general_v0`. Its needed function is interchangeable tooling for bending sheet metal: an upper punch and lower die/V-die blocks that set bend angle, inside radius, clearance, tonnage requirement, and surface quality.

The item also appears in BOMs for `press_brake_or_roller` and `bending_machine_v0`. This is best interpreted as tooling or a tooling kit, not as an independently powered machine.

## Reality classification

Real practical tooling set, not a standalone machine.

The KB's 40 kg mass is plausible for a small collection of sectionalized press brake punches and dies. The current manufacturing recipe is also plausible at a high level: tool steel stock, machining, heat treatment, precision grinding, and mounting hardware. The main realism issue is classification. A press brake die set should normally be modeled as `kind: part`, `tooling`, or `tool_set`, even if the simulator currently uses `kind: machine` for capability providers.

## Evidence links

- WILA describes press brake tooling for sheet-metal bending on press brakes, with standardized tooling systems across machine types: <https://www.wilatooling.com/en-us/products/press-brake-tooling/>
- Mate Precision Technologies lists press brake punches, dies, specials, accessories, and tooling styles made from premium alloy tool steels: <https://www.mate.com/products/press-brake-tooling/>
- Polyurethane Products describes steel press brake tooling made from induction-hardened or through-hardened steel, precision ground to tight tolerances: <https://www.polyprod.com/steel-press-brake-tooling/>
- MSC Industrial Supply sells press brake punch and die sets as catalog tooling, supporting the item as a purchasable tooling kit rather than a custom machine: <https://www.mscdirect.com/browse/tn/Machinery/Metal-Forming-Cutting-Machines/Press-Brakes-Punches-Dies/Press-Brake-Punch-Die-Sets?navid=2107604>

## Commercial alternatives

- Standard American-style or European-style press brake punch/die sets.
- Sectionalized V-die and punch sets for small shop brakes.
- Custom press brake tooling for special bend radii, gooseneck clearance, hemming, offset bends, or box forming.
- Polyurethane or specialty tooling for surface-sensitive bends, where steel dies may mark the workpiece.

## Build or open-source references

No robust open-source design package for precision press brake tooling was found in this pass. The generic manufacturing path is well understood: select tool steel, machine punch and die geometry, harden/temper, precision grind working surfaces, and verify fit to the press brake clamping style.

The current KB recipe is a reasonable abstraction for local manufacture if the model already has precision machining, heat treatment, and surface grinding. For high-quality bends, the recipe should not be reduced to simple cutting or welded fabrication.

## Related machine research

Related local reports:

- `research/machines/press_brake.md`
- `research/machines/steel_forming_press.md`
- `research/machines/hydraulic_press.md`
- `research/machines/drawing_die_set_basic.md`

These support the distinction between the powered forming machine and interchangeable tooling.

## Recommendation for KB realism

Keep the item, but treat it explicitly as tooling.

Recommended options:

- Rename or annotate as `press_brake_tooling_set` if the KB wants clearer language.
- Change `kind` from `machine` to a tooling/part category when schema support allows it, while preserving process requirements through a tooling requirement field.
- Keep the separate requirement in `sheet_metal_forming_v0`; a press brake without matched punches/dies is incomplete.
- Keep the current 40 kg mass for a small general-purpose set. Use larger masses only for long tooling sets or heavy-duty/specialized dies.
- Do not merge with `press_brake`; commercial practice and maintenance reality make separate tooling more realistic.

## Confidence and open questions

Confidence: high that this is a real, necessary tooling set; high that the current 40 kg value is plausible for a basic set; medium on exact recipe hours because heat treatment and precision grinding depend strongly on tooling length and tolerance.

Open questions:

- Does the KB schema need a dedicated `tooling` kind or should simulator capability providers continue to use `kind: machine`?
- Which press brake tooling standard is assumed by `press_brake`: American, European, WILA/Trumpf style, or an abstract compatible interface?
- Should bend-specific tooling be modeled separately for tight-radius, hemming, or offset operations?
