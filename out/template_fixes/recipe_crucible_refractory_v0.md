# Fix Intelligence: recipe_crucible_refractory_v0

## Files

- **Recipe:** `kb/recipes/recipe_crucible_refractory_v0.yaml`
- **Target item:** `crucible_refractory`
  - File: `kb/items/crucible_refractory.yaml`
- **BOM:** None
- **Steps:** 4 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_crucible_refractory_import_v0` → crucible_refractory (4 steps)

## Errors (4 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'ceramic_forming_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `ceramic_forming_basic_v0`
  - File: `kb/processes/ceramic_forming_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: ceramic_forming_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

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

- Step 0 produces: `green_ceramic_parts` (5.0 kg)

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'ceramic_firing_high_temp_v0') requires input 'green_ceramic_part' which is not available

**Location:** Step 2
**Process:** `ceramic_firing_high_temp_v0`
  - File: `kb/processes/ceramic_firing_high_temp_v0.yaml`

**Current step:**
```yaml
- process_id: ceramic_firing_high_temp_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'surface_finishing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
**Process:** `surface_finishing_basic_v0`
  - File: `kb/processes/surface_finishing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: surface_finishing_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `green_ceramic_parts` (5.0 kg)
- Step 1 produces: `dried_material` (1.0 kg)
- Step 2 produces: `sintered_shapes` (0.95 kg)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_crucible_refractory_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
