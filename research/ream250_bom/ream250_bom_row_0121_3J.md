---
row_identity:
  item: "3J"
  cad_file: "3J_pipe_ISO_K_DN63_320RZS063"
  source_row_number: 121
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320RZS063"
function:
  summary: "Straight ISO-K DN 63 full nipple / vacuum pipe spool connecting two ISO-K flanged vacuum components in the reAM250 vacuum plumbing."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3J_pipe_ISO_K_DN63_320RZS063.step; https://vacuum-shop.com/shop/en_US/category/2073062/product/320rzs063/full-nipple-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "BOM row 121 identifies Pfeiffer Vacuum product 320RZS063; CAD preview shows a straight hollow tube with ISO-K flanges at both ends; official_alternate_route_check: BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320RZS063 corresponds to Pfeiffer Vacuum product 320RZS063, while the accessible Pfeiffer Vacuum online shop page on vacuum-shop.com lists 320RZS063 as a 'Full nipple' with connection flange DN 63 ISO-K, matching the BOM product ID and CAD geometry."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row represents one straight full nipple; BOM quantity 2 means two identical pieces."
  uncertainty_notes: []
mass:
  value_kg: 0.914
  basis: "FreeCAD measured one CAD solid volume as 113870.559 mm^3. Using local stainless_steel_1_4301 density 8030 kg/m^3 gives 113870.559e-9 m^3 * 8030 kg/m^3 = 0.914 kg per full nipple. BOM quantity is 2, so the row total is about 1.83 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3J_pipe_ISO_K_DN63_320RZS063.step; kb/materials/properties.yaml; https://vacuum-shop.com/shop/en_US/category/2073062/product/320rzs063/full-nipple-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 113870.559 mm^3, area 60263.770 mm^2, and bounding box 88.00 x 105.13 x 105.13 mm. The local density table gives stainless_steel_1_4301 as 8030 kg/m^3. official_alternate_route_check: BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320RZS063 maps to the accessible Pfeiffer Vacuum online shop page on vacuum-shop.com for the same product ID 320RZS063, which states stainless steel 1.4301/AISI 304 and length 88 mm."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the per-unit metal volume for the physical row item."
  uncertainty_notes:
    - "CAD volume may omit very small chamfers, weld-prep details, or surface finish effects, so the estimate is best used as an approximate per-unit planning mass."
material:
  primary_material: "stainless steel 1.4301 / AISI 304"
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073062/product/320rzs063/full-nipple-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "The official Pfeiffer Vacuum online shop page for 320RZS063 names the product 'Full nipple, stainless steel 1.4301/304' and lists media-contact material as stainless steel 1.4301 (AISI 304). official_alternate_route_check: BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320RZS063 identifies the same Pfeiffer product ID; the accessible vacuum-shop.com page is a Pfeiffer Vacuum Components & Solutions shop page and matches product ID 320RZS063."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "Assembly STEP material metadata for this CAD object is only 'Generic' at density 1000, so the usable material evidence comes from the row-matched Pfeiffer product route rather than embedded CAD material metadata."
how_to_make:
  summary: "Prepare as a standard Pfeiffer 320RZS063 ISO-K DN 63 full nipple, or manufacture locally as a stainless 304/1.4301 vacuum tube with two ISO-K flange ends, weld/braze or form the tube-flange geometry, then finish and leak-test for high-vacuum service"
  manufacturing_steps:
    - "Cut stainless 304/1.4301 tube stock to the 88 mm overall length envelope for DN 63 ISO-K geometry."
    - "Form or machine the ISO-K flange lips/end features and join them to the tube if made from separate flange rings."
    - "Deburr and clean the internal bore and sealing faces for vacuum compatibility."
    - "Leak-test and inspect the finished spool against ISO-K DN 63 interface dimensions."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3J_pipe_ISO_K_DN63_320RZS063.step; https://vacuum-shop.com/shop/en_US/category/2073062/product/320rzs063/full-nipple-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "Pfeiffer identifies the row product as a stainless 1.4301/304 full nipple with DN 63 ISO-K connection and 88 mm length; CAD preview shows a straight hollow cylindrical spool with flanged ends. targeted_web_search: searched 'Pfeiffer 320RZS063 manufacturing full nipple stainless steel 1.4301' and '320RZS063 datasheet manufacturing' and found row-matched product/datasheet facts but no row-specific manufacturing process description."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The manufacturing route follows common vacuum hardware fabrication practice inferred from the product geometry and material, not a Pfeiffer-published process sheet."
  uncertainty_notes:
    - "Exact factory process details such as deep drawing versus machined flange rings plus welded tube are not resolved."
