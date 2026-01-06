# Fix Intelligence: recipe_coolant_pump_system_v0

## Files

- **Recipe:** `kb/recipes/recipe_coolant_pump_system_v0.yaml`
- **Target item:** `coolant_pump_system`
  - File: `kb/items/coolant_pump_system.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'machining_to_coolant_pump_v0') requires input 'cut_parts' which is not available

**Location:** Step 0
**Process:** `machining_to_coolant_pump_v0`
  - File: `kb/processes/machining_to_coolant_pump_v0.yaml`

**Current step:**
```yaml
- process_id: machining_to_coolant_pump_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_coolant_pump_system_v0.yaml`
- **BOM available:** No
