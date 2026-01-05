# Fix Intelligence: recipe_part_bearing_set_heavy_v0

## Files

- **Recipe:** `kb/recipes/recipe_part_bearing_set_heavy_v0.yaml`
- **Target item:** `bearing_set_heavy`
  - File: `kb/items/bearing_set_heavy.yaml`
- **BOM:** None
- **Steps:** 2 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_bearing_set_heavy_v0` → bearing_set_heavy (13 steps)

## Errors (2 found)

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

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'sintering_and_hot_pressing_v0') requires input 'regolith_fine_fraction' which is not available

**Location:** Step 1
**Process:** `sintering_and_hot_pressing_v0`
  - File: `kb/processes/sintering_and_hot_pressing_v0.yaml`

**Current step:**
```yaml
- process_id: sintering_and_hot_pressing_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_part_bearing_set_heavy_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
