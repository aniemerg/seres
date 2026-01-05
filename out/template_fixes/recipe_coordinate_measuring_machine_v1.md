# Fix Intelligence: recipe_coordinate_measuring_machine_v1

## Files

- **Recipe:** `kb/recipes/recipe_coordinate_measuring_machine_v1.yaml`
- **Target item:** `coordinate_measuring_machine`
  - File: `kb/items/coordinate_measuring_machine.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 2 recipes producing similar items:

- `recipe_machine_coordinate_measuring_machine_v0` → coordinate_measuring_machine_v0 (8 steps)
- `recipe_coordinate_measuring_machine_v0` → coordinate_measuring_machine_v0 (8 steps)

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
- **Recipe file:** `kb/recipes/recipe_coordinate_measuring_machine_v1.yaml`
- **BOM available:** No
- **Similar recipes:** 2 found
