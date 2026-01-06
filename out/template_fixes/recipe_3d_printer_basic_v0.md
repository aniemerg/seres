# Fix Intelligence: recipe_3d_printer_basic_v0

## Files

- **Recipe:** `kb/recipes/recipe_3d_printer_basic_v0.yaml`
- **Target item:** `3d_printer_basic_v0`
  - File: `kb/items/3d_printer_basic_v0.yaml`
- **BOM:** `kb/boms/bom_3d_printer_basic_v0.yaml` ✓
  - Components: 5
- **Steps:** 2 total

## Errors (1 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'calibration_and_test_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `calibration_and_test_basic_v0`
  - File: `kb/processes/calibration_and_test_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: calibration_and_test_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 5 components:

- `printer_frame_generic` (qty: 1.0 unit)
- `extruder_head_basic` (qty: 1.0 unit)
- `power_electronics_module` (qty: 1.0 unit)
- `power_supply_low_voltage` (qty: 1.0 unit)
- `power_supply_chassis_basic` (qty: 1.0 unit)

Suggested fix:
```yaml
- process_id: calibration_and_test_basic_v0
  inputs:
  - item_id: printer_frame_generic
    qty: 1.0
    unit: unit
  - item_id: extruder_head_basic
    qty: 1.0
    unit: unit
  - item_id: power_electronics_module
    qty: 1.0
    unit: unit
  - item_id: power_supply_low_voltage
    qty: 1.0
    unit: unit
  - item_id: power_supply_chassis_basic
    qty: 1.0
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `3d_printer_basic_v0` (1.0 unit)

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_3d_printer_basic_v0.yaml`
- **BOM available:** Yes (5 components)
