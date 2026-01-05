# Fix Intelligence: recipe_fms_control_system_v0

## Files

- **Recipe:** `kb/recipes/recipe_fms_control_system_v0.yaml`
- **Target item:** `fms_control_system_v0`
  - File: `kb/items/fms_control_system_v0.yaml`
- **BOM:** `kb/boms/bom_fms_control_system_v0.yaml` ✓
  - Components: 3
- **Steps:** 2 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'pcb_fabrication_process_v0') requires input 'copper_clad_laminate' which is not available

**Location:** Step 0
**Process:** `pcb_fabrication_process_v0`
  - File: `kb/processes/pcb_fabrication_process_v0.yaml`

**Current step:**
```yaml
- process_id: pcb_fabrication_process_v0
  inputs:
  - item_id: copper_clad_laminate
    qty: 0.2
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `copper_clad_laminate` not found

This item doesn't exist in the KB.

**Suggestions:**
1. Check if item name is misspelled
2. Add item to BOM if it should be a component
3. Replace with an output from a previous step

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_fms_control_system_v0.yaml`
- **BOM available:** Yes (3 components)
