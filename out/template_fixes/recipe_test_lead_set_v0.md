# Fix Intelligence: recipe_test_lead_set_v0

## Files

- **Recipe:** `kb/recipes/recipe_test_lead_set_v0.yaml`
- **Target item:** `test_lead_set`
  - File: `kb/items/test_lead_set.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'cutting_basic_v0') requires input 'wire_copper_insulated' which is not available

**Location:** Step 0
**Process:** `cutting_basic_v0`
  - File: `kb/processes/cutting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: cutting_basic_v0
  inputs:
  - item_id: wire_copper_insulated
    qty: 0.8
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `wire_copper_insulated` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'crimping_and_soldering_basic_v0') requires input 'electrical_wire_and_connectors' which is not available

**Location:** Step 1
**Process:** `crimping_and_soldering_basic_v0`
  - File: `kb/processes/crimping_and_soldering_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: crimping_and_soldering_basic_v0
  inputs:
  - item_id: electrical_wire_and_connectors
    qty: 0.2
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `electrical_wire_and_connectors` not found

This item doesn't exist in the KB.

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'integration_test_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
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

- Step 0 produces: `cut_parts` (9.5 kg)
- Step 1 produces: `assembled_wire_harness` (1.0 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_test_lead_set_v0.yaml`
- **BOM available:** No
