

## Memo: Build v0 of the Lunar Factory KB + Index + Agent Loop

### 0) Goal and non-goals

**Goal:** implement the smallest runnable pipeline that:

1. stores KB YAML files for **processes / items / resources / recipes**
2. builds a **Central Index** from those YAML files
3. supports a **Writer Agent** loop that creates *one new YAML item per call*, with **dangling references allowed**
4. produces a **work queue** that alternates Ellery layers (0→8→0→…) and expands both backward and forward.

**Non-goals (v0):**

* no optimization, no scheduling/Gantt
* no strict canonical vocabulary enforcement
* no perfect dedup; do reconciliation later
  (Consistent with Memo A + Meta-Memo emphasis on “structure before precision.”)

---

### 1) Repository layout (data + generated artifacts)

Create (or confirm) these folders:

* `design/` (already exists)

  * `design/papers/` (Ellery txt files; optional inspiration corpus)
  * `design/memos/` (keep Memo A/B + meta-memo + future notes)
* `kb/` *(human-authored + agent-authored YAML)*

  * `kb/schema/` (schema version + JSONSchema/Pydantic model)
  * `kb/processes/`
  * `kb/items/materials/`
  * `kb/items/parts/`
  * `kb/items/machines/`
  * `kb/resources/`
  * `kb/recipes/`
  * `kb/scenarios/`
* `out/` *(generated)*

  * `out/index.json` (or sqlite)
  * `out/validation_report.md`
  * `out/work_queue.jsonl`
  * `out/unresolved_refs.jsonl`
  * `out/alias_suggestions.jsonl`

This matches Memo A’s suggested structure, but keep it minimal at first.

---

### 2) YAML dialect + schema versioning

**Decision:** YAML 1.2, parsed with Python (`ruamel.yaml` preferred for round-trip edits).

Add `kb/schema/version.yaml`:

* `schema_version: 0.1`
* `id_rules: lowercase_snake_case`
* base units: kg, kWh, hr (as in Memo A/B)

Implement:

* Pydantic models (or JSONSchema) for *at least*:

  * `Process`
  * `Item` (material/part/machine)
  * `ResourceType`
  * `Recipe`
* “soft validation”: allow missing numeric fields and dangling references, but **record them**.

---

### 3) Central Index: data model (the coordination brain)

Implement `Index` as JSON (later migrate to sqlite if needed). Minimum fields:

**For every node (process/item/resource/recipe):**

* `id`, `kind` (`process|material|part|machine|resource_type|recipe`)
* `status`: `defined | referenced_only | deprecated | alias`
* `defined_in`: filepath if defined
* `refs_out`: list of referenced IDs (even if missing)
* `refs_in`: reverse refs (who references this)
* `layer_tags`: optional list (`layer_0`…`layer_8`)
* `aliases`: optional list of strings

**For unresolved references:**

* `ref_string` (raw text if not an ID)
* `context`: `{owner_id, owner_kind, field_path}`
* `first_seen_in`, `count`, `priority_score`

Key design choice you asked for:

* allow requirements to be expressed as **plain English “requirement strings”** (ex: `"ball mill"`) that later get resolved to `ball_mill_v0` or similar.

So: store two parallel forms:

* `requires_ids: [...]` when known
* `requires_text: [...]` always allowed

---

### 4) Indexer: when/how it runs

Implement the indexer as **deterministic code** (not an agent):

**Entry points (v0 pick one, but design for both):**

1. `python -m kbtool index`

   * scans `kb/**/*.yaml`
   * parses, validates (soft), updates `out/index.json`
2. optional: filesystem watch mode

   * `python -m kbtool watch`
   * re-index on file write

In v0, keep it simple: *every agent run ends by calling the indexer CLI*. That answers “how does it get called?” without needing daemonization.

---

### 5) Writer Agent: one item per call

**Unit of work:** exactly one YAML file per call (your preference).

Inputs to the Writer Agent:

