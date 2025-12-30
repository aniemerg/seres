NOTE: Migration/analysis document for pre-ADR-012 schema. See docs/kb_schema_reference.md for current rules.

# Implementation Plan: KB Core Refactor with ADR 12-17

**Status:** In Progress
**Created:** 2024-12-30
**Branch:** `refactor/kb-core-adr-12-17`
**Goal:** Refactor codebase to implement ADRs 12-17 with tests, in new git branch, parallel to existing code.

**Timeline:** 6-7 weeks
**Approach:** Build new in `src/`, keep old code for reference, cutover when complete

---

## Overview

This implementation plan guides the refactoring of the KB tooling and simulation engine to implement:
- **ADR-012:** Process Types and Time Model Redesign
- **ADR-013:** Recipe Override Mechanics
- **ADR-014:** Energy Model Redesign
- **ADR-016:** Unit Conversion and Type System
- **ADR-017:** Validation and Error Detection Strategy

**Key Decisions:**
- Two-layer model architecture (RawModels → ValidatedModels)
- Unified KB loader with lazy loading
- New schemas only, no backward compatibility during development
- Validation at index time with ERROR/WARNING/INFO levels
- Auto-fix for mechanical migrations
- Work in parallel branch, merge when complete

---

## Phase 1: Core Infrastructure (Week 1-2)

### 1.1 Project Setup

**Tasks:**
- [x] Create new git branch `refactor/kb-core-adr-12-17`
- [ ] Create directory structure
- [ ] Set up pytest configuration
- [ ] Add `pytest`, `pytest-cov` to dependencies

**Directory Structure:**
```
src/
  __init__.py
  kb_core/
    __init__.py
    schema.py           # Pydantic models (Raw + Validated)
    validators.py       # Validation logic (ADR-017)
    unit_converter.py   # Enhanced converter (ADR-016)
    calculations.py     # Time/energy calculations (ADR-012, 014)
    kb_loader.py        # Unified KB loading
    config.py           # Configuration management

  indexer/
    __init__.py
    indexer.py          # KB scanning, validation, work queue
    closure_analysis.py # Material closure analysis
    queue_tool.py       # Work queue management
    auto_fix.py         # Auto-fix mechanical migrations
    cli.py              # Indexer CLI commands

  simulation/
    __init__.py
    engine.py           # Simulation engine
    cli.py              # Simulation CLI commands

  cli.py                # Unified CLI entry point

test/
  __init__.py
  unit/
    __init__.py
    test_schema.py
    test_unit_converter.py
    test_calculations.py
    test_validators.py
    test_auto_fix.py
    test_kb_loader.py
    test_override_resolution.py
  integration/
    __init__.py
    test_indexer_flow.py
    test_simulation_flow.py
    test_end_to_end.py
    test_kb_migration.py
  fixtures/
    __init__.py
    processes/
    recipes/
    items/
  conftest.py

pytest.ini
```

**pytest.ini:**
```ini
[pytest]
testpaths = test
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts =
    -v
    --strict-markers
    --tb=short
```

**Estimated time:** 2 hours

---

### 1.2 Schema Definitions (New Models)

**File:** `src/kb_core/schema.py`

**Tasks:**
- [ ] Define `RawProcess`, `RawRecipe`, `RawItem` (permissive parsing)
- [ ] Define `ValidatedProcess`, `ValidatedRecipe`, `ValidatedItem` (strict validation)
- [ ] Define new `TimeModel`, `EnergyModel` per ADR-012, ADR-014
- [ ] Define `RecipeStep` with override support per ADR-013
- [ ] Add comprehensive docstrings with examples

**Key Model Structure:**

