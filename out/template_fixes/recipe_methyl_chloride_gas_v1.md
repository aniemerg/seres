# Fix Intelligence: recipe_methyl_chloride_gas_v1

## Files

- **Recipe:** `kb/recipes/recipe_methyl_chloride_gas_v1.yaml`
- **Target item:** `methyl_chloride_gas`
  - File: `kb/items/methyl_chloride_gas.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'methylchloride_synthesis_v0') requires input 'methane_gas' which is not available

**Location:** Step 0
**Process:** `methylchloride_synthesis_v0`
  - File: `kb/processes/methylchloride_synthesis_v0.yaml`

**Current step:**
```yaml
- process_id: methylchloride_synthesis_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_methyl_chloride_gas_v1.yaml`
- **BOM available:** No
