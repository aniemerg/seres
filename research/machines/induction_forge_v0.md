# Induction Forge

## Machine identity

- KB ID: `induction_forge_v0`
- KB name: Induction forge
- KB file: `kb/items/machines/induction_forge_v0.yaml`
- Current KB type: `machine`
- Current KB mass: 1800 kg
- Current KB capabilities: `forging`, `induction_heating`
- Current KB description: induction forge for rapid controllable heating of metal billets and bars before forging and heat treatment.

## KB usage and needed function

The KB uses `induction_forge_v0` for:

- `forging_basic_v0`
- `forging_bearing_ring_blanks_v0`
- `bearing_set_heavy_production_v0`
- `fastener_kit_medium_production_v0`
- `electrical_steel_production_v0`
- `machine_frame_small_casting_v0`
- `motor_housing_casting_v0`

It also appears in simulation learning notes and the minimal self-reproducing set. The needed function is rapid localized or full-section heating of conductive metal stock to forging or heat-treatment temperature before deformation by a press/hammer or before thermal fitting.

## Reality classification

Classification: real practical machine, but current canonical BOM is incomplete.

Induction forging/heating is a standard industrial method for heating bars, billets, bar ends, and other conductive workpieces before hot forming. Small induction forges also exist for blacksmithing and toolmaking. The machine class is realistic and distinct from a fuel-fired forge because heat is generated electromagnetically in the workpiece.

The KB mass of 1800 kg is plausible for an industrial billet/bar induction heating cell with frame, coil station, power supply, cooling system, controls, and handling. It is far too high for a small 15 kW blacksmith induction forge, but plausible for a production-oriented system. The current canonical BOM and recipe are not realistic for induction heating because they mostly contain a steel frame, motor, shafts, bearings, and fasteners. The ISRU recipe is closer because it includes heating elements/coil, insulation, power conditioning, and control compute.

## Evidence links

- Coal Iron Works sells an induction forge for quick, precise heating during forging and heat treating, including a pre-connected industrial chiller, amperage control, and interchangeable coils. Source: https://coaliron.com/products/induction-forge
- Inductotherm describes Inductoforge induction billet heating systems for forge shops to heat material quickly and uniformly before forging. Source: https://inductothermgroup.com/products/inductoforge-induction-billet-heating-systems-for-forging/
- Interpower Induction describes induction bar heating systems that use electromagnetic induction to heat bars, rods, and billets to forging temperature without direct contact or open flame. Source: https://www.interpowerinduction.com/applications/heat-processes/forging/bar-heating/
- TY Induction describes billet/bar induction heating equipment for billets from 25 mm to 150 mm diameter and temperatures from 900 C to 1300 C, used before hot forming by forging. Source: https://www.ty-induction.com/induction-billet-heating-system-for-forging/billet/bar-induction-total-heating-equipment.html
- FOCO Induction states that bar induction heating machines include medium-frequency induction power supply, compensating capacitors, induction coils, water cooling systems, and material conveying/loading systems. Source: https://www.focoinduction.com/induction-heating-equipment/induction-heating-system-for-forging/induction-bar-heating-system/
- AZoM describes induction heating for forging as a clean, non-contact method generally used for heating metal billets and bar ends before forging. Source: https://www.azom.com/article.aspx?ArticleID=8400

## Commercial alternatives

- Small 15 kW blacksmith induction forge with chiller and interchangeable coils.
- Industrial bar-end induction heater.
- Continuous billet induction heating line with conveyors/pushers.
- Gas or coal forge for lower-electrical-complexity heating.
- Resistance furnace or box furnace for slower bulk heating.
- Induction shrink-fit heater for bearings and thermal fits.

The KB item is closest to an industrial induction billet/bar heating station, not a compact hobby forge.

## Build or open-source references

Small induction heaters are buildable from off-the-shelf power electronics modules, copper tubing coils, water cooling, resonant capacitors, power supplies, and controls. However, a robust forge-scale system requires:

- High-power inverter/RF or medium-frequency power supply.
- Copper induction coils matched to stock geometry.
- Resonant capacitor bank or tank circuit.
- Water chiller/cooling loop for coils and electronics.
- Workpiece handling and insulating supports.
- Temperature measurement, power control, and safety interlocks.
- Shielding, grounding, and electromagnetic compatibility controls.

For KB realism, the BOM should include induction coil(s), high-power electronics, capacitor bank, cooling loop/chiller, temperature sensing, and controls. A motor/shaft/bearing set may belong to material handling but is not the core heating mechanism.

## Related machine research

Related reports already present:

- `power_hammer_or_press.md`
- `furnace_high_temp.md`
- `heating_furnace.md`
- `hot_press_v0.md`
- `power_conditioning_equipment.md`
- `high_temperature_power_supply_v0.md`

`induction_forge_v0` pairs naturally with `power_hammer_or_press` and `anvil_or_die_set` for forging workflows. It should remain distinct from generic furnaces where rapid localized heating, clean operation, or electrical control matter.

## Recommendation for KB realism

Keep as a real machine, but refine the BOM and name/scope.

Recommended future wording: "industrial induction billet/bar heater for forging and heat treatment." If the intent is a blacksmith-scale unit, reduce mass substantially. If the intent is a production forging heater, keep the large mass but add explicit induction power supply, capacitor bank, copper coils, cooling/chiller, temperature sensing, controls, and handling hardware.

Do not merge it with generic furnace items unless the process does not need induction-specific fast and localized heating. Do not model it as mainly a motor/shaft/bearing assembly.

## Confidence and open questions

Confidence: high that induction forges/heaters are real and relevant; high that the current BOM is incomplete; medium on the intended scale.

Open questions:

- Is this intended to be a small forge-shop induction heater or a production billet heating line?
- What power level, frequency range, stock diameter, and duty cycle are assumed?
- Should coils be replaceable tooling/consumables?
- Should bearing thermal fitting use this same machine or a smaller induction bearing heater?
