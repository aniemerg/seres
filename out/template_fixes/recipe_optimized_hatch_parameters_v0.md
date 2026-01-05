# Fix Intelligence: recipe_optimized_hatch_parameters_v0

## Files

- **Recipe:** `kb/recipes/recipe_optimized_hatch_parameters_v0.yaml`
- **Target item:** `optimized_hatch_parameters`
  - File: `kb/items/optimized_hatch_parameters.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'hatch_spacing_optimization_v0') requires input 'uncoded_data_stream' which is not available

**Location:** Step 0
**Process:** `hatch_spacing_optimization_v0`
  - File: `kb/processes/hatch_spacing_optimization_v0.yaml`

**Current step:**
```yaml
- process_id: hatch_spacing_optimization_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_optimized_hatch_parameters_v0.yaml`
- **BOM available:** No
