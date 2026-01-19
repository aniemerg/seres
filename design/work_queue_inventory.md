# Work Queue Task Inventory

**Generated**: 2025-12-22 (Updated)
**Total Pending Tasks**: 346 (was 136)
**Source**: `out/work_queue.jsonl`

## Overview

This document provides a comprehensive inventory of all tasks currently in the work queue. The queue is automatically rebuilt on each indexer run and reflects current gaps in the knowledge base.

**Change Summary**:
- Queue grew from 136 → 346 tasks (+210, +154%)
- `referenced_only`: 62 → 254 (+192)
- `no_recipe`: 17 → 55 (+38)
- `invalid_recipe_schema`: 44 → 34 (-10, now 17 unique recipes)
- `import_stub`: 13 → 3 (-10, safety imports fixed)

The growth is primarily due to:
1. Cleanup work exposing new references (removed machines had dependencies)
2. Improved indexing discovering more gaps
3. BOM expansion as machines are better defined

See README for queue workflow:
- Lease task: `.venv/bin/python -m kbtool queue lease --agent <name>`
- Complete task: `.venv/bin/python -m kbtool queue complete --id <gap_type:item_id> --agent <name>`
- List counts: `.venv/bin/python -m kbtool queue ls`

---

## Task Categories

| Gap Type | Count | Previous | Change | Description |
|----------|-------|----------|--------|-------------|
| `referenced_only` | 254 | 62 | +192 | Items referenced but not yet defined |
| `no_recipe` | 55 | 17 | +38 | Items without any manufacturing recipe |
| `invalid_recipe_schema` | 34 | 44 | -10 | Recipes with schema validation issues |
| `import_stub` | 3 | 13 | -10 | Items with import recipes needing local manufacturing |

---

## 1. Referenced Only (254 tasks)

Items that are referenced in BOMs, recipes, or processes but don't have corresponding item definitions.

### 1.1 Import Placeholders (10 items)

These "Import X from Earth" references need to be either:
- Replaced with proper item definitions, OR
- Have corresponding import recipes created

```
Import 6-axis force/torque sensor from Earth
Import LED ring light from Earth
Import Li-ion battery backup from Earth
Import capacitive touch sensor from Earth
Import harmonic drive reducer from Earth
Import inductive proximity sensor from Earth
Import polymer cable drag chain from Earth
Import power distribution board from Earth
Import quick-change tool interface from Earth
Import servo drive controller from Earth
```

**Action**: These should likely have proper item definitions created and corresponding import recipes (similar to what was done for safety systems).

### 1.2 BOM References (57 items)

BOM files that are referenced but don't exist. Many of these are machine BOMs.

**High-priority BOMs** (commonly referenced or for critical machines):
```
bom_cnc_mill_v0_v0.yaml
bom_electrolysis_cell_aluminum_v0
bom_electrolyzer_pem_v0_v0.yaml
bom_ffc_reactor_unit_v0_v0.yaml
bom_induction_furnace_v0_v0.yaml
bom_inverter_dc_to_ac_v0_v0.yaml
bom_welding_arc_welder_v0.yaml
bom_welding_tig_unit_v0_v0.yaml
```

**Specialized/Analysis BOMs** (lower priority):
```
bom_carbonyl_safety_system_v0.yaml
bom_cryocooler_active_v0.yaml
bom_cryogenic_chiller_provider_v0_v0.yaml
bom_crystallization_unit_v0.yaml
bom_fms_control_system_v0_v0.yaml
bom_forge_or_induction_heater_v0.yaml
bom_generic_chemical_reactor_v0_v0.yaml
bom_grinder_cylindrical_v0.yaml
bom_heat_pipe_solar_receiver_advanced_v0.yaml
bom_heliostat_array_system_v0_v0.yaml
bom_hose_crimping_station_v0
bom_lab_v0.yaml
bom_lab_v0_v0.yaml
bom_lubrication_mixer_v0
bom_machine_vision_processing_v0_v0.yaml
bom_microstructure_analysis_system_v0_v0.yaml
bom_molding_press_v0.yaml
bom_neims_control_system_v0_v0.yaml
bom_nife_meteorite_magnetic_detection_v0_v0.yaml
bom_pelletizer_v0.yaml
bom_precision_grinding_system_v0.yaml
bom_rms_reconfigurable_system_v0_v0.yaml
bom_rolling_mill_v0.yaml
bom_strain_gauge_bonding_station_v0.yaml
bom_tensile_test_machine_v0.yaml
bom_visual_odometry_system_v0_v0.yaml
bom_water_purification_distillation_v0.yaml
```

