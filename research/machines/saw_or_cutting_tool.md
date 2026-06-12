# Saw or cutting tool

## Machine identity

- KB ID: `saw_or_cutting_tool`
- KB file: `kb/items/machines/saw_or_cutting_tool.yaml`
- KB name: Saw or cutting tool
- KB mass: 1 kg per unit
- Current KB role: handheld saw/cutting tool for low-throughput manual fabrication tasks.

## KB usage and needed function

Local usage shows this is a small manual cutting resource:

- It is listed in the minimal/self-reproducing machine set.
- It is required by `cutting_basic_v0` and several gasket sheet cutting processes.
- It is a component of `cutting_tools_general`.
- Its BOM includes a tool frame, blade/band, fasteners, grip, and tensioning hardware.
- `docs/dedupe_decisions.md` keeps `metal_shear_or_saw` as the primary heavier metal cutting tool, while this item remains a small hand tool.

The needed function is basic manual cutting of bars, tubing, plate/fixture stock, and sheet/gasket materials when a powered saw, shear, laser, or CNC tool is unnecessary.

## Reality classification

Classification: real practical hand tool / generic name needs cleanup.

The item is realistic if interpreted as a hacksaw/frame saw with replaceable metal-cutting blades. The name "saw or cutting tool" is overly broad and should not be used for all cutting operations. It should mean a specific low-mass manual saw or simple cutting hand-tool kit.

## Evidence links

- Soteck describes hacksaws as common hand-operated metal cutting tools and manufactures hacksaw frames and blades: https://www.soteck.com.tw/en/category/CAT-Metal-Cutting-Saw.html
- RS Components explains hacksaw frames, replaceable blades, steel/aluminum frames, and blade holders: https://uk.rs-online.com/web/content/discovery/ideas-and-advice/hacksaws-guide
- Milwaukee's compact hacksaw product shows a commercial hand saw with replaceable bi-metal blade and tool-free blade change: https://www.homedepot.com/p/Milwaukee-Compact-Hack-Saw-with-10-in-24-TPI-Bi-Metal-Blade-48-22-0012/202523986
- Malco lists shears, saws, snips, and replaceable-blade cutting tools for sheet metal and related materials: https://www.malcotools.com/categories/cutting-tools/
- Pilana Metal describes hand hacksaw blades made from carbon steel, high-speed steel, and bimetal material: https://www.pilanametal.com/hand-hacksaw-blades.html?page=all

## Commercial alternatives

Commercial alternatives include:

- Standard 10-12 inch hacksaw frames with replaceable HSS or bi-metal blades.
- Compact hacksaws and junior hacksaws for tight spaces.
- Tin snips or aviation snips for thin sheet.
- Metal shears, bandsaws, abrasive chop saws, and cold saws for higher-throughput or heavier stock.
- `metal_shear_or_saw` in the KB for heavier shop cutting.

For low-volume gasket or fixture prep, the handheld saw/tool item is realistic. It should not substitute for heavy stock cutting if throughput, accuracy, or material thickness is important.

## Build or open-source references

- Instructables has a simple hacksaw-bladed bow saw/frame saw build: https://www.instructables.com/Hacking-Together-a-Bow-Saw-for-the-2017-Build-a-To/
- HomemadeTools documents repurposing broken bandsaw blades as hacksaw blades: https://www.homemadetools.net/forum/free-hacksaw-blades-how-make-them-75797
- Hobby-machinist builders document homemade power hacksaw frames; these are heavier than the KB's 1 kg manual tool but support buildability of simple saw mechanisms: https://www.hobby-machinist.com/threads/homemade-power-hacksaw.87088/

The simplest local build is a steel frame, handle, tensioning screw/pin, and replaceable blade. Blade metallurgy matters more than the frame for cutting performance.

## Related machine research

Related KB items:

- `cutting_tools_general`
- `metal_shear_or_saw`
- `shear_blade_or_saw_band`
- `hand_tools_mechanical`
- `refractory_installation_tools`

No follow-up tasks were enqueued, per task constraint.

## Recommendation for KB realism

Keep the item, but rename or annotate it as a specific manual saw.

Recommended cleanup when KB edits are allowed:

- Rename display name to "Hand hacksaw" or "Manual metal-cutting saw" rather than "Saw or cutting tool".
- Keep the 1 kg mass for a hand saw with spare blade/hardware.
- Use `cutting_tools_general` for a broader manual cutting kit and `metal_shear_or_saw` for heavier shop cutting.
- Avoid assigning this item to operations requiring powered cutting, precise kerf control, thick plate, or high production rate.
- Consider whether gasket cutting should use a utility knife/die cutter rather than a hacksaw, depending on material.

## Confidence and open questions

Confidence: high that the item is real as a hand saw; medium that every current process reference is the best fit.

Open questions:

- Should gasket-sheet cutting use a blade/knife/die item instead of this saw?
- Should the KB collapse this into `cutting_tools_general`, or keep it as a concrete component of that kit?
- What materials and thicknesses are intended for `cutting_basic_v0`?
