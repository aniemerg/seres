# Fix Intelligence: recipe_machine_stepper_motor_v0

## Files

- **Recipe:** `kb/recipes/recipe_machine_stepper_motor_v0.yaml`
- **Target item:** `stepper_motor_v0`
  - File: `kb/items/stepper_motor_v0.yaml`
- **BOM:** `kb/boms/bom_stepper_motor_v0.yaml` ✓
  - Components: 7
- **Steps:** 5 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_stamping_process_v0') requires input 'electrical_steel_sheet' which is not available

**Location:** Step 0
**Process:** `metal_stamping_process_v0`
  - File: `kb/processes/metal_stamping_process_v0.yaml`

**Current step:**
```yaml
- process_id: metal_stamping_process_v0
  inputs:
  - item_id: electrical_steel_sheet
    qty: 1.2
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `electrical_steel_sheet` not found

This item doesn't exist in the KB.

**Suggestions:**
1. Check if item name is misspelled
2. Add item to BOM if it should be a component
3. Replace with an output from a previous step

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'machining_process_turning_v0') requires input 'aluminum_alloy_ingot' which is not available

**Location:** Step 3
**Process:** `machining_process_turning_v0`
  - File: `kb/processes/machining_process_turning_v0.yaml`

**Current step:**
```yaml
- process_id: machining_process_turning_v0
  inputs:
  - item_id: aluminum_alloy_ingot
    qty: 0.6
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `aluminum_alloy_ingot` not found

This item doesn't exist in the KB.

**Suggestions:**
1. Check if item name is misspelled
2. Add item to BOM if it should be a component
3. Replace with an output from a previous step

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 4 (process 'assembly_process_general_v0') requires input 'stator_wound' which is not available

**Location:** Step 4
**Process:** `assembly_process_general_v0`
  - File: `kb/processes/assembly_process_general_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_process_general_v0
  inputs:
  - item_id: stator_wound
    qty: 1.0
    unit: kg
  - item_id: steel_lamination_stack
    qty: 0.2
    unit: kg
  - item_id: rotor_magnets_magnetized
    qty: 0.2
    unit: kg
  - item_id: steel_shaft_machined
    qty: 0.2
    unit: kg
  - item_id: motor_housing_steel
    qty: 0.4
    unit: kg
  - item_id: bearing_ball_steel
    qty: 2.0
    unit: each
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `stator_wound` not found

This item doesn't exist in the KB.

**Suggestions:**
1. Check if item name is misspelled
2. Add item to BOM if it should be a component
3. Replace with an output from a previous step

#### Problem: Item `steel_lamination_stack` not found

This item doesn't exist in the KB.

#### Problem: Item `rotor_magnets_magnetized` not found

This item doesn't exist in the KB.

**Suggestions:**
1. Check if item name is misspelled
2. Add item to BOM if it should be a component
3. Replace with an output from a previous step

#### Problem: Item `steel_shaft_machined` not found

This item doesn't exist in the KB.

#### Problem: Item `motor_housing_steel` not found

This item doesn't exist in the KB.

**Suggestions:**
1. Check if item name is misspelled
2. Add item to BOM if it should be a component
3. Replace with an output from a previous step

#### Problem: Item `bearing_ball_steel` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_machine_stepper_motor_v0.yaml`
- **BOM available:** Yes (7 components)
