# GitHub Issue: Add Recipe Step Input Satisfaction Validation (ADR-019 Amendment)

## Title
Add validation for recipe step input satisfaction (ADR-019 amendment)

## Labels
- `enhancement`
- `validation`
- `ADR-019`
- `indexer`
- `high-priority`

## Problem Statement

During simulation testing (sim: `echo_genesis_934`, 2026-01-02), multiple recipes failed because their process steps require inputs that are neither:
1. Produced by previous steps in the recipe, nor
2. Listed in the recipe's explicit inputs

This means the recipe assumes materials exist in inventory but doesn't declare this assumption, making recipes incomplete and unrunnable from a clean state.

### Examples of Broken Recipes

**Example 1: `recipe_anorthite_ore_v0`**

Current definition:
```yaml
id: recipe_anorthite_ore_v0
kind: recipe
target_item_id: anorthite_ore
variant_id: v0
steps:
  - process_id: beneficiation_magnetic_basic_v0
  - process_id: regolith_screening_sieving_v0
notes: |
  Extract anorthite ore from lunar highland regolith.
```

**What happened:**
```
$ python -m src.cli sim run-recipe --sim-id echo_genesis_934 --recipe recipe_anorthite_ore_v0
✗ Failed to run recipe: Recipe recipe_anorthite_ore_v0 has no inputs (neither explicit, nor inferred from steps, nor from BOM)
```

**Analysis:**
- Step 1 (`beneficiation_magnetic_basic_v0`) requires input: `regolith_powder` (1.0 kg)
- Step 2 (`regolith_screening_sieving_v0`) requires input: `regolith_lunar_mare` (1.0 kg)
- Neither input is:
  - ✗ Produced by a previous step
  - ✗ Listed in recipe's explicit inputs
  - ✗ Available in BOM (no BOM for anorthite_ore)
- Additionally, the steps don't chain: Step 2's outputs (`regolith_coarse_fraction`, `regolith_fine_fraction`) don't match Step 1's input (`regolith_powder`)

**Example 2: `recipe_machine_frame_small_v0`**

Current definition:
```yaml
id: recipe_machine_frame_small_v0
target_item_id: machine_frame_small
variant_id: v0
steps:
  - process_id: metal_cutting_basic_v0
    est_time_hr: 1.0
    machine_hours: 1.0
  - process_id: welding_and_fabrication_v0
    est_time_hr: 3.0
    labor_hours: 3.0
  - process_id: machining_finish_basic_v0
    est_time_hr: 1.5
    machine_hours: 1.5
```

**What happened:**
```
$ python -m src.cli sim run-recipe --sim-id echo_genesis_934 --recipe recipe_machine_frame_small_v0
✗ Failed to run recipe: Recipe recipe_machine_frame_small_v0 has no inputs (neither explicit, nor inferred from steps, nor from BOM)
```

**Analysis:**
- Steps reference generic processes that work on various materials
- The recipe doesn't specify WHICH materials to use (steel plate? aluminum stock? steel tubing?)
- No explicit inputs defined
- No BOM exists for `machine_frame_small`

### Counter-Example: Well-Formed Recipe

**Example 3: `recipe_robot_arm_link_aluminum_v0`** (GOOD)

```yaml
id: recipe_robot_arm_link_aluminum_v0
kind: recipe
target_item_id: robot_arm_link_aluminum
variant_id: v0
inputs:
  - item_id: aluminum_alloy_ingot
    qty: 9.0
    unit: kg
    notes: Aluminum alloy for casting or forming link structure
outputs:
  - item_id: robot_arm_link_aluminum
    qty: 1.0
    unit: unit
steps:
  - process_id: metal_casting_basic_v0
    notes: Cast aluminum link blank
  - process_id: machining_finish_basic_v0
    notes: CNC machine mounting surfaces and cable channels
  - process_id: inspection_basic_v0
    notes: Verify dimensions and structural integrity
```

**Why this works:**
- ✅ Explicit input: `aluminum_alloy_ingot` (9.0 kg) declared at recipe level
- ✅ All process steps can access this input from inventory
- ✅ Recipe is self-contained and runnable from clean state

## Proposed Solution

### Validation Rule: `recipe_step_input_not_satisfied`

Add a new validation rule that checks every step in a recipe to ensure all required inputs are satisfied.

**For each step in a recipe:**
1. Determine all inputs required by the step:
   - From step-level input overrides, OR
   - From the process definition's inputs
2. For each required input, verify it comes from ONE of:
   - **Previous step output**: An output of any previous step (N-1, N-2, ..., step 1)
   - **Recipe explicit input**: Listed in the recipe's `inputs` field
   - **BOM component**: If recipe has `target_item_id`, check BOM (ADR-019 existing behavior)
3. If an input is not satisfied by any of the above: **ENQUEUE WORK**

**Validation Level:**
- **ERROR**: Step input required but not satisfied
- Enqueue as gap type: `recipe_step_input_not_satisfied`

### Implementation Requirements

**1. Indexer Validation (`src/kb_core/validators.py`)**

Add function: `validate_recipe_step_inputs(recipe, kb) -> List[ValidationIssue]`

