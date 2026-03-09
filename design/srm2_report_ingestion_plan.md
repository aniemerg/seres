# SRM2 Research Report Ingestion Plan

Inputs:
- `design/srm2_bom_research_results/*.md` (research-agent outputs)
- `design/self_replicating_machines_2_kb_enrichment_plan.md`

Policy basis reviewed:
- `docs/project_overview.md`
- `docs/kb_schema_reference.md`
- `docs/knowledge_acquisition_protocol.md`
- `docs/parts_and_labor_guidelines.md`
- `docs/conservative_mode_guide.md`
- `docs/ADRs/018-recipe-inputs-outputs-validation.md`

## Operating Rules for Ingestion
- Prefer reuse over creation (5x equivalence rule).
- Processes before machines; avoid introducing a machine if labor bot + tools is sufficient.
- If capability exists under another ID, map/alias/update references instead of adding new ID.
- Keep software/intangibles out of BOM and material flow.
- For uncertain/high-complexity items, allow `is_import: true` as interim boundary.
- New process/recipe entries must satisfy current schema (`process_type`, `time_model`, `energy_model`, resolvable recipe I/O).

## Standard Ingestion Workflow (Apply to Every Report)
1. Extract candidate entities from report:
   - processes, machines, parts, materials, resources, and any explicit I/O.
2. KB mapping pass:
   - find exact ID matches.
   - find equivalent/near-equivalent IDs by function/material class.
3. Decision gate (Conservative Mode):
   - `reuse existing`
   - `add variant`
   - `add new`
   - `defer/import`
4. Process-centric modeling:
   - define process steps and I/O first.
   - add machine entries only if capability cannot be represented by existing machine + tool stack.
5. BOM readiness check:
   - do we have enough research detail for a defendable BOM?
   - if not, create minimal placeholder with explicit uncertainty notes and queue follow-up.
6. Validation readiness:
   - confirm units, target outputs, and step I/O closure (ADR-018 behavior).
7. Produce one mini-spec per accepted delta:
   - IDs, rationale, I/O, required machines, substitution decision, uncertainty.

## Output Artifacts Per Report
For each `design/srm2_bom_research_results/NN_*.md`, produce:
- `decision`: reuse / variant / new / defer
- `kb_mapping`: existing IDs used or replaced
- `delta_list`: exact YAML entries to add/update
- `risks`: schema/policy/data risks
- `confidence`: H/M/L

## Report-by-Report Next Step Plan

### 01 Prospecting Module
Next step:
- Model as rover tool modularity, not standalone survey process.
- Check whether to add `prospecting_module_v0` part/machine or just capability tags on existing rover.
Decision focus:
- Reuse `kapvik_microrover_30kg_v0` + new module part preferred.
Expected delta type:
- likely `part/machine` additions + recipe/BOM, minimal new process.

### 02 Magnetometer Payload
Next step:
- Compare proposed payload against existing sensor/measurement parts.
- Determine if a dedicated payload ID is justified.
Decision focus:
- add `magnetometer_payload_v0` only if no equivalent sensor module exists.
Expected delta type:
- small new part + assembly recipe (+ optional integration step in prospecting module BOM).

### 03 Electrostatic Separator Machine
Next step:
- Compare to existing beneficiation machines (`magnetic_separator*`, `gravity_separator`, `centrifugal_separator`).
- Decide on new machine ID vs extending existing machine capabilities.
Decision focus:
- likely net-new machine due to distinct physics/high-voltage requirements.
Expected delta type:
- new machine + BOM + recipe + capability list.

### 04 Electrostatic Beneficiation Process
Next step:
- Map to existing beneficiation item IDs (`anorthite_ore`, `pyroxene_concentrate`, `non_magnetic_tailings`).
- Define explicit step I/O and machine requirements.
Decision focus:
- add process (likely new) with conservative splits and explicit uncertainty.
Expected delta type:
- new process + at least one recipe variant using it.