```python
# Two-layer architecture:
# Layer 1: Raw models (permissive, for YAML parsing)
# Layer 2: Validated models (strict, for simulation)

# Raw Models (permissive)
class RawTimeModel(BaseModel):
    model_config = ConfigDict(extra="allow")
    type: Optional[str] = None
    rate: Optional[float] = None
    rate_unit: Optional[str] = None
    scaling_basis: Optional[str] = None
    hr_per_batch: Optional[float] = None
    setup_hr: Optional[float] = None
    # Accept deprecated fields for parsing
    rate_kg_per_hr: Optional[float] = None
    hr_per_kg: Optional[float] = None

class RawProcess(BaseModel):
    model_config = ConfigDict(extra="allow")
    id: str
    process_type: Optional[str] = None
    inputs: List[RawQuantity] = Field(default_factory=list)
    outputs: List[RawQuantity] = Field(default_factory=list)
    time_model: Optional[RawTimeModel] = None
    energy_model: Optional[RawEnergyModel] = None

# Validated Models (strict)
class TimeModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: Literal["linear_rate", "batch"]
    rate: Optional[float] = None
    rate_unit: Optional[str] = None
    scaling_basis: Optional[str] = None
    hr_per_batch: Optional[float] = None
    setup_hr: Optional[float] = Field(default=0.0)

class Process(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    process_type: Literal["batch", "continuous"]
    inputs: List[Quantity]
    outputs: List[Quantity]
    time_model: TimeModel
    energy_model: Optional[EnergyModel] = None
```

**Tests:** `test/unit/test_schema.py`
- Test raw parsing accepts invalid data
- Test validated models reject invalid data
- Test field validation for each model
- Test override parsing (partial and complete)

**Estimated time:** 1 day

---

### 1.3 Unit Converter Enhancement

**File:** `src/kb_core/unit_converter.py`

**Tasks:**
- [ ] Port existing `base_builder/unit_converter.py`
- [ ] Add compound unit parsing (`parse_compound_unit()`)
- [ ] Add time normalization (`normalize_time_to_hours()`)
- [ ] Add convertibility checking (`can_convert()`)
- [ ] Add validation helpers

**Key Functions:**
- `parse_compound_unit("kg/hr")` → `("kg", "hr")`
- `normalize_time_to_hours(5, "min")` → `300` (converts 5/min to 300/hr)
- `can_convert("L", "kg", "water")` → `True` (via density)
- `convert_for_calculation()` - raises ValueError if impossible

**Tests:** `test/unit/test_unit_converter.py`
- Test compound unit parsing (valid and invalid)
- Test time normalization (min, hr, day, s)
- Test can_convert for all strategies
- Test convert_for_calculation success and failure

**Estimated time:** 2 days

---

### 1.4 KB Loader (Unified)

**File:** `src/kb_core/kb_loader.py`

**Tasks:**
- [ ] Consolidate `kbtool/indexer.py` and `base_builder/kb_loader.py` loading logic
- [ ] Implement lazy loading with caching
- [ ] Add `load_all()` option for indexer
- [ ] Parse to `RawProcess`, `RawRecipe`, etc.
- [ ] Add error tracking

**Key Features:**
- Lazy loading by default (simulation use case)
- Force full load with `load_all()` (indexer use case)
- Caching to avoid re-parsing
- Error collection without failing

