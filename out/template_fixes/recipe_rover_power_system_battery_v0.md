# Fix Intelligence: recipe_rover_power_system_battery_v0

## Files

- **Recipe:** `kb/recipes/recipe_rover_power_system_battery_v0.yaml`
- **Target item:** `rover_power_system_battery_v0`
  - File: `kb/items/rover_power_system_battery_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'battery_pack_assembly_nife') requires input 'nife_battery_cell' which is not available

**Location:** Step 0
**Process:** `battery_pack_assembly_nife`
  - File: `kb/processes/battery_pack_assembly_nife.yaml`

**Current step:**
```yaml
- process_id: battery_pack_assembly_nife
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_rover_power_system_battery_v0.yaml`
- **BOM available:** No
