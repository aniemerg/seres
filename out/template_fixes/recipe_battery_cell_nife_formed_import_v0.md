# Fix Intelligence: recipe_battery_cell_nife_formed_import_v0

## Files

- **Recipe:** `kb/recipes/recipe_battery_cell_nife_formed_import_v0.yaml`
- **Target item:** `battery_cell_nife_formed`
  - File: `kb/items/battery_cell_nife_formed.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_battery_cell_nife_formed_v0` → battery_cell_nife_formed (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'formation_cycle_nife') requires input 'battery_cell_nife' which is not available

**Location:** Step 0
**Process:** `formation_cycle_nife`
  - File: `kb/processes/formation_cycle_nife.yaml`

**Current step:**
```yaml
- process_id: formation_cycle_nife
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_battery_cell_nife_formed_import_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
