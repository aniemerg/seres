# Fix Intelligence: recipe_iron_powder_or_sheet_v0

## Files

- **Recipe:** `kb/recipes/recipe_iron_powder_or_sheet_v0.yaml`
- **Target item:** `iron_powder_or_sheet`
  - File: `kb/items/iron_powder_or_sheet.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'iron_pure_production_from_ilmenite_v0') requires input 'iron_ore_or_ilmenite' which is not available

**Location:** Step 0
**Process:** `iron_pure_production_from_ilmenite_v0`
  - File: `kb/processes/iron_pure_production_from_ilmenite_v0.yaml`

**Current step:**
```yaml
- process_id: iron_pure_production_from_ilmenite_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_iron_powder_or_sheet_v0.yaml`
- **BOM available:** No
