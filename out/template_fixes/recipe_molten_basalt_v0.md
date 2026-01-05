# Fix Intelligence: recipe_molten_basalt_v0

## Files

- **Recipe:** `kb/recipes/recipe_molten_basalt_v0.yaml`
- **Target item:** `molten_basalt`
  - File: `kb/items/molten_basalt.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'basalt_melting_v0') requires input 'basalt_aggregate' which is not available

**Location:** Step 0
**Process:** `basalt_melting_v0`
  - File: `kb/processes/basalt_melting_v0.yaml`

**Current step:**
```yaml
- process_id: basalt_melting_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'holding_and_pouring_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `holding_and_pouring_basic_v0`
  - File: `kb/processes/holding_and_pouring_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: holding_and_pouring_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `basalt_molten` (1.0 kg)

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_molten_basalt_v0.yaml`
- **BOM available:** No
