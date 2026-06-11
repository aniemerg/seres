# Dust collection system

## Machine identity

- KB ID: `dust_collection_system`
- KB name: Dust collection system
- KB file: `kb/items/machines/dust_collection_system_v0.yaml`
- KB kind: `machine`
- Current KB mass: 200 kg
- Current KB structure: cyclone separator body, dust filter cartridges, industrial blower, motor, ductwork, collection hopper, and fasteners.

## KB usage and needed function

The KB uses `dust_collection_system` as support equipment for dusty regolith handling:

- `kb/processes/regolith_crushing_grinding_v0.yaml` requires it alongside a rock crusher and ball mill.
- `kb/processes/regolith_screening_sieving_v0.yaml` requires it alongside a vibrating screen.

The needed function is dust capture and particulate separation during crushing, grinding, screening, and sieving. The BOM and recipe describe a cyclone-plus-filter system with blower, ducting, hopper, and collection components, which is a realistic architecture for coarse and fine particulate control.

## Reality classification

Classification: real practical machine category.

`dust_collection_system` is a generic equipment category rather than a single standardized model. That is appropriate for the KB because the process needs a reusable dust-control function, not a particular commercial SKU.

The current 200 kg mass is plausible for a small industrial or large shop-scale system. It would be low for a full plant baghouse, but reasonable for a compact cyclone/filter collector serving a crusher, mill, or screening station in a minimal manufacturing seed.

## Evidence links

- IQS Directory describes dust collection systems and cyclone collectors, including centrifugal separation into a collection hopper. Source: https://www.iqsdirectory.com/articles/dust-collector/dust-collection-system.html
- Hastings Air Energy Control lists industrial dust collectors including cartridge, baghouse, cyclone, portable, and wet collectors for applications such as grinding, blasting, metal fabrication, cutting, and mixing. Source: https://www.hastingsair.com/products/dust-collectors/
- Nederman MikroPul describes cyclone dust collectors as pre-separators that reduce dust load reaching final filters and protect filter media. Source: https://www.nedermanmikropul.com/en/products/cyclone-separators/cyclone-dust-collectors
- Imperial Systems explains cyclone filter systems as spinning incoming air so larger particles drop out before finer filtration. Source: https://www.isystemsweb.com/dust-collection-equipment/cyclone-dust-collectors/

## Commercial alternatives

Commercial alternatives include:

- Small industrial cyclone dust collector with cartridge or bag filter.
- Cartridge dust collector for fine dust.
- Baghouse collector for heavier continuous dust load.
- Portable dust collector or shop cyclone collector for smaller machines.
- Wet dust collector if the dust is hazardous, combustible, or difficult to handle dry.

For the current KB usage, a cyclone-plus-filter collector is a good conservative abstraction. Regolith processing will likely create abrasive dust, so cyclone pre-separation before filters is more realistic than filters alone.

## Build or open-source references

Open build references exist at shop scale:

- Bill Pentz provides cyclone dust collector design information, drawings, and scaling guidance: https://billpentz.com/woodworking/cyclone/cyclone_plan.php
- Instructables has a "Dust Cyclone Cart" build guide: https://www.instructables.com/Dust-Cyclone-Cart/
- DIY Builds documents converting a 2 HP dust collector into a two-stage cyclone separator using sheet metal: https://www.diybuilds.ca/cyclone-dust-collector.html

These references are woodshop-oriented, not lunar-regolith-specific, but they support the manufacturability of cyclone bodies, ducting, blower integration, and collection bins. Filter media and abrasive wear surfaces may still need specific materials in the KB.

## Related machine research

Related queue items and KB equipment likely include:

- `vibrating_screen_v0`
- `rock_crusher_basic`
- `ball_mill_v0`
- `screening_equipment`
- `vacuum_pump_small`
- `vapor_capture_system_v0`

The dust collector should remain a support system for comminution and screening rather than being merged with the crusher, mill, or screen.

## Recommendation for KB realism

Keep the item as a real generic machine category.

Recommended clarification: define it as a small industrial cyclone-plus-cartridge dust collection system for dusty mineral/regolith processing. If the KB later models high-throughput continuous mining, split larger equipment into `cyclone_preseparator`, `baghouse_or_cartridge_collector`, `industrial_blower`, and `ductwork_system`. For the current minimal self-reproduction list, the current combined system is realistic and avoids unnecessary item proliferation.

Consider normalizing duplicate files: both `kb/items/machines/dust_collection_system.yaml` and `kb/items/machines/dust_collection_system_v0.yaml` appear to define the same `id`. That is outside this research task, but it is relevant for future KB cleanup.

## Confidence and open questions

Confidence: high that the machine category is real and that the current BOM architecture is plausible.

Open questions:

- What particle size distribution and dust loading are expected from lunar regolith grinding and screening?
- Does the modeled system need HEPA-level final filtration, abrasion-resistant linings, or explosion/combustion mitigation?
- Should consumable filter cartridges be modeled as replaceable parts with lifetime assumptions?
