# Fix Intelligence: recipe_pcb_paste_applied_v0

## Files

- **Recipe:** `kb/recipes/recipe_pcb_paste_applied_v0.yaml`
- **Target item:** `pcb_paste_applied`
  - File: `kb/items/pcb_paste_applied.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'solder_paste_application_v0') requires input 'pcb_bare_board' which is not available

**Location:** Step 0
**Process:** `solder_paste_application_v0`
  - File: `kb/processes/solder_paste_application_v0.yaml`

**Current step:**
```yaml
- process_id: solder_paste_application_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_pcb_paste_applied_v0.yaml`
- **BOM available:** No
