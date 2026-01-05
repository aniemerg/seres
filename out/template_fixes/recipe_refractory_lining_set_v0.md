# Fix Intelligence: recipe_refractory_lining_set_v0

## Files

- **Recipe:** `kb/recipes/recipe_refractory_lining_set_v0.yaml`
- **Target item:** `refractory_lining_set`
  - File: `kb/items/refractory_lining_set.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'refractory_casting_v0') requires input 'alumina_powder' which is not available

**Location:** Step 0
**Process:** `refractory_casting_v0`
  - File: `kb/processes/refractory_casting_v0.yaml`

**Current step:**
```yaml
- process_id: refractory_casting_v0
  inputs:
  - item_id: alumina_powder
    qty: 10.0
    unit: kg
  - item_id: ceramic_binder
    qty: 2.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `alumina_powder` not found

This item doesn't exist in the KB.

#### Problem: Item `ceramic_binder` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'drying_and_curing_v0') requires input 'wet_material' which is not available

**Location:** Step 1
**Process:** `drying_and_curing_v0`
  - File: `kb/processes/drying_and_curing_v0.yaml`

**Current step:**
```yaml
- process_id: drying_and_curing_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_refractory_lining_set_v0.yaml`
- **BOM available:** No