### 05 Liquation Fe/TiO2 Separation
Next step:
- Connect to existing ilmenite reduction outputs and Fe/TiO2 item IDs.
- Define whether this is a standalone process or embedded as a step in existing ilmenite route.
Decision focus:
- favor variant process before introducing new material intermediates.
Expected delta type:
- process variant + recipe variant.

### 06 Quartz Piezo Sensor Fabrication
Next step:
- Map to existing `quartz_crystal` and sensor/electrode parts.
- Decide if this produces a new sensor part or upgrades existing sensor chain.
Decision focus:
- add process/recipe if no equivalent tactile pressure sensor exists.
Expected delta type:
- new part + process + recipe; possibly reuse existing assembly machines.

### 07 Wheatstone Bridge Module
Next step:
- Search existing circuitry modules for equivalent bridge topology.
- If missing, create module part with clear inputs and assembly path.
Decision focus:
- likely new part; process may reuse generic PCB/passive assembly steps.
Expected delta type:
- new part + recipe, minimal process additions.

### 08 Selective Solar Sinterer
Next step:
- Compare against existing solar concentrator + furnace + 3D printer machines.
- Decide whether a capability extension can avoid a full new machine.
Decision focus:
- if distinct motion/control + thermal deposition needed, add new machine variant.
Expected delta type:
- machine variant + BOM/recipe; optional operation process.

### 09 EBAM Printer
Next step:
- Compare with current 3D printer and vacuum/electron-gun chains.
- Identify irreducible unique subsystems (electron gun, HV, vacuum chamber).
Decision focus:
- likely new machine; may start as `is_import: true` if BOM confidence low.
Expected delta type:
- machine entry + staged BOM maturity plan (import -> local subchains).

### 10 Multi-Material 3D Printer
Next step:
- Assess if this should be modeled as a base printer + interchangeable toolheads.
- Reuse existing `3d_printer_basic_v0`/cartesian framework where possible.
Decision focus:
- prefer modular toolhead architecture over monolithic new machine.
Expected delta type:
- toolhead parts/machines + optional printer variant.

### 11 Grinding Media (Alumina/Silumin)
Next step:
- Add only if existing generic grinding media is insufficient for contamination-sensitive cases.
- Map to ball-mill chain requirements.
Decision focus:
- likely add materials/parts and integrate into ball mill recipes/BOM notes.
Expected delta type:
- small material/part additions + minor BOM updates.

### 12 Electrical Insulation Form Factors
Next step:
- Map to existing `ceramic_insulators`, insulation materials, kaolinite/fused-silica chains.
- decide form-factor variants vs net-new.
Decision focus:
- prefer variants under existing insulation hierarchy.
Expected delta type:
- variant parts/materials + recipe variants.

### 13 PMT Localization Feasibility
Next step:
- Evaluate recommendation against existing `photomultiplier_tube_v0` import and vacuum tube chain.
- Choose one path: keep import / hybrid local / local full.
Decision focus:
- default conservative path: keep import unless strong BOM confidence.
Expected delta type:
- policy decision + optional variant entry (`photomultiplier_tube_v1_local`).

### 14 Kovar Wire Form Factor
Next step:
- Map to existing `kovar_alloy_fe_ni_co_v0` + wiring processes.
- Decide if wire form factor materially changes downstream process compatibility.
Decision focus:
- likely add `kovar_wire_v0` part/material variant and wire-drawing route if justified.
Expected delta type:
- small variant addition + recipe/process reuse.

## Prioritized Ingestion Order (to maximize momentum)
1. 03, 04, 05 (beneficiation and Fe/Ti separation core)
2. 01, 02 (rover modular prospecting)
3. 07, 06 (bridge + quartz piezo sensing)
4. 11, 12, 14 (low-risk form-factor/material updates)
5. 08, 10, 09 (complex machine families)
6. 13 (PMT localization decision gate)

## Per-Report Acceptance Criteria
- Decision documented (`reuse/variant/new/defer`).
- Existing-ID mapping documented.
- If new/variant chosen: draft IDs + process I/O + machine requirements listed.
- BOM confidence stated (H/M/L) with top uncertainties.
- Conservative-mode rationale documented (why not reusing existing, if new).

