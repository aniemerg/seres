# Rolling Mill v0 Machine Reality Research

## Machine identity

- KB machine id: `rolling_mill_v0`
- KB name: Rolling mill v0
- KB file: `kb/items/machines/rolling_mill_v0.yaml`
- Current KB mass: 1200 kg
- Current BOM: `bom_rolling_mill_v0`
- Current recipe: `recipe_rolling_mill_v0`

## KB usage and needed function

The item is used by `electrical_steel_production_v0`, `steel_bar_stock_rolling_shop_v0`, `rolling_basic_shop_v0`, and `sheet_metal_fabrication_v0`. The local notes say it is for hot and cold rolling to achieve electrical steel sheet gauge.

The needed function is flat rolling/reduction of metal stock into sheet, strip, or bar: high roll force, hardened rolls, strong frame, bearings, drive, roll gap adjustment, and repeated passes. This is the same broad function already documented for `plate_rolling_mill`.

## Reality classification

Real practical machine, but likely redundant with `plate_rolling_mill`.

Rolling mills are standard metalworking equipment. A 1200 kg small/light-industrial rolling mill is plausible for coarse modeling, but the KB already has `plate_rolling_mill`, and local dedupe notes explicitly select `plate_rolling_mill` as the canonical rolling mill for rolling operations. `rolling_mill_v0` should therefore be treated as an older or smaller variant unless the KB intentionally distinguishes shop-scale rolling from the heavier plate mill.

## Evidence links

Evidence collected in `research/machines/plate_rolling_mill.md` applies directly:

- Element Machinery sells rolling mill machinery for steel rolling, steel plate rolling, and metal processing: <https://elementmachinery.com/products/metal-processing/rolling-mill/>
- International Rolling Mills lists 2-high, 4-high, laboratory, hot, cold, wire/rod, strip, and other rolling mill types: <https://www.introllingmills.com/categories/5287-rolling-mills>
- Sente Software describes plate rolling mills as reversing mills that reduce stock thickness pass by pass: <https://www.sentesoftware.co.uk/site-media/hotrolling>
- Cooksongold's rolling mill guide demonstrates the same basic roll-gap reduction mechanism at jewelry scale: <https://www.cooksongold.com/blog/learn/how-to-use-a-rolling-mill-for-jewellery-making-a-beginners-guide-2/>

## Commercial alternatives

- Laboratory 2-high rolling mill for small hot/cold rolling tests.
- Jewelry/light-shop rolling mill for nonferrous sheet and wire.
- 4-high cold rolling mill for thin strip and better gauge control.
- Reversing plate mill for plate/sheet reduction.
- Bar/rod rolling mill for long products.

## Build or open-source references

Small rolling mills can be built at jewelry or hobby scale, but useful steel rolling demands hardened/ground rolls, a rigid frame, bearings, screwdown or hydraulic gap control, drive reduction, guards, lubrication, heating/annealing support, and metrology. The roll quality directly transfers to product quality.

The current KB BOM is a seed assembly and should not be treated as a fully detailed local manufacturing closure for a production rolling mill.

## Related machine research

Related local reports:

- `research/machines/plate_rolling_mill.md`
- `research/machines/metal_forming_basic_v0.md`
- `research/machines/press_brake.md`
- `research/machines/stamping_press_basic.md`

Local dedupe notes:

- `docs/dedupe_decisions.md` says to keep only `plate_rolling_mill` as the canonical rolling mill and consolidate older `rolling_mill` references into it. Some active references to `rolling_mill_v0` remain.

## Recommendation for KB realism

Prefer consolidation with `plate_rolling_mill` unless a smaller shop-scale variant is intentional.

Recommended options:

- Use `plate_rolling_mill` as the canonical item for flat rolling/reduction of ingots, billets, sheet, plate, strip, and bar.
- Keep `rolling_mill_v0` only if it is explicitly defined as a smaller shop/lab rolling mill for limited stock sizes.
- Do not confuse flat rolling/reduction with plate roll-bending machines used to curve plates into cylinders.
- If retained, document capacity limits: maximum roll width, roll force, hot/cold use, and product thickness range.
- Consider retargeting active process references to `plate_rolling_mill` later, consistent with existing dedupe decisions.

## Confidence and open questions

Confidence: high that rolling mills are real; high that this item overlaps with `plate_rolling_mill`; medium on whether a smaller variant is intentionally needed for electrical steel sheet production.

Open questions:

- Is `rolling_mill_v0` meant to be a shop/lab mill while `plate_rolling_mill` is a heavier production mill?
- Which processes truly need 4-high/precision cold rolling versus a generic 2-high mill?
- Should electrical steel production require annealing, pickling/descaling, insulation coating, and gauge-control equipment beyond the rolling mill?
