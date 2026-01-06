# Fix Intelligence: recipe_hv_rectifier_stack_v0

## Files

- **Recipe:** `kb/recipes/recipe_hv_rectifier_stack_v0.yaml`
- **Target item:** `hv_rectifier_stack`
  - File: `kb/items/hv_rectifier_stack.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'electronics_assembly_v0') requires input 'pcb_populated' which is not available

**Location:** Step 0
**Process:** `electronics_assembly_v0`
  - File: `kb/processes/electronics_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: electronics_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'potting_and_encapsulation_v0') requires input 'electronic_assembly' which is not available

**Location:** Step 1
**Process:** `potting_and_encapsulation_v0`
  - File: `kb/processes/potting_and_encapsulation_v0.yaml`

**Current step:**
```yaml
- process_id: potting_and_encapsulation_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_hv_rectifier_stack_v0.yaml`
- **BOM available:** No
