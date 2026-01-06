# Fix Intelligence: recipe_sorel_cement_v0

## Files

- **Recipe:** `kb/recipes/recipe_sorel_cement_v0.yaml`
- **Target item:** `sorel_cement`
  - File: `kb/items/sorel_cement.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'sorel_cement_synthesis_v0') requires input 'magnesium_oxide' which is not available

**Location:** Step 0
**Process:** `sorel_cement_synthesis_v0`
  - File: `kb/processes/sorel_cement_synthesis_v0.yaml`

**Current step:**
```yaml
- process_id: sorel_cement_synthesis_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_sorel_cement_v0.yaml`
- **BOM available:** No
