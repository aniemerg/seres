# Fix Intelligence: recipe_silicon_carbide_ceramic_v0

## Files

- **Recipe:** `kb/recipes/recipe_silicon_carbide_ceramic_v0.yaml`
- **Target item:** `silicon_carbide_ceramic_v0`
  - File: `kb/items/silicon_carbide_ceramic_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'carbothermal_synthesis_silicon_carbide_v0') requires input 'silica_purified' which is not available

**Location:** Step 0
**Process:** `carbothermal_synthesis_silicon_carbide_v0`
  - File: `kb/processes/carbothermal_synthesis_silicon_carbide_v0.yaml`

**Current step:**
```yaml
- process_id: carbothermal_synthesis_silicon_carbide_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_silicon_carbide_ceramic_v0.yaml`
- **BOM available:** No
