# Fix Intelligence: recipe_wire_feed_system_basic_v0

## Files

- **Recipe:** `kb/recipes/recipe_wire_feed_system_basic_v0.yaml`
- **Target item:** `wire_feed_system_basic`
  - File: `kb/items/wire_feed_system_basic.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'assembly_basic_v0') requires input 'drive_motor_small' which is not available

**Location:** Step 0
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: drive_motor_small
    qty: 1.0
    unit: unit
  - item_id: gearbox_reducer_small
    qty: 1.0
    unit: unit
  - item_id: belt_and_pulley_set
    qty: 1.0
    unit: unit
  - item_id: wire_tensioning_system
    qty: 1.0
    unit: unit
  - item_id: fastener_kit_small
    qty: 0.2
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `drive_motor_small` not found

This item doesn't exist in the KB.

#### Problem: Item `gearbox_reducer_small` not found

This item doesn't exist in the KB.

#### Problem: Item `belt_and_pulley_set` not found

This item doesn't exist in the KB.

#### Problem: Item `wire_tensioning_system` not found

This item doesn't exist in the KB.

#### Problem: Item `fastener_kit_small` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_wire_feed_system_basic_v0.yaml`
- **BOM available:** No
