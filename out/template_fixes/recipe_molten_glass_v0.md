# Fix Intelligence: recipe_molten_glass_v0

## Files

- **Recipe:** `kb/recipes/recipe_molten_glass_v0.yaml`
- **Target item:** `molten_glass`
  - File: `kb/items/molten_glass.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'mineral_processing_basic_v0') requires input 'regolith_lunar_mare' which is not available

**Location:** Step 0
**Process:** `mineral_processing_basic_v0`
  - File: `kb/processes/mineral_processing_basic_v0.yaml`

**Current step:**
```yaml
- process_id: mineral_processing_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'glass_melting_v0') requires input 'glass_batch_mix' which is not available

**Location:** Step 1
**Process:** `glass_melting_v0`
  - File: `kb/processes/glass_melting_v0.yaml`

**Current step:**
```yaml
- process_id: glass_melting_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_molten_glass_v0.yaml`
- **BOM available:** No
