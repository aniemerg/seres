# Molding Press Machine Reality Research

## Machine identity

- KB machine id: `molding_press`
- KB name: Molding press
- KB file: `kb/items/machines/molding_press.yaml`
- Current KB mass: 285 kg
- Current BOM: `bom_molding_press`
- Current recipe: `recipe_molding_press_v1`

## KB usage and needed function

The item is used by `graphite_molding_v0`. Most other plastic, rubber, elastomer, silicone, and basic molding processes use `molding_press_basic`.

The needed function is pressing material inside a mold under controlled force, alignment, and possibly heat. For graphite molding, the likely need is powder/graphite compaction in a mold, potentially followed by baking/sintering or high-temperature treatment depending on the product.

## Reality classification

Real practical machine category, but likely duplicate or near-duplicate of `molding_press_basic`.

Compression molding presses, powder compaction presses, and hydraulic platen presses are real. The KB's 285 kg mass is plausible for a small lab/light shop hydraulic molding press and very close to `molding_press_basic` at roughly 300 kg. The current note explicitly says to refine with variants such as `molding_press_basic`, suggesting this unversioned item is a broad placeholder.

## Evidence links

Evidence from `research/machines/molding_press_basic.md` applies:

- Alma Machinery lists compression molding presses with heated platens, tonnage ratings, daylight, stroke, and controls for plastics, rubber, foam, and composites: <https://www.almamachinery.com/for-sale/used-presses/hydraulic-presses/compression-molding-presses/>
- MetalPress Machinery describes powder pressing as compacting metal, ceramic, or composite powders into green compacts using hydraulic presses: <https://metalpressmachinery.com/vcompression-molding-powder-pressing-advanced-press-technologies/>
- MSE Supplies sells laboratory pellet/powder pressing equipment for materials research, metallurgy, ceramics, catalysis, and battery materials: <https://www.msesupplies.com/products/mse-pro-lab-scale-20-ton-electric-hydraulic-pellet-press>
- Carver sells manual and automatic hydraulic laboratory presses used for molding, laminating, and sample preparation: <https://www.carverpress.com/>

## Commercial alternatives

- Basic hydraulic platen molding press.
- Heated-platen compression molding press for rubber, thermosets, composites, and some plastics.
- Powder compaction press for graphite, ceramic, metal powder, and ferrite parts.
- Hot press for simultaneous heat and pressure at elevated temperature.
- Pellet/tablet press for small cylindrical powder compacts.

## Build or open-source references

The physical machine can be built from a welded or bolted frame, hydraulic cylinder, pump/power unit, platens, controls, and guards. Real mold pressing also requires die/mold tooling, load/pressure measurement, platen parallelism, ejectors, and sometimes heated platens.

For graphite molding, the key unknown is whether the process requires simple cold compaction, warm compression molding with binder, or high-temperature hot pressing. Those should map to different equipment if the process physics matter.

## Related machine research

Related local reports:

- `research/machines/molding_press_basic.md`
- `research/machines/pellet_press.md`
- `research/machines/pressing_mold_set.md`
- `research/machines/hot_press_v0.md`
- `research/machines/hydraulic_press.md`

## Recommendation for KB realism

Prefer consolidation with `molding_press_basic` unless graphite molding needs a distinct service class.

Recommended options:

- Use `molding_press_basic` as the canonical basic molding press for ordinary compression molding and cold/warm pressing.
- Keep `molding_press` only if it is redefined as a graphite-specific or powder-compaction press with explicit differences.
- Use `hot_press_v0` if graphite molding requires simultaneous high temperature and pressure.
- Keep `pressing_mold_set` separate as tooling; the press and mold set are not the same item.
- If retained, document whether the press includes heated platens, force rating, daylight, stroke, and ejector capability.

## Confidence and open questions

Confidence: high that molding presses are real; high that this item overlaps with `molding_press_basic`; medium on whether `graphite_molding_v0` needs specialized equipment.

Open questions:

- Should `graphite_molding_v0` use `molding_press_basic`, `hot_press_v0`, or a graphite-specific powder press?
- Is the current 285 kg mass intended to distinguish this from the 300 kg basic press?
- Should unversioned `molding_press`, `molding_press_v0`, and `molding_press_basic` be consolidated?
