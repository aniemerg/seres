# Fix Intelligence: recipe_pcb_assembled_board_v0

## Files

- **Recipe:** `kb/recipes/recipe_pcb_assembled_board_v0.yaml`
- **Target item:** `pcb_assembled_board`
  - File: `kb/items/pcb_assembled_board.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'pcb_fabrication_v0') requires input 'copper_clad_laminate' which is not available

**Location:** Step 0
**Process:** `pcb_fabrication_v0`
  - File: `kb/processes/pcb_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: pcb_fabrication_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'pcb_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `pcb_assembly_basic_v0`
  - File: `kb/processes/pcb_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: pcb_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `bare_pcb` (1.0 unit)

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'reflow_soldering_process_v0') requires input 'pcb_components_placed' which is not available

**Location:** Step 2
**Process:** `reflow_soldering_process_v0`
  - File: `kb/processes/reflow_soldering_process_v0.yaml`

**Current step:**
```yaml
- process_id: reflow_soldering_process_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_pcb_assembled_board_v0.yaml`
- **BOM available:** No
