# Fix Intelligence: recipe_heliostat_mounting_bracket_v0

## Files

- **Recipe:** `kb/recipes/recipe_heliostat_mounting_bracket_v0.yaml`
- **Target item:** `heliostat_mounting_bracket_v0`
  - File: `kb/items/heliostat_mounting_bracket_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'heliostat_mounting_bracket_fabrication_v0') requires input 'steel_plate_or_sheet' which is not available

**Location:** Step 0
**Process:** `heliostat_mounting_bracket_fabrication_v0`
  - File: `kb/processes/heliostat_mounting_bracket_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: heliostat_mounting_bracket_fabrication_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_heliostat_mounting_bracket_v0.yaml`
- **BOM available:** No
