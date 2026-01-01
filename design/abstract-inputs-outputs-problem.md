# Abstract vs Concrete Inputs/Outputs: Architectural Issue and Design Exploration

**Date:** 2025-12-30
**Status:** Design Exploration
**Related ADRs:** ADR-013 (Recipe Override Mechanics)

## Problem Statement

The knowledge base requires generic/reusable processes (e.g., testing, commissioning, import) that can work with many different types of items. However, our current architecture struggles with representing these processes without either:

1. Creating abstract placeholder items (e.g., `system_under_test`, `fuel_generic`) that don't represent real physical items
2. Creating an explosion of specialized processes (e.g., `test_motor_v0`, `test_pump_v0`, `test_sensor_v0`, ...)

### Motivating Example

`load_testing_and_commissioning_v0.yaml` currently uses:
- Input: `system_under_test` (abstract)
- Output: `system_commissioned` (abstract)

This is problematic because:
- These items don't correspond to real physical objects
- Material flow tracking becomes meaningless
- Recipes must override inputs/outputs to make them concrete
- Simulation may struggle with abstract item properties (mass, energy content, etc.)

Yet the alternative—creating `test_motor_v0`, `test_pump_v0`, etc.—would require hundreds of near-duplicate processes.

## Current State: Architectural Patterns

### Pattern 1: Empty Placeholder Processes

**Purpose:** Processes with zero inputs/outputs where recipes define everything

**Examples:**
- `import_placeholder_v0.yaml` - inputs: `[]`, outputs: `[]`
- `resource_availability_placeholder_v0.yaml` - inputs: `[]`, outputs: `[]`

**Recipe Specialization:**
```yaml
# Recipe step overrides empty process
steps:
  - process_id: import_placeholder_v0
    inputs:
      - item_id: copper_plate_or_sheet  # Defined in recipe
        qty: 5.0
        unit: kg
    outputs:
      - item_id: jacket_panels_formed   # Defined in recipe
        qty: 4.0
        unit: kg
```

**Usage:** 25+ recipes use this pattern for imports and abstract resources

**Advantages:**
- Single reusable process for all imports
- Recipes fully control material flow
- No abstract items needed

**Disadvantages:**
- Process definition is meaningless on its own
- Energy/time models may not be representative for all use cases
- Validation can't check process in isolation

### Pattern 2: Generic Placeholder Items

**Purpose:** Abstract items that represent "any system/component of this type"

**Examples:**
- `system_under_test` → `system_commissioned` (testing)
- `fuel_generic` → `electricity` (generation)
- `gripper_components` → `robot_gripper_parallel_jaw_v0` (assembly)
- `component_to_seal` → used across multiple sealing processes

**Recipe Specialization:**
```yaml
# Recipe overrides generic items with specific ones
steps:
  - process_id: load_testing_and_commissioning_v0
    inputs:
      - item_id: motor_electric_small    # Override system_under_test
        qty: 1.0
        unit: unit
    outputs:
      - item_id: motor_electric_small_tested  # Override system_commissioned
        qty: 1.0
        unit: unit
```

**Usage:** ~20-30 processes identified

**Advantages:**
- Process has meaningful default energy/time estimates
- Can define realistic resource requirements
- Self-documenting purpose

**Disadvantages:**
- Creates abstract items in the item database
- Material flow tracking sees phantom items
- Validation gaps for undefined abstract items (currently 20+ in work_queue.jsonl)
- Recipe authors must remember to override

### Pattern 3: Seed/Bootstrap Processes

**Purpose:** Create initial items from nothing to bootstrap the system

**Examples:**
- `seed_packed_bed_v0.yaml` - inputs: `[]`, outputs: `[packed_bed_v0]`
- `seed_output_generation_v0.yaml` - minimal inputs to produce system outputs
- 114 processes total with empty inputs or outputs

**Advantages:**
- Necessary for system initialization
- Clear semantic meaning (bootstrap)
- Well-understood pattern

**Disadvantages:**
- Violates conservation of mass/energy
- Only valid at t=0 or for external inputs
- May confuse simulation if used incorrectly

## Current Override Mechanism (ADR-013)

Recipe steps can override process-level fields:

