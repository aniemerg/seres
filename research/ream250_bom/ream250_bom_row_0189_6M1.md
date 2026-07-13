---
row_identity:
  item: "6M1"
  cad_file: "6M1_carriage_LEFG32-S-600N"
  source_row_number: 189
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.smcpneumatics.com/LEFG32-S-600.html"
function:
  summary: "Carriage/table portion of an SMC LEFG32-S-600 support guide used as the passive top linear guide for an LEF-series slider axis; it supports overhung workpieces and aligns with the driven LEF body."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; https://content2.smcetech.com/pdf/LEF_1.pdf; research/ream250_bom/ream250_bom_row_0189_6M1__views_2x2.png"
    cited_fact_or_basis: "BOM row 189 names item 6M1, quantity 1, CAD file 6M1_carriage_LEFG32-S-600N, description 'linear guide top', and manufacturer SMC Pneumatics. Manifest row 189 maps it to a matched vendor-component STEP. The SMC LEF catalog describes LEFG as a support guide for workpieces with significant overhang, with the same dimensions as the LEF body and standard seal bands; the LEFG32-S-600 model has 600 mm stroke. The rendered CAD contact sheet shows a narrow carriage/table block with mounting holes and relieved faces. bom_url_route_check: the BOM-provided smcpneumatics.com URL was checked but returned Access Denied in this environment, so the row-matched official SMC catalog PDF was used for function and dimensional context."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The row's 'carriage' CAD split represents the moving/top carriage or table portion of the full LEFG32-S-600 support-guide product, while row 190 covers the rail."
  uncertainty_notes:
    - "The catalog describes the complete support guide, not the isolated CAD-split carriage row."
mass:
  value_kg: 0.243
  basis: "Per unit for quantity 1. FreeCAD measured one solid with volume 90126.159 mm^3, area 20527.861 mm^2, and bounding box 60.00 x 15.20 x 122.00 mm. Using aluminum density 2700 kg/m^3 from kb/materials/properties.yaml gives 90126.159 mm^3 * 1e-9 m^3/mm^3 * 2700 kg/m^3 = 0.243 kg. The SMC catalog lists the complete LEFG32-S-600 support guide as 2.68 kg, which is whole-product context and not used as the row carriage mass."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6M1_carriage_LEFG32-S-600N.step; kb/materials/properties.yaml; https://content2.smcetech.com/pdf/LEF_1.pdf"
    cited_fact_or_basis: "FreeCAD measured the row STEP as one solid with 90126.159 mm^3 volume. The local density table lists aluminum density as 2700 kg/m^3. The SMC catalog component-material table lists the LEF-family table/body aluminum-alloy parts as anodized aluminum alloy, and the LEFG32-S weight table lists the complete 600 mm support guide as 2.68 kg. bom_url_route_check: the BOM-provided smcpneumatics.com route was checked but returned Access Denied, so the row-matched official SMC catalog PDF plus local CAD volume were used."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The CAD solid volume is a suitable proxy for one physical carriage/table item."
    - "The row carriage is treated as aluminum alloy rather than including rail, seal band, bearings, or fasteners from the complete LEFG support guide."
  uncertainty_notes:
    - "The STEP material extractor returned only placeholder Generic material with density 1000.0; mass therefore depends on mapping the CAD-split carriage to the catalog aluminum-alloy table/body material."
material:
  primary_material: "anodized aluminum alloy carriage/table, with the complete LEFG support-guide family also using stainless steel dust seal/band stopper and synthetic-resin/NBR seal or bushing elements outside this CAD-split carriage."
  source:
    url_or_path: "https://content2.smcetech.com/pdf/LEF_1.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The SMC catalog component-material tables for the LEF/LEFG support-guide family list body/table-style structural parts as aluminum alloy with anodized finish, band stoppers and dust seal bands as stainless steel, and seal-band holders or bushings as synthetic resin/NBR. Local assembly STEP material extraction for 6M1_carriage_LEFG32-S-600N returned only Generic with density 1000.0, which is placeholder metadata under this task's criteria. bom_url_route_check: the BOM-provided smcpneumatics.com route was checked but returned Access Denied, so the official SMC catalog PDF was used for material family evidence."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The visible one-solid carriage/table CAD item corresponds to the aluminum-alloy table/body class in the SMC catalog rather than to the rail guide or seal-band components."
  uncertainty_notes:
    - "No row-specific material property was embedded in the STEP file; exact aluminum alloy grade is not identified."
