# Fix Intelligence: recipe_gas_inlet_manifold_v0

## Files

- **Recipe:** `kb/recipes/recipe_gas_inlet_manifold_v0.yaml`
- **Target item:** `gas_inlet_manifold_v0`
  - File: `kb/items/gas_inlet_manifold_v0.yaml`
- **BOM:** None
- **Steps:** 2 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_gas_inlet_manifold_v1` → gas_inlet_manifold (2 steps)

## Errors (2 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'cutting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `cutting_basic_v0`
  - File: `kb/processes/cutting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: cutting_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'machining_finish_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `machining_finish_basic_v0`
  - File: `kb/processes/machining_finish_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_finish_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `cut_parts` (9.5 kg)

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_gas_inlet_manifold_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
