# Fix Intelligence: recipe_antenna_parabolic_dish_v0

## Files

- **Recipe:** `kb/recipes/recipe_antenna_parabolic_dish_v0.yaml`
- **Target item:** `antenna_parabolic_dish_v0`
  - File: `kb/items/antenna_parabolic_dish_v0.yaml`
- **BOM:** `kb/boms/bom_antenna_parabolic_dish_v0.yaml` ✓
  - Components: 7
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

BOM has 7 components:

- `aluminum_sheet_reflector_v0` (qty: 30.0 kg)
- `feed_horn_antenna_v0` (qty: 1.0 each)
- `support_struts_aluminum` (qty: 10.0 kg)
- `mounting_bracket_azimuth_elevation` (qty: 1.0 each)
- `bearing_ball_steel` (qty: 4.0 each)
- `coaxial_cable_low_loss` (qty: 20.0 m)
- `protective_coating_aluminum` (qty: 0.5 kg)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: aluminum_sheet_reflector_v0
    qty: 30.0
    unit: kg
  - item_id: feed_horn_antenna_v0
    qty: 1.0
    unit: each
  - item_id: support_struts_aluminum
    qty: 10.0
    unit: kg
  - item_id: mounting_bracket_azimuth_elevation
    qty: 1.0
    unit: each
  - item_id: bearing_ball_steel
    qty: 4.0
    unit: each
  - item_id: coaxial_cable_low_loss
    qty: 20.0
    unit: m
  - item_id: protective_coating_aluminum
    qty: 0.5
    unit: kg
```

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_antenna_parabolic_dish_v0.yaml`
- **BOM available:** Yes (7 components)
