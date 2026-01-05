# Fix Intelligence: recipe_circuit_breaker_assembled_v0

## Files

- **Recipe:** `kb/recipes/recipe_circuit_breaker_assembled_v0.yaml`
- **Target item:** `circuit_breaker_assembled`
  - File: `kb/items/circuit_breaker_assembled.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'assembly_process_general_v0') requires input 'housing_with_contacts' which is not available

**Location:** Step 0
**Process:** `assembly_process_general_v0`
  - File: `kb/processes/assembly_process_general_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_process_general_v0
  inputs:
  - item_id: housing_with_contacts
    qty: 0.1
    unit: kg
  - item_id: bimetallic_element
    qty: 0.04
    unit: kg
  - item_id: spring_compression_small
    qty: 1.0
    unit: each
  - item_id: plastic_housing_molded
    qty: 0.05
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `housing_with_contacts` not found

This item doesn't exist in the KB.

#### Problem: Item `bimetallic_element` not found

This item doesn't exist in the KB.

#### Problem: Item `spring_compression_small` not found

This item doesn't exist in the KB.

#### Problem: Item `plastic_housing_molded` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_circuit_breaker_assembled_v0.yaml`
- **BOM available:** No
