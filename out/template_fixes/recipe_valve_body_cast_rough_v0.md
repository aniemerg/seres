# Fix Intelligence: recipe_valve_body_cast_rough_v0

## Files

- **Recipe:** `kb/recipes/recipe_valve_body_cast_rough_v0.yaml`
- **Target item:** `valve_body_cast_rough_v0`
  - File: `kb/items/valve_body_cast_rough_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_valve_body_cast_rough_v1` → valve_body_cast_rough (1 steps)

## Errors (1 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'metal_casting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `metal_casting_basic_v0`
  - File: `kb/processes/metal_casting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: metal_casting_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_valve_body_cast_rough_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
