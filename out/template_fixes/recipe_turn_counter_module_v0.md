# Fix Intelligence: recipe_turn_counter_module_v0

## Files

- **Recipe:** `kb/recipes/recipe_turn_counter_module_v0.yaml`
- **Target item:** `turn_counter_module`
  - File: `kb/items/turn_counter_module.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'pcb_assembly_basic_v0') requires input 'bare_pcb' which is not available

**Location:** Step 0
**Process:** `pcb_assembly_basic_v0`
  - File: `kb/processes/pcb_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: pcb_assembly_basic_v0
  inputs:
  - item_id: bare_pcb
    qty: 0.1
    unit: kg
  - item_id: electronic_components_set
    qty: 0.1
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `bare_pcb` not found

This item doesn't exist in the KB.

#### Problem: Item `electronic_components_set` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'sensor_integration_v0') requires input 'sensor_suite_general' which is not available

**Location:** Step 1
**Process:** `sensor_integration_v0`
  - File: `kb/processes/sensor_integration_v0.yaml`

**Current step:**
```yaml
- process_id: sensor_integration_v0
  inputs:
  - item_id: sensor_suite_general
    qty: 0.1
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `sensor_suite_general` not found

This item doesn't exist in the KB.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'assembly_basic_v0') requires input 'enclosure_small' which is not available

**Location:** Step 2
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: enclosure_small
    qty: 0.2
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `enclosure_small` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_turn_counter_module_v0.yaml`
- **BOM available:** No
