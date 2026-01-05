# Fix Intelligence: recipe_proximity_sensor_inductive_v0

## Files

- **Recipe:** `kb/recipes/recipe_proximity_sensor_inductive_v0.yaml`
- **Target item:** `proximity_sensor_inductive`
  - File: `kb/items/proximity_sensor_inductive.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'electronics_assembly_v0') requires input 'copper_wire_magnet' which is not available

**Location:** Step 0
**Process:** `electronics_assembly_v0`
  - File: `kb/processes/electronics_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: electronics_assembly_v0
  inputs:
  - item_id: copper_wire_magnet
    qty: 0.05
    unit: kg
  - item_id: pcb_populated
    qty: 0.02
    unit: kg
  - item_id: aluminum_alloy_ingot
    qty: 0.15
    unit: kg
  - item_id: potting_compound
    qty: 0.03
    unit: kg
  - item_id: wire_copper_insulated
    qty: 0.03
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `copper_wire_magnet` not found

This item doesn't exist in the KB.

#### Problem: Item `pcb_populated` not found

This item doesn't exist in the KB.

#### Problem: Item `aluminum_alloy_ingot` not found

This item doesn't exist in the KB.

#### Problem: Item `potting_compound` not found

This item doesn't exist in the KB.

#### Problem: Item `wire_copper_insulated` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_proximity_sensor_inductive_v0.yaml`
- **BOM available:** No
