# Cached Context for Autonomous Queue Agent

This context is cached and reused across all agent invocations.

---
## 1. Project Memos

### Meta-Memo (Project Overview)

Meta-Memo — Modeling Self-Replicating Lunar Industrial Systems
Purpose
The purpose of this project is to make self-replicating industrial systems analyzable, computable, and comparable.
Self-replication is often discussed qualitatively — as an idea, an architecture, or a long-term vision — but rarely as something that can be quantified:
 How much mass must be imported?
 How much energy is required per replication cycle?
 What limits the growth rate?
 Which components matter, and which can be safely ignored?
This project exists to answer those questions systematically, using a data-driven dependency graph that can be refined over time.

Motivation
1. Self-replication is a growth-rate problem, not a gadget problem
In lunar and space-industrialization contexts, the dominant constraint is not efficiency or elegance, but how fast production capacity can grow under extreme mass and energy constraints.
A system that is:
heavier but faster-replicating
 may dominate one that is:


lighter but slow to replicate


Understanding this requires explicit accounting of dependencies, throughput, energy, and time — not just architectural diagrams.

2. Existing work (including Ellery’s) defines structure but not closure
Alex Ellery’s work is unusually concrete in identifying:
the classes of machines required


the chemical reaction families


the importance of manufacturable actuation and computation


the recursive nature of production


However, this work stops short of:
closing the dependency graph


quantifying tradeoffs


computing replication cost or time


identifying dominant bottlenecks


This project treats Ellery’s work as a structural seed, not a finished model.

3. “Replicate everything” is a policy choice, not a claim
The project adopts the rule:
Anything that can’t be replicated locally is treated as imported.
This is not an assertion that full self-replication is achievable, but a modeling boundary condition that:
forces gaps to be explicit


assigns mass penalties to unknowns


avoids hand-waving about “assumed infrastructure”


This rule allows partial replication to be analyzed without pretending it is total replication.

4. Quantification reveals leverage
Only once the system is computable can we ask:
Which machines dominate imported mass?


Which processes dominate energy?


Which resource constrains replication time?


Where should modeling effort be spent next?


Without quantification, these questions are answered by intuition. With it, they can be answered by inspection.

Core Goal
The core goal is to build a computable, extensible representation of a self-replicating lunar seed factory that can:
enumerate its full dependency structure


account for mass, energy, time, and throughput


surface missing knowledge explicitly


be iteratively refined as better assumptions become available


The goal is not to prove feasibility, but to make feasibility (or infeasibility) legible.

Design Philosophy
1. Structure before precision
The project prioritizes:
correct dependency structure


conservation relationships


explicit flows


over:
precise chemistry


high-fidelity physics


tight tolerances


Coarse, wrong-but-useful numbers are acceptable if they preserve structure and are labeled as such.

2. Processes before machines
Manufacturing and ISRU are modeled as unit operations (processes), not bespoke machines.
Machines are treated as:
capacity providers for processes


bundles of resources


themselves products of other processes


This prevents premature commitment to specific designs.

3. Incompleteness is a feature
The system is designed to run even when:
many items are imported


many parameters are placeholders


large uncertainties exist


Incompleteness is surfaced, not hidden.

4. Iteration is guided by bottlenecks
Modeling effort is directed by outputs:
imported mass contributors


energy-dominant processes


time-dominant resources


This prevents modeling the long tail prematurely.

Ellery-Style Dependency Graph (Conceptual Backbone)
The project is grounded in a layered dependency graph inspired by Ellery’s work:
Layer 0 — Environment
vacuum


solar energy


lunar regolith


Layer 1 — Power & Actuation
power generation


motors and motion


basic distribution


Layer 2 — Regolith Handling
excavation


crushing


grinding


beneficiation


Layer 3 — Thermal & Chemical Primitives
furnaces


reactors


electrolysis


gas handling


Layer 4 — Oxygen & Metals Extraction
ilmenite reduction


carbothermal processes


molten regolith electrolysis


Layer 5 — Structural Materials
metals


glass


ceramics


Layer 6 — Manufacturing Capability
casting


sintering


machining


additive processes


Layer 7 — Assembly & Control
assembly processes


manipulators


low-precision control systems


Layer 8 — Recursive Closure
machines that make machines


expansion of production capacity


This graph is not assumed to be complete — it is the hypothesis under test.

Why Memos A and B Exist
Memo A (Software Spec) exists because:


without a formal representation, reasoning collapses into narrative


we need a compiler, not a whiteboard


Memo B (Knowledge Acquisition Protocol) exists because:


the data will be messy, incomplete, and LLM-assisted


without discipline, entropy overwhelms progress


Together, they allow:
Ellery’s qualitative insights


best-guess engineering assumptions


and future refinements


to coexist in a single evolving system.

Success Criteria (Early Phase)
The project is successful if it can:
run with incomplete data


compute total imported mass for a seed factory


identify top energy and time bottlenecks


clearly state what must be modeled next


Success is clarity, not optimism.

Non-Goals (Explicit)
Proving near-term feasibility


Designing a flight-ready factory


Resolving all chemistry or materials questions


Modeling precision manufacturing or electronics fabrication in detail


Those are downstream possibilities, not prerequisites.

Summary
This project treats self-replicating lunar industry not as science fiction, but as a systems-engineering object whose assumptions can be inspected, challenged, and improved.
By turning narrative architectures into dependency graphs with accounting, it aims to replace vague plausibility arguments with explicit tradeoffs — and to make growth, not elegance, the central quantity of interest.


### Memo A (Software Specification)

