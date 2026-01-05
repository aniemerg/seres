# Fix Intelligence: recipe_transformer_step_down_welding_v0

## Files

- **Recipe:** `kb/recipes/recipe_transformer_step_down_welding_v0.yaml`
- **Target item:** `transformer_step_down_welding`
  - File: `kb/items/transformer_step_down_welding.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'assembly_basic_v0') requires input 'laminated_silicon_steel_core_v0' which is not available

**Location:** Step 0
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: laminated_silicon_steel_core_v0
    qty: 1.0
    unit: unit
  - item_id: magnet_wire_copper
    qty: 1.5
    unit: kg
  - item_id: insulation_coating_material
    qty: 0.3
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `laminated_silicon_steel_core_v0` not found

This item doesn't exist in the KB.

#### Problem: Item `magnet_wire_copper` not found

This item doesn't exist in the KB.

#### Problem: Item `insulation_coating_material` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_transformer_step_down_welding_v0.yaml`
- **BOM available:** No
