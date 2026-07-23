---
row_identity:
  item: "63"
  cad_file: "63_retaining_ring_DIN 471 - 5x0,6"
  source_row_number: 269
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Small DIN 471 external retaining ring for a 5 mm shaft/groove interface; it acts as a removable axial shoulder to retain a mating component on a shaft."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/63_retaining_ring_DIN 471 - 5x0,6.step; research/ream250_bom/ream250_bom_row_0269_63__views_2x2.png"
    cited_fact_or_basis: "BOM row 269 lists item 63, quantity 1, CAD file '63_retaining_ring_DIN 471 - 5x0,6', and description 'spring retaining ring'. The manifest maps the same row to a matched part STEP. FreeCAD measured one solid with a 6.65 x 8.45 x 0.60 mm bounding box, and the rendered preview shows a thin split external circlip with lug holes."
    evidence_basis: "bom_provided"
  assumptions:
    - "The DIN 471 - 5x0,6 text is interpreted as the standard external shaft retaining-ring designation and nominal size."
  uncertainty_notes: []
mass:
  value_kg: 0.0000971
  basis: "FreeCAD volume 12.365 mm^3 equals 1.2365e-8 m^3. Assembly STEP material metadata reports Steel, Mild with density 7850 kg/m^3 for this product, giving 1.2365e-8 m^3 * 7850 kg/m^3 = 0.0000971 kg per retaining ring. BOM quantity is 1, so the row total is also about 0.0000971 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/63_retaining_ring_DIN 471 - 5x0,6.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 12.365 mm^3, area 67.203 mm^2, and bounding box 6.65 x 8.45 x 0.60 mm. The local STEP material extractor matched product 63_retaining_ring_DIN 471 - 5x0,6 and reported material Steel, Mild with density 7850.0."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP volume is treated as the complete solid volume for one physical retaining ring."
    - "The STEP density is used as the calculation constant for the row-level mass estimate."
  uncertainty_notes:
    - "The CAD-derived value is very small and sensitive to whether the STEP geometry includes every edge radius/chamfer, but it is appropriate for BOM-scale mass accounting."
material:
  primary_material: "steel family; local STEP metadata labels the row material as Steel, Mild, while DIN 471 retaining rings are commonly spring-steel hardware"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://ametric.com/Images/document/RetainingRings-Metric.pdf; https://www.fastenermart.com/din-471-external-retaining-rings.html"
    cited_fact_or_basis: "The local STEP material extractor reports Steel, Mild and density 7850.0 for the row product. Ametric's DIN 471 retaining-ring catalog table lists hardened spring steel C60-DIN/AISI 1060 with phosphate finish for external retaining rings, and Fastener Mart describes DIN 471 as external retaining rings for shafts."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "For KB planning, model this as steel-family retaining-ring hardware rather than encoding mild steel as a functional spring grade."
  uncertainty_notes:
    - "The row-specific CAD metadata gives a steel family but may be a generic CAD material assignment; exact grade, heat treatment, and finish are not resolved for this specific BOM row."
how_to_make:
  summary: "Prepare as a standard DIN 471 external retaining ring; blanking/stamping the ring profile from spring-steel strip, heat treating if not supplied pre-hardened, finishing/coating, and inspecting shaft-groove fit"
  manufacturing_steps:
    - "Select steel strip or spring-steel stock at about 0.6 mm thickness for the small DIN 471 ring size."
    - "Blank or stamp the split-ring outline, lug ends, and plier holes."
    - "Deburr edges and heat treat or stress relieve as needed for spring retention behavior."
    - "Apply a corrosion-protection finish if required, then inspect free shape, thickness, lug holes, and fit in the mating shaft groove."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0269_63__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/63_retaining_ring_DIN 471 - 5x0,6.step; https://www.huyett.com/dsh-010-zc; https://ametric.com/Images/document/RetainingRings-Metric.pdf"
    cited_fact_or_basis: "The CAD preview shows a thin stamped-looking split retaining ring with lug holes. Huyett's DIN 471 snap-ring page for the same family lists Type: Snap Rings External, material Carbon Spring Steel, and Style: Stamped. Ametric's DIN 471 table lists hardened spring steel for external retaining rings. targeted_web_search: searched 'DIN 471 retaining ring 5 x 0.6 material spring steel stainless steel', 'DIN 471 external retaining ring function shaft groove spring steel', and 'DIN 471 retaining ring manufacturing stamped spring steel'; results resolved standard retaining-ring function, common material family, and a stamped style for comparable DIN 471 rings, but did not provide a row-specific factory process for this exact reAM250 item."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The inferred from the standard ring geometry, thin sheet/strip thickness, and comparable catalog description of DIN 471 rings as stamped external snap rings."
  uncertainty_notes:
    - "The cited sources do not specify the actual supplier or process used for the reAM250 row, so heat treatment and finish remain planning assumptions."
