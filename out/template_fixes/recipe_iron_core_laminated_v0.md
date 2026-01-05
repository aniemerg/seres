# Fix Intelligence: recipe_iron_core_laminated_v0

## Files

- **Recipe:** `kb/recipes/recipe_iron_core_laminated_v0.yaml`
- **Target item:** `iron_core_laminated`
  - File: `kb/items/iron_core_laminated.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'iron_core_lamination_basic_v0') requires input 'steel_sheet_1mm' which is not available

**Location:** Step 0
**Process:** `iron_core_lamination_basic_v0`
  - File: `kb/processes/iron_core_lamination_basic_v0.yaml`

**Current step:**
```yaml
- process_id: iron_core_lamination_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_iron_core_laminated_v0.yaml`
- **BOM available:** No
