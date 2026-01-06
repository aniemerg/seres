# Fix Intelligence: recipe_tank_shell_spun_v0

## Files

- **Recipe:** `kb/recipes/recipe_tank_shell_spun_v0.yaml`
- **Target item:** `tank_shell_spun`
  - File: `kb/items/tank_shell_spun.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_spinning_process_v0') requires input 'stainless_steel_sheet' which is not available

**Location:** Step 0
**Process:** `metal_spinning_process_v0`
  - File: `kb/processes/metal_spinning_process_v0.yaml`

**Current step:**
```yaml
- process_id: metal_spinning_process_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_tank_shell_spun_v0.yaml`
- **BOM available:** No
