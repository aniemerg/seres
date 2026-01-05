# Fix Intelligence: recipe_potted_electronic_assembly_v0

## Files

- **Recipe:** `kb/recipes/recipe_potted_electronic_assembly_v0.yaml`
- **Target item:** `potted_electronic_assembly`
  - File: `kb/items/potted_electronic_assembly.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'electronic_assembly_v0') requires input 'pcb_populated' which is not available

**Location:** Step 0
**Process:** `electronic_assembly_v0`
  - File: `kb/processes/electronic_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: electronic_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'potting_and_encapsulation_v0') requires input 'potting_compound' which is not available

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
- **Recipe file:** `kb/recipes/recipe_potted_electronic_assembly_v0.yaml`
- **BOM available:** No
