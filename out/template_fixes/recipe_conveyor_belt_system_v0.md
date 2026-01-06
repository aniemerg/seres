# Fix Intelligence: recipe_conveyor_belt_system_v0

## Files

- **Recipe:** `kb/recipes/recipe_conveyor_belt_system_v0.yaml`
- **Target item:** `conveyor_belt_system_v0`
  - File: `kb/items/conveyor_belt_system_v0.yaml`
- **BOM:** `kb/boms/bom_conveyor_belt_system_v0.yaml` ✓
  - Components: 3
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

BOM has 3 components:

- `conveyor_belt_small` (qty: 1.0 None)
- `conveyor_drive_unit` (qty: 1.0 None)
- `conveyor_idler_set` (qty: 1.0 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: conveyor_belt_small
    qty: 1.0
    unit: None
  - item_id: conveyor_drive_unit
    qty: 1.0
    unit: None
  - item_id: conveyor_idler_set
    qty: 1.0
    unit: None
```

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'integration_test_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
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

BOM has 3 components:

- `conveyor_belt_small` (qty: 1.0 None)
- `conveyor_drive_unit` (qty: 1.0 None)
- `conveyor_idler_set` (qty: 1.0 None)

Suggested fix:
```yaml
- process_id: integration_test_basic_v0
  inputs:
  - item_id: conveyor_belt_small
    qty: 1.0
    unit: None
  - item_id: conveyor_drive_unit
    qty: 1.0
    unit: None
  - item_id: conveyor_idler_set
    qty: 1.0
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_conveyor_belt_system_v0.yaml`
- **BOM available:** Yes (3 components)
