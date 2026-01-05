# Fix Intelligence: recipe_basalt_aggregate_v0

## Files

- **Recipe:** `kb/recipes/recipe_basalt_aggregate_v0.yaml`
- **Target item:** `basalt_aggregate`
  - File: `kb/items/basalt_aggregate.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'rock_excavation_basic_v0') requires input 'regolith_lunar_mare' which is not available

**Location:** Step 0
**Process:** `rock_excavation_basic_v0`
  - File: `kb/processes/rock_excavation_basic_v0.yaml`

**Current step:**
```yaml
- process_id: rock_excavation_basic_v0
  inputs:
  - item_id: regolith_lunar_mare
    qty: 1.2
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `regolith_lunar_mare` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'crushing_and_screening_basic_v0') requires input 'regolith_lunar_mare' which is not available

**Location:** Step 1
**Process:** `crushing_and_screening_basic_v0`
  - File: `kb/processes/crushing_and_screening_basic_v0.yaml`

**Current step:**
```yaml
- process_id: crushing_and_screening_basic_v0
  inputs:
  - item_id: regolith_lunar_mare
    qty: 1.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `regolith_lunar_mare` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_basalt_aggregate_v0.yaml`
- **BOM available:** No
