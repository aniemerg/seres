# Fix Intelligence: recipe_regolith_concrete_polymer_v0

## Files

- **Recipe:** `kb/recipes/recipe_regolith_concrete_polymer_v0.yaml`
- **Target item:** `regolith_concrete_polymer_v0`
  - File: `kb/items/regolith_concrete_polymer_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'regolith_concrete_polymer_binding_v0') requires input 'regolith_powder' which is not available

**Location:** Step 0
**Process:** `regolith_concrete_polymer_binding_v0`
  - File: `kb/processes/regolith_concrete_polymer_binding_v0.yaml`

**Current step:**
```yaml
- process_id: regolith_concrete_polymer_binding_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_regolith_concrete_polymer_v0.yaml`
- **BOM available:** No
