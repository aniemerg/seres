# Fix Intelligence: recipe_programmed_microcontroller_v1

## Files

- **Recipe:** `kb/recipes/recipe_programmed_microcontroller_v1.yaml`
- **Target item:** `programmed_microcontroller`
  - File: `kb/items/programmed_microcontroller.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'firmware_programming_v0') requires input 'microcontroller_or_embedded_board' which is not available

**Location:** Step 0
**Process:** `firmware_programming_v0`
  - File: `kb/processes/firmware_programming_v0.yaml`

**Current step:**
```yaml
- process_id: firmware_programming_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_programmed_microcontroller_v1.yaml`
- **BOM available:** No
