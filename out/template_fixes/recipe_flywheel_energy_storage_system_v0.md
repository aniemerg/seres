# Fix Intelligence: recipe_flywheel_energy_storage_system_v0

## Files

- **Recipe:** `kb/recipes/recipe_flywheel_energy_storage_system_v0.yaml`
- **Target item:** `flywheel_energy_storage_system_v0`
  - File: `kb/items/flywheel_energy_storage_system_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'flywheel_energy_storage_system_assembly_v0') requires input 'flywheel_rotor_composite_v0' which is not available

**Location:** Step 0
**Process:** `flywheel_energy_storage_system_assembly_v0`
  - File: `kb/processes/flywheel_energy_storage_system_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: flywheel_energy_storage_system_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_flywheel_energy_storage_system_v0.yaml`
- **BOM available:** No
