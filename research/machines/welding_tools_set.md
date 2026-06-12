# Welding Tools Set

## Machine identity

- KB ID: `welding_tools_set`
- KB name: Welding tools set
- KB file: `kb/items/machines/welding_tools_set.yaml`
- Current KB type: `machine`
- Current KB mass: 15 kg
- Current KB description: welding helmet, gloves, electrode holders, ground clamps, chipping hammers, wire brushes, and welding gauges for arc, MIG, and TIG welding operations.

## KB usage and needed function

The KB uses `welding_tools_set` for:

- `welded_fabrication_basic_v0`
- `welding_basic_v0`
- `welding_structural_v0`
- `welding_process_general_v0`
- `welding_tig_basic_v0`
- `gas_scrubbing_unit_frame_v0`
- `fabricate_structural_steel_frame_v0`

The needed function is welding support: PPE, holders, clamps, cleaning tools, gauges, and general accessories used with a separate welding machine/power source.

## Reality classification

Classification: real tool/accessory/PPE kit, not a standalone welding machine.

The listed items are standard welding accessories. A 15 kg kit is plausible for helmet, gloves, electrode holder, ground clamp, chipping hammer, brushes, gauges, clamps, leads, and small hand tools. The important modeling point is that this kit does not provide welding current or process capability by itself. It must be paired with a TIG welder, arc welder, spot welder, MIG power source, or other welding machine.

## Evidence links

- WeldingMart describes minimum stick-welding accessories as electrode holder, work/ground clamp, welding leads, welding helmet, welding gloves, and chipping hammer. Source: https://weldingmart.com/collections/stick-accessories
- Cyberweld sells welding hand tools including chipping hammers, scratch brushes, welding magnets, soapstone holders, welding clamps, and pipe measuring tools. Source: https://store.cyberweld.com/collections/hand-tools
- Haun Welding Supply lists arc welding accessories including cable, chipping hammers, electrode holders, ground clamps, MIG torches/consumables, plasma consumables, and rod ovens. Source: https://haunweldingsupply.com/products/
- Home Depot sells a welder accessory start-up kit with welding helmet, gloves, chipping hammer, and scratch brush. Source: https://www.homedepot.com/p/RIDGID-Welder-Accessories-Start-Up-Kit-ADF-Helmet-Gloves-Wire-Brushand-Chipping-Hammer-RWSUK/326666868
- Weld Shop Supply describes ground clamps as vital welding setup components for maintaining a safe and efficient welding circuit. Source: https://www.weldshopsupply.com/collections/stick-welding-ground-clamps
- Welding For Less lists beginner welding tools such as auto-darkening helmet, gloves, wire brush, chipping hammer, MIG pliers, and clamps. Source: https://www.weldingforless.com/blogs/welders-blog/welding-tools-kit-10-must-have-tools-for-beginners

## Commercial alternatives

- Stick welding accessory kit.
- MIG/TIG accessory kit.
- Welding PPE kit: helmet, gloves, jacket/apron, respirator.
- Welding clamps and fixturing set.
- Weld inspection gauge set.
- Dedicated TIG torch/consumables kit.
- Welding power source, which is separate from this item.

## Build or open-source references

Many kit components are locally buildable or repairable:

- Chipping hammers, wire brushes, clamps, and gauges can be fabricated from steel/tool steel.
- Electrode holders and ground clamps need conductive copper/brass contact parts, insulation, springs, and current-rated cables.
- Gloves and clothing require heat-resistant textiles or leather.
- Welding helmets need safe filter lenses or certified auto-darkening filters; this is the least locally trivial component.

For realism, PPE certification and eye protection matter. A locally fabricated opaque shell is not enough without correct shade and optical protection.

## Related machine research

Related reports already present:

- `welding_tig_unit_v0.md`
- `fixturing_workbench.md`
- `hand_tools_basic.md`
- `cutting_tools_general.md`

Related KB items:

- `welding_arc_welder_v0`
- `welding_spot_welder_v0`
- `welding_tig_unit_v0`
- `electrode_copper_welding`
- `welding_electrode_copper`

## Recommendation for KB realism

Keep the concept, but reclassify it as welding tools/PPE/accessories rather than a machine.

Do not use `welding_tools_set` alone as the machine that performs welding. Welding processes should require both an appropriate welding machine, such as `welding_tig_unit_v0` or `welding_arc_welder_v0`, and this tool/PPE/accessory kit where manual welding is modeled.

The current 15 kg mass and component list are plausible. The recipe may overstate local manufacturability of helmet optics and protective gloves unless appropriate lens/filter and heat-resistant material items exist.

## Confidence and open questions

Confidence: high that the item is real as a kit; high that it is not a standalone machine.

Open questions:

- Should welding PPE be separated from electrode holders/clamps and inspection gauges?
- Should welding leads/cables be explicit components?
- Should certified filter lenses or auto-darkening modules be imported initially?