Memo A — Lunar Self-Replicating Factory Model: Software Specification (Data-First, Best-Guess Engineering)
Purpose
Build a Python-based compiler + accountant for an evolving manufacturing knowledge base describing a lunar seed factory capable of replicating itself to the maximum extent possible, with any gaps treated as imports. The system ingests YAML describing items, processes, machines/resources, and transport, compiles this into a quantitative dependency hypergraph, and produces scalar totals:
total imported mass


total local material throughput (e.g., regolith processed)


total energy per replication cycle


total machine-hours per machine type


a crude replication-time lower bound (optional, schedule-free)


It is explicitly designed for iterative refinement (“capture the entropy”): incomplete models should still run, produce outputs, and highlight missing/uncertain pieces.

Non-goals (for this phase)
No full discrete-event schedule, no Gantt chart requirement (architecture should permit later addition, but not constrain this phase).


No tolerance/precision modeling.


No high-fidelity thermodynamics or chemical kinetics (coarse blocks only).


No environmental externalities; waste can be tracked but not constrained.


No finite import cadence or supply chain constraints (imports are unlimited; mass is the penalty).



Core Conceptual Model
A. Two linked graphs, represented implicitly in data
Product Structure (BOM)


Machines and parts are made of subassemblies, parts, and materials.


This is a containment graph: Machine → Subassembly → Part → Material.


Process Network (Manufacturing/ISRU “unit operations”)


Processes transform inputs → outputs using resources and energy/time.


This is a hypergraph (many inputs, many outputs), best represented as:


Item(s) → ProcessStep → Item(s)


Key join: every manufacturable Item must have at least one Recipe, which is a graph of process steps that produces it (possibly via intermediates). If no recipe exists (or policy disables it), the item is an import.

Data Model (Concepts and Required Fields)
1) Items
Items are “things you can count” (mass, units). Three primary item kinds:
Material
Examples: regolith_raw, regolith_powder, ilmenite_concentrate, iron_ingot, oxygen_gas, glass_bulk, slag_tailings.
Required fields:
id (stable slug)


name


kind: material


unit (typically kg; sometimes m3, mol, kWh for bookkeeping—see “Resources vs Items” below)


density (optional but helpful)


notes (freeform)


Optional:
composition (coarse, e.g., oxide fractions or “unknown”)


state (solid/powder/liquid/gas)


source_tags (provenance)


Part
Examples: motor_stator, crucible, gearbox_housing, electrode_graphite_rod.
Required fields:
id


name


kind: part


mass (kg) or a parametric mass model placeholder with uncertainty


material_class (e.g., steel, aluminum, ceramic, glass, polymer) — coarse is fine


notes


Optional:
dimensions (coarse)


substitutable_with (list of alternative part ids)


uncertainty (distribution / min-mid-max)


Machine
Machines are also items (they can be built), but additionally can act as resources (capacity providers).
 Examples: ball_mill_v0, mre_reactor_v0, excavator_v0, casting_furnace_v0, hauler_v0.
Required fields:
id


name


kind: machine


mass


bom (a BOM reference; may be empty early)


capabilities (what process types it can run, with rates/limits)


Optional:
power_draw_kW (if treated as fixed)


duty_cycle assumptions


availability (fraction uptime)


uncertainty



2) BOMs
A BOM is a quantitative tree (or DAG) describing composition.
Required fields:
id


owner_item_id (the machine/part this BOM builds)


components: list of {item_id, qty}


Optional:
scrap_rate (fraction lost during assembly/manufacture)


fasteners_implicit flag (if you don’t want to enumerate bolts early)


notes, source_tags


Important: the BOM may be intentionally incomplete early. Missing components are allowed and simply reduce calculated mass closure (flagged in validation).

3) Processes (Unit Operations)
A Process is a parameterized transform with accounting.
Required fields:
id


name


inputs: list of {item_id, qty, unit}


outputs: list of {item_id, qty, unit}


byproducts / waste (optional but recommended): list of {item_id, qty, unit}


resource_requirements: list of {resource_type, amount, unit}
 (e.g., machine:ball_mill, machine_hours: 2 hr, or requires: hauler capacity)


time_model (coarse): one of:


fixed_time


linear_rate (e.g., time = setup + qty / rate)


energy_model (coarse): one of:


kWh_per_kg_input


kWh_per_unit_output


kW_times_time (power draw × computed time)


notes, source_tags


Conservation checks (soft early, strict later):
mass balance (allow losses to waste/byproducts)


unit consistency


non-negative yields



4) Recipes
A recipe says: “how do I make item X?” It can reference a single process or a chain.
Required fields:
id


target_item_id


variant_id (so multiple recipes can exist for same target)


steps: ordered list of process ids (or a small DAG if needed later)


assumptions (freeform) + source_tags


Optional:
applicability constraints (e.g., requires certain other materials or machines)


yield_overrides / rate_overrides (tuning knobs)


Policy: If multiple recipes exist, the planner/optimizer chooses one; if none, item becomes import.

5) Resources
Resources constrain throughput/time (even if you’re not scheduling yet). In this phase, resources are used mainly to compute machine-hours and identify bottlenecks.
Resource types:
machine_type (e.g., “ball_mill”, “furnace”, “electrolysis_cell”, “assembler”, “hauler”)


optionally power_bus (if you later add peak power constraints)


Resource definitions include:
id


type (machine_type / hauler / etc.)


count (how many available)


capacity (payload, volume, kg/hr, etc. — depending on type)


energy_intensity (for transport)


notes


Note: In Phase A, you can treat power as unconstrained (continuous power), so power bus constraints are not necessary.

6) Transport Model
Transport is represented as just another Process family (“move X kg over distance d using hauler type H”).
Transport step required fields:
cargo_item_id


distance_km (or distance bucket id)


hauler_type


payload_kg


