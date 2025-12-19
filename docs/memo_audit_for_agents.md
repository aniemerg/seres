# Memo Audit for Agent Optimization

## Agent Purpose & Needs

**What agents do:**
- Process work queue items (gaps in the KB)
- Create/modify YAML entries to resolve gaps
- Follow existing patterns and conventions
- Validate with indexer
- Make conservative assumptions when uncertain

**What agents need to know:**
1. Required fields for each KB entity type
2. Naming conventions and file structure
3. Valid units and data formats
4. Examples of well-formed entries
5. When to make assumptions vs give up
6. What makes an entry valid

**What agents don't need:**
- Project history and motivation
- Philosophical rationale
- Implementation details of the compiler
- Verbose explanations
- Meta-level workflow guidance

---

## Meta-Memo Analysis (~1,593 tokens)

### Section 1: Purpose (lines 2-9)
**Content:** High-level project goals - making self-replication quantifiable
**Agent needs:** NO
**Rationale:** Philosophical motivation, not operational guidance
**Keep:** Nothing
**Tokens saved:** ~50

### Section 2: Motivation (lines 11-82)
**Content:** Four subsections explaining why the project exists:
- Self-replication is a growth-rate problem
- Ellery defines structure but not closure
- "Replicate everything" is a policy choice
- Quantification reveals leverage

**Agent needs:** MINIMAL - Only the import policy
**Rationale:** Historical context and rationale for design decisions
**Keep:** "Anything that can't be replicated locally is treated as imported" (~15 tokens)
**Tokens saved:** ~320

### Section 3: Core Goal (lines 84-98)
**Content:** Build computable representation with dependency structure
**Agent needs:** NO
**Rationale:** Project-level goals, not creation guidance
**Keep:** Nothing
**Tokens saved:** ~80

### Section 4: Design Philosophy (lines 100-162)
**Content:** Four principles:
1. Structure before precision - coarse numbers OK if labeled
2. Processes before machines - unit operations preferred
3. Incompleteness is a feature - placeholders allowed
4. Iteration guided by bottlenecks - human workflow

**Agent needs:** YES for principles 1-3
**Rationale:** These guide behavior when uncertain or incomplete
**Keep:** Condensed version:
```
Core principles:
- Structure before precision: coarse numbers OK if labeled as estimates
- Processes before machines: prefer unit operations, machines are capacity providers
- Incompleteness allowed: use placeholders, surface gaps explicitly
```
**Tokens saved:** ~220 (keep ~80)

### Section 5: Ellery-Style Dependency Graph (lines 164-262)
**Content:** 9-layer conceptual hierarchy from environment to recursive closure
**Agent needs:** NO
**Rationale:** Conceptual framework, not operational guidance
**Keep:** Nothing
**Tokens saved:** ~350

### Sections 6-9: Why memos exist, Success criteria, Non-goals, Summary (lines 264-328)
**Content:** Meta-documentation and project goals
**Agent needs:** NO
**Rationale:** Project context, not creation guidance
**Keep:** Nothing
**Tokens saved:** ~240

**Meta-Memo Summary:**
- Current: ~1,593 tokens
- Optimized: ~95 tokens (import policy + 3 design principles)
- **Savings: ~1,500 tokens (94%)**

---

## Memo A Analysis (~3,026 tokens)

### Section 1: Purpose (lines 2-19)
**Content:** System goals and outputs
**Agent needs:** MINIMAL
**Keep:** "System designed for iterative refinement - incomplete models should run and highlight gaps" (~20 tokens)
**Tokens saved:** ~80

### Section 2: Non-goals (lines 21-36)
**Content:** What not to model (scheduling, precision, etc.)
**Agent needs:** NO
**Rationale:** Implementation constraints
**Keep:** Nothing
**Tokens saved:** ~80

### Section 3: Core Conceptual Model (lines 38-61)
**Content:** Two graphs - Product Structure (BOM) and Process Network
**Agent needs:** YES - Foundation for understanding entity relationships
**Keep:** Condensed version:
```
Two linked graphs:
1. Product Structure (BOM): Machine → Subassembly → Part → Material
2. Process Network: Item(s) → Process → Item(s) (using resources + energy/time)

Every manufacturable item needs a Recipe (process chain). No recipe = import.
```
**Tokens saved:** ~120 (keep ~100)

