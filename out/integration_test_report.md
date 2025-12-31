# Integration Testing Report - Phase 4.4

**Date:** 2025-12-30
**Tester:** Codex (GPT-5)

## Summary

- Total tests run: 10 automated + 7 manual tasks
- Passed: 9 automated, 3 manual
- Failed: 1 automated, 4 manual
- Warnings: 49 (pytest deprecation warnings)

## Manual Testing Results

### Bootstrap Simulation
- [x] PASS
- Notes: regolith_mining_highlands_v0 completed; energy 50.00 kWh; regolith_lunar_highlands 100.00 kg; event log present at simulations/integration_test/simulation.jsonl.

### Calculated Duration
- [ ] FAIL
- Notes: `sim start-process` without duration fails: "Must provide either duration_hours or (output_quantity + output_unit)" and CLI does not expose output_quantity/output_unit. Engine duration calc also fails for input-based scaling (crushing_basic_v0). Output-quantity duration works for output-based scaling (rock_excavation_basic_v0), but output quantities are not scaled by output_quantity.

### Recipe Execution
- [ ] FAIL
- Notes: No recipes with time_model overrides found in KB. Running recipe_feed_horn_antenna_v0 failed with AttributeError in unit conversion (RawItem .get) during machine availability check.

### Machine Building
- [ ] FAIL
- Notes: After importing required components, build-machine for crusher_basic_v0 failed with AttributeError in unit conversion (RawItem .get). Initial failure due to missing components resolved by import.

### Closure Analysis
- [ ] FAIL
- Notes: `closure --machine crusher_basic_v0` reports machine not found. Using `crusher_basic` succeeds but emits many warnings for recipes with no inputs. `closure --all --output out/closure_test.txt` completes.

### Calculation Verification
- [x] PASS
- Process 1: regolith_mining_highlands_v0 (8.00 hr, 50.00 kWh)
- Process 2: metal_forming_basic_v0 (1.50 hr, 1.50 kWh)
- Process 3: crushing_basic_v0 (0.30 hr, 1.50 kWh)
- Details recorded in out/calculation_verification.md

## Automated Tests

### test_kb_migration.py
- Total: 7 tests
- Passed: 6
- Failed: 1
- Coverage: Not measured
- Failure: test_recipe_with_partial_override (partial override not merged; time_model.type missing)

### test_end_to_end.py
- Total: 3 tests
- Passed: 3
- Failed: 0
- Coverage: Not measured

## Issues Found

### Issue 1: Calculated duration path unreachable from CLI
- **Severity:** High
- **Description:** CLI start-process without duration fails because engine requires output_quantity/output_unit, but CLI does not accept those args.
- **Steps to reproduce:** `.venv/bin/python -m src.cli sim start-process --sim-id integration_test --process crushing_basic_v0`
- **Expected:** Duration calculated from process time_model.
- **Actual:** Error: "Must provide either duration_hours or (output_quantity + output_unit)".
- **Fix required:** Yes

### Issue 2: Duration calc fails for input-based scaling
- **Severity:** High
- **Description:** Engine passes empty inputs to calculate_duration when output_quantity is provided; linear_rate scaling_basis on inputs raises error.
- **Steps to reproduce:** Engine start_process with output_quantity for crushing_basic_v0.
- **Expected:** Duration calculated using input scaling_basis.
- **Actual:** "scaling_basis 'anorthite_ore' not found in inputs or outputs".
- **Fix required:** Yes

### Issue 3: output_quantity does not scale outputs/inputs
- **Severity:** Medium
- **Description:** output_quantity only affects duration, not outputs or inputs, causing mismatched results (e.g., rock_excavation_basic_v0 output remains 1 kg when output_quantity=100 kg).
- **Steps to reproduce:** start_process with output_quantity for rock_excavation_basic_v0 and advance time.
- **Expected:** Outputs scaled to requested output_quantity.
- **Actual:** Outputs remain base quantities.
- **Fix required:** Yes

### Issue 4: Unit conversion crashes on RawItem
- **Severity:** High
- **Description:** UnitConverter._try_count_conversion uses item.get(...) but item is RawItem (pydantic), causing AttributeError. Breaks run_recipe and build_machine when count conversions occur.
- **Steps to reproduce:** `sim run-recipe --recipe recipe_feed_horn_antenna_v0` or `sim build-machine --machine crusher_basic_v0`.
- **Expected:** Machine availability check and build succeed with count/unit conversions.
- **Actual:** AttributeError: 'RawItem' object has no attribute 'get'.
- **Fix required:** Yes

### Issue 5: Partial recipe time_model overrides not merged
- **Severity:** Medium
- **Description:** resolve_step replaces time_model entirely, losing base fields when override omits type.
- **Steps to reproduce:** test_recipe_with_partial_override in test/integration/test_kb_migration.py.
- **Expected:** Partial override merges with process time_model.
- **Actual:** time_model.type is None.
- **Fix required:** Yes

### Issue 6: Machine ID mismatch in docs/commands
- **Severity:** Low
- **Description:** Instructions reference crusher_basic_v0, but KB machine id is crusher_basic.
- **Steps to reproduce:** `.venv/bin/python -m src.cli closure --machine crusher_basic_v0`.
- **Expected:** Machine exists.
- **Actual:** Machine not found.
- **Fix required:** No (doc/KB alignment)

## Performance Notes

- Indexing time: Not measured
- Simulation startup: Not measured
- Process execution: Not measured
- Closure --all runtime: ~6.1s (observed)

## Recommendations

1. Add CLI support for output_quantity/output_unit and update start_process to use inputs for duration calc.
2. Fix UnitConverter to handle pydantic models (use model_dump or attribute access) and retest run-recipe/build-machine.
3. Implement partial override merge semantics per ADR-013 and add regression tests.

## Sign-off

- [ ] All critical tests passing
- [ ] No regressions found
- [ ] Performance acceptable
- [ ] Ready for Phase 5 (Cutover)
