# Fix Intelligence: recipe_thermal_insulation_high_temp_v0

## Files

- **Recipe:** `kb/recipes/recipe_thermal_insulation_high_temp_v0.yaml`
- **Target item:** `thermal_insulation_high_temp`
  - File: `kb/items/thermal_insulation_high_temp.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'thermal_insulation_high_temp_production_v0') requires input 'ceramic_powder' which is not available

**Location:** Step 0
**Process:** `thermal_insulation_high_temp_production_v0`
  - File: `kb/processes/thermal_insulation_high_temp_production_v0.yaml`

**Current step:**
```yaml
- process_id: thermal_insulation_high_temp_production_v0
  inputs:
  - item_id: ceramic_powder
    qty: 1.5
    unit: kg
  - item_id: binder_material
    qty: 0.5
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `ceramic_powder` not found

This item doesn't exist in the KB.

#### Problem: Item `binder_material` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_thermal_insulation_high_temp_v0.yaml`
- **BOM available:** No
