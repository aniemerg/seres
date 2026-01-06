# Fix Intelligence: recipe_chemical_processing_unit_v0

## Files

- **Recipe:** `kb/recipes/recipe_chemical_processing_unit_v0.yaml`
- **Target item:** `chemical_processing_unit`
  - File: `kb/items/chemical_processing_unit.yaml`
- **BOM:** `kb/boms/bom_chemical_processing_unit.yaml` ✓
  - Components: 5
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'import_receiving_basic_v0') requires input 'bulk_material_or_parts' which is not available

**Location:** Step 0
**Process:** `import_receiving_basic_v0`
  - File: `kb/processes/import_receiving_basic_v0.yaml`

**Current step:**
```yaml
- process_id: import_receiving_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
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

BOM has 5 components:

- `machine_frame_medium` (qty: 1.0 None)
- `power_conditioning_module` (qty: 1.0 None)
- `control_panel_basic` (qty: 1.0 None)
- `sensor_suite_general` (qty: 1.0 None)
- `fastener_kit_medium` (qty: 1.0 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: machine_frame_medium
    qty: 1.0
    unit: None
  - item_id: power_conditioning_module
    qty: 1.0
    unit: None
  - item_id: control_panel_basic
    qty: 1.0
    unit: None
  - item_id: sensor_suite_general
    qty: 1.0
    unit: None
  - item_id: fastener_kit_medium
    qty: 1.0
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `bulk_material_or_parts` (1.0 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'inspection_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `inspection_basic_v0`
  - File: `kb/processes/inspection_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: inspection_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 5 components:

- `machine_frame_medium` (qty: 1.0 None)
- `power_conditioning_module` (qty: 1.0 None)
- `control_panel_basic` (qty: 1.0 None)
- `sensor_suite_general` (qty: 1.0 None)
- `fastener_kit_medium` (qty: 1.0 None)

Suggested fix:
```yaml
- process_id: inspection_basic_v0
  inputs:
  - item_id: machine_frame_medium
    qty: 1.0
    unit: None
  - item_id: power_conditioning_module
    qty: 1.0
    unit: None
  - item_id: control_panel_basic
    qty: 1.0
    unit: None
  - item_id: sensor_suite_general
    qty: 1.0
    unit: None
  - item_id: fastener_kit_medium
    qty: 1.0
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `bulk_material_or_parts` (1.0 kg)
- Step 1 produces: `assembled_equipment` (1.0 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_chemical_processing_unit_v0.yaml`
- **BOM available:** Yes (5 components)
