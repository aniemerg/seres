# Drying oven

## Machine identity

- KB ID: `drying_oven`
- KB file: `kb/items/machines/drying_oven.yaml`
- KB name: Drying oven
- KB mass: 120 kg per unit
- Current KB role: low-temperature forced-air drying/curing oven for powders, ceramics, coatings, adhesives, and moisture removal.

## KB usage and needed function

Local usage shows `drying_oven` is the canonical low-temperature oven:

- It is listed in the minimal/self-reproducing machine set.
- It supports `drying_process_oven_v0`.
- Its item notes specify 50-300 C operation, air circulation, insulated chamber, heating elements, and temperature control.
- `docs/dedupe_decisions.md` keeps `drying_oven` as the primary drying/curing oven and treats `curing_oven` as consolidated into it.
- `research/machines/drying_basic_v0.md` identifies `drying_basic_v0` as likely duplicate or naming artifact relative to this clearer item.

The needed function is controlled low-temperature drying, curing, and moisture removal, not high-temperature annealing, kiln firing, sintering, or vacuum drying.

## Reality classification

Classification: real practical machine.

Forced-air drying ovens, cabinet ovens, lab drying ovens, and curing ovens are standard equipment. The KB item's temperature range and component description are realistic for a small industrial/lab oven.

## Evidence links

- International Thermal Systems describes industrial drying ovens as equipment that removes water or other liquid from materials, with batch or conveyor configurations and engineered exhaust: https://www.internationalthermalsystems.com/industrial-ovens/drying-oven/
- Carbolite describes fan-assisted drying ovens with chamber air circulation, moisture extraction, and stoving/curing options: https://www.carbolite.com/products/drying-ovens/
- LEWCO describes industrial drying ovens for paint drying, post-wash drying, metal finishing, and other manufacturing processes: https://ovens.lewcoinc.com/applications/drying-ovens/
- Thermal Product Solutions lists industrial ovens for drying, annealing, laboratory testing, and related thermal processes: https://www.thermalproductsolutions.com/product-lines/industrial-ovens
- BEING Scientific forced-air drying oven examples include ambient+10 C to 300 C range, PID control, convection, exhaust, and overtemperature protection: https://www.beinglab-usa.com/lab-equipment/product/forced-air-drying-oven-19

## Commercial alternatives

Commercial alternatives include:

- Laboratory forced-air drying ovens.
- Industrial cabinet or batch ovens.
- Walk-in/truck-in ovens for large assemblies.
- Conveyor ovens for continuous production.
- Vacuum drying ovens for oxidation-sensitive or low-temperature drying.
- Higher-temperature annealing ovens/kilns for stress relief or ceramic firing.

For current KB use, a cabinet forced-air oven is the right analogy.

## Build or open-source references

A basic drying oven can be built from:

- Insulated sheet-metal chamber.
- Electric heating elements.
- Fan/air circulation.
- Temperature sensor and PID/controller.
- Exhaust/venting and overtemperature cutoff.
- Shelves/trays and basic safety interlocks.

Local fabrication is plausible if heating elements, insulation, sheet metal, fan/motor, controller, and temperature sensors are available. The main hazards are fire, overheating, fumes, solvent vapors, and poor temperature uniformity.

## Related machine research

Related local report:

- `research/machines/drying_basic_v0.md`

Related KB items:

- `drying_basic_v0`
- `curing_oven` (consolidated per docs)
- `annealing_oven_small`
- `furnace_basic`
- `kiln_basic`

No follow-up tasks were enqueued, per task constraint.

## Recommendation for KB realism

Keep `drying_oven` as the canonical low-temperature drying and curing oven.

Recommended cleanup when KB edits are allowed:

- Continue using `drying_oven` for 50-300 C drying, stoving, and adhesive/coating cure.
- Do not use it for high-temperature annealing, ceramic firing, sintering, or vacuum drying unless explicitly upgraded.
- Review `drying_basic_v0` for possible consolidation into this item.
- Preserve `annealing_oven_small` only for genuinely higher-temperature heat treatment.
- Add notes for solvent/off-gas handling if processes dry flammable or hazardous materials.

## Confidence and open questions

Confidence: high that the item is real and correctly modeled at coarse level.

Open questions:

- What chamber volume and batch mass does the 120 kg oven represent?
- Do any processes require vacuum drying or inert atmosphere?
- Are exhaust, condensation, and volatile/waste handling modeled for wet materials?
