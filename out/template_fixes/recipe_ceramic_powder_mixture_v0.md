# Fix Intelligence: recipe_ceramic_powder_mixture_v0

## Files

- **Recipe:** `kb/recipes/recipe_ceramic_powder_mixture_v0.yaml`
- **Target item:** `ceramic_powder_mixture`
  - File: `kb/items/ceramic_powder_mixture.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (4 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'mixing_basic_v0') requires input 'alumina_powder' which is not available

**Location:** Step 0
**Process:** `mixing_basic_v0`
  - File: `kb/processes/mixing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: mixing_basic_v0
  inputs:
  - item_id: alumina_powder
    qty: 0.5
    unit: kg
  - item_id: silica_purified
    qty: 0.3
    unit: kg
  - item_id: kaolinite_clay
    qty: 0.2
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `alumina_powder` not found

This item doesn't exist in the KB.

#### Problem: Item `silica_purified` not found

This item doesn't exist in the KB.

#### Problem: Item `kaolinite_clay` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'ball_milling_v0') requires input 'coarse_powder' which is not available

**Location:** Step 1
**Process:** `ball_milling_v0`
  - File: `kb/processes/ball_milling_v0.yaml`

**Current step:**
```yaml
- process_id: ball_milling_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'drying_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `drying_basic_v0`
  - File: `kb/processes/drying_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: drying_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `ceramic_powder_mixture` (1.0 kg)
- Step 1 produces: `fine_powder` (0.98 kg)

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'screening_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
**Process:** `screening_basic_v0`
  - File: `kb/processes/screening_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: screening_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `ceramic_powder_mixture` (1.0 kg)
- Step 1 produces: `fine_powder` (0.98 kg)
- Step 2 produces: `dried_material` (1.0 kg)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_ceramic_powder_mixture_v0.yaml`
- **BOM available:** No
