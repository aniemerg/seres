# Machine identity

- Queue item: `machine_reality_welding_power_supply_v0`
- KB item: `welding_power_supply_v0`
- KB name: Welding power supply v0
- KB file: `kb/items/machines/welding_power_supply_v0.yaml`
- Current KB kind: `machine`
- Current mass: 99 kg
- Current BOM: `bom_welding_power_supply_v0`
- Current recipe: `recipe_machine_welding_power_supply_v0`

# KB usage and needed function

`welding_power_supply_v0` is used by general welding and fabrication processes including `welding_basic_v0`, `welding_process_general_v0`, `welding_brazing_basic_v0`, `welding_and_fabrication_v0`, `welding_structural_v0`, `fabricate_structural_steel_frame_v0`, and related assembly/frame processes.

The needed function is active electrical power conversion for arc welding: deliver controlled high-current output with the correct constant-current or constant-voltage behavior for SMAW/stick, TIG/GTAW, MIG/GMAW, flux-cored, or related welding processes. The BOM currently includes the power unit, torch, ground clamp/cables, power conditioning, controls, sensors, and fasteners, so it is closer to a compact welding power-source package than a bare transformer/rectifier.

# Reality classification

Real practical machine.

Welding power supplies are standard industrial equipment. The KB's 99 kg mass is plausible for an older transformer/rectifier or shop-grade multiprocess welder with cables/accessories, though many modern inverter power sources are much lighter. The item should be kept distinct from `welding_tools_set` and from complete process-specific systems such as `welding_tig_unit_v0` or `welding_spot_welder_v0`.

# Evidence links

- TWI explains that the prime objective of an arc welding power source is to deliver controllable welding current at the voltage demanded by the welding process: https://www.twi-global.com/technical-knowledge/job-knowledge/power-source-characteristics-121
- Lincoln Electric explains constant-current versus constant-voltage welding output; CC maintains current while CV maintains voltage, matching different welding processes: https://www.lincolnelectric.com/en/welding-and-cutting-resource-center/process-and-theory/constant-current-vs-constant-voltage-output
- Miller Multimatic 235 is a commercial multiprocess welder with CC/CV output for MIG/flux-cored, stick, and DC TIG, with rated amperage/duty cycle specifications: https://www.millerwelds.com/equipment/welders/multiprocess/multimatic-235-multiprocess-welder-240v-m30250
- Miller XMT 450 CC/CV is a commercial multiprocess welding power source with 15-600 A range, CC/CV output, and 55.3 kg net weight: https://millerweldseurope.com/products/xmt-450-cc-cv/
- Miller's welding equipment page lists multiprocess power sources such as XMT units delivering hundreds of amps at substantial duty cycle: https://www.millerwelds.com/
- Lincoln Electric lists welding power sources as equipment selected for power, efficiency, handling, and suitability to the welding need: https://www.lincolnelectric.com/en/Products/Equipment/Training-Equipment/Welding-Power-Sources

# Commercial alternatives

Commercial alternatives include:

- Transformer stick welder: rugged, heavy, simple, mostly SMAW.
- Inverter stick/TIG power source: lighter, more efficient, more electronics-dependent.
- MIG/GMAW CV power source with wire feeder.
- Multiprocess CC/CV welder for stick, TIG, MIG, and flux-cored work.
- TIG-specific AC/DC power source with high-frequency start and gas/cooler integration.
- Resistance spot-welding power supply, which is a distinct high-current short-duration system.

# Build or open-source references

Simple welding power supplies can be built from transformers/rectifiers or adapted DC power sources, but safe, useful welding hardware requires:

- current/voltage control,
- output inductance/filtering appropriate to process,
- thermal management and duty-cycle protection,
- isolation and grounding,
- welding leads, torch/electrode holder, and work clamp,
- arc-start and gas control for TIG if applicable,
- safety-rated enclosure, fusing, and operator protection.

The KB recipe is plausible as assembly from subcomponents. Local manufacture of a rugged transformer-based unit is more plausible than a high-performance inverter power source if power electronics and controls are scarce.

# Related machine research

Related local reports:

- `welding_tig_unit_v0.md`
- `welding_tools_set.md`
- `power_conditioning_equipment.md`
- `power_supply_benchtop.md`
- `high_temperature_power_supply_v0.md`
- `fixturing_workbench.md`

# Recommendation for KB realism

Keep `welding_power_supply_v0` as a real welding machine.

Recommended refinements:

- Define it as a general CC/CV arc-welding power source for basic structural welding unless a process-specific welder is required.
- Keep `welding_tig_unit_v0` for complete TIG/GTAW systems with shielding gas, torch, coolant, and precision weld controls.
- Keep `welding_spot_welder_v0` separate because resistance spot welding has different electrical and mechanical requirements.
- Do not let `welding_power_supply_v0` alone imply shielding gas, wire feed, TIG torch, coolant, PPE, fixturing, or qualified weld procedures.
- Add output current/voltage, duty cycle, input power, process modes, and whether it is transformer or inverter based.

# Confidence and open questions

Confidence: high that this is real and necessary; high that 99 kg is plausible for a shop-grade system; medium on scope because the BOM includes torch/cables and overlaps with complete process-specific welders.

Open questions:

- Is this item intended as a bare power source or a complete basic arc-welding package?
- Which processes require CV/MIG versus CC/stick/TIG?
- Should inverter electronics be imported while transformer/rectifier versions are locally buildable?
