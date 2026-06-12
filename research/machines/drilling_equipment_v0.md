# Drilling equipment v0

## Machine identity

- KB ID: `drilling_equipment_v0`
- KB name: Drilling equipment (field/mining)
- KB file: `kb/items/machines/drilling_equipment_v0.yaml`
- KB kind: `machine`
- Current KB mass: 500 kg
- Current KB structure: rotary drill head, diamond/carbide bits, drill string/casing, electric or hydraulic power transmission, cooling/lubrication, and cuttings removal.

## KB usage and needed function

The KB uses `drilling_equipment_v0` for subsurface and polar-resource operations:

- `kb/processes/regolith_mining_polar_psc_v0.yaml` requires it for ice-cemented polar regolith that cannot be treated as simple loose excavation.
- `kb/processes/polar_water_ice_extraction_v0.yaml` requires it for accessing polar water ice.
- `kb/recipes/recipe_regolith_polar_psc_v0.yaml` notes that polar permanently shadowed crater regolith needs drilling equipment and heliostat infrastructure.

This is not a drill press or general shop drilling machine. The needed function is field drilling: penetrating hard frozen regolith, extracting or loosening subsurface material, handling drill string/tooling, and removing cuttings.

## Reality classification

Classification: real practical machine category, but broad.

`drilling_equipment_v0` is a generic category rather than a single machine. It maps to compact geotechnical, exploration, water-well, auger, or core drilling rigs. For the KB's polar regolith use case, it should be interpreted as a compact field drilling rig or auger/coring system.

The 500 kg mass is plausible for a compact, mobile, lightweight rig or robotic lunar drilling payload with support equipment. It would be too low for many full-scale truck, track, or deep mineral exploration rigs, so the KB should not imply deep terrestrial mining capability.

## Evidence links

- Epiroc sells core drilling rigs for surface and underground exploration and describes core drilling as specialized equipment for demanding exploration drilling environments. Source: https://www.epiroc.com/en-us/products/drill-rigs/exploration-drill-rigs/core-drilling-rigs
- Geoprobe manufactures drilling rigs and tooling for water well, geothermal, geotechnical, environmental, exploration, construction, and foundation drilling; it also describes compact surface drill rigs for exploration. Source: https://geoprobe.com/ and https://geoprobe.com/applications/exploration/exploration-drilling-rigs
- Central Mine Equipment Company lists drill rigs for subsurface investigation in geotechnical, environmental, mineral exploration, water well, and construction industries. Source: https://cmeco.com/drill-rigs.html
- NASA's PRIME-1 mission includes the TRIDENT drill, intended to extract lunar regolith up to about three feet below the surface and support water/resource analysis. Source: https://www.nasa.gov/mission/polar-resources-ice-mining-experiment-1-prime-1/

## Commercial alternatives

Commercial alternatives include:

- Compact geotechnical drill rig.
- Portable core drilling rig.
- Auger drilling rig for shallow subsurface access.
- Water-well or geothermal drill rig for deeper drilling.
- Robotic lunar drill/auger payload for shallow volatile prospecting.

For the current KB, a compact field drilling rig is the best interpretation. It should not be merged with `drill_press`, which serves shop machining and is not suitable for subsurface ice/regolith access.

## Build or open-source references

Build references exist for simple water-well and hydro-drill rigs, but they are usually informal workshop projects rather than robust mining equipment:

- Public DIY hydro-drill builds show trailer or frame-mounted rigs assembled from basic steel fabrication, drill, grinder, and welding tools. Example search result: https://www.youtube.com/watch?v=79wHBi92w6c
- DIY water-well drilling rig plans are commercially circulated, but quality varies and they should not be treated as validated industrial designs.

The KB item's level of complexity is more realistic as a manufactured rig assembled from modeled parts than as a simple hand-built tool. Drill bits, drill string, seals, bearings, motors, and cuttings removal are the key subassemblies to preserve.

## Related machine research

Related KB machines and parts likely include:

- `drill_press`
- `auger_drill_assembly_v0`
- `drill_string_steel`
- `drill_bit_carbide`
- `rock_crusher_basic`
- `excavator_basic`
- `labor_bot_general_v0`

`drilling_equipment_v0` should remain distinct from `drill_press` and from simple hand tools. It may overlap with `auger_drill_assembly_v0`; if both are retained, `auger_drill_assembly_v0` should be a component or tooling subsystem rather than a parallel machine with the same purpose.

## Recommendation for KB realism

Keep the item, but clarify its name or notes.

Recommended label: compact field drilling rig for polar regolith/ice access.

The current name `drilling_equipment_v0` is broad enough to invite misuse. A clearer ID such as `field_drilling_rig_v0`, `polar_regolith_drill_rig_v0`, or `compact_core_drill_rig_v0` would better match the KB function. Do not replace it with a drill press or generic hand drill.

The 500 kg mass should be documented as a shallow-access, compact rig assumption, not a deep mining or deep water-well rig.

## Confidence and open questions

Confidence: high that this is a real practical equipment category; medium that the exact KB mass and capability are sufficient for polar ice-cemented regolith.

Open questions:

- What depth, diameter, and penetration rate does the KB assume for polar ice extraction?
- Is the drill rotary, rotary-percussive, coring, auger, or thermal?
- Are drill bits, casing, and drill string consumables with finite wear life in abrasive frozen regolith?
- Does the system need a separate mast/feed mechanism, anchoring system, and cuttings conveyance modeled explicitly?
