# Fix Intelligence: recipe_data_encoding_manchester_v0

## Files

- **Recipe:** `kb/recipes/recipe_data_encoding_manchester_v0.yaml`
- **Target item:** `data_encoding_manchester_v0`
  - File: `kb/items/data_encoding_manchester_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'manchester_encoding_basic_v0') requires input 'raw_data_stream_manchester_v0' which is not available

**Location:** Step 0
**Process:** `manchester_encoding_basic_v0`
  - File: `kb/processes/manchester_encoding_basic_v0.yaml`

**Current step:**
```yaml
- process_id: manchester_encoding_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_data_encoding_manchester_v0.yaml`
- **BOM available:** No
