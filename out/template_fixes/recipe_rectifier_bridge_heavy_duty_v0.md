# Fix Intelligence: recipe_rectifier_bridge_heavy_duty_v0

## Files

- **Recipe:** `kb/recipes/recipe_rectifier_bridge_heavy_duty_v0.yaml`
- **Target item:** `rectifier_bridge_heavy_duty`
  - File: `kb/items/rectifier_bridge_heavy_duty.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'assembly_basic_v0') requires input 'electronic_components_set' which is not available

**Location:** Step 0
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: electronic_components_set
    qty: 0.4
    unit: kg
  - item_id: heat_sink
    qty: 3.0
    unit: unit
  - item_id: bus_bar_copper
    qty: 0.3
    unit: kg
  - item_id: fastener_kit_medium
    qty: 0.1
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `electronic_components_set` not found

This item doesn't exist in the KB.

#### Problem: Item `heat_sink` not found

This item doesn't exist in the KB.

#### Problem: Item `bus_bar_copper` not found

This item doesn't exist in the KB.

#### Problem: Item `fastener_kit_medium` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_rectifier_bridge_heavy_duty_v0.yaml`
- **BOM available:** No
