# Fix Intelligence: recipe_signal_generator_analog_v0

## Files

- **Recipe:** `kb/recipes/recipe_signal_generator_analog_v0.yaml`
- **Target item:** `signal_generator_analog_v0`
  - File: `kb/items/signal_generator_analog_v0.yaml`
- **BOM:** `kb/boms/bom_signal_generator_analog_v0.yaml` ✓
  - Components: 8
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'assembly_process_general_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `assembly_process_general_v0`
  - File: `kb/processes/assembly_process_general_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_process_general_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 8 components:

- `vacuum_tube_triode_v0` (qty: 3.0 each)
- `capacitor_variable_tuning_v0` (qty: 2.0 each)
- `resistor_wire_wound_v0` (qty: 10.0 each)
- `ferrite_toroid_core_v0` (qty: 2.0 each)
- `steel_sheet_3mm` (qty: 2.0 kg)
- `aluminum_sheet_2mm` (qty: 0.5 kg)
- `wire_copper_insulated` (qty: 0.3 kg)
- `knob_control_dial` (qty: 3.0 each)

Suggested fix:
```yaml
- process_id: assembly_process_general_v0
  inputs:
  - item_id: vacuum_tube_triode_v0
    qty: 3.0
    unit: each
  - item_id: capacitor_variable_tuning_v0
    qty: 2.0
    unit: each
  - item_id: resistor_wire_wound_v0
    qty: 10.0
    unit: each
  - item_id: ferrite_toroid_core_v0
    qty: 2.0
    unit: each
  - item_id: steel_sheet_3mm
    qty: 2.0
    unit: kg
  - item_id: aluminum_sheet_2mm
    qty: 0.5
    unit: kg
  - item_id: wire_copper_insulated
    qty: 0.3
    unit: kg
  - item_id: knob_control_dial
    qty: 3.0
    unit: each
```

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_signal_generator_analog_v0.yaml`
- **BOM available:** Yes (8 components)
