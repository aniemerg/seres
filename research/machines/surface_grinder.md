# Machine identity

- Queue item: `machine_reality_surface_grinder`
- KB item: `surface_grinder`
- KB name: Surface grinder
- KB file: `kb/items/machines/surface_grinder.yaml`
- Current KB kind: `machine`
- Current mass: 950 kg
- Current preferred variant: `simple`
- Current BOM: `bom_surface_grinder_v0`
- Current recipe: `recipe_surface_grinder_v0`

# KB usage and needed function

`surface_grinder` is used by many precision finishing processes, including `precision_grinding_basic_v0`, `surface_grinding_precision_v0`, `precision_grinding_and_scraping_v0`, `grinding_process_precision_v0`, `machining_precision_v0`, `surface_finishing_v0`, `surface_finishing_basic_v0`, `mirror_polishing_v0`, `finishing_deburring_v0`, and `alnico_machining_grinding_v0`.

The BOM includes a large machine base, grinding spindle assembly, table drive, magnetic chuck, coolant system, imported compute/control module, sensors, power conditioning, and fasteners. This matches the needed function: produce flat, smooth, dimensionally accurate surfaces with a high-speed abrasive wheel, controlled table motion, workholding, coolant, and alignment.

# Reality classification

Real practical machine.

A surface grinder is a standard machine tool for precision flat grinding. The KB's 950 kg mass is plausible for a small industrial manual or automatic surface grinder. It should remain distinct from a bench grinder, polishing station, cylindrical grinder, bearing grinder, and ball mill; those all grind material, but their geometry and workholding are different.

# Evidence links

- Chevalier lists grinding machines including manual, semi-automatic, fully automatic, CNC SMART surface grinders, vertical grinders, double-column grinders, and 5-axis grinding centers: https://www.chevalierusa.com/grinding-machine.html
- Chevalier's product overview lists manual surface grinders, fully automatic surface grinders, and semi-automatic surface grinders as commercial product families: https://www.chevalierusa.com/
- A used Chevalier FSG-818AD listing gives typical small surface-grinder details: 8 in x 18 in table, magnetic chuck, hydraulic longitudinal travel, and variable table speed: https://www.normanmachinetool.com/product/chevalier-8-x-18-automatic-precision-surface-grinder-fsg-818ad/
- Okamoto GX-series listing shows commercial surface grinders with permanent/electromagnetic chucks, coolant/magnetic separator options, 2-5 hp spindles, 8 x 21.6 in to 20 x 41.3 in table areas, and weights from 3,810 to 10,580 lb: https://www.titanmachinerysales.com/itemdetail/820GX
- Disha describes surface grinders as machines for very smooth, precise flat surfaces using a rotating abrasive wheel under coolant/lubrication: https://dishaagroup.com/surface-grinder/
- H. Schmidt notes high-quality flat surface grinding setup depends on magnetic chuck installation and maintenance, wheel selection/balancing, and diamond selection: https://www.hschmidt.com/qa/achieve-high-quality-flat-surface-grinding-results/

# Commercial alternatives

Commercial alternatives include:

- Manual surface grinder with permanent magnetic chuck: lowest complexity and good fit for early small-shop precision work.
- Hydraulic automatic surface grinder: better repeatability and productivity.
- CNC surface grinder: more capable but requires controls, drives, and software.
- Double-column surface grinder: for large plates and large precision surfaces.
- Cylindrical grinder: separate machine for round shafts, rolls, and bearing races.
- Lapping/honing/polishing machines: separate finishing technologies for very fine finish or optical surfaces.

# Build or open-source references

The KB assembly recipe is plausible as a final assembly of prebuilt subassemblies, but the subassemblies are hard to manufacture:

- rigid, stable base/casting or welded frame,
- precision-ground table ways and column ways,
- low-runout grinding spindle with high-quality bearings,
- accurate table feed/cross feed,
- magnetic chuck or equivalent workholding,
- wheel guard, dresser, coolant filtration, and dust/sludge handling,
- metrology and scraping/alignment capability.

Small DIY belt-grinder "surface grinder attachments" exist, but they are not equivalent to a 950 kg precision surface grinder. For KB realism, local manufacture should depend on an existing precision machining/metrology chain rather than being treated as simple assembly.

# Related machine research

Related local reports:

- `cnc_mill.md`
- `milling_machine_general_v0.md`
- `inspection_tools_basic.md`
- `cutting_tools_general.md`
- `work_rest_adjustable.md`
- `press_brake_die_set.md`
- `dies.md`

Related KB items include `grinder_cylindrical_v0`, `bearing_grinding_machine_v0`, `precision_grinding_system_v0`, `grinding_wheels`, and `magnetic_chuck_surface_grinder`.

# Recommendation for KB realism

Keep `surface_grinder` as a real machine.

Recommended refinements:

- Preserve it as the default flat-surface precision grinder, as existing dedupe notes already suggest.
- Do not use it as the only grinder for cylindrical rolls, bearing races, balls, or internal/external diameters; use cylindrical/bearing-specific grinders where geometry matters.
- Keep `grinding_wheels` separate as consumable/tooling; the grinder is incomplete without appropriate wheels and dressing.
- Add wheel dresser, guards, coolant filtration/sludge handling, and metrology dependencies if future KB edits expand the BOM.
- Treat imported controls as optional for a manual variant; a fully manual grinder can be useful without CNC compute, though drives and spindle control remain necessary.

# Confidence and open questions

Confidence: high that the item is real; high that the KB mass/BOM are plausible; medium that all current process references are scoped correctly because some finishing/polishing processes may need lapping, polishing, or cylindrical grinding instead.

Open questions:

- Is the intended default grinder manual, hydraulic automatic, or CNC?
- Should `mirror_polishing_v0` require separate lapping/polishing equipment after surface grinding?
- Should the KB distinguish flat surface grinding from precision grinding of shafts, races, balls, and rolls more consistently?
