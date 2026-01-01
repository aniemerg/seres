NOTE: Historical document. Superseded by docs/kb_schema_reference.md.

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