speed_kmph


energy_kWh_per_km (or per tonne-km)


Outputs:
same cargo item (possibly with loss fraction)


This enables:
machine-hours for haulers


energy for hauling


time lower bound contributions (optional)



Repository / YAML Layout
Suggested structure (data repo):
schema/version.yaml — schema version, unit conventions


items/materials/*.yaml


items/parts/*.yaml


items/machines/*.yaml


boms/*.yaml — one BOM per complex item (or grouped)


processes/*.yaml — unit operations, grouped by domain:


processes/regolith_handling.yaml


processes/beneficiation.yaml


processes/oxygen_extraction.yaml


processes/metals.yaml


processes/glass_ceramics.yaml


processes/manufacturing.yaml


processes/assembly.yaml


processes/transport.yaml


recipes/*.yaml — recipe variants per target family


scenarios/*.yaml — defines “seed factory” composition + counts + objectives:


selected machine instances


available resource counts


policy toggles (allow/disallow certain recipe families)


objective definition (min import mass vs min time)



Compiler Stages (What the Python engine does)
Stage 1: Load + Normalize
Load YAML into in-memory objects.


Normalize IDs, units, and defaults.


Validate referential integrity (missing ids flagged but tolerated).


Outputs:
a canonical in-memory model


a validation report with severity levels


Stage 2: Build the dependency hypergraph
Construct an internal representation that links:
BOM edges: owner → component (qty)


Recipe edges: target item → recipe variant → process steps


Process hyperedges: inputs → process → outputs/byproducts


Resource edges: process → resource types


This is the core “entropy capture”: it makes the structure explicit even with placeholder numbers.
Stage 3: Scenario expansion (“what is one replication cycle?”)
Input: a scenario defining the seed factory “target set” (list of machines to replicate, quantities).
Steps:
Expand the seed factory into required items via BOM.


For each required item:


if it’s a material: accumulate demand


if it’s manufacturable and recipe exists: expand its recipe steps (and their input demands)


else: mark as import demand (mass counted)


Iterate until closure (no new demands) or until you hit recursion limits.


Important: prevent infinite loops with:
recursion detection (e.g., machine requires itself)


explicit “bootstrap exception list” (allowed circularity if imported initially)


Stage 4: Accounting (scalar totals)
Compute:
Imported mass: sum mass of imported parts/machines/materials


Local material demand: total kg of each material required per replication


Energy: sum of step energy models


Machine-hours by resource type: sum time requirements by required machine_type


Waste streams: total kg waste/byproducts per category


Optional:
Crude replication time bound:


For each machine type: work_hours / count


Take max (dominant bottleneck)


Stage 5: Reporting
Produce:
human-readable summary (markdown/text)


machine-readable results (JSON)


“Top bottlenecks” tables:


top energy-consuming processes


top machine-hour consumers


top imported mass contributors


“Missing knowledge” list:


items with no recipes


processes with placeholder energy/time


missing densities/masses



Validation & Quality Controls
Hard validations (fail scenario)
Unknown units


Negative quantities


Dangling references (item_id doesn’t exist) if used in scenario


Soft validations (warnings)
Mass imbalance in processes (unless waste/byproducts declared)


Missing mass for a part (treated as unknown; blocks imported mass calc for that part)


Missing recipe for an item (will become import; flagged)


Missing energy/time model (treated as unknown; totals partial; flagged)


Provenance & uncertainty
Every numeric parameter should be allowed to carry:
source: paper, ai_estimate, hand_assumption


confidence: low/med/high


optional distribution: min/mid/max


The engine should support computing:
deterministic totals (using midpoints)


optional Monte Carlo later (not required in Memo A, but schema should not block it)



Objective Switching (Architecture Requirement)
The dataset and compiler should support two primary objective families without restructuring:
Min imported mass


primary output: imported_mass_kg


secondary outputs: energy_kWh, replication_time_bound_hr


Min replication time bound


primary output: max(machine_hours/type_count)


constraint output: imported_mass_kg


Implementation note (spec-level): objectives live in scenario YAML; the engine simply computes metrics. Optimization can be a later module that searches over:
recipe variant choices


machine counts


policy toggles



“Bootstrap Reality” Rules (Your boundary condition encoded)
“Replicate everything” means: if an item has no enabled recipe, it is imported.


“Long tail termination” is natural: you only model what matters; everything else is import with mass penalty.


The system must be comfortable being wrong early — it should surface what dominates the totals so you know what to model next.



Minimal Scenario Definition
A scenario should specify:
target_seed_factory: list of {machine_id, qty}


available_resources: counts by machine_type (or derived from machine list)


policy:


enable/disable recipe families (e.g., allow vacuum tubes or not)


cap recursion depth


objective: min_import_mass or min_time_bound



Deliverables from this memo (what you can paste into a project plan)
A stable YAML schema and directory layout for items/processes/recipes/scenarios.


A compiler pipeline definition: load → graph → expand → account → report.


A clear separation between:


the knowledge base (YAMLs; evolves via Ellery + best-guess engineering)


the engine (Python; deterministic and testable)


A workflow-friendly set of “missing knowledge” outputs to guide iteration.


### Memo B (Knowledge Acquisition Protocol)

Memo B — Knowledge Acquisition & Normalization Protocol
(Ellery-seeded, Best-Guess Engineering, LLM-assisted)
Purpose
Define a repeatable, convergent process for turning Alex Ellery’s literature (plus adjacent ISRU/manufacturing sources) into a structured YAML knowledge base compatible with the Memo A software spec.
This memo is not about correctness on the first pass. It is about:
extracting structure before precision


tagging uncertainty explicitly


preventing entropy explosion as multiple LLM passes accumulate data


ensuring the dataset can run early and guide what to model next



Guiding Principles
Processes before machines


Unit operations (crush, grind, reduce, electrolyze, cast) are more stable than machine designs.


Machines are capacity providers for processes; BOM expansion is deferred until it matters.


Best-guess engineering is allowed — but must be labeled


Every numeric value has provenance (ellery_paper, nasa_report, ai_estimate, hand_assumption).


Unknowns are first-class citizens.


Iterative closure


The system should run even if half the world is imports.


Bottlenecks determine what to model next, not philosophical completeness.


LLMs produce deltas, not essays


Each extraction task yields YAML fragments + an assumption table + a “what’s missing” list.



Scope of Sources
Primary seed sources
Alex Ellery:


The Machine to End All Machines (2018)


I-SAIRAS papers on sustainable lunar exploration


Related ISRU/self-replication papers


Secondary enrichment (later passes)
NASA ISRU system studies (oxygen extraction, regolith handling)


ESA / Blue Origin / ICON public ISRU material


Terrestrial analogs (cement kilns, aluminum electrolysis, glass furnaces)


Policy: Ellery defines structure and intent. External sources are allowed to fill in rates, energies, and material properties.

What to Extract (Canonical Units of Knowledge)
Every source is mined for five categories, in this order:
1. Process Modules (highest priority)
Extract anything that looks like a unit operation:
Examples:
regolith excavation


crushing / comminution


sieving / classification


magnetic beneficiation


hydrogen reduction of ilmenite


carbothermal reduction


molten regolith electrolysis (MRE)


casting


sintering


glass melting


simple machining


assembly


For each process module, extract:
inputs (materials, consumables)


outputs (products, waste)


rough throughput (kg/hr or batch size)


rough energy intensity (kWh/kg or kW)


implied operating conditions (temperature, vacuum, continuous/batch)


implied required resource type (furnace, mill, reactor, hauler, assembler)


Rule: Even if numbers are missing, the process must exist as a named node.

2. Material Transformations
Extract:
which materials appear as intermediates


which materials are assumed recyclable


which materials are treated as losses/waste


Examples:
regolith → regolith_powder


ilmenite → iron + titania + oxygen


molten regolith → oxygen + metal alloy + slag


These populate materials.yaml and ensure mass flows can be closed later.

3. Implied Equipment (not yet full machines)
Ellery often says things like “a grinder,” “a furnace,” “a unit chemical processor.”
Extract these as resource types, not machines:
grinder


ball mill


furnace


electrolysis cell


casting mold


manipulator


hauler


Do not expand into full machines unless:
the equipment dominates mass/energy totals


or is clearly critical (motors, reactors, haulers)



4. Consumables & Wear Items
Extract anything that is used up:
electrodes


crucible liners


refractory coatings


lubricants


sacrificial reducing agents (C, H₂)


These become:
process inputs


later candidates for local manufacturing or import termination



5. Explicit Unknowns & Gaps
This is mandatory output.
For each source:
What does the paper assume exists but never describes?


What process clearly needs another upstream process?


What quantities are completely unspecified?


These gaps drive future modeling.

The LLM Extraction Protocol
Per-paper workflow
Each paper is processed in three LLM passes, each constrained and structured.

Pass 1 — Process Skeleton Extraction
Prompt intent: identify what exists, not how well it works.
LLM output (strict):
List of process modules (IDs + 1-sentence description)


List of materials mentioned or implied


List of resource types mentioned


List of consumables


No numbers required. No speculation.

Pass 2 — Quantitative Best-Guess Enrichment
Prompt intent: attach coarse numbers where possible.
For each process module:
plausible throughput range (min / typical / max)


plausible energy intensity range


batch vs continuous assumption


source of estimate (paper vs analogy vs AI guess)


LLM must output:
YAML fragment per process


a table of numeric assumptions with provenance



Pass 3 — Dependency Closure & Gap Identification
Prompt intent: find what’s missing.
For each process:
list required upstream processes not yet defined


list downstream processes that would consume outputs


list materials/equipment assumed but undefined


This is where the recursive nature emerges.

Normalization & Canonicalization Rules
These are non-negotiable and prevent entropy.
Naming
All IDs are lowercase snake_case.


Materials end in _material only if ambiguous; otherwise descriptive.


Processes are verbs: crush_regolith, mre_oxygen_extraction.


Units
Mass: kg


Energy: kWh


Time: hr


Rates: kg/hr


Distance: km


LLM outputs not in these units are converted or flagged.

Provenance tagging
Every numeric field must allow:
value


source (ellery_2018, nasa_isru, ai_estimate, etc.)


confidence (low, medium, high)


Missing tags are warnings.

Unknowns as explicit placeholders
If something is unknown, do not omit it.
 Use:
value: null


confidence: unknown


This allows the compiler to surface gaps.

YAML Population Strategy (Order Matters)
processes/ — create first, even with placeholders


materials.yaml — add only what processes require


resources.yaml — resource types, not machines


recipes/ — simple recipes mapping item → process chain


machines/ — only after bottlenecks emerge


boms/ — last, and only for critical machines


This avoids premature BOM explosion.

When to Stop Modeling and Import
A part/material becomes an import when any of the following hold:
no recipe exists after two modeling passes


estimated modeling effort > estimated mass impact


it does not appear in top-N contributors to:


imported mass


energy


machine-hours


This rule is explicit and mechanical, not aesthetic.

Quality Gates per Iteration
Each modeling iteration should end with:
A runnable scenario


A report showing:


top imported mass items


top energy-consuming processes


top machine-hour bottlenecks


A ranked list of “next things to model”


This closes the loop and prevents drift.

Expected Failure Modes (and how this protocol avoids them)
Over-specifying machines too early → avoided by process-first extraction


LLM hallucinated precision → provenance + confidence tags


Combinatorial explosion → import termination rule


Stalled progress waiting for perfect data → placeholders allowed everywhere



Deliverables of Memo B
A standard LLM prompt template for each extraction pass


A normalization checklist used after every LLM output


A curated process vocabulary seeded from Ellery


A disciplined rule for deciding what not to model



Strategic Insight (why this works)
Ellery gives you the shape of a self-replicating industrial ecology, but not the closure. This protocol turns his qualitative architecture into a computable, inspectable object — without pretending we know more than we do.
Once Memo A + Memo B are in place, the software becomes almost boring: it just compiles and reports. The real intellectual work lives in this memo.

If you want next steps, the obvious candidates are:
Draft the exact LLM extraction prompt for Pass 1–3


Do a pilot extraction on one Ellery paper to test entropy control


Define the initial scenario YAML (one minimal seed factory) purely to exercise the pipeline


Tell me which one you want to do next.


---
## 2. Knowledge Base Structure


The KB is organized as:

```
kb/
├── items/
│   ├── materials/    # Raw and processed materials (regolith, metals, glass, etc.)
│   ├── parts/        # Components (bearings, gears, electrodes, etc.)
│   └── machines/     # Equipment that provides manufacturing capacity
├── processes/        # Unit operations (crush, grind, cast, sinter, etc.)
├── recipes/          # How to make items (chains of processes)
├── boms/            # Bill of materials (item composition trees)
├── resources/       # Resource types (machine capabilities)
└── seeds/           # Seed configurations for analysis

Each YAML file defines one entity with:
- Unique `id` (lowercase snake_case)
- Required fields per kind (see memo_a.md)
- Optional provenance, notes, source_tags
```


---
## 3. Complex Examples (Templates)


Use these as templates when creating new KB entries.


### Process Examples

```yaml
# kb/processes/vacuum_tube_assembly_v0.yaml
id: vacuum_tube_assembly_v0
kind: process
name: Vacuum tube assembly
layer_tags:
- layer_7
- layer_8
inputs:
- item_id: tungsten_cathode_coated
  qty: 1.0
  unit: unit
- item_id: nickel_anode_plate
  qty: 1.0
  unit: unit
- item_id: fused_silica_envelope
  qty: 1.0
  unit: unit
- item_id: vacuum_seal_assembly
  qty: 1.0
  unit: unit
outputs:
- item_id: thermionic_vacuum_tube
  qty: 1.0
  unit: unit
requires_ids:
- vacuum_pump_small
- glassworking_station
- leak_test_equipment
resource_requirements:
- resource_type: labor_bot_general
  qty: 4.0
  unit: hr
energy_model:
  total_energy_kwh: 3.0
time_model:
  total_time_hr: 4.5
notes: Assembly of thermionic vacuum tube for solar power conversion. Install tungsten
  cathode (CaO-coated) and nickel anode inside fused silica envelope. Hermetic sealing
  under vacuum (10^-6 to 10^-7 torr). Critical process for thermionic converter production.
  Requires clean room conditions and leak-free seals. Leak testing verifies vacuum
  integrity. See design/solar_thermionics_report.md for specifications.
```

```yaml
# kb/processes/steel_refining_basic_v0.yaml
id: steel_refining_basic_v0
kind: process
name: Basic steel refining and casting
layer_tags:
- layer_4
- layer_5
inputs:
- item_id: iron_pig_or_ingot
  qty: 1.05
  unit: kg
outputs:
- item_id: steel_billet_or_slab
  qty: 1.0
  unit: kg
- item_id: slag
  qty: 0.05
  unit: kg
requires_ids:
- reduction_furnace
- casting_furnace
- molds
resource_requirements:
- resource_type: labor_bot_general
  qty: 0.6
  unit: hr
- resource_type: high_temperature_power_supply
  qty: 0.6
  unit: hr
energy_model:
  type: kWh_per_kg
  value: 1.5
  notes: Electric melting/refining and holding energy for pig iron to steel conversion;
    small-batch EAF/BOF analog.
time_model:
  type: fixed_time
  hr_per_batch: 2.0
  notes: Melt, refine (oxygen blow), and cast billets/slabs; batch cycle includes
    heat-up and tap.
notes: Refines pig iron into low-carbon steel and casts into billets/slabs for rolling.
  Includes decarburization and impurity removal with slag tapped separately.
```

```yaml
# kb/processes/strain_gauge_bonding_process_v0.yaml
id: strain_gauge_bonding_process_v0
kind: process
name: Strain gauge bonding process v0
layer_tags:
- layer_5
inputs:
- item_id: strain_gauge_foil_v0
  qty: 1.0
  unit: each
- item_id: adhesive_cyanoacrylate
  qty: 0.002
  unit: kg
- item_id: test_part_surface
  qty: 1.0
  unit: each
outputs:
- item_id: strain_gauge_bonded_assembly
  qty: 1.0
  unit: each
requires_ids:
- strain_gauge_bonding_station_v0
resource_requirements:
- resource_type: labor_bot_general
  amount: 0.5
  unit: hr
energy_model:
  type: kWh_per_batch
  value: 0.1
  notes: Minimal energy for surface prep and curing
time_model:
  type: fixed_time
  hr_per_batch: 1.0
  notes: Surface prep, application, alignment, curing
notes: 'Process for bonding strain gauges to test surfaces for structural monitoring.

  Source: docs/paper_reviews/paper_reviews_dec2024_comprehensive_v0 (seed file)

  Method: Adhesive bonding of foil strain gauge to cleaned surface

  Steps: Surface cleaning, adhesive application, gauge placement, curing

  Applications: Structural health monitoring, load testing, calibration

  Curing: Room temperature or low-heat accelerated cure

  Critical for: Validating structural designs, monitoring self-replicating system
  health

  '
```


### Recipe Examples

```yaml
# kb/recipes/recipe_press_hydraulic_v0.yaml
id: recipe_press_hydraulic_v0
kind: recipe
name: Recipe for hydraulic press
produces_id: press_hydraulic
produces_qty: 1.0
produces_unit: unit
steps:
- process_id: metal_casting_basic_v0
  notes: Cast frame, columns, and base (approx 600 kg)
- process_id: welding_brazing_basic_v0
  notes: Weld hydraulic cylinder mounting, reinforcement gussets
- process_id: machining_finish_basic_v0
  notes: Machine ram guides, platen surfaces, cylinder mounting bores
- process_id: assembly_basic_v0
  notes: Assemble hydraulic cylinders, rams, platens, pressure gauges
- process_id: hydraulic_system_integration_v0
  notes: Install hydraulic pump, valves, hoses, and pressure controls
- process_id: wiring_and_electronics_integration_v0
  notes: Install electrical controls, safety interlocks, pressure sensors
notes: Multi-purpose hydraulic press for bearing installation, forming, and press
  fit operations.
```

```yaml
# kb/recipes/recipe_heat_treatment_furnace_v0.yaml
id: recipe_heat_treatment_furnace_v0
kind: recipe
name: Recipe for heat treatment furnace
produces_id: heat_treatment_furnace
produces_qty: 1.0
produces_unit: unit
steps:
- process_id: metal_casting_basic_v0
  notes: Cast or fabricate outer shell and frame (approx 300 kg)
- process_id: refractory_lining_installation_v0
  notes: Install ceramic fiber or brick refractory insulation lining
- process_id: coil_winding_basic_v0
  notes: Wind or install resistive heating elements (nichrome or silicon carbide)
- process_id: wiring_and_electronics_integration_v0
  notes: Install temperature controllers, thermocouples, power relays, safety interlocks
- process_id: assembly_basic_v0
  notes: Assemble door, hinges, seals, ventilation system
notes: High-temperature furnace for heat treating metals with controlled atmosphere
  capability.
```


### Bom Examples


### Machine Examples

```yaml
# kb/items/machines/plate_rolling_mill.yaml
id: plate_rolling_mill
kind: machine
name: Plate rolling mill
mass: 1500.0
unit: kg
bom: bom_plate_rolling_mill_v0
capabilities:
- rolling
- metal_forming
- plate_production
material_class: steel
notes: Plate rolling mill for producing metal plate from ingots or billets. Heavy
  rollers compress heated metal through multiple passes to achieve desired thickness.
  Used for producing steel plate, sheet metal stock, and structural materials. Includes
  drive motors, roll adjustment, and heating system.
preferred_variant: simple
```

```yaml
# kb/items/machines/furnace_basic.yaml
id: furnace_basic
kind: machine
name: Basic furnace
mass: 300.0
unit: kg
material_class: steel
capabilities:
- heating
- melting
- heat_treating
bom: bom_furnace_basic_v0
notes: "Basic electric or fuel-fired furnace for heating, melting, and heat treatment.\
  \ Refractory-lined chamber with heating elements or burners. Temperature range 200-1200\xB0\
  C. Used for metal melting, heat treatment, ceramic firing, and process heating.\
  \ Includes temperature controller and insulation."
```

```yaml
# kb/items/machines/loom_or_knitting_machine.yaml
id: loom_or_knitting_machine
kind: machine
name: Loom or knitting machine
mass: 120
unit: kg
bom: bom_loom_or_knitting_machine_v0
material_class: steel
capabilities:
- weaving
- knitting
- fabric_production
notes: Textile manufacturing equipment for converting yarn into fabric. Can be either
  a loom for weaving or a knitting machine. Includes frame, tensioning system, pattern
  control, and drive mechanism.
```


### Part Examples

```yaml
# kb/items/parts/hydraulic_hose_assembly.yaml
id: hydraulic_hose_assembly
kind: part
name: Hydraulic hose assembly
mass: 3.0
unit: kg
material_class: composite
notes: Complete hydraulic hose assembly with reinforced rubber or thermoplastic hose,
  crimp fittings, and protective covering. Rated for high pressure (200-400 bar).
  Used for hydraulic power transmission in presses, cylinders, and mobile equipment.
  Includes both flexible hose and metal end fittings.
```

```yaml
# kb/items/parts/rectifier_full_bridge_v0.yaml
id: rectifier_full_bridge_v0
kind: part
name: Full-bridge rectifier module
mass: 0.3
unit: unit
material_class: electronic
notes: "Bridge rectifier module for AC\u2192DC conversion; diode pack with heat sink\
  \ and leads."
```

```yaml
# kb/items/parts/hammer_drive_motor.yaml
id: hammer_drive_motor
kind: part
name: Hammer drive motor
mass: 30.0
unit: kg
material_class: steel
notes: Drive motor for power hammer; coarse mass estimate.
```


### Material Examples

```yaml
# kb/items/materials/finished_part_deburred.yaml
id: finished_part_deburred
kind: material
name: Finished part (deburred)
mass: 1.0
unit: kg
material_class: metal
notes: 'Generic placeholder for a part after deburring operations.

  Represents any part that has had sharp edges, burrs, and flash removed.

  Used as output in deburring and finishing processes.

  Actual material properties depend on the input part being deburred.

  '
```

```yaml
# kb/items/materials/sintered_parts.yaml
id: sintered_parts
kind: material
name: Sintered parts
mass: 1.0
unit: kg
material_class: ceramic
notes: Parts produced by sintering process from powder metal or ceramic. Consolidated
  solid structure formed by diffusion bonding below melting point. Can be metal or
  ceramic depending on input powder.
```

```yaml
# kb/items/materials/iron_ore_or_ilmenite.yaml
id: iron_ore_or_ilmenite
kind: material
name: Iron ore or ilmenite
mass: 1.0
unit: kg
material_class: composite
notes: Iron-bearing ore for metal extraction. On the Moon, primary source is ilmenite
  (FeTiO3) found in lunar mare basalts, typically 10-20% by mass in regolith. Also
  available from NiFe meteorites. On Earth includes magnetite (Fe3O4), hematite (Fe2O3),
  and other iron oxides. Ilmenite processed by carbothermal reduction or hydrogen
  reduction to yield metallic iron and titanium oxide. Lunar ilmenite abundance makes
  it key feedstock for in-situ iron production. Raw ore requires crushing, concentration,
  and reduction/smelting to extract pure iron metal.
```


---
## 4. Available Papers


Papers are located in `design/papers/`. Use `rg_search` to search extracted text.


Available papers:

- ✓ `3-D-Printed-motors-2.pdf` → `3-D-Printed-motors-2.txt`
- ✓ `3D-Printed-Motor.pdf` → `3D-Printed-Motor.txt`
- ✓ `Affordable-rapid-bootstrapping-of-space-industry-and-solar-system-civilization.pdf` → `Affordable-rapid-bootstrapping-of-space-industry-and-solar-system-civilization.txt`
- ✓ `Alex-Ellery-CV-2023.pdf` → `Alex-Ellery-CV-2023.txt`
- ✓ `An-architecture-for-self-replicating-lunar-factories-Chirikjian.pdf` → `An-architecture-for-self-replicating-lunar-factories-Chirikjian.txt`
- ✓ `Bootstrapping-neural-electronics-from-lunar-resources.pdf` → `Bootstrapping-neural-electronics-from-lunar-resources.txt`
- ✓ `Control-of-Shape-Memory-Alloy.pdf` → `Control-of-Shape-Memory-Alloy.txt`
- ✓ `Ellery-Neural-Electronics-Lunar-2022.pdf` → `Ellery-Neural-Electronics-Lunar-2022.txt`
- ✓ `Ellery-Self-Replicating-Machines-Feasible.pdf` → `Ellery-Self-Replicating-Machines-Feasible.txt`
- ✓ `Engineering-a-lunar-photolithoautotroph-on-the-moon.pdf` → `Engineering-a-lunar-photolithoautotroph-on-the-moon.txt`
- ✓ `FFC-process-for-deep-ISRU.pdf` → `FFC-process-for-deep-ISRU.txt`
- ✓ `Heat-Pipe-Solar-Receiver-O2-2009.pdf` → `Heat-Pipe-Solar-Receiver-O2-2009.txt`
- ✓ `I-SAIRAS-2020-Sustainable-Lunar-Exploration.pdf` → `I-SAIRAS-2020-Sustainable-Lunar-Exploration.txt`
- ✓ `ISRU-Neural-Computing.pdf` → `ISRU-Neural-Computing.txt`
- ✓ `ISRU-Sensors.pdf` → `ISRU-Sensors.txt`
- ✓ `JHU-Self-Replicating-Robots-2002.pdf` → `JHU-Self-Replicating-Robots-2002.txt`
- ✓ `Lunar-Demandite.pdf` → `Lunar-Demandite.txt`
- ✓ `Lunar-ISRU-2019-Lomax.pdf` → `Lunar-ISRU-2019-Lomax.txt`
- ✓ `MIT-ISRU-Architecture-2008.pdf` → `MIT-ISRU-Architecture-2008.txt`
- ✓ `NASA-ICES-2024-ISRU-Modeling.pdf` → `NASA-ICES-2024-ISRU-Modeling.txt`
- ✓ `NASA-ISRU-Progress-2012.pdf` → `NASA-ISRU-Progress-2012.txt`
- ✓ `NASA-Lunar-Polar-Illumination-2008.pdf` → `NASA-Lunar-Polar-Illumination-2008.txt`
- ✓ `NASA-TM-20210009988-Bootstrapping-Space-Industry.pdf` → `NASA-TM-20210009988-Bootstrapping-Space-Industry.txt`
- ✓ `NIAC-Chirikjian-Self-Replicating-Lunar-Factories.pdf` → `NIAC-Chirikjian-Self-Replicating-Lunar-Factories.txt`
- ✓ `NPV-cost-benefit-analysis-of-self-replication.pdf` → `NPV-cost-benefit-analysis-of-self-replication.txt`
- ✓ `NSS-Bootstrapping-Lunar-Industry-2016.pdf` → `NSS-Bootstrapping-Lunar-Industry-2016.txt`
- ✓ `Power-on-the-Moon-using-ISRU.pdf` → `Power-on-the-Moon-using-ISRU.txt`
- ✓ `RepRap-Robotica-2011.pdf` → `RepRap-Robotica-2011.txt`
- ✓ `Rover-Prospecting-and-Mining.pdf` → `Rover-Prospecting-and-Mining.txt`
- ✓ `Self-Assembling-Structures.pdf` → `Self-Assembling-Structures.txt`
- ✓ `Self-Replicating-Machines-on-the-Moon.pdf` → `Self-Replicating-Machines-on-the-Moon.txt`
- ✓ `Sustainable-ISRU-on-the-Moon.pdf` → `Sustainable-ISRU-on-the-Moon.txt`
- ✓ `TTU-Thermal-Design-ISRU.pdf` → `TTU-Thermal-Design-ISRU.txt`
- ✓ `UCF-ISRU-Modeling-Optimization.pdf` → `UCF-ISRU-Modeling-Optimization.txt`
- ✓ `building-physical-self-replicating-machines.pdf` → `building-physical-self-replicating-machines.txt`
- ✓ `ceramics-08-00107.pdf` → `ceramics-08-00107.txt`
- ✓ `ellery-2021-generating-and-storing-power-on-the-moon-using-in-situ-resources.pdf` → `ellery-2021-generating-and-storing-power-on-the-moon-using-in-situ-resources.txt`
- ✓ `ellery-2021-leveraging-in-situ-resources-for-lunar-base-construction.pdf` → `ellery-2021-leveraging-in-situ-resources-for-lunar-base-construction.txt`
- ✓ `ellery-et-al-2022-metalysis-fray-farthing-chen-process-as-a-strategic-lunar-in-situ-resource-utilization-technology.pdf` → `ellery-et-al-2022-metalysis-fray-farthing-chen-process-as-a-strategic-lunar-in-situ-resource-utilization-technology.txt`
- ✓ `sustainable-lunar-exploration-through-self-replicating-robots.pdf` → `sustainable-lunar-exploration-through-self-replicating-robots.txt`


Key papers from Alex Ellery:
- Ellery's work on self-replicating lunar systems is canonical
- Focus on processes, ISRU methods, and manufacturable actuation
- Papers describe chemical reaction families and machine classes
- Use as primary source for process parameters and material flows


---
## 5. Queue Workflow

# Multi-Agent Queue Usage

## REQUIRED READING FIRST

**Before working on the queue, you MUST read:**
1. `design/meta-memo.md` — Project overview and goals
2. `design/memo_a.md` — Specification and design principles
3. `design/memo_b.md` — Knowledge acquisition methodology

See `docs/README.md` for full onboarding documentation.

## Queue Operations

- IDs are stable: `id = "<gap_type>:<item_id>"` with `gap_type`, `item_id`, `reason`, `context`, `status`, `lease_id`, `lease_expires_at`.
- Always lease before editing:
  - Lease: `.venv/bin/python -m kbtool queue lease --agent <name> [--ttl 900] [--priority gap1,gap2]`
    - Only one lease per `item_id` is allowed; if another entry with the same `item_id` is leased, the request is denied.
  - Complete: `.venv/bin/python -m kbtool queue complete --id <gap_type:item_id> --agent <name>`
  - Release: `.venv/bin/python -m kbtool queue release --id <gap_type:item_id> --agent <name>`
  - GC expired leases: `.venv/bin/python -m kbtool queue gc [--prune-done-older-than N]`
  - List: `.venv/bin/python -m kbtool queue ls`
- Do not edit items you haven’t leased. If you find another agent’s edits, reconcile rather than overwrite; leave context in `notes`.
- Indexer rebuilds the queue each run, preserving leases/done status; gaps resurface if fixes are incomplete.
- Pruning only removes items marked `resolved`/`superseded`; gaps persist until fixes land.


---
## 6. Gap Types and Validation


The indexer identifies several gap types:

1. **missing_field** - Required fields not populated
   - Examples: `material_class` for parts, `energy_model` for processes
   - Fix: Research similar items and add the missing field

2. **no_recipe** - Items without manufacturing recipes
   - These will be treated as imports unless a recipe is created
   - Fix: Create a recipe referencing appropriate processes

3. **unresolved_ref** - Free-text requirements needing definition
   - Example: `requires_text: ["ball mill or grinder"]`
   - Fix: Replace with structured `requires_ids` or create the missing item

4. **referenced_only** - IDs referenced but not defined
   - Fix: Create the missing item definition

5. **import_stub** - Recipes marked as imports needing local manufacturing
   - Fix: Replace import recipe with actual manufacturing steps

6. **no_provider_machine** - Resource types with no machine providing them
   - Fix: Add capability to an existing machine or create a new machine

The indexer outputs:
- `out/work_queue.jsonl` - All gaps (rebuilt each run)
- `out/validation_report.md` - Detailed validation results
- `out/unresolved_refs.jsonl` - Unresolved references
- `out/missing_fields.jsonl` - Missing required fields


---
## 7. Best Practices


When filling gaps:

1. **Research first**: Use `rg_search` to find similar items in the KB
2. **Follow patterns**: Use the complex examples above as templates
3. **Be specific**: Use proper IDs, units, and structure
4. **Add context**: Include notes explaining assumptions or sources
5. **One item well**: Focus on quality over quantity
6. **Let indexer guide**: Don't try to anticipate downstream gaps
7. **Conservative assumptions**: When uncertain, use reasonable defaults from similar items
8. **Provenance**: Note sources in comments (e.g., "Based on ball_mill_v0")

File naming conventions:
- Items: `{category}_{description}_v{N}.yaml` (e.g., `ball_mill_v0.yaml`)
- Processes: `{action}_{target}_{variant}.yaml` (e.g., `crushing_basic_v0.yaml`)
- Recipes: `recipe_{target}_v{N}.yaml` (e.g., `recipe_steel_ingot_v0.yaml`)
- BOMs: `bom_{owner_item}_v{N}.yaml` (e.g., `bom_ball_mill_v0.yaml`)

Required fields by kind:
- **Material**: id, name, kind: material, unit (usually kg)
- **Part**: id, name, kind: part, mass, material_class
- **Machine**: id, name, kind: machine, mass, capabilities (optional: bom)
- **Process**: id, name, inputs, outputs, resource_requirements, energy_model, time_model
- **Recipe**: id, target_item_id, steps (list of process_ids)
- **BOM**: id, owner_item_id, components (list of {item_id, qty})
