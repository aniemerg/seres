---
row_identity:
  item: "6N2"
  cad_file: "6N2_rail_LEFS32REA-600N"
  source_row_number: 192
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.smcpneumatics.com/lefs32rea-600bk.html"
function:
  summary: "Back/base rail portion of an SMC LEFS32REA-600BK electric linear actuator, providing the long guided support structure for the slider carriage."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6N2_rail_LEFS32REA-600N.step; https://www.smcusa.com/products/lefs-electric-actuator-slider-type-ball-screw-drive~125690; https://content2.smcetech.com/pdf/LEF_EU.pdf"
    cited_fact_or_basis: "BOM row 192 identifies item 6N2 as CAD file 6N2_rail_LEFS32REA-600N, description linear guide back, manufacturer SMC Pneumatics, quantity 6, with BOM link LEFS32REA-600BK. FreeCAD measured one solid with bounding box 70.00 x 61.90 x 770.00 mm. SMC describes the LEFS as an electric actuator slider with ball screw drive, body size 32, stroke options including 600 mm, and linear guide construction. official_alternate_route_check: the original BOM URL is on smcpneumatics.com for LEFS32REA-600BK; smcusa.com and smcetech.com are official SMC product/catalog domains for the same SMC LEFS actuator family and size/stroke route, so they are treated as BOM-side official alternate/canonical evidence."
    evidence_basis: "bom_provided"
  assumptions:
    - "The BOM-provided product URL and row name are treated as identifying the SMC LEFS32REA-600BK actuator family; the official SMC catalog/product pages are used only to interpret that row-matched actuator family."
    - "The exported 6N2 STEP represents the long fixed rail/back/base portion rather than the moving carriage, because the sibling row 6N1 is named carriage and this row's preview is a long stationary rail-like body."
  uncertainty_notes: []
mass:
  value_kg: 5.91
  basis: "FreeCAD volume 2,190,132.685 mm^3 = 0.002190133 m^3; aluminum density from local kb/materials/properties.yaml is 2700 kg/m^3; aluminum-equivalent mass is about 5.91 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6N2_rail_LEFS32REA-600N.step; kb/materials/properties.yaml; https://content2.smcetech.com/pdf/LEF_EU.pdf"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 2,190,132.685 mm^3, area 195,710.042 mm^2, and bounding box 70.00 x 61.90 x 770.00 mm. The local density table lists aluminum density as 2700 kg/m^3. The SMC catalog construction table lists aluminum alloy for the LEFS body and several housings/covers, while the rail guide material field is not specified. targeted_web_search: searched 'SMC LEFS32REA-600BK material rail', 'LEFS32REA-600BK SMC linear guide material rail', and 'LEFS32REA-600BK datasheet'; found SMC catalog/product-family data but no mass or material split for the exported 6N2 rail subpart."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The long STEP solid is used as a coarse volume proxy for the exported rail/back part."
    - "Aluminum density is used as the representative calculation constant because the CAD resembles the LEFS body/base extrusion and the SMC construction table names aluminum alloy for the body."
  uncertainty_notes:
    - "The assembly STEP material extractor returned only Generic material with density 1000.0, so it does not resolve the material."
    - "The SMC construction table does not directly state the rail guide material, and the CAD is a single vendor solid without separable inserts or void validation; mass could be materially different if this row includes significant steel guide surfaces or if the CAD volume over-fills hollow regions."
material:
  primary_material: "aluminum alloy body/base rail with possible steel guide elements"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6N2_rail_LEFS32REA-600N.step; https://content2.smcetech.com/pdf/LEF_EU.pdf"
    cited_fact_or_basis: "BOM row 192 identifies the part as 6N2_rail_LEFS32REA-600N, linear guide back, SMC Pneumatics. The rendered STEP preview shows a long rail/base-shaped component. The SMC LEFS construction table lists Body as aluminum alloy and anodised, Table as aluminum alloy, several housings/covers as aluminum alloy or aluminum die-casted, Connected shaft and dust seal band as stainless steel, and Rail guide with no material specified. targeted_web_search: searched 'SMC LEFS32REA-600BK material rail', 'LEFS32REA-600BK SMC linear guide material rail', and 'LEFS32REA-600BK datasheet'; found SMC catalog/function/construction data but no row-specific material statement for the exported 6N2 rail subpart beyond the LEFS construction table."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The exported rail/back is treated primarily as the actuator body/base rail, so the SMC body aluminum alloy entry is the best available material proxy."
    - "Steel guide elements remain possible because precision linear guides commonly use hardened steel contact surfaces and SMC leaves the LEFS rail guide material unspecified in the table."
  uncertainty_notes:
    - "Do not use this as a specific alloy or heat-treatment claim; the evidence supports only a broad mixed actuator-rail material hypothesis."