how_to_make:
  summary: "Represent this row as a CNC-machined/anodized aluminum carriage/table component that is assembled with the rail, seal band, and guide hardware in the complete support-guide module"
  manufacturing_steps:
    - "For local manufacture of the carriage only, machine the carriage/table from aluminum-alloy bar or plate/extrusion stock to the 60.00 x 15.20 x 122.00 mm CAD envelope with mounting holes, side reliefs, and guide interfaces."
    - "Deburr, clean, and anodize the aluminum carriage; inspect mounting-hole positions and guide contact/reference faces."
    - "Assemble the carriage with the companion rail/support-guide hardware, stainless seal-band parts, and any bushing or guide elements needed for the full LEFG support guide."
  source:
    url_or_path: "https://content2.smcetech.com/pdf/LEF_1.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6M1_carriage_LEFG32-S-600N.step; research/ream250_bom/ream250_bom_row_0189_6M1__views_2x2.png"
    cited_fact_or_basis: "The SMC catalog identifies LEFG as a support guide, gives LEFG32-S-600 dimensions/weight, and lists aluminum-alloy anodized structural parts plus stainless steel seal-band components for the product family. CAD/preview show one machined carriage-like solid with mounting holes and relieved faces. The detailed machining, anodizing, inspection, and assembly sequence is inferred from geometry and catalog material stack rather than stated by SMC as a manufacturing process. targeted_web_search: searched 'SMC LEFG32-S-600 weight material', 'LEFG32-S-600 SMC linear guide datasheet mass', 'LEFG32-S-600 manufacturing process', and 'SMC LEFG support guide material table'; results found row-matched SMC catalog/distributor function, dimensions, weight, and material-family evidence but no row-specific manufacturing-process specification."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Model the carriage as a machined aluminum part and the complete guide as a later assembly, not as a monolithic casting."
  uncertainty_notes:
    - "Guide contact geometry, bearing interfaces, tolerances, surface treatment details, and any proprietary slider hardware are not fully specified by the accessible sources."
kb_implications:
  - "item_granularity: simple_part - Model row 6M1 as the reusable aluminum carriage/table part of an SMC LEFG support-guide assembly; keep the full LEFG32-S-600 as a separate purchased or assembled module if later rows combine carriage, rail, seal band, and guide hardware."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0189_6M1.md
source_research_sha256: "271913aafd6e6e02b8713febc43c6941c985e398cfe4f38604830e78f7fff10f"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed the original function, CAD-split carriage assumption, CAD-derived mass, aluminum-alloy material evidence, machining/anodizing route, and previewed mounting-hole plus guide-face geometry before conversion."
decomposition:
  decision: simple_part
  rationale: "This row is the isolated carriage/table solid from a larger support-guide assembly. Treat the carriage as one precision part now, while leaving rail, seal band, bushings, and guide hardware to related rows and later assembly staging."
  proposed_subparts: []
process_abstraction:
  original_process_family: cnc_machined_anodized_aluminum_carriage
  primary_process_bucket: general_subtractive_machining
  supporting_processes:
    - stock_preparation
    - cutting
    - precision_machining
    - drilling
    - deburring
    - surface_finishing
    - dimensional_inspection
    - assembly
  candidate_existing_processes:
    - process_id: machining_basic_v0
      fit: partial
      reason: "Covers aluminum stock removal to a carriage-like body, but does not capture guide-face tolerance and mounting-hole location control."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Relevant for guide reference faces, mounting-hole positions, and precision mechanism mating surfaces."
    - process_id: surface_treatment_anodizing_v0
      fit: supporting
      reason: "Anchors the anodized aluminum finish called out by the LEF-family material evidence."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers dimensional checks of hole pattern, guide interfaces, envelope size, and visible relieved faces."
    - process_id: assembly_basic_v0
      fit: supporting
      reason: "Relevant when this carriage is later combined with rail, seal band, bushings, and guide hardware into the complete support-guide module."
  abstraction_decision: keep_original_family
  rationale: "The source route already maps to machined and anodized aluminum carriage production. Keep the subtractive-machining family, with precision and assembly guardrails preserved for later guide-module staging."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: support and align a moving table on a passive linear guide axis
  material: anodized_aluminum_alloy
  scale_or_capacity:
    mass_kg: 0.243
    bom_quantity: 1
    row_total_mass_kg: 0.243
    scale_class: small
  geometry_form: machined_carriage_table_with_mounting_holes_and_guide_faces
merge_pool:
  eligible: true
  functional_purpose_key: linear_guidance
  precision_guardrails:
    - guide_face_tolerance
    - mounting_hole_position
    - alignment_accuracy
    - anodized_surface_condition
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - general_subtractive_machining
    - machining_precision_v0
    - surface_treatment_anodizing_v0
  import_risk_factors:
    - "Complete LEFG support-guide performance depends on rail, seal band, bushing elements, and vendor-specific guide hardware outside this CAD-split row."
    - "Guide contact geometry, tolerance class, and anodized surface specification are not fully specified by accessible evidence."
  post_merge_decision_notes: "Final import/local manufacture decision is deferred until merge review compares this with related linear guidance carriage and table parts."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely candidate for a generic small anodized aluminum linear-guide carriage if precision guardrails converge."
assumptions:
  - "BOM quantity is 1 and CAD-derived mass is 0.243 kg for the carriage/table solid."
  - "The row solid maps to the aluminum-alloy carriage/table class from the SMC catalog, not to the rail and seal-band hardware."
  - "Subtractive machining plus anodizing is sufficient as the Phase 1 closure abstraction unless later guide accuracy review blocks local manufacture."
unresolved:
  - "Exact aluminum alloy grade, guide-face tolerance, surface treatment specification, and bearing interface details remain unavailable."
  - "Merge review must decide whether this carriage can share a closure item with other small linear-guidance carriage/table parts."
```
