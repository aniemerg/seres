# Fix Intelligence: recipe_heat_sink_assembly_large_v0

## Files

- **Recipe:** `kb/recipes/recipe_heat_sink_assembly_large_v0.yaml`
- **Target item:** `heat_sink_assembly_large`
  - File: `kb/items/heat_sink_assembly_large.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_extrusion_process_v0') requires input 'aluminum_alloy_ingot' which is not available

**Location:** Step 0
**Process:** `metal_extrusion_process_v0`
  - File: `kb/processes/metal_extrusion_process_v0.yaml`

**Current step:**
```yaml
- process_id: metal_extrusion_process_v0
  inputs:
  - item_id: aluminum_alloy_ingot
    qty: 25.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `aluminum_alloy_ingot` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'machining_process_milling_v0') requires input 'heat_sink_cut_to_length' which is not available

**Location:** Step 2
**Process:** `machining_process_milling_v0`
  - File: `kb/processes/machining_process_milling_v0.yaml`

**Current step:**
```yaml
- process_id: machining_process_milling_v0
  inputs:
  - item_id: heat_sink_cut_to_length
    qty: 21.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `heat_sink_cut_to_length` not found

This item doesn't exist in the KB.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'surface_treatment_anodizing_v0') requires input 'heat_sink_base_machined' which is not available

**Location:** Step 3
**Process:** `surface_treatment_anodizing_v0`
  - File: `kb/processes/surface_treatment_anodizing_v0.yaml`

**Current step:**
```yaml
- process_id: surface_treatment_anodizing_v0
  inputs:
  - item_id: heat_sink_base_machined
    qty: 20.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `heat_sink_base_machined` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_heat_sink_assembly_large_v0.yaml`
- **BOM available:** No
