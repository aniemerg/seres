# Fix Intelligence: recipe_strain_gauge_bonded_assembly_v0

## Files

- **Recipe:** `kb/recipes/recipe_strain_gauge_bonded_assembly_v0.yaml`
- **Target item:** `strain_gauge_bonded_assembly`
  - File: `kb/items/strain_gauge_bonded_assembly.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'strain_gauge_bonding_process_v0') requires input 'strain_gauge_foil_v0' which is not available

**Location:** Step 0
**Process:** `strain_gauge_bonding_process_v0`
  - File: `kb/processes/strain_gauge_bonding_process_v0.yaml`

**Current step:**
```yaml
- process_id: strain_gauge_bonding_process_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_strain_gauge_bonded_assembly_v0.yaml`
- **BOM available:** No
