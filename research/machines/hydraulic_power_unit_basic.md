# Hydraulic power unit basic

## Machine identity

- Queue item: `machine_reality_hydraulic_power_unit_basic`
- KB ID: `hydraulic_power_unit_basic`
- KB file: `kb/items/machines/hydraulic_power_unit_basic.yaml`
- KB name: Hydraulic power unit (basic)
- KB kind: `machine`
- KB modeled mass: 150 kg

The KB defines this as a basic hydraulic power unit supplying pressurized hydraulic fluid. It includes a hydraulic pump, reservoir, motor, filtration, pressure relief valve, controls, and related hydraulic power/fluid power capabilities. The BOM contains a hydraulic reservoir, pump, valve manifold, small electric motor, power output terminals, and fasteners.

## KB usage and needed function

`hydraulic_power_unit_basic` is used primarily as a subassembly in recipes and BOMs for hydraulic machines:

- `hydraulic_press`
- `hydraulic_press_small`
- `regolith_brick_press_v0`
- `regolith_brick_press_hydraulic_v0`
- `molding_press_basic`
- `forging_press_v0`
- `drilling_equipment_v0`

The needed function is to convert electric motor power into pressurized hydraulic fluid flow for cylinders, presses, clamps, drilling equipment, or other hydraulic actuators. It is a component/subsystem rather than a production machine by itself.

## Reality classification

Classification: real practical machine subsystem / hydraulic power pack.

Hydraulic power units are standard industrial components. The KB's 150 kg mass is plausible for a small-to-medium shop/industrial HPU with reservoir, pump, motor, valve manifold, filtration, and controls. It should remain distinct from `hydraulic_press`: the press is the machine applying force, while the HPU is the hydraulic energy source.

## Evidence links

- Engineering LibreTexts, "Operation of a Hydraulic Power Unit": https://eng.libretexts.org/Courses/Northeast_Wisconsin_Technical_College/Fluids_2%3A_Basic_Hydraulics_%28NWTC%29/02%3A_Power_Units/2.01%3A_Operation_of_a_Hydraulic_Power_Unit
  - Describes the power unit as the part of a hydraulic system that supplies hydraulic energy.
  - Lists key components including electric motor, hydraulic pump, reservoir, suction/supply/return lines, relief valve, suction strainer, filler/breather, level gauge, and return filter.
  - Explains flow from reservoir through pump to actuators and back to the reservoir.

- Parker Hannifin standard hydraulic power units installation and maintenance manual: https://www.parker.com/content/dam/Parker-com/Literature/Hydraulic-Pump-Division/Power-Units-Files/hydraulic-power-units-installation-maintenance-manual.pdf
  - Documents real standard hydraulic power units manufactured by Parker.
  - Describes pump/motor assemblies mounted to reservoir top plates, reservoir nameplates, tank size, pump flow, maximum pressure, and installation/maintenance safety.

- Bailey Hydraulics, "How Does a Hydraulic System Work?": https://www.baileyhydraulics.com/resources/education/how-does-a-hydraulic-system-work/
  - Describes hydraulic valve assemblies controlling direction, pressure, and flow rate.
  - Describes hydraulic cylinders and motors as actuators, and fluid coolers as components preventing overheating.

- ARGO-HYTOS pressure relief valves: https://www.argo-hytos.com/news/product-news/product-news-view/the-different-types-of-pressure-relief-valves-and-their-application-in-hydraulic-systems.html
  - Explains relief valves regulate maximum system pressure and protect hydraulic systems from overpressure.
  - Notes valves return excess flow to the tank and protect hoses, pumps, cylinders, and other components.

## Commercial alternatives

- Catalog hydraulic power packs from Parker, Bosch Rexroth, Bailey, Flowfit, and other fluid power suppliers.
- Custom hydraulic power units sized by pressure, flow, reservoir volume, duty cycle, cooling, filtration, valve stack, and controls.
- Integrated hydraulic units built directly into a machine frame, which may not need a separately modeled HPU item.
- Manual bottle-jack or hand-pump hydraulics for very small presses, not equivalent to this motorized unit.

## Build or open-source references

Small hydraulic power packs can be assembled from commercial or locally manufactured components: reservoir tank, pump, electric motor, coupling, valve manifold, relief valve, filters, hoses/fittings, gauges, breather, and controls. Full local manufacturing of precision pumps, seals, hoses, and valve spools is harder than assembling the unit.

For KB realism, keep this as an assembly of specialized components. Do not hide hydraulic fluid, seals, filters, relief protection, and contamination control if reliability matters.

## Related machine research

Existing related reports:

- `research/machines/hydraulic_press.md`
- `research/machines/metal_forming_basic_v0.md`
- `research/machines/press_brake.md`
- `research/machines/steel_forming_press.md`
- `research/machines/power_hammer_or_press.md`

These reports support the role of the HPU as a reusable subsystem for hydraulic presses and forming equipment.

## Recommendation for KB realism

Keep `hydraulic_power_unit_basic` as a real reusable subsystem.

Specific recommendation:

- Keep separate from `hydraulic_press`; it is a power subsystem used by multiple machines.
- Consider classifying/documenting it as `equipment` or `subassembly` if the KB later distinguishes those from machines.
- Preserve pump, reservoir, motor, valve manifold, relief valve, filtration, and controls in the model.
- Add or document hydraulic fluid, seals, hoses/fittings, pressure gauge, return filter, breather, and cooling if higher fidelity is needed.
- Size-specific variants are not needed unless pressure/flow differs by more than the Conservative Mode 5x rule or specific machines require incompatible ratings.

## Confidence and open questions

Confidence: high.

Open questions:

- What pressure and flow rating does the seed system require?
- Does the 150 kg mass include hydraulic fluid, hoses, filters, and controls?
- Should hydraulic fluid be modeled as a consumable/imported material?
- Can the same HPU serve multiple machines by quick-connect plumbing, or is one unit embedded per machine?

