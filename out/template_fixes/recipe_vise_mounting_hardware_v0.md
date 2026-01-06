# Fix Intelligence: recipe_vise_mounting_hardware_v0

## Files

- **Recipe:** `kb/recipes/recipe_vise_mounting_hardware_v0.yaml`
- **Target item:** `vise_mounting_hardware`
  - File: `kb/items/vise_mounting_hardware.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'machining_finish_basic_v0') requires input 'steel_stock_bar_or_billet' which is not available

**Location:** Step 0
**Process:** `machining_finish_basic_v0`
  - File: `kb/processes/machining_finish_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_finish_basic_v0
  inputs:
  - item_id: steel_stock_bar_or_billet
    qty: 5.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Generic placeholder `steel_stock_bar_or_billet`

This is not a real item. Need to replace with specific item.

**Specific items matching pattern:**

- `stainless_billet_or_slab`
- `steel_stock_bar_or_billet`
- `steel_billet_or_slab`

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_vise_mounting_hardware_v0.yaml`
- **BOM available:** No
