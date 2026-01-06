# Fix Intelligence: recipe_krypton_gas_v0

## Files

- **Recipe:** `kb/recipes/recipe_krypton_gas_v0.yaml`
- **Target item:** `krypton_gas`
  - File: `kb/items/krypton_gas.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'noble_gas_extraction_v0') requires input 'carbon_dioxide_gas' which is not available

**Location:** Step 0
**Process:** `noble_gas_extraction_v0`
  - File: `kb/processes/noble_gas_extraction_v0.yaml`

**Current step:**
```yaml
- process_id: noble_gas_extraction_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_krypton_gas_v0.yaml`
- **BOM available:** No
