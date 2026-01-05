# Fix Intelligence: recipe_machine_chemical_separation_equipment_v0

## Files

- **Recipe:** `kb/recipes/recipe_machine_chemical_separation_equipment_v0.yaml`
- **Target item:** `chemical_separation_equipment`
  - File: `kb/items/chemical_separation_equipment.yaml`
- **BOM:** None
- **Steps:** 6 total

## Errors (6 found)

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

**Message:** Step 1 uses template process 'welded_fabrication_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
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

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'plumbing_and_pneumatics_v0') requires input 'piping_components' which is not available

**Location:** Step 2
**Process:** `plumbing_and_pneumatics_v0`
  - File: `kb/processes/plumbing_and_pneumatics_v0.yaml`

**Current step:**
```yaml
- process_id: plumbing_and_pneumatics_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'heating_element_installation_v0') requires input 'heating_element_resistive' which is not available

**Location:** Step 3
**Process:** `heating_element_installation_v0`
  - File: `kb/processes/heating_element_installation_v0.yaml`

**Current step:**
```yaml
- process_id: heating_element_installation_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

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

- Step 0 produces: `cut_parts` (9.5 kg)
- Step 1 produces: `welded_fabrications` (1.0 kg)
- Step 2 produces: `plumbing_system_assembly` (1.0 unit)
- Step 3 produces: `furnace_chamber_equipped` (1.0 unit)

---

### Error 6: recipe_template_missing_step_inputs

**Message:** Step 5 uses template process 'integration_test_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 5
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
- Step 1 produces: `welded_fabrications` (1.0 kg)
- Step 2 produces: `plumbing_system_assembly` (1.0 unit)
- Step 3 produces: `furnace_chamber_equipped` (1.0 unit)
- Step 4 produces: `wired_electrical_system` (1.0 unit)

---

## Summary

- **Total errors:** 6
- **Recipe file:** `kb/recipes/recipe_machine_chemical_separation_equipment_v0.yaml`
- **BOM available:** No
