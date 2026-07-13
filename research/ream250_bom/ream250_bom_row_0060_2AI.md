---
row_identity:
  item: "2AI"
  cad_file: "2AI_connection_axis"
  source_row_number: 60
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.karl-hipp.de/produkte/praezisionskugelgewindetriebe/nenndurchmesser-16mm/16-04/item/kgt-f1-16-04"
function:
  summary: "Precision connection-axis / flanged ball-screw-nut interface for the reAM250 z-axis drive: it couples the 16 mm lead-4 Karl Hipp ball-screw nut family into the local mount, with a central bore and six flange bolt holes visible in the row STEP."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; https://www.karl-hipp.de/en/products/precision-ball-screws/nominal-diameter-16mm/16-04/item/kgt-f1-16-04; research/ream250_bom/ream250_bom_row_0060_2AI__views_2x2.png"
    cited_fact_or_basis: "BOM row 60 identifies item 2AI as quantity 1, CAD file 2AI_connection_axis, manufacturer Karl Hipp GmbH, and description 'connection axis R16-05T3-DEB-401-490-'. The row-matched Karl Hipp page identifies the linked product family as Flange nut - F1 with nominal diameter 16 mm, lead 4 mm, ball diameter 2.5 mm, 4 circuits, wiper yes, Cdyn 8700 N, and Cstat 13100 N. The CAD preview shows a short flanged cylindrical part with a central bore and six bolt holes."
    evidence_basis: "bom_provided"
  assumptions:
    - "The BOM Link URL is treated as the intended vendor-family route even though the original German path redirects to the English row-matched product page for inspection."
  uncertainty_notes:
    - "The BOM description says 'connection axis' while the vendor route is a flange-nut product family; the CAD geometry is consistent with a flanged nut/interface, so the function is locked to this row rather than generalized to the whole ball screw."
mass:
  value_kg: 0.198
  basis: "Per-unit estimate for quantity 1. FreeCAD measured one solid with volume 25229.522 mm^3, surface area 9826.902 mm^2, and bounding box about 40.00 x 40.47 x 48.00 mm. Using local generic steel density 7850 kg/m^3 from kb/materials/properties.yaml: 25229.522 mm^3 = 0.000025229522 m^3, so mass is about 0.198 kg. The BOM row quantity is 1, so the row total is also about 0.198 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AI_connection_axis.step; kb/materials/properties.yaml; https://www.schneeberger.com/fileadmin/documents/downloadcenter/01_product_catalogues_company_brochures/09_Others/Hipp_Product_catalog_EN.pdf"
    cited_fact_or_basis: "FreeCAD measured the row STEP as one solid with volume 25229.522 mm^3 and bounding box about 40.00 x 40.47 x 48.00 mm. The Hipp product catalog states standard ballscrew nut material as 100Cr6 hardened to 60 +/-2 HRC. kb/materials/properties.yaml lists generic steel density as 7850 kg/m^3. bom_url_route_check: the BOM-provided Karl Hipp URL was checked first and resolved the row-matched F1 16-04 product family but did not expose material or catalog mass, so the Hipp product catalog hosted on Schneeberger was used for the material basis."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The CAD solid volume is treated as the physical solid volume of one row item."
    - "100Cr6 bearing steel is approximated by the local generic steel density constant because the local density table has steel but no separate 100Cr6 entry."
  uncertainty_notes:
    - "No row-specific catalog mass was found; mass depends on CAD volume fidelity and the steel-density approximation."
material:
  primary_material: "100Cr6 hardened bearing steel for the ballscrew nut body; the row-matched F1 16-04 family also lists a wiper, whose material is not resolved."
  source:
    url_or_path: "https://www.schneeberger.com/fileadmin/documents/downloadcenter/01_product_catalogues_company_brochures/09_Others/Hipp_Product_catalog_EN.pdf; https://www.karl-hipp.de/en/products/precision-ball-screws/nominal-diameter-16mm/16-04/item/kgt-f1-16-04; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The Hipp product catalog states standard ballscrew nut material as 100Cr6 hardened to 60 +/-2 HRC and stainless nut variant material as 1.4034 on request. The row-matched Karl Hipp F1 16-04 page lists wiper: yes. Local assembly STEP material extraction for 2AI_connection_axis returned only Generic material and density 1000.0, which does not resolve material. bom_url_route_check: the BOM-provided Karl Hipp URL matched the F1 16-04 product family but did not state material, so the product catalog was used for material. independent web search: searched 'Karl Hipp KGT-F1 16-04 material' and found the Hipp product catalog PDF with the standard nut material statement."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The standard 100Cr6 material is used because the BOM row does not indicate a stainless or special-order variant."
  uncertainty_notes:
    - "The catalog material resolves the ball-screw nut body, not detailed material splits for balls, return pieces, or wiper material."