**Support Equipment BOMs**:
```
bom_assembly_tools_basic
bom_battery_formation
bom_chemical_mixing
bom_chemical_reactor_basic
bom_core_memory_assembly
bom_cpu_core
bom_cutting_station_v0.yaml
bom_cutting_tools_general
bom_electrolysis_cell
bom_epoxy_synthesis_unit
bom_filtration_unit
bom_lab_assistant
bom_labor_bot_electronics
bom_labor_bot_welder
bom_mineral_processing_unit
bom_power_supply_basic
bom_procurement_agent
bom_regeneration_furnace
bom_robot_fab_station_v0_v0.yaml
bom_seed_lab
```

**Action**:
- For high-priority BOMs: Create proper BOM files when these machines become bottlenecks
- For specialized BOMs: Only create if needed for analysis or specific use cases
- For support equipment: Many can remain undefined until needed
- Consider removing BOM references from machine definitions if BOMs aren't critical

**Note**: Per the "incompleteness is a feature" principle, many machines can operate without complete BOMs during early modeling.

### 1.3 Materials (40 items)

Raw materials, intermediate materials, and chemical compounds:

**Minerals/Ores**:
```
alumina_pure
anorthite_ore
```

**Chemicals**:
```
aluminum_chloride_anhydrous
aluminum_chloride_hexahydrate
calcium_carbonate
calcium_chloride_anhydrous
calcium_chloride_molten
calcium_metal_pure
calcium_silicate
carbon_monoxide_gas
water_vapor
sodium_aluminate_solution
```

**Metals/Alloys**:
```
carbon_electrode
```

**Material Forms** (powders, sheets, pellets, etc.):
```
carbon_feed_system
filler_material
inert_anode_v0
```

**Others**:
```
alumina_pellets
carbon_anode_prebake
coke_metallurgical
cryolite_molten
electrolyte_molten
fluoride_salts
flux_mixture
foundry_sand
glass_fiber
graphite_powder_fine
high_purity_mgo
iron_filings
lime_powder
mold_release_agent
molybdenum_disulfide_powder
nickel_carbonyl_liquid
quartz_sand
rock_dust
silica_gel
slag_molten
sodium_cyanide_solution
solder_lead_free
```

**Action**: Create material definitions in `kb/items/materials/` as needed. Many of these may be process outputs that need recipe linkage.

### 1.4 Electrical & Control Components (32 items)

Electronics, sensors, and control systems:

**Control Components**:
```
circuit_breaker_set
computer_controller
control_board_3d_printer
control_plc_basic
din_rail_steel
relay_set_industrial
switch_selector_industrial
terminal_block_set
```

**Power Components**:
```
amplifier_waveform
bus_bar_copper
capacitor_bank_large
connector_heavy_duty
inductor_filter
oscillator_crystal
oscillator_precision
transformer_heavy_duty
transformer_step_down
```

**Sensors & Optics**:
```
camera_industrial
indicator_light_set
led_illumination_ring
```

**Antennas**:
```
antenna_dish_parabolic
antenna_whip
rf_feed_horn
```

**Enclosures**:
```
enclosure_electrical
enclosure_insulated
```

**Other**:
```
chassis_heavy_duty
motor_dc_small
motor_servo_small
stepper_motor_large
thermoelectric_cooler
wire_harness_control
```

**Action**: Create part definitions in `kb/items/parts/` or consolidate with existing equivalent parts per 5× magnitude rule.

### 1.5 Machines & Equipment (33 items)

Manufacturing equipment, processing machines, and systems:

**Processing Equipment**:
```
acid_resistant_reactor_v0
ball_mill
calcination_furnace_v0
casting_furnace
chlorine_handling_system_v0
crystallization_unit
crystallization_vessel
ffc_electrolysis_cell_v0
rotary_kiln_v0
```

**Extraction/Separation**:
```
electrolysis_cell_stack
extraction_unit
filtration_assembly
sieve_set
vibrating_screen
```

**Material Handling**:
```
collection_tank
combustion_chamber
condenser_coil
dispensing_nozzle
dispensing_unit
dump_bed_hydraulic
storage_hopper
storage_rack_small
vibratory_feeder
```

**Thermal Management**:
```
heat_source_nuclear
heat_transport_loop
radiator_heat_rejection
radiator_panels
solar_concentrator_high_temp_v0
solar_concentrator_v0
```

