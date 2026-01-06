# Fix Intelligence: recipe_wire_tensioning_system_v0

## Files

- **Recipe:** `kb/recipes/recipe_wire_tensioning_system_v0.yaml`
- **Target item:** `wire_tensioning_system`
  - File: `kb/items/wire_tensioning_system.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'machining_process_turning_v0') requires input 'steel_bar_stock' which is not available

**Location:** Step 0
**Process:** `machining_process_turning_v0`
  - File: `kb/processes/machining_process_turning_v0.yaml`

**Current step:**
```yaml
- process_id: machining_process_turning_v0
  inputs:
  - item_id: steel_bar_stock
    qty: 2.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `steel_bar_stock` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'metal_fabrication_welding_v0') requires input 'steel_bar_stock' which is not available

**Location:** Step 1
**Process:** `metal_fabrication_welding_v0`
  - File: `kb/processes/metal_fabrication_welding_v0.yaml`

**Current step:**
```yaml
- process_id: metal_fabrication_welding_v0
  inputs:
  - item_id: steel_bar_stock
    qty: 1.5
    unit: kg
  - item_id: steel_sheet_3mm
    qty: 0.5
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `steel_bar_stock` not found

This item doesn't exist in the KB.

#### Problem: Item `steel_sheet_3mm` not found

This item doesn't exist in the KB.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'assembly_process_general_v0') requires input 'tensioner_frame_welded' which is not available

**Location:** Step 2
**Process:** `assembly_process_general_v0`
  - File: `kb/processes/assembly_process_general_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_process_general_v0
  inputs:
  - item_id: tensioner_frame_welded
    qty: 1.9
    unit: kg
  - item_id: tension_roller_set
    qty: 1.8
    unit: kg
  - item_id: spring_compression_small
    qty: 2.0
    unit: each
  - item_id: bearing_ball_steel
    qty: 2.0
    unit: each
  - item_id: bolt_hex_medium_steel
    qty: 2.0
    unit: each
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `tensioner_frame_welded` not found

This item doesn't exist in the KB.

#### Problem: Item `tension_roller_set` not found

This item doesn't exist in the KB.

#### Problem: Item `spring_compression_small` not found

This item doesn't exist in the KB.

#### Problem: Item `bearing_ball_steel` not found

This item doesn't exist in the KB.

#### Problem: Item `bolt_hex_medium_steel` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_wire_tensioning_system_v0.yaml`
- **BOM available:** No