* `work_item` (define a specific process/resource/machine/material/recipe)
* “why now” (what referenced it, or which layer seed triggered it)
* relevant slice of index (top matches + nearby graph neighborhood)
* optional: snippets from `design/papers/` when the work item is tied to a paper domain

Outputs:

* a single YAML file placed under correct folder
* `requires_text` entries are allowed and encouraged if no canonical ID exists yet

---

### 6) Work queue manager: alternating Ellery layers + pressure-based expansion

Seed the queue using the **Layer 0–8** backbone from the Meta-Memo.

**Queue policy:**

* Maintain 9 per-layer subqueues.
* Pop in round-robin: `0,1,2,3,4,5,6,7,8,0,1,…`
* Within a layer, prioritize items using a score:

  * high if referenced by many defined nodes (backward pressure)
  * high if it produces outputs consumed by many processes (forward opportunity)
  * diversity penalty (avoid 10 motors in a row)

**Where do new work items come from?**

* After each indexing pass:

  * any unresolved `requires_text` gets enqueued for *resolution* (Linker step) OR for *definition*
  * any `referenced_only` IDs get enqueued for definition
  * optionally, “forward chain” suggestions: for new outputs, propose downstream processes that consume them (even as stubs)

This implements Memo B’s “dependency closure & gap identification” as a mechanical loop.

---

### 7) Linker / Reconciler (v0 lightweight)

Implement a **semi-automatic** linker pass:

**Inputs:**

* `out/unresolved_refs.jsonl`
* current `out/index.json`

**Outputs:**

* either: update YAML references to canonical IDs
* or: create an alias node
* or: enqueue a new definition

Mechanics:

* fuzzy match unresolved strings against:

  * existing IDs
  * `name` fields
  * `aliases`
* propose top N candidates with a confidence score
* if confidence > threshold, auto-link; else emit `alias_suggestions.jsonl` and enqueue a “human review” work item

---

### 8) Handling splits (furnace → glass_furnace + metal_furnace)

You called out a real pain point. Here’s a v0 approach that avoids mass-editing everything immediately:

**Add an explicit “alias / abstract” mechanism** in the index:

* Keep `furnace` as a **resource_type** but mark it as:

  * `status: deprecated` or `status: alias`
  * `redirects_to: [glass_furnace, metal_furnace]`
  * `split_policy: lazy`

**Lazy resolution rule:**

* If a process requires `furnace` and does not specify material domain, keep it.
* If a process is in domain `glass_ceramics` (layer 5/6-ish), linker can automatically rewrite `furnace → glass_furnace`.
* If it’s `metals` or `oxygen_extraction` thermal steps, rewrite `furnace → metal_furnace`.

So: “split” becomes a *mapping layer*, not a refactoring event. Later, if you want, you can run a bulk “normalize references” migration.

---

### 9) Minimal runnable scenario + reporting (close the loop)

Per Memo A, v0 should already compile and report “what’s missing / what dominates.”

Implement:

* `python -m kbtool report --scenario kb/scenarios/min_seed.yaml`
* produce:

  * imported mass top items (will be huge early; that’s fine)
  * energy totals (partial)
  * machine-hours by resource_type (partial)
  * missing recipes / missing masses list

This is how you prevent drift and decide what to model next (Meta-Memo + Memo B).

### 10) Bootstrapping plan: get **breadth fast**, but keep **enough specificity** to generate machines/parts

You’re basically choosing between “stubs everywhere” vs “a few concrete anchors.” Do both:

#### 10.1 Two-tier seeding: Anchors + Stubs

* **Anchors (10–20 items)**: moderately specific processes that *force* equipment/parts/materials to appear (ball mill, kiln/furnace, electrolyzer, casting, etc.). These create real dependency pressure quickly.
* **Stubs (1–3 per Ellery layer)**: ultra-light “process family” nodes that exist mainly to preserve breadth and guide future expansion (excavation family, thermal processing family, etc.).

Run the queue round-robin across layers, but allow anchors to “jump the line” when they create lots of unresolved refs.

