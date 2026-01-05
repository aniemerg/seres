# Fix Intelligence: recipe_dressing_tool_diamond_v0

## Files

- **Recipe:** `kb/recipes/recipe_dressing_tool_diamond_v0.yaml`
- **Target item:** `dressing_tool_diamond`
  - File: `kb/items/dressing_tool_diamond.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'diamond_synthesis_hpht_v0') requires input 'graphite_powder' which is not available

**Location:** Step 0
**Process:** `diamond_synthesis_hpht_v0`
  - File: `kb/processes/diamond_synthesis_hpht_v0.yaml`

**Current step:**
```yaml
- process_id: diamond_synthesis_hpht_v0
  inputs:
  - item_id: graphite_powder
    qty: 0.01
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `graphite_powder` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'machining_process_turning_v0') requires input 'steel_bar_stock' which is not available

**Location:** Step 1
**Process:** `machining_process_turning_v0`
  - File: `kb/processes/machining_process_turning_v0.yaml`

**Current step:**
```yaml
- process_id: machining_process_turning_v0
  inputs:
  - item_id: steel_bar_stock
    qty: 0.3
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `steel_bar_stock` not found

This item doesn't exist in the KB.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'brazing_process_v0') requires input 'tool_holder_machined' which is not available

**Location:** Step 2
**Process:** `brazing_process_v0`
  - File: `kb/processes/brazing_process_v0.yaml`

**Current step:**
```yaml
- process_id: brazing_process_v0
  inputs:
  - item_id: tool_holder_machined
    qty: 0.25
    unit: kg
  - item_id: diamond_synthetic_industrial
    qty: 0.005
    unit: kg
  - item_id: brazing_alloy_generic
    qty: 0.005
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `tool_holder_machined` not found

This item doesn't exist in the KB.

#### Problem: Item `diamond_synthetic_industrial` not found

This item doesn't exist in the KB.

#### Problem: Item `brazing_alloy_generic` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_dressing_tool_diamond_v0.yaml`
- **BOM available:** No
