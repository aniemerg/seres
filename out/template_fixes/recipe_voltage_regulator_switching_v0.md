# Fix Intelligence: recipe_voltage_regulator_switching_v0

## Files

- **Recipe:** `kb/recipes/recipe_voltage_regulator_switching_v0.yaml`
- **Target item:** `voltage_regulator_switching_v0`
  - File: `kb/items/voltage_regulator_switching_v0.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'electrical_assembly_basic_v0') requires input 'pcb_bare_board' which is not available

**Location:** Step 0
**Process:** `electrical_assembly_basic_v0`
  - File: `kb/processes/electrical_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: electrical_assembly_basic_v0
  inputs:
  - item_id: pcb_bare_board
    qty: 0.3
    unit: kg
  - item_id: electronic_components_set
    qty: 0.5
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `pcb_bare_board` not found

This item doesn't exist in the KB.

#### Problem: Item `electronic_components_set` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_voltage_regulator_switching_v0.yaml`
- **BOM available:** No
