# Integration Testing Instructions - Phase 4.4

**Context:** The KB has been fully migrated to ADR-012/014/017 schemas. All validation errors are resolved. The simulation engine has been rebuilt with new models. We need to verify everything works correctly end-to-end.

**Your Task:** Perform integration testing to verify the simulation works correctly with the migrated KB.

## Before You Start

**Required Reading:**
1. `docs/SIMULATION_GUIDE.md` - Complete simulation guide
2. `docs/CLI_COMMANDS_GUIDE.md` - CLI reference
3. `docs/ADRs/ADR-012-process-types-and-time-model.md` - Time model spec
4. `docs/ADRs/ADR-014-energy-model-redesign.md` - Energy model spec
5. `docs/ADRs/ADR-017-validation-and-error-detection.md` - Validation spec

**Current Status:**
- ✅ Simulation engine implemented (`src/simulation/engine.py`)
- ✅ Simulation CLI implemented (`src/simulation/cli.py`)
- ✅ KB fully migrated (0 validation errors)
- ✅ All 93 work queue items resolved

## Testing Tasks

### Task 1: Manual Bootstrap Simulation (30 min)

Run a complete bootstrap scenario manually to verify basic functionality.

**Steps:**

```bash
# 1. Create test simulation
python -m src.cli sim init --sim-id integration_test

# 2. Import bootstrap items
python -m src.cli sim import --sim-id integration_test --item labor_bot_general_v0 --quantity 2 --unit unit

# 3. Start mining process (should calculate energy)
python -m src.cli sim start-process --sim-id integration_test --process regolith_mining_highlands_v0 --duration 24

# 4. Preview advancement
python -m src.cli sim preview --sim-id integration_test --hours 24

# 5. Advance time
python -m src.cli sim advance-time --sim-id integration_test --hours 24

# 6. View state
python -m src.cli sim view-state --sim-id integration_test
```

**Expected Results:**
- Mining process completes after 24 hours
- Energy calculated (should be ~50 kWh based on process energy_model)
- Regolith added to inventory (~100 kg)
- No errors or warnings

**Verify:**
- [ ] Process starts successfully
- [ ] Energy calculation works
- [ ] Time advancement works
- [ ] Outputs added to inventory
- [ ] Event log created at `simulations/integration_test/simulation.jsonl`

### Task 2: Test Calculated Duration (15 min)

Test the engine's ability to calculate duration from time_model.

```bash
# Start a process WITHOUT providing duration - engine should calculate it
python -m src.cli sim start-process --sim-id integration_test --process crushing_basic_v0
```

**Expected Results:**
- Engine calculates duration from process `time_model`
- Output shows "Duration: X.XX hours (calculated)"
- Process starts successfully

**Verify:**
- [ ] Duration calculated correctly (check against process time_model)
- [ ] No errors about missing duration

### Task 3: Test Recipe Execution (20 min)

Test recipe execution with override resolution.

```bash
# Find a recipe with time_model overrides
grep -l "time_model:" kb/recipes/*.yaml | head -1

# Run the recipe
python -m src.cli sim run-recipe --sim-id integration_test --recipe <recipe_id>
```

**Verify:**
- [ ] Recipe steps execute sequentially
- [ ] Overrides applied correctly
- [ ] Total duration calculated
- [ ] All outputs produced

### Task 4: Test Machine Building (15 min)

Test BOM-based machine construction.

```bash
# Import parts for a simple machine
python -m src.cli sim import --sim-id integration_test --item steel_plate --quantity 50 --unit kg
# (import other parts as needed)

# Build machine
python -m src.cli sim build-machine --sim-id integration_test --machine crusher_basic_v0
```

**Verify:**
- [ ] Parts consumed from inventory
- [ ] Machine added to machines_built list
- [ ] No time advancement (instant build)

### Task 5: Run Closure Analysis (10 min)

Verify closure analysis works with migrated KB.

```bash
# Analyze specific machine
python -m src.cli closure --machine crusher_basic_v0

# Analyze all machines
python -m src.cli closure --all --output out/closure_test.txt
```

**Verify:**
- [ ] Analysis completes without errors
- [ ] Raw materials identified correctly
- [ ] Imported items identified correctly
- [ ] ISRU percentage calculated
- [ ] No unresolved items (or documented if expected)

### Task 6: Verify Calculations (30 min)

Spot-check that calculations are correct.

**Pick 3 processes with different characteristics:**
1. Continuous process with linear_rate time model
2. Batch process with batch time model
3. Process with per_unit energy model

**For each process:**

```bash
# Validate it first
python -m src.cli validate --id process:<process_id>

# Read the process YAML
cat kb/processes/<process_id>.yaml

# Start it in simulation
python -m src.cli sim start-process --sim-id integration_test --process <process_id> --duration <X>
python -m src.cli sim advance-time --sim-id integration_test --hours <X>
```

