# ADR 005 — Recipe Step Processing and Hybrid Process Model

**Status:** ✅ IMPLEMENTED (Phase 1)
**Date:** 2025-12-21 (Proposed) → 2025-12-21 (Phase 1 Implemented)
**Owner:** base_builder/sim_engine.py

## Context / Problem

The knowledge base has two levels of production modeling:
1. **Processes** (`kb/processes/*.yaml`) - Unit operations with inputs, outputs, machine requirements
2. **Recipes** (`kb/recipes/*.yaml`) - Multi-step production sequences that produce items

**Current state:**
- Recipes have `steps:` field listing process IDs from the original design (memo_a.md)
- Recipe steps already include inline overrides (`est_time_hr`, `machine_hours`, `notes`)
- BUT: `sim_engine.run_recipe()` completely ignores the `steps:` field
- Only checks optional `required_machines` at recipe level (which most recipes lack)
- Uses recipe-level `inputs`/`outputs`/`duration` directly

**Problems identified:**
1. **Machine requirements not enforced** - Ran motor production without stamping press, winding machine, etc.
2. **Process definitions unused** - Processes define `requires_ids` and `resource_requirements`, but simulation doesn't check them
3. **Design vs implementation mismatch** - memo_a.md specifies `steps: ordered list of process ids` but implementation ignores this
4. **Duplicate data** - Both recipe and processes define inputs/outputs, leading to inconsistency potential

**Example of current gap:**
```yaml
# kb/recipes/recipe_drive_motor_medium_v1.yaml
inputs:  # Used by sim_engine
  - item_id: stator_rotor_lamination_set
    qty: 36.0
outputs:  # Used by sim_engine
  - item_id: drive_motor_medium
    qty: 1.0
steps:  # IGNORED by sim_engine
  - process_id: lamination_stamping_v0  # Requires stamping_press_basic (not checked!)
  - process_id: coil_winding_basic_v0   # Requires coil_winding_machine (not checked!)
```

## Decision / Direction

Implement **hybrid process model** where recipe steps can:
1. **Reference processes** (primary) - Inherit from process definition with optional overrides
2. **Inline processes** (rare) - Define everything directly for one-off steps

### Step Resolution Semantics

```python
def resolve_step(step_def, kb):
    """
    Resolve a recipe step to a fully-specified process instance.

    Returns: {
        'inputs': [...],
        'outputs': [...],
        'byproducts': [...],
        'requires_ids': [...],
        'resource_requirements': [...],
        'energy_model': {...},
        'time_model': {...},
    }
    """
    if 'process_id' in step_def:
        # Reference mode: Load base process and apply overrides
        base_process = kb.get_process(step_def['process_id'])

        # Merge: step fields override process fields
        resolved = deep_merge(base_process, step_def)

    else:
        # Inline mode: Step IS the process definition
        resolved = step_def

    # Validate required fields present
    validate_required_fields(resolved, [
        'inputs', 'outputs', 'requires_ids'
    ])

    return resolved
```

### Override Fields Supported

Step-level fields that override/augment process definitions:

| Field | Behavior |
|-------|----------|
| `scale` | Multiply all quantities (inputs, outputs, time) |
| `inputs_override` | Replace specific input items/quantities |
| `outputs_override` | Replace specific output items/quantities |
| `est_time_hr` | Override estimated time |
| `machine_hours` | Override machine time requirement |
| `labor_hours` | Override labor time requirement |
| `notes` | Add recipe-specific context |
| Direct fields (`inputs`, `outputs`, etc.) | Full replacement (for inline mode) |

### Recipe Processing Algorithm

```python
def run_recipe(recipe_id, quantity):
    recipe = kb.get_recipe(recipe_id)

    # Step 1: Resolve all steps to process instances
    resolved_steps = [resolve_step(step, kb) for step in recipe['steps']]

    # Step 2: Aggregate requirements across all steps
    all_required_machines = set()
    total_machine_hours = {}
    total_energy = 0

    for step in resolved_steps:
        all_required_machines.update(step.get('requires_ids', []))

        for req in step.get('resource_requirements', []):
            machine_id = req['machine_id']
            hours = req['qty']
            total_machine_hours[machine_id] = total_machine_hours.get(machine_id, 0) + hours

        if 'energy_model' in step:
            total_energy += calculate_energy(step['energy_model'], step['inputs'])

    # Step 3: Check machine availability
    for machine_id in all_required_machines:
        if machine_id not in state.machines_built:
            if not has_item(machine_id, 1, 'count'):
                return error(f"Required machine '{machine_id}' not available")

    # Step 4: Process material flows
    # Use recipe-level inputs/outputs if present (current behavior)
    # OR aggregate from steps (future enhancement)
    if 'inputs' in recipe and 'outputs' in recipe:
        # Current simplified model: recipe defines aggregate I/O
        process_materials(recipe['inputs'], recipe['outputs'])
    else:
        # Future: Execute steps sequentially, tracking intermediates
        for step in resolved_steps:
            process_materials(step['inputs'], step['outputs'])

    # Step 5: Calculate duration
    total_duration = sum(calculate_duration(step) for step in resolved_steps)

    # Step 6: Create active process and log
    create_active_process(recipe_id, total_duration, ...)
```

### Three Modes of Recipe Definition

**Mode 1: Reference-based (most common)**
```yaml
# Reuse process definitions, minimal recipe overhead
steps:
  - process_id: lamination_stamping_v0
  - process_id: coil_winding_basic_v0
  - process_id: motor_assembly_v0
```

