# Fix Intelligence: recipe_conveyor_belt_loop_v0

## Files

- **Recipe:** `kb/recipes/recipe_conveyor_belt_loop_v0.yaml`
- **Target item:** `conveyor_belt_loop`
  - File: `kb/items/conveyor_belt_loop.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'conveyor_belt_loop_fabrication_v0') requires input 'molded_rubber_or_plastic_piece_v0' which is not available

**Location:** Step 0
**Process:** `conveyor_belt_loop_fabrication_v0`
  - File: `kb/processes/conveyor_belt_loop_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: conveyor_belt_loop_fabrication_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_conveyor_belt_loop_v0.yaml`
- **BOM available:** No
