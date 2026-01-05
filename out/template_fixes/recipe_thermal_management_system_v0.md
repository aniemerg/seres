# Fix Intelligence: recipe_thermal_management_system_v0

## Files

- **Recipe:** `kb/recipes/recipe_thermal_management_system_v0.yaml`
- **Target item:** `thermal_management_system`
  - File: `kb/items/thermal_management_system.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'assembly_basic_v0') requires input 'heat_pipes_set' which is not available

**Location:** Step 0
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: heat_pipes_set
    qty: 1.0
    unit: unit
  - item_id: radiator_panel_set
    qty: 1.0
    unit: unit
  - item_id: thermal_interface_material
    qty: 0.2
    unit: kg
  - item_id: fastener_kit_small
    qty: 1.0
    unit: unit
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `heat_pipes_set` not found

This item doesn't exist in the KB.

#### Problem: Item `radiator_panel_set` not found

This item doesn't exist in the KB.

#### Problem: Item `thermal_interface_material` not found

This item doesn't exist in the KB.

#### Problem: Item `fastener_kit_small` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_thermal_management_system_v0.yaml`
- **BOM available:** No
