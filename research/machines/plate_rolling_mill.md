# Plate rolling mill

## Machine identity

- KB ID: `plate_rolling_mill`
- KB file: `kb/items/machines/plate_rolling_mill.yaml`
- KB name: Plate rolling mill
- KB mass: 1501 kg per unit
- Current KB role: canonical rolling mill for converting ingots, billets, slabs, and stock into plate, sheet, strip, and bar through roll reduction.

## KB usage and needed function

Local usage shows this is a central metal-forming machine:

- It is listed in the minimal/self-reproducing machine set.
- It is used by rolling processes for steel bar stock, steel stock, steel strip, copper sheet/strip, nickel sheet, brass sheet, and generic metal sheet.
- `docs/dedupe_decisions.md` explicitly keeps `plate_rolling_mill` as the canonical rolling mill, consolidating the older `rolling_mill`.
- It is also used in some sheet metal forming processes as the default forming tool after press-brake/roller consolidation.
- Its item notes describe heavy rollers compressing heated metal through multiple passes.

The needed function is flat rolling/reduction, not primarily rolling plate into cylinders. It should be understood as a small rolling mill for plate/sheet/bar production with work rolls, frame, drive, roll adjustment, and possibly heating/reheating support.

## Reality classification

Classification: real practical machine.

Rolling mills are standard metalworking machines. The KB's use of one small canonical rolling mill is conservative and reasonable for coarse self-reproduction modeling, as long as its scope is documented. The name "plate rolling mill" can be ambiguous because "plate rolling" is also used for roll-bending flat plate into cylinders. In this KB, the notes and process references point to flat rolling/reduction.

## Evidence links

- Primetals describes plate mill solutions for producing plates and coils with controlled surface quality, flatness, mechanical properties, and automation: https://www.primetals.com/en/portfolio/solutions/hot-rolling/plate-mill/
- Element Machinery sells rolling mill machinery for steel rolling, steel plate rolling, and metal processing: https://elementmachinery.com/products/metal-processing/rolling-mill/
- International Rolling Mills lists 2-high, 4-high, laboratory, hot, cold, wire/rod, strip, and other rolling mill types: https://www.introllingmills.com/categories/5287-rolling-mills
- A Sente Software hot rolling note describes plate rolling mills as mostly reversing mills that reduce stock thickness pass by pass: https://www.sentesoftware.co.uk/site-media/hotrolling
- US Korea Hotlink describes forged and cast steel work rolls and related rolls for steel mills and processing lines: https://www.uskoreahotlink.com/products/manufacturing/precision-industrial-rolls-shafts/
- Cooksongold's rolling mill guide shows the same basic mechanism at jewelry scale: sheet metal is annealed, fed through rollers, and reduced by adjusting the roller gap: https://www.cooksongold.com/blog/learn/how-to-use-a-rolling-mill-for-jewellery-making-a-beginners-guide-2/

## Commercial alternatives

Commercial alternatives include:

- Laboratory 2-high rolling mills for small sheet/strip work.
- 4-high and cluster mills for thinner sheet and improved stiffness.
- Hot plate mills, Steckel mills, and reversing plate mills for larger steel production.
- Jewelry/light-shop rolling mills for nonferrous thin sheet and wire.
- Plate roll/bending machines for cylindrical shells, which are related but different from flat rolling mills.

For the KB's scale, a small laboratory/light-industrial rolling mill is more plausible than a full steelworks plate mill, but it still requires high roll loads, hardened rolls, strong frame, bearings, gearing, and careful alignment.

## Build or open-source references

- Small jewelry/shop rolling mills show basic manufacturability but only for soft metals and small sections.
- Practical Machinist discussions of micro rolling mills emphasize hardened, ground rolls and strong construction because rolling loads are high and roll defects transfer to product: https://www.practicalmachinist.com/forum/threads/suggestions-to-build-a-micro-rolling-mill.188251/
- Ganoksin discussions similarly emphasize steel, heat-treatable rolls and strong frames for tiny rolling mills: https://orchid.ganoksin.com/t/bootstrapping-a-tiny-but-effective-rolling-mill/37975

These build references support simple mills at small scale, but industrial plate/sheet production requires much more stiffness, roll quality, power, and process control.

## Related machine research

Related local reports:

- `research/machines/press_brake.md`
- `research/machines/spinning_machine_v0.md`

Related KB items:

- `rolling_mill` (deprecated/consolidated)
- `rolling_mill_rolls_set`
- `rolling_cylinders_hardened`
- `press_brake`
- `press_brake_or_roller`
- `steel_forming_press`

No follow-up tasks were enqueued, per task constraint.

## Recommendation for KB realism

Keep `plate_rolling_mill` as the canonical rolling mill.

Recommended cleanup when KB edits are allowed:

- Clarify in notes or display name that this is a flat rolling/reduction mill, not a roll-bending machine for curved shells.
- Keep the current consolidation decision: use this for generic rolling operations unless a process needs a materially different mill.
- Use `press_brake` for straight-line bending and a plate roller/roll bender for cylindrical shell forming if that becomes distinct.
- Review the 1501 kg mass against target width, roll diameter, stock temperature, and material. It is plausible for a very small/light mill, not for heavy industrial plate production.
- Keep roll-set hardness, grinding, bearings, frame stiffness, and alignment as realism-critical notes.

## Confidence and open questions

Confidence: high that the machine is real; medium on whether one canonical mill can cover all current materials and section sizes.

Open questions:

- What maximum sheet/plate width and thickness does the KB require?
- Are hot rolling and cold rolling intentionally sharing one mill?
- Does the mill include reheating/annealing capability, or should that remain separate furnace capacity?
