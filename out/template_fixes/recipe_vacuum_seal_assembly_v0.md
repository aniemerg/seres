# Fix Intelligence: recipe_vacuum_seal_assembly_v0

## Files

- **Recipe:** `kb/recipes/recipe_vacuum_seal_assembly_v0.yaml`
- **Target item:** `vacuum_seal_assembly`
  - File: `kb/items/vacuum_seal_assembly.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'vacuum_seal_assembly_fabrication_v0') requires input 'formed_sheet_metal_parts' which is not available

**Location:** Step 0
**Process:** `vacuum_seal_assembly_fabrication_v0`
  - File: `kb/processes/vacuum_seal_assembly_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: vacuum_seal_assembly_fabrication_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_vacuum_seal_assembly_v0.yaml`
- **BOM available:** No
