# Fix Intelligence: recipe_nickel_metal_import_v0

## Files

- **Recipe:** `kb/recipes/recipe_nickel_metal_import_v0.yaml`
- **Target item:** `nickel_metal`
  - File: `kb/items/nickel_metal.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'nickel_extraction_meteorite_v0') requires input 'meteorite_iron' which is not available

**Location:** Step 0
**Process:** `nickel_extraction_meteorite_v0`
  - File: `kb/processes/nickel_extraction_meteorite_v0.yaml`

**Current step:**
```yaml
- process_id: nickel_extraction_meteorite_v0
  inputs:
  - item_id: meteorite_iron
    qty: 10.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `meteorite_iron` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_nickel_metal_import_v0.yaml`
- **BOM available:** No
