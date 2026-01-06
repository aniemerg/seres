# Fix Intelligence: recipe_metal_tubing_stock_v1

## Files

- **Recipe:** `kb/recipes/recipe_metal_tubing_stock_v1.yaml`
- **Target item:** `metal_tubing_stock`
  - File: `kb/items/metal_tubing_stock.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_metal_tubing_stock_v0` → metal_tubing_stock (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'tube_stock_forming_v0') requires input 'steel_stock' which is not available

**Location:** Step 0
**Process:** `tube_stock_forming_v0`
  - File: `kb/processes/tube_stock_forming_v0.yaml`

**Current step:**
```yaml
- process_id: tube_stock_forming_v0
  inputs:
  - item_id: steel_stock
    qty: 1.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `steel_stock` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_metal_tubing_stock_v1.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
