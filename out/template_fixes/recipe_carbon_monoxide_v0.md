# Fix Intelligence: recipe_carbon_monoxide_v0

## Files

- **Recipe:** `kb/recipes/recipe_carbon_monoxide_v0.yaml`
- **Target item:** `carbon_monoxide`
  - File: `kb/items/carbon_monoxide.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'boudouard_reaction_v0') requires input 'carbon_reductant' which is not available

**Location:** Step 0
**Process:** `boudouard_reaction_v0`
  - File: `kb/processes/boudouard_reaction_v0.yaml`

**Current step:**
```yaml
- process_id: boudouard_reaction_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_carbon_monoxide_v0.yaml`
- **BOM available:** No