### Complete Override (when `type` specified):
```yaml
steps:
  - process_id: crushing_basic_v0
    time_model:
      type: linear_rate      # Type present = complete override
      rate: 50.0
      rate_unit: kg/hr
      scaling_basis: regolith_lunar_mare
```

### Partial Override (when `type` omitted):
```yaml
steps:
  - process_id: crushing_basic_v0
    time_model:
      rate: 50.0             # Only override rate, inherit type/unit/etc
```

### Input/Output Override:
```yaml
steps:
  - process_id: import_placeholder_v0
    inputs:                   # Completely replaces process.inputs
      - item_id: steel_stock
        qty: 10.0
        unit: kg
    outputs:                  # Completely replaces process.outputs
      - item_id: steel_plate
        qty: 9.5
        unit: kg
```

**Schema Support:** `src/kb_core/schema.py:160-163`
```python
# Step-level inputs/outputs (optional, for explicit material flow)
inputs: List[RawQuantity] = Field(default_factory=list)
outputs: List[RawQuantity] = Field(default_factory=list)
byproducts: List[RawQuantity] = Field(default_factory=list)
```

## Validation and Simulation Constraints

### Validation Behavior (src/kb_core/validators.py)

**Current validation checks:**
- `process_type` required (ERROR)
- `scaling_basis` must reference actual items in inputs/outputs (ERROR)
- Energy/time model consistency (ERROR/WARNING)

**Does NOT validate:**
- Whether items are "abstract" vs "concrete"
- Whether abstract items are overridden in recipes
- Whether empty inputs/outputs are legitimate

### Simulation Expectations

**From examination of schema and loaders:**
- Material flow simulation needs concrete items with properties (mass_kg, density, etc.)
- Energy calculations use `scaling_basis` to find the driving item
- Empty inputs/outputs likely break conservation laws unless overridden

**Work queue contains 20+ gaps for abstract items:**
- `item_not_found`: material_wet, raw_materials_batch, seal_material, chemical_feedstock, molten_metal_generic, etc.
- These abstract items are referenced but never defined as concrete items
- Causes closure analysis failures

## Issue Taxonomy

### Issue 1: Semantic Ambiguity
**Problem:** Hard to distinguish legitimate placeholder processes from incomplete/broken processes

**Examples:**
- Is `system_under_test` intentionally abstract or missing definition?
- Should `fuel_generic` be specialized or is it actually generic fuel?
- Empty inputs: bootstrap seed or forgotten to define?

**Impact:**
- Validation cannot distinguish intentional vs accidental abstraction
- KB maintainers can't tell if items need to be created
- Documentation unclear about which processes need recipe specialization

### Issue 2: Closure Analysis Failures
**Problem:** Abstract items break dependency closure tracking

**Evidence from work_queue.jsonl:**
- 20+ `item_not_found` gaps for abstract items
- Circular dependencies involving generic items
- Recipe steps reference undefined abstract items

**Impact:**
- Cannot compute full manufacturing closure
- Dependency graphs incomplete
- Simulation cannot initialize material state

### Issue 3: Conservation Law Violations
**Problem:** Abstract items have no physical properties (mass, energy, etc.)

**Examples:**
- `system_under_test` has no mass_kg → cannot track mass balance
- `fuel_generic` has no energy content → cannot validate energy conservation
- Empty inputs violate mass conservation (unless at boundary)

**Impact:**
- Simulation may crash or produce nonsense results
- Cannot validate conservation laws
- Recipe authors must ensure overrides have proper properties

### Issue 4: Maintenance Burden
**Problem:** Recipe authors must remember which processes need specialization

**Current state:**
- 25+ recipes manually override placeholder processes
- No validation that overrides are complete
- No documentation of which processes are templates

**Impact:**
- Error-prone recipe authoring
- Silent failures when overrides are forgotten
- Knowledge scattered across recipe files

### Issue 5: Explosion of Specialized Processes
**Problem:** Without abstraction, need separate process for each item type

**Example:** Testing processes
- Need: testing for motors, pumps, sensors, circuits, assemblies, etc.
- With specialization: 1 generic process + recipe overrides
- Without: 100+ near-duplicate test processes

