# Fix Intelligence: recipe_pressure_test_rig_basic_alias_v0

## Files

- **Recipe:** `kb/recipes/recipe_pressure_test_rig_basic_alias_v0.yaml`
- **Target item:** `pressure_test_rig_basic`
  - File: `kb/items/pressure_test_rig_basic.yaml`
- **BOM:** None
- **Steps:** 2 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_pressure_test_rig_basic_v0` → pressure_test_rig_basic_v0 (2 steps)

## Errors (1 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_pressure_test_rig_basic_alias_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
