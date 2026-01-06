# Fix Intelligence: recipe_inert_gas_fill_v0

## Files

- **Recipe:** `kb/recipes/recipe_inert_gas_fill_v0.yaml`
- **Target item:** `inert_gas_fill_v0`
  - File: `kb/items/inert_gas_fill_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'inert_gas_fill_basic_v0') requires input 'nitrogen_gas_purified' which is not available

**Location:** Step 0
**Process:** `inert_gas_fill_basic_v0`
  - File: `kb/processes/inert_gas_fill_basic_v0.yaml`

**Current step:**
```yaml
- process_id: inert_gas_fill_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_inert_gas_fill_v0.yaml`
- **BOM available:** No
