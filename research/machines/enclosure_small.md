# Machine identity

- Queue item: `machine_reality_enclosure_small`
- KB item: `enclosure_small`
- KB name: Enclosure (small)
- KB file: `kb/items/parts/enclosure_small.yaml`
- Current KB kind: `machine`
- Current mass: 5 kg
- Current capabilities: `electronics_housing`, `environmental_enclosure`

# KB usage and needed function

`enclosure_small` is used broadly as a housing component for electronics, instruments, power supplies, control units, and lab devices. It appears in many recipes and BOMs as an input part, not as a production asset. One process, `computer_core_assembly_v0`, lists it as a `machine_id`, but the surrounding usage points to an enclosure as the physical case or chassis around electronics rather than a machine that performs work.

The KB has two manufacturing routes:

- `recipe_enclosure_small_v0`: sheet-metal fabrication from steel sheet, followed by joining, drilling, coating, and inspection.
- `recipe_enclosure_small_additive_v0`: polymer printing plus cleanup and hardware installation.

The needed function is credible: protect electronics, provide mounting, reduce accidental contact, support cable openings and grounding, and provide some environmental shielding. The imported-machine-list classification is the weak part; this is better modeled as a part/subassembly or optional purchased enclosure than as a machine.

# Reality classification

Real practical object, but not a machine. It is a generic electrical/electronics enclosure category.

Small metal, plastic, and die-cast enclosures are standard commercial parts. A 5 kg enclosure is plausible for a small steel control/equipment box, especially if it includes cover, fasteners, mounting hardware, and modest wall thickness. The KB's polymer additive variant is plausible for non-high-temperature indoor electronics, but its `material_class: steel` conflicts with the preferred additive polymer route.

# Evidence links

- NEMA describes an electrical enclosure as a cabinet or box that protects electrical/electronic equipment and prevents shock, commonly made from rigid plastics, steel, stainless steel, or aluminum: https://www.nema.org/membership/products/view/enclosures
- Hammond Manufacturing has a broad "Small Enclosures" product family covering die-cast, plastic, extruded, and general-purpose electronic enclosures: https://www.hammfg.com/electronics/small-case
- Bud Industries lists general-use electronic enclosures including sheet metal enclosures, chassis, hand-held enclosures, breadboards, and steel/aluminum/plastic options: https://www.budind.com/
- Bud's SN Series is a steel sheet-metal electronics enclosure family with NEMA/IP ratings, using 14 gauge steel: https://www.budind.com/series/nema-ip-rated-boxes/sn-series-electronics-enclosure/
- Polycase describes metal enclosures for electronics in aluminum, steel, stainless steel, die-cast aluminum, extruded aluminum, and carbon steel, with indoor/outdoor use and inherent EMI shielding benefits: https://www.polycase.com/metal-enclosures
- Protocase's electronic enclosure design guide covers metal selection, bending, self-clinching fasteners, welding, and finishing, matching the KB's sheet-metal fabrication route: https://www.protocase.com/blog/2017/02/16/electronic-enclosure-design-101/

# Commercial alternatives

Commercial substitutes are abundant:

- Off-the-shelf Hammond small electronic enclosures for instrument/project electronics.
- Bud Industries NEMA/IP steel, aluminum, plastic, fiberglass, and die-cast enclosures.
- Polycase metal and plastic electronics enclosures.
- Custom fabricated Protocase-style sheet-metal enclosures when exact cutouts, brackets, or mounting patterns are needed.

For the KB, this means `enclosure_small` does not need to be imported as a special machine. It can be fabricated locally if sheet-metal or polymer printing capability exists, or imported as a purchased part when local fabrication is not yet available.

# Build or open-source references

The KB's sheet-metal recipe is realistic for a small enclosure: cut/bend sheet, join or fasten, drill openings and mounting holes, apply coating, and inspect dimensions/grounding. The Protocase guide is a useful design/manufacturing reference for this route.

The additive route is also realistic for protective electronics housings, but only for conditions compatible with polymer properties. It should not silently stand in for a steel enclosure in high-temperature, high-impact, vacuum/outgassing-sensitive, fire-rated, or EMI-sensitive contexts unless materials and certification assumptions are explicit.

# Related machine research

- `power_distribution_bus.md`: related because electrical distribution equipment usually needs cabinets, busbar enclosures, covers, and touch-safe shielding.
- `wire_crimping_tools.md`: related as a tool set used during electrical/electronics assembly, often paired with enclosure wiring.

# Recommendation for KB realism

Do not treat `enclosure_small` as a real machine. Keep it as a real, reusable part or subassembly.

Recommended cleanup:

- Reclassify from `kind: machine` to a part/subassembly classification if the schema allows it.
- Consider renaming to `electronics_enclosure_small` or `electrical_enclosure_small` for clarity.
- Preserve the two manufacturing routes, but split material assumptions: sheet-metal steel enclosure versus polymer printed enclosure.
- Review `computer_core_assembly_v0` listing it as `machine_id`; that is probably a misuse unless the process means "assembly fixture/chassis".
- Keep a purchased/import option for early bootstrap scenarios, because off-the-shelf enclosures are standard and cheap.

# Confidence and open questions

Confidence: high that the object is real and commercially standard; high that it is not a machine; medium on the exact 5 kg mass because commercial enclosure mass depends strongly on size, wall thickness, NEMA/IP rating, door/cover design, and hardware.

Open questions:

- Does the KB schema permit a non-machine item to advertise capabilities like `electronics_housing` and `environmental_enclosure`?
- Should the additive and steel variants be separate item IDs, or should material choice remain a recipe variant?
- Does any simulation logic depend on `kind: machine` for `enclosure_small`, or is that only a legacy classification artifact?
