---
row_identity:
  item: "6N1"
  cad_file: "6N1_carriage_LEFS32REA-600N"
  source_row_number: 191
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.smcpneumatics.com/lefs32rea-600bk.html"
function:
  summary: "Moving carriage/table block for an SMC LEFS32REA-600BK slider actuator, providing the workpiece mounting surface that travels along the actuator's linear guide."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6N1_carriage_LEFS32REA-600N.step; research/ream250_bom/ream250_bom_row_0191_6N1__views_2x2.png"
    cited_fact_or_basis: "BOM row 191 identifies item 6N1 as quantity 6, cad_file 6N1_carriage_LEFS32REA-600N, description 'linear guide back', manufacturer SMC Pneumatics. FreeCAD measured one solid with 60.00 x 18.20 x 122.00 mm bounding box; the rendered preview shows a narrow rectangular carriage/table-like block with mounting and guide features."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row name 'carriage' and the LEFS actuator context refer to the moving table/carriage subcomponent rather than the full 600 mm actuator."
  uncertainty_notes:
    - "The CAD export is a vendor component but appears as one simplified solid, so internal rolling elements or inserts are not separately visible."
mass:
  value_kg: 0.275
  basis: "Per-unit estimate for one carriage: FreeCAD STEP volume 101,703.924 mm^3 = 0.000101704 m^3. Using the local aluminum density constant 2700 kg/m^3 gives 0.2746 kg, rounded to 0.275 kg per carriage. BOM quantity is 6, so the row total is about 1.65 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6N1_carriage_LEFS32REA-600N.step; kb/materials/properties.yaml; https://smccatalog.partbuilder.smcpneumatics.com/assets/manual/en-jp/files/LEF-OM004xx.pdf"
    cited_fact_or_basis: "FreeCAD measured the row STEP as one solid with volume 101,703.924 mm^3. kb/materials/properties.yaml lists aluminum density as 2700 kg/m^3. SMC LEF manual search result text for LEFS parts lists the table as aluminum alloy, anodized. bom_url_route_check: BOM URL https://www.smcpneumatics.com/lefs32rea-600bk.html was checked but returned an access-denied page locally; material was resolved from an agent-initiated search result for an SMC-hosted LEF manual matching the same LEFS actuator family."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The exported carriage solid is used as the per-unit physical item represented by BOM row 191."
    - "The carriage volume is treated as aluminum alloy for mass estimation because the SMC LEF material table identifies the table as aluminum alloy."
  uncertainty_notes:
    - "If the actual carriage includes non-aluminum bearing/guide inserts not represented as separate STEP volumes, the true mass could be higher; the same CAD volume at generic steel density would be about 0.80 kg."
material:
  primary_material: "aluminum alloy carriage/table, anodized; possible steel guide or bearing elements not quantified by the row CAD"
  source:
    url_or_path: "https://smccatalog.partbuilder.smcpneumatics.com/assets/manual/en-jp/files/LEF-OM004xx.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6N1_carriage_LEFS32REA-600N.step"
    cited_fact_or_basis: "SMC LEF manual search result text for the LEFS family lists the table as aluminum alloy with anodized finish, while rail guide, ball screw shaft, and ball screw nut materials are not specified in that snippet. The row STEP material extractor returned only Generic with density 1000.0, which is placeholder metadata and was not used as material evidence. bom_url_route_check: BOM URL https://www.smcpneumatics.com/lefs32rea-600bk.html was checked but access was denied locally, so the material section uses an agent-initiated search result for an SMC-hosted manual matching the LEFS actuator family."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The BOM row's carriage corresponds most closely to the LEFS table/carriage material entry."
  uncertainty_notes:
    - "The source resolves the table material family but not a specific aluminum alloy grade or any hidden bearing/guide insert material."
