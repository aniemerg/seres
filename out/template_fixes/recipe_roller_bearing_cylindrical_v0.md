# Fix Intelligence: recipe_roller_bearing_cylindrical_v0

## Files

- **Recipe:** `kb/recipes/recipe_roller_bearing_cylindrical_v0.yaml`
- **Target item:** `roller_bearing_cylindrical_v0`
  - File: `kb/items/roller_bearing_cylindrical_v0.yaml`
- **BOM:** None
- **Steps:** 5 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_forging_process_v0') requires input 'bearing_ring_blanks' which is not available

**Location:** Step 0
**Process:** `metal_forging_process_v0`
  - File: `kb/processes/metal_forging_process_v0.yaml`

**Current step:**
```yaml
- process_id: metal_forging_process_v0
  inputs:
  - item_id: bearing_ring_blanks
    qty: 1.3
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `bearing_ring_blanks` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'heat_treatment_hardening_v0') requires input 'bearing_rings_machined' which is not available

**Location:** Step 2
**Process:** `heat_treatment_hardening_v0`
  - File: `kb/processes/heat_treatment_hardening_v0.yaml`

**Current step:**
```yaml
- process_id: heat_treatment_hardening_v0
  inputs:
  - item_id: bearing_rings_machined
    qty: 1.1
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `bearing_rings_machined` not found

This item doesn't exist in the KB.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 4 (process 'assembly_basic_v0') requires input 'bearing_rings_ground' which is not available

**Location:** Step 4
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: bearing_rings_ground
    qty: 1.0
    unit: kg
  - item_id: rolling_elements_set
    qty: 6.0
    unit: kg
  - item_id: bearing_cage_set
    qty: 2.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `bearing_rings_ground` not found

This item doesn't exist in the KB.

#### Problem: Item `rolling_elements_set` not found

This item doesn't exist in the KB.

#### Problem: Item `bearing_cage_set` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_roller_bearing_cylindrical_v0.yaml`
- **BOM available:** No
