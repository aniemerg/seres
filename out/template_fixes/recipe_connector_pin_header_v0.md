# Fix Intelligence: recipe_connector_pin_header_v0

## Files

- **Recipe:** `kb/recipes/recipe_connector_pin_header_v0.yaml`
- **Target item:** `connector_pin_header_v0`
  - File: `kb/items/connector_pin_header_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_connector_pin_header_alias_v0` → connector_pin_header (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'pin_header_fabrication_v0') requires input 'raw_metal_block' which is not available

**Location:** Step 0
**Process:** `pin_header_fabrication_v0`
  - File: `kb/processes/pin_header_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: pin_header_fabrication_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_connector_pin_header_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
