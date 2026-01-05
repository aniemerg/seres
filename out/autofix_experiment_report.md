# Auto-Fix Experiment Results

**Date:** 1767577406.5265267
**Recipes tested:** 10

## Summary Statistics

- **Total fix attempts:** 17
- **Validation passed:** 17 (100.0%)
- **BOM strategy successes:** 8
- **Previous output strategy successes:** 9

---

## Individual Recipe Results

### 1. recipe_3d_printer_basic_v0

- **Target:** `3d_printer_basic_v0`
- **BOM:** Yes (5 components)
- **Errors before fix:** 1

#### Error 1: Step 1

**Rule:** `recipe_template_missing_step_inputs`
**Message:** Step 1 uses template process 'calibration_and_test_basic_v0' but doesn't provide step-level input overrides

**Original step:**
```yaml
process_id: calibration_and_test_basic_v0
time_model: null
energy_model: null
inputs: []
outputs: []
byproducts: []
est_time_hr: null
labor_hours: null
machine_hours: null
notes: null
```

**Fix attempt:** bom_all_components ✅

*Add all 5 BOM components as step inputs*

**Fixed step:**
```yaml
process_id: calibration_and_test_basic_v0
time_model: null
energy_model: null
inputs:
- item_id: printer_frame_generic
  qty: 1.0
  unit: unit
- item_id: extruder_head_basic
  qty: 1.0
  unit: unit
- item_id: power_electronics_module
  qty: 1.0
  unit: unit
- item_id: power_supply_low_voltage
  qty: 1.0
  unit: unit
- item_id: power_supply_chassis_basic
  qty: 1.0
  unit: unit
outputs: []
byproducts: []
est_time_hr: null
labor_hours: null
machine_hours: null
notes: null
```

**Validation:** PASSED

**Fix attempt:** previous_outputs ✅

*Use outputs from previous steps as inputs*

**Fixed step:**
```yaml
process_id: calibration_and_test_basic_v0
time_model: null
energy_model: null
inputs:
- item_id: 3d_printer_basic_v0
  qty: 1.0
  unit: unit
  notes: null
outputs: []
byproducts: []
est_time_hr: null
labor_hours: null
machine_hours: null
notes: null
```

**Validation:** PASSED

---


### 2. recipe_acid_reactor_v0

- **Target:** `acid_reactor_v0`
- **BOM:** Yes (7 components)
- **Errors before fix:** 4

#### Error 1: Step 0

**Rule:** `recipe_template_missing_step_inputs`
**Message:** Step 0 uses template process 'welding_and_fabrication_v0' but doesn't provide step-level input overrides

**Original step:**
```yaml
process_id: welding_and_fabrication_v0
time_model: null
energy_model: null
inputs: []
outputs: []
byproducts: []
est_time_hr: 16.0
labor_hours: 16.0
machine_hours: null
notes: Fabricate stainless steel vessel and heating jacket
```

**Fix attempt:** bom_all_components ✅

*Add all 7 BOM components as step inputs*

**Fixed step:**
```yaml
process_id: welding_and_fabrication_v0
time_model: null
energy_model: null
inputs:
- item_id: chemical_reactor_vessel_v0
  qty: 1
  unit: null
- item_id: acid_resistant_lining
  qty: 1
  unit: null
- item_id: jacket_with_fittings
  qty: 1
  unit: null
- item_id: reactor_agitator_mixer_v0
  qty: 1
  unit: null
- item_id: gas_outlet_manifold
  qty: 2
  unit: null
- item_id: valve_set_gas_handling
  qty: 1
  unit: null
- item_id: thermocouple_type_s_v0
  qty: 2
  unit: null
outputs: []
byproducts: []
est_time_hr: 16.0
labor_hours: 16.0
machine_hours: null
notes: Fabricate stainless steel vessel and heating jacket
```

**Validation:** PASSED

---

#### Error 2: Step 1

**Rule:** `recipe_step_input_not_satisfied`
**Message:** Step 1 (process 'ceramic_coating_v0') requires input 'finished_part' which is not available

**Original step:**
```yaml
process_id: ceramic_coating_v0
time_model: null
energy_model: null
inputs: []
outputs: []
byproducts: []
est_time_hr: 8.0
labor_hours: 8.0
machine_hours: null
notes: Apply acid-resistant lining (glass or PTFE coating)
```

**Fix attempt:** bom_all_components ✅

*Add all 7 BOM components as step inputs*

