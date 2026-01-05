# Fix Intelligence: recipe_circuit_breaker_thermal_v0

## Files

- **Recipe:** `kb/recipes/recipe_circuit_breaker_thermal_v0.yaml`
- **Target item:** `circuit_breaker_thermal_v0`
  - File: `kb/items/circuit_breaker_thermal_v0.yaml`
- **BOM:** None
- **Steps:** 5 total

## Errors (5 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'bimetallic_strip_forming_v0') requires input 'steel_strip_thin' which is not available

**Location:** Step 0
**Process:** `bimetallic_strip_forming_v0`
  - File: `kb/processes/bimetallic_strip_forming_v0.yaml`

**Current step:**
```yaml
- process_id: bimetallic_strip_forming_v0
  inputs:
  - item_id: steel_strip_thin
    qty: 0.02
    unit: kg
  - item_id: copper_strip_thin
    qty: 0.02
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `steel_strip_thin` not found

This item doesn't exist in the KB.

#### Problem: Item `copper_strip_thin` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'metal_stamping_process_v0') requires input 'steel_sheet_1mm' which is not available

**Location:** Step 1
**Process:** `metal_stamping_process_v0`
  - File: `kb/processes/metal_stamping_process_v0.yaml`

**Current step:**
```yaml
- process_id: metal_stamping_process_v0
  inputs:
  - item_id: steel_sheet_1mm
    qty: 0.1
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `steel_sheet_1mm` not found

This item doesn't exist in the KB.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'contact_material_application_v0') requires input 'silver_contact_material' which is not available

**Location:** Step 2
**Process:** `contact_material_application_v0`
  - File: `kb/processes/contact_material_application_v0.yaml`

**Current step:**
```yaml
- process_id: contact_material_application_v0
  inputs:
  - item_id: breaker_housing_and_mechanism
    qty: 0.09
    unit: kg
  - item_id: silver_contact_material
    qty: 0.01
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `breaker_housing_and_mechanism` not found

This item doesn't exist in the KB.

#### Problem: Item `silver_contact_material` not found

This item doesn't exist in the KB.

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'assembly_process_general_v0') requires input 'housing_with_contacts' which is not available

**Location:** Step 3
**Process:** `assembly_process_general_v0`
  - File: `kb/processes/assembly_process_general_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_process_general_v0
  inputs:
  - item_id: housing_with_contacts
    qty: 0.1
    unit: kg
  - item_id: bimetallic_element
    qty: 0.04
    unit: kg
  - item_id: spring_compression_small
    qty: 1.0
    unit: each
  - item_id: plastic_housing_molded
    qty: 0.05
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `housing_with_contacts` not found

This item doesn't exist in the KB.

#### Problem: Item `bimetallic_element` not found

This item doesn't exist in the KB.

#### Problem: Item `spring_compression_small` not found

This item doesn't exist in the KB.

#### Problem: Item `plastic_housing_molded` not found

This item doesn't exist in the KB.

---

### Error 5: recipe_step_input_not_satisfied

**Message:** Step 4 (process 'testing_and_calibration_circuit_breaker_v0') requires input 'circuit_breaker_assembled' which is not available

**Location:** Step 4
**Process:** `testing_and_calibration_circuit_breaker_v0`
  - File: `kb/processes/testing_and_calibration_circuit_breaker_v0.yaml`

**Current step:**
```yaml
- process_id: testing_and_calibration_circuit_breaker_v0
  inputs:
  - item_id: circuit_breaker_assembled
    qty: 0.25
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `circuit_breaker_assembled` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 5
- **Recipe file:** `kb/recipes/recipe_circuit_breaker_thermal_v0.yaml`
- **BOM available:** No
