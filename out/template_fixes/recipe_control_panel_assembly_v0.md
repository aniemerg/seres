# Fix Intelligence: recipe_control_panel_assembly_v0

## Files

- **Recipe:** `kb/recipes/recipe_control_panel_assembly_v0.yaml`
- **Target item:** `control_panel_assembly_v0`
  - File: `kb/items/control_panel_assembly_v0.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

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

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'electrical_assembly_basic_v0') requires input 'raw_metal_block' which is not available

**Location:** Step 1
**Process:** `electrical_assembly_basic_v0`
  - File: `kb/processes/electrical_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: electrical_assembly_basic_v0
  inputs:
  - item_id: raw_metal_block
    qty: 25.0
    unit: kg
  - item_id: control_components
    qty: 1.0
    unit: unit
  - item_id: assembled_wire_harness
    qty: 1.0
    unit: unit
  - item_id: terminal_block_set
    qty: 1.0
    unit: unit
  - item_id: power_output_terminals
    qty: 1.0
    unit: unit
  - item_id: fastener_kit_medium
    qty: 1.0
    unit: unit
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `raw_metal_block` not found

This item doesn't exist in the KB.

#### Problem: Item `control_components` not found

This item doesn't exist in the KB.

#### Problem: Item `assembled_wire_harness` not found

This item doesn't exist in the KB.

#### Problem: Item `terminal_block_set` not found

This item doesn't exist in the KB.

#### Problem: Item `power_output_terminals` not found

This item doesn't exist in the KB.

#### Problem: Item `fastener_kit_medium` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_control_panel_assembly_v0.yaml`
- **BOM available:** No
