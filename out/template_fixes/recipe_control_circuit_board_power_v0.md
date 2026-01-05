# Fix Intelligence: recipe_control_circuit_board_power_v0

## Files

- **Recipe:** `kb/recipes/recipe_control_circuit_board_power_v0.yaml`
- **Target item:** `control_circuit_board_power`
  - File: `kb/items/control_circuit_board_power.yaml`
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
  inputs:
  - item_id: copper_clad_laminate
    qty: 0.25
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `copper_clad_laminate` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'electronics_assembly_v0') requires input 'pcb_substrate_v0' which is not available

**Location:** Step 1
**Process:** `electronics_assembly_v0`
  - File: `kb/processes/electronics_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: electronics_assembly_v0
  inputs:
  - item_id: pcb_substrate_v0
    qty: 0.25
    unit: kg
  - item_id: electronic_components_set
    qty: 1.0
    unit: unit
  - item_id: solder_paste_tin_lead
    qty: 0.05
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `pcb_substrate_v0` not found

This item doesn't exist in the KB.

#### Problem: Item `electronic_components_set` not found

This item doesn't exist in the KB.

#### Problem: Item `solder_paste_tin_lead` not found

This item doesn't exist in the KB.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'firmware_programming_v0') requires input 'microcontroller_or_embedded_board' which is not available

**Location:** Step 2
**Process:** `firmware_programming_v0`
  - File: `kb/processes/firmware_programming_v0.yaml`

**Current step:**
```yaml
- process_id: firmware_programming_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'electrical_testing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
**Process:** `electrical_testing_basic_v0`
  - File: `kb/processes/electrical_testing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: electrical_testing_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `pcb_substrate_v0` (0.25 kg)
- Step 1 produces: `control_circuit_board_power` (1.0 unit)
- Step 2 produces: `programmed_microcontroller` (1.0 unit)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_control_circuit_board_power_v0.yaml`
- **BOM available:** No
