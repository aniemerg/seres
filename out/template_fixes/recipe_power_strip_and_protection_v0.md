# Fix Intelligence: recipe_power_strip_and_protection_v0

## Files

- **Recipe:** `kb/recipes/recipe_power_strip_and_protection_v0.yaml`
- **Target item:** `power_strip_and_protection`
  - File: `kb/items/power_strip_and_protection.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'electrical_assembly_basic_v0') requires input 'wire_copper_insulated' which is not available

**Location:** Step 0
**Process:** `electrical_assembly_basic_v0`
  - File: `kb/processes/electrical_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: electrical_assembly_basic_v0
  inputs:
  - item_id: wire_copper_insulated
    qty: 0.6
    unit: kg
  - item_id: electronic_components_set
    qty: 0.4
    unit: kg
  - item_id: enclosure_small
    qty: 1.0
    unit: unit
  - item_id: fastener_kit_small
    qty: 0.2
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `wire_copper_insulated` not found

This item doesn't exist in the KB.

#### Problem: Item `electronic_components_set` not found

This item doesn't exist in the KB.

#### Problem: Item `enclosure_small` not found

This item doesn't exist in the KB.

#### Problem: Item `fastener_kit_small` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'sealing_and_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `sealing_and_assembly_basic_v0`
  - File: `kb/processes/sealing_and_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: sealing_and_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `power_strip_and_protection` (1.0 unit)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
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

- Step 0 produces: `power_strip_and_protection` (1.0 unit)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_power_strip_and_protection_v0.yaml`
- **BOM available:** No
