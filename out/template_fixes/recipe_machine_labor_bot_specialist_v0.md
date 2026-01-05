# Fix Intelligence: recipe_machine_labor_bot_specialist_v0

## Files

- **Recipe:** `kb/recipes/recipe_machine_labor_bot_specialist_v0.yaml`
- **Target item:** `labor_bot_specialist_v0`
  - File: `kb/items/labor_bot_specialist_v0.yaml`
- **BOM:** `kb/boms/bom_labor_bot_specialist_v0.yaml` ✓
  - Components: 6
- **Steps:** 1 total

## Errors (1 found)

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

BOM has 6 components:

- `support_frame_welded` (qty: 1 None)
- `drive_motor_medium` (qty: 1 None)
- `bearing_set_heavy` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)
- `power_conditioning_module` (qty: 1 None)
- `control_compute_module_imported` (qty: 1 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: support_frame_welded
    qty: 1
    unit: None
  - item_id: drive_motor_medium
    qty: 1
    unit: None
  - item_id: bearing_set_heavy
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
  - item_id: power_conditioning_module
    qty: 1
    unit: None
  - item_id: control_compute_module_imported
    qty: 1
    unit: None
```

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_machine_labor_bot_specialist_v0.yaml`
- **BOM available:** Yes (6 components)
