NOTE: Historical document. Superseded by docs/knowledge_acquisition_protocol.md.

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
