# Fix Intelligence: recipe_core_memory_sense_amplifier_v0

## Files

- **Recipe:** `kb/recipes/recipe_core_memory_sense_amplifier_v0.yaml`
- **Target item:** `core_memory_sense_amplifier_v0`
  - File: `kb/items/core_memory_sense_amplifier_v0.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

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

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'alignment_and_testing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `alignment_and_testing_basic_v0`
  - File: `kb/processes/alignment_and_testing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: alignment_and_testing_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `circuit_board_v0` (1.0 unit)

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_core_memory_sense_amplifier_v0.yaml`
- **BOM available:** No
