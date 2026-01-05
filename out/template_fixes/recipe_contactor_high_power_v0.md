# Fix Intelligence: recipe_contactor_high_power_v0

## Files

- **Recipe:** `kb/recipes/recipe_contactor_high_power_v0.yaml`
- **Target item:** `contactor_high_power_v0`
  - File: `kb/items/contactor_high_power_v0.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (4 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_stamping_process_v0') requires input 'steel_sheet_1mm' which is not available

**Location:** Step 0
**Process:** `metal_stamping_process_v0`
  - File: `kb/processes/metal_stamping_process_v0.yaml`

**Current step:**
```yaml
- process_id: metal_stamping_process_v0
  inputs:
  - item_id: steel_sheet_1mm
    qty: 0.05
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `steel_sheet_1mm` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'wire_winding_process_v0') requires input 'copper_wire_magnet' which is not available

**Location:** Step 1
**Process:** `wire_winding_process_v0`
  - File: `kb/processes/wire_winding_process_v0.yaml`

**Current step:**
```yaml
- process_id: wire_winding_process_v0
  inputs:
  - item_id: copper_wire_magnet
    qty: 0.04
    unit: kg
  - item_id: iron_core_laminated
    qty: 0.03
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `copper_wire_magnet` not found

This item doesn't exist in the KB.

#### Problem: Item `iron_core_laminated` not found

This item doesn't exist in the KB.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'contact_material_application_v0') requires input 'steel_sheet_1mm' which is not available

**Location:** Step 2
**Process:** `contact_material_application_v0`
  - File: `kb/processes/contact_material_application_v0.yaml`

**Current step:**
```yaml
- process_id: contact_material_application_v0
  inputs:
  - item_id: steel_sheet_1mm
    qty: 0.04
    unit: kg
  - item_id: silver_contact_material
    qty: 0.005
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `steel_sheet_1mm` not found

This item doesn't exist in the KB.

#### Problem: Item `silver_contact_material` not found

This item doesn't exist in the KB.

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'assembly_process_general_v0') requires input 'plastic_housing_molded' which is not available

**Location:** Step 3
**Process:** `assembly_process_general_v0`
  - File: `kb/processes/assembly_process_general_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_process_general_v0
  inputs:
  - item_id: relay_coil_assembly
    qty: 0.05
    unit: kg
  - item_id: contacts_with_applied_material_v0
    qty: 0.045
    unit: kg
  - item_id: plastic_housing_molded
    qty: 0.015
    unit: kg
  - item_id: spring_compression_small
    qty: 1.0
    unit: each
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `relay_coil_assembly` not found

This item doesn't exist in the KB.

#### Problem: Item `contacts_with_applied_material_v0` not found

This item doesn't exist in the KB.

#### Problem: Item `plastic_housing_molded` not found

This item doesn't exist in the KB.

#### Problem: Item `spring_compression_small` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_contactor_high_power_v0.yaml`
- **BOM available:** No
