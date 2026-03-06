# Self-Replicating-Machines-2 Candidate Enrichment Plan

Source triage:
- `design/self_replicating_machines_2_kb_page_review.md`
- `design/Self-Replicating-Machines-2_extracted-text.txt`

Date: 2026-03-03

## Goal
Enrich page-review candidates into actionable KB updates by identifying:
- what is already represented (possibly under different IDs),
- what is only partially represented,
- what is missing,
- what machines/process I/O would be needed for missing or weakly modeled candidates.

## Method Used
- Exact ID check for all candidates from the page review `Implementation Extraction List`.
- Alias/near-match mapping across `kb/items/{materials,machines,parts}`, `kb/processes`, and `kb/recipes`.
- Enrichment pass for non-trivial gaps: proposed `inputs`, `outputs`, `resource_requirements`, and key schema/policy risks.

## Coverage Snapshot
- Candidate names checked: 40
- Exact string ID matches: 0
- Represented via existing equivalent IDs/processes: many
- Net-new likely additions (high confidence): geomagnetic survey stack, electrostatic beneficiation stack, selective-solar-sintering/EBAM machine stack, explicit magnetometer payload, explicit Wheatstone bridge module

Interpretation:
- Most chemistry/power/vacuum-tube/flywheel items already exist in some form.
- The highest-value updates are mostly in survey/beneficiation/advanced-manufacturing machine definitions and tightening placeholder models.
- Use rover modularity for prospecting/survey capability where possible (tool modules on a shared rover platform) rather than introducing standalone survey-only processes.

## Candidate Matrix (Status + Mapping)

Status legend:
- `represented`: usable equivalent already in KB
- `partial`: related entities exist but coverage is weak, generic, imported, or missing key step
- `missing`: no practical equivalent found

1) `subsurface_water_ice_deposit` -> `partial`
- Existing mapping: `regolith_polar_psc`, `polar_water_ice_extraction_v0`
- Gap: no dedicated resource/material node for subsurface ice deposit class.

2) `c_type_volatile_mixture` -> `partial`
- Existing mapping: `regolith_carbonaceous`, `regolith_mining_carbonaceous_v0`
- Gap: no explicit mixed-volatile material stream item.

3) `water_ice_thermal_extraction` -> `represented`
- Existing mapping: `polar_water_ice_extraction_v0`

4) `water_vapor_capture_condensation` -> `represented`
- Existing mapping: `vapor_capture_system_v0`, `cold_trap_cryogenic_v0`

5) `regolith_volatiles_heating_700c` -> `represented`
- Existing mapping: `regolith_volatile_thermal_extraction_v0`

6) `fractional_distillation_cryogenic_volatiles` -> `partial`
- Existing mapping: `helium3_cryogenic_separation_v0`, `packed_bed_distillation_v0`, `distillation_column_simple_v0`
- Gap: no single explicit volatile-fractionation process for the full Page-4 spectrum.

7) `geomagnetic_survey` -> `defer-as-standalone`
- Plan adjustment: do not add standalone survey process for now; express this as rover-assisted prospecting requirement via modular tooling.

8) `geotechnical_rover_survey` -> `defer-as-standalone`
- Plan adjustment: represent through process prerequisites requiring rover + prospecting module/tooling.

9) `regolith_comminution_ball_mill` -> `partial`
- Existing mapping: `ball_milling_v0`, `crushing_and_grinding_v0`, `regolith_crushing_grinding_v0`
- Gap: no explicit named comminution process tied to mineral liberation quality targets.

10) `electrostatic_beneficiation` -> `missing`

11) `liquation_fe_tio2_separation` -> `missing`

12) `ferrite_ceramic_paste_prep` -> `partial`
- Existing mapping: ferrite precursor and shaping/sintering (`ferrite_powder_precursor_synthesis_v0`, `ferrite_pressing_shaping_v0`)
- Gap: explicit water/clay/binder paste route from Page 69 not modeled as a dedicated process.

13) `ferrite_high_temp_sintering` -> `represented`
- Existing mapping: `ferrite_toroid_sintering_v0`

14) `quartz_piezo_sensor_fabrication` -> `partial`
- Existing mapping: `quartz_crystal_synthesis_v0`
- Gap: no explicit piezo sensor assembly process using quartz electrode stacks.

15) `vacuum_tube_fabrication` -> `represented`
- Existing mapping: `vacuum_tube_assembly_v0` and related envelope/subassembly processes.

