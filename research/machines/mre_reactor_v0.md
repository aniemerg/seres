# MRE reactor v0

## Machine identity

- KB ID: `mre_reactor_v0`
- KB file: `kb/items/machines/mre_reactor_v0.yaml`
- KB name: MRE reactor v0
- KB mass: 1254.5 kg per unit
- Current KB role: molten regolith electrolysis reactor for extracting oxygen and crude metals from lunar/regolith feedstock.

## KB usage and needed function

Local usage confirms MRE means molten regolith electrolysis:

- It is listed in the minimal/self-reproducing machine set and `min_seed.yaml`.
- It is required by `oxygen_extraction_molten_regolith_electrolysis_v0`.
- It supports recipes for `oxygen_gas_v0` and `regolith_metal_crude`.
- The BOM/recipes include high-temperature reactor vessel and electrode-set parts.
- Related reports for `electrodes` and `electrolysis_cell_unit_v0` identify MRE as a high-temperature electrochemical reactor rather than generic electrolysis.

The needed function is to melt regolith, pass current through the molten oxide mixture, evolve oxygen, and recover reduced metal/metalloid products. This requires roughly 1600-1700 C operation, refractory containment, electrodes, high-current power electronics, oxygen collection, thermal management, and handling of corrosive molten oxide/metal phases.

## Reality classification

Classification: real experimental/pilot technology, not mature commodity equipment.

Molten regolith electrolysis reactors are real research hardware and are under NASA/industry/academic development for lunar ISRU. They are not ordinary commercial machines. The KB item is realistic as an imported or advanced seed machine, but it should carry high technical uncertainty around electrode material, refractory lifetime, oxygen collection, product removal, and thermal control.

## Evidence links

- NASA TechPort describes Molten Regolith Electrolysis as a technology to produce oxygen and metals from raw lunar or Martian regolith: https://techport.nasa.gov/projects/116413
- NASA Kennedy reports testing an extraction reactor that heated about 25 kg of simulated regolith to about 1700 C and passed current through the molten regolith to separate oxygen from metals: https://www.nasa.gov/centers-and-facilities/kennedy/nasa-kennedy-breathes-life-into-moon-soil-testing/
- MIT thesis/research on MRE reactor modeling predicts MRE-based ISRU systems and explores reactor design/performance: https://dspace.mit.edu/entities/publication/be50a699-718a-447f-b6ed-c15ec7f417ba
- Advanced Concepts for Molten Regolith Electrolysis discusses operation above 1600 C, cold-walled reactor designs, Joule heating, and electrode material challenges: https://www.hou.usra.edu/meetings/lunarisru2019/pdf/5100.pdf
- Blue Origin describes Blue Alchemist as using molten regolith electrolysis to extract iron, silicon, aluminum, and oxygen from molten regolith: https://www.blueorigin.com/news/blue-alchemist-powers-our-lunar-future
- Tech Briefs describes cathode assemblies for MRE and notes operation near 1600 C: https://www.techbriefs.com/component/content/article/9916-cathode-assembly-for-molten-regolith-electrolysis

## Commercial alternatives

There are no straightforward commodity commercial MRE reactors comparable to a normal furnace or electrolyzer.

Adjacent alternatives include:

- NASA/industry prototype MRE systems.
- Molten oxide electrolysis laboratory reactors.
- Molten salt electrolysis systems for lower-temperature oxygen extraction approaches.
- Hydrogen reduction, carbothermal reduction, or ilmenite reduction systems for lunar oxygen, each with different feedstock/reagent constraints.
- Generic high-temperature electrolysis cells, furnaces, and oxygen collection systems as component analogs.

For KB realism, this should remain an advanced, imported or difficult-to-build system unless the model explicitly tracks its demanding materials and controls.

## Build or open-source references

No safe hobby/open-source build reference is appropriate for a true MRE reactor. Relevant build evidence is research and prototype literature:

- Research reactors use high-temperature furnaces, refractory containment, specialized electrodes, current feedthroughs, oxygen collection, and atmosphere/vacuum controls.
- Cold-wall and Joule-heated concepts attempt to protect vessel walls by keeping corrosive molten regolith away from the container.
- The most difficult local build issues are refractory/insulation design, high-temperature electrode life, power feedthroughs, oxygen separation, and handling molten metal/regolith.

## Related machine research

Related local reports:

- `research/machines/electrolysis_cell_unit_v0.md`
- `research/machines/electrodes.md`

Related KB items:

- `electrode_set_mre`
- `reactor_vessel_mre`
- `oxygen_collection_system_ffc_v0`
- `ffc_reactor_unit_v0`
- `furnace_high_temp`
- `optical_pyrometer_temperature_sensor_v0`
- `thermocouple_contact_temperature_sensor_v0`

No follow-up tasks were enqueued, per task constraint.

## Recommendation for KB realism

Keep `mre_reactor_v0`, but mark it as advanced experimental ISRU equipment rather than a mature commodity machine.

Recommended cleanup when KB edits are allowed:

- Expand the display name to "Molten regolith electrolysis reactor" so `MRE` is not opaque.
- Keep it distinct from ordinary electrolysis cells and generic chemical reactors.
- Ensure electrode sets are modeled as consumable or maintenance-limited parts if lifetime is uncertain.
- Keep high-temperature sensors, oxygen collection, refractory vessel, power supply, and thermal management as explicit subsystems.
- Consider adding notes that the reactor is plausible but high-risk and probably not first-generation local manufacturing.

## Confidence and open questions

Confidence: high that the technology is real; medium on the KB mass and build assumptions because the technology is still maturing.

Open questions:

- What electrode material and lifetime should be assumed?
- Does the KB reactor use cold-wall Joule heating, an external furnace, or both?
- How are oxygen bubbles, molten metal products, and slag/regolith residue removed?
- Is 1254.5 kg meant to include power electronics, oxygen collection, feed handling, and thermal insulation?
