# Rock Crusher Basic

## Machine identity

- KB ID: `rock_crusher_basic`
- KB name: Rock crusher (basic)
- KB file: `kb/items/machines/rock_crusher_basic.yaml`
- Current KB type: `machine`
- Current KB mass: 500 kg
- Current KB description: basic rock crusher for primary size reduction of regolith, ore, and rock; jaw or cone design.

## KB usage and needed function

The KB uses this as the primary size-reduction machine in `crushing_basic_v0`, `crushing_and_screening_basic_v0`, `crushing_and_grinding_v0`, `regolith_crushing_grinding_v0`, `mineral_processing_basic_v0`, and related extraction processes. It is also listed in the minimal self-reproducing set and in `docs/self_reproduction_imported_machines.md`.

The local dedupe notes already identify `rock_crusher_basic` as the canonical crusher, replacing older or duplicate entries such as `crusher_basic` and `jaw_crusher_v0`. That is consistent with conservative-mode reuse.

## Reality classification

Classification: real practical machine / broad but acceptable category.

Rock crushers are standard mining, quarrying, recycling, and mineral-processing machines. The KB item describes a generic jaw or cone crusher rather than a specific model. For the KB's regolith and ore size-reduction role, the most realistic interpretation is a small jaw crusher or compact primary crusher.

The 500 kg mass is plausible for a very small industrial or laboratory/field crusher, though many commercial units are heavier. For example, commercial small jaw crushers can range from compact bench/lab machines up to multi-ton yard machines.

## Evidence links

- Metso, "Crushers": describes jaw crushers as primary crushers that reduce rock and other material between fixed and moving jaws, producing material small enough for conveyors and later crushing stages. Source: https://www.metso.com/aggregates/products/crushers/
- FLS, "Jaw crushers": describes jaw crushers for high-capacity primary crushing in hard rock applications, including mining, quarrying, and recycling. Source: https://fls.com/en/equipment/crushing/jaw-crushers
- Mt. Baker Mining and Metals, "Jaw Crushers": sells ready-to-run jaw crushers with steel skids, motors, bearings, castings, and manganese jaw plates; sizes range from 6 x 10 inches through 20 x 30 inches. Source: https://mbmmllc.com/products/jaw-crushers/
- 911Metallurgist, "5 x 7 high reduction ratio jaw crusher": commercial small jaw crusher for coarse and mid-range primary crushing, using a 5 HP motor and 5 x 7 inch jaw cavity. Source: https://www.911metallurgist.com/equipment/high-reduction-ratio-jaw-crusher
- Open Source Ecology Wiki, "Crusher": describes crushers as machines for reducing material size in mineral processing and recycling, with jaw crushers as the common basic-mining type. Source: https://wiki.opensourceecology.org/wiki/Crusher

## Commercial alternatives

- Small and medium jaw crushers from Mt. Baker Mining and Metals, 911Metallurgist, Retsch, MEKA, McLanahan, Metso, FLS, and similar suppliers.
- Compact laboratory jaw crushers for sample preparation.
- Trailer/skid-mounted small jaw crushers for field ore, concrete, and aggregate crushing.

## Build or open-source references

Open Source Ecology has a crusher concept page, but it is more of a project/wiki reference than a complete validated industrial build package.

911Metallurgist also documents a small homemade jaw crusher kit requiring welding and a supplied motor, which supports the KB's basic fabrication assumption at a very small scale: https://www.911metallurgist.com/blog/diy-homemade-crusher/

The KB recipe is broadly plausible because jaw crushers are mainly steel frame, jaw plates, flywheel/shaft, bearings, motor, gearbox, hopper/feed hardware, and guards. Wear-resistant jaw plates and robust frame alignment are the main realism constraints.

## Related machine research

Related KB entries and notes:

- `jaw_crusher_v0` is deprecated/consolidated into `rock_crusher_basic`.
- `crusher_basic` is deprecated/consolidated into `rock_crusher_basic`.
- `crushing_jaw_set`, `crusher_frame_medium`, `flywheel_medium`, `toggle_mechanism_set`, and `hopper_feed_system` are component-level related items.
- `ball_mill_v0` and other mills should remain separate because crushing and grinding are different stages.

## Recommendation for KB realism

Keep `rock_crusher_basic` as the canonical coarse crusher.

The item is realistic and useful as a generic imported machine. If refined later, document it specifically as a small jaw crusher rather than "jaw or cone" because the current BOM and recipe are jaw-crusher shaped. Do not split unless the KB needs separate throughput classes; the existing 5x magnitude reuse policy supports keeping one coarse item.

The 500 kg mass should be treated as a compact/light crusher estimate. If higher-throughput regolith processing becomes important, add a recipe/process note or variant rather than creating duplicate crusher IDs immediately.

## Confidence and open questions

Confidence: high that this is a real practical machine and appropriate for the KB.

Open questions:

- Whether the canonical item should be renamed or described as `jaw_crusher_basic` to match its BOM.
- Whether the process throughput assumptions should be revisited if the 500 kg mass is intended to represent more than a lab/field crusher.
- Whether remaining deprecated crusher references should be manually migrated in future KB cleanup.