16) `glass_sealing_and_evacuation` -> `partial`
- Existing mapping: `glass_envelope_forming_v0`, `vacuum_tube_sealed` chain
- Gap: explicit evacuation + seal-off process step is implicit rather than clearly modeled.

17) `solar_concentrator_furnace_operation` -> `partial`
- Existing mapping: concentrator machines/assemblies exist (`solar_concentrator_fresnel*`, aligned concentrator)
- Gap: operation process that consumes solar resource and outputs process heat stream is weak/implicit.

18) `thermoelectric_generation_mg2si` -> `partial`
- Existing mapping: `recipe_magnesium_silicide_thermoelectric_v0`
- Gap: explicit power-generation process using Mg2Si device performance assumptions not clearly represented.

19) `flywheel_energy_storage_assembly` -> `represented`
- Existing mapping: `flywheel_energy_storage_system_assembly_v0`

20) `prospecting_rover` -> `partial`
- Existing mapping: `kapvik_microrover_30kg_v0` and rover subassemblies
- Gap: generic prospecting rover machine variant/capabilities tag not explicit.

21) `magnetometer_payload` -> `missing`

22) `electrostatic_separator` -> `missing`

23) `selective_solar_sinterer` -> `missing`

24) `multi_material_3d_printer` -> `missing` (closest is basic/cartesian 3D printer)

25) `ebam_printer` -> `missing`

26) `vacuum_tube_sealing_station` -> `partial`
- Existing mapping: `vacuum_chamber`, leak-test/glassworking equipment and recipes
- Gap: dedicated sealing-station machine entry absent.

27) `flywheel_energy_storage_unit` -> `partial`
- Existing mapping: `flywheel_energy_storage_system_v0` (part), `flywheel_motor_generator_v0` (machine)
- Gap: role split between part/machine could be clarified.

28) `alumina_grinding_media` -> `missing`

29) `silumin_grinding_media` -> `missing`

30) `glass_fiber_cloth_insulation` -> `partial`
- Existing mapping: basalt/ceramic fiber and generic insulation entries
- Gap: explicit glass-fiber-cloth electrical insulation material not present.

31) `porcelain_insulator` -> `partial`
- Existing mapping: `ceramic_insulators`, kaolinite chain
- Gap: dedicated porcelain-based variant not explicit.

32) `enamel_glass_insulation` -> `missing`

33) `potentiometer_assembly` -> `partial`
- Existing mapping: `potentiometer_wirewound_v0`, `potentiometer_conductive_polymer_v0`
- Gap: full assembled potentiometer module definition unclear.

34) `strain_gauge_element` -> `represented`
- Existing mapping: `strain_gauge_foil_v0`, bonding chain

35) `wheatstone_bridge_module` -> `missing`

36) `photomultiplier_tube` -> `partial`
- Existing mapping: `photomultiplier_tube_v0` exists as `is_import: true`
- Gap: no full local fabrication chain for PMT-specific internals.

37) `vacuum_glass_envelope` -> `represented`
- Existing mapping: `glass_envelope_vacuum_tube_v0`, `vacuum_envelope_quartz`

38) `tungsten_cathode` -> `represented`
- Existing mapping: `tungsten_cathode_blank_v0`, `tungsten_cathode_coated`, `tungsten_cathode_oxide_coated_v0`

39) `nickel_grid_anode` -> `partial`
- Existing mapping: `nickel_anode_vacuum_tube_v0`, `nickel_anode_plate`
- Gap: explicit “grid + anode” electrode set may need clearer separation.

40) `kovar_wire` -> `partial`
- Existing mapping: `kovar_alloy_fe_ni_co_v0`, `kovar_wiring_insulation_v0`
- Gap: explicit wire-form part/material ID absent.

## High-Interest Update Packages

### Package A: Survey and Site Characterization (mostly missing)
Target additions:
- `part/machine:prospecting_module_v0` (rover attachable tool module)
- `part/machine:magnetometer_payload_v0` (tool module or submodule)
- (optional) `machine:prospecting_rover_v0` alias/variant to Kapvik chain if clearer than reusing existing rover IDs

Suggested machine requirements:
- `kapvik_microrover_30kg_v0` (or `prospecting_rover_v0`)
- `prospecting_module_v0` (new attachable module)
- existing drill/sampling hardware where appropriate (`drilling_equipment_v0`, `auger_drill_assembly`)

