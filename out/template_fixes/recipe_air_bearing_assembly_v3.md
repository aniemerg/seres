# Fix Intelligence: recipe_air_bearing_assembly_v3

## Files

- **Recipe:** `kb/recipes/recipe_air_bearing_assembly_v3.yaml`
- **Target item:** `air_bearing_assembly`
  - File: `kb/items/air_bearing_assembly.yaml`
- **BOM:** None
- **Steps:** 2 total

## Similar Recipes

Found 3 recipes producing similar items:

- `recipe_air_bearing_assembly_local_v0` → air_bearing_assembly (1 steps)
- `recipe_air_bearing_assembly_v0` → air_bearing_assembly (1 steps)
- `recipe_air_bearing_assembly_v1` → air_bearing_assembly (1 steps)

## Errors (2 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'machining_finish_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `machining_finish_basic_v0`
  - File: `kb/processes/machining_finish_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_finish_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'assembly_basic_v0') requires input 'raw_metal_block' which is not available

**Location:** Step 1
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: raw_metal_block
    qty: 10.0
    unit: kg
  - item_id: air_manifold_and_nozzles
    qty: 1.0
    unit: unit
  - item_id: fittings_and_valves
    qty: 1.0
    unit: unit
  - item_id: fastener_kit_small
    qty: 1.0
    unit: unit
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `raw_metal_block` not found

This item doesn't exist in the KB.

#### Problem: Item `air_manifold_and_nozzles` not found

This item doesn't exist in the KB.

#### Problem: Item `fittings_and_valves` not found

This item doesn't exist in the KB.

#### Problem: Item `fastener_kit_small` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_air_bearing_assembly_v3.yaml`
- **BOM available:** No
- **Similar recipes:** 3 found
