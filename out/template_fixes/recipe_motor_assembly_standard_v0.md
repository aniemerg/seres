# Fix Intelligence: recipe_motor_assembly_standard_v0

## Files

- **Recipe:** `kb/recipes/recipe_motor_assembly_standard_v0.yaml`
- **Target item:** `motor_assembly_standard_v0`
  - File: `kb/items/motor_assembly_standard_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'motor_assembly_standard_fabrication_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `motor_assembly_standard_fabrication_v0`
  - File: `kb/processes/motor_assembly_standard_fabrication_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: motor_assembly_standard_fabrication_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_motor_assembly_standard_v0.yaml`
- **BOM available:** No
