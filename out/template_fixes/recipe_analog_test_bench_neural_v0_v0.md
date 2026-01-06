# Fix Intelligence: recipe_analog_test_bench_neural_v0_v0

## Files

- **Recipe:** `kb/recipes/recipe_analog_test_bench_neural_v0_v0.yaml`
- **Target item:** `analog_test_bench_neural_v0`
  - File: `kb/items/analog_test_bench_neural_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_analog_test_bench_neural_v0` → analog_test_bench_neural_v0 (1 steps)

## Errors (1 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_analog_test_bench_neural_v0_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
