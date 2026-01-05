# Fix Intelligence: recipe_ceramic_drill_chip_waste_v0

## Files

- **Recipe:** `kb/recipes/recipe_ceramic_drill_chip_waste_v0.yaml`
- **Target item:** `ceramic_drill_chip_waste`
  - File: `kb/items/ceramic_drill_chip_waste.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'machining_process_drilling_v0') requires input 'center_insulator_ceramic' which is not available

**Location:** Step 0
**Process:** `machining_process_drilling_v0`
  - File: `kb/processes/machining_process_drilling_v0.yaml`

**Current step:**
```yaml
- process_id: machining_process_drilling_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_ceramic_drill_chip_waste_v0.yaml`
- **BOM available:** No
