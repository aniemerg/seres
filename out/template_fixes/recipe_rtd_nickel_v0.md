# Fix Intelligence: recipe_rtd_nickel_v0

## Files

- **Recipe:** `kb/recipes/recipe_rtd_nickel_v0.yaml`
- **Target item:** `rtd_nickel_v0`
  - File: `kb/items/rtd_nickel_v0.yaml`
- **BOM:** None
- **Steps:** 5 total

## Errors (4 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'wire_drawing_process_v0') requires input 'nickel_metal_pure' which is not available

**Location:** Step 0
**Process:** `wire_drawing_process_v0`
  - File: `kb/processes/wire_drawing_process_v0.yaml`

**Current step:**
```yaml
- process_id: wire_drawing_process_v0
  inputs:
  - item_id: nickel_metal_pure
    qty: 0.05
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `nickel_metal_pure` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'ceramic_sintering_process_v0') requires input 'alumina_powder' which is not available

**Location:** Step 1
**Process:** `ceramic_sintering_process_v0`
  - File: `kb/processes/ceramic_sintering_process_v0.yaml`

**Current step:**
```yaml
- process_id: ceramic_sintering_process_v0
  inputs:
  - item_id: alumina_powder
    qty: 0.01
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `alumina_powder` not found

This item doesn't exist in the KB.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'assembly_process_general_v0') requires input 'wire_copper_insulated' which is not available

**Location:** Step 3
**Process:** `assembly_process_general_v0`
  - File: `kb/processes/assembly_process_general_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_process_general_v0
  inputs:
  - item_id: rtd_element_wound
    qty: 0.01
    unit: kg
  - item_id: wire_copper_insulated
    qty: 0.005
    unit: kg
  - item_id: stainless_steel_sheath
    qty: 0.008
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `rtd_element_wound` not found

This item doesn't exist in the KB.

#### Problem: Item `wire_copper_insulated` not found

This item doesn't exist in the KB.

#### Problem: Item `stainless_steel_sheath` not found

This item doesn't exist in the KB.

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 4 (process 'calibration_temperature_sensor_v0') requires input 'rtd_assembled_uncalibrated' which is not available

**Location:** Step 4
**Process:** `calibration_temperature_sensor_v0`
  - File: `kb/processes/calibration_temperature_sensor_v0.yaml`

**Current step:**
```yaml
- process_id: calibration_temperature_sensor_v0
  inputs:
  - item_id: rtd_assembled_uncalibrated
    qty: 0.02
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `rtd_assembled_uncalibrated` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_rtd_nickel_v0.yaml`
- **BOM available:** No
