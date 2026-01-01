NOTE: Historical document. Superseded by docs/project_overview.md.

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
