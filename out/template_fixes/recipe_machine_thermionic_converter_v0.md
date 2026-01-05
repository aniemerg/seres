# Fix Intelligence: recipe_machine_thermionic_converter_v0

## Files

- **Recipe:** `kb/recipes/recipe_machine_thermionic_converter_v0.yaml`
- **Target item:** `thermionic_converter`
  - File: `kb/items/thermionic_converter.yaml`
- **BOM:** None
- **Steps:** 3 total

## Similar Recipes

Found 2 recipes producing similar items:

- `recipe_thermionic_converter_v0_v0` → thermionic_converter_v0 (8 steps)
- `recipe_thermionic_converter_v0` → thermionic_converter (5 steps)

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'assembly_basic_v0') requires input 'thermionic_vacuum_tube' which is not available

**Location:** Step 0
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: thermionic_vacuum_tube
    qty: 1.0
    unit: unit
  - item_id: converter_housing_assembly
    qty: 1.0
    unit: unit
  - item_id: vacuum_seal_assembly
    qty: 1.0
    unit: unit
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `thermionic_vacuum_tube` not found

This item doesn't exist in the KB.

#### Problem: Item `converter_housing_assembly` not found

This item doesn't exist in the KB.

#### Problem: Item `vacuum_seal_assembly` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'integration_test_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
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

- Step 0 produces: `thermionic_converter` (1.0 unit)

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

- Step 0 produces: `thermionic_converter` (1.0 unit)
- Step 1 produces: `assembled_electronics` (1.0 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_machine_thermionic_converter_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 2 found
