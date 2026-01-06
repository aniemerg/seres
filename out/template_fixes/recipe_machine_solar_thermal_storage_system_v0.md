# Fix Intelligence: recipe_machine_solar_thermal_storage_system_v0

## Files

- **Recipe:** `kb/recipes/recipe_machine_solar_thermal_storage_system_v0.yaml`
- **Target item:** `solar_thermal_storage_system_v0`
  - File: `kb/items/solar_thermal_storage_system_v0.yaml`
- **BOM:** `kb/boms/bom_solar_thermal_storage_system_v0.yaml` ✓
  - Components: 4
- **Steps:** 4 total

## Errors (4 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_fabrication_welding_v0') requires input 'steel_plate_or_sheet' which is not available

**Location:** Step 0
**Process:** `metal_fabrication_welding_v0`
  - File: `kb/processes/metal_fabrication_welding_v0.yaml`

**Current step:**
```yaml
- process_id: metal_fabrication_welding_v0
  inputs:
  - item_id: steel_plate_or_sheet
    qty: 500.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Generic placeholder `steel_plate_or_sheet`

This is not a real item. Need to replace with specific item.

**Specific items matching pattern:**

- `gasket_sheet_material_v0`
- `gasket_sheet`
- `steel_plate_raw`
- `steel_plate_or_sheet`
- `iron_powder_or_sheet`
- `sheet_metal_or_structural_steel`
- `brass_sheet`
- `nickel_sheet_rolling_forming_v0`
- `steel_sheet_1mm`
- `steel_sheet_3mm`

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'refractory_casting_v0') requires input 'refractory_castable' which is not available

**Location:** Step 1
**Process:** `refractory_casting_v0`
  - File: `kb/processes/refractory_casting_v0.yaml`

**Current step:**
```yaml
- process_id: refractory_casting_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'regolith_collection_and_processing_v0') requires input 'regolith_lunar_mare' which is not available

**Location:** Step 2
**Process:** `regolith_collection_and_processing_v0`
  - File: `kb/processes/regolith_collection_and_processing_v0.yaml`

**Current step:**
```yaml
- process_id: regolith_collection_and_processing_v0
  inputs:
  - item_id: regolith_lunar_mare
    qty: 1000.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `regolith_lunar_mare` not found

This item doesn't exist in the KB.

**Suggestions:**
1. Check if item name is misspelled
2. Add item to BOM if it should be a component
3. Replace with an output from a previous step

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'assembly_process_general_v0') requires input 'tank_shell_steel' which is not available

**Location:** Step 3
**Process:** `assembly_process_general_v0`
  - File: `kb/processes/assembly_process_general_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_process_general_v0
  inputs:
  - item_id: tank_shell_steel
    qty: 450.0
    unit: kg
  - item_id: thermal_insulation_high_temp
    qty: 280.0
    unit: kg
  - item_id: thermal_storage_media_regolith
    qty: 950.0
    unit: kg
  - item_id: heat_exchanger_tube_bundle
    qty: 100.0
    unit: kg
  - item_id: thermocouple_type_k_v0
    qty: 10.0
    unit: each
  - item_id: piping_and_valves_set
    qty: 20.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `tank_shell_steel` not found

This item doesn't exist in the KB.

**Suggestions:**
1. Check if item name is misspelled
2. Add item to BOM if it should be a component
3. Replace with an output from a previous step

#### Problem: Item `thermal_insulation_high_temp` not found

This item doesn't exist in the KB.

**Suggestions:**
1. Check if item name is misspelled
2. Add item to BOM if it should be a component
3. Replace with an output from a previous step

#### Problem: Item `thermal_storage_media_regolith` not found

This item doesn't exist in the KB.

**Suggestions:**
1. Check if item name is misspelled
2. Add item to BOM if it should be a component
3. Replace with an output from a previous step

#### Problem: Item `heat_exchanger_tube_bundle` not found

This item doesn't exist in the KB.

**Suggestions:**
1. Check if item name is misspelled
2. Add item to BOM if it should be a component
3. Replace with an output from a previous step

#### Problem: Item `thermocouple_type_k_v0` not found

This item doesn't exist in the KB.

**Suggestions:**
1. Check if item name is misspelled
2. Add item to BOM if it should be a component
3. Replace with an output from a previous step

#### Problem: Item `piping_and_valves_set` not found

This item doesn't exist in the KB.

**Suggestions:**
1. Check if item name is misspelled
2. Add item to BOM if it should be a component
3. Replace with an output from a previous step

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_machine_solar_thermal_storage_system_v0.yaml`
- **BOM available:** Yes (4 components)
