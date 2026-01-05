# Fix Intelligence: recipe_spindle_head_basic_v0

## Files

- **Recipe:** `kb/recipes/recipe_spindle_head_basic_v0.yaml`
- **Target item:** `spindle_head_basic`
  - File: `kb/items/spindle_head_basic.yaml`
- **BOM:** None
- **Steps:** 5 total

## Errors (5 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_casting_basic_v0') requires input 'metal_alloy_bulk' which is not available

**Location:** Step 0
**Process:** `metal_casting_basic_v0`
  - File: `kb/processes/metal_casting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: metal_casting_basic_v0
  inputs:
  - item_id: metal_alloy_bulk
    qty: 50.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `metal_alloy_bulk` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'machining_finish_basic_v0') requires input 'steel_bar_stock' which is not available

**Location:** Step 1
**Process:** `machining_finish_basic_v0`
  - File: `kb/processes/machining_finish_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_finish_basic_v0
  inputs:
  - item_id: cast_metal_parts
    qty: 47.5
    unit: kg
  - item_id: steel_bar_stock
    qty: 16.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `cast_metal_parts` not found

This item doesn't exist in the KB.

#### Problem: Item `steel_bar_stock` not found

This item doesn't exist in the KB.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'precision_grinding_basic_v0') requires input 'shaft_steel_machined' which is not available

**Location:** Step 2
**Process:** `precision_grinding_basic_v0`
  - File: `kb/processes/precision_grinding_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: precision_grinding_basic_v0
  inputs:
  - item_id: shaft_steel_machined
    qty: 15.0
    unit: kg
  - item_id: machined_metal_block_v0
    qty: 12.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `shaft_steel_machined` not found

This item doesn't exist in the KB.

#### Problem: Item `machined_metal_block_v0` not found

This item doesn't exist in the KB.

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'heat_treatment_cycle_basic_v0') requires input 'machined_steel_part_precision' which is not available

**Location:** Step 3
**Process:** `heat_treatment_cycle_basic_v0`
  - File: `kb/processes/heat_treatment_cycle_basic_v0.yaml`

**Current step:**
```yaml
- process_id: heat_treatment_cycle_basic_v0
  inputs:
  - item_id: machined_steel_part_precision
    qty: 26.5
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `machined_steel_part_precision` not found

This item doesn't exist in the KB.

---

### Error 5: recipe_step_input_not_satisfied

**Message:** Step 4 (process 'assembly_basic_v0') requires input 'machined_steel_part_precision' which is not available

**Location:** Step 4
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: machined_steel_part_precision
    qty: 26.5
    unit: kg
  - item_id: motor_housing_steel
    qty: 25.0
    unit: kg
  - item_id: bearing_set_heavy
    qty: 4.0
    unit: kg
  - item_id: belt_and_pulley_set
    qty: 2.5
    unit: kg
  - item_id: seal_mechanical_rotary
    qty: 0.4
    unit: kg
  - item_id: fastener_kit_medium
    qty: 1.0
    unit: kg
  - item_id: metal_alloy_bulk
    qty: 1.1
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `machined_steel_part_precision` not found

This item doesn't exist in the KB.

#### Problem: Item `motor_housing_steel` not found

This item doesn't exist in the KB.

#### Problem: Item `bearing_set_heavy` not found

This item doesn't exist in the KB.

#### Problem: Item `belt_and_pulley_set` not found

This item doesn't exist in the KB.

#### Problem: Item `seal_mechanical_rotary` not found

This item doesn't exist in the KB.

#### Problem: Item `fastener_kit_medium` not found

This item doesn't exist in the KB.

#### Problem: Item `metal_alloy_bulk` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 5
- **Recipe file:** `kb/recipes/recipe_spindle_head_basic_v0.yaml`
- **BOM available:** No
