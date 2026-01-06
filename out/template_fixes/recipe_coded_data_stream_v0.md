# Fix Intelligence: recipe_coded_data_stream_v0

## Files

- **Recipe:** `kb/recipes/recipe_coded_data_stream_v0.yaml`
- **Target item:** `coded_data_stream`
  - File: `kb/items/coded_data_stream.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'error_correction_coding_v0') requires input 'uncoded_data_stream' which is not available

**Location:** Step 0
**Process:** `error_correction_coding_v0`
  - File: `kb/processes/error_correction_coding_v0.yaml`

**Current step:**
```yaml
- process_id: error_correction_coding_v0
  inputs:
  - item_id: uncoded_data_stream
    qty: 1.0
    unit: unit
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `uncoded_data_stream` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_coded_data_stream_v0.yaml`
- **BOM available:** No