**Fixed step:**
```yaml
process_id: ceramic_coating_v0
time_model: null
energy_model: null
inputs:
- item_id: chemical_reactor_vessel_v0
  qty: 1
  unit: null
- item_id: acid_resistant_lining
  qty: 1
  unit: null
- item_id: jacket_with_fittings
  qty: 1
  unit: null
- item_id: reactor_agitator_mixer_v0
  qty: 1
  unit: null
- item_id: gas_outlet_manifold
  qty: 2
  unit: null
- item_id: valve_set_gas_handling
  qty: 1
  unit: null
- item_id: thermocouple_type_s_v0
  qty: 2
  unit: null
outputs: []
byproducts: []
est_time_hr: 8.0
labor_hours: 8.0
machine_hours: null
notes: Apply acid-resistant lining (glass or PTFE coating)
```

**Validation:** PASSED

**Fix attempt:** previous_outputs ✅

*Use outputs from previous steps as inputs*

**Fixed step:**
```yaml
process_id: ceramic_coating_v0
time_model: null
energy_model: null
inputs:
- item_id: welded_fabrications
  qty: 9.5
  unit: kg
  notes: null
outputs: []
byproducts: []
est_time_hr: 8.0
labor_hours: 8.0
machine_hours: null
notes: Apply acid-resistant lining (glass or PTFE coating)
```

**Validation:** PASSED

---

#### Error 3: Step 2

**Rule:** `recipe_template_missing_step_inputs`
**Message:** Step 2 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Original step:**
```yaml
process_id: assembly_basic_v0
time_model: null
energy_model: null
inputs: []
outputs: []
byproducts: []
est_time_hr: 12.0
labor_hours: 12.0
machine_hours: null
notes: Install stirring mechanism, gas ports, valves, and sensors
```

**Fix attempt:** bom_all_components ✅

*Add all 7 BOM components as step inputs*

**Fixed step:**
```yaml
process_id: assembly_basic_v0
time_model: null
energy_model: null
inputs:
- item_id: chemical_reactor_vessel_v0
  qty: 1
  unit: null
- item_id: acid_resistant_lining
  qty: 1
  unit: null
- item_id: jacket_with_fittings
  qty: 1
  unit: null
- item_id: reactor_agitator_mixer_v0
  qty: 1
  unit: null
- item_id: gas_outlet_manifold
  qty: 2
  unit: null
- item_id: valve_set_gas_handling
  qty: 1
  unit: null
- item_id: thermocouple_type_s_v0
  qty: 2
  unit: null
outputs: []
byproducts: []
est_time_hr: 12.0
labor_hours: 12.0
machine_hours: null
notes: Install stirring mechanism, gas ports, valves, and sensors
```

**Validation:** PASSED

**Fix attempt:** previous_outputs ✅

*Use outputs from previous steps as inputs*

**Fixed step:**
```yaml
process_id: assembly_basic_v0
time_model: null
energy_model: null
inputs:
- item_id: welded_fabrications
  qty: 9.5
  unit: kg
  notes: null
- item_id: finished_part
  qty: 1.0
  unit: kg
  notes: null
outputs: []
byproducts: []
est_time_hr: 12.0
labor_hours: 12.0
machine_hours: null
notes: Install stirring mechanism, gas ports, valves, and sensors
```

**Validation:** PASSED

---

#### Error 4: Step 4

**Rule:** `recipe_template_missing_step_inputs`
**Message:** Step 4 uses template process 'integration_test_basic_v0' but doesn't provide step-level input overrides

**Original step:**
```yaml
process_id: integration_test_basic_v0
time_model: null
energy_model: null
inputs: []
outputs: []
byproducts: []
est_time_hr: 4.0
labor_hours: 4.0
machine_hours: null
notes: Test heating, stirring, and gas handling systems
```

**Fix attempt:** bom_all_components ✅

*Add all 7 BOM components as step inputs*

**Fixed step:**
```yaml
process_id: integration_test_basic_v0
time_model: null
energy_model: null
inputs:
- item_id: chemical_reactor_vessel_v0
  qty: 1
  unit: null
- item_id: acid_resistant_lining
  qty: 1
  unit: null
- item_id: jacket_with_fittings
  qty: 1
  unit: null
- item_id: reactor_agitator_mixer_v0
  qty: 1
  unit: null
- item_id: gas_outlet_manifold
  qty: 2
  unit: null
- item_id: valve_set_gas_handling
  qty: 1
  unit: null
- item_id: thermocouple_type_s_v0
  qty: 2
  unit: null
outputs: []
byproducts: []
est_time_hr: 4.0
labor_hours: 4.0
machine_hours: null
notes: Test heating, stirring, and gas handling systems
```

**Validation:** PASSED

