# Fix Intelligence: recipe_expansion_valve_cryogenic_v0

## Files

- **Recipe:** `kb/recipes/recipe_expansion_valve_cryogenic_v0.yaml`
- **Target item:** `expansion_valve_cryogenic`
  - File: `kb/items/expansion_valve_cryogenic.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'machining_precision_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `machining_precision_v0`
  - File: `kb/processes/machining_precision_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_precision_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
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

- Step 0 produces: `machined_steel_part_precision` (7.0 kg)

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_expansion_valve_cryogenic_v0.yaml`
- **BOM available:** No
