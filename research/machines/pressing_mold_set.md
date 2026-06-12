# Pressing Mold Set Machine Reality Research

## Machine identity

- KB item id: `pressing_mold_set`
- KB name: Pressing mold set
- KB file: `kb/items/machines/pressing_mold_set.yaml`
- Current KB kind: `machine`
- Current KB mass: 30 kg
- Current BOM: `bom_pressing_mold_set_v0`
- Current recipe: `recipe_pressing_mold_set_v0`

## KB usage and needed function

The item is used for powder pressing, ferrite pressing/shaping, ferrite/toroid processes, ceramic forming, ceramic block fabrication, regolith pellet/block pressing, acid-resistant reactor lining fabrication, and as a component in battery cell sealing and regolith brick press machinery.

The needed function is a set of dies, punches, cavity plates, ejector parts, and mold frames used with a hydraulic/mechanical press to shape powders or green ceramic bodies. It does not provide pressing force by itself.

## Reality classification

Real practical tooling set, not a standalone machine.

Pressing molds and powder-compaction dies are standard equipment for ceramics, powder metallurgy, ferrites, analytical pellets, and battery/electrode materials. The 30 kg mass is plausible for a small set of steel dies and punches. The item should remain separate from `pellet_press` or `hydraulic_press`, because a press frame/actuator without suitable dies cannot form the target geometry.

## Evidence links

- MTI sells laboratory pressing dies, including pellet pressing dies and silicon nitride dies for hot pressing: <https://mtixtl.com/collections/pressing-dies>
- Across International sells pellet press die sets for hydraulic presses, showing dies as separate press tooling: <https://www.acrossinternational.com/collections/pellet-press-dies>
- MetalPress Machinery describes powder pressing as compacting metal, ceramic, or composite powders into green compacts with hydraulic press force control: <https://metalpressmachinery.com/vcompression-molding-powder-pressing-advanced-press-technologies/>
- MSE Supplies sells a lab-scale electric hydraulic pellet press for powder pressing in materials research, metallurgy, ceramics, catalysis, and battery materials: <https://www.msesupplies.com/products/mse-pro-lab-scale-20-ton-electric-hydraulic-pellet-press>

## Commercial Alternatives

- Cylindrical pellet die sets for FTIR/XRF/sample pellets and battery/materials research.
- Custom powder metallurgy compaction dies with punches, core rods, and ejectors.
- Ceramic pressing molds for green body forming.
- Ferrite/toroid pressing dies for magnetic cores.
- Hot-press dies made from graphite, silicon nitride, or other high-temperature materials.

## Build or open-source references

Simple pressing molds can be machined from steel for low-volume ceramic or powder work. Realistic production tooling requires hardened/wear-resistant materials, polished cavity surfaces, controlled clearances, ejector design, powder flow considerations, venting, lubrication, and strength checks for compaction pressure.

The KB recipe is plausible as a coarse fabrication path if precision machining, heat treatment, and surface finishing exist. For abrasive ceramics or high-pressure powder metallurgy, tool steel quality and surface finish are important.

## Related machine research

Related local reports:

- `research/machines/pellet_press.md`
- `research/machines/molding_press_basic.md`
- `research/machines/hydraulic_press.md`
- `research/machines/dies.md`

These all support the distinction between active press machinery and passive mold/die tooling.

## Recommendation for KB realism

Keep the item, but classify it conceptually as press tooling.

Recommended options:

- Keep `pressing_mold_set` separate from `pellet_press` and `hydraulic_press`.
- Treat it as reusable tooling/part set rather than a machine when schema support allows.
- Preserve generic use for coarse modeling, but add part-specific molds where geometry matters, such as ferrite toroids, regolith bricks, battery electrodes, or ceramic blocks.
- Distinguish cold powder pressing dies from hot-press dies if temperature/material compatibility matters.
- Keep the 30 kg mass for a modest die set; larger brick/block molds or production tooling may be heavier.

## Confidence and open questions

Confidence: high that the item represents real practical tooling; high that it should not be treated as a standalone machine; medium on whether one generic mold set should cover all current powder, ferrite, ceramic, and regolith geometries.

Open questions:

- Which processes need dedicated mold geometry versus generic pellet/block dies?
- Should hot pressing use graphite/ceramic tooling rather than steel dies?
- Should die wear and replacement be modeled for abrasive regolith and ceramic powders?
