# Vapor Capture System v0

## Machine identity

- KB ID: `vapor_capture_system_v0`
- KB name: Vapor capture system v0
- KB file: `kb/items/machines/vapor_capture_system_v0.yaml`
- Current KB type: `machine`
- Current KB mass: 80 kg
- Current KB description: vapor capture and condensation system for collecting water vapor from thermal extraction and volatile recovery operations.
- Current KB BOM: cold trap module, vacuum pump, piping/fittings, coolant reservoir, compact heat exchanger, sensors, and control panel.

## KB usage and needed function

The KB uses `vapor_capture_system_v0` for:

- `polar_water_ice_extraction_v0`
- `pidgeon_process_magnesium_v0`
- `ammonia_recovery_cao_v0`
- `hcl_recovery_from_cacl2_v0`
- `olivine_carbothermal_reduction_v0`

The KB also has related references to `vapor_condenser_cold_trap`, `cold_trap_module_v0`, `cryogenic_chiller_v0`, thermal water extraction, and ammonia recovery. The needed function is collecting and condensing or freezing vapor streams from heated regolith or chemical reactors, with enough pumping, cooling, heat rejection, and plumbing to move vapor to a capture surface/reservoir.

## Reality classification

Classification: real practical subsystem/system category.

The concept is realistic. Cold traps, condensers, vacuum vapor lines, and chilled collection surfaces are standard in vacuum systems, distillation, laboratory evaporators, and ISRU water-extraction concepts. For lunar polar water, the system may collect vapor as ice on a cold surface rather than immediately as liquid water.

The 80 kg mass is plausible for a small pilot-scale capture system with cold trap, vacuum pump, piping, heat exchanger, coolant reservoir, and controls. It is too generic for every vapor species in the KB: water, ammonia, HCl, magnesium vapor, phosphorus, and mixed volatiles require different temperatures, materials, corrosion handling, and capture chemistry.

## Evidence links

- NASA TFAWS 2024 thermal mining presentation describes a regolith chamber, vapor line, and cold trap tank for ice extraction, with cold-trap tank functionality demonstrated for ice collection and removal modes. Source: https://tfaws.nasa.gov/wp-content/uploads/TFAWS2024_ID-07.pdf
- NASA NTRS Lunar Auger Dryer ISRU abstract describes icy regolith processed in an auger dryer, water vapor sent to a cold trap subsystem, and ice deposition in the cold trap as vapor is converted into ice. Source: https://ntrs.nasa.gov/api/citations/20220007322/downloads/PTMSS-SRR_LADI%20Abstract.pdf
- NASA LUSTRE thermal mining quadchart describes an advanced thermal mining technology that integrates extraction, transportation, and condensation of water vapor from lunar regolith. Source: https://www.nasa.gov/wp-content/uploads/2021/03/lustr_quadchart_advanced_thermal_mining_approach_choudhuri.pdf
- NASA TechPort ICICLE project describes a cold trap designed to selectively freeze and collect water vapor from volatile contaminants. Source: https://techport.nasa.gov/projects/113309
- A 2025 lunar regolith water-production paper reports water vapor transmitted through a closed flow path and liquid water collected in a cold trap after condensation. Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC12308065/
- EYELA describes cold traps as apparatus for capturing water vapor and toxic fumes from vacuum drying or concentration equipment, protecting vacuum systems and exhaust systems. Source: https://eyelaworld.com/products/cold-trap/

## Commercial alternatives

- Laboratory cold trap for vacuum systems.
- Vacuum condenser/cold finger.
- Refrigerated vapor trap for rotary evaporators or vacuum ovens.
- Cryogenic cold trap for high-vacuum or volatile separation.
- Shell-and-tube or plate condenser for non-vacuum process streams.
- Scrubber/absorber where the vapor is chemically absorbed rather than condensed.
- Process-specific condenser for ammonia, HCl, magnesium, phosphorus, or water.

## Build or open-source references

The system is buildable from known subsystems:

- Condenser or cold-trap surface.
- Refrigeration, cryocooler, passive radiator, or cold environment interface.
- Vacuum pump or blower where pressure control is needed.
- Vapor manifold and dust/particulate filters.
- Condensate or ice reservoir.
- Heat exchanger and coolant loop.
- Temperature, pressure, and fill-level sensors.
- Corrosion-compatible materials for reactive vapors.

For lunar water extraction, dust control and avoiding recondensation in the wrong place are major design issues. For HCl or ammonia, corrosion and absorption chemistry may matter more than simple condensation.

## Related machine research

Related reports already present:

- `vacuum_pump_small.md`
- `dust_collection_system.md`
- `drying_oven.md`
- `reduction_furnace_v0.md`
- `cryogenic_chiller_v0` may be related if researched separately.

Related KB items:

- `vapor_condenser_cold_trap`
- `cold_trap_module_v0`
- `cryogenic_chiller_v0`
- `thermal_water_extractor_v0`
- `water_auger_dryer_ladi_v0`
- `ammonia_recovery_unit_v0`

## Recommendation for KB realism

Keep as a real system category, but narrow or split by volatile class.

For lunar water extraction, the current BOM is reasonable as a small vapor capture/cold-trap subsystem. Recommended wording: "water vapor capture and cold-trap condensation system for thermal regolith extraction." If the same item is used for HCl, ammonia, Mg vapor, or high-temperature metal vapors, add process-specific variants or note compatible materials and capture temperatures.

Do not treat this as just a passive condenser. The useful system includes vapor transport, pressure control, heat rejection, reservoir management, sensors, and dust/corrosion handling.

## Confidence and open questions

Confidence: high that the item is real and relevant; medium that one 80 kg system covers all current chemical uses.

Open questions:

- Is this primarily a water/ice capture system or a generic vapor condenser?
- Should `vapor_condenser_cold_trap` be a component of this system rather than a parallel machine?
- What vapor temperatures, pressures, and species are in scope?
- Does polar regolith extraction need filters/demisters to prevent dust transport into the cold trap?
