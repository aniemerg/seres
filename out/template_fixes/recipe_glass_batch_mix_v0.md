# Fix Intelligence: recipe_glass_batch_mix_v0

## Files

- **Recipe:** `kb/recipes/recipe_glass_batch_mix_v0.yaml`
- **Target item:** `glass_batch_mix`
  - File: `kb/items/glass_batch_mix.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (2 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'batching_and_mixing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `batching_and_mixing_basic_v0`
  - File: `kb/processes/batching_and_mixing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: batching_and_mixing_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `fine_powder` (1.0 kg)

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'drying_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
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

- Step 0 produces: `fine_powder` (1.0 kg)
- Step 1 produces: `powder_mixture` (1.0 kg)

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_glass_batch_mix_v0.yaml`
- **BOM available:** No