**Fabrication**:
```
fiber_spinneret
solder_paste_dispenser
spinning_machine
winding_drums
```

**Other**:
```
catalyst_bed_nickel
molds
recycling_unit
stirring_mechanism
tumbling_deburring_v0
vacuum_enclosure
```

**Action**: Create machine or equipment definitions in `kb/items/machines/` as needed for production modeling.

### 1.6 Mechanical Parts (4 items)

```
ball_screw_precision
precision_actuator
wheel_assembly_industrial
```

**Action**: Create part definitions or consolidate with existing parts.

### 1.7 Uncategorized (74 items)

Various items that don't fit clear categories:

**Precision Equipment**:
```
fixturing_table
grinder_small
grinding_machine
heat_treatment_basic
heated_bed
hotend_assembly
insulation_thermal
insulation_thermal_thick
insulator_ceramic
interferometer_unit
laser_measurement
linear_rail_precision
linear_rail_set
linear_stage_small
low_temp_heating
mounting_fixture
mounting_gimbal
```

**Solar/Energy**:
```
pete_cell_array
pete_solar_panel
solar_array
thermionic_converter_cell
```

**Systems**:
```
resource_3d_printer_cartesian_v0
resource_prospecting_ai_v0
```

**Other**:
```
crucible
dispensing_unit
extraction_unit
heat_treatment_basic
mounting_fixture
```

(Full list of 74 items available in work queue file)

**Action**: Review and categorize these items, then create appropriate definitions.

---

## 2. No Recipe (55 tasks)

Items that exist but have no manufacturing recipe (neither local nor import).

### 2.1 Machines (16 items)

```
3d_printer_basic
3d_printer_cartesian
assembly_tools_basic
atmosphere_control_system
battery_formation
bending_machine
calibration_station
chemical_mixing
chemical_reactor_basic
cryogenic_chiller_v0
cutting_station
cutting_tools_general
electrolysis_cell
electrolysis_cell_aluminum_v0
hose_crimping_station_v0
lubrication_mixer_v0
```

**Action**: Create manufacturing recipes or import recipes in `kb/recipes/`. Many of these are support equipment that may be acceptable as imports.

### 2.2 Support Equipment & Systems (23 items)

```
contact_applicator
core_memory_assembly
cpu_core
dc_power_supply_ffc
directional_antenna
epoxy_synthesis_unit
filtration_unit
grinding_mill
heat_exchanger_loop
heating_system_low_temp
lab_assistant
labor_bot_electronics
labor_bot_welder
mineral_processing_unit
mixer_basic
optical_inspection_system
optical_measurement_system
power_conditioner
power_distribution_bus
power_supply_basic
precision_stage
radio_transmitter
signal_generator
```

**Action**: Determine which should be manufactured vs. imported. Create appropriate recipes.

### 2.3 Specialized Equipment (16 items)

```
forming_furnace
pete_solar_panel
procurement_agent
regeneration_furnace
resource_3d_printer_basic_v0
robot_fab_station_v0
sabatier_reactor
seed_generator
seed_lab
seed_processor
shear_machine
tailings_dump_truck
thermal_water_extractor
thermionic_generator
water_electrolyzer
welding_consumables
```

**Action**: Create recipes when these become relevant to production modeling. Some (like `procurement_agent`) may be conceptual and not need recipes.

---

## 3. Invalid Recipe Schema (34 tasks = 17 unique recipes)

Recipes that fail schema validation. Each unique recipe appears twice in the queue (likely a duplicate detection issue).

### 3.1 Import Recipes Needing Schema Fix (9 recipes)

These are import recipes that likely have old schema format:

```
recipe_battery_backup_small_import_v0
recipe_cable_drag_chain_import_v0
recipe_force_torque_sensor_6axis_import_v0
recipe_harmonic_drive_reducer_medium_import_v0
recipe_led_ring_light_import_v0
recipe_power_distribution_board_import_v0
recipe_proximity_sensor_inductive_import_v0
recipe_quick_change_tool_interface_import_v0
recipe_servo_drive_controller_import_v0
recipe_touch_sensor_capacitive_import_v0
```

**Expected Fix**: Convert from old `produces_id/qty/unit` format to:
```yaml
id: recipe_X_import_v0
kind: recipe
target_item_id: X
variant_id: import_v0
steps: []
notes: |
  Import recipe for X.
  Import required: [description of what's imported]
```

### 3.2 Manufacturing Recipes Needing Schema Fix (8 recipes)

