# Fix Intelligence: recipe_power_cable_assembly_v0

## Files

- **Recipe:** `kb/recipes/recipe_power_cable_assembly_v0.yaml`
- **Target item:** `power_cable_assembly`
  - File: `kb/items/power_cable_assembly.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'power_cable_assembly_v0') requires input 'electrical_wire_and_connectors' which is not available

**Location:** Step 0
**Process:** `power_cable_assembly_v0`
  - File: `kb/processes/power_cable_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: power_cable_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_power_cable_assembly_v0.yaml`
- **BOM available:** No
