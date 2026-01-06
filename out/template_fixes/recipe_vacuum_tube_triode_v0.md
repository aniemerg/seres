# Fix Intelligence: recipe_vacuum_tube_triode_v0

## Files

- **Recipe:** `kb/recipes/recipe_vacuum_tube_triode_v0.yaml`
- **Target item:** `vacuum_tube_triode_v0`
  - File: `kb/items/vacuum_tube_triode_v0.yaml`
- **BOM:** None
- **Steps:** 5 total

## Errors (4 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'glass_blowing_process_v0') requires input 'glass_tube_borosilicate' which is not available

**Location:** Step 0
**Process:** `glass_blowing_process_v0`
  - File: `kb/processes/glass_blowing_process_v0.yaml`

**Current step:**
```yaml
- process_id: glass_blowing_process_v0
  inputs:
  - item_id: glass_tube_borosilicate
    qty: 0.02
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `glass_tube_borosilicate` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'wire_forming_process_v0') requires input 'nickel_wire_fine' which is not available

**Location:** Step 1
**Process:** `wire_forming_process_v0`
  - File: `kb/processes/wire_forming_process_v0.yaml`

**Current step:**
```yaml
- process_id: wire_forming_process_v0
  inputs:
  - item_id: nickel_wire_fine
    qty: 0.005
    unit: kg
  - item_id: tungsten_wire_drawing_v0
    qty: 0.003
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `nickel_wire_fine` not found

This item doesn't exist in the KB.

#### Problem: Item `tungsten_wire_drawing_v0` not found

This item doesn't exist in the KB.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'oxide_coating_cathode_v0') requires input 'barium_oxide' which is not available

**Location:** Step 2
**Process:** `oxide_coating_cathode_v0`
  - File: `kb/processes/oxide_coating_cathode_v0.yaml`

**Current step:**
```yaml
- process_id: oxide_coating_cathode_v0
  inputs:
  - item_id: tube_electrode_set
    qty: 0.007
    unit: kg
  - item_id: barium_oxide
    qty: 0.001
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `tube_electrode_set` not found

This item doesn't exist in the KB.

#### Problem: Item `barium_oxide` not found

This item doesn't exist in the KB.

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'tube_assembly_and_evacuation_v0') requires input 'tube_base_ceramic' which is not available

**Location:** Step 3
**Process:** `tube_assembly_and_evacuation_v0`
  - File: `kb/processes/tube_assembly_and_evacuation_v0.yaml`

**Current step:**
```yaml
- process_id: tube_assembly_and_evacuation_v0
  inputs:
  - item_id: tube_envelope_blown
    qty: 0.018
    unit: kg
  - item_id: cathode_coated
    qty: 0.008
    unit: kg
  - item_id: tube_base_ceramic
    qty: 0.01
    unit: kg
  - item_id: getter_material_raw
    qty: 0.002
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `tube_envelope_blown` not found

This item doesn't exist in the KB.

#### Problem: Item `cathode_coated` not found

This item doesn't exist in the KB.

#### Problem: Item `tube_base_ceramic` not found

This item doesn't exist in the KB.

#### Problem: Item `getter_material_raw` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_vacuum_tube_triode_v0.yaml`
- **BOM available:** No
