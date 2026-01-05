# Fix Intelligence: recipe_blower_fan_small_v0

## Files

- **Recipe:** `kb/recipes/recipe_blower_fan_small_v0.yaml`
- **Target item:** `blower_fan_small`
  - File: `kb/items/blower_fan_small.yaml`
- **BOM:** None
- **Steps:** 6 total

## Errors (6 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'sheet_metal_forming_v0') requires input 'steel_plate_or_sheet' which is not available

**Location:** Step 0
**Process:** `sheet_metal_forming_v0`
  - File: `kb/processes/sheet_metal_forming_v0.yaml`

**Current step:**
```yaml
- process_id: sheet_metal_forming_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'machining_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `machining_basic_v0`
  - File: `kb/processes/machining_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `formed_sheet_metal_parts` (0.95 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'welding_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `welding_basic_v0`
  - File: `kb/processes/welding_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: welding_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `formed_sheet_metal_parts` (0.95 kg)
- Step 1 produces: `machined_metal_block_v0` (1.8 kg)

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

- Step 0 produces: `formed_sheet_metal_parts` (0.95 kg)
- Step 1 produces: `machined_metal_block_v0` (1.8 kg)
- Step 2 produces: `welded_assemblies` (1.0 kg)

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'balancing_dynamic_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
**Process:** `balancing_dynamic_basic_v0`
  - File: `kb/processes/balancing_dynamic_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: balancing_dynamic_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `formed_sheet_metal_parts` (0.95 kg)
- Step 1 produces: `machined_metal_block_v0` (1.8 kg)
- Step 2 produces: `welded_assemblies` (1.0 kg)
- Step 3 produces: `assembled_equipment` (1.0 kg)

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

- Step 0 produces: `formed_sheet_metal_parts` (0.95 kg)
- Step 1 produces: `machined_metal_block_v0` (1.8 kg)
- Step 2 produces: `welded_assemblies` (1.0 kg)
- Step 3 produces: `assembled_equipment` (1.0 kg)
- Step 4 produces: `machined_part_raw` (1.0 kg)

---

## Summary

- **Total errors:** 6
- **Recipe file:** `kb/recipes/recipe_blower_fan_small_v0.yaml`
- **BOM available:** No
