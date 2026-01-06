# Fix Intelligence: recipe_photoresist_solution_v0

## Files

- **Recipe:** `kb/recipes/recipe_photoresist_solution_v0.yaml`
- **Target item:** `photoresist_solution_v0`
  - File: `kb/items/photoresist_solution_v0.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'chemical_synthesis_basic_v0') requires input 'methanol_liquid' which is not available

**Location:** Step 0
**Process:** `chemical_synthesis_basic_v0`
  - File: `kb/processes/chemical_synthesis_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: chemical_synthesis_basic_v0
  inputs:
  - item_id: methanol_liquid
    qty: 1.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `methanol_liquid` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'mixing_basic_v0') requires input 'epoxy_resin_base' which is not available

**Location:** Step 1
**Process:** `mixing_basic_v0`
  - File: `kb/processes/mixing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: mixing_basic_v0
  inputs:
  - item_id: epoxy_resin_base
    qty: 0.2
    unit: kg
  - item_id: solvent_generic
    qty: 0.8
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `epoxy_resin_base` not found

This item doesn't exist in the KB.

#### Problem: Item `solvent_generic` not found

This item doesn't exist in the KB.

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'inspection_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
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

- Step 0 produces: `chemical_product_crude` (0.85 kg)
- Step 1 produces: `photoresist_solution_v0` (1.0 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_photoresist_solution_v0.yaml`
- **BOM available:** No
