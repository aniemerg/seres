# Machine identity

- Queue item: `machine_reality_solar_tracking_optional`
- KB item: `solar_tracking_optional`
- KB name: Solar tracking system (optional)
- KB file: `kb/items/machines/solar_tracking_optional.yaml`
- Current KB kind: `machine`
- Current mass: 121.5 kg
- Current BOM: `bom_solar_tracking_optional_v0`
- Current recipe: `recipe_machine_solar_tracking_optional_v0`

# KB usage and needed function

`solar_tracking_optional` is used by `solar_power_generation_basic_v0` alongside `solar_array_v0`, `power_conditioning_equipment`, and `labor_bot_general_v0`. It is also listed in the imported/self-reproducing set.

The BOM contains a tracking mount structure, drive assembly, control unit, position sensor set, terminals, and fasteners. The recipe fabricates a frame, machines pivots/gears/bearing interfaces, integrates motors/control/sensors, and tests tracking motion. This is a realistic functional decomposition for a solar tracker.

The needed function is to point PV modules or solar concentrators toward the sun to increase captured energy. The item is optional because fixed-tilt arrays are also real and often simpler.

# Reality classification

Real practical equipment/subsystem, not a manufacturing machine.

Solar trackers are real commercial equipment. The KB item is best interpreted as the tracker mechanism for a small solar array or concentrator: structural frame plus torque/pivot hardware, drive actuator, control electronics, sensors, and wiring. A 121.5 kg mass is plausible for a small single-axis tracker or a light dual-axis unit, but the KB should not imply this covers a large utility tracker row.

# Evidence links

- NREL/Sandia/SunSpec PV O&M best-practices report covers photovoltaic systems and O&M practices and recognizes design/configuration-dependent maintenance issues, including tracking-related performance and maintenance concerns: https://www.nrel.gov/docs/fy19osti/73822.pdf
- NREL technical report on one-axis trackers frames single-axis solar tracking systems as commercial PV infrastructure where improved reliability, durability, performance, and installation cost matter: https://www.nrel.gov/docs/fy08osti/42769.pdf
- Nextpower's NX Horizon products are commercial single-axis solar trackers for utility PV, showing the category exists at scale with tracker-specific hardware and controls: https://nextpower.com/products/trackers
- Antai Solar describes a tracker system using a slew-drive design, high-strength steel structure, corrosion-resistant coatings, and harsh-environment operation: https://www.antaisolar.com/tracker
- Super Solar's single-axis tracker overview lists core components matching the KB decomposition: torque tube/bearing system, drive motor or actuator, controller/sensor, mounting structure, and foundations: https://www.supersolarpv.com/single-axis-tracker-solar-power-tracking-system
- PNNL's solar PV O&M best-practice page notes that regular O&M keeps arrays operating safely and efficiently, and that tracking system performance monitoring helps identify issues and maximize savings: https://www.pnnl.gov/projects/om-best-practices/solar-photovoltaic

# Commercial alternatives

Commercial options include:

- Fixed-tilt PV racking: simpler, cheaper, lower maintenance, lower energy capture at many sites.
- Single-axis tracker: common for larger ground-mounted PV where energy gain justifies moving hardware.
- Dual-axis tracker: higher pointing flexibility, often more complexity; useful for concentrators or specialized systems.
- Heliostat drive/tracking hardware: related but not identical, because heliostats point reflected sunlight at a target rather than maximize direct PV incidence.

For the KB's small base context, a single-axis tracker is the most conservative interpretation unless a concentrator explicitly needs dual-axis precision.

# Build or open-source references

The KB recipe is broadly plausible:

- fabricate/weld the mount structure,
- machine pivots, bearing seats, gear/actuator mounts, and drive interfaces,
- assemble bearings, drive motor/actuator, gears or slew drive, and frame,
- integrate controller, limit/position sensors, and wiring,
- calibrate and test travel, stow behavior, and pointing accuracy.

Small hobby/open hardware solar trackers also exist, but those are much lighter than this KB item and are not equivalent to a rugged 121.5 kg array tracker. For a serious base model, the commercial tracker architecture is the better analogy.

# Related machine research

- `solar_array_v0.md`: directly related; this tracker is an optional mount/pointing subsystem for the array.
- `power_conditioning_equipment.md`: related electrical BOS equipment, but not a substitute for tracking hardware.
- `power_distribution_bus.md`: related power infrastructure downstream of the array.
- `heliostat_array_system_v0.md`: related sun-tracking infrastructure for reflected/concentrated solar systems.

# Recommendation for KB realism

Keep the item, but classify it as optional solar infrastructure/equipment rather than a generic machine.

Recommended refinements:

- Rename or scope as `solar_tracker_single_axis_small` if the intended scale is one small array.
- If dual-axis concentrator tracking is needed, model that separately because the structure, precision, control, and maintenance burden are different.
- Keep it optional in `solar_power_generation_basic_v0`; fixed mounts should remain a valid lower-complexity path.
- Add operational assumptions when allowed: stow position, dust/abrasion tolerance, lubrication/bearing life, actuator sealing, and maintenance access.
- Do not merge it into `solar_array_v0` if the simulator benefits from optional power-yield upgrades, but document that it is part of the PV balance-of-system rather than a separate production machine.

# Confidence and open questions

Confidence: high that solar trackers are real and practical; high that the KB decomposition is directionally realistic; medium on the 121.5 kg mass because tracker mass depends on panel area, wind/launch/lunar loads, axis count, bearings, and foundations.

Open questions:

- Is this intended for PV panels, a thermal concentrator, or both? A shared item may hide important differences.
- Does the simulation currently apply any generation bonus for including this optional tracker?
- Should the lunar setting prefer fixed or seasonally adjustable mounts because the lunar day/night cycle and dust environment change the economics of active tracking?
