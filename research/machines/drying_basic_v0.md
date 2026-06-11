# Drying Basic V0

## Machine identity

- KB ID: `drying_basic_v0`
- KB name: not populated in the machine item
- KB file: `kb/items/machines/drying_basic_v0.yaml`
- Current KB type: `machine`
- Current KB mass: 370 kg
- Current KB description: basic drying/curing oven or chamber; placeholder machine based on a drying oven BOM scaled for larger capacity.

## KB usage and needed function

The KB has both:

- `kb/items/machines/drying_basic_v0.yaml` as a machine item.
- `kb/processes/drying_basic_v0.yaml` as a template drying process with the same ID string.

The machine is used as a resource in `drying_and_curing_v0`. Many recipes reference `drying_basic_v0` as a process, not as a machine, including ceramic, refractory, powder, glass-batch, capacitor, sensor, and insulation recipes.

The machine's needed function is a heated drying/curing chamber for removing moisture or volatiles and curing coatings, ceramics, refractory mixes, powders, or similar materials.

## Reality classification

Classification: real practical machine category, but the KB entry is ambiguous and likely duplicative.

Industrial drying ovens, forced-air lab ovens, cabinet ovens, batch ovens, conveyor ovens, and curing ovens are real equipment. The KB description maps to an industrial drying oven or curing chamber. However, the KB already has `drying_oven`, a clearer 120 kg machine with name, material class, process support, 50-300 C range, air circulation, heating elements, and temperature control.

The `drying_basic_v0` machine appears to be a larger-capacity placeholder or duplicate rather than a distinct machine concept. The same ID also being used for a process increases confusion.

## Evidence links

- International Thermal Systems, "Drying Oven": describes industrial drying ovens as equipment that removes water or other liquid from materials, with batch or conveyor configurations and engineered exhaust. Source: https://www.internationalthermalsystems.com/industrial-ovens/drying-oven/
- Carbolite, "Drying Ovens": describes fan-assisted drying ovens with chamber air circulation, moisture extraction, and stoving/curing options. Source: https://www.carbolite.com/products/drying-ovens/
- LEWCO, "Drying Ovens": describes industrial drying ovens for manufacturing processes including paint drying, post-wash drying, and metal finishing, with batch and walk-in models. Source: https://ovens.lewcoinc.com/applications/drying-ovens/
- Thermal Product Solutions, "Industrial Ovens": lists industrial ovens for processes ranging from annealing and drying to laboratory testing, including batch and laboratory ovens. Source: https://www.thermalproductsolutions.com/product-lines/industrial-ovens
- BEING Scientific forced-air drying oven: example of a forced-air oven with ambient+10 C to 300 C range, PID temperature control, convection, adjustable exhaust, and overtemperature protection. Source: https://www.beinglab-usa.com/lab-equipment/product/forced-air-drying-oven-19

## Commercial alternatives

- Laboratory forced-air drying ovens.
- Industrial cabinet/batch drying ovens.
- Walk-in or truck-in drying/curing ovens for larger parts.
- Conveyor drying ovens for continuous production.
- Vacuum drying ovens for lower-temperature drying or oxidation-sensitive materials.

## Build or open-source references

Basic drying ovens can be built from an insulated chamber, heating elements, fan/air circulation, temperature sensor, PID controller, exhaust/venting, and safety cutoff. The challenge is not conceptual feasibility but safe operation, temperature uniformity, off-gas handling, and fire/explosion risk when drying solvents or flammable volatiles.

For the KB, a locally fabricated drying oven is plausible if heating elements, insulation, sheet metal, fan/motor, controller, and temperature sensors are available. This matches the existing `drying_oven` item better than the ambiguous `drying_basic_v0` machine.

## Related machine research

Related KB entries:

- `drying_oven`
- `drying_basic_v0` process
- `drying_and_curing_v0`
- `furnace_high_temp`
- `annealing_oven_small`
- `curing_oven` is already noted in local dedupe docs as consolidated into `drying_oven`

The local dedupe decision for low-temperature ovens explicitly keeps `drying_oven` as the primary low-temp drying/curing oven and preserves `annealing_oven_small` for higher-temperature stress relief. That suggests `drying_basic_v0` should be reviewed as a duplicate or naming artifact.

## Recommendation for KB realism

Keep the real-world concept, but consider consolidating or renaming.

Best future cleanup recommendation:

- Use `drying_oven` as the canonical machine for low-temperature drying/curing.
- Keep `drying_basic_v0` as a process ID only, or rename the machine to something distinct such as `drying_chamber_large_v0` if the 370 kg larger-capacity chamber is genuinely needed.
- Add a `name` and `material_class` if the machine remains.
- Avoid having a machine and process with the same ID string, because this makes research, queue work, and simulation interpretation harder.

Do not replace with labor-only work. Labor can load/unload and inspect, but controlled heating, airflow, and venting are the machine function.

## Confidence and open questions

Confidence: high that drying/curing ovens are real practical equipment; medium-low that `drying_basic_v0` should remain a separate machine from `drying_oven`.

Open questions:

- Does the 370 kg machine represent a large drying chamber distinct from the 120 kg `drying_oven`?
- Should recipes using process `drying_basic_v0` require `drying_oven` rather than `furnace_high_temp`?
- Should the machine ID be renamed to avoid collision with process `drying_basic_v0`?
