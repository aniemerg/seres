# Fix Intelligence: recipe_mixing_tank_medium_v0

## Files

- **Recipe:** `kb/recipes/recipe_mixing_tank_medium_v0.yaml`
- **Target item:** `mixing_tank_medium`
  - File: `kb/items/mixing_tank_medium.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (4 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_spinning_process_v0') requires input 'stainless_steel_sheet' which is not available

**Location:** Step 0
**Process:** `metal_spinning_process_v0`
  - File: `kb/processes/metal_spinning_process_v0.yaml`

**Current step:**
```yaml
- process_id: metal_spinning_process_v0
  inputs:
  - item_id: stainless_steel_sheet
    qty: 30.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `stainless_steel_sheet` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'welding_process_tig_v0') requires input 'stainless_steel_sheet' which is not available

**Location:** Step 1
**Process:** `welding_process_tig_v0`
  - File: `kb/processes/welding_process_tig_v0.yaml`

**Current step:**
```yaml
- process_id: welding_process_tig_v0
  inputs:
  - item_id: tank_shell_spun
    qty: 28.0
    unit: kg
  - item_id: stainless_steel_sheet
    qty: 5.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `tank_shell_spun` not found

This item doesn't exist in the KB.

#### Problem: Item `stainless_steel_sheet` not found

This item doesn't exist in the KB.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'machining_process_milling_v0') requires input 'steel_bar_stock' which is not available

**Location:** Step 2
**Process:** `machining_process_milling_v0`
  - File: `kb/processes/machining_process_milling_v0.yaml`

**Current step:**
```yaml
- process_id: machining_process_milling_v0
  inputs:
  - item_id: steel_bar_stock
    qty: 3.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `steel_bar_stock` not found

This item doesn't exist in the KB.

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'assembly_process_general_v0') requires input 'mixer_agitator_shaft_and_paddles' which is not available

**Location:** Step 3
**Process:** `assembly_process_general_v0`
  - File: `kb/processes/assembly_process_general_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_process_general_v0
  inputs:
  - item_id: tank_shell_spun
    qty: 32.0
    unit: kg
  - item_id: mixer_agitator_shaft_and_paddles
    qty: 2.5
    unit: kg
  - item_id: electric_motor_small
    qty: 1.0
    unit: each
  - item_id: seal_mechanical_rotary
    qty: 1.0
    unit: each
  - item_id: valve_ball_stainless
    qty: 2.0
    unit: each
  - item_id: glass_to_metal_seal_v0
    qty: 1.0
    unit: each
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `tank_shell_spun` not found

This item doesn't exist in the KB.

#### Problem: Item `mixer_agitator_shaft_and_paddles` not found

This item doesn't exist in the KB.

#### Problem: Item `electric_motor_small` not found

This item doesn't exist in the KB.

#### Problem: Item `seal_mechanical_rotary` not found

This item doesn't exist in the KB.

#### Problem: Item `valve_ball_stainless` not found

This item doesn't exist in the KB.

#### Problem: Item `glass_to_metal_seal_v0` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_mixing_tank_medium_v0.yaml`
- **BOM available:** No
