# Fix Intelligence: recipe_tactile_sensor_silicone_v0

## Files

- **Recipe:** `kb/recipes/recipe_tactile_sensor_silicone_v0.yaml`
- **Target item:** `tactile_sensor_silicone_v0`
  - File: `kb/items/tactile_sensor_silicone_v0.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'silicone_polymer_synthesis_v0') requires input 'silicone_precursor' which is not available

**Location:** Step 0
**Process:** `silicone_polymer_synthesis_v0`
  - File: `kb/processes/silicone_polymer_synthesis_v0.yaml`

**Current step:**
```yaml
- process_id: silicone_polymer_synthesis_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'silicone_rubber_vulcanization_v0') requires input 'silicone_curing_agent' which is not available

**Location:** Step 1
**Process:** `silicone_rubber_vulcanization_v0`
  - File: `kb/processes/silicone_rubber_vulcanization_v0.yaml`

**Current step:**
```yaml
- process_id: silicone_rubber_vulcanization_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_tactile_sensor_silicone_v0.yaml`
- **BOM available:** No