**Tests:** `test/unit/test_kb_loader.py`
- Test lazy loading (only loads when accessed)
- Test eager loading (load_all forces full load)
- Test caching (second access doesn't reload)
- Test error handling (invalid YAML)

**Estimated time:** 1.5 days

---

### 1.5 Time & Energy Calculation

**File:** `src/kb_core/calculations.py`

**Tasks:**
- [ ] Implement `calculate_duration()` per ADR-012
- [ ] Implement `calculate_energy()` per ADR-014
- [ ] Integrate with unit converter
- [ ] Handle both agent-provided duration and calculated duration
- [ ] Add comprehensive error messages

**Key Functions:**

```python
def calculate_duration(
    process: Process,
    inputs: Dict[str, Quantity],
    converter: UnitConverter
) -> float:
    """Calculate process duration from time_model."""
    # For linear_rate: get scaling_basis, convert units, apply rate
    # For batch: return setup_hr + hr_per_batch

def calculate_energy(
    process: Process,
    inputs: Dict[str, Quantity],
    outputs: Dict[str, Quantity],
    converter: UnitConverter
) -> float:
    """Calculate process energy from energy_model."""
    # For per_unit: get scaling_basis, convert units, apply rate
    # For fixed_per_batch: return value
```

**Tests:** `test/unit/test_calculations.py`
- Test calculate_duration for linear_rate (various units)
- Test calculate_duration for batch
- Test calculate_energy for per_unit (various units)
- Test calculate_energy for fixed_per_batch
- Test error cases (missing scaling_basis, conversion failure)
- Test time normalization (kg/min → kg/hr)

**Estimated time:** 2 days

---

### 1.6 Validators

**File:** `src/kb_core/validators.py`

**Tasks:**
- [ ] Implement validation functions per ADR-017
- [ ] Schema validation (process_type, required fields)
- [ ] Semantic validation (scaling_basis exists, positive values)
- [ ] Unit conversion validation (convertibility checks)
- [ ] Cross-model validation (time/energy coupling)
- [ ] Override validation (complete vs partial)
- [ ] Return `ValidationError` objects with level (ERROR/WARNING/INFO)

**Validation Levels:**
- **ERROR:** Schema violations, cannot be used in simulation → work queue
- **WARNING:** Missing recommended fields, may affect quality → work queue
- **INFO:** Suggestions for improvement → logged, NOT in work queue

**Key Functions:**

```python
def validate_process(
    raw_process: RawProcess,
    kb_loader: KBLoader,
    converter: UnitConverter
) -> List[ValidationError]:
    """Validate a raw process against all rules."""

def validate_recipe(
    raw_recipe: RawRecipe,
    kb_loader: KBLoader,
    converter: UnitConverter
) -> List[ValidationError]:
    """Validate a raw recipe including override validation."""
```

**Validation Rules (28+ rules):**
- `process_type_required` (ERROR)
- `process_type_invalid` (ERROR)
- `time_model_type_mismatch` (ERROR)
- `required_field_missing` (ERROR)
- `deprecated_field` (ERROR)
- `scaling_basis_not_found` (ERROR)
- `setup_hr_in_continuous` (ERROR)
- `negative_value` (ERROR)
- `invalid_compound_unit` (ERROR)
- `conversion_not_possible` (ERROR)
- `density_missing` (ERROR - if needed)
- `mass_kg_missing` (ERROR - if needed)
- `time_model_missing` (WARNING)
- `energy_model_missing` (WARNING)
- And more...

**Tests:** `test/unit/test_validators.py`
- Test each validation rule individually
- Test validation error generation
- Test error levels (ERROR/WARNING/INFO)
- Test fix hints are helpful
- Test validation with valid and invalid processes

**Estimated time:** 3 days

---

### Phase 1 Summary

**Deliverables:**
- ✅ Project structure and pytest setup
- ✅ Complete schema definitions (Raw + Validated)
- ✅ Enhanced unit converter with compound units
- ✅ Unified KB loader with lazy loading
- ✅ Time and energy calculation functions
- ✅ Comprehensive validation system
- ✅ Full test suite for all of the above

**Test Coverage:** Critical paths (calculations, validators, unit converter) extensively tested

**Estimated Total Time:** 1.5-2 weeks

---

## Phase 2: Indexer Integration (Week 2-3)

### 2.1 Indexer Core

**File:** `src/indexer/indexer.py`

**Tasks:**
- [ ] Port `kbtool/indexer.py` to use new `kb_core`
- [ ] Load all KB files using `KBLoader`
- [ ] Validate all processes using validators
- [ ] Collect validation errors
- [ ] Generate work queue items for ERROR and WARNING (NOT INFO)
- [ ] Write `out/validation_errors.jsonl` (all levels)
- [ ] Write `out/work_queue.jsonl` (ERROR + WARNING only)

**Key Function:**

```python
def build_index(kb_root: Path, out_dir: Path) -> dict:
    """Build KB index with validation."""
    # Load KB
    loader = KBLoader(kb_root, lazy=False)
    loader.load_all()

    # Validate all processes and recipes
    all_errors = validate_all(loader)

    # Separate by level
    errors = [e for e in all_errors if e.level == ValidationLevel.ERROR]
    warnings = [e for e in all_errors if e.level == ValidationLevel.WARNING]
    info = [e for e in all_errors if e.level == ValidationLevel.INFO]

    # Write validation errors (all levels)
    write_validation_errors(out_dir, all_errors)

    # Generate work queue (ERROR + WARNING only, NOT INFO)
    work_items = [error_to_work_item(e) for e in errors + warnings]
    write_work_queue(out_dir, work_items)

    return summary
```

**Tests:** `test/integration/test_indexer_flow.py`
- Test indexer loads KB
- Test validation errors generated
- Test work queue items created (ERROR + WARNING, not INFO)
- Test output files written correctly

**Estimated time:** 2 days

---

### 2.2 Auto-Fix System

**File:** `src/indexer/auto_fix.py`

**Tasks:**
- [ ] Implement auto-fix for mechanical migrations
- [ ] `rate_kg_per_hr: 10` → `rate: 10, rate_unit: kg/hr`
- [ ] `hr_per_kg: 0.1` → `rate: 10, rate_unit: kg/hr` (invert)
- [ ] `type: fixed_time` → `type: batch`
- [ ] Infer `scaling_basis` for single-input processes
- [ ] Infer `process_type` from time_model.type
- [ ] Write fixes back to YAML files
- [ ] Generate fix report

**Auto-Fix Workflow:**
```bash
# 1. Index to find issues
python -m src.cli index

# 2. Run auto-fix
python -m src.cli auto-fix

# 3. Re-index to verify
python -m src.cli index

# 4. Check remaining errors
cat out/work_queue.jsonl | wc -l
```

**Tests:** `test/unit/test_auto_fix.py`
- Test rate_kg_per_hr conversion
- Test hr_per_kg inversion
- Test scaling_basis inference
- Test process_type inference
- Test YAML written correctly

**Estimated time:** 1.5 days

---

### 2.3 CLI Commands

**File:** `src/indexer/cli.py` and `src/cli.py`

**Tasks:**
- [ ] Implement `index` command
- [ ] Implement `validate --id <id>` command
- [ ] Implement `auto-fix` command
- [ ] Add to unified CLI at `src/cli.py`

**Commands:**
```bash
python -m src.cli index
python -m src.cli index --kb-root kb --out-dir out
python -m src.cli auto-fix
python -m src.cli auto-fix --kb-root kb
python -m src.cli validate --id process:crushing_v0
```

**Estimated time:** 1 day

---

### 2.4 Closure Analysis Update

**File:** `src/indexer/closure_analysis.py`

**Tasks:**
- [ ] Port `kbtool/closure_analysis.py` to use new `kb_core`
- [ ] Update to use validated models
- [ ] Maintain existing functionality

**Estimated time:** 1 day

---

### Phase 2 Summary

**Deliverables:**
- ✅ Indexer using new kb_core
- ✅ Validation error generation (ERROR/WARNING/INFO)
- ✅ Work queue generation (ERROR + WARNING only)
- ✅ Auto-fix system with verification loop
- ✅ CLI commands
- ✅ Updated closure analysis

**Estimated Total Time:** 1 week

---

## Phase 3: Simulation Integration (Week 3-4)

### 3.1 Simulation Engine Update

**File:** `src/simulation/engine.py`

**Tasks:**
- [ ] Port `base_builder/sim_engine.py` to use new `kb_core`
- [ ] Update `start_process()` to use `calculate_duration()` or agent-provided duration
- [ ] Update energy tracking to use `calculate_energy()`
- [ ] Add runtime validation before process execution
- [ ] Maintain existing simulation state management
- [ ] Update recipe execution with override resolution

**Two Duration Modes:**
1. **Agent provides duration** (primary, current behavior)
2. **Agent provides output quantity, duration calculated** (new capability)

**Runtime Validation:**
- Validate process before execution
- Block if ERROR-level validation issues
- Calculate duration from time_model if not provided
- Calculate energy from energy_model

**Tests:** `test/integration/test_simulation_flow.py`
- Test process start with agent-provided duration
- Test process start with calculated duration
- Test runtime validation catches errors
- Test energy calculation
- Test unit conversion during execution

**Estimated time:** 3 days

---

### 3.2 Recipe Override Resolution

**File:** `src/simulation/engine.py`

**Tasks:**
- [ ] Implement override resolution per ADR-013
- [ ] Merge partial overrides with process time_model
- [ ] Use complete overrides as-is
- [ ] Validate merged result

**Override Resolution Rules:**
- If recipe step `time_model` has `type` field → **complete override** (use as-is)
- If recipe step `time_model` lacks `type` field → **partial override** (merge with process)

**Tests:** `test/unit/test_override_resolution.py`
- Test complete override (type specified)
- Test partial override (type omitted)
- Test partial override with no base (error)
- Test invalid complete override (error)

**Estimated time:** 1.5 days

---

### 3.3 Simulation CLI

**File:** `src/simulation/cli.py`

**Tasks:**
- [ ] Port existing CLI commands
- [ ] Update to use new engine
- [ ] Add to unified CLI

**Commands:**
```bash
python -m src.cli sim init --sim-id test
python -m src.cli sim import --sim-id test --item labor_bot_v0 --qty 1
python -m src.cli sim start-process --sim-id test --process mining_v0 --duration 10
python -m src.cli sim advance-time --sim-id test --hours 10
python -m src.cli sim view-state --sim-id test
```

**Estimated time:** 1 day

---

### Phase 3 Summary

**Deliverables:**
- ✅ Simulation engine using kb_core
- ✅ Time/energy calculation integration
- ✅ Runtime validation
- ✅ Override resolution (complete and partial)
- ✅ Updated CLI

**Estimated Total Time:** 1 week

---

## Phase 4: KB Migration & Testing (Week 4-6)

### 4.1 Initial Auto-Fix Run

**Tasks:**
- [ ] Run indexer on current KB (expect many errors)
- [ ] Review validation errors by category
- [ ] Run auto-fix
- [ ] Re-index to verify auto-fixes worked
- [ ] Review remaining errors

**Process:**
```bash
# 1. Initial index
python -m src.cli index
# Expected: hundreds of validation errors

# 2. Review error breakdown
cat out/validation_errors.jsonl | jq '.rule' | sort | uniq -c | sort -rn

# 3. Run auto-fix
python -m src.cli auto-fix
# Expected: fixes rate_kg_per_hr, hr_per_kg, infers scaling_basis

# 4. Re-index
python -m src.cli index
# Expected: fewer errors

# 5. Review work queue
cat out/work_queue.jsonl | jq '.validation_error.rule' | sort | uniq -c
```

**Estimated time:** 1 day

---

### 4.2 Manual Fixes for Testing

**Tasks:**
- [ ] Manually fix 5-10 processes to test workflow
- [ ] Verify auto-fix didn't introduce errors
- [ ] Create example fixes for common patterns
- [ ] Document manual fix patterns

**Common patterns:**
- Multiple inputs → must specify `scaling_basis` manually
- Missing mass_kg → add to item definition
- Missing density → add to materials/properties.yaml

**Estimated time:** 2 days

---

### 4.3 Agent-Driven Fixes

**Tasks:**
- [ ] Update queue agents to handle `validation_fix` work items
- [ ] Run agents on work queue
- [ ] Monitor progress
- [ ] Iterate: index → agent fix → re-index
- [ ] Continue until work queue empty

**Note:** This runs in parallel with other development work

**Estimated time:** 2-3 weeks (parallel)

---

### 4.4 Integration Testing

**Tasks:**
- [ ] Test simulation with migrated KB
- [ ] Run closure analysis on migrated KB
- [ ] Verify calculations correct
- [ ] Compare with old code results (spot checks)
- [ ] Fix any issues found

**Test Cases:**
- Load process, calculate duration, compare with expected
- Load recipe with override, verify resolution correct
- Run full simulation, verify energy accounting
- Run closure analysis, verify ISRU percentages

**Tests:** `test/integration/test_kb_migration.py`, `test/integration/test_end_to_end.py`

**Estimated time:** 3 days

---

### 4.5 Documentation Updates

**Tasks:**
- [ ] Update `docs/README.md` with new structure
- [ ] Update `docs/CLI_COMMANDS_GUIDE.md` with new commands
- [ ] Update design docs to reference new implementation
- [ ] Add migration guide for future KB changes

**Estimated time:** 2 days

---

### Phase 4 Summary

**Deliverables:**
- ✅ KB migrated to new schema
- ✅ All validation errors resolved
- ✅ Integration tests passing
- ✅ Documentation updated

**Estimated Total Time:** 2-3 weeks (agent work in parallel)

---

## Phase 5: Cutover & Cleanup (Week 6-7)

### 5.1 Verification

**Verification Checklist:**
- [ ] All unit tests passing (`pytest test/unit/`)
- [ ] All integration tests passing (`pytest test/integration/`)
- [ ] Indexer runs cleanly (`python -m src.cli index` - no errors)
- [ ] Work queue empty (all KB issues resolved)
- [ ] Sample simulations work correctly
- [ ] Closure analysis produces expected results
- [ ] Performance acceptable (indexing < 5 min)
- [ ] No regressions vs old code (spot checks)

**Estimated time:** 2 days

---

### 5.2 Merge to Main

**Tasks:**
- [ ] Create PR from `refactor/kb-core-adr-12-17` to `main`
- [ ] Final code review
- [ ] Merge to main
- [ ] Tag release: `v2.0.0-kb-core-refactor`
- [ ] Update main branch documentation

**Estimated time:** 1 day

---

### 5.3 Deprecate Old Code

**Tasks:**
- [ ] Move old code to `deprecated/` folder
  - `kbtool/` → `deprecated/kbtool/`
  - `base_builder/` → `deprecated/base_builder/`
  - `queue_agents/` → `deprecated/queue_agents/`
- [ ] Add deprecation notices to old modules
- [ ] Update any external scripts that import old modules
- [ ] Plan for eventual removal (6 months?)

**Estimated time:** 0.5 day

---

### Phase 5 Summary

**Deliverables:**
- ✅ All verification complete
- ✅ Merged to main
- ✅ Old code deprecated
- ✅ Release tagged

**Estimated Total Time:** 0.5 week

---

## Summary Timeline

| Phase | Tasks | Duration | Cumulative |
|-------|-------|----------|------------|
| **Phase 1** | Core infrastructure (schema, validators, calculations) | 1.5-2 weeks | Week 2 |
| **Phase 2** | Indexer integration (validation, auto-fix, CLI) | 1 week | Week 3 |
| **Phase 3** | Simulation integration (engine, overrides, CLI) | 1 week | Week 4 |
| **Phase 4** | KB migration & testing (auto-fix, agents, docs) | 2-3 weeks | Week 6-7 |
| **Phase 5** | Cutover & cleanup (verify, merge, deprecate) | 0.5 week | Week 7 |
| **Total** | | **6-7 weeks** | |

---

## Key Milestones

- **Week 2:** Core infrastructure complete, all tests passing
- **Week 3:** Indexer validates KB, generates work queue
- **Week 4:** Simulation runs with new models
- **Week 6-7:** KB fully migrated, all errors resolved
- **Week 7:** Merge to main, release v2.0.0

---

## Risk Mitigation

**Risk 1:** KB migration takes longer than expected
- **Mitigation:** Auto-fix handles most cases (~70-80%), agents handle rest in parallel

**Risk 2:** Tests reveal calculation errors
- **Mitigation:** Extensive unit tests catch issues early in Phase 1, before migration

**Risk 3:** Performance degradation
- **Mitigation:** Benchmark early, optimize if needed, lazy loading helps

**Risk 4:** Breaking changes affect existing workflows
- **Mitigation:** Work in branch, test thoroughly before merge, keep old code available

---

## Success Criteria

1. ✅ All ADRs 12-17 implemented
2. ✅ 100% of critical paths tested
3. ✅ KB fully migrated with zero validation errors
4. ✅ Simulation produces correct results
5. ✅ Closure analysis works correctly
6. ✅ Documentation updated
7. ✅ Performance acceptable
8. ✅ Code reviewed and merged

---

## Next Steps

1. **Create branch** ✓
2. **Phase 1.1:** Set up directory structure
3. **Phase 1.2:** Define schemas in `src/kb_core/schema.py`
4. **Phase 1.3:** Enhance unit converter
5. **Continue through phases...**

---

## Notes & Decisions Log

### 2024-12-30: Initial Planning
- Confirmed two-layer model architecture (RawModels → ValidatedModels)
- Confirmed ERROR/WARNING/INFO levels, with only ERROR+WARNING in work queue
- Confirmed auto-fix with verification loop
- Confirmed override resolution: validate at index time, resolve at sim time
- Confirmed work in branch, merge when complete

---

## Contact & Questions

For questions or issues during implementation:
- Review ADRs 12-17 in `docs/ADRs/`
- Check test examples in `test/` for patterns
- Refer to this plan for phase-by-phase guidance
