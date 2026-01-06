# Fix Intelligence: recipe_voltage_regulation_circuit_alias_v0

## Files

- **Recipe:** `kb/recipes/recipe_voltage_regulation_circuit_alias_v0.yaml`
- **Target item:** `voltage_regulation_circuit`
  - File: `kb/items/voltage_regulation_circuit.yaml`
- **BOM:** None
- **Steps:** 3 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_voltage_regulation_circuit_v0` → voltage_regulation_circuit_v0 (3 steps)

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'pcb_assembly_v0') requires input 'pcb_bare_board' which is not available

**Location:** Step 0
**Process:** `pcb_assembly_v0`
  - File: `kb/processes/pcb_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: pcb_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'electronics_assembly_v0') requires input 'electronic_components_set' which is not available

**Location:** Step 1
**Process:** `electronics_assembly_v0`
  - File: `kb/processes/electronics_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: electronics_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'voltage_regulation_circuit_assembly_v0') requires input 'voltage_regulator_switching_v0' which is not available

**Location:** Step 2
**Process:** `voltage_regulation_circuit_assembly_v0`
  - File: `kb/processes/voltage_regulation_circuit_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: voltage_regulation_circuit_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_voltage_regulation_circuit_alias_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
