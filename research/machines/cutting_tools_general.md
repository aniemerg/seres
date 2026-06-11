# Cutting Tools General

## Machine identity

- KB ID: `cutting_tools_general`
- KB name: General cutting tools
- KB file: `kb/items/machines/cutting_tools_general.yaml`
- Current KB type: `machine`
- Current KB mass: 30 kg
- Current KB description: stub machine from ADR 003 migration; referenced by processes but not originally defined.
- Current KB BOM: `hand_tools_basic`, two `saw_or_cutting_tool`, `shear_blade_or_saw_band`, and `fastener_kit_small`.

## KB usage and needed function

The KB uses `cutting_tools_general` as a required machine/resource in many processes, including machining, gear cutting, metal cutting, wire cutting/stripping, hot rolling support, gas scrubber frame fabrication, and rough/finish machining.

The needed function is broad cutting capability: hand cutting, sawing, shearing, drilling, milling cutters, turning inserts, taps, dies, reamers, bandsaw blades, and other tooling. The current BOM only covers a small manual cutting kit, while many process references imply machine-tool consumables.

## Reality classification

Classification: real tooling category or kit, not a standalone machine.

Cutting tools are real and essential. They are generally consumable tooling used by machines or labor, not machines themselves. A 30 kg general shop cutting-tool kit is plausible as a starter inventory, but the name is too broad and can hide important distinctions between hand cutting, saw blades, milling cutters, lathe tools, drills, taps, and specialty gear cutters.

## Evidence links

- MSC Industrial Supply sells cutting tools for indexable tooling, holemaking, milling, threading, and turning applications. Source: https://www.mscdirect.com/products/cutting-tools
- Sandvik Coromant offers metal cutting tools and carbide inserts for machining operations including turning, milling, drilling, threading, boring, parting, and grooving. Source: https://www.sandvik.coromant.com/en-us/tools
- Kennametal describes end mills as rotating cutting tools for milling applications, usually made from high-speed steel or carbide and available in many shapes and sizes. Source: https://www.kennametal.com/us/en/resources/blog/metal-cutting/beginners-guide-to-end-mills.html
- Morse Cutting Tools sells drill bits, taps, end mills, reamers, counterbores, thread mills, and tool holding products. Source: https://www.morsecuttingtools.com/
- Sandvik Group describes its manufacturing tools as including tools and inserts for turning, milling, drilling, threading, boring, parting, grooving, and tooling systems. Source: https://www.home.sandvik/en/offerings/products-and-services/tools-and-software-for-component-manufacturing/
- B.I.R.S. Machine & Supply lists carbide end mills, taps, drills, broaches, routers, saws, burrs, deburring tools, inserts, and toolholders as cutting-tool products. Source: https://www.knowbirs.com/cutting-tools

## Commercial alternatives

- Manual cutting kit: hacksaw, snips, files, deburring tools, blades.
- Machine cutting-tool set: drills, end mills, reamers, taps, dies, countersinks, boring bars.
- Lathe tool set: HSS blanks, carbide inserts, holders, cut-off blades, grooving tools.
- Saw tooling: bandsaw blades, circular cold-saw blades, abrasive cutoff wheels.
- Gear cutting tooling: involute cutters, hobs, broaches, form tools.
- Precision tooling set for CNC milling and turning.

## Build or open-source references

Simple cutting tools can be made or sharpened locally from tool steel if the system has heat treatment, grinding, and inspection. Examples include HSS lathe tool bits, scrapers, simple punches, and crude saw blades.

High-performance tooling is harder:

- Carbide inserts require powder metallurgy, sintering, grinding, coatings, and precision edge prep.
- End mills and drills require flute grinding, heat treatment, geometry control, and sometimes coatings.
- Saw bands need alloy strip, tooth forming, heat treatment, welding, and setting.
- Gear cutters and hobs require precise profile generation and hardening.

The KB should treat cutting tools partly as consumables/wear items, not only as durable equipment.

## Related machine research

Related reports already present:

- `saw_or_cutting_tool.md`
- `hand_tools_basic.md`
- `cnc_mill.md`
- `milling_machine_general_v0.md`
- `inspection_tools_basic.md`

`saw_or_cutting_tool` should cover a specific handheld saw/cutter. `cutting_tools_general` should cover a broader tooling inventory only if it is not used as a substitute for real powered saws, mills, lathes, or shears.

## Recommendation for KB realism

Keep the concept, but reclassify and narrow it.

Recommended future cleanup:

- Rename display name to "General cutting-tool kit" or "Machine cutting-tool inventory."
- Model it as tooling/consumables rather than a machine.
- Split hand cutting tools from machine cutting tools if process realism matters.
- Use `saw_or_cutting_tool` for manual cutting and `metal_shear_or_saw` for powered stock cutting.
- Add separate specialty tooling where needed for gear cutting, threading, milling, drilling, or carbide tooling.

Do not count this as a major imported machine in realism summaries. It is a necessary shop inventory and consumable set.

## Confidence and open questions

Confidence: high that the category is real; high that it is not a machine; medium on how much splitting the KB needs.

Open questions:

- Should cutting tools be consumed by processes according to wear rate?
- Does the self-reproducing seed inventory include carbide tooling, HSS tooling, or only hand tools?
- Should gear cutting require explicit hobs/form cutters rather than `cutting_tools_general`?
