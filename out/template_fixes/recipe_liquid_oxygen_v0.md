# Fix Intelligence: recipe_liquid_oxygen_v0

## Files

- **Recipe:** `kb/recipes/recipe_liquid_oxygen_v0.yaml`
- **Target item:** `liquid_oxygen_v0`
  - File: `kb/items/liquid_oxygen_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_liquid_oxygen_from_cryogenic_v0` → liquid_oxygen_v0 (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'cold_trap_cryogenic_v0') requires input 'oxygen_gas' which is not available

**Location:** Step 0
**Process:** `cold_trap_cryogenic_v0`
  - File: `kb/processes/cold_trap_cryogenic_v0.yaml`

**Current step:**
```yaml
- process_id: cold_trap_cryogenic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_liquid_oxygen_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
