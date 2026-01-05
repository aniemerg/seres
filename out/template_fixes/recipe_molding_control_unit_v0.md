# Fix Intelligence: recipe_molding_control_unit_v0

## Files

- **Recipe:** `kb/recipes/recipe_molding_control_unit_v0.yaml`
- **Target item:** `molding_control_unit`
  - File: `kb/items/molding_control_unit.yaml`
- **BOM:** None
- **Steps:** 6 total

## Errors (6 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'sheet_metal_fabrication_v0') requires input 'sheet_metal_or_structural_steel' which is not available

**Location:** Step 0
**Process:** `sheet_metal_fabrication_v0`
  - File: `kb/processes/sheet_metal_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: sheet_metal_fabrication_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'electronics_assembly_v0') requires input 'pcb_populated' which is not available

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

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'wiring_and_electronics_integration_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `wiring_and_electronics_integration_v0`
  - File: `kb/processes/wiring_and_electronics_integration_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: wiring_and_electronics_integration_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `formed_sheet_metal_parts` (9.5 kg)
- Step 1 produces: `assembled_electronics` (1.0 unit)

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'firmware_programming_v0') requires input 'microcontroller_or_embedded_board' which is not available

**Location:** Step 3
**Process:** `firmware_programming_v0`
  - File: `kb/processes/firmware_programming_v0.yaml`

**Current step:**
```yaml
- process_id: firmware_programming_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'electrical_testing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
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

- Step 0 produces: `formed_sheet_metal_parts` (9.5 kg)
- Step 1 produces: `assembled_electronics` (1.0 unit)
- Step 2 produces: `wired_electrical_system` (1.0 unit)
- Step 3 produces: `programmed_microcontroller` (1.0 unit)

---

### Error 6: recipe_template_missing_step_inputs

**Message:** Step 5 uses template process 'inspection_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 5
**Process:** `inspection_basic_v0`
  - File: `kb/processes/inspection_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: inspection_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `formed_sheet_metal_parts` (9.5 kg)
- Step 1 produces: `assembled_electronics` (1.0 unit)
- Step 2 produces: `wired_electrical_system` (1.0 unit)
- Step 3 produces: `programmed_microcontroller` (1.0 unit)
- Step 4 produces: `tested_electrical_equipment` (1.0 unit)

---

## Summary

- **Total errors:** 6
- **Recipe file:** `kb/recipes/recipe_molding_control_unit_v0.yaml`
- **BOM available:** No
