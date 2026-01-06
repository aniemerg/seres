# Fix Intelligence: recipe_lead_screw_assembly_v0

## Files

- **Recipe:** `kb/recipes/recipe_lead_screw_assembly_v0.yaml`
- **Target item:** `lead_screw_assembly`
  - File: `kb/items/lead_screw_assembly.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'lead_screw_fabrication_v0') requires input 'steel_bar_stock' which is not available

**Location:** Step 0
**Process:** `lead_screw_fabrication_v0`
  - File: `kb/processes/lead_screw_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: lead_screw_fabrication_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_lead_screw_assembly_v0.yaml`
- **BOM available:** No
