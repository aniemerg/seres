# Fix Intelligence: recipe_pump_housing_machined_v0

## Files

- **Recipe:** `kb/recipes/recipe_pump_housing_machined_v0.yaml`
- **Target item:** `pump_housing_machined`
  - File: `kb/items/pump_housing_machined.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'machining_raw_to_machined_part_v0') requires input 'cut_parts' which is not available

**Location:** Step 0
**Process:** `machining_raw_to_machined_part_v0`
  - File: `kb/processes/machining_raw_to_machined_part_v0.yaml`

**Current step:**
```yaml
- process_id: machining_raw_to_machined_part_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'pump_housing_machining_v0') requires input 'cutting_fluid' which is not available

**Location:** Step 1
**Process:** `pump_housing_machining_v0`
  - File: `kb/processes/pump_housing_machining_v0.yaml`

**Current step:**
```yaml
- process_id: pump_housing_machining_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_pump_housing_machined_v0.yaml`
- **BOM available:** No
