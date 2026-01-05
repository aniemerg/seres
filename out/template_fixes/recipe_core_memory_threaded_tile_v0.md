# Fix Intelligence: recipe_core_memory_threaded_tile_v0

## Files

- **Recipe:** `kb/recipes/recipe_core_memory_threaded_tile_v0.yaml`
- **Target item:** `core_memory_threaded_tile_v0`
  - File: `kb/items/core_memory_threaded_tile_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'core_memory_threading_process_v0') requires input 'magnetic_core_memory_tile' which is not available

**Location:** Step 0
**Process:** `core_memory_threading_process_v0`
  - File: `kb/processes/core_memory_threading_process_v0.yaml`

**Current step:**
```yaml
- process_id: core_memory_threading_process_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_core_memory_threaded_tile_v0.yaml`
- **BOM available:** No