**Manually verify:**
- [ ] Duration calculation matches time_model spec
- [ ] Energy calculation matches energy_model spec
- [ ] Units converted correctly
- [ ] Scaling_basis applied correctly

**Document findings in `out/calculation_verification.md`**

### Task 7: Create Automated Tests (2-3 hours)

Create pytest integration tests to prevent regressions.

**File:** `test/integration/test_kb_migration.py`

**Tests to create:**

```python
def test_process_with_linear_rate_time_model():
    """Test duration calculation for continuous process."""
    # Load process with linear_rate
    # Calculate expected duration
    # Start process in sim
    # Verify duration matches expected

def test_process_with_batch_time_model():
    """Test duration calculation for batch process."""
    # Similar structure

def test_energy_calculation_per_unit():
    """Test energy calculation with per_unit model."""
    # Load process with per_unit energy
    # Calculate expected energy
    # Run process
    # Verify energy matches expected

def test_energy_calculation_fixed_per_batch():
    """Test energy calculation with fixed_per_batch model."""
    # Similar structure

def test_recipe_with_complete_override():
    """Test recipe step with complete time_model override."""
    # Load recipe with complete override (has 'type' field)
    # Verify override used instead of process time_model

def test_recipe_with_partial_override():
    """Test recipe step with partial time_model override."""
    # Load recipe with partial override (no 'type' field)
    # Verify merged with process time_model

def test_full_bootstrap_chain():
    """Test complete production chain from regolith to parts."""
    # Create sim
    # Import labor bots
    # Mine regolith
    # Process ore
    # Smelt metal
    # Make parts
    # Verify inventory at each step
```

**File:** `test/integration/test_end_to_end.py`

**Tests to create:**

```python
def test_simulation_lifecycle():
    """Test complete simulation lifecycle."""
    # Create sim
    # Import items
    # Start processes
    # Advance time
    # Build machine
    # Verify state
    # Load from disk
    # Verify persistence

def test_validation_at_runtime():
    """Test that runtime validation catches errors."""
    # Try to start process with validation errors
    # Verify it fails with helpful message

def test_closure_analysis_integration():
    """Test closure analysis with real KB."""
    # Run closure on several machines
    # Verify results reasonable
    # Check for infinite loops
```

**Run tests:**
```bash
pytest test/integration/test_kb_migration.py -v
pytest test/integration/test_end_to_end.py -v
```

### Task 8: Document Findings (30 min)

Create a test report at `out/integration_test_report.md`:

**Template:**

```markdown
# Integration Testing Report - Phase 4.4

**Date:** YYYY-MM-DD
**Tester:** [Your name/agent name]

## Summary

- Total tests run: X
- Passed: X
- Failed: X
- Warnings: X

## Manual Testing Results

### Bootstrap Simulation
- [ ] PASS / FAIL
- Notes: ...

### Calculated Duration
- [ ] PASS / FAIL
- Notes: ...

### Recipe Execution
- [ ] PASS / FAIL
- Notes: ...

### Machine Building
- [ ] PASS / FAIL
- Notes: ...

### Closure Analysis
- [ ] PASS / FAIL
- Notes: ...

### Calculation Verification
- [ ] PASS / FAIL
- Process 1: ...
- Process 2: ...
- Process 3: ...

## Automated Tests

### test_kb_migration.py
- Total: X tests
- Passed: X
- Failed: X
- Coverage: X%

### test_end_to_end.py
- Total: X tests
- Passed: X
- Failed: X
- Coverage: X%

## Issues Found

### Issue 1: [Title]
- **Severity:** Critical / High / Medium / Low
- **Description:** ...
- **Steps to reproduce:** ...
- **Expected:** ...
- **Actual:** ...
- **Fix required:** Yes / No

## Performance Notes

- Indexing time: X seconds
- Simulation startup: X ms
- Process execution: X ms

## Recommendations

1. ...
2. ...
3. ...

## Sign-off

- [ ] All critical tests passing
- [ ] No regressions found
- [ ] Performance acceptable
- [ ] Ready for Phase 5 (Cutover)
```

## Success Criteria

Before marking Phase 4.4 complete:

- [ ] All manual tests pass
- [ ] Automated tests created and passing
- [ ] Calculations verified correct (spot checks)
- [ ] Closure analysis works
- [ ] No critical issues found
- [ ] Test report created
- [ ] Any issues documented with severity

## Getting Help

If you encounter issues:

1. Check `docs/SIMULATION_GUIDE.md` for troubleshooting
2. Review ADR specs for expected behavior
3. Examine `src/simulation/engine.py` implementation
4. Check validation errors: `python -m src.cli validate --id process:<id>`
5. Look at event logs: `simulations/<sim-id>/simulation.jsonl`

## Estimated Time

- Manual testing: 2 hours
- Automated tests: 2-3 hours
- Documentation: 30 min
- **Total: 4.5-5.5 hours**

## Next Phase

After completing this phase, report back with your test report. The next phase (Phase 5) will be cutover & cleanup if all tests pass.