**Impact:**
- KB becomes massive and unmaintainable
- Changes to test procedure require updating 100+ files
- Harder to ensure consistency

## Tradeoffs Analysis

### Tradeoff 1: Reusability vs Concreteness

| Approach | Reusability | Concreteness | Validation | Simulation |
|----------|-------------|--------------|------------|------------|
| Abstract items | High (1 process, many uses) | Low (phantom items) | Partial (can't validate item properties) | Requires overrides |
| Empty processes | Highest (pure template) | Zero (recipe defines all) | None (process is shell) | Requires overrides |
| Specialized processes | None (1:1 mapping) | High (real items only) | Complete (full validation) | Works directly |

**Observation:** There is an inherent tension between reusability and concreteness. No solution eliminates this tradeoff entirely.

### Tradeoff 2: Compile-Time vs Runtime Binding

| Approach | When Specialized | Validation | Flexibility | Complexity |
|----------|------------------|------------|-------------|------------|
| Process-level (concrete items) | KB authoring time | Full | Low | Low |
| Recipe-level (override) | Recipe authoring time | Partial | High | Medium |
| Template expansion (proposed) | Build/index time | Full (after expansion) | Medium | High |
| Runtime polymorphism (proposed) | Simulation time | Minimal | Highest | Highest |

**Observation:** Earlier binding enables better validation but reduces flexibility. Later binding increases flexibility but complicates validation.

### Tradeoff 3: Explicit vs Implicit Templating

| Approach | Template Marker | Discoverability | Validation | Migration Cost |
|----------|-----------------|-----------------|------------|----------------|
| No marker (status quo) | None | Hard (grep for patterns) | Cannot distinguish | Zero |
| Naming convention | `_placeholder_` suffix | Medium (searchable) | Pattern detection | Low (rename) |
| Kind field | `kind: process_template` | Easy (schema-aware) | Can enforce rules | Medium (schema change) |
| Metadata field | `is_template: true` | Easy | Can enforce rules | Medium (schema change) |

**Observation:** Explicit markers enable better tooling but require schema changes and migration effort.

## Possible Solutions

### Solution 1: Status Quo + Documentation

**Approach:** Accept current patterns, improve documentation

**Changes:**
1. Document placeholder process pattern in ADR
2. Add comments to placeholder processes: `# Template process - recipe must override inputs/outputs`
3. Create validation rule: WARN if abstract item referenced but not defined
4. Add KB style guide for when to use each pattern

**Advantages:**
- Zero implementation cost
- Preserves existing patterns
- Backward compatible

**Disadvantages:**
- Doesn't solve validation or simulation issues
- Relies on human discipline
- Abstract items still cause closure gaps

**Assessment:** Minimal improvement over current state. Insufficient.

### Solution 2: Explicit Template Marker

**Approach:** Add metadata to distinguish template processes from concrete ones

**Schema change:**
```yaml
# src/kb_core/schema.py
class Process(BaseModel):
    id: str
    kind: Literal["process"]
    is_template: bool = Field(default=False)  # NEW FIELD
    template_params: Optional[List[str]] = None  # NEW: ["input_item", "output_item"]
    ...
```

**Process definition:**
```yaml
id: load_testing_and_commissioning_v0
kind: process
is_template: true                           # Marks as template
template_params: [input_system, output_system]  # Expected overrides
inputs:
  - item_id: system_under_test              # Template placeholder
    qty: 1.0
    unit: unit
outputs:
  - item_id: system_commissioned            # Template placeholder
    qty: 1.0
    unit: unit
```

**Validation rules:**
```python
# New validator
def validate_template_process(process):
    if process.is_template:
        # Allow abstract items in templates
        # But warn if template_params not documented
        if not process.template_params:
            yield Warning("Template process should document template_params")
    else:
        # Concrete processes: validate all items exist
        for item_id in process.inputs + process.outputs:
            if not item_exists(item_id):
                yield Error(f"Item {item_id} not found")

def validate_recipe_step(recipe, step):
    process = lookup_process(step.process_id)
    if process.is_template:
        # Require overrides for template params
        for param in process.template_params:
            if param not in step.overrides:
                yield Error(f"Recipe must override template param: {param}")
```

**Advantages:**
- Clear semantic distinction
- Enables targeted validation rules
- Self-documenting templates
- Can generate documentation automatically

**Disadvantages:**
- Requires schema migration
- Need to update existing placeholder processes
- Adds conceptual complexity
- Still requires manual recipe authoring

**Implementation effort:** Medium (1-2 days)

### Solution 3: Template Expansion at Index Time

**Approach:** Expand templates into concrete processes during indexing

**Build-time expansion:**
```python
# src/kb_core/indexer.py
def expand_template_processes(kb):
    """Expand template processes based on recipe usage"""
    expanded = []

    for recipe in kb.recipes:
        for step in recipe.steps:
            process = kb.processes[step.process_id]

            if process.is_template and step.inputs and step.outputs:
                # Create concrete process instance
                concrete = Process(
                    id=f"{process.id}_{recipe.id}_step{step_idx}",
                    kind="process",
                    is_template=False,
                    inputs=step.inputs,      # Use recipe overrides
                    outputs=step.outputs,
                    energy_model=merge(process.energy_model, step.energy_model),
                    time_model=merge(process.time_model, step.time_model),
                    ...
                )
                expanded.append(concrete)

    return expanded
```

**Result:** Index contains both templates AND concrete instances

**Advantages:**
- Validation can work on concrete instances
- Simulation sees only concrete processes
- Templates remain reusable
- Enables full closure analysis

**Disadvantages:**
- Index size grows (1 template → N concrete instances)
- Expansion logic adds complexity
- Harder to trace errors back to source
- Unclear ownership (template or recipe?)

**Implementation effort:** High (3-5 days)

### Solution 4: Item Type Hierarchies (Advanced)

**Approach:** Allow items to have abstract types that concrete items implement

**Schema:**
```yaml
# Abstract item type
id: system_testable
kind: item_type                    # New kind
is_abstract: true
required_properties:
  - mass_kg
  - power_rating_w
description: "Any system that can be tested and commissioned"

# Concrete item implements type
id: motor_electric_small
kind: item
implements: [system_testable]      # Implements interface
mass_kg: 12.0
power_rating_w: 750.0
...
```

**Process uses abstract type:**
```yaml
id: load_testing_and_commissioning_v0
kind: process
inputs:
  - item_type: system_testable     # Accepts any item implementing this type
    qty: 1.0
    unit: unit
outputs:
  - item_type: system_testable     # Same type out
    qty: 1.0
    unit: unit
```

**Recipe binds type to concrete item:**
```yaml
steps:
  - process_id: load_testing_and_commissioning_v0
    type_bindings:
      system_testable: motor_electric_small   # Bind abstract → concrete
```

**Advantages:**
- Clean type system
- Recipe validation can check type compatibility
- Self-documenting requirements
- Enables powerful abstractions

**Disadvantages:**
- Major schema redesign required
- High implementation complexity
- Significant learning curve
- May be overengineering for current needs

**Implementation effort:** Very High (2+ weeks)

### Solution 5: Recipe-Level Item Aliases

**Approach:** Allow recipes to define item name mappings

**Recipe schema:**
```yaml
id: recipe_motor_testing_v0
kind: recipe
item_aliases:                       # NEW SECTION
  system_under_test: motor_electric_small
  system_commissioned: motor_electric_small_tested
steps:
  - process_id: load_testing_and_commissioning_v0
    # Automatic substitution of aliases in inputs/outputs
```

**Processing:**
```python
# During recipe resolution
def resolve_aliases(recipe, step):
    resolved_inputs = []
    for inp in step.process.inputs:
        item_id = recipe.item_aliases.get(inp.item_id, inp.item_id)
        resolved_inputs.append(inp.copy(update={"item_id": item_id}))
    return resolved_inputs
```

**Advantages:**
- Lightweight solution
- Minimal schema changes
- Easy to understand
- Backward compatible (aliases optional)

**Disadvantages:**
- Aliases scattered across recipes
- No validation of alias compatibility
- Harder to track item usage
- Manual mapping required

**Implementation effort:** Low (1 day)

### Solution 6: Hybrid Approach (Recommended)

**Approach:** Combine explicit template markers + item aliases + improved validation

**Phase 1: Minimal Viable Solution (1-2 days)**
1. Add `is_template: bool` field to process schema
2. Add `template_notes: str` field explaining expected overrides
3. Mark existing placeholder processes as templates
4. Add validation rule: ERROR if template used in recipe without input/output overrides
5. Add validation rule: WARNING if non-template process has undefined items

**Phase 2: Enhanced Usability (3-5 days)**
6. Add `item_aliases` to recipe schema for lightweight binding
7. Document template pattern in ADR
8. Create KB style guide for templates
9. Add indexer check: list all templates and their usage

**Phase 3: Future Enhancement (optional)**
10. Consider template expansion for simulation
11. Consider item type system if pattern proves insufficient

**Advantages:**
- Incremental implementation
- Immediate value from Phase 1
- Low risk (mostly metadata)
- Can validate approach before deeper investment

**Disadvantages:**
- Still requires manual recipe authoring
- Doesn't solve all abstraction needs
- May need Phase 3 eventually

**Implementation effort:** Medium (1-2 days for Phase 1)

## Validation Impact Analysis

### Current Validation Gaps

**From work_queue.jsonl analysis:**
- 20+ undefined abstract items causing `item_not_found` gaps
- 25+ recipes using placeholder processes without validation
- Circular dependencies involving abstract items

### Validation Rules Needed

**Rule 1: Template Process Validation**
```python
if process.is_template:
    # Allow abstract items in inputs/outputs
    # But require documentation
    if not process.template_notes:
        yield WARNING("Template process should document expected overrides")
else:
    # Concrete process: all items must exist
    for item_id in all_referenced_items(process):
        if not item_exists(item_id):
            yield ERROR(f"Item {item_id} not found")
```

**Rule 2: Recipe Override Validation**
```python
process = kb.processes[step.process_id]
if process.is_template:
    if not (step.inputs and step.outputs):
        yield ERROR(f"Template process {process.id} requires input/output overrides in recipe")

    # Validate override completeness
    if has_abstract_items(step.inputs) or has_abstract_items(step.outputs):
        yield WARNING("Recipe overrides still contain abstract items")
```

**Rule 3: Conservation Law Validation (for simulation)**
```python
# After recipe override resolution
resolved_step = resolve_overrides(recipe, step)
total_mass_in = sum(item.mass_kg * qty for item, qty in resolved_step.inputs)
total_mass_out = sum(item.mass_kg * qty for item, qty in resolved_step.outputs)

if abs(total_mass_in - total_mass_out) > tolerance:
    yield ERROR("Mass conservation violated in recipe step")
```

## Simulation Impact Analysis

### Current Simulation Assumptions

**From schema and loader code:**
1. All items have concrete properties (mass_kg, density, etc.)
2. Material flow is tracked via item_id references
3. Energy/time calculations use `scaling_basis` to find driving item

### Simulation Strategies

**Strategy 1: Recipe-Resolved Simulation**
- Resolve all recipe overrides before simulation
- Create material flow graph from resolved steps
- Simulate using only concrete items

**Advantages:**
- Clean separation: templates → resolution → simulation
- All conservation laws checkable
- No special handling in simulator

**Disadvantages:**
- Need robust resolution logic
- Errors appear late (at resolution time, not authoring time)

**Strategy 2: Template Expansion Simulation**
- Expand templates during indexing
- Simulator sees only concrete process instances
- Original templates preserved for authoring

**Advantages:**
- Validation can happen at index time
- Simulator has no template awareness needed
- Can validate all instances independently

**Disadvantages:**
- Index bloat (N instances per template)
- Harder error messages (which instance failed?)

**Strategy 3: Runtime Polymorphic Simulation**
- Simulator handles templates directly
- Binds template params at simulation time
- Dynamic dispatch for abstract items

**Advantages:**
- Most flexible
- Can explore parameter space
- Matches OOP mental model

**Disadvantages:**
- Complex simulator implementation
- Harder to validate
- Performance overhead

## Recommendations

### Immediate Actions (This Sprint)

1. **Document Current Patterns**
   - Create ADR-XXX documenting placeholder process pattern
   - Add inline comments to existing placeholder processes
   - Update KB README with pattern examples

2. **Improve Validation**
   - Add WARNING for processes with empty inputs/outputs (unless explicitly marked)
   - Add INFO logging for abstract items found in work queue
   - Document which items are intentionally abstract vs missing

3. **Mark Existing Templates**
   - Add `# TEMPLATE PROCESS - requires recipe override` comments
   - Create a `kb/templates/README.md` listing all template processes
   - Document expected overrides for each

**Effort:** 1 day
**Risk:** Low
**Value:** Immediate clarity for KB authors

### Short-Term Enhancement (Next Sprint)

4. **Implement Solution 6 Phase 1**
   - Add `is_template` field to process schema
   - Add template validation rules
   - Migrate existing placeholder processes
   - Update validation reports to distinguish templates from concrete

**Effort:** 1-2 days
**Risk:** Low (additive change)
**Value:** Enables automated validation of template usage

### Medium-Term (Next Month)

5. **Implement Solution 6 Phase 2**
   - Add item_aliases to recipe schema
   - Implement alias resolution in recipe processing
   - Add examples and documentation
   - Consider template expansion for simulation

**Effort:** 3-5 days
**Risk:** Medium (requires testing recipe resolution)
**Value:** Reduces recipe authoring burden

### Long-Term (As Needed)

6. **Evaluate Advanced Solutions**
   - Monitor template usage patterns
   - Collect pain points from recipe authoring
   - Consider item type system (Solution 4) if simple templates prove insufficient
   - Consider template expansion (Solution 3) if simulation needs it

**Effort:** 2+ weeks
**Risk:** High (major architecture change)
**Value:** Depends on actual need

## Open Questions

1. **Item Property Inheritance**: If recipe overrides `system_under_test` → `motor_electric_small`, should the override inherit other properties from the template? Or completely replace?

2. **Scaling Basis in Templates**: How should `scaling_basis` work when items are abstract? Should it reference template params?

3. **Multiple Implementations**: Can one template be specialized differently in different recipes? (Answer: Yes, that's the point. But how to validate consistency?)

4. **Template Composition**: Can templates reference other templates? Should this be allowed or forbidden?

5. **Boundary vs Internal**: Should we distinguish "boundary templates" (import, resource availability) from "internal templates" (testing, assembly)? Different validation rules?

6. **Conservation Laws**: Should template processes specify conservation constraints (e.g., "mass_out = mass_in", "energy_out < energy_in + process_energy")? How to validate?

## Related Issues in Codebase

### Files Requiring Updates

**If implementing Solution 6:**

1. `src/kb_core/schema.py` - Add `is_template`, `template_notes` fields
2. `src/kb_core/validators.py` - Add template validation rules
3. `src/kb_core/recipe_resolution.py` (may need to create) - Override resolution logic
4. `kb/processes/*_placeholder_v0.yaml` - Mark as templates
5. `design/ADR-XXX-template-processes.md` - New ADR documenting pattern

### Existing Code to Preserve

- ADR-013 override mechanics (complete vs partial)
- Recipe step override schema (inputs/outputs)
- Current validation infrastructure

### Migration Path

1. Add new fields as optional (`is_template: bool = False`)
2. Migrate placeholder processes incrementally
3. Add validation rules with grace period (WARNING → ERROR)
4. Update documentation
5. Announce in KB changelog

## Conclusion

The abstract inputs/outputs issue represents a fundamental tension between **reusability** and **concreteness** in the knowledge base. Our current implicit template pattern works but lacks validation, documentation, and tool support.

**Recommended path forward:**
1. **Document** current patterns (1 day) - immediate value
2. **Mark** templates explicitly (1-2 days) - enables validation
3. **Validate** recipe overrides (ongoing) - prevents errors
4. **Evaluate** advanced solutions only if simple approach proves insufficient

The hybrid approach (Solution 6) provides incremental value without high-risk architectural changes. It preserves the flexibility of the current system while adding much-needed validation and documentation.

---

**Next Steps:**
1. Review this document with team
2. Decide on solution approach
3. Create ADR if proceeding with schema changes
4. Implement Phase 1 changes
5. Monitor usage and iterate
