# Fix Intelligence: recipe_logic_gate_vacuum_tube_v0

## Files

- **Recipe:** `kb/recipes/recipe_logic_gate_vacuum_tube_v0.yaml`
- **Target item:** `logic_gate_vacuum_tube_v0`
  - File: `kb/items/logic_gate_vacuum_tube_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'logic_gate_vacuum_tube_production_v0') requires input 'vacuum_tube_assembled_evacuated' which is not available

**Location:** Step 0
**Process:** `logic_gate_vacuum_tube_production_v0`
  - File: `kb/processes/logic_gate_vacuum_tube_production_v0.yaml`

**Current step:**
```yaml
- process_id: logic_gate_vacuum_tube_production_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_logic_gate_vacuum_tube_v0.yaml`
- **BOM available:** No
