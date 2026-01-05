# Fix Intelligence: recipe_concentrated_mineral_v0

## Files

- **Recipe:** `kb/recipes/recipe_concentrated_mineral_v0.yaml`
- **Target item:** `concentrated_mineral`
  - File: `kb/items/concentrated_mineral.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (4 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'crushing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `crushing_basic_v0`
  - File: `kb/processes/crushing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: crushing_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'grinding_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `grinding_basic_v0`
  - File: `kb/processes/grinding_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: grinding_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `regolith_crushed` (1.0 kg)

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'mineral_concentration_v0') requires input 'crushed_ore' which is not available

**Location:** Step 2
**Process:** `mineral_concentration_v0`
  - File: `kb/processes/mineral_concentration_v0.yaml`

**Current step:**
```yaml
- process_id: mineral_concentration_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'drying_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
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

- Step 0 produces: `regolith_crushed` (1.0 kg)
- Step 1 produces: `finished_part_deburred` (0.99 kg)
- Step 2 produces: `concentrated_mineral` (0.3 kg)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_concentrated_mineral_v0.yaml`
- **BOM available:** No
