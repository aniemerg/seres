# Fix Intelligence: recipe_machine_power_conditioner_v0

## Files

- **Recipe:** `kb/recipes/recipe_machine_power_conditioner_v0.yaml`
- **Target item:** `power_conditioner`
  - File: `kb/items/power_conditioner.yaml`
- **BOM:** None
- **Steps:** 1 total

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
- **Recipe file:** `kb/recipes/recipe_machine_power_conditioner_v0.yaml`
- **BOM available:** No
