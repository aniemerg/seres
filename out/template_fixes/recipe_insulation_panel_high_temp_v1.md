# Fix Intelligence: recipe_insulation_panel_high_temp_v1

## Files

- **Recipe:** `kb/recipes/recipe_insulation_panel_high_temp_v1.yaml`
- **Target item:** `insulation_panel_high_temp`
  - File: `kb/items/insulation_panel_high_temp.yaml`
- **BOM:** None
- **Steps:** 3 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_insulation_panel_high_temp_v0` → insulation_panel_high_temp_v0 (3 steps)

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'insulation_panel_forming_v0') requires input 'ceramic_powder' which is not available

**Location:** Step 0
**Process:** `insulation_panel_forming_v0`
  - File: `kb/processes/insulation_panel_forming_v0.yaml`

**Current step:**
```yaml
- process_id: insulation_panel_forming_v0
  inputs:
  - item_id: ceramic_powder
    qty: 35.0
    unit: kg
  - item_id: binder_material
    qty: 5.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `ceramic_powder` not found

This item doesn't exist in the KB.

#### Problem: Item `binder_material` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'drying_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `drying_basic_v0`
  - File: `kb/processes/drying_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: drying_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `insulation_panel_raw` (5.0 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'firing_ceramic_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `firing_ceramic_basic_v0`
  - File: `kb/processes/firing_ceramic_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: firing_ceramic_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `insulation_panel_raw` (5.0 kg)
- Step 1 produces: `dried_material` (1.0 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_insulation_panel_high_temp_v1.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
