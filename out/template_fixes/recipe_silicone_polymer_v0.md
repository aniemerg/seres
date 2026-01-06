# Fix Intelligence: recipe_silicone_polymer_v0

## Files

- **Recipe:** `kb/recipes/recipe_silicone_polymer_v0.yaml`
- **Target item:** `silicone_polymer`
  - File: `kb/items/silicone_polymer.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'silicone_polymer_synthesis_v0') requires input 'silicone_precursor' which is not available

**Location:** Step 0
**Process:** `silicone_polymer_synthesis_v0`
  - File: `kb/processes/silicone_polymer_synthesis_v0.yaml`

**Current step:**
```yaml
- process_id: silicone_polymer_synthesis_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_silicone_polymer_v0.yaml`
- **BOM available:** No
