# Heliostat Array System V0

## Machine identity

- KB ID: `heliostat_array_system_v0`
- KB name: HelioStat array system v0
- KB file: `kb/items/machines/heliostat_array_system_v0.yaml`
- Current KB type: `machine`
- Current KB mass: 885 kg
- Current KB description: generic heliostat field configured to direct solar energy to a receiver, with mirrors, actuators, controls, and mounting components modeled separately.

## KB usage and needed function

The KB uses this item in polar/resource processes:

- `polar_water_ice_extraction_v0` uses heliostats for light/heat/power support in permanently shadowed regions.
- `regolith_mining_polar_psc_v0` uses heliostat power for lighting and equipment operation in polar shadowed craters.
- `recipe_heliostat_array_system_v0_v0` assembles the item from `heliostat_frame_v0`, `heliostat_mirror_panel_v0`, `heliostat_actuator_unit_v0`, `heliostat_control_electronics_v0`, and `heliostat_mounting_bracket_v0`.

The needed function is a field or array of sun-tracking mirrors that reflects sunlight toward a receiver or target area. In the lunar polar context, that may mean redirecting sunlight from high-illumination ridges into shadowed operations or concentrating heat on a receiver.

## Reality classification

Classification: real practical system category / array of machines.

Heliostats are real concentrating solar thermal components. A heliostat is a tracking mirror or mirror assembly that aims sunlight at a fixed receiver or target. A heliostat array/field is a coordinated group of these units.

The KB item is realistic if interpreted as a small modular heliostat field. It is not a single monolithic machine in the usual sense, and it should not be confused with a complete utility-scale concentrated solar power tower plant. The 885 kg mass is plausible for a small field or prototype system, but far below industrial CSP fields with hundreds or thousands of heliostats.

## Evidence links

- U.S. Department of Energy, HelioCon: defines a heliostat as a device that tilts a mirror or mirror facets to track the sun and reflect sunlight toward a predetermined target such as a tower receiver. Source: https://www.energy.gov/cmei/systems/heliocon
- DOE, "No Smoke, All Mirrors": describes heliostats as tracking mirrors that focus sunlight onto a receiver at the top of a power tower, heating a working fluid for electricity or industrial process heat. Source: https://www.energy.gov/cmei/systems/articles/no-smoke-all-mirrors-developing-next-generation-heliostats
- HelioCon overview PDF: describes a power-tower CSP plant as a field of heliostat mirrors tracking the sun through the day and year to reflect solar energy to a receiver. Source: https://heliocon.org/resource_download/An_Overview_of_Heliostats_and_Concentrating_Solar_Power_Tower_Plants.pdf
- Sandia National Laboratories, "Tower-based power systems": describes a test facility with 218 individually computer-controlled heliostats producing high flux on a tower target. Source: https://energy.sandia.gov/programs/renewable-energy/concentrating-solar-thermal-technologies/tower-based-power-systems/
- NREL report on concentrating solar-thermal technologies: notes that power tower systems use focused mirrors called heliostats, and each heliostat uses two-axis tracking to focus sun on the tower receiver. Source: https://www.nrel.gov/docs/fy21osti/80574.pdf

## Commercial alternatives

- Utility-scale CSP heliostat fields from concentrated solar thermal vendors.
- Smaller industrial heliostat/solar-thermal demonstrators.
- Dual-axis solar trackers with mirror panels for small receiver/lighting applications.
- Fresnel lens or parabolic dish concentrators where a single receiver/concentrator is more appropriate than a field.

## Build or open-source references

Small solar trackers and DIY heliostats are feasible with frames, mirrors, two-axis actuation, sensors or astronomical tracking, and a controller. Public references include:

- Arduino Project Hub dual-axis solar tracker: https://projecthub.arduino.cc/Aboubakr_Elhammoumi/arduino-solar-tracker-77347b
- Instructables dual-axis solar tracker: https://www.instructables.com/Build-a-Dual-Axis-Solar-Tracker-Using-Arduino/
- Heliowatcher/open-source solar tracker discussion: https://edgeryders.eu/t/open-source-solar-tracker-project-heliowatcher/2732

These are small-scale tracker references, not complete industrial heliostat fields. Scaling requires optical calibration, wind/structural design, field layout optimization, cleaning/maintenance, receiver aiming logic, and safety controls.

## Related machine research

Related KB items:

- `heliostat_frame_v0`
- `heliostat_mirror_panel_v0`
- `heliostat_actuator_unit_v0`
- `heliostat_control_electronics_v0`
- `heliostat_mounting_bracket_v0`
- `solar_concentrator_fresnel`
- `thermal_receiver_assembly`
- `optical_metrology_tools`
- `stewart_platform_calibrator`

The heliostat field overlaps with other solar concentrator entries, but the geometry is distinct: heliostats redirect sunlight to a remote receiver, while Fresnel lenses or dish concentrators focus locally.

## Recommendation for KB realism

Keep, but clarify as a small heliostat array/field module.

Recommended future wording: "Small modular heliostat field for redirecting/concentrating sunlight to a fixed receiver or target; composed of mirror panels, frames, actuators, controls, and mounts." If the KB later models utility-scale CSP or kilometer-scale lunar polar illumination, scale by number of heliostat modules rather than making one generic unit cover all cases.

Do not replace with labor bot plus mirrors. Manual setup may be possible, but operational heliostats need continuous tracking and coordinated aim control.

## Confidence and open questions

Confidence: high that heliostats and heliostat fields are real practical systems; medium that the 885 kg item is appropriately scaled for the current polar mining/extraction use cases.

Open questions:

- Is the item meant to provide heat, light, electrical power support, or all three?
- What mirror area does the 885 kg system represent?
- Should polar illumination and solar thermal concentration be separate machine/process abstractions?
- How should optical metrology and calibration be represented for field alignment?
