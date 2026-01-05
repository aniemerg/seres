# Fix Intelligence: recipe_separator_membrane_porous_v0

## Files

- **Recipe:** `kb/recipes/recipe_separator_membrane_porous_v0.yaml`
- **Target item:** `separator_membrane_porous`
  - File: `kb/items/separator_membrane_porous.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'mixing_and_blending_v0') requires input 'zirconia_ceramic_v0' which is not available

**Location:** Step 0
**Process:** `mixing_and_blending_v0`
  - File: `kb/processes/mixing_and_blending_v0.yaml`

**Current step:**
```yaml
- process_id: mixing_and_blending_v0
  inputs:
  - item_id: zirconia_ceramic_v0
    qty: 0.6
    unit: kg
  - item_id: silicone_polymer
    qty: 0.3
    unit: kg
  - item_id: water
    qty: 0.2
    unit: L
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `zirconia_ceramic_v0` not found

This item doesn't exist in the KB.

#### Problem: Item `silicone_polymer` not found

This item doesn't exist in the KB.

#### Problem: Item `water` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'ceramic_forming_v0') requires input 'ceramic_powder_mixture' which is not available

**Location:** Step 1
**Process:** `ceramic_forming_v0`
  - File: `kb/processes/ceramic_forming_v0.yaml`

**Current step:**
```yaml
- process_id: ceramic_forming_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'sintering_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `sintering_basic_v0`
  - File: `kb/processes/sintering_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: sintering_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `blended_mixture` (1.0 kg)
- Step 1 produces: `green_ceramic_part` (5.0 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_separator_membrane_porous_v0.yaml`
- **BOM available:** No
