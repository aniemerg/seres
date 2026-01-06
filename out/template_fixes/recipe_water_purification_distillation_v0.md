# Fix Intelligence: recipe_water_purification_distillation_v0

## Files

- **Recipe:** `kb/recipes/recipe_water_purification_distillation_v0.yaml`
- **Target item:** `water_purification_distillation_v0`
  - File: `kb/items/water_purification_distillation_v0.yaml`
- **BOM:** `kb/boms/bom_water_purification_distillation_v0.yaml` ✓
  - Components: 1
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

#### Option A: Use BOM components

BOM has 1 components:

- `distillation_column_simple_v0` (qty: 1.0 unit)

Suggested fix:
```yaml
- process_id: cutting_basic_v0
  inputs:
  - item_id: distillation_column_simple_v0
    qty: 1.0
    unit: unit
```

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

#### Option A: Use BOM components

BOM has 1 components:

- `distillation_column_simple_v0` (qty: 1.0 unit)

Suggested fix:
```yaml
- process_id: metal_forming_basic_v0
  inputs:
  - item_id: distillation_column_simple_v0
    qty: 1.0
    unit: unit
```

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

#### Option A: Use BOM components

BOM has 1 components:

- `distillation_column_simple_v0` (qty: 1.0 unit)

Suggested fix:
```yaml
- process_id: welded_fabrication_basic_v0
  inputs:
  - item_id: distillation_column_simple_v0
    qty: 1.0
    unit: unit
```

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

#### Option A: Use BOM components

BOM has 1 components:

- `distillation_column_simple_v0` (qty: 1.0 unit)

Suggested fix:
```yaml
- process_id: machining_finish_basic_v0
  inputs:
  - item_id: distillation_column_simple_v0
    qty: 1.0
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `cut_parts` (9.5 kg)
- Step 1 produces: `formed_metal_part` (0.95 kg)
- Step 2 produces: `welded_fabrications` (1.0 kg)

---

### Error 5: recipe_step_input_not_satisfied

**Message:** Step 4 (process 'plumbing_and_pneumatics_v0') requires input 'piping_components' which is not available

**Location:** Step 4
**Process:** `plumbing_and_pneumatics_v0`
  - File: `kb/processes/plumbing_and_pneumatics_v0.yaml`

**Current step:**
```yaml
- process_id: plumbing_and_pneumatics_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

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

#### Option A: Use BOM components

BOM has 1 components:

- `distillation_column_simple_v0` (qty: 1.0 unit)

Suggested fix:
```yaml
- process_id: integration_test_basic_v0
  inputs:
  - item_id: distillation_column_simple_v0
    qty: 1.0
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `cut_parts` (9.5 kg)
- Step 1 produces: `formed_metal_part` (0.95 kg)
- Step 2 produces: `welded_fabrications` (1.0 kg)
- Step 3 produces: `machined_part_raw` (1.0 kg)
- Step 4 produces: `plumbing_system_assembly` (1.0 unit)

---

## Summary

- **Total errors:** 6
- **Recipe file:** `kb/recipes/recipe_water_purification_distillation_v0.yaml`
- **BOM available:** Yes (1 components)