how_to_make:
  summary: "Model as a precision-machined/anodized aluminum actuator rail or base extrusion, with any hardened guide surfaces or inserts treated as external precision guide components until the internal LEFS rail construction is modeled"
  manufacturing_steps:
    - "Start from aluminum extrusion or machined aluminum bar sized for the LEFS32 base/rail envelope."
    - "Mill the longitudinal channels, mounting faces, slots, and end features visible in the CAD preview."
    - "Drill, tap, and finish mounting holes and reference faces to actuator alignment tolerances."
    - "Anodize the aluminum body/base surfaces where applicable."
    - "Install or integrate precision guide/contact elements if the later KB model separates the steel guide function from the aluminum base."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0192_6N2__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6N2_rail_LEFS32REA-600N.step; https://content2.smcetech.com/pdf/LEF_EU.pdf"
    cited_fact_or_basis: "The contact sheet shows a long rail/base-like component with a 70.00 x 61.90 x 770.00 mm bounding box and visible longitudinal channels/features. The SMC construction table lists anodised aluminum alloy for the LEFS body and anodised aluminum alloy for multiple structural covers/housings; the LEFS actuator uses a linear guide and ball screw drive. targeted_web_search: searched 'SMC LEFS32REA-600BK material rail', 'LEFS32REA-600BK SMC linear guide material rail', and 'LEFS32REA-600BK datasheet'; found SMC construction/dimension data but no manufacturing process sheet for the exported rail/back component."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The dominant fabrication route is inferred from the rail/base geometry and aluminum structural entries in the SMC construction table."
    - "Precision guide-contact manufacture is separated from the coarse base rail route because the catalog does not disclose the guide rail material or construction in enough detail."
  uncertainty_notes:
    - "The manufacturing route is suitable for KB planning, not a process sheet for reproducing the SMC precision actuator component."
kb_implications:
  - "item_granularity: simple_part - treat this row as one long actuator rail/base part for coarse BOM closure; split out purchased precision guide inserts only if later evidence resolves them."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0192_6N2.md
source_research_sha256: "95925c034c67c7051353a9ef4a178aff55338008a40ef94dd31143dccb49a0cf"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed the SMC actuator rail/base function, 5.91 kg per-unit mass with BOM quantity 6 and 35.46 kg row total, aluminum alloy base with possible steel guide elements, inferred extrusion/machining/anodizing route, KB implication, and CAD preview showing a long channeled rail-like body."
decomposition:
  decision: simple_part
  rationale: "The row represents the long fixed rail/base portion of an actuator rather than the full actuator module. Treat as one structural guide/base part while preserving possible precision guide inserts as unresolved."
  proposed_subparts: []
process_abstraction:
  original_process_family: precision_machined_aluminum_actuator_rail_base
  primary_process_bucket: structural_profile_stock_fabrication_cutting
  supporting_processes:
    - stock_preparation
    - extrusion
    - cutting
    - drilling
    - precision_machining
    - deburring
    - coating
    - dimensional_inspection
    - assembly
  candidate_existing_processes:
    - process_id: aluminum_tube_stock_extrusion_v0
      fit: poor_fit
      reason: "Existing extrusion anchor uses tube stock, but it is the closest current process for aluminum profile formation."
    - process_id: machining_precision_v0
      fit: partial
      reason: "Covers machined slots, reference faces, holes, and alignment-critical features after profile stock is made."
    - process_id: drilling_basic_v0
      fit: supporting
      reason: "Covers mounting holes and tapped features after rail/base stock preparation."
    - process_id: surface_treatment_anodizing_v0
      fit: supporting
      reason: "Relevant because SMC construction evidence names anodized aluminum body components."
    - process_id: finishing_deburring_v0
      fit: supporting
      reason: "Covers edge cleanup after profile cutting and machining."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers basic dimensional checks, with later staging needing straightness and alignment checks."
  abstraction_decision: substitute_process_family
  rationale: "The row-specific source is a vendor actuator rail/base, but closure can model the local path as structural profile formation, cutting, precision machining, anodizing, and inspection while leaving guide-contact details unresolved."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: high
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: "long guided support base for an electric linear actuator carriage"
  material: aluminum_alloy_with_possible_steel_guide_elements
  scale_or_capacity:
    mass_kg: 5.91
    bom_quantity: 6
    row_total_mass_kg: 35.46
    scale_class: large
  geometry_form: long_channeled_actuator_rail_base_profile
merge_pool:
  eligible: true
  functional_purpose_key: linear_guidance
  precision_guardrails:
    - straightness
    - alignment_accuracy
    - guide_surface_material
    - anodized_surface
    - long_profile_geometry
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - structural_profile_stock_fabrication_cutting
  import_risk_factors:
    - "Guide-contact material and construction are unresolved; hardened steel inserts could make this more than a simple aluminum profile."
    - "Straightness, reference-face accuracy, and actuator alignment over the 770 mm length may require precision machining and inspection."
  post_merge_decision_notes: "Final import/local decision is deferred until this rail/base is compared with other actuator rails, guide bases, and precision linear-guidance rows."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely candidate for a generic long aluminum actuator rail/base if precision guide elements are modeled separately."
assumptions:
  - "BOM quantity is 6, mass is 5.91 kg per unit, and row total mass is 35.46 kg."
  - "Aluminum alloy is used as the primary base material based on SMC body construction evidence and CAD form."
  - "Possible steel guide-contact elements are preserved as unresolved and not assigned a separate subpart during row conversion."
unresolved:
  - "Exact alloy, extrusion profile route, guide material, steel insert presence, straightness tolerance, and surface treatment specification remain unresolved."
  - "Whether this should merge with generic linear rail/base stock versus remain tied to the LEFS actuator family is deferred."
```
