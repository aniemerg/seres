# Fix Intelligence: recipe_vibration_drive_module_v0

## Files

- **Recipe:** `kb/recipes/recipe_vibration_drive_module_v0.yaml`
- **Target item:** `vibration_drive_module`
  - File: `kb/items/vibration_drive_module.yaml`
- **BOM:** None
- **Steps:** 5 total

## Errors (5 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'machining_finish_basic_v0') requires input 'steel_stock_bar_or_billet' which is not available

**Location:** Step 0
**Process:** `machining_finish_basic_v0`
  - File: `kb/processes/machining_finish_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_finish_basic_v0
  inputs:
  - item_id: steel_stock_bar_or_billet
    qty: 8.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Generic placeholder `steel_stock_bar_or_billet`

This is not a real item. Need to replace with specific item.

**Specific items matching pattern:**

- `stainless_billet_or_slab`
- `steel_stock_bar_or_billet`
- `steel_billet_or_slab`

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'assembly_basic_v0') requires input 'motor_electric_small' which is not available

**Location:** Step 1
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: motor_electric_small
    qty: 10.0
    unit: kg
  - item_id: ball_bearing_steel_v0
    qty: 2.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `motor_electric_small` not found

This item doesn't exist in the KB.

#### Problem: Item `ball_bearing_steel_v0` not found

This item doesn't exist in the KB.

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'balancing_dynamic_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `balancing_dynamic_basic_v0`
  - File: `kb/processes/balancing_dynamic_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: balancing_dynamic_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `machined_part_raw` (1.0 kg)
- Step 1 produces: `assembled_equipment` (1.0 kg)

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'integration_test_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
**Process:** `integration_test_basic_v0`
  - File: `kb/processes/integration_test_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: integration_test_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `machined_part_raw` (1.0 kg)
- Step 1 produces: `assembled_equipment` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'inspection_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
**Process:** `inspection_basic_v0`
  - File: `kb/processes/inspection_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: inspection_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `machined_part_raw` (1.0 kg)
- Step 1 produces: `assembled_equipment` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)
- Step 3 produces: `assembled_electronics` (1.0 kg)

---

## Summary

- **Total errors:** 5
- **Recipe file:** `kb/recipes/recipe_vibration_drive_module_v0.yaml`
- **BOM available:** No
