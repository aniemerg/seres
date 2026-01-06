# Fix Intelligence: recipe_wire_brush_set_v0

## Files

- **Recipe:** `kb/recipes/recipe_wire_brush_set_v0.yaml`
- **Target item:** `wire_brush_set`
  - File: `kb/items/wire_brush_set.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'wire_drawing_basic_v0') requires input 'steel_stock_bar_or_billet' which is not available

**Location:** Step 0
**Process:** `wire_drawing_basic_v0`
  - File: `kb/processes/wire_drawing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: wire_drawing_basic_v0
  inputs:
  - item_id: steel_stock_bar_or_billet
    qty: 0.6
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Generic placeholder `steel_stock_bar_or_billet`

This is not a real item. Need to replace with specific item.

**Specific items matching pattern:**

- `stainless_billet_or_slab`
- `steel_stock_bar_or_billet`
- `steel_billet_or_slab`

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'machining_finish_basic_v0') requires input 'steel_stock_bar_or_billet' which is not available

**Location:** Step 1
**Process:** `machining_finish_basic_v0`
  - File: `kb/processes/machining_finish_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_finish_basic_v0
  inputs:
  - item_id: steel_stock_bar_or_billet
    qty: 0.4
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Generic placeholder `steel_stock_bar_or_billet`

This is not a real item. Need to replace with specific item.

**Specific items matching pattern:**

- `stainless_billet_or_slab`
- `steel_stock_bar_or_billet`
- `steel_billet_or_slab`

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `metal_wire_feed` (1.0 kg)
- Step 1 produces: `machined_part_raw` (1.0 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_wire_brush_set_v0.yaml`
- **BOM available:** No
