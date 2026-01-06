# Fix Intelligence: recipe_carbon_safety_system_v0_v0

## Files

- **Recipe:** `kb/recipes/recipe_carbon_safety_system_v0_v0.yaml`
- **Target item:** `carbon_safety_system_v0_v0`
  - File: `kb/items/carbon_safety_system_v0_v0.yaml`
- **BOM:** `kb/boms/bom_carbon_safety_system_v0_v0.yaml` ✓
  - Components: 3
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'assembly_basic_v0') requires input 'gasket_sheet_core_v0_part' which is not available

**Location:** Step 0
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: gasket_sheet_core_v0_part
    qty: 1.0
    unit: kg
  - item_id: gas_inlet_manifold_v0
    qty: 1.0
    unit: kg
  - item_id: valve_body_cast_rough_v0
    qty: 1.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `gasket_sheet_core_v0_part` not found

This item doesn't exist in the KB.

**Suggestions:**
1. Check if item name is misspelled
2. Add item to BOM if it should be a component
3. Replace with an output from a previous step

#### Problem: Item `gas_inlet_manifold_v0` not found

This item doesn't exist in the KB.

#### Problem: Item `valve_body_cast_rough_v0` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_carbon_safety_system_v0_v0.yaml`
- **BOM available:** Yes (3 components)
