# Fix Intelligence: recipe_current_sensing_circuit_v0

## Files

- **Recipe:** `kb/recipes/recipe_current_sensing_circuit_v0.yaml`
- **Target item:** `current_sensing_circuit`
  - File: `kb/items/current_sensing_circuit.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (4 found)

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

**Message:** Step 2 (process 'electronics_assembly_v0') requires input 'pcb_populated' which is not available

**Location:** Step 2
**Process:** `electronics_assembly_v0`
  - File: `kb/processes/electronics_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: electronics_assembly_v0
  inputs:
  - item_id: pcb_populated
    qty: 1.0
    unit: unit
  - item_id: electronic_components_set
    qty: 1.0
    unit: unit
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `pcb_populated` not found

This item doesn't exist in the KB.

#### Problem: Item `electronic_components_set` not found

This item doesn't exist in the KB.

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `bare_pcb` (1.0 unit)
- Step 1 produces: `pcb_populated` (1.0 unit)
- Step 2 produces: `pcb_components_placed` (0.15 kg)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_current_sensing_circuit_v0.yaml`
- **BOM available:** No
