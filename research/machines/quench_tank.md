# Quench tank

## Machine identity

- Queue item: `machine_reality_quench_tank`
- KB ID: `quench_tank`
- KB file: `kb/items/machines/quench_tank.yaml`
- KB name: Quench tank
- KB kind: `machine`
- KB modeled mass: 200 kg

The KB defines this as a tank for rapid cooling of heat-treated parts using water, oil, or polymer quenchant with optional agitation. Its BOM includes a steel tank shell, agitation pump, lid/basket, level sensor, power conditioning, sensor suite, imported control compute module, and fasteners.

## KB usage and needed function

`quench_tank` is used by `heat_treatment_basic_v0`.

The needed function is immersion quenching after heating, with enough liquid capacity, agitation, safety provisions, and part-handling support to cool parts reproducibly. For oil quenching, fire safety and lid/overtemperature controls can matter. For water or polymer quenching, agitation and temperature management matter for uniformity and distortion control.

## Reality classification

Classification: real practical machine/equipment, with a spectrum from simple tank to controlled industrial quench system.

The KB item is not a placeholder. Quench tanks are standard heat-treatment equipment. The KB's 200 kg mass is plausible for a small industrial or shop-scale quench tank with pump/agitation and controls. It is heavier and more capable than a simple blacksmith bucket or pipe tank, but far smaller than large integrated quench systems used with production furnaces.

## Evidence links

- Kleenair custom quench tanks: https://www.kleenairusa.com/industrial-furnaces-ovens/quenching-systems
  - Commercial quench tanks are integrated with industrial furnaces for water, oil, or polymer quenching baths.
  - The source describes rapid transfer from heat source to bath and lists heat-treatment benefits such as hardness, toughness, wear resistance, and retained structure.

- L&L Special Furnace agitated heated oil quench tank: https://llfurnace.com/blog/press-release-ll-special-furnace-ships-an-agitated-heated-oil-quench-tank/
  - Commercial example of a small heated oil quench tank for tool steels.
  - Includes 65 gallons of oil, impeller agitation with an explosion-proof motor, immersion heater, safety lid, overtemperature protection, optional coolers, baskets, and production elevators.

- Thermal Processing, "Determining the agitation needed in a quench tank": https://thermalprocessing.com/determining-the-agitation-needed-in-a-quench-tank/
  - Explains that agitation design and motor controls are important for quench tank performance.
  - Shows a polymer quench tank example and discusses flow velocity through the load.

- ASM Digital Library, "Quench System Design": https://dl.asminternational.org/handbooks/edited-volume/194/chapter-abstract/3910213/Quench-System-Design
  - Abstract identifies agitation as critical for quench uniformity and describes agitator types including recirculation pumps, jet mixers, sparging, and impellers.
  - Notes quench tank design affects mechanical properties, hardness, strength, fracture toughness, and distortion control.

- FM Global Data Sheet 7-41, heat treating using oil quenching and molten salt baths: https://www.fm.com/FMAApi/data/ApprovalStandardsDownload?itemId=%7BDFE78408-165A-40FF-8072-45E4CAC5E821%7D
  - Provides loss-prevention guidance for metal heat treatment by immersion or quenching in oil and other liquid media.
  - Highlights fire hazards from ignitable quench liquids and the importance of tank arrangement, liquid quantity, exposed surface area, and equipment construction.

## Commercial alternatives

- Simple open water quench tank: lowest complexity, suitable for rough shop heat treatment where uniformity and fire risk are limited.
- Heated/agitated oil quench tank: appropriate for tool steel and more controlled hardening; may include heater, impeller, safety lid, overtemperature protection, basket/elevator, and cooler.
- Polymer quench tank: used where water/oil tradeoffs are unacceptable; agitation and concentration/temperature control are important.
- Integral quench furnace tank: larger production system integrated with furnace transfer, agitation, cooling, and controls.
- Salt bath quench system: related but materially different and higher hazard; should not be collapsed into the same simple KB item without notes.

## Build or open-source references

Simple quench tanks are commonly shop-built from steel pipe, welded tanks, or fabricated rectangular vessels. A practical controlled quench tank can be built locally from a welded steel tank, lid, basket/fixture, pump or impeller, plumbing, heater/cooler if needed, level/temperature sensors, controls, and guards.

No formal open-source industrial design package was found during this task. For KB realism, "build locally" should still include safety design, fluid compatibility, fire controls for oil, and agitation verification, not just a bare tank.

## Related machine research

Existing related research found:

- `research/machines/glass_furnace_v0.md`

Related KB items for future comparison include `heat_treat_furnace`, `controlled_atmosphere_chamber`, `temperature_controller_module`, `agitation_pump_small`, and `tank_shell_steel` if they appear in the imported-machine list.

## Recommendation for KB realism

Keep `quench_tank` as a real machine/equipment item.

Recommended interpretation:

- Keep as a small controlled quench tank, not merely a passive container.
- The BOM is realistic in concept: tank shell, agitation, lid/basket, sensors, and controls are all plausible.
- Consider clarifying whether the modeled quench medium is water, oil, or polymer for each heat-treatment process. The equipment and safety requirements differ.
- If future KB cleanup permits, distinguish a simple `quench_tank_basic` from a `heated_agitated_oil_quench_tank` only if process realism requires it. Otherwise the generic item is acceptable under Conservative Mode.
- Include fire safety and ventilation assumptions for oil quench tasks, and agitation/temperature control assumptions for polymer/water quench tasks.

## Confidence and open questions

Confidence: high.

Open questions:

- Does `heat_treatment_basic_v0` require oil, water, or polymer quench behavior?
- Should the quench tank consume/contain a modeled quenchant inventory, or is the quenchant treated as part of machine operation?
- Is 200 kg the right mass for the modeled capacity? It is plausible for a small controlled tank, but capacity should be checked against the largest heat-treated part batch.

