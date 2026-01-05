# Fix Intelligence: recipe_machine_water_electrolysis_system_v0

## Files

- **Recipe:** `kb/recipes/recipe_machine_water_electrolysis_system_v0.yaml`
- **Target item:** `water_electrolysis_system_v0`
  - File: `kb/items/water_electrolysis_system_v0.yaml`
- **BOM:** `kb/boms/bom_water_electrolysis_system_v0.yaml` ✓
  - Components: 9
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_fabrication_welding_v0') requires input 'steel_sheet_3mm' which is not available

**Location:** Step 0
**Process:** `metal_fabrication_welding_v0`
  - File: `kb/processes/metal_fabrication_welding_v0.yaml`

**Current step:**
```yaml
- process_id: metal_fabrication_welding_v0
  inputs:
  - item_id: steel_sheet_3mm
    qty: 50.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `steel_sheet_3mm` not found

This item doesn't exist in the KB.

**Suggestions:**
1. Check if item name is misspelled
2. Add item to BOM if it should be a component
3. Replace with an output from a previous step

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'assembly_process_general_v0') requires input 'sealing_gaskets' which is not available

**Location:** Step 1
**Process:** `assembly_process_general_v0`
  - File: `kb/processes/assembly_process_general_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_process_general_v0
  inputs:
  - item_id: gas_separation_chamber
    qty: 45.0
    unit: kg
  - item_id: sealing_gaskets
    qty: 20.0
    unit: each
  - item_id: electrolyzer_cell_stack
    qty: 1.0
    unit: each
  - item_id: piping_and_valves_set
    qty: 10.0
    unit: kg
  - item_id: gas_collection_system
    qty: 2.0
    unit: each
  - item_id: power_supply_dc_controlled
    qty: 1.0
    unit: each
  - item_id: pressure_gauge
    qty: 2.0
    unit: each
  - item_id: thermocouple_type_k_v0
    qty: 2.0
    unit: each
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `gas_separation_chamber` not found

This item doesn't exist in the KB.

#### Problem: Item `sealing_gaskets` not found

This item doesn't exist in the KB.

**Suggestions:**
1. Check if item name is misspelled
2. Add item to BOM if it should be a component
3. Replace with an output from a previous step

#### Problem: Item `electrolyzer_cell_stack` not found

This item doesn't exist in the KB.

#### Problem: Item `piping_and_valves_set` not found

This item doesn't exist in the KB.

**Suggestions:**
1. Check if item name is misspelled
2. Add item to BOM if it should be a component
3. Replace with an output from a previous step

#### Problem: Item `gas_collection_system` not found

This item doesn't exist in the KB.

**Suggestions:**
1. Check if item name is misspelled
2. Add item to BOM if it should be a component
3. Replace with an output from a previous step

#### Problem: Item `power_supply_dc_controlled` not found

This item doesn't exist in the KB.

#### Problem: Item `pressure_gauge` not found

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

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_machine_water_electrolysis_system_v0.yaml`
- **BOM available:** Yes (9 components)