kb_implications:
  - "item_granularity: simple_part - Model as a reusable stainless ISO-K DN 63 straight full nipple / pipe spool rather than a reAM250-specific assembly."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0121_3J.md
source_research_sha256: "e0a6961cc6b74ddbbd0fb6d8ed742e6689bac4409177cac39ed5ee21dac5b1f8"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read the row function, CAD-derived mass basis, stainless 1.4301/AISI 304 material evidence, inferred tube/flange fabrication route, and CAD geometry showing a straight hollow ISO-K DN 63 flanged spool."
decomposition:
  decision: simple_part
  rationale: "The row is one repeated vacuum pipe spool/full nipple with no internal subassembly exposed by the evidence; BOM quantity 2 represents duplicate simple parts."
  proposed_subparts: []
process_abstraction:
  original_process_family: tube_flange_fabrication_and_leak_testing
  primary_process_bucket: plumbing_connector_fabrication_testing
  supporting_processes:
    - cutting
    - forming
    - joining
    - precision_machining
    - deburring
    - cleaning
    - leak_testing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: plumbing_and_pneumatics_v0
      fit: partial
      reason: "Covers pipe/tube fitting work and pressure/leak checks, but is written for system installation rather than fabrication of a standalone ISO-K nipple."
    - process_id: tube_stock_forming_v0
      fit: supporting
      reason: "Relevant to producing/preparing tube stock before flange-end fabrication."
    - process_id: welding_brazing_basic_v0
      fit: supporting
      reason: "Supports the inferred route where separate stainless flange rings are joined to a tube spool."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Covers finish machining of flange lips, sealing faces, and interface dimensions if formed parts need final tolerance control."
    - process_id: leak_testing_v0
      fit: direct
      reason: "Directly covers leak testing and sealed-joint checks needed for vacuum plumbing service."
    - process_id: cleaning_basic_v0
      fit: supporting
      reason: "Vacuum-facing stainless bore and sealing surfaces require cleaning after fabrication."
  abstraction_decision: substitute_process_family
  rationale: "The source route is a commercial Pfeiffer vacuum nipple; for closure analysis it is better handled as a reusable stainless plumbing connector made from tube/flange features and verified by dimensional inspection and leak testing."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: high
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: straight pipe spool connecting two ISO-K DN 63 vacuum plumbing interfaces
  material: stainless_steel_304
  scale_or_capacity:
    mass_kg: 0.914
    bom_quantity: 2
    row_total_mass_kg: 1.828
    scale_class: small
  geometry_form: straight_hollow_cylindrical_tube_with_iso_k_flanged_ends
merge_pool:
  eligible: true
  functional_purpose_key: plumbing_connection
  precision_guardrails:
    - sealing_face_finish
    - iso_k_interface_dimensions
    - leak_tightness
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - plumbing_connector_fabrication_testing
  import_risk_factors:
    - "High-vacuum sealing quality and cleanliness requirements may force tighter process control than ordinary pipe fabrication."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares this ISO-K spool with other plumbing connector rows."
kb_staging:
  proposed_item_id: null
  notes: "Leave item identity open for merge review with other vacuum/gas plumbing connectors; preserve DN 63 ISO-K and stainless evidence as guardrails."
assumptions:
  - "BOM quantity 2 is represented as two identical simple parts at 0.914 kg each."
  - "The local closure route may use welded/formed flange ends plus finish machining even though the Pfeiffer factory process is not published."
unresolved:
  - "Exact manufacturing route for the commercial nipple, including whether flange lips are formed, one-piece machined, welded from separate rings, is unresolved."
  - "Required leak-rate class and sealing-face finish are not specified in the row evidence and need review before final KB staging."
```
