# Fix Intelligence: recipe_refractory_brick_set_v0

## Files

- **Recipe:** `kb/recipes/recipe_refractory_brick_set_v0.yaml`
- **Target item:** `refractory_brick_set`
  - File: `kb/items/refractory_brick_set.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (4 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'powder_processing_v0') requires input 'alumina_powder' which is not available

**Location:** Step 0
**Process:** `powder_processing_v0`
  - File: `kb/processes/powder_processing_v0.yaml`

**Current step:**
```yaml
- process_id: powder_processing_v0
  inputs:
  - item_id: alumina_powder
    qty: 150.0
    unit: kg
  - item_id: ceramic_powder
    qty: 40.0
    unit: kg
  - item_id: binder_material
    qty: 10.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `alumina_powder` not found

This item doesn't exist in the KB.

#### Problem: Item `ceramic_powder` not found

This item doesn't exist in the KB.

#### Problem: Item `binder_material` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'pressing_operations_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `pressing_operations_basic_v0`
  - File: `kb/processes/pressing_operations_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: pressing_operations_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `processed_powder_mixture` (1.0 kg)

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'sintering_basic_v0') requires input 'powder_metal_or_ceramic' which is not available

**Location:** Step 2
**Process:** `sintering_basic_v0`
  - File: `kb/processes/sintering_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: sintering_basic_v0
  inputs:
  - item_id: powder_metal_or_ceramic
    qty: 200.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Generic placeholder `powder_metal_or_ceramic`

This is not a real item. Need to replace with specific item.

**Specific items matching pattern:**

- `ceramic_fiber_raw`
- `ceramic_insulator_tube`
- `zirconia_ceramic_v0`
- `ceramic_fiber_slurry`
- `silicon_nitride_ceramic_v0`
- `powder_metal_or_ceramic`
- `alumina_ceramic_v0`
- `ceramic_block_small_v0`
- `ceramic_fired_high_temp`
- `ceramic_powder_mixture`

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'inspection_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
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

- Step 0 produces: `processed_powder_mixture` (1.0 kg)
- Step 1 produces: `pressed_component` (9.5 kg)
- Step 2 produces: `sintered_parts` (0.95 kg)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_refractory_brick_set_v0.yaml`
- **BOM available:** No
