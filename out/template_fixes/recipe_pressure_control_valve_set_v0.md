# Fix Intelligence: recipe_pressure_control_valve_set_v0

## Files

- **Recipe:** `kb/recipes/recipe_pressure_control_valve_set_v0.yaml`
- **Target item:** `pressure_control_valve_set`
  - File: `kb/items/pressure_control_valve_set.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'machining_finish_basic_v0') requires input 'stainless_steel_bar' which is not available

**Location:** Step 0
**Process:** `machining_finish_basic_v0`
  - File: `kb/processes/machining_finish_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_finish_basic_v0
  inputs:
  - item_id: stainless_steel_bar
    qty: 5.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `stainless_steel_bar` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'pressure_control_valve_assembly_v0') requires input 'steel_stock' which is not available

**Location:** Step 1
**Process:** `pressure_control_valve_assembly_v0`
  - File: `kb/processes/pressure_control_valve_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: pressure_control_valve_assembly_v0
  inputs:
  - item_id: steel_stock
    qty: 0.5
    unit: kg
  - item_id: gasket_sheet_material_v0
    qty: 0.5
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `steel_stock` not found

This item doesn't exist in the KB.

#### Problem: Item `gasket_sheet_material_v0` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_pressure_control_valve_set_v0.yaml`
- **BOM available:** No
