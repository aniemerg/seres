# Fix Intelligence: recipe_epoxy_precursor_block_v0

## Files

- **Recipe:** `kb/recipes/recipe_epoxy_precursor_block_v0.yaml`
- **Target item:** `epoxy_precursor_block_v0`
  - File: `kb/items/epoxy_precursor_block_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'epoxy_precursor_block_synthesis_v0') requires input 'epoxy_monomer_v0' which is not available

**Location:** Step 0
**Process:** `epoxy_precursor_block_synthesis_v0`
  - File: `kb/processes/epoxy_precursor_block_synthesis_v0.yaml`

**Current step:**
```yaml
- process_id: epoxy_precursor_block_synthesis_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_epoxy_precursor_block_v0.yaml`
- **BOM available:** No
