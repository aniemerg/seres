# Fix Intelligence: recipe_holonic_control_prosa_output_v2

## Files

- **Recipe:** `kb/recipes/recipe_holonic_control_prosa_output_v2.yaml`
- **Target item:** `holonic_control_prosa_output`
  - File: `kb/items/holonic_control_prosa_output.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'holonic_control_prosa_v0') requires input 'software_service_license' which is not available

**Location:** Step 0
**Process:** `holonic_control_prosa_v0`
  - File: `kb/processes/holonic_control_prosa_v0.yaml`

**Current step:**
```yaml
- process_id: holonic_control_prosa_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_holonic_control_prosa_output_v2.yaml`
- **BOM available:** No
