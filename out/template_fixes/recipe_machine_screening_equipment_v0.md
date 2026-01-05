# Fix Intelligence: recipe_machine_screening_equipment_v0

## Files

- **Recipe:** `kb/recipes/recipe_machine_screening_equipment_v0.yaml`
- **Target item:** `screening_equipment`
  - File: `kb/items/screening_equipment.yaml`
- **BOM:** None
- **Steps:** 6 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_screening_equipment_v0` → screening_equipment_v0 (6 steps)

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

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'welding_and_fabrication_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `welding_and_fabrication_v0`
  - File: `kb/processes/welding_and_fabrication_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: welding_and_fabrication_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `formed_sheet_metal_parts` (9.5 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
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

- Step 0 produces: `formed_sheet_metal_parts` (9.5 kg)
- Step 1 produces: `welded_fabrications` (9.5 kg)

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

- Step 0 produces: `formed_sheet_metal_parts` (9.5 kg)
- Step 1 produces: `welded_fabrications` (9.5 kg)
- Step 2 produces: `assembled_equipment` (1.0 kg)

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'integration_test_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
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

- Step 0 produces: `formed_sheet_metal_parts` (9.5 kg)
- Step 1 produces: `welded_fabrications` (9.5 kg)
- Step 2 produces: `assembled_equipment` (1.0 kg)
- Step 3 produces: `wired_electrical_system` (1.0 unit)

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
- Step 1 produces: `welded_fabrications` (9.5 kg)
- Step 2 produces: `assembled_equipment` (1.0 kg)
- Step 3 produces: `wired_electrical_system` (1.0 unit)
- Step 4 produces: `assembled_electronics` (1.0 kg)

---

## Summary

- **Total errors:** 6
- **Recipe file:** `kb/recipes/recipe_machine_screening_equipment_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
