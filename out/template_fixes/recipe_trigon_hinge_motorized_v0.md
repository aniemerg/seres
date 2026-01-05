# Fix Intelligence: recipe_trigon_hinge_motorized_v0

## Files

- **Recipe:** `kb/recipes/recipe_trigon_hinge_motorized_v0.yaml`
- **Target item:** `trigon_hinge_motorized_v0`
  - File: `kb/items/trigon_hinge_motorized_v0.yaml`
- **BOM:** None
- **Steps:** 6 total

## Errors (6 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'motor_assembly_3d_printed_v0') requires input 'sma_motor_components' which is not available

**Location:** Step 1
**Process:** `motor_assembly_3d_printed_v0`
  - File: `kb/processes/motor_assembly_3d_printed_v0.yaml`

**Current step:**
```yaml
- process_id: motor_assembly_3d_printed_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'electrical_wiring_and_controls_v0') requires input 'electrical_wire_and_connectors' which is not available

**Location:** Step 2
**Process:** `electrical_wiring_and_controls_v0`
  - File: `kb/processes/electrical_wiring_and_controls_v0.yaml`

**Current step:**
```yaml
- process_id: electrical_wiring_and_controls_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'electronic_assembly_v0') requires input 'pcb_populated' which is not available

**Location:** Step 3
**Process:** `electronic_assembly_v0`
  - File: `kb/processes/electronic_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: electronic_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'finishing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
**Process:** `finishing_basic_v0`
  - File: `kb/processes/finishing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: finishing_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)
- Step 1 produces: `3d_printed_motor_ironpla_v0` (1.0 unit)
- Step 2 produces: `wired_electrical_system` (1.0 unit)
- Step 3 produces: `electronic_assembly` (1.0 unit)

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

- Step 0 produces: `assembled_equipment` (1.0 kg)
- Step 1 produces: `3d_printed_motor_ironpla_v0` (1.0 unit)
- Step 2 produces: `wired_electrical_system` (1.0 unit)
- Step 3 produces: `electronic_assembly` (1.0 unit)
- Step 4 produces: `finished_part` (1.0 unit)

---

## Summary

- **Total errors:** 6
- **Recipe file:** `kb/recipes/recipe_trigon_hinge_motorized_v0.yaml`
- **BOM available:** No
