# Fix Intelligence: recipe_metal_alloy_bulk_v0

## Files

- **Recipe:** `kb/recipes/recipe_metal_alloy_bulk_v0.yaml`
- **Target item:** `metal_alloy_bulk`
  - File: `kb/items/metal_alloy_bulk.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'regolith_screening_sieving_v0') requires input 'regolith_lunar_mare' which is not available

**Location:** Step 1
**Process:** `regolith_screening_sieving_v0`
  - File: `kb/processes/regolith_screening_sieving_v0.yaml`

**Current step:**
```yaml
- process_id: regolith_screening_sieving_v0
  inputs:
  - item_id: regolith_lunar_mare
    qty: 100.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `regolith_lunar_mare` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'oxygen_extraction_molten_regolith_electrolysis_v0') requires input 'electrical_energy' which is not available

**Location:** Step 3
**Process:** `oxygen_extraction_molten_regolith_electrolysis_v0`
  - File: `kb/processes/oxygen_extraction_molten_regolith_electrolysis_v0.yaml`

**Current step:**
```yaml
- process_id: oxygen_extraction_molten_regolith_electrolysis_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_metal_alloy_bulk_v0.yaml`
- **BOM available:** No
