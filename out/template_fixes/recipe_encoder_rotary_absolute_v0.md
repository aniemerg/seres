# Fix Intelligence: recipe_encoder_rotary_absolute_v0

## Files

- **Recipe:** `kb/recipes/recipe_encoder_rotary_absolute_v0.yaml`
- **Target item:** `encoder_rotary_absolute`
  - File: `kb/items/encoder_rotary_absolute.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'pcb_assembly_basic_v0') requires input 'pcb_bare_board' which is not available

**Location:** Step 0
**Process:** `pcb_assembly_basic_v0`
  - File: `kb/processes/pcb_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: pcb_assembly_basic_v0
  inputs:
  - item_id: pcb_bare_board
    qty: 0.05
    unit: kg
  - item_id: electronic_components_set
    qty: 0.02
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `pcb_bare_board` not found

This item doesn't exist in the KB.

#### Problem: Item `electronic_components_set` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'machining_precision_v0') requires input 'aluminum_alloy_ingot' which is not available

**Location:** Step 1
**Process:** `machining_precision_v0`
  - File: `kb/processes/machining_precision_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_precision_v0
  inputs:
  - item_id: aluminum_alloy_ingot
    qty: 0.3
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `aluminum_alloy_ingot` not found

This item doesn't exist in the KB.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'assembly_process_general_v0') requires input 'encoder_pcb_assembled' which is not available

**Location:** Step 2
**Process:** `assembly_process_general_v0`
  - File: `kb/processes/assembly_process_general_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_process_general_v0
  inputs:
  - item_id: encoder_pcb_assembled
    qty: 0.06
    unit: kg
  - item_id: encoder_disk_coded
    qty: 0.15
    unit: kg
  - item_id: aluminum_housing_machined_v0
    qty: 0.05
    unit: kg
  - item_id: bearing_set_small
    qty: 1.0
    unit: each
  - item_id: fastener_kit_small
    qty: 0.01
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `encoder_pcb_assembled` not found

This item doesn't exist in the KB.

#### Problem: Item `encoder_disk_coded` not found

This item doesn't exist in the KB.

#### Problem: Item `aluminum_housing_machined_v0` not found

This item doesn't exist in the KB.

#### Problem: Item `bearing_set_small` not found

This item doesn't exist in the KB.

#### Problem: Item `fastener_kit_small` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_encoder_rotary_absolute_v0.yaml`
- **BOM available:** No