kb_implications:
  - "item_granularity: simple_part - standard small external retaining-ring hardware; later KB modeling should reuse or parameterize a generic DIN 471 steel retaining ring rather than create a machine-specific custom part."
---

Research result for reAM250 BOM row 269.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0269_63.md
source_research_sha256: "a0a36a5f09685ce7a03b6e66f1cc2eba9db3b9d7a110353ab4dca36640db7de7"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed the DIN 471 external retaining-ring function, 0.0000971 kg mass with BOM quantity 1, steel-family material evidence, stamped spring retaining-ring route, KB implication, and CAD preview showing a small split circlip with lug holes."
decomposition:
  decision: simple_part
  rationale: "The row is one standard small retaining ring with no internal assemblies; it should merge into generic retaining hardware rather than become a row-specific part."
  proposed_subparts: []
process_abstraction:
  original_process_family: stamped_spring_steel_retaining_ring
  primary_process_bucket: fastener_forming_thread_rolling
  supporting_processes:
    - stock_preparation
    - cutting
    - forming
    - deburring
    - heat_treatment
    - surface_finishing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: fastener_kit_small_fabrication_v0
      fit: partial
      reason: "Closest existing small hardware fabrication anchor, though retaining rings need stamped spring behavior rather than threaded fastener production."
    - process_id: sheet_metal_cutting_v0
      fit: supporting
      reason: "Relevant to blanking the thin ring profile from strip stock."
    - process_id: metal_forming_basic_v0
      fit: supporting
      reason: "Relevant to stamping and forming the split ring geometry."
    - process_id: heat_treatment_hardening_v0
      fit: supporting
      reason: "Relevant if spring-steel retention behavior is locally produced."
    - process_id: finishing_deburring_v0
      fit: supporting
      reason: "Covers edge cleanup before finishing and fit checks."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers ring thickness, lug hole, free shape, and groove-fit checks."
  abstraction_decision: substitute_process_family
  rationale: "The item is standard fastener-like retention hardware. The canonical fastener bucket is close enough for Phase 1, with stamping and heat treatment captured as supporting operations."
  process_guardrails:
    tolerance: moderate
    surface_finish: low_to_moderate
    sealing_quality: not_applicable
    alignment_accuracy: low
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: "removable axial retention shoulder for a small shaft groove"
  material: steel_retaining_ring_family
  scale_or_capacity:
    mass_kg: 0.0000971
    bom_quantity: 1
    row_total_mass_kg: 0.0000971
    scale_class: small
  geometry_form: small_split_external_circlip_with_lug_holes
merge_pool:
  eligible: true
  functional_purpose_key: mechanical_retention
  precision_guardrails:
    - din_471_standard
    - shaft_size_5mm
    - spring_temper
    - ring_thickness
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - fastener_forming_thread_rolling
  import_risk_factors:
    - "Very small standardized spring hardware may be more practical as imported stock unless fastener production already includes retaining rings."
    - "Exact heat treatment and finish for this row are not specified."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review groups small retaining rings and other mechanical retention hardware."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely reusable as a generic small DIN 471 steel retaining ring."
assumptions:
  - "BOM quantity is 1 and row total mass is 0.0000971 kg."
  - "Steel-family material is accepted from local STEP metadata, while spring grade is inferred from DIN 471 hardware practice."
  - "The fastener bucket is used as the closest canonical hardware process bucket despite stamping-specific details."
unresolved:
  - "Exact supplier, spring steel grade, heat treatment, finish, and groove-fit tolerance are unknown."
  - "Whether to represent DIN 471 rings parametrically across sizes is deferred to merge review."
```
