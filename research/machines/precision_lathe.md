# Precision Lathe Machine Reality Research

## Machine identity

- KB machine id: `precision_lathe`
- KB name: Precision lathe
- KB file: `kb/items/machines/precision_lathe.yaml`
- Current KB mass: 1200 kg
- Current BOM: `bom_precision_lathe_v0`
- Current recipe: `recipe_precision_lathe_v0`

## KB usage and needed function

The lathe supports ball screw fabrication, lead screw fabrication, knob/control dial machining, lathe headstock turning, general precision turning, and valve body boring.

The needed function is accurate turning of cylindrical parts: turning, facing, boring, threading, taper work, and precision concentric features. For the KB's ball screw, lead screw, spindle/headstock, and valve-bore applications, the critical properties are spindle runout, bed straightness, carriage/feed accuracy, rigidity, vibration damping, workholding, and tooling.

## Reality classification

Real practical machine.

Precision/toolroom lathes are standard machine tools. The KB's 1200 kg mass is plausible for a serious toolroom or medium engine lathe, and the BOM's bed/headstock, carriage/cross-slide, spindle/bearings, leadscrew/feed system, motor/drive, tailstock, coolant, tooling, and electrical controls are realistic components. This should remain distinct from `lathe_engine_v0`, which is a smaller general-purpose lathe.

## Evidence links

- Sharp Industries describes toolroom lathes for small workpieces requiring ultra-high precision, with spindle runout within 50 millionths of an inch: <https://sharp-industries.com/product-category/manual-machines/lathes/>
- Clausing describes precision/high-performance geared-head and variable-speed lathes, and its CT toolroom lathes list circularity accuracy to 0.00125 mm: <https://clausing-industrial.com/lathes/clausing-ct-precision-tool-room-lathes/>
- Kent USA sells manual precision lathes with capacities from 11 x 18 inches to 44 x 320 inches, spindle bores from 1.56 to 12 inches, and spindle motors up to 20 HP: <https://kentusa.com/machine/lathes/manual-precision-lathes/>
- TRAK/Southwestern Industries sells toolroom lathes with large swings, long center distances, and multiple spindle ranges, supporting the machine category as a commercial industrial product: <https://www.southwesternindustries.com/products/lathes>

## Commercial alternatives

- Manual toolroom lathe: best fit for low-volume precision turning, boring, and threading.
- Precision engine lathe: broader manual shop lathe with less emphasis on toolroom tolerances.
- CNC lathe/turning center: higher repeatability and productivity, especially for repeated parts.
- Swiss-type lathe: specialized for small high-precision shaft-like parts.
- Cylindrical grinder: not a lathe substitute, but needed where final roundness/surface finish exceeds turning capability.

## Build or open-source references

Self-building a precision lathe is possible only with substantial machine-tool-building capability. The KB's detailed bed/headstock recipe correctly notes cast iron, stress relief, precision-ground/scraped ways, spindle bearing accuracy, leadscrew precision, and long assembly/inspection times.

The hard closure problem is recursive: a precision lathe depends on other precision machines, metrology, scraping/grinding skill, spindle bearings, leadscrews/ballscrews, and stable castings. A locally fabricated low-precision engine lathe is much easier than a true precision/toolroom lathe.

## Related machine research

Related local reports:

- `research/machines/cnc_mill.md`
- `research/machines/milling_machine_general_v0.md`
- `research/machines/cutting_tools_general.md`
- `research/machines/work_rest_adjustable.md`
- `research/machines/spinning_machine_v0.md`

Relevant local dedupe notes:

- `docs/dedupe_decisions.md` keeps `lathe_engine_v0` and `precision_lathe` separate because they represent different precision tiers and process needs.

## Recommendation for KB realism

Keep `precision_lathe` as a real high-value imported machine.

Recommended boundaries:

- Keep it distinct from `lathe_engine_v0`; use the smaller engine lathe for general turning and this item for tight-tolerance leadscrews, ball screws, headstocks, bores, and precision shafts.
- Do not merge turning operations into `cnc_mill`; turning and milling are different process geometries.
- Add or require precision metrology, cutting tools, workholding, coolant, and possibly grinding/lapping for the highest-accuracy components.
- Treat local manufacture as advanced machine-tool reproduction, not a simple assembly task.
- If CNC capability matters later, create or map a separate CNC turning center instead of silently upgrading this manual precision lathe.

## Confidence and open questions

Confidence: high that the machine is real and correctly separated from generic engine-lathe capability; medium on whether the current KB recipes fully capture the metrology and scraping/grinding burden.

Open questions:

- What tolerance level does the KB intend for `precision_lathe` operations: 0.01 mm, 0.005 mm, or better?
- Are ballscrews and lead screws meant to be cut on the lathe alone, or finished by grinding/lapping?
- Should the precision lathe require a separate metrology/tooling package in process requirements?
