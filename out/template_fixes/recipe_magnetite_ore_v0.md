# Fix Intelligence: recipe_magnetite_ore_v0

## Files

- **Recipe:** `kb/recipes/recipe_magnetite_ore_v0.yaml`
- **Target item:** `magnetite_ore`
  - File: `kb/items/magnetite_ore.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'olivine_hydration_v0') requires input 'olivine_concentrate' which is not available

**Location:** Step 0
**Process:** `olivine_hydration_v0`
  - File: `kb/processes/olivine_hydration_v0.yaml`

**Current step:**
```yaml
- process_id: olivine_hydration_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_magnetite_ore_v0.yaml`
- **BOM available:** No
