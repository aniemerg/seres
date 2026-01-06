# Fix Intelligence: recipe_operator_cabin_v0

## Files

- **Recipe:** `kb/recipes/recipe_operator_cabin_v0.yaml`
- **Target item:** `operator_cabin`
  - File: `kb/items/operator_cabin.yaml`
- **BOM:** None
- **Steps:** 3 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_operator_cabin_v1` → operator_cabin (3 steps)

## Errors (3 found)

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

**Message:** Step 1 uses template process 'welded_fabrication_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `welded_fabrication_basic_v0`
  - File: `kb/processes/welded_fabrication_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: welded_fabrication_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `cut_parts` (9.5 kg)

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'glazing_and_installation_v0') requires input 'panel_or_door_assembly' which is not available

**Location:** Step 2
**Process:** `glazing_and_installation_v0`
  - File: `kb/processes/glazing_and_installation_v0.yaml`

**Current step:**
```yaml
- process_id: glazing_and_installation_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_operator_cabin_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