```
recipe_base_grease_stock_v0
recipe_carbon_anode_v0
recipe_methyl_chloride_gas_v0
recipe_methyl_chloride_gas_v1
recipe_mos2_solid_lubricant_v0
recipe_silicon_purified_v0
recipe_surface_treatment_station_v0
```

**Expected Fix**: Ensure proper structure:
```yaml
id: recipe_X_v0
kind: recipe
target_item_id: X
variant_id: v0  # or other variant
steps:
  - process_id: some_process_v0
    notes: "Step description"
notes: |
  Overall recipe notes
```

**Action**:
1. Read each recipe file
2. Convert to proper schema format (see `design/memo_a.md`)
3. Verify process references exist
4. Run indexer to confirm fix

**Quick Win**: Fixing these 17 unique recipes will eliminate 34 queue entries.

---

## 4. Import Stub (3 tasks)

Items that currently have import recipes (empty manufacturing steps) that were intentionally created.

```
emergency_stop_system
safety_controller_plc
safety_light_curtain
```

**Status**: These are safety-critical items that were correctly set up as imports during the recent cleanup. They represent components that should be imported from Earth rather than manufactured locally.

**Action**: No action needed - these are correct as import stubs.

---

## Progress Summary

### Completed Since Last Inventory

1. **Removed out-of-scope machines** (7 machines + 11 BOMs + references):
   - grey_goo_mitigation_system_v0
   - inflatable_habitat_module variants
   - mlp_5_4_4_4_network variants
   - terrain_analysis_ai variants

2. **Fixed safety import recipes** (3 recipes):
   - Converted emergency_stop_system, safety_controller_plc, safety_light_curtain to proper schema

3. **Cleaned up import stubs** (14 removed):
   - Deleted redundant import stubs that already had manufacturing recipes

4. **Fixed material patterns**:
   - Converted recovered_salt → sodium_chloride pattern
   - Created regolith_carbonaceous collection recipe
   - Consolidated highland regolith variants

5. **Fastener consolidation**:
   - Applied 5× substitution rule to fastener kits
   - Deleted 9 fastener files without recipes
   - Updated 2 fastener kit BOMs

**Net Result**: Despite cleanup work, queue grew due to:
- Better dependency tracking exposing more gaps
- Removed machines revealing downstream dependencies
- More thorough indexing

---

## Priority Recommendations

Based on project principles (structure before precision, iteration guided by bottlenecks):

### Immediate Quick Wins

1. **Fix 17 invalid recipe schemas** → Eliminates 34 queue entries
   - Focus on import recipes first (simple schema conversion)
   - Then manufacturing recipes (may need process verification)

2. **Create 10 import item definitions** → Enables proper import recipe linking
   - 6-axis force/torque sensor, LED ring light, etc.
   - Pattern: Create item definition + import recipe (like safety systems)

### High Priority (After Bottleneck Analysis)

3. **High-priority machine BOMs** → Only if these machines are bottlenecks
   - cnc_mill_v0_v0
   - electrolysis_cell_aluminum_v0
   - welding units

4. **Electrical components** → If these appear in critical paths
   - circuit_breaker_set, control_plc_basic, etc.
   - Consider consolidation per 5× rule

### Medium Priority

5. **No-recipe machines** → Create recipes for production-critical machines
6. **Material definitions** → For process inputs/outputs in critical paths

### Low Priority

7. **Specialized BOMs** → Only create when needed for specific analysis
8. **Support equipment recipes** → Many acceptable as imports
9. **Uncategorized items** → Address as they become relevant

**Next Action**: Run bottleneck analysis to identify which items dominate mass/energy/time:
```bash
.venv/bin/python -m kbtool index
# Review out/reports/ for top contributors
# Prioritize queue work based on bottleneck analysis
```

---

## Related Documentation

- **README.md** — Queue workflow and commands
- **design/memo_a.md** — Formal specification and recipe schema
- **design/memo_b.md** — Knowledge acquisition methodology
- **docs/parts_and_labor_guidelines.md** — Parts reuse policy (5× rule) and BOM best practices

---

## Notes

- This inventory is a snapshot. Run `.venv/bin/python -m kbtool index` to regenerate the queue
- Queue growth is expected as the knowledge base becomes more interconnected
- Many gaps are acceptable per the "incompleteness is a feature" principle
- Focus effort on items that appear in bottleneck analysis, not on exhaustive closure
- The duplicate queue entries for invalid_recipe_schema items suggest an indexer issue to investigate
