# Fix Intelligence: recipe_neims_control_system_v0

## Files

- **Recipe:** `kb/recipes/recipe_neims_control_system_v0.yaml`
- **Target item:** `neims_control_system_v0`
  - File: `kb/items/neims_control_system_v0.yaml`
- **BOM:** None
- **Steps:** 5 total

## Errors (4 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'formation_control_unit_assembly_v0') requires input 'raw_formation_control_material_v0' which is not available

**Location:** Step 0
**Process:** `formation_control_unit_assembly_v0`
  - File: `kb/processes/formation_control_unit_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: formation_control_unit_assembly_v0
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

**Message:** Step 3 uses template process 'wiring_and_electronics_integration_v0' but doesn't provide step-level input overrides

**Location:** Step 3
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

- Step 0 produces: `formation_control_unit` (1.0 kg)
- Step 1 produces: `assembled_electronics` (1.0 unit)
- Step 2 produces: `programmed_microcontroller` (1.0 unit)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_neims_control_system_v0.yaml`
- **BOM available:** No
