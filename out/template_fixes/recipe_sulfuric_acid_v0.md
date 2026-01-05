# Fix Intelligence: recipe_sulfuric_acid_v0

## Files

- **Recipe:** `kb/recipes/recipe_sulfuric_acid_v0.yaml`
- **Target item:** `sulfuric_acid`
  - File: `kb/items/sulfuric_acid.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'sulfuric_acid_dilution_v0') requires input 'sulfuric_acid_concentrated' which is not available

**Location:** Step 0
**Process:** `sulfuric_acid_dilution_v0`
  - File: `kb/processes/sulfuric_acid_dilution_v0.yaml`

**Current step:**
```yaml
- process_id: sulfuric_acid_dilution_v0
  inputs:
  - item_id: sulfuric_acid_concentrated
    qty: 1.0
    unit: kg
  - item_id: water
    qty: 4.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `sulfuric_acid_concentrated` not found

This item doesn't exist in the KB.

#### Problem: Item `water` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_sulfuric_acid_v0.yaml`
- **BOM available:** No
