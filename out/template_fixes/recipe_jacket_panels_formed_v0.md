# Fix Intelligence: recipe_jacket_panels_formed_v0

## Files

- **Recipe:** `kb/recipes/recipe_jacket_panels_formed_v0.yaml`
- **Target item:** `jacket_panels_formed`
  - File: `kb/items/jacket_panels_formed.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_forming_basic_v0') requires input 'metal_sheet_or_plate' which is not available

**Location:** Step 0
**Process:** `metal_forming_basic_v0`
  - File: `kb/processes/metal_forming_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: metal_forming_basic_v0
  inputs:
  - item_id: metal_sheet_or_plate
    qty: 3.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Generic placeholder `metal_sheet_or_plate`

This is not a real item. Need to replace with specific item.

**Specific items matching pattern:**

- `steel_plate_raw`
- `steel_plate_or_sheet`
- `copper_plate_or_sheet`
- `metal_sheet`
- `plate_rolling_mill`
- `heating_plate_or_induction_heater`
- `mold_platen_assembly_v0`
- `press_platen_set_small`
- `granite_surface_plate_large`
- `jaw_plates_set`

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_jacket_panels_formed_v0.yaml`
- **BOM available:** No
