# Fix Intelligence: recipe_electrical_steel_sheet_v0

## Files

- **Recipe:** `kb/recipes/recipe_electrical_steel_sheet_v0.yaml`
- **Target item:** `electrical_steel_sheet`
  - File: `kb/items/electrical_steel_sheet.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'electrical_steel_production_v0') requires input 'iron_metal_pure' which is not available

**Location:** Step 0
**Process:** `electrical_steel_production_v0`
  - File: `kb/processes/electrical_steel_production_v0.yaml`

**Current step:**
```yaml
- process_id: electrical_steel_production_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_electrical_steel_sheet_v0.yaml`
- **BOM available:** No
