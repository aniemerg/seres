# Fix Intelligence: recipe_core_memory_controller_v0

## Files

- **Recipe:** `kb/recipes/recipe_core_memory_controller_v0.yaml`
- **Target item:** `core_memory_controller_v0`
  - File: `kb/items/core_memory_controller_v0.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'pcb_fabrication_process_v0') requires input 'copper_clad_laminate' which is not available

**Location:** Step 0
**Process:** `pcb_fabrication_process_v0`
  - File: `kb/processes/pcb_fabrication_process_v0.yaml`

**Current step:**
```yaml
- process_id: pcb_fabrication_process_v0
  inputs:
  - item_id: copper_clad_laminate
    qty: 0.05
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `copper_clad_laminate` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'reflow_soldering_process_v0') requires input 'pcb_bare_board' which is not available

**Location:** Step 1
**Process:** `reflow_soldering_process_v0`
  - File: `kb/processes/reflow_soldering_process_v0.yaml`

**Current step:**
```yaml
- process_id: reflow_soldering_process_v0
  inputs:
  - item_id: pcb_bare_board
    qty: 0.04
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `pcb_bare_board` not found

This item doesn't exist in the KB.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'firmware_programming_v0') requires input 'compiled_firmware_binary' which is not available

**Location:** Step 2
**Process:** `firmware_programming_v0`
  - File: `kb/processes/firmware_programming_v0.yaml`

**Current step:**
```yaml
- process_id: firmware_programming_v0
  inputs:
  - item_id: pcb_assembled_board
    qty: 0.038
    unit: kg
  - item_id: compiled_firmware_binary
    qty: 1.0
    unit: unit
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `pcb_assembled_board` not found

This item doesn't exist in the KB.

#### Problem: Item `compiled_firmware_binary` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_core_memory_controller_v0.yaml`
- **BOM available:** No
