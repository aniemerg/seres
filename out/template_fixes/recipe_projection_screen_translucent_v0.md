# Fix Intelligence: recipe_projection_screen_translucent_v0

## Files

- **Recipe:** `kb/recipes/recipe_projection_screen_translucent_v0.yaml`
- **Target item:** `projection_screen_translucent`
  - File: `kb/items/projection_screen_translucent.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'projection_screen_sheet_casting_v0') requires input 'plastic_pellets' which is not available

**Location:** Step 0
**Process:** `projection_screen_sheet_casting_v0`
  - File: `kb/processes/projection_screen_sheet_casting_v0.yaml`

**Current step:**
```yaml
- process_id: projection_screen_sheet_casting_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_projection_screen_translucent_v0.yaml`
- **BOM available:** No
