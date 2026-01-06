# Fix Intelligence: recipe_hydraulic_adjustment_system_v0

## Files

- **Recipe:** `kb/recipes/recipe_hydraulic_adjustment_system_v0.yaml`
- **Target item:** `hydraulic_adjustment_system`
  - File: `kb/items/hydraulic_adjustment_system.yaml`
- **BOM:** None
- **Steps:** 5 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_hydraulic_adjustment_system_import_v0` → hydraulic_adjustment_system (5 steps)

## Errors (5 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_casting_process_v0') requires input 'aluminum_alloy_ingot' which is not available

**Location:** Step 0
**Process:** `metal_casting_process_v0`
  - File: `kb/processes/metal_casting_process_v0.yaml`

**Current step:**
```yaml
- process_id: metal_casting_process_v0
  inputs:
  - item_id: aluminum_alloy_ingot
    qty: 8.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `aluminum_alloy_ingot` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'machining_process_boring_v0') requires input 'hydraulic_cylinder_body_cast' which is not available

**Location:** Step 1
**Process:** `machining_process_boring_v0`
  - File: `kb/processes/machining_process_boring_v0.yaml`

**Current step:**
```yaml
- process_id: machining_process_boring_v0
  inputs:
  - item_id: hydraulic_cylinder_body_cast
    qty: 7.2
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `hydraulic_cylinder_body_cast` not found

This item doesn't exist in the KB.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'machining_process_turning_v0') requires input 'steel_bar_stock' which is not available

**Location:** Step 2
**Process:** `machining_process_turning_v0`
  - File: `kb/processes/machining_process_turning_v0.yaml`

**Current step:**
```yaml
- process_id: machining_process_turning_v0
  inputs:
  - item_id: steel_bar_stock
    qty: 3.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `steel_bar_stock` not found

This item doesn't exist in the KB.

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'machining_process_milling_v0') requires input 'aluminum_alloy_ingot' which is not available

**Location:** Step 3
**Process:** `machining_process_milling_v0`
  - File: `kb/processes/machining_process_milling_v0.yaml`

**Current step:**
```yaml
- process_id: machining_process_milling_v0
  inputs:
  - item_id: aluminum_alloy_ingot
    qty: 2.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `aluminum_alloy_ingot` not found

This item doesn't exist in the KB.

---

### Error 5: recipe_step_input_not_satisfied

**Message:** Step 4 (process 'assembly_process_general_v0') requires input 'hydraulic_cylinder_body_machined' which is not available

**Location:** Step 4
**Process:** `assembly_process_general_v0`
  - File: `kb/processes/assembly_process_general_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_process_general_v0
  inputs:
  - item_id: hydraulic_cylinder_body_machined
    qty: 6.5
    unit: kg
  - item_id: steel_shaft_machined
    qty: 2.5
    unit: kg
  - item_id: hydraulic_control_valve_set
    qty: 1.5
    unit: kg
  - item_id: seal_mechanical_rotary
    qty: 4.0
    unit: each
  - item_id: hydraulic_hose_assembly
    qty: 2.0
    unit: kg
  - item_id: cutting_fluid
    qty: 3.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `hydraulic_cylinder_body_machined` not found

This item doesn't exist in the KB.

#### Problem: Item `steel_shaft_machined` not found

This item doesn't exist in the KB.

#### Problem: Item `hydraulic_control_valve_set` not found

This item doesn't exist in the KB.

#### Problem: Item `seal_mechanical_rotary` not found

This item doesn't exist in the KB.

#### Problem: Item `hydraulic_hose_assembly` not found

This item doesn't exist in the KB.

#### Problem: Item `cutting_fluid` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 5
- **Recipe file:** `kb/recipes/recipe_hydraulic_adjustment_system_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