how_to_make:
  summary: "Best modeled initially as a vendor linear-actuator carriage/table component; machine the carriage from aluminum alloy stock, anodize it, and integrate precision guide/bearing interfaces during actuator assembly."
  manufacturing_steps:
    - "Mill the carriage body from aluminum alloy bar or plate stock to the measured envelope and mounting features."
    - "Anodize the aluminum body and fit or interface it with precision guide, ball screw nut, and bearing elements during actuator assembly."
    - "Inspect mounting surfaces, hole locations, and sliding alignment before installation."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6N1_carriage_LEFS32REA-600N.step; https://www.smcworld.com/products/pickup/en-jp/electric_actuator/slider_prod_lefs.html"
    cited_fact_or_basis: "CAD preview shows a machined block-like carriage with mounting/guide features. SMC's official LEFS product page identifies LEFS as an electric actuator/slider type, ball screw drive series with linear guide/slider product context. targeted_web_search: tried 'SMC LEFS32REA-600BK linear guide back material weight', 'LEFS32REA-600BK SMC datasheet weight material', and 'SMC LEFS LEFS32 table aluminum alloy material'; searches found SMC LEFS family function/material evidence but no row-specific manufacturing process for the separate 6N1 carriage."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Machining plus finishing is a plausible route for the visible aluminum carriage geometry, but it is not directly stated by SMC for this replacement row."
  uncertainty_notes:
    - "Precision guide and ball-screw interfaces may require vendor-grade grinding, bearing fitting, or matched assembly tolerances beyond a simple machined block."
kb_implications:
  - "item_granularity: simple_part - Treat as a reusable linear-actuator carriage/table part for later KB modeling, with notes that it belongs to an SMC LEFS32 actuator assembly and may carry precision-interface constraints."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0191_6N1.md
source_research_sha256: "be094102b288d4d1202810389f5bb7be9f4bea6d9724af4d35950b4d224f86a1"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read the moving-carriage function, CAD-volume aluminum mass basis, anodized aluminum material evidence, machining/anodizing route, KB implication, and preview of the narrow carriage block."
decomposition:
  decision: simple_part
  rationale: "The row CAD represents the carriage/table body as one simplified solid; hidden guide inserts remain unresolved but are not visible enough to decompose at row stage."
  proposed_subparts: []
process_abstraction:
  original_process_family: machined_anodized_aluminum_carriage
  primary_process_bucket: general_subtractive_machining
  supporting_processes:
    - stock_preparation
    - cutting
    - drilling
    - precision_machining
    - deburring
    - coating
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: machining_basic_v0
      fit: partial
      reason: "Covers stock removal for the aluminum carriage envelope and mounting features."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Relevant for guide references, mounting-hole position, and sliding alignment surfaces."
    - process_id: surface_treatment_anodizing_v0
      fit: supporting
      reason: "Covers anodized aluminum finishing consistent with the SMC table material evidence."
    - process_id: grinding_and_finishing_v0
      fit: supporting
      reason: "May be needed if guide contact surfaces require smoother finish than milled surfaces."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers dimensional checks; later staging may require a stronger metrology step."
  abstraction_decision: keep_original_family
  rationale: "The original fallback route is machining an aluminum carriage body and anodizing it; the selected bucket keeps that family while recording precision guide interfaces as guardrails."
  process_guardrails:
    tolerance: high
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: high
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: moving carriage table providing a mounting surface on a linear actuator guide
  material: anodized_aluminum_alloy_with_possible_unresolved_guide_inserts
  scale_or_capacity:
    mass_kg: 0.275
    bom_quantity: 6
    row_total_mass_kg: 1.65
    scale_class: small
  geometry_form: narrow_rectangular_machined_carriage_block_with_mounting_and_guide_features
merge_pool:
  eligible: true
  functional_purpose_key: linear_guidance
  precision_guardrails:
    - guide_alignment
    - mounting_hole_position
    - sliding_surface_finish
    - hidden_insert_materials
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - general_subtractive_machining
  import_risk_factors:
    - "Vendor actuator carriage may include bearing/guide interface details not captured by the single-solid CAD export."
    - "Alignment surfaces and matched actuator fit may require tighter inspection than ordinary machined blocks."
  post_merge_decision_notes: "Final import/local manufacture decision is deferred until after merge review with other linear guide and actuator carriage rows."
kb_staging:
  proposed_item_id: null
  notes: "Leave final closure item ID open; likely merge review should compare this with other linear-guidance carriage/table components by function, scale, and precision."
assumptions:
  - "Treat the visible solid as the aluminum carriage/table body named by the SMC LEFS context."
  - "Use aluminum alloy and anodized finish from LEFS material evidence; hidden steel inserts remain a guardrail."
  - "Use 0.275 kg per unit and quantity 6 for later scale grouping."
unresolved:
  - "Specific aluminum alloy grade and anodize specification."
  - "Presence, material, and mass of hidden guide inserts."
  - "Required straightness, flatness, and mounting alignment tolerance."
```
