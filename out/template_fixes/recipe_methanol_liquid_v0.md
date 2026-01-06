# Fix Intelligence: recipe_methanol_liquid_v0

## Files

- **Recipe:** `kb/recipes/recipe_methanol_liquid_v0.yaml`
- **Target item:** `methanol_liquid`
  - File: `kb/items/methanol_liquid.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'methanol_synthesis_from_syngas_v0') requires input 'carbon_monoxide' which is not available

**Location:** Step 0
**Process:** `methanol_synthesis_from_syngas_v0`
  - File: `kb/processes/methanol_synthesis_from_syngas_v0.yaml`

**Current step:**
```yaml
- process_id: methanol_synthesis_from_syngas_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_methanol_liquid_v0.yaml`
- **BOM available:** No
