# Fix Intelligence: crushing_jaw_set_v0

## Files

- **Recipe:** `kb/recipes/crushing_jaw_set_v0.yaml`
- **Target item:** `crushing_jaw_set`
  - File: `kb/items/crushing_jaw_set.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_crushing_jaw_set_v0` → crushing_jaw_set (5 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'jaw_set_fabrication_v0') requires input 'steel_ingot' which is not available

**Location:** Step 0
**Process:** `jaw_set_fabrication_v0`
  - File: `kb/processes/jaw_set_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: jaw_set_fabrication_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/crushing_jaw_set_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
