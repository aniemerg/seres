# Fix Intelligence: recipe_battery_pack_large_nife_import_v0

## Files

- **Recipe:** `kb/recipes/recipe_battery_pack_large_nife_import_v0.yaml`
- **Target item:** `battery_pack_large_nife`
  - File: `kb/items/battery_pack_large_nife.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 2 recipes producing similar items:

- `recipe_battery_pack_large_nife_v0_alias_v0` → battery_pack_large_nife_v0 (1 steps)
- `recipe_battery_pack_large_nife_v0` → battery_pack_large_nife (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'battery_pack_assembly_nife') requires input 'nife_battery_cell' which is not available

**Location:** Step 0
**Process:** `battery_pack_assembly_nife`
  - File: `kb/processes/battery_pack_assembly_nife.yaml`

**Current step:**
```yaml
- process_id: battery_pack_assembly_nife
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_battery_pack_large_nife_import_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 2 found
