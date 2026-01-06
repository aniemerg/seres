# Fix Intelligence: recipe_hydraulic_pump_unit_v0

## Files

- **Recipe:** `kb/recipes/recipe_hydraulic_pump_unit_v0.yaml`
- **Target item:** `hydraulic_pump_unit_v0`
  - File: `kb/items/hydraulic_pump_unit_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'hydraulic_pump_unit_assembly_v0') requires input 'hydraulic_pump_basic' which is not available

**Location:** Step 0
**Process:** `hydraulic_pump_unit_assembly_v0`
  - File: `kb/processes/hydraulic_pump_unit_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: hydraulic_pump_unit_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_hydraulic_pump_unit_v0.yaml`
- **BOM available:** No
