# Fix Intelligence: recipe_bearing_ball_steel_v0

## Files

- **Recipe:** `kb/recipes/recipe_bearing_ball_steel_v0.yaml`
- **Target item:** `bearing_ball_steel`
  - File: `kb/items/bearing_ball_steel.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'bearing_ball_steel_cast_v0') requires input 'steel_ingot' which is not available

**Location:** Step 0
**Process:** `bearing_ball_steel_cast_v0`
  - File: `kb/processes/bearing_ball_steel_cast_v0.yaml`

**Current step:**
```yaml
- process_id: bearing_ball_steel_cast_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_bearing_ball_steel_v0.yaml`
- **BOM available:** No
