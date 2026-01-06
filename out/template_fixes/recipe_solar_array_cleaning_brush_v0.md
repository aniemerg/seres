# Fix Intelligence: recipe_solar_array_cleaning_brush_v0

## Files

- **Recipe:** `kb/recipes/recipe_solar_array_cleaning_brush_v0.yaml`
- **Target item:** `solar_array_cleaning_brush_v0`
  - File: `kb/items/solar_array_cleaning_brush_v0.yaml`
- **BOM:** `kb/boms/bom_solar_array_cleaning_brush_v0.yaml` ✓
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

- `wire_brush_set` (qty: 1 None)
- `drive_motor_small` (qty: 1 None)
- `support_frame_small` (qty: 1 None)
- `power_storage_pack` (qty: 1 None)
- `control_panel_basic` (qty: 1 None)
- `mounting_fixtures_adjustable` (qty: 1 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: wire_brush_set
    qty: 1
    unit: None
  - item_id: drive_motor_small
    qty: 1
    unit: None
  - item_id: support_frame_small
    qty: 1
    unit: None
  - item_id: power_storage_pack
    qty: 1
    unit: None
  - item_id: control_panel_basic
    qty: 1
    unit: None
  - item_id: mounting_fixtures_adjustable
    qty: 1
    unit: None
```

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_solar_array_cleaning_brush_v0.yaml`
- **BOM available:** Yes (6 components)
