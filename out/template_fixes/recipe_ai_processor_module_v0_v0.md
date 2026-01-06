# Fix Intelligence: recipe_ai_processor_module_v0_v0

## Files

- **Recipe:** `kb/recipes/recipe_ai_processor_module_v0_v0.yaml`
- **Target item:** `ai_processor_module_v0`
  - File: `kb/items/ai_processor_module_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'ai_processor_module_assembly_v0') requires input 'microcontroller_unit_v0' which is not available

**Location:** Step 0
**Process:** `ai_processor_module_assembly_v0`
  - File: `kb/processes/ai_processor_module_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: ai_processor_module_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_ai_processor_module_v0_v0.yaml`
- **BOM available:** No
