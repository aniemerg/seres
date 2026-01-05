# Fix Intelligence: recipe_valve_set_gas_handling_v0

## Files

- **Recipe:** `kb/recipes/recipe_valve_set_gas_handling_v0.yaml`
- **Target item:** `valve_set_gas_handling`
  - File: `kb/items/valve_set_gas_handling.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'valve_set_gas_handling_assembly_v0') requires input 'valve_body_machined' which is not available

**Location:** Step 0
**Process:** `valve_set_gas_handling_assembly_v0`
  - File: `kb/processes/valve_set_gas_handling_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: valve_set_gas_handling_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_valve_set_gas_handling_v0.yaml`
- **BOM available:** No
