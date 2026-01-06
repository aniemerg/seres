# Fix Intelligence: recipe_brass_bar_stock_v0

## Files

- **Recipe:** `kb/recipes/recipe_brass_bar_stock_v0.yaml`
- **Target item:** `brass_bar_stock`
  - File: `kb/items/brass_bar_stock.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_casting_basic_v0') requires input 'copper_rod_ingot' which is not available

**Location:** Step 0
**Process:** `metal_casting_basic_v0`
  - File: `kb/processes/metal_casting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: metal_casting_basic_v0
  inputs:
  - item_id: copper_rod_ingot
    qty: 0.7
    unit: kg
  - item_id: zinc_metal_v0
    qty: 0.3
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `copper_rod_ingot` not found

This item doesn't exist in the KB.

#### Problem: Item `zinc_metal_v0` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_brass_bar_stock_v0.yaml`
- **BOM available:** No
