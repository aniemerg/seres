# Fix Intelligence: recipe_speed_control_module_v0

## Files

- **Recipe:** `kb/recipes/recipe_speed_control_module_v0.yaml`
- **Target item:** `speed_control_module`
  - File: `kb/items/speed_control_module.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'pcb_assembly_basic_v0') requires input 'pcb_substrate_v0' which is not available

**Location:** Step 0
**Process:** `pcb_assembly_basic_v0`
  - File: `kb/processes/pcb_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: pcb_assembly_basic_v0
  inputs:
  - item_id: pcb_substrate_v0
    qty: 0.3
    unit: kg
  - item_id: electronic_components_set
    qty: 1.0
    unit: unit
  - item_id: solder_paste_tin_lead
    qty: 0.05
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `pcb_substrate_v0` not found

This item doesn't exist in the KB.

#### Problem: Item `electronic_components_set` not found

This item doesn't exist in the KB.

#### Problem: Item `solder_paste_tin_lead` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'enclosure_assembly_basic_v0') requires input 'pcb_populated' which is not available

**Location:** Step 1
**Process:** `enclosure_assembly_basic_v0`
  - File: `kb/processes/enclosure_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: enclosure_assembly_basic_v0
  inputs:
  - item_id: pcb_populated
    qty: 1.0
    unit: unit
  - item_id: enclosure_steel_small
    qty: 1.0
    unit: unit
  - item_id: heat_sink
    qty: 1.0
    unit: unit
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `pcb_populated` not found

This item doesn't exist in the KB.

#### Problem: Item `enclosure_steel_small` not found

This item doesn't exist in the KB.

#### Problem: Item `heat_sink` not found

This item doesn't exist in the KB.

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'calibration_and_test_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `calibration_and_test_basic_v0`
  - File: `kb/processes/calibration_and_test_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: calibration_and_test_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `pcb_populated` (1.0 unit)
- Step 1 produces: `speed_control_module` (1.0 unit)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_speed_control_module_v0.yaml`
- **BOM available:** No
