# Fix Intelligence: recipe_tungsten_cathode_oxide_coated_v0

## Files

- **Recipe:** `kb/recipes/recipe_tungsten_cathode_oxide_coated_v0.yaml`
- **Target item:** `tungsten_cathode_oxide_coated_v0`
  - File: `kb/items/tungsten_cathode_oxide_coated_v0.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'tungsten_wire_drawing_v0') requires input 'tungsten_metal_pure' which is not available

**Location:** Step 0
**Process:** `tungsten_wire_drawing_v0`
  - File: `kb/processes/tungsten_wire_drawing_v0.yaml`

**Current step:**
```yaml
- process_id: tungsten_wire_drawing_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'tungsten_sintering_high_temp_v0') requires input 'tungsten_powder' which is not available

**Location:** Step 1
**Process:** `tungsten_sintering_high_temp_v0`
  - File: `kb/processes/tungsten_sintering_high_temp_v0.yaml`

**Current step:**
```yaml
- process_id: tungsten_sintering_high_temp_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'cathode_oxide_coating_process_v0') requires input 'nickel_sheet_rolling_v0' which is not available

**Location:** Step 2
**Process:** `cathode_oxide_coating_process_v0`
  - File: `kb/processes/cathode_oxide_coating_process_v0.yaml`

**Current step:**
```yaml
- process_id: cathode_oxide_coating_process_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_tungsten_cathode_oxide_coated_v0.yaml`
- **BOM available:** No
