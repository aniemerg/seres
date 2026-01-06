# Fix Intelligence: recipe_braitenberg_vehicle_circuit_v0

## Files

- **Recipe:** `kb/recipes/recipe_braitenberg_vehicle_circuit_v0.yaml`
- **Target item:** `braitenberg_vehicle_circuit_v0`
  - File: `kb/items/braitenberg_vehicle_circuit_v0.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'circuit_board_assembly_v0') requires input 'pcb_substrate_v0' which is not available

**Location:** Step 0
**Process:** `circuit_board_assembly_v0`
  - File: `kb/processes/circuit_board_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: circuit_board_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_braitenberg_vehicle_circuit_v0.yaml`
- **BOM available:** No
