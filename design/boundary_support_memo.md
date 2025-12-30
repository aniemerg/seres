Subject: Boundary time/energy model support - current mismatch and decision points

Context
- Documentation currently describes a "boundary" time_model/energy_model type for terminal/import-like processes.
- ADR-017 validators and ADR-012/014 schemas do not accept "boundary" types.
- Two processes were using boundary types: `steel_bar_raw_production_v0` and `immune_response_manufacturing_v0`.
- As a stopgap, these were migrated to `process_type: batch` with `fixed_per_batch` placeholders to satisfy validation.

Clarified desired semantics (from feedback)
- Boundary should represent *in-situ extraction* of raw lunar resources (e.g., regolith/ice) only.
- Earth-sourced materials should be **imports** (explicit import items/recipes), not boundary.
- Everything else should be manufacturable from imports + boundary outputs.
- Boundary indicates "no required material inputs," but should still:
  - Have time/energy totals (not zero by default).
  - Use a machine/resource requirement (e.g., mining equipment).
  - Be traceable in closure analysis.
- Boundary as a **third process_type** could signal "inputs optional/none" while still using time/energy models.

Observed mismatch
- Docs: boundary types are encouraged for terminal nodes (ambiguous between imports vs in-situ).
- Code: schema/validators/calculations only allow `batch` or `linear_rate` time models and `per_unit` or `fixed_per_batch` energy models.
- Result: boundary types fail validation and block queue completion.

Why this matters
- Boundary nodes are conceptually useful for *in-situ* resource collection (regolith/ice).
- Forcing them into `batch` is semantically awkward and can be misleading in downstream calculations.
- Multiple agents will keep hitting this mismatch if boundary appears in templates or future additions.

Options
1) Add boundary support as **process_type: boundary** (recommended if boundary is a core concept).
   - Semantics: no material inputs required, but time/energy and machine use are modeled.
   - Pros:
     - Aligns code with intended in-situ resource collection semantics.
     - Avoids placeholder "fake batches" for mining/collection.
   - Cons:
     - Requires updates in schema, validators, calculations, docs/tests.
     - Need to decide how boundary interacts with closure and scaling.
2) Remove boundary concept from docs and enforce batch placeholders.
   - Pros:
     - Keeps code simple and consistent with current validators.
   - Cons:
     - Semantics are muddy; boundary processes look like real work.
     - Requires consistent conventions for placeholder values across the KB.

Implementation notes if adding boundary support
- Schema updates:
  - Add `process_type: boundary` to the allowed values in `Process`.
  - Keep time_model and energy_model as standard types (batch or linear_rate), since boundary should still have time/energy.
  - Enforce "no material inputs" rule for boundary (inputs may be empty list only).
- Validator updates:
  - Allow `process_type: boundary`.
  - For boundary: allow inputs to be empty; require outputs, time_model, energy_model, and machine/resource requirements.
  - Skip scaling_basis checks only if a boundary uses fixed_per_batch/batch; if linear_rate/per_unit, scaling_basis should still be required.
- Calculations updates:
  - Use existing batch/linear_rate calculations; boundary only changes input requirements and validation rules.
  - Ensure closure treats boundary outputs as in-situ sources (not imports).
- CLI/auto-fix:
  - Auto-fix should not coerce boundary to batch/continuous.
- Docs:
  - Define boundary as in-situ resource collection (regolith/ice), not imports.
  - Provide examples of boundary mining processes and their outputs.

Unknowns / questions
- Should boundary be a third `process_type` (preferred) or a special flag on batch/continuous?
- Should boundary be allowed to use linear_rate/per_unit models (to capture throughput), or restricted to batch/fixed_per_batch?
- Should boundary outputs be the only allowed sources of regolith/ice (i.e., remove raw in-situ items from KB)?
- Should imports remain distinct (import items/recipes only), and how should closure report boundary vs import fractions?
- Are there other files already using boundary (beyond the two found)?

Recommendation
- Treat boundary as a first-class concept **for in-situ resource collection only**.
- Implement `process_type: boundary` with standard time/energy models and machine use.
- Keep imports separate (explicit import items/recipes).
- Remove boundary references for non-mining placeholders (e.g., `steel_bar_raw_production_v0`, `immune_response_manufacturing_v0`).
