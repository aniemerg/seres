# Fix Intelligence: recipe_co2_gas_v0

## Files

- **Recipe:** `kb/recipes/recipe_co2_gas_v0.yaml`
- **Target item:** `co2_gas`
  - File: `kb/items/co2_gas.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'aluminum_smelting_hall_heroult_v0') requires input 'alumina_powder' which is not available

**Location:** Step 0
**Process:** `aluminum_smelting_hall_heroult_v0`
  - File: `kb/processes/aluminum_smelting_hall_heroult_v0.yaml`

**Current step:**
```yaml
- process_id: aluminum_smelting_hall_heroult_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_co2_gas_v0.yaml`
- **BOM available:** No
