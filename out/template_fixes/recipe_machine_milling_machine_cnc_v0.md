# Fix Intelligence: recipe_machine_milling_machine_cnc_v0

## Files

- **Recipe:** `kb/recipes/recipe_machine_milling_machine_cnc_v0.yaml`
- **Target item:** `milling_machine_cnc`
  - File: `kb/items/milling_machine_cnc.yaml`
- **BOM:** None
- **Steps:** 9 total

## Errors (9 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'casting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `casting_basic_v0`
  - File: `kb/processes/casting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: casting_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'machining_precision_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `machining_precision_v0`
  - File: `kb/processes/machining_precision_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_precision_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'welding_structural_v0') requires input 'cut_parts' which is not available

**Location:** Step 2
**Process:** `welding_structural_v0`
  - File: `kb/processes/welding_structural_v0.yaml`

**Current step:**
```yaml
- process_id: welding_structural_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

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

- Step 1 produces: `machined_steel_part_precision` (7.0 kg)
- Step 2 produces: `welded_fabrications` (1.05 kg)

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'wiring_and_electronics_integration_v0' but doesn't provide step-level input overrides

**Location:** Step 4
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

- Step 1 produces: `machined_steel_part_precision` (7.0 kg)
- Step 2 produces: `welded_fabrications` (1.05 kg)
- Step 3 produces: `assembled_equipment` (1.0 kg)

---

### Error 6: recipe_step_input_not_satisfied

**Message:** Step 5 (process 'precision_alignment_and_leveling_v0') requires input 'machine_frame_small' which is not available

**Location:** Step 5
**Process:** `precision_alignment_and_leveling_v0`
  - File: `kb/processes/precision_alignment_and_leveling_v0.yaml`

**Current step:**
```yaml
- process_id: precision_alignment_and_leveling_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 7: recipe_template_missing_step_inputs

**Message:** Step 6 uses template process 'integration_test_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 6
**Process:** `integration_test_basic_v0`
  - File: `kb/processes/integration_test_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: integration_test_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 1 produces: `machined_steel_part_precision` (7.0 kg)
- Step 2 produces: `welded_fabrications` (1.05 kg)
- Step 3 produces: `assembled_equipment` (1.0 kg)
- Step 4 produces: `wired_electrical_system` (1.0 unit)
- Step 5 produces: `machine_frame_small` (1.0 kg)

---

### Error 8: recipe_template_missing_step_inputs

**Message:** Step 7 uses template process 'calibration_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 7
**Process:** `calibration_basic_v0`
  - File: `kb/processes/calibration_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: calibration_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 1 produces: `machined_steel_part_precision` (7.0 kg)
- Step 2 produces: `welded_fabrications` (1.05 kg)
- Step 3 produces: `assembled_equipment` (1.0 kg)
- Step 4 produces: `wired_electrical_system` (1.0 unit)
- Step 5 produces: `machine_frame_small` (1.0 kg)
- Step 6 produces: `assembled_electronics` (1.0 kg)

---

### Error 9: recipe_template_missing_step_inputs

**Message:** Step 8 uses template process 'inspection_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 8
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

- Step 1 produces: `machined_steel_part_precision` (7.0 kg)
- Step 2 produces: `welded_fabrications` (1.05 kg)
- Step 3 produces: `assembled_equipment` (1.0 kg)
- Step 4 produces: `wired_electrical_system` (1.0 unit)
- Step 5 produces: `machine_frame_small` (1.0 kg)
- Step 6 produces: `assembled_electronics` (1.0 kg)
- Step 7 produces: `instrument_calibrated` (1.0 unit)

---

## Summary

- **Total errors:** 9
- **Recipe file:** `kb/recipes/recipe_machine_milling_machine_cnc_v0.yaml`
- **BOM available:** No
