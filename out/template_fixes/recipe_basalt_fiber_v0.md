# Fix Intelligence: recipe_basalt_fiber_v0

## Files

- **Recipe:** `kb/recipes/recipe_basalt_fiber_v0.yaml`
- **Target item:** `basalt_fiber`
  - File: `kb/items/basalt_fiber.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'glass_melting_and_forming_v0') requires input 'regolith_fine_fraction' which is not available

**Location:** Step 0
**Process:** `glass_melting_and_forming_v0`
  - File: `kb/processes/glass_melting_and_forming_v0.yaml`

**Current step:**
```yaml
- process_id: glass_melting_and_forming_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_basalt_fiber_v0.yaml`
- **BOM available:** No
