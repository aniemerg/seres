# Fix Intelligence: recipe_linear_guide_rails_v0

## Files

- **Recipe:** `kb/recipes/recipe_linear_guide_rails_v0.yaml`
- **Target item:** `linear_guide_rails`
  - File: `kb/items/linear_guide_rails.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (4 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'machining_finish_basic_v0') requires input 'steel_bar_stock' which is not available

**Location:** Step 0
**Process:** `machining_finish_basic_v0`
  - File: `kb/processes/machining_finish_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_finish_basic_v0
  inputs:
  - item_id: steel_bar_stock
    qty: 22.0
    unit: kg
  - item_id: ball_bearing_steel_v0
    qty: 4.0
    unit: kg
  - item_id: fastener_kit_small
    qty: 0.5
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `steel_bar_stock` not found

This item doesn't exist in the KB.

#### Problem: Item `ball_bearing_steel_v0` not found

This item doesn't exist in the KB.

#### Problem: Item `fastener_kit_small` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'heat_treatment_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `heat_treatment_basic_v0`
  - File: `kb/processes/heat_treatment_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: heat_treatment_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `linear_guide_rails` (1.0 unit)

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'surface_grinding_precision_v0') requires input 'rough_part' which is not available

**Location:** Step 2
**Process:** `surface_grinding_precision_v0`
  - File: `kb/processes/surface_grinding_precision_v0.yaml`

**Current step:**
```yaml
- process_id: surface_grinding_precision_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `linear_guide_rails` (1.0 unit)
- Step 1 produces: `finished_part` (10.0 kg)
- Step 2 produces: `finished_part_deburred` (1.0 kg)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_linear_guide_rails_v0.yaml`
- **BOM available:** No
