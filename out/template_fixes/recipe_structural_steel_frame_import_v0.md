# Fix Intelligence: recipe_structural_steel_frame_import_v0

## Files

- **Recipe:** `kb/recipes/recipe_structural_steel_frame_import_v0.yaml`
- **Target item:** `structural_steel_frame`
  - File: `kb/items/structural_steel_frame.yaml`
- **BOM:** None
- **Steps:** 3 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_structural_steel_frame_v0` → structural_steel_frame (6 steps)

## Errors (2 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'cutting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `cutting_basic_v0`
  - File: `kb/processes/cutting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: cutting_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'welding_structural_v0') requires input 'cut_parts' which is not available

**Location:** Step 1
**Process:** `welding_structural_v0`
  - File: `kb/processes/welding_structural_v0.yaml`

**Current step:**
```yaml
- process_id: welding_structural_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_structural_steel_frame_import_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
