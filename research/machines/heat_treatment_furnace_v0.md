# Heat Treatment Furnace v0

## Machine identity

- KB ID: `heat_treatment_furnace_v0`
- KB name: Heat treatment furnace v0
- KB file: `kb/items/machines/heat_treatment_furnace_v0.yaml`
- Current KB type: `machine`
- Current KB mass: 537 kg
- Current KB description: heat treatment furnace for self-replication modeling.
- Current KB BOM: insulated shell, refractory lining, heating elements, temperature controller, sensors, imported control compute, power conditioning, quench racks/baskets, and fasteners.

## KB usage and needed function

The KB uses `heat_treatment_furnace_v0` for:

- `heat_treatment_basic_v0`
- `heat_treat_basic_v0`
- `heat_treatment_cycle_basic_v0`
- `heat_treatment_hardening_v0`
- `annealing_basic_v0`
- `stress_relief_basic_v0`
- `bearing_set_heavy_production_v0`
- `alnico_heat_treatment_v0`

The needed function is controlled thermal cycling of metal parts for hardening, tempering, annealing, stress relief, and magnet/alloy processing. This requires repeatable temperature control, soak times, part handling, and often quenching or controlled atmosphere.

## Reality classification

Classification: real practical machine.

Heat-treatment furnaces are standard industrial and shop equipment. They are distinct from generic heating furnaces because metallurgy requires controlled ramp/soak/cool cycles and temperature uniformity. They are also distinct from reduction furnaces, which focus on chemical reduction and offgas/reductant management.

The KB's 537 kg mass is plausible for a medium chamber furnace or small industrial heat-treatment furnace with insulation, refractory, controls, power, and handling racks. It is heavier than a small benchtop kiln and far lighter than a continuous production line.

## Evidence links

- Abbott Furnace describes industrial heat-treatment furnaces and gives typical hardening, annealing, normalizing, and tempering temperature ranges for steels. Source: https://abbottfurnace.com/industrial-heat-treatment-furnace-guide/
- International Thermal Systems describes heat-treatment furnaces for hardening, annealing, and tempering metals, emphasizing uniform heating and production integration. Source: https://www.internationalthermalsystems.com/2025/12/heat-treatment-furnaces-for-metals-101-hardening-annealing-and-tempering/
- Nabertherm describes furnaces for solution annealing, artificial aging, stress-relief annealing, normalizing, soft annealing, hardening, and tempering of aluminum and steel. Source: https://nabertherm.com/en/processes/foundry/heat-treatment-forms-and-cast-pieces/artificial-ageing-tempering-quenching
- Industrial Physics lists controlled-atmosphere furnace applications including annealing, nitriding, hardening, tempering, brazing, and sintering. Source: https://industrialphysics.com/knowledgebase/articles/application-controlled-atmosphere-ovens-furnaces/
- Linde describes controlled furnace atmospheres for annealing, hardening, carburizing, nitriding, brazing, and related heat-treatment processes. Source: https://www.linde-gas.com/industries/metal-fabrication/heat-treatment/controlled-furnace-atmospheres
- Penn Tool's Nabertherm listing describes annealing, hardening, and brazing furnaces for heat-treating metals, with protective gas boxes and quench tank/cooling station accessories. Source: https://www.penntoolco.com/n41h/

## Commercial alternatives

- Chamber heat-treatment furnace.
- Box furnace or kiln with programmable controller.
- Salt bath furnace for some heat-treatment operations.
- Vacuum furnace for oxidation-sensitive alloys and clean heat treatment.
- Controlled-atmosphere furnace for carburizing, nitriding, bright annealing, and oxidation control.
- Continuous belt or strand furnace for production heat treatment.
- Induction heater/forge for localized heat treatment.

## Build or open-source references

A basic heat-treatment furnace can be locally built from:

- Insulated/refractory chamber.
- Electric heating elements or fuel-fired heat source.
- Thermocouples and programmable temperature controller.
- Power relay/contactors or power electronics.
- Racks, trays, baskets, and tongs.
- Quench tank or cooling station where hardening is required.

Better metallurgy may require temperature uniformity surveys, protective gas, vacuum, oxygen control, calibrated sensors, and quench media management. The KB BOM captures the main chamber/control elements but may need explicit gas atmosphere and quench tank integration for advanced alloys.

## Related machine research

Related reports already present:

- `furnace_high_temp.md`
- `heating_furnace.md`
- `reduction_furnace_v0.md`
- `sintering_furnace_v0.md`
- `induction_forge_v0.md`
- `quench_tank.md`

The existing local research supports using `heat_treatment_furnace_v0` for controlled metal heat-treatment cycles and reserving other furnaces for melting, reduction, sintering, glass, or generic heating.

## Recommendation for KB realism

Keep as a real and useful machine.

Recommended future wording: "programmable chamber heat-treatment furnace for hardening, tempering, annealing, and stress relief." Keep it distinct from `furnace_high_temp`, `reduction_furnace_v0`, and `sintering_furnace_v0`.

If processes require carburizing, nitriding, bright annealing, or oxygen-sensitive alloys, add controlled-atmosphere hardware explicitly. If hardening is modeled, keep quench racks/baskets and link to a quench tank or cooling station.

## Confidence and open questions

Confidence: high that the item is real and appropriately modeled; medium on whether controlled atmosphere is needed for all current uses.

Open questions:

- Does AlNiCo heat treatment need magnetic-field fixtures or special atmosphere?
- Should quench tank be a separate required machine for hardening operations?
- What temperature uniformity and maximum temperature are assumed?
