# Fix Intelligence: recipe_centrifugal_separator_v0

## Files

- **Recipe:** `kb/recipes/recipe_centrifugal_separator_v0.yaml`
- **Target item:** `centrifugal_separator_v0`
  - File: `kb/items/centrifugal_separator_v0.yaml`
- **BOM:** `kb/boms/bom_centrifugal_separator_v0.yaml` ✓
  - Components: 8
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

BOM has 8 components:

- `motor_electric_medium` (qty: 1 unit)
- `centrifugal_bowl_steel` (qty: 80.0 kg)
- `bearing_set_heavy` (qty: 2 unit)
- `structural_frame_steel` (qty: 100.0 kg)
- `spring_and_dampener_set` (qty: 4 unit)
- `control_panel_basic` (qty: 1 unit)
- `piping_and_fittings_set` (qty: 20.0 kg)
- `fastener_kit_medium` (qty: 2 unit)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: motor_electric_medium
    qty: 1
    unit: unit
  - item_id: centrifugal_bowl_steel
    qty: 80.0
    unit: kg
  - item_id: bearing_set_heavy
    qty: 2
    unit: unit
  - item_id: structural_frame_steel
    qty: 100.0
    unit: kg
  - item_id: spring_and_dampener_set
    qty: 4
    unit: unit
  - item_id: control_panel_basic
    qty: 1
    unit: unit
  - item_id: piping_and_fittings_set
    qty: 20.0
    unit: kg
  - item_id: fastener_kit_medium
    qty: 2
    unit: unit
```

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_centrifugal_separator_v0.yaml`
- **BOM available:** Yes (8 components)
