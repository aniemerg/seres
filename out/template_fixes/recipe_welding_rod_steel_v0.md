# Fix Intelligence: recipe_welding_rod_steel_v0

## Files

- **Recipe:** `kb/recipes/recipe_welding_rod_steel_v0.yaml`
- **Target item:** `welding_rod_steel`
  - File: `kb/items/welding_rod_steel.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'metal_forming_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `metal_forming_basic_v0`
  - File: `kb/processes/metal_forming_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: metal_forming_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_welding_rod_steel_v0.yaml`
- **BOM available:** No