### Section 4: Data Model - Items (lines 63-162)
**Content:** Material, Part, Machine definitions with required/optional fields
**Agent needs:** YES - CRITICAL - This is the schema
**Keep:** Streamlined version with required fields only:
```
MATERIAL:
- id, name, kind: material
- unit (typically kg)
- Optional: density, composition, state, notes

PART:
- id, name, kind: part
- mass (kg)
- material_class (steel, ceramic, glass, etc.)
- Optional: dimensions, notes

MACHINE:
- id, name, kind: machine
- mass (kg)
- bom (reference to BOM)
- capabilities (list of process types + rates)
- Optional: power_draw_kW, notes
```
**Tokens saved:** ~600 (keep ~400)

### Section 5: Data Model - BOMs (lines 164-186)
**Content:** BOM structure
**Agent needs:** YES
**Keep:**
```
BOM:
- id, owner_item_id
- components: [{item_id, qty}, ...]
- Optional: scrap_rate, notes
```
**Tokens saved:** ~80 (keep ~80)

### Section 6: Data Model - Processes (lines 188-243)
**Content:** Process structure with inputs/outputs/resources
**Agent needs:** YES - CRITICAL
**Keep:**
```
PROCESS:
- id, name
- inputs: [{item_id, qty, unit}, ...]
- outputs: [{item_id, qty, unit}, ...]
- byproducts/waste (optional): [{item_id, qty, unit}, ...]
- resource_requirements: [{resource_type, amount, unit}, ...]
- time_model: fixed_time | linear_rate
- energy_model: kWh_per_kg_input | kWh_per_unit_output | kW_times_time
- notes
```
**Tokens saved:** ~120 (keep ~200)

### Section 7: Data Model - Recipes (lines 245-270)
**Content:** Recipe structure
**Agent needs:** YES
**Keep:**
```
RECIPE:
- id, target_item_id
- variant_id (optional: for multiple recipes)
- steps: [process_id, process_id, ...]
- assumptions, notes
```
**Tokens saved:** ~60 (keep ~80)

### Section 8-9: Resources & Transport (lines 272-336)
**Content:** Resource types and transport modeling
**Agent needs:** MINIMAL
**Keep:** Brief mention (~40 tokens)
**Tokens saved:** ~200

### Section 10: Repository Layout (lines 338-399)
**Content:** Directory structure
**Agent needs:** YES - Where to create files
**Keep:**
```
Directory structure:
kb/
├── items/materials/*.yaml
├── items/parts/*.yaml
├── items/machines/*.yaml
├── boms/*.yaml
├── processes/*.yaml
├── recipes/*.yaml
└── seeds/*.yaml
```
**Tokens saved:** ~180 (keep ~100)

### Sections 11-16: Compiler stages, Validation, Objectives, Rules, Scenarios, Deliverables (lines 401-644)
**Content:** How the engine works, validation details, system architecture
**Agent needs:** PARTIAL - Only validation rules
**Keep:** Condensed validation rules:
```
Validation:
Hard errors (must fix):
- Unknown units, negative quantities
- Dangling references in active recipes

Soft warnings (flag but allow):
- Mass imbalance in processes (unless waste declared)
- Missing mass for parts
- Missing recipe (becomes import)
- Missing energy/time models
```
**Tokens saved:** ~800 (keep ~150)

**Memo A Summary:**
- Current: ~3,026 tokens
- Optimized: ~1,150 tokens (core schema + validation)
- **Savings: ~1,876 tokens (62%)**

---

## Memo B Analysis (~2,035 tokens)

### Section 1: Purpose (lines 3-17)
**Content:** Why knowledge acquisition protocol exists
**Agent needs:** MINIMAL
**Keep:** "Extract structure before precision, tag uncertainty explicitly" (~15 tokens)
**Tokens saved:** ~60

