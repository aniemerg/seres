# Fix Intelligence: recipe_electrolyte_tank_v0

## Files

- **Recipe:** `kb/recipes/recipe_electrolyte_tank_v0.yaml`
- **Target item:** `electrolyte_tank`
  - File: `kb/items/electrolyte_tank.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'additive_manufacturing_polymer_v0') requires input 'polymer_printing_feedstock' which is not available

**Location:** Step 0
**Process:** `additive_manufacturing_polymer_v0`
  - File: `kb/processes/additive_manufacturing_polymer_v0.yaml`

**Current step:**
```yaml
- process_id: additive_manufacturing_polymer_v0
  inputs:
  - item_id: polymer_printing_feedstock
    qty: 1.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `polymer_printing_feedstock` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_electrolyte_tank_v0.yaml`
- **BOM available:** No
