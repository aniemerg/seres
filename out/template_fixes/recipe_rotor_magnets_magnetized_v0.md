# Fix Intelligence: recipe_rotor_magnets_magnetized_v0

## Files

- **Recipe:** `kb/recipes/recipe_rotor_magnets_magnetized_v0.yaml`
- **Target item:** `rotor_magnets_magnetized`
  - File: `kb/items/rotor_magnets_magnetized.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'magnet_magnetization_process_v0') requires input 'permanent_magnet_neodymium' which is not available

**Location:** Step 0
**Process:** `magnet_magnetization_process_v0`
  - File: `kb/processes/magnet_magnetization_process_v0.yaml`

**Current step:**
```yaml
- process_id: magnet_magnetization_process_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_rotor_magnets_magnetized_v0.yaml`
- **BOM available:** No
