# Fix Intelligence: recipe_vacuum_furnace_v0_v0

## Files

- **Recipe:** `kb/recipes/recipe_vacuum_furnace_v0_v0.yaml`
- **Target item:** `vacuum_furnace_v0`
  - File: `kb/items/vacuum_furnace_v0.yaml`
- **BOM:** None
- **Steps:** 9 total

## Errors (9 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'cutting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `cutting_basic_v0`
  - File: `kb/processes/cutting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: cutting_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'metal_forming_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `metal_forming_basic_v0`
  - File: `kb/processes/metal_forming_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: metal_forming_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `cut_parts` (9.5 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'welded_fabrication_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `welded_fabrication_basic_v0`
  - File: `kb/processes/welded_fabrication_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: welded_fabrication_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `cut_parts` (9.5 kg)
- Step 1 produces: `formed_metal_part` (0.95 kg)

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'machining_finish_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
**Process:** `machining_finish_basic_v0`
  - File: `kb/processes/machining_finish_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_finish_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `cut_parts` (9.5 kg)
- Step 1 produces: `formed_metal_part` (0.95 kg)
- Step 2 produces: `welded_fabrications` (1.0 kg)

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'enclosure_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
**Process:** `enclosure_assembly_basic_v0`
  - File: `kb/processes/enclosure_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: enclosure_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `cut_parts` (9.5 kg)
- Step 1 produces: `formed_metal_part` (0.95 kg)
- Step 2 produces: `welded_fabrications` (1.0 kg)
- Step 3 produces: `machined_part_raw` (1.0 kg)

---

### Error 6: recipe_step_input_not_satisfied

**Message:** Step 5 (process 'heating_element_installation_v0') requires input 'heating_element_resistive' which is not available

**Location:** Step 5
**Process:** `heating_element_installation_v0`
  - File: `kb/processes/heating_element_installation_v0.yaml`

**Current step:**
```yaml
- process_id: heating_element_installation_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 7: recipe_template_missing_step_inputs

**Message:** Step 6 uses template process 'lamination_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 6
**Process:** `lamination_basic_v0`
  - File: `kb/processes/lamination_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: lamination_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `cut_parts` (9.5 kg)
- Step 1 produces: `formed_metal_part` (0.95 kg)
- Step 2 produces: `welded_fabrications` (1.0 kg)
- Step 3 produces: `machined_part_raw` (1.0 kg)
- Step 4 produces: `enclosure_electrical_medium` (1.0 kg)
- Step 5 produces: `furnace_chamber_equipped` (1.0 unit)

---

### Error 8: recipe_template_missing_step_inputs

**Message:** Step 7 uses template process 'wiring_and_electronics_integration_v0' but doesn't provide step-level input overrides

**Location:** Step 7
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

- Step 0 produces: `cut_parts` (9.5 kg)
- Step 1 produces: `formed_metal_part` (0.95 kg)
- Step 2 produces: `welded_fabrications` (1.0 kg)
- Step 3 produces: `machined_part_raw` (1.0 kg)
- Step 4 produces: `enclosure_electrical_medium` (1.0 kg)
- Step 5 produces: `furnace_chamber_equipped` (1.0 unit)
- Step 6 produces: `copper_clad_laminate` (1.0 kg)

---

### Error 9: recipe_template_missing_step_inputs

**Message:** Step 8 uses template process 'integration_test_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 8
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

- Step 0 produces: `cut_parts` (9.5 kg)
- Step 1 produces: `formed_metal_part` (0.95 kg)
- Step 2 produces: `welded_fabrications` (1.0 kg)
- Step 3 produces: `machined_part_raw` (1.0 kg)
- Step 4 produces: `enclosure_electrical_medium` (1.0 kg)
- Step 5 produces: `furnace_chamber_equipped` (1.0 unit)
- Step 6 produces: `copper_clad_laminate` (1.0 kg)
- Step 7 produces: `wired_electrical_system` (1.0 unit)

---

## Summary

- **Total errors:** 9
- **Recipe file:** `kb/recipes/recipe_vacuum_furnace_v0_v0.yaml`
- **BOM available:** No