how_to_make:
  summary: "Start from bearing-steel bar or forging, rough turn the cylindrical and flange features, drill the bolt circle and central bore, grind the ball track/thread geometry, heat treat to about 60 HRC, finish grind/lap bearing surfaces, install balls/return/wiper elements if part of the delivered nut, and inspect lead, preload/axial play, and flange interfaces"
  manufacturing_steps:
    - "For local manufacture, rough-machine 100Cr6 bearing-steel stock to the flanged cylindrical CAD envelope."
    - "Drill and finish the six flange mounting holes and central bore visible in the row STEP."
    - "Generate and grind the ball-screw nut race/thread geometry, then harden and finish-grind to precision ball-screw tolerances."
    - "Assemble recirculating balls, return path, and wiper elements if the row item represents the complete flange nut, then inspect against the screw-drive tolerance class."
  source:
    url_or_path: "https://www.karl-hipp.de/en/products/precision-ball-screws/nominal-diameter-16mm/16-04/item/kgt-f1-16-04; https://www.schneeberger.com/fileadmin/documents/downloadcenter/01_product_catalogues_company_brochures/09_Others/Hipp_Product_catalog_EN.pdf; research/ream250_bom/ream250_bom_row_0060_2AI__views_2x2.png"
    cited_fact_or_basis: "The row-matched Karl Hipp page identifies a precision F1 flange-nut family and lists F1 16-04 ordering parameters and performance data. The Hipp catalog states ball tracks are ground after heat treatment and that nut material is 100Cr6 hardened to 60 +/-2 HRC. The CAD preview shows the flanged cylindrical mounting form. targeted_web_search: searched 'Karl Hipp KGT-F1 16-04 material', 'R16-05T3-DEB-401-490 Karl Hipp', and 'Karl Hipp 100Cr6 ballscrew nut manufacturing'; results resolved product-family material and precision ball-screw catalog context but no row-specific manufacturing drawing for the custom connection axis."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The manufacturing route extrapolates common precision ball-screw-nut manufacturing steps from the sourced hardened, ground ball-track facts and visible flange geometry."
  uncertainty_notes:
    - "The exact custom operations for the R16-05T3-DEB-401-490 connection-axis variant are not published in the sources checked."
kb_implications:
  - "item_granularity: simple_part - model as one reusable precision ball-screw nut/connection-axis hardware item for now; keep procurement/manufacturing difficulty in the recipe/process layer rather than making it a separate machine subsystem."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0060_2AI.md
source_research_sha256: "ac1425baa6415cf99788ae4bd8be5b048782af9dc8dd9fe0e02e0b8497314a3b"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read the precision ball-screw flange-nut function, CAD-derived steel mass basis, 100Cr6 hardened material evidence, inferred precision machining/grinding route, and preview showing a flanged cylindrical part with central bore and six bolt holes."
decomposition:
  decision: complex_module
  rationale: "The row is one purchased precision motion component, but closure-relevant dependencies include hardened nut body, ground ball track, recirculating balls, return path, wiper, preload, and inspection."
  proposed_subparts:
    - hardened_ballscrew_nut_body
    - recirculating_bearing_balls
    - ball_return_path
    - wiper_element
    - flange_mounting_features
process_abstraction:
  original_process_family: precision_ballscrew_nut_manufacture
  primary_process_bucket: precision_component_import_decompose_later
  supporting_processes:
    - precision_machining
    - thread_forming
    - heat_treatment
    - grinding_lapping
    - assembly
    - cleaning
    - calibration
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: machining_precision_v0
      fit: partial
      reason: "Covers precision machining of the flange, bore, and mounting interfaces, but not ground recirculating ball tracks."
    - process_id: grinding_process_precision_v0
      fit: supporting
      reason: "Relevant to final ball-track and bearing-surface finish after heat treatment."
    - process_id: heat_treatment_hardening_v0
      fit: supporting
      reason: "Relevant to hardening 100Cr6 bearing steel to the catalog hardness range."
    - process_id: assembly_process_bearing_v0
      fit: partial
      reason: "Covers assembly of balls, seals, and grease in bearing-like hardware, but not a ball-screw return circuit."
    - process_id: calibration_basic_v0
      fit: supporting
      reason: "Relevant to preload, axial play, and motion-quality verification after assembly."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers interface checks, with precision metrology needed for lead, preload, and race quality."
  abstraction_decision: substitute_process_family
  rationale: "The row is not ordinary flange machining; precision ball-screw function and hardened ground tracks make it a precision component to defer until motion-component closure is in scope."
  process_guardrails:
    tolerance: high
    surface_finish: high
    sealing_quality: review
    alignment_accuracy: high
    blocked_by_precision: true
identity_for_merge:
  functional_purpose: precision ball-screw nut interface converting screw rotation into Z-axis linear motion
  material: hardened_100cr6_bearing_steel_with_unresolved_wiper
  scale_or_capacity:
    mass_kg: 0.198
    bom_quantity: 1
    row_total_mass_kg: 0.198
    scale_class: small
  geometry_form: flanged_cylindrical_ballscrew_nut_with_central_bore_and_six_bolt_holes
merge_pool:
  eligible: false
  functional_purpose_key: linear_actuation
  precision_guardrails:
    - ground_ball_track_quality
    - preload
    - axial_play
    - lead_accuracy
    - flange_alignment
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - precision_component_import_decompose_later
  import_risk_factors:
    - "Precision ball-screw nut manufacture requires hardened 100Cr6, ground tracks, recirculating balls, return path, wiper materials, and high-grade inspection."
    - "Custom connection-axis variant details are not published."
  post_merge_decision_notes: "Final import/local decision is deferred; this row should be decomposed with other precision linear-motion hardware before staging."
kb_staging:
  proposed_item_id: null
  notes: "Do not assign a simple closure ID yet; preserve the F1 16-04, 16 mm nominal, 4 mm lead evidence for later motion-component review."
assumptions:
  - "Standard 100Cr6 nut material is used because no special variant is indicated."
  - "The row item may include internal balls and wiper even though the CAD shows a simplified flanged body."
unresolved:
  - "Exact custom variant features, ball count, return path, wiper material, preload class, and tolerance class are unknown."
  - "Complete ball-screw nut module versus split flange-body/rolling-element modeling needs group review."
```