**Algorithm:**
```python
def validate_recipe_step_inputs(recipe, kb):
    issues = []
    accumulated_outputs = set()  # Outputs from previous steps
    recipe_inputs = {inp['item_id'] for inp in recipe.get('inputs', [])}

    # Add BOM components to available inputs (ADR-019)
    if target_item_id := recipe.get('target_item_id'):
        if bom := kb.get_bom(target_item_id):
            recipe_inputs.update(comp['item_id'] for comp in bom.get('components', []))

    for step_idx, step in enumerate(recipe.get('steps', [])):
        # Get required inputs for this step
        step_inputs = get_step_required_inputs(step, kb)  # Helper function

        for inp in step_inputs:
            item_id = inp['item_id']

            # Check if satisfied
            if item_id not in accumulated_outputs and item_id not in recipe_inputs:
                issues.append(ValidationIssue(
                    level=ValidationLevel.ERROR,
                    category="recipe",
                    rule="recipe_step_input_not_satisfied",
                    entity_id=recipe['id'],
                    message=f"Step {step_idx+1} ({step.get('process_id')}) requires input '{item_id}' which is not produced by previous steps nor listed in recipe inputs",
                    fix_hint=f"Add '{item_id}' to recipe inputs, or ensure a previous step produces it"
                ))

        # Accumulate outputs from this step for next steps
        step_outputs = get_step_outputs(step, kb)  # Helper function
        accumulated_outputs.update(out['item_id'] for out in step_outputs)

    return issues
```

**2. Work Queue Integration**

When validation finds `recipe_step_input_not_satisfied`:
- Enqueue to `out/work_queue.jsonl`
- Gap type: `recipe_step_input_not_satisfied`
- Context: Include step number, required input, and suggestions

**3. Test Cases**

Must pass these tests before issue is resolved:

**Test 1: Detect broken recipe with no inputs**
```python
def test_recipe_anorthite_ore_v0_validation():
    """recipe_anorthite_ore_v0 should fail validation"""
    recipe = load_recipe("recipe_anorthite_ore_v0")
    issues = validate_recipe_step_inputs(recipe, kb)

    # Should have errors for unsatisfied inputs
    assert any(
        issue.rule == "recipe_step_input_not_satisfied"
        and "regolith_powder" in issue.message
        for issue in issues
    )
    assert any(
        issue.rule == "recipe_step_input_not_satisfied"
        and "regolith_lunar_mare" in issue.message
        for issue in issues
    )
```

**Test 2: Detect recipe with generic processes needing explicit inputs**
```python
def test_recipe_machine_frame_small_v0_validation():
    """recipe_machine_frame_small_v0 should fail validation"""
    recipe = load_recipe("recipe_machine_frame_small_v0")
    issues = validate_recipe_step_inputs(recipe, kb)

    # Should have error for unsatisfied inputs in first step
    assert any(
        issue.rule == "recipe_step_input_not_satisfied"
        for issue in issues
    )
```

**Test 3: Accept well-formed recipe with explicit inputs**
```python
def test_recipe_robot_arm_link_aluminum_v0_validation():
    """recipe_robot_arm_link_aluminum_v0 should pass validation"""
    recipe = load_recipe("recipe_robot_arm_link_aluminum_v0")
    issues = validate_recipe_step_inputs(recipe, kb)

    # Should NOT have step input satisfaction errors
    assert not any(
        issue.rule == "recipe_step_input_not_satisfied"
        for issue in issues
    )
```

**Test 4: Accept recipe where step N+2 uses output from step N**
```python
def test_recipe_with_non_sequential_dependencies():
    """Recipe where step 3 uses output from step 1 (skipping step 2)"""
    recipe = {
        'id': 'test_recipe',
        'inputs': [],
        'steps': [
            {'process_id': 'process_a'},  # outputs: item_x
            {'process_id': 'process_b'},  # outputs: item_y
            {'process_id': 'process_c'}   # needs: item_x (from step 1)
        ]
    }
    issues = validate_recipe_step_inputs(recipe, kb)

    # Should pass - step 3 can use output from step 1
    assert not any(
        issue.rule == "recipe_step_input_not_satisfied"
        and "item_x" in issue.message
        for issue in issues
    )
```

**Test 5: Accept recipe using BOM inputs (ADR-019)**
```python
def test_recipe_with_bom_inputs():
    """Recipe with target_item_id and BOM should use BOM as inputs"""
    recipe = load_recipe("recipe_machine_labor_bot_general_v0")
    issues = validate_recipe_step_inputs(recipe, kb)

    # Should NOT have step input satisfaction errors
    # (BOM provides the inputs)
    assert not any(
        issue.rule == "recipe_step_input_not_satisfied"
        for issue in issues
    )
```

## Expected Outcomes

**After implementation:**

1. **Indexer run identifies broken recipes:**
   ```
   $ python -m src.cli index
   Found 47 validation issues (15 errors, 32 warnings)
   ERROR: recipe_anorthite_ore_v0: Step 1 requires 'regolith_powder' (not satisfied)
   ERROR: recipe_machine_frame_small_v0: Step 1 requires input materials (not satisfied)
   ...
   ```

2. **Work queue populated:**
   ```
   $ python -m src.cli queue ls
   recipe_step_input_not_satisfied: 15 items
   ```

3. **Recipes can be fixed by:**
   - Adding explicit `inputs:` field
   - Reorganizing steps to produce required inputs
   - Removing incompatible process steps

## Related

- **ADR-019**: BOM-Recipe Relationship and Input Inference
- **ADR-018**: Recipe Inputs/Outputs Validation
- **Simulation**: `echo_genesis_934` (Labor Bot ISRU Manufacturing Test)
- **Issue List**: `simulations/echo_genesis_934/issues_found.md`

## Acceptance Criteria

- [ ] Validation function implemented in `src/kb_core/validators.py`
- [ ] All 5 test cases pass
- [ ] Indexer detects broken recipes and enqueues work
- [ ] Work queue entries created for `recipe_step_input_not_satisfied`
- [ ] Documentation updated in ADR-019
- [ ] At least 2 example broken recipes fixed to verify workflow
