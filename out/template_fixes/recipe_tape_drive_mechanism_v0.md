# Fix Intelligence: recipe_tape_drive_mechanism_v0

## Files

- **Recipe:** `kb/recipes/recipe_tape_drive_mechanism_v0.yaml`
- **Target item:** `tape_drive_mechanism`
  - File: `kb/items/tape_drive_mechanism.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_tape_drive_mechanism_v1` → tape_drive_mechanism (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'tape_drive_mechanism_fabrication_v0') requires input 'steel_stock' which is not available

**Location:** Step 0
**Process:** `tape_drive_mechanism_fabrication_v0`
  - File: `kb/processes/tape_drive_mechanism_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: tape_drive_mechanism_fabrication_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_tape_drive_mechanism_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
