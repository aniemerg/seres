# `sim plan` Crashes When Item Has No Mass Defined

## Problem

The `sim plan` command crashes with a `TypeError` when planning a recipe whose target item has no `mass` field defined. This prevents users from using the planning tool to understand dependencies.

## Observed Behavior

During simulation `echo_genesis_934` (2026-01-02):

```bash
$ python -m src.cli sim plan --recipe recipe_anorthite_ore_v0

Error: unsupported format string passed to NoneType.__format__
Traceback (most recent call last):
  File "/Users/allanniemerg/dev2/self-replicating-system-modeling/src/cli.py", line 241, in main
    return run_sim_command(args, kb_loader)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/allanniemerg/dev2/self-replicating-system-modeling/src/simulation/cli.py", line 954, in run_sim_command
    return handler(args, kb_loader)
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/allanniemerg/dev2/self-replicating-system-modeling/src/simulation/cli.py", line 546, in cmd_plan
    print(f"TARGET: {target_item_id} (1 unit, {target_mass:.2f} kg)")
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: unsupported format string passed to NoneType.__format__
================================================================================
PRODUCTION PLAN: Anorthite ore
================================================================================
```

## Root Cause

**File**: `src/simulation/cli.py`
**Line**: 546
**Code**:
```python
print(f"TARGET: {target_item_id} (1 unit, {target_mass:.2f} kg)")
```

The `target_mass` variable is `None` because the item `anorthite_ore` doesn't have a `mass` field defined in its YAML file. The f-string format specifier `.2f` expects a number, not `None`.

## Expected Behavior

The command should handle missing mass gracefully:

**Option 1: Skip mass display**
```
================================================================================
PRODUCTION PLAN: Anorthite ore
================================================================================

TARGET: anorthite_ore (1 unit)

DEPENDENCY TREE:
...
```

**Option 2: Show "unknown mass"**
```
================================================================================
PRODUCTION PLAN: Anorthite ore
================================================================================

TARGET: anorthite_ore (1 unit, mass unknown)

DEPENDENCY TREE:
...
```

**Option 3: Use fallback format**
```
================================================================================
PRODUCTION PLAN: Anorthite ore
================================================================================

TARGET: anorthite_ore (1 unit, ~?.?? kg)

DEPENDENCY TREE:
...
```

## Impact

**Severity**: Medium (Crash / UX)

**Impact**:
- Users cannot use `sim plan` for items without mass data
- Blocks understanding of dependencies for affected recipes
- Provides poor user experience (crash instead of graceful degradation)
- Forces users to manually check KB files to understand dependencies

**Affected Items**:
Any item without a `mass` field. Examples from KB:
- `anorthite_ore` - no mass defined
- Various intermediate materials
- Abstract/template items

## Proposed Solutions

### Option A: Conditional Format (Recommended)

```python
# src/simulation/cli.py, line ~546
if target_mass is not None:
    print(f"TARGET: {target_item_id} (1 unit, {target_mass:.2f} kg)")
else:
    print(f"TARGET: {target_item_id} (1 unit, mass unknown)")
```

**Pros**:
- Simple, clear fix
- Informative to user
- No crashes

### Option B: Use Format Specifier with Default

```python
# src/simulation/cli.py, line ~546
mass_str = f"{target_mass:.2f} kg" if target_mass is not None else "unknown"
print(f"TARGET: {target_item_id} (1 unit, {mass_str})")
```

**Pros**:
- Slightly more flexible
- Easier to add other fallbacks later

### Option C: Comprehensive None Handling

Add a helper function for safe formatting:

```python
def format_mass(mass: Optional[float]) -> str:
    """Format mass with fallback for None."""
    if mass is None:
        return "unknown"
    return f"{mass:.2f} kg"

# Usage:
print(f"TARGET: {target_item_id} (1 unit, {format_mass(target_mass)})")
```

**Pros**:
- Reusable for other display code
- Consistent formatting throughout codebase

## Implementation Tasks

- [ ] Fix crash in `src/simulation/cli.py` line 546
- [ ] Check for other f-string format crashes (grep for `.2f`, `.1f` on potentially-None variables)
- [ ] Add test case for `sim plan` with missing mass
- [ ] Consider adding validation warning for items missing mass (optional)

## Test Cases

**Test 1: Recipe with target item missing mass**
```python
def test_sim_plan_missing_mass():
    """sim plan should not crash when item has no mass"""
    result = run_cli_command([
        "sim", "plan",
        "--recipe", "recipe_anorthite_ore_v0"
    ])

    assert result.exit_code == 0
    assert "mass unknown" in result.output or "anorthite_ore (1 unit)" in result.output
```

**Test 2: Recipe with target item having mass**
```python
def test_sim_plan_with_mass():
    """sim plan should show mass when available"""
    result = run_cli_command([
        "sim", "plan",
        "--recipe", "recipe_robot_arm_link_aluminum_v0"
    ])

    assert result.exit_code == 0
    assert "8.00 kg" in result.output  # Expected mass
```

**Test 3: Process with missing mass**
```python
def test_sim_plan_process_missing_mass():
    """sim plan for process should handle missing output mass"""
    result = run_cli_command([
        "sim", "plan",
        "--process", "alumina_crude_extraction_v0"
    ])

    assert result.exit_code == 0
    # Should not crash
```

## Related Crashes to Check

Search for similar format string crashes:

```bash
# Find all .2f, .1f format strings that might crash on None
grep -n "{\w\+:.2f}" src/simulation/cli.py
grep -n "{\w\+:.1f}" src/simulation/cli.py
grep -n "{\w\+:d}" src/simulation/cli.py
```

Ensure all numeric format strings have None checks.

## Acceptance Criteria

- [ ] `sim plan` does not crash when item has no mass
- [ ] Output clearly indicates when mass is unknown
- [ ] All three test cases pass
- [ ] Other format string crashes identified and fixed (if any)
- [ ] Code review for similar issues in other display functions

## Related

- **Simulation**: `echo_genesis_934` (Labor Bot ISRU Manufacturing Test)
- **Related Issue**: #2 (Import Mass Calculation)
- **File**: `src/simulation/cli.py` line 546
