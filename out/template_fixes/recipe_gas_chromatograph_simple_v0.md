# Fix Intelligence: recipe_gas_chromatograph_simple_v0

## Files

- **Recipe:** `kb/recipes/recipe_gas_chromatograph_simple_v0.yaml`
- **Target item:** `gas_chromatograph_simple_v0`
  - File: `kb/items/gas_chromatograph_simple_v0.yaml`
- **BOM:** `kb/boms/bom_gas_chromatograph_simple_v0.yaml` ✓
  - Components: 4
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

BOM has 4 components:

- `enclosure_small` (qty: 1 unit)
- `control_panel_basic` (qty: 1 unit)
- `pressure_gauge_set` (qty: 1 unit)
- `sensor_suite_general` (qty: 1 unit)

Suggested fix:
```yaml
- process_id: cutting_basic_v0
  inputs:
  - item_id: enclosure_small
    qty: 1
    unit: unit
  - item_id: control_panel_basic
    qty: 1
    unit: unit
  - item_id: pressure_gauge_set
    qty: 1
    unit: unit
  - item_id: sensor_suite_general
    qty: 1
    unit: unit
```

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

#### Option A: Use BOM components

BOM has 4 components:

- `enclosure_small` (qty: 1 unit)
- `control_panel_basic` (qty: 1 unit)
- `pressure_gauge_set` (qty: 1 unit)
- `sensor_suite_general` (qty: 1 unit)

Suggested fix:
```yaml
- process_id: welded_fabrication_basic_v0
  inputs:
  - item_id: enclosure_small
    qty: 1
    unit: unit
  - item_id: control_panel_basic
    qty: 1
    unit: unit
  - item_id: pressure_gauge_set
    qty: 1
    unit: unit
  - item_id: sensor_suite_general
    qty: 1
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `cut_parts` (9.5 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'enclosure_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `enclosure_assembly_basic_v0`
  - File: `kb/processes/enclosure_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: enclosure_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 4 components:

- `enclosure_small` (qty: 1 unit)
- `control_panel_basic` (qty: 1 unit)
- `pressure_gauge_set` (qty: 1 unit)
- `sensor_suite_general` (qty: 1 unit)

Suggested fix:
```yaml
- process_id: enclosure_assembly_basic_v0
  inputs:
  - item_id: enclosure_small
    qty: 1
    unit: unit
  - item_id: control_panel_basic
    qty: 1
    unit: unit
  - item_id: pressure_gauge_set
    qty: 1
    unit: unit
  - item_id: sensor_suite_general
    qty: 1
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `cut_parts` (9.5 kg)
- Step 1 produces: `welded_fabrications` (1.0 kg)

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'electrical_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
**Process:** `electrical_assembly_basic_v0`
  - File: `kb/processes/electrical_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: electrical_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 4 components:

- `enclosure_small` (qty: 1 unit)
- `control_panel_basic` (qty: 1 unit)
- `pressure_gauge_set` (qty: 1 unit)
- `sensor_suite_general` (qty: 1 unit)

Suggested fix:
```yaml
- process_id: electrical_assembly_basic_v0
  inputs:
  - item_id: enclosure_small
    qty: 1
    unit: unit
  - item_id: control_panel_basic
    qty: 1
    unit: unit
  - item_id: pressure_gauge_set
    qty: 1
    unit: unit
  - item_id: sensor_suite_general
    qty: 1
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `cut_parts` (9.5 kg)
- Step 1 produces: `welded_fabrications` (1.0 kg)
- Step 2 produces: `enclosure_electrical_medium` (1.0 kg)

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 4 components:

- `enclosure_small` (qty: 1 unit)
- `control_panel_basic` (qty: 1 unit)
- `pressure_gauge_set` (qty: 1 unit)
- `sensor_suite_general` (qty: 1 unit)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: enclosure_small
    qty: 1
    unit: unit
  - item_id: control_panel_basic
    qty: 1
    unit: unit
  - item_id: pressure_gauge_set
    qty: 1
    unit: unit
  - item_id: sensor_suite_general
    qty: 1
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `cut_parts` (9.5 kg)
- Step 1 produces: `welded_fabrications` (1.0 kg)
- Step 2 produces: `enclosure_electrical_medium` (1.0 kg)

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

BOM has 4 components:

- `enclosure_small` (qty: 1 unit)
- `control_panel_basic` (qty: 1 unit)
- `pressure_gauge_set` (qty: 1 unit)
- `sensor_suite_general` (qty: 1 unit)

Suggested fix:
```yaml
- process_id: integration_test_basic_v0
  inputs:
  - item_id: enclosure_small
    qty: 1
    unit: unit
  - item_id: control_panel_basic
    qty: 1
    unit: unit
  - item_id: pressure_gauge_set
    qty: 1
    unit: unit
  - item_id: sensor_suite_general
    qty: 1
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `cut_parts` (9.5 kg)
- Step 1 produces: `welded_fabrications` (1.0 kg)
- Step 2 produces: `enclosure_electrical_medium` (1.0 kg)
- Step 4 produces: `assembled_equipment` (1.0 kg)

---

## Summary

- **Total errors:** 6
- **Recipe file:** `kb/recipes/recipe_gas_chromatograph_simple_v0.yaml`
- **BOM available:** Yes (4 components)
