# Fix Intelligence: recipe_insulated_assembly_v0

## Files

- **Recipe:** `kb/recipes/recipe_insulated_assembly_v0.yaml`
- **Target item:** `insulated_assembly`
  - File: `kb/items/insulated_assembly.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'insulation_installation_v0') requires input 'insulation_thermal_blanket' which is not available

**Location:** Step 0
**Process:** `insulation_installation_v0`
  - File: `kb/processes/insulation_installation_v0.yaml`

**Current step:**
```yaml
- process_id: insulation_installation_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_insulated_assembly_v0.yaml`
- **BOM available:** No
