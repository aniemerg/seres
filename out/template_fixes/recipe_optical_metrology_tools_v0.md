# Fix Intelligence: recipe_optical_metrology_tools_v0

## Files

- **Recipe:** `kb/recipes/recipe_optical_metrology_tools_v0.yaml`
- **Target item:** `optical_metrology_tools`
  - File: `kb/items/optical_metrology_tools.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'optical_metrology_tools_assembly_v0') requires input 'autocollimator_imported' which is not available

**Location:** Step 0
**Process:** `optical_metrology_tools_assembly_v0`
  - File: `kb/processes/optical_metrology_tools_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: optical_metrology_tools_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_optical_metrology_tools_v0.yaml`
- **BOM available:** No
