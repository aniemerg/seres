# Machine identity

- Queue item: `machine_reality_dies`
- KB item: `dies`
- KB name: Dies and tooling
- KB file: `kb/items/parts/dies.yaml`
- Current KB kind: `machine`
- Current mass: 40 kg
- Current BOM: `bom_dies_v0`
- Current recipe: `recipe_dies_v0`

# KB usage and needed function

`dies` is currently required by `sintering_and_hot_pressing_v0` together with `hot_press_v0`, `sintering_furnace_v0`, and `labor_bot_general_v0`. The item notes describe dies and tooling sets for pressing and sintering operations, with hardened steel construction for shape forming.

The needed function is passive tooling: contain powder or green body material, transmit pressure from the press, define the part geometry, survive heat/mechanical load, and allow part release. This is tooling used by a press/furnace system, not an independently powered machine.

The KB has more specific die/tooling items elsewhere, including `drawing_die_set_basic`, `press_brake_die_set`, `punch_die_set`, `crimping_die_set`, `anvil_and_die_set`, and `pressing_mold_set`. This generic `dies` item therefore functions as a placeholder for hot-press/sintering dies unless renamed or split.

# Reality classification

Real practical tooling set, but overly generic and not a standalone machine.

Dies for powder metallurgy, ceramic pressing, and hot pressing are real and necessary. However, the current KB details are internally mixed:

- The item says hardened steel construction.
- The BOM says high-carbon tool steel.
- The recipe casts and machines from `regolith_metal_crude`, with heat treatment still TBD.
- The process using it is `sintering_and_hot_pressing_v0`, where graphite, ceramic, carbide, or refractory tooling may be more realistic than ordinary steel depending on temperature, atmosphere, pressure, and material chemistry.

# Evidence links

- POCO/Entegris describes fine-grain graphite grades used as dies for hot-pressing powdered metal and ceramic processes, emphasizing surface finish, die life, thermal conductivity, and release behavior: https://poco.entegris.com/en/home/our-science/by-industry/general-industrial/hot-press-die--hpd-.html
- Hyperion Materials & Technologies describes powder-metallurgy compaction tooling: precision dies, punches, and core rods compact powder into near-net shapes under high pressure before sintering: https://www.hyperionmt.com/en/products/forming-tools/compaction-components/
- NIST/ASM hot pressing reference notes that ceramic or graphite tooling is frequently used and that brittle tooling can fail catastrophically if overloaded; die and punch thermal expansion compatibility matters: https://materialsdata.nist.gov/bitstream/handle/11115/194/Forging%20and%20Hot%20Pressing.pdf?sequence=3
- MTI sells small pressing dies including silicon nitride dies for hot pressing and customizable pellet pressing dies, supporting commercial availability of specialized lab-scale die sets: https://mtixtl.com/collections/pressing-dies
- PowderMetallurgy.com discusses powder-metallurgy die design, including the die's role in determining finished shape/size and the effect of pressing and sintering on die dimensions: https://powdermetallurgy.com/powder-metallurgy-die-design/

# Commercial alternatives

Commercial alternatives depend on the process:

- Graphite hot-press dies for ceramics and powdered metals in vacuum/inert/reducing atmospheres.
- Silicon nitride or other ceramic dies for specific temperature/material compatibility needs.
- Hardened tool-steel compaction dies, punches, and core rods for cold powder pressing before sintering.
- Carbide or wear-resistant inserts for abrasive powders and high-volume compaction.
- Custom tool-and-die shop fabrication when the part geometry, press interface, or material compatibility is specific.

# Build or open-source references

The KB's generic manufacturing path is plausible only for simple metal dies at modest temperature: cast or forge blank, machine working surfaces, heat treat, grind/polish, and inspect.

For hot pressing, local fabrication probably needs a different route:

- graphite blank selection and precision machining for many ceramic/powder hot-press dies,
- matched punch and die materials to control thermal expansion,
- lubricants/release coatings or separators such as graphite foil/BN where appropriate,
- pressure/temperature derating to avoid brittle tooling fracture,
- replacement/spares because hot-press tooling can be consumable.

No single open-source die design covers the KB's generic `dies` item; die geometry must follow the part, powder behavior, press stroke, ejection method, shrinkage, and thermal expansion.

# Related machine research

Related local reports:

- `hot_press_v0.md`
- `drawing_die_set_basic.md`
- `press_brake_die_set.md`
- `stamping_press_basic.md`
- `steel_forming_press.md`
- `hydraulic_press.md`
- `wire_crimping_tools.md`

These reports support separating powered presses from passive die/tooling sets.

# Recommendation for KB realism

Keep the concept, but make it less generic.

Recommended options:

- Rename to `hot_press_die_set_basic` or `powder_pressing_die_set_basic` if its primary use remains `sintering_and_hot_pressing_v0`.
- Change classification from `machine` to tooling/part if the schema supports it; if not, document that `kind: machine` is only a simulator capacity convention.
- Do not treat this as interchangeable with `press_brake_die_set`, `drawing_die_set_basic`, or `punch_die_set`; those are different tooling families.
- Revisit material assumptions: high-temperature hot pressing often needs graphite or ceramic tooling, while cold powder compaction may use hardened steel/carbide.
- Add heat treatment, precision grinding/polishing, and dimensional inspection if the steel-die route is retained.

# Confidence and open questions

Confidence: high that the item represents real practical tooling; high that it is not a standalone machine; medium on whether 40 kg is appropriate because die mass depends on press capacity, part size, tool material, and whether it is a single die or a set.

Open questions:

- Is this intended for hot pressing ceramics/regolith, cold powder compaction, or generic press tooling?
- Should the KB model graphite hot-press dies as consumable or finite-life tooling?
- Does the process need shape-specific die sets rather than one generic `dies` item?
