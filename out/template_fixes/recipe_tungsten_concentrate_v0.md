# Fix Intelligence: recipe_tungsten_concentrate_v0

## Files

- **Recipe:** `kb/recipes/recipe_tungsten_concentrate_v0.yaml`
- **Target item:** `tungsten_concentrate`
  - File: `kb/items/tungsten_concentrate.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'tungsten_density_separation_v0') requires input 'nife_alloy_byproduct' which is not available

**Location:** Step 0
**Process:** `tungsten_density_separation_v0`
  - File: `kb/processes/tungsten_density_separation_v0.yaml`

**Current step:**
```yaml
- process_id: tungsten_density_separation_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_tungsten_concentrate_v0.yaml`
- **BOM available:** No