**Fix attempt:** previous_outputs ✅

*Use outputs from previous steps as inputs*

**Fixed step:**
```yaml
process_id: integration_test_basic_v0
time_model: null
energy_model: null
inputs:
- item_id: welded_fabrications
  qty: 9.5
  unit: kg
  notes: null
- item_id: finished_part
  qty: 1.0
  unit: kg
  notes: null
- item_id: assembled_equipment
  qty: 1.0
  unit: kg
  notes: null
outputs: []
byproducts: []
est_time_hr: 4.0
labor_hours: 4.0
machine_hours: null
notes: Test heating, stirring, and gas handling systems
```

**Validation:** PASSED

---


### 3. recipe_ammonia_recovery_unit_v0

- **Target:** `ammonia_recovery_unit_v0`
- **BOM:** Yes (9 components)
- **Errors before fix:** 1

#### Error 1: Step 0

**Rule:** `recipe_template_missing_step_inputs`
**Message:** Step 0 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Original step:**
```yaml
process_id: assembly_basic_v0
time_model: null
energy_model: null
inputs: []
outputs: []
byproducts: []
est_time_hr: null
labor_hours: null
machine_hours: null
notes: Assemble ammonia recovery unit per BOM
```

**Fix attempt:** bom_all_components ✅

*Add all 9 BOM components as step inputs*

**Fixed step:**
```yaml
process_id: assembly_basic_v0
time_model: null
energy_model: null
inputs:
- item_id: pressure_vessel_steel
  qty: 150.0
  unit: kg
- item_id: heating_element_resistive
  qty: 2
  unit: unit
- item_id: vapor_condenser_cold_trap
  qty: 1
  unit: unit
- item_id: piping_and_fittings_thermal
  qty: 50.0
  unit: kg
- item_id: valve_set_gas_handling
  qty: 1
  unit: unit
- item_id: structural_frame_steel
  qty: 100.0
  unit: kg
- item_id: thermal_insulation_basic
  qty: 30.0
  unit: kg
- item_id: control_panel_basic
  qty: 1
  unit: unit
- item_id: fastener_kit_medium
  qty: 1
  unit: unit
outputs: []
byproducts: []
est_time_hr: null
labor_hours: null
machine_hours: null
notes: Assemble ammonia recovery unit per BOM
```

**Validation:** PASSED

---


### 4. recipe_analog_test_bench_neural_circuits_v0

- **Target:** `analog_test_bench_neural_circuits_v0`
- **BOM:** Yes (2 components)
- **Errors before fix:** 1

#### Error 1: Step 0

**Rule:** `recipe_template_missing_step_inputs`
**Message:** Step 0 uses template process 'machine_assembly_basic_v0' but doesn't provide step-level input overrides

**Original step:**
```yaml
process_id: machine_assembly_basic_v0
time_model: null
energy_model: null
inputs: []
outputs: []
byproducts: []
est_time_hr: null
labor_hours: null
machine_hours: null
notes: Assemble from machine_frame_small and power_electronics_module using assembly_station.
```

**Fix attempt:** bom_all_components ✅

*Add all 2 BOM components as step inputs*

**Fixed step:**
```yaml
process_id: machine_assembly_basic_v0
time_model: null
energy_model: null
inputs:
- item_id: machine_frame_small
  qty: 1.0
  unit: unit
- item_id: power_electronics_module
  qty: 1.0
  unit: unit
outputs: []
byproducts: []
est_time_hr: null
labor_hours: null
machine_hours: null
notes: Assemble from machine_frame_small and power_electronics_module using assembly_station.
```

**Validation:** PASSED

---


### 5. recipe_antenna_parabolic_dish_v0

- **Target:** `antenna_parabolic_dish_v0`
- **BOM:** Yes (7 components)
- **Errors before fix:** 1

#### Error 1: Step 0

**Rule:** `recipe_template_missing_step_inputs`
**Message:** Step 0 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Original step:**
```yaml
process_id: assembly_basic_v0
time_model: null
energy_model: null
inputs: []
outputs: []
byproducts: []
est_time_hr: 6.0
labor_hours: 2.0
machine_hours: 4.0
notes: Assemble parabolic dish from BOM components (reflector, feed, struts, mount,
  connectors).
```

**Fix attempt:** bom_all_components ✅

*Add all 7 BOM components as step inputs*

