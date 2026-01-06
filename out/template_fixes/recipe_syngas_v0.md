# Fix Intelligence: recipe_syngas_v0

## Files

- **Recipe:** `kb/recipes/recipe_syngas_v0.yaml`
- **Target item:** `syngas`
  - File: `kb/items/syngas.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'syngas_generation_steam_reforming_v0') requires input 'methane_gas' which is not available

**Location:** Step 0
**Process:** `syngas_generation_steam_reforming_v0`
  - File: `kb/processes/syngas_generation_steam_reforming_v0.yaml`

**Current step:**
```yaml
- process_id: syngas_generation_steam_reforming_v0
  inputs:
  - item_id: methane_gas
    qty: 1.0
    unit: kg
  - item_id: water
    qty: 2.25
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `methane_gas` not found

This item doesn't exist in the KB.

#### Problem: Item `water` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_syngas_v0.yaml`
- **BOM available:** No
