# Fix Intelligence: recipe_copper_clad_laminate_v0_alt

## Files

- **Recipe:** `kb/recipes/recipe_copper_clad_laminate_v0_alt.yaml`
- **Target item:** `copper_clad_laminate`
  - File: `kb/items/copper_clad_laminate.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_copper_clad_laminate_v0` → copper_clad_laminate (1 steps)

## Errors (1 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'lamination_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `lamination_basic_v0`
  - File: `kb/processes/lamination_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: lamination_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_copper_clad_laminate_v0_alt.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