**Fixed step:**
```yaml
process_id: assembly_basic_v0
time_model: null
energy_model: null
inputs:
- item_id: aluminum_sheet_reflector_v0
  qty: 30.0
  unit: kg
- item_id: feed_horn_antenna_v0
  qty: 1.0
  unit: each
- item_id: support_struts_aluminum
  qty: 10.0
  unit: kg
- item_id: mounting_bracket_azimuth_elevation
  qty: 1.0
  unit: each
- item_id: bearing_ball_steel
  qty: 4.0
  unit: each
- item_id: coaxial_cable_low_loss
  qty: 20.0
  unit: m
- item_id: protective_coating_aluminum
  qty: 0.5
  unit: kg
outputs: []
byproducts: []
est_time_hr: 6.0
labor_hours: 2.0
machine_hours: 4.0
notes: Assemble parabolic dish from BOM components (reflector, feed, struts, mount,
  connectors).
```

**Validation:** PASSED

---


### 6. recipe_basalt_fiber_v0

- **Target:** `basalt_fiber`
- **BOM:** No
- **Errors before fix:** 1

#### Error 1: Step 0

**Rule:** `recipe_step_input_not_satisfied`
**Message:** Step 0 (process 'glass_melting_and_forming_v0') requires input 'regolith_fine_fraction' which is not available

**Original step:**
```yaml
process_id: glass_melting_and_forming_v0
time_model: null
energy_model: null
inputs: []
outputs: []
byproducts: []
est_time_hr: 2.5
labor_hours: null
machine_hours: 2.5
notes: null
```

---


### 7. recipe_carbon_reductant_v0

- **Target:** `carbon_reductant`
- **BOM:** No
- **Errors before fix:** 3

#### Error 1: Step 0

**Rule:** `recipe_step_input_not_satisfied`
**Message:** Step 0 (process 'carbon_extraction_from_carbonaceous_v0') requires input 'regolith_carbonaceous' which is not available

**Original step:**
```yaml
process_id: carbon_extraction_from_carbonaceous_v0
time_model: null
energy_model: null
inputs: []
outputs: []
byproducts: []
est_time_hr: 1.5
labor_hours: null
machine_hours: null
notes: Extract carbon reductant from carbonaceous regolith feedstock.
```

---

#### Error 2: Step 1

**Rule:** `recipe_template_missing_step_inputs`
**Message:** Step 1 uses template process 'drying_basic_v0' but doesn't provide step-level input overrides

**Original step:**
```yaml
process_id: drying_basic_v0
time_model: null
energy_model: null
inputs: []
outputs: []
byproducts: []
est_time_hr: 0.5
labor_hours: null
machine_hours: 0.5
notes: null
```

**Fix attempt:** previous_outputs ✅

*Use outputs from previous steps as inputs*

**Fixed step:**
```yaml
process_id: drying_basic_v0
time_model: null
energy_model: null
inputs:
- item_id: carbon_reductant
  qty: 0.3
  unit: kg
  notes: null
- item_id: tailings
  qty: 9.7
  unit: kg
  notes: null
outputs: []
byproducts: []
est_time_hr: 0.5
labor_hours: null
machine_hours: 0.5
notes: null
```

**Validation:** PASSED

---

#### Error 3: Step 2

**Rule:** `recipe_step_input_not_satisfied`
**Message:** Step 2 (process 'sizing_grinding_basic_v0') requires input 'coarse_powder' which is not available

**Original step:**
```yaml
process_id: sizing_grinding_basic_v0
time_model: null
energy_model: null
inputs: []
outputs: []
byproducts: []
est_time_hr: 0.5
labor_hours: null
machine_hours: 0.5
notes: null
```

**Fix attempt:** previous_outputs ✅

*Use outputs from previous steps as inputs*

**Fixed step:**
```yaml
process_id: sizing_grinding_basic_v0
time_model: null
energy_model: null
inputs:
- item_id: carbon_reductant
  qty: 0.3
  unit: kg
  notes: null
- item_id: tailings
  qty: 9.7
  unit: kg
  notes: null
- item_id: dried_material
  qty: 1.0
  unit: kg
  notes: null
outputs: []
byproducts: []
est_time_hr: 0.5
labor_hours: null
machine_hours: 0.5
notes: null
```

**Validation:** PASSED

---


### 8. recipe_cast_metal_parts_v0

- **Target:** `cast_metal_parts`
- **BOM:** No
- **Errors before fix:** 2

#### Error 1: Step 1

**Rule:** `recipe_template_missing_step_inputs`
**Message:** Step 1 uses template process 'metal_casting_basic_v0' but doesn't provide step-level input overrides

**Original step:**
```yaml
process_id: metal_casting_basic_v0
time_model: null
energy_model: null
inputs: []
outputs: []
byproducts: []
est_time_hr: 1.5
labor_hours: null
machine_hours: 1.5
notes: null
```

