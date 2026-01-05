# Fix Intelligence: recipe_casting_patterns_wooden_v0

## Files

- **Recipe:** `kb/recipes/recipe_casting_patterns_wooden_v0.yaml`
- **Target item:** `casting_patterns_wooden`
  - File: `kb/items/casting_patterns_wooden.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'woodworking_basic_v0') requires input 'binder_material' which is not available

**Location:** Step 0
**Process:** `woodworking_basic_v0`
  - File: `kb/processes/woodworking_basic_v0.yaml`

**Current step:**
```yaml
- process_id: woodworking_basic_v0
  inputs:
  - item_id: binder_material
    qty: 2.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `binder_material` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'woodworking_basic_v0') requires input 'cellulose_raw' which is not available

**Location:** Step 1
**Process:** `woodworking_basic_v0`
  - File: `kb/processes/woodworking_basic_v0.yaml`

**Current step:**
```yaml
- process_id: woodworking_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

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

- Step 0 produces: `finished_part` (1.0 kg)
- Step 1 produces: `finished_part` (1.0 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_casting_patterns_wooden_v0.yaml`
- **BOM available:** No
