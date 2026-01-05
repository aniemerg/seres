# Fix Intelligence: recipe_power_distribution_board_import_v0

## Files

- **Recipe:** `kb/recipes/recipe_power_distribution_board_import_v0.yaml`
- **Target item:** `power_distribution_board`
  - File: `kb/items/power_distribution_board.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'assembly_process_general_v0') requires input 'bus_bar_copper' which is not available

**Location:** Step 0
**Process:** `assembly_process_general_v0`
  - File: `kb/processes/assembly_process_general_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_process_general_v0
  inputs:
  - item_id: bus_bar_copper
    qty: 1.0
    unit: kg
  - item_id: circuit_breaker_thermal_v0
    qty: 6.0
    unit: each
  - item_id: terminal_block_set
    qty: 1.0
    unit: set
  - item_id: indicator_light_set
    qty: 1.0
    unit: set
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `bus_bar_copper` not found

This item doesn't exist in the KB.

#### Problem: Item `circuit_breaker_thermal_v0` not found

This item doesn't exist in the KB.

#### Problem: Item `terminal_block_set` not found

This item doesn't exist in the KB.

#### Problem: Item `indicator_light_set` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_power_distribution_board_import_v0.yaml`
- **BOM available:** No
