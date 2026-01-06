# Fix Intelligence: recipe_ratslam_hardware_implementation_v0

## Files

- **Recipe:** `kb/recipes/recipe_ratslam_hardware_implementation_v0.yaml`
- **Target item:** `ratslam_hardware_implementation_v0`
  - File: `kb/items/ratslam_hardware_implementation_v0.yaml`
- **BOM:** `kb/boms/bom_ratslam_hardware_implementation_v0.yaml` ✓
  - Components: 4
- **Steps:** 2 total

## Errors (2 found)

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

#### Option A: Use BOM components

BOM has 4 components:

- `computer_core_imported` (qty: 1 None)
- `electronic_components_set` (qty: 1 None)
- `enclosure_electrical_medium` (qty: 1 None)
- `steel_ingot` (qty: 1.0 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: computer_core_imported
    qty: 1
    unit: None
  - item_id: electronic_components_set
    qty: 1
    unit: None
  - item_id: enclosure_electrical_medium
    qty: 1
    unit: None
  - item_id: steel_ingot
    qty: 1.0
    unit: None
```

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'electrical_testing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `electrical_testing_basic_v0`
  - File: `kb/processes/electrical_testing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: electrical_testing_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 4 components:

- `computer_core_imported` (qty: 1 None)
- `electronic_components_set` (qty: 1 None)
- `enclosure_electrical_medium` (qty: 1 None)
- `steel_ingot` (qty: 1.0 None)

Suggested fix:
```yaml
- process_id: electrical_testing_basic_v0
  inputs:
  - item_id: computer_core_imported
    qty: 1
    unit: None
  - item_id: electronic_components_set
    qty: 1
    unit: None
  - item_id: enclosure_electrical_medium
    qty: 1
    unit: None
  - item_id: steel_ingot
    qty: 1.0
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_ratslam_hardware_implementation_v0.yaml`
- **BOM available:** Yes (4 components)
