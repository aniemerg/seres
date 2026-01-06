# Fix Intelligence: recipe_connector_electrical_multi_pin_v0

## Files

- **Recipe:** `kb/recipes/recipe_connector_electrical_multi_pin_v0.yaml`
- **Target item:** `connector_electrical_multi_pin`
  - File: `kb/items/connector_electrical_multi_pin.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'connector_multi_pin_assembly_v0') requires input 'connector_pin_header_v0' which is not available

**Location:** Step 0
**Process:** `connector_multi_pin_assembly_v0`
  - File: `kb/processes/connector_multi_pin_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: connector_multi_pin_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_connector_electrical_multi_pin_v0.yaml`
- **BOM available:** No
