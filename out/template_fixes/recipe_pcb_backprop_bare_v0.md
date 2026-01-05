# Fix Intelligence: recipe_pcb_backprop_bare_v0

## Files

- **Recipe:** `kb/recipes/recipe_pcb_backprop_bare_v0.yaml`
- **Target item:** `pcb_backprop_bare`
  - File: `kb/items/pcb_backprop_bare.yaml`
- **BOM:** None
- **Steps:** 1 total

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
    qty: 0.5
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `copper_clad_laminate` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_pcb_backprop_bare_v0.yaml`
- **BOM available:** No