### Section 2: Guiding Principles (lines 19-52)
**Content:** 4 principles for knowledge acquisition
**Agent needs:** PARTIAL
**Keep:**
```
Guidelines:
- Best-guess engineering allowed - must be labeled with provenance
- Unknowns are first-class: use null + confidence:unknown
- System should run with incomplete data
```
**Tokens saved:** ~120 (keep ~60)

### Section 3: Scope of Sources (lines 54-78)
**Content:** What papers to reference
**Agent needs:** MINIMAL
**Keep:** "Ellery defines structure, external sources provide rates/energies" (~15 tokens)
**Tokens saved:** ~100

### Section 4: What to Extract (lines 80-234)
**Content:** 5 categories from paper extraction
**Agent needs:** PARTIAL - Examples useful as patterns
**Keep:** Key examples only:
```
Common process patterns:
- Regolith handling: excavate, crush, grind, sieve, beneficiate
- Extraction: H2 reduction, carbothermal, electrolysis
- Manufacturing: cast, sinter, machine, assemble
- Material flows: regolith → powder → concentrate → metal/oxygen/slag
```
**Tokens saved:** ~400 (keep ~150)

### Section 5: LLM Extraction Protocol (lines 236-292)
**Content:** 3-pass paper extraction workflow
**Agent needs:** NO - Human workflow
**Keep:** Nothing
**Tokens saved:** ~240

### Section 6: Normalization Rules (lines 294-346)
**Content:** Naming, units, provenance tagging
**Agent needs:** YES - CRITICAL for consistency
**Keep:** All of it:
```
Normalization rules:
Naming:
- All IDs: lowercase_snake_case
- Materials: descriptive (regolith_powder, iron_ingot)
- Processes: verbs (crush_regolith, mre_oxygen_extraction)

Units (REQUIRED):
- Mass: kg
- Energy: kWh
- Time: hr
- Rates: kg/hr
- Distance: km

Provenance (SHOULD HAVE):
- value + source (ellery_2018, ai_estimate, etc.)
- confidence (low, medium, high)
- Use value:null + confidence:unknown for unknowns
```
**Tokens saved:** ~40 (keep ~200)

### Section 7: YAML Population Strategy (lines 348-367)
**Content:** Order to create files
**Agent needs:** MINIMAL
**Keep:** "Create processes first, then materials, then recipes. Defer machines/BOMs until bottlenecks emerge" (~25 tokens)
**Tokens saved:** ~90

### Section 8: When to Stop Modeling (lines 369-389)
**Content:** Import termination rule
**Agent needs:** YES
**Keep:**
```
When to import (give up):
- No recipe after research
- Estimated effort > mass impact
- Not in top contributors to mass/energy/time
```
**Tokens saved:** ~80 (keep ~80)

### Sections 9-12: Quality gates, Failure modes, Deliverables, Strategic insight (lines 391-455)
**Content:** Human workflow and meta-commentary
**Agent needs:** NO
**Keep:** Nothing
**Tokens saved:** ~280

**Memo B Summary:**
- Current: ~2,035 tokens
- Optimized: ~545 tokens (normalization + patterns + import policy)
- **Savings: ~1,490 tokens (73%)**

---

## Overall Summary

### Current State
- meta-memo.md: 1,593 tokens
- memo_a.md: 3,026 tokens
- memo_b.md: 2,035 tokens
- **Total: 6,654 tokens**

### Optimized for Agents
- Core principles: ~95 tokens (import policy + design philosophy)
- Schema & structure: ~1,150 tokens (required fields + validation)
- Normalization & patterns: ~545 tokens (naming, units, common patterns)
- **Total: ~1,790 tokens**

### Savings: ~4,864 tokens (73%)

---

## Recommended New "Agent Memo"

Create a single condensed memo combining the essential parts:

**Sections:**
1. Core Principles (~95 tokens)
2. Schema Reference (~1,150 tokens)
   - Required fields for each entity type
   - Validation rules
   - Directory structure
3. Normalization Guide (~545 tokens)
   - Naming conventions
   - Standard units
   - Provenance tagging
   - Common process patterns
   - When to give up

This would replace all three memos in the cached context, saving ~4,864 tokens while preserving all operationally critical information.