I/O modeling challenge:
- Survey outputs are informational, but KB schema is materially oriented.
- Recommended workaround: model physical outputs such as `sampled_regolith_core`, `mapped_site_marker_set`, `survey_data_storage_module` (physical storage medium), and avoid pure-intangible outputs.

### Package B: Beneficiation Extensions
Target additions:
- `machine:electrostatic_separator_v0`
- `process:electrostatic_beneficiation_v0`
- `process:liquation_fe_tio2_separation_v0`
- optional explicit naming wrapper for comminution quality control (`regolith_comminution_ball_mill_v0`)

Likely process I/O:
- `electrostatic_beneficiation_v0`:
  - inputs: `regolith_crushed`
  - outputs: `pyroxene_concentrate` + `anorthite_ore` + `non_magnetic_tailings`
- `liquation_fe_tio2_separation_v0`:
  - inputs: ilmenite-reduction mixed output (or explicit mixed `fe_tio2_melt`)
  - outputs: `iron_metal_impure` + `titanium_oxide`

Machines:
- new `electrostatic_separator_v0`
- existing `furnace_high_temp`, `gas_handling_loop_v0`, `magnetic_separator_drum_v0`, `gravity_separator`

### Package C: Sensor/Electronics Completion
Target additions:
- `part:wheatstone_bridge_module_v0`
- `process:quartz_piezo_sensor_fabrication_v0`
- optional explicit `machine:vacuum_tube_sealing_station_v0`
- optional PMT-local path (`photomultiplier_tube_v1` local variant)

Likely process I/O:
- `quartz_piezo_sensor_fabrication_v0`:
  - inputs: `quartz_crystal`, `nickel_sheet` (or Al electrode), insulation ceramic
  - outputs: `piezo_sensor_element_v0`
- `wheatstone_bridge_module_v0`:
  - inputs: resistive elements (`strain_gauge_foil_v0`/resistor parts), substrate, conductors
  - outputs: bridge module part

Issue notes:
- PMT currently import-only; local chain would require vacuum envelope + cathode + dynode manufacturing assumptions and may remain high-uncertainty.

### Package D: Advanced Manufacturing Machines (3D/Solar/EBAM)
Target additions:
- `machine:selective_solar_sinterer_v0`
- `machine:multi_material_3d_printer_v0`
- `machine:ebam_printer_v0`
- `process:solar_concentrator_furnace_operation_v0` (operational process model)

Likely process I/O:
- operation process can consume `solar_radiation` resource and output `process_heat_high_temp` material/resource proxy for downstream thermal steps.

Issue notes:
- strong dependence on resource modeling conventions (`resource_types` vs materialized heat carriers).
- avoid duplicating existing generic 3D printer unless capability deltas are explicit (metal melt deposition, EBAM high-voltage subsystem, multi-head toolchain).

### Package E: Material Form-Factor Gaps
Target additions:
- `material/part:alumina_grinding_media_v0`
- `material/part:silumin_grinding_media_v0`
- `material:glass_fiber_cloth_insulation_v0`
- `part:porcelain_insulator_v0` (or variant under existing ceramic insulators)
- `material:enamel_glass_insulation_v0`
- `part:kovar_wire_v0`

Issue notes:
- prefer variants of existing canonical items where function is similar.
- only add net-new IDs if recipe inputs/outputs or simulation behavior materially differ.

## Enrichment Risks Identified
- Survey-process outputs are information-centric; schema expects material flow.
- Several relevant chains exist but are placeholder-heavy; adding duplicates without tightening existing placeholders will add noise.
- Some advanced candidates (PMT local fab, EBAM printer, full multi-material printer) will need explicit assumptions and likely `status`/policy tags to avoid overconfidence.

## Suggested Next Step
Create a “delta shortlist” for immediate KB edits:
1. Add only high-confidence missing infrastructure (`electrostatic_separator_v0`, `electrostatic_beneficiation_v0`, `wheatstone_bridge_module_v0`, `prospecting_module_v0`, `magnetometer_payload_v0`).
2. Tighten existing partial chains before adding large new machine families (PMT local production, EBAM, multi-material printer).
3. For each selected candidate, draft a one-page mini-spec:
   - chosen ID(s), variant/alias strategy, expected machine requirements, full I/O, and validation checks.
