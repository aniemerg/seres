# Fix Intelligence: recipe_grinder_cylindrical_v0_v0

## Files

- **Recipe:** `kb/recipes/recipe_grinder_cylindrical_v0_v0.yaml`
- **Target item:** `grinder_cylindrical_v0`
  - File: `kb/items/grinder_cylindrical_v0.yaml`
- **BOM:** `kb/boms/bom_grinder_cylindrical_v0.yaml` ✓
  - Components: 7
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'grinding_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `grinding_basic_v0`
  - File: `kb/processes/grinding_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: grinding_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 7 components:

- `steel_casting_machine_base` (qty: 1 None)
- `drive_motor_medium` (qty: 1 None)
- `bearing_set_heavy` (qty: 1 None)
- `tailstock_assembly` (qty: 1 None)
- `coolant_pump_system` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)
- `dressing_tool_diamond` (qty: 1 None)

Suggested fix:
```yaml
- process_id: grinding_basic_v0
  inputs:
  - item_id: steel_casting_machine_base
    qty: 1
    unit: None
  - item_id: drive_motor_medium
    qty: 1
    unit: None
  - item_id: bearing_set_heavy
    qty: 1
    unit: None
  - item_id: tailstock_assembly
    qty: 1
    unit: None
  - item_id: coolant_pump_system
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
  - item_id: dressing_tool_diamond
    qty: 1
    unit: None
```

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_grinder_cylindrical_v0_v0.yaml`
- **BOM available:** Yes (7 components)
