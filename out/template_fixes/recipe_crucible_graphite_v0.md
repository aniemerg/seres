# Fix Intelligence: recipe_crucible_graphite_v0

## Files

- **Recipe:** `kb/recipes/recipe_crucible_graphite_v0.yaml`
- **Target item:** `crucible_graphite`
  - File: `kb/items/crucible_graphite.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'graphite_molding_v0') requires input 'graphite_powder' which is not available

**Location:** Step 0
**Process:** `graphite_molding_v0`
  - File: `kb/processes/graphite_molding_v0.yaml`

**Current step:**
```yaml
- process_id: graphite_molding_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'sintering_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `sintering_basic_v0`
  - File: `kb/processes/sintering_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: sintering_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `crucible_graphite` (0.01 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'machining_finish_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
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

- Step 0 produces: `crucible_graphite` (0.01 kg)
- Step 1 produces: `sintered_parts` (0.95 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_crucible_graphite_v0.yaml`
- **BOM available:** No
