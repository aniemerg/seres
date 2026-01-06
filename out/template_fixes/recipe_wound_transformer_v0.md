# Fix Intelligence: recipe_wound_transformer_v0

## Files

- **Recipe:** `kb/recipes/recipe_wound_transformer_v0.yaml`
- **Target item:** `wound_transformer`
  - File: `kb/items/wound_transformer.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'transformer_winding_v0') requires input 'transformer_core' which is not available

**Location:** Step 0
**Process:** `transformer_winding_v0`
  - File: `kb/processes/transformer_winding_v0.yaml`

**Current step:**
```yaml
- process_id: transformer_winding_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_wound_transformer_v0.yaml`
- **BOM available:** No
