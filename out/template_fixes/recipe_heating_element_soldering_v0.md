# Fix Intelligence: recipe_heating_element_soldering_v0

## Files

- **Recipe:** `kb/recipes/recipe_heating_element_soldering_v0.yaml`
- **Target item:** `heating_element_soldering`
  - File: `kb/items/heating_element_soldering.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'coil_winding_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `coil_winding_basic_v0`
  - File: `kb/processes/coil_winding_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: coil_winding_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'coating_insulation_v0') requires input 'substrate_part_or_wire' which is not available

**Location:** Step 1
**Process:** `coating_insulation_v0`
  - File: `kb/processes/coating_insulation_v0.yaml`

**Current step:**
```yaml
- process_id: coating_insulation_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'assembly_basic_v0') requires input 'nickel_chromium_alloy' which is not available

**Location:** Step 2
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: nickel_chromium_alloy
    qty: 0.1
    unit: kg
  - item_id: ceramic_insulators
    qty: 0.1
    unit: kg
  - item_id: power_output_terminals
    qty: 1.0
    unit: unit
  - item_id: wire_copper_insulated
    qty: 0.05
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `nickel_chromium_alloy` not found

This item doesn't exist in the KB.

#### Problem: Item `ceramic_insulators` not found

This item doesn't exist in the KB.

#### Problem: Item `power_output_terminals` not found

This item doesn't exist in the KB.

#### Problem: Item `wire_copper_insulated` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_heating_element_soldering_v0.yaml`
- **BOM available:** No
