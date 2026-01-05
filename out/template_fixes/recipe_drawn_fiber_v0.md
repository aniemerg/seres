# Fix Intelligence: recipe_drawn_fiber_v0

## Files

- **Recipe:** `kb/recipes/recipe_drawn_fiber_v0.yaml`
- **Target item:** `drawn_fiber`
  - File: `kb/items/drawn_fiber.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'glass_melting_v0') requires input 'glass_batch_mix' which is not available

**Location:** Step 0
**Process:** `glass_melting_v0`
  - File: `kb/processes/glass_melting_v0.yaml`

**Current step:**
```yaml
- process_id: glass_melting_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'fiber_drawing_basic_v0') requires input 'molten_material_or_preform' which is not available

**Location:** Step 1
**Process:** `fiber_drawing_basic_v0`
  - File: `kb/processes/fiber_drawing_basic_v0.yaml`

**Current step:**
```yaml
- process_id: fiber_drawing_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'annealing_v0') requires input 'material_unannealed' which is not available

**Location:** Step 2
**Process:** `annealing_v0`
  - File: `kb/processes/annealing_v0.yaml`

**Current step:**
```yaml
- process_id: annealing_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_drawn_fiber_v0.yaml`
- **BOM available:** No
