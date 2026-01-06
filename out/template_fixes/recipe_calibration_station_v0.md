# Fix Intelligence: recipe_calibration_station_v0

## Files

- **Recipe:** `kb/recipes/recipe_calibration_station_v0.yaml`
- **Target item:** `calibration_station`
  - File: `kb/items/calibration_station.yaml`
- **BOM:** `kb/boms/bom_calibration_station.yaml` ✓
  - Components: 3
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

BOM has 3 components:

- `support_frame_welded` (qty: 1 None)
- `mounting_fixtures_adjustable` (qty: 1 None)
- `calibration_artifacts` (qty: 1 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: support_frame_welded
    qty: 1
    unit: None
  - item_id: mounting_fixtures_adjustable
    qty: 1
    unit: None
  - item_id: calibration_artifacts
    qty: 1
    unit: None
```

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_calibration_station_v0.yaml`
- **BOM available:** Yes (3 components)
