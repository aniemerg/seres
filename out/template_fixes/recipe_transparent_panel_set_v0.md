# Fix Intelligence: recipe_transparent_panel_set_v0

## Files

- **Recipe:** `kb/recipes/recipe_transparent_panel_set_v0.yaml`
- **Target item:** `transparent_panel_set`
  - File: `kb/items/transparent_panel_set.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'glass_casting_v0') requires input 'glass_raw_materials' which is not available

**Location:** Step 0
**Process:** `glass_casting_v0`
  - File: `kb/processes/glass_casting_v0.yaml`

**Current step:**
```yaml
- process_id: glass_casting_v0
  inputs:
  - item_id: glass_raw_materials
    qty: 11.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `glass_raw_materials` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'surface_finishing_v0') requires input 'sealing_gaskets' which is not available

**Location:** Step 1
**Process:** `surface_finishing_v0`
  - File: `kb/processes/surface_finishing_v0.yaml`

**Current step:**
```yaml
- process_id: surface_finishing_v0
  inputs:
  - item_id: cast_glass_parts
    qty: 10.0
    unit: kg
  - item_id: sealing_gaskets
    qty: 1.0
    unit: unit
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `cast_glass_parts` not found

This item doesn't exist in the KB.

#### Problem: Item `sealing_gaskets` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_transparent_panel_set_v0.yaml`
- **BOM available:** No