#### 10.2 A concrete initial seed set (suggested)

Keep them as **processes** (process-first), but each should have `requires_text` that is specific enough to imply machines/parts later.

**Layer 0–1 (site ops / feedstock handling)**

1. `excavate_regolith_surface_v0` (scoop + haul + dump)
2. `regolith_screening_sieving_v0` (coarse/fine separation)
3. `regolith_crushing_grinding_v0` (ball mill / jaw crusher choice left open)

**Layer 2–3 (beneficiation / volatiles / oxygen)**
4) `beneficiate_regolith_magnetic_v0` (magnetic separator)
5) `oxygen_extraction_molten_regolith_electrolysis_v0` (MRE “anchor”)
6) `oxygen_extraction_carbothermal_reduction_v0` (alternate anchor; creates furnace + carbon + offgas handling)

**Layer 4–5 (metals / glass / ceramics / binders)**
7) `iron_reduction_from_ilmenite_v0` (or generic “metal oxide reduction” if you want broader)
8) `glass_melting_and_forming_v0` (glass furnace appears early)
9) `basalt_fiber_production_v0` (creates spinnerets/nozzles, tension control parts)

**Layer 6–7 (parts fabrication / joining)**
10) `metal_casting_basic_v0` (sand/investment casting; creates molds, crucibles)
11) `sintering_and_hot_pressing_v0` (creates presses, dies)
12) `welding_brazing_basic_v0` (creates power electronics, electrodes)

**Layer 8 (power / control / utilities)**
13) `solar_power_generation_basic_v0` (even if “imported PV,” it forces power accounting)
14) `power_storage_basic_v0` (batteries vs flywheel as unresolved choice)
15) `thermal_management_radiators_basic_v0`

That’s already broad, but each one is “machine-generative.”

#### 10.3 How the Writer Agent should write these (to preserve specificity without overfitting)

For each process YAML:

* Always include:

  * `inputs` / `outputs` (can be approximate)
  * `requires_text`: **short noun phrases** with optional qualifiers

    * Good: `"ball mill (50 kg/hr throughput)"`, `"glass furnace (1200–1500 C)"`, `"magnetic separator (drum)"`.
    * Avoid: long paragraphs.
* If uncertain between alternatives, list both:

  * `requires_text: ["ball mill OR jaw crusher", "screen/sieve"]`
  * The linker/reconciler can later choose or split into variants.

This gives you breadth while keeping each node actionable.

#### 10.4 Breadth control: round-robin layers + “pressure” interrupts

Keep your `0,1,2,…,8,0,1…` round robin, but add two interrupt rules:

* **High-pressure unresolved refs**: if a new process creates an unresolved requirement referenced by ≥N nodes (say N=3), enqueue it immediately.
* **Unlockers**: if defining one machine would resolve ≥M unresolved refs (say M=5), it jumps earlier.

So you get breadth, but the graph still *tightens*.

#### 10.5 Early split-safe handling (“furnace” example)

When seeds reference `"furnace"`, do it as:

* `requires_text: ["furnace (high-temp)"]`
  Later you can split lazily by creating:
* `resource_type: furnace` with `redirects_to: [metal_furnace, glass_furnace]`
  and a reconciler rule:
* if process has `domain: glass_ceramics` → rewrite to `glass_furnace`
* if `domain: metals` / `oxygen` thermal → rewrite to `metal_furnace`

This prevents early schema bikeshedding but still supports principled splits.

#### 10.6 “Breadth now, precision later” guardrails (so it doesn’t become mush)

Two guardrails only:

1. **Requirement strings must be short** (≤ ~8 words) so they’re matchable.
2. Every process must include **at least one concrete piece of equipment** (even if generic), so you don’t end up with purely conceptual nodes.

---

If you want, I can also give you a **ready-to-paste “Seed Queue JSONL”** for these (layer-tagged + round-robin ordering) so you can drop it straight into `out/work_queue.jsonl`.
