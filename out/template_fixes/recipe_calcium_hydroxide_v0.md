# Fix Intelligence: recipe_calcium_hydroxide_v0

## Files

- **Recipe:** `kb/recipes/recipe_calcium_hydroxide_v0.yaml`
- **Target item:** `calcium_hydroxide`
  - File: `kb/items/calcium_hydroxide.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'chemical_mixing_basic_v0') requires input 'calcium_oxide' which is not available

**Location:** Step 0
**Process:** `chemical_mixing_basic_v0`
  - File: `kb/processes/chemical_mixing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: chemical_mixing_basic_v0
  inputs:
  - item_id: calcium_oxide
    qty: 0.76
    unit: kg
  - item_id: water
    qty: 0.24
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `calcium_oxide` not found

This item doesn't exist in the KB.

#### Problem: Item `water` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_calcium_hydroxide_v0.yaml`
- **BOM available:** No
