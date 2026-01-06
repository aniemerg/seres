# Fix Intelligence: recipe_yn_neuron_differential_pair_v0

## Files

- **Recipe:** `kb/recipes/recipe_yn_neuron_differential_pair_v0.yaml`
- **Target item:** `yn_neuron_differential_pair_v0`
  - File: `kb/items/yn_neuron_differential_pair_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'yn_neuron_differential_pair_fabrication_v0') requires input 'steel_stock' which is not available

**Location:** Step 0
**Process:** `yn_neuron_differential_pair_fabrication_v0`
  - File: `kb/processes/yn_neuron_differential_pair_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: yn_neuron_differential_pair_fabrication_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_yn_neuron_differential_pair_v0.yaml`
- **BOM available:** No
