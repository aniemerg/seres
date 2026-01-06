# Fix Intelligence: recipe_steel_stock_bar_or_billet_v0

## Files

- **Recipe:** `kb/recipes/recipe_steel_stock_bar_or_billet_v0.yaml`
- **Target item:** `steel_stock_bar_or_billet`
  - File: `kb/items/steel_stock_bar_or_billet.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'rolling_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `rolling_basic_v0`
  - File: `kb/processes/rolling_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: rolling_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_steel_stock_bar_or_billet_v0.yaml`
- **BOM available:** No