---

#### Error 2: Step 2

**Rule:** `recipe_template_missing_step_inputs`
**Message:** Step 2 uses template process 'machining_finish_basic_v0' but doesn't provide step-level input overrides

**Original step:**
```yaml
process_id: machining_finish_basic_v0
time_model: null
energy_model: null
inputs: []
outputs: []
byproducts: []
est_time_hr: 1.0
labor_hours: null
machine_hours: 1.0
notes: null
```

**Fix attempt:** previous_outputs ✅

*Use outputs from previous steps as inputs*

**Fixed step:**
```yaml
process_id: machining_finish_basic_v0
time_model: null
energy_model: null
inputs:
- item_id: cast_metal_parts
  qty: 0.95
  unit: kg
  notes: null
outputs: []
byproducts: []
est_time_hr: 1.0
labor_hours: null
machine_hours: 1.0
notes: null
```

**Validation:** PASSED

---


### 9. crushing_jaw_set_v0

- **Target:** `crushing_jaw_set`
- **BOM:** No
- **Errors before fix:** 1

#### Error 1: Step 0

**Rule:** `recipe_step_input_not_satisfied`
**Message:** Step 0 (process 'jaw_set_fabrication_v0') requires input 'steel_ingot' which is not available

**Original step:**
```yaml
process_id: jaw_set_fabrication_v0
time_model: null
energy_model: null
inputs: []
outputs: []
byproducts: []
est_time_hr: null
labor_hours: null
machine_hours: null
notes: null
```

---


### 10. recipe_cutting_tool_set_basic_v0

- **Target:** `cutting_tool_set_basic`
- **BOM:** No
- **Errors before fix:** 3

#### Error 1: Step 0

**Rule:** `recipe_step_input_not_satisfied`
**Message:** Step 0 (process 'import_receiving_basic_v0') requires input 'bulk_material_or_parts' which is not available

**Original step:**
```yaml
process_id: import_receiving_basic_v0
time_model: null
energy_model: null
inputs: []
outputs: []
byproducts: []
est_time_hr: 0.5
labor_hours: 0.5
machine_hours: null
notes: null
```

---

#### Error 2: Step 1

**Rule:** `recipe_template_missing_step_inputs`
**Message:** Step 1 uses template process 'metal_casting_basic_v0' but doesn't provide step-level input overrides

**Original step:**
```yaml
process_id: metal_casting_basic_v0
time_model: null
energy_model: null
inputs: []
outputs: []
byproducts: []
est_time_hr: 1.0
labor_hours: null
machine_hours: 1.0
notes: null
```

**Fix attempt:** previous_outputs ✅

*Use outputs from previous steps as inputs*

**Fixed step:**
```yaml
process_id: metal_casting_basic_v0
time_model: null
energy_model: null
inputs:
- item_id: bulk_material_or_parts
  qty: 1.0
  unit: kg
  notes: null
outputs: []
byproducts: []
est_time_hr: 1.0
labor_hours: null
machine_hours: 1.0
notes: null
```

**Validation:** PASSED

---

#### Error 3: Step 2

**Rule:** `recipe_template_missing_step_inputs`
**Message:** Step 2 uses template process 'machining_finish_basic_v0' but doesn't provide step-level input overrides

**Original step:**
```yaml
process_id: machining_finish_basic_v0
time_model: null
energy_model: null
inputs: []
outputs: []
byproducts: []
est_time_hr: 1.0
labor_hours: null
machine_hours: 1.0
notes: null
```

**Fix attempt:** previous_outputs ✅

*Use outputs from previous steps as inputs*

**Fixed step:**
```yaml
process_id: machining_finish_basic_v0
time_model: null
energy_model: null
inputs:
- item_id: bulk_material_or_parts
  qty: 1.0
  unit: kg
  notes: null
- item_id: cast_metal_parts
  qty: 0.95
  unit: kg
  notes: null
outputs: []
byproducts: []
est_time_hr: 1.0
labor_hours: null
machine_hours: 1.0
notes: null
```

**Validation:** PASSED

---


## Manual Review Guidance

### Questions to Ask:

1. **Semantic correctness:** Does the fix make sense for what the process does?
2. **Quantity appropriateness:** Are the quantities reasonable?
3. **Input selection:** Should ALL BOM components be used, or only some?
4. **Process intent:** Does the fix align with the process's purpose?

### Common Issues to Watch For:

- Adding ALL BOM components when process only needs 1-2
- Using outputs that don't match process input requirements
- Quantities that are too large/small for the process
- Materials that don't match process type (e.g., liquids in welding)
