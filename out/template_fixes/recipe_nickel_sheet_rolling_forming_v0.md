# Fix Intelligence: recipe_nickel_sheet_rolling_forming_v0

## Files

- **Recipe:** `kb/recipes/recipe_nickel_sheet_rolling_forming_v0.yaml`
- **Target item:** `nickel_sheet_rolling_forming_v0`
  - File: `kb/items/nickel_sheet_rolling_forming_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'rolling_forming_nickel_sheet_v0') requires input 'nickel_sheet_rolling_v0' which is not available

**Location:** Step 0
**Process:** `rolling_forming_nickel_sheet_v0`
  - File: `kb/processes/rolling_forming_nickel_sheet_v0.yaml`

**Current step:**
```yaml
- process_id: rolling_forming_nickel_sheet_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_nickel_sheet_rolling_forming_v0.yaml`
- **BOM available:** No
