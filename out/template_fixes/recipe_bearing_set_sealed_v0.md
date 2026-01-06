# Fix Intelligence: recipe_bearing_set_sealed_v0

## Files

- **Recipe:** `kb/recipes/recipe_bearing_set_sealed_v0.yaml`
- **Target item:** `bearing_set_sealed`
  - File: `kb/items/bearing_set_sealed.yaml`
- **BOM:** None
- **Steps:** 5 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_forging_process_v0') requires input 'steel_bar_stock' which is not available

**Location:** Step 0
**Process:** `metal_forging_process_v0`
  - File: `kb/processes/metal_forging_process_v0.yaml`

**Current step:**
```yaml
- process_id: metal_forging_process_v0
  inputs:
  - item_id: steel_bar_stock
    qty: 1.5
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `steel_bar_stock` not found

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

**Message:** Step 4 (process 'assembly_process_bearing_v0') requires input 'bearing_rings_ground' which is not available

**Location:** Step 4
**Process:** `assembly_process_bearing_v0`
  - File: `kb/processes/assembly_process_bearing_v0.yaml`

**Current step:**
```yaml
- process_id: assembly_process_bearing_v0
  inputs:
  - item_id: bearing_rings_ground
    qty: 1.0
    unit: kg
  - item_id: bearing_ball_steel
    qty: 0.3
    unit: kg
  - item_id: bearing_cage_stamped
    qty: 0.1
    unit: kg
  - item_id: seal_rubber_bearing
    qty: 0.05
    unit: kg
  - item_id: grease_bearing_high_temp
    qty: 0.05
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `bearing_rings_ground` not found

This item doesn't exist in the KB.

#### Problem: Item `bearing_ball_steel` not found

This item doesn't exist in the KB.

#### Problem: Item `bearing_cage_stamped` not found

This item doesn't exist in the KB.

#### Problem: Item `seal_rubber_bearing` not found

This item doesn't exist in the KB.

#### Problem: Item `grease_bearing_high_temp` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_bearing_set_sealed_v0.yaml`
- **BOM available:** No