**Mode 2: Reference with overrides**
```yaml
# Customize specific aspects for this recipe
steps:
  - process_id: lamination_stamping_v0
    scale: 2.0  # Double the batch size
  - process_id: coil_winding_basic_v0
    est_time_hr: 15.0  # Override time estimate
    inputs_override:
      - item_id: copper_wire  # Use copper instead of aluminum
        qty: 30.0
```

**Mode 3: Fully inline (rare, one-off processes)**
```yaml
# Define everything inline when no reusable process exists
steps:
  - name: "Custom motor winding for prototype"
    inputs:
      - item_id: exotic_wire_alloy
        qty: 5.0
        unit: kg
    outputs:
      - item_id: prototype_coil
        qty: 4.5
        unit: kg
    requires_ids:
      - experimental_winding_station
    resource_requirements:
      - machine_id: experimental_winding_station
        qty: 20.0
        unit: hr
    time_model:
      type: fixed_time
      hours: 20.0
```

## Design Philosophy

### Process = Vocabulary, Recipe = Sentence

- **Processes** are reusable unit operation templates (like words)
- **Steps** are contextualized instances (like words in a sentence)
- **Recipes** compose steps into production sequences (like sentences)

Inline steps are "anonymous processes" (like lambda functions in code) - useful for one-offs but not the norm.

### Hierarchy Principle

```
Process Definition (kb/processes/)
    ↓ (inherits from)
Recipe Step (kb/recipes/...steps[])
    ↓ (optionally overrides)
Runtime Process Instance (sim_engine)
```

This follows CSS semantics:
- Class definition (process)
- Element with class + inline styles (step with process_id + overrides)
- Fully inline element (step without process_id)

### Does This Damage the Process Abstraction?

**No**, if we maintain clear semantics:
1. Processes remain the primary abstraction (90%+ of steps should reference them)
2. Overrides are explicitly marked (clear which fields are customized)
3. Inline steps are discouraged unless necessary (linter could flag them)
4. Process reusability is preserved (can still analyze "all uses of process X")

The flexibility helps with:
- Recipe-specific scaling
- Prototyping new processes before generalizing
- Handling variations without creating process proliferation

## Implementation Plan

### Phase 1: Process step resolution (required for machine checking) ✅ COMPLETE
- [x] Implement `resolve_step(step_def, kb)` function
- [x] Aggregate `requires_ids` from all steps
- [x] Check machine availability before running recipe
- [x] **Hard enforcement: Fail recipe if required machines missing** (originally planned as soft enforcement, changed to hard enforcement for data integrity)

### Phase 2: Resource and energy accounting
- [ ] Aggregate `resource_requirements` (machine-hours)
- [ ] Track machine utilization in simulation state
- [ ] Calculate energy consumption from `energy_model`
- [ ] Add to simulation reports

### Phase 3: Sequential step execution (optional future enhancement)
- [ ] Execute steps sequentially instead of treating recipe as black box
- [ ] Track intermediate materials between steps
- [ ] Enable step-level debugging/inspection
- [ ] Support parallel step execution where dependencies allow

## Consequences

### Positive
- **Machine requirements enforced** - Can't run processes without required machines
- **Design compliance** - Implements original intent from memo_a.md
- **Flexibility** - Can customize processes per recipe when needed
- **Reusability** - Processes remain DRY and centralized
- **Better simulation** - Tracks machine utilization, energy, real time estimates

### Negative
- **Complexity** - Two modes (reference vs inline) to understand
- **Migration** - Existing recipes might need updates
- **Validation** - More complex validation logic needed
- **Performance** - Step resolution adds overhead (mitigated by caching)

### Neutral
- **Backward compatible** - Can implement incrementally (Phase 1 doesn't break existing recipes)
- **Documentation burden** - Need clear examples and guidelines for when to inline vs reference

## Related ADRs
- [ADR-003: Process-Machine Refactor](003-process-machine-refactor.md) - Established process vs machine distinction
- [ADR-004: Base Builder Simulation](004-base-builder-simulation.md) - Simulation framework this enhances

## Implementation Notes (2025-12-21)

### Phase 1 Implementation Details

**Files Modified:**
- `base_builder/sim_engine.py`:
  - Added `resolve_step(step_def)` method (lines 316-375)
  - Updated `run_recipe()` to resolve steps and check machines (lines 397-447)

**Key Implementation Decisions:**

1. **Hard Enforcement Adopted**: Initially planned soft enforcement (warnings only), but changed to hard enforcement during implementation. Recipes now fail immediately if required machines are unavailable.
   - **Rationale**: Data integrity and realistic simulation trumps convenience. Forces KB completeness.
   - **Consequence**: Existing simulations may break until machines are added/imported.

2. **Hybrid Resolution**: Steps can reference processes OR define inline, with override support via `scale` parameter and direct field replacement.

3. **Legacy Support**: Still checks `required_machines` at recipe level for backward compatibility.

4. **Error Format**: Returns structured error with `missing_machines` list for programmatic handling.

**Testing:**
- Verified machine checking with `recipe_stator_rotor_lamination_set_v0` (requires `stamping_press_basic`)
- Verified machine checking with `recipe_motor_coil_wound_v0` (requires `coil_winding_machine`)
- Recipe execution now fails with clear error message when machines unavailable

### Next Steps
- Phase 2: Resource and energy accounting (aggregate machine-hours, track utilization)
- Phase 3: Sequential step execution (track intermediates between steps)

## References
- `design/memo_a.md` - Original design specifying `steps: ordered list of process ids`
- `base_builder/sim_engine.py:316-447` - `resolve_step()` and updated `run_recipe()` implementation
- `kb/processes/lamination_stamping_v0.yaml` - Example process with `requires_ids`
- `kb/recipes/recipe_drive_motor_medium_v1.yaml` - Example recipe with steps
