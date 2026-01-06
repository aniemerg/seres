# Fix Intelligence: recipe_cmc_solution_v0

## Files

- **Recipe:** `kb/recipes/recipe_cmc_solution_v0.yaml`
- **Target item:** `cmc_solution`
  - File: `kb/items/cmc_solution.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'chemical_synthesis_process_v0') requires input 'cellulose_raw' which is not available

**Location:** Step 0
**Process:** `chemical_synthesis_process_v0`
  - File: `kb/processes/chemical_synthesis_process_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: chemical_synthesis_process_v0
  inputs:
  - item_id: cellulose_raw
    qty: 1.0
    unit: kg
  - item_id: sodium_hydroxide
    qty: 0.3
    unit: kg
  - item_id: monochloroacetic_acid
    qty: 0.4
    unit: kg
  - item_id: water
    qty: 5.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `cellulose_raw` not found

This item doesn't exist in the KB.

#### Problem: Item `sodium_hydroxide` not found

This item doesn't exist in the KB.

#### Problem: Item `monochloroacetic_acid` not found

This item doesn't exist in the KB.

#### Problem: Item `water` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_cmc_solution_v0.yaml`
- **BOM available:** No
